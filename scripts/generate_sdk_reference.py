"""Generate current bilingual SDK signatures from AST without importing runtime code.

Historical version documents are intentionally left unchanged.
"""
import ast
from pathlib import Path
import os

SITE = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ.get('NEXUS_SDK_SOURCE', 'sdk-source/src')) / 'nexus_agent'
ROOTS = [SITE / 'docs-sdk', SITE / 'i18n/en/docusaurus-plugin-content-docs-sdk/current']
SELECT = {
    'agent': {'NexusAgent': ['__init__', 'capability', 'stream_capability', 'start', 'run', 'as_mcp_server', 'invoke', 'invoke_stream', 'public_ipv6']},
    'client': {'NexusAgentClient': ['__init__', 'register', 'invoke_intent', 'invoke_stream'], 'AgentLease': ['renew', 'close']},
    'server': {'NexusAgentServer': ['__init__', 'handler', 'stream_handler', 'serve_forever', 'serve_in_thread', 'serve_registered', 'shutdown', 'server_close']},
    'direct_ipv6': {'DirectIPv6Agent': ['__init__', 'plain_http', 'invoke', 'invoke_stream']},
    'public_ipv6_agent': {'PublicIPv6Agent': ['__init__', 'start', 'run']},
    'computer_runtime': {'NexusComputerRuntime': ['setup', 'status', 'run', 'close']},
}

def main():
    init = ast.parse((SOURCE / '__init__.py').read_text(encoding='utf-8'))
    exports = next(ast.literal_eval(n.value) for n in init.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == '__all__' for t in n.targets))
    origins = {alias.asname or alias.name: n.module for n in init.body if isinstance(n, ast.ImportFrom) for alias in n.names}
    chunks = []
    for module, classes in SELECT.items():
        tree = ast.parse((SOURCE / f'{module}.py').read_text(encoding='utf-8'))
        for name, methods in classes.items():
            cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
            lines = []
            for method in methods:
                node = next((n for n in cls.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == method), None)
                if node is None:
                    continue  # Inherited methods are documented on their defining class.
                returns = f' -> {ast.unparse(node.returns)}' if node.returns else ''
                lines.append(f'def {name}.{method}({ast.unparse(node.args)}){returns}: ...')
            chunks.append(f'## `{name}`\n\n[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/{module}.py)\n\n```text\n' + '\n\n'.join(lines) + '\n```\n')
    for i, root in enumerate(ROOTS):
        title = '核心类与方法' if i == 0 else 'Core classes and methods'
        intro = ('以下签名从当前 SDK 源码静态生成，包含 hosted、资源声明与 Computer Runtime。默认值与类型以当前源码为准；发布 wheel 可能落后于 main。阅读流程说明：[运行模式](../concepts/runtime-model.md)、[Computer Runtime](../guides/computer-runtime.md)。' if i == 0 else 'These signatures are generated statically from current SDK source, including hosted mode, resource declarations and Computer Runtime. Release wheels can lag behind main. For usage, see [runtime modes](../concepts/runtime-model.md) and [Computer Runtime](../guides/computer-runtime.md).')
        (root / 'reference/core-methods.md').write_text(f'---\nsidebar_position: 1\ntitle: {title}\n---\n\n# {title}\n\n{intro}\n\n'+'\n'.join(chunks),encoding='utf-8')
        page = root / 'reference/api.md'
        text = page.read_text(encoding='utf-8').split('\n## Current source export index')[0]
        text += '\n## Current source export index\n\n' + '\n'.join(f'- `{name}` — [`nexus_agent.{origins.get(name, "__init__")}`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/{origins.get(name, "__init__")}.py)' for name in sorted(exports)) + '\n'
        page.write_text(text,encoding='utf-8')
    print(f'Generated current signatures and {len(exports)} exports for both locales.')

if __name__ == '__main__':
    main()
