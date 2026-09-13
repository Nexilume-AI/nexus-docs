"""Render public definitions and reachable Run context helpers; --check detects drift.

Uses AST only, so optional integrations do not need to be installed. The public
surface is top-level exports, public definitions in their modules plus FastMCP,
A2A, files and inbox, and helper objects constructed by NexusRunContext.
"""
import ast
import html
import json
from pathlib import Path
import os
import sys

SITE = Path(__file__).resolve().parents[1]
SRC = Path(os.environ.get('NEXUS_SDK_SOURCE', 'sdk-source/src')) / 'nexus_agent'
ROOTS = [SITE/'docs-sdk', SITE/'i18n/en/docusaurus-plugin-content-docs-sdk/current']

def main():
    trees = {p.stem: ast.parse(p.read_text(encoding='utf-8')) for p in SRC.glob('*.py')}
    init = trees['__init__']
    exports = next(ast.literal_eval(n.value) for n in init.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == '__all__' for t in n.targets))
    origins = {a.asname or a.name: n.module for n in init.body if isinstance(n, ast.ImportFrom) for a in n.names}
    modules = sorted({origins[x] for x in exports} | {'fastmcp', 'a2a', 'files', 'inbox'})
    classes = {n.name: (mod, n) for mod in modules for n in trees[mod].body if isinstance(n, ast.ClassDef)}
    aliases = {'NexusRunContext': 'ctx'}
    queue = ['NexusRunContext']
    while queue:
        name = queue.pop(0)
        for node in ast.walk(classes[name][1]):
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call) or not isinstance(node.value.func, ast.Name):
                continue
            child = node.value.func.id
            if child not in classes or child in aliases:
                continue
            for target in node.targets:
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self' and not target.attr.startswith('_'):
                    aliases[child] = aliases[name]+'.'+target.attr
                    queue.append(child)
    records = []
    pages = {}
    def sig(node):
        args = ast.unparse(node.args)
        returns = ast.unparse(node.returns) if node.returns else 'not annotated; see contract/source'
        return args, returns
    def method(node, owner, module, prefix=''):
        key = f'{module}.{owner+"." if owner else ""}{node.name}'
        records.append(key)
        args, returns = sig(node)
        async_ = 'async ' if isinstance(node, ast.AsyncFunctionDef) else ''
        name = prefix+'.'+node.name if prefix else (owner+'.' if owner else '')+node.name
        prop = any(ast.unparse(d) == 'property' for d in node.decorator_list)
        display = f'{name}: {returns}' if prop else f'{async_}{name}({args}) -> {returns}'
        result = f'### `{name}`\n\n```text\n{display}\n```\n\n'
        doc = ast.get_docstring(node)
        if doc:
            result += html.escape(doc).replace('{', '&#123;').replace('}', '&#125;')+'\n\n'
        params = node.args.posonlyargs + node.args.args + node.args.kwonlyargs
        defaults = [None]*(len(node.args.posonlyargs+node.args.args)-len(node.args.defaults))+node.args.defaults+node.args.kw_defaults
        rows=[]
        for param,default in zip(params,defaults):
            if param.arg in ('self','cls') or param.arg.startswith('_'):continue
            typ=ast.unparse(param.annotation) if param.annotation else 'not annotated'
            val=ast.unparse(default) if default is not None else 'required'
            rows.append(f'| `{param.arg}` | `{typ.replace("|", "&#124;")}` | `{val.replace("|", "&#124;")}` |')
        if rows:result+='| Parameter | Type | Default |\n| --- | --- | --- |\n'+'\n'.join(rows)+'\n\n'
        raised=sorted({ast.unparse(n.exc.func if isinstance(n.exc,ast.Call) else n.exc) for n in ast.walk(node) if isinstance(n,ast.Raise) and n.exc is not None})
        if raised:result+='Direct raises (not exhaustive): '+', '.join('`'+x+'`' for x in raised)+'.\n\n'
        result+=f'[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/{module}.py#L{node.lineno})\n\n'
        return result
    for mod in modules:
        chunks=[]
        for node in trees[mod].body:
            if isinstance(node, (ast.FunctionDef,ast.AsyncFunctionDef)) and not node.name.startswith('_'):
                chunks.append(method(node,'',mod))
            if not isinstance(node,ast.ClassDef) or (node.name.startswith('_') and node.name not in aliases):continue
            key=f'{mod}.{node.name}';records.append(key)
            label=aliases.get(node.name,node.name)
            body=f'## `{label}`\n\n'
            if node.name.startswith('_'):body+=f'Access through `{label}`; do not import the implementation class.\n\n'
            if node.bases:body+='Bases: '+', '.join('`'+ast.unparse(x)+'`' for x in node.bases)+'. Inherited behavior is defined on the base class.\n\n'
            doc=ast.get_docstring(node)
            if doc:body+=html.escape(doc).replace('{', '&#123;').replace('}', '&#125;')+'\n\n'
            fields=[n for n in node.body if isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and not n.target.id.startswith('_')]
            if fields:
                body+='| Field | Type | Default |\n| --- | --- | --- |\n'
                for field in fields:
                    records.append(key+'.'+field.target.id)
                    val=ast.unparse(field.value) if field.value is not None else 'required'
                    body+=f'| `{field.target.id}` | `{ast.unparse(field.annotation).replace("|", "&#124;")}` | `{val.replace("|", "&#124;")}` |\n'
                body+='\n'
            for child in node.body:
                if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef)) and (not child.name.startswith('_') or child.name=='__init__'):
                    body+=method(child,node.name,mod,aliases.get(node.name,''))
            chunks.append(body)
        pages[mod]='\n'.join(chunks)
    changed=[]
    def save(path,body):
        if '--check' in sys.argv:
            if not path.exists() or path.read_text(encoding='utf-8')!=body:changed.append(str(path))
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body,encoding='utf-8')
    for index,root in enumerate(ROOTS):
        for mod,body in pages.items():
            intro=('本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。' if index==0 else 'Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.')
            save(root/f'reference/modules/{mod}.md',f'---\ntitle: "{mod} API"\n---\n\n# {mod} API\n\n{intro}\n\n{body}')
        save(root/'reference/modules/_category_.json',json.dumps({'label':'完整接口参考' if index==0 else 'Detailed API reference','position':10},ensure_ascii=False,indent=2)+'\n')
        title='接口覆盖范围' if index==0 else 'API coverage'
        intro=('覆盖顶层导出所属模块、FastMCP/A2A/Files/Inbox 的公开定义，以及 RunContext 构造的辅助对象。不是对全部网络功能的验收声明。' if index==0 else 'Covers defining modules of top-level exports, public FastMCP/A2A/Files/Inbox definitions and helpers constructed by RunContext. This is documentation coverage, not certification of all network features.')
        save(root/'reference/coverage.md',f'---\ntitle: {title}\nsidebar_position: 3\n---\n\n# {title}\n\n{intro}\n\n'+f'{len(exports)} top-level exports; {len(set(records))} class/function/method/field entries across {len(modules)} modules.\n\n'+'\n'.join(f'- [{mod}](modules/{mod}.md)' for mod in modules)+'\n\n`python scripts/generate_sdk_details.py --check` checks exact generated content against current source.\n')
    if changed:raise SystemExit('Stale generated docs:\n'+'\n'.join(changed))
    print(f'Detailed API coverage: {len(exports)} exports, {len(set(records))} entries, {len(modules)} modules; '+('verified' if '--check' in sys.argv else 'generated'))

if __name__=='__main__':main()
