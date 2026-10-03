import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {runInNewContext} from 'node:vm';
import {test} from 'node:test';
import {spawnSync} from 'node:child_process';
import {readFileSync} from 'node:fs';

const require = createRequire(import.meta.url);
const from = parent => createRequire(require.resolve(parent));

for (const parent of ['copy-webpack-plugin', 'css-minimizer-webpack-plugin']) {
  test(`${parent} retains its real serialization contract with the security update`, () => {
    const serialize = from(parent)('serialize-javascript');
    // Fixed local fixture only: never evaluate source/content from a user.
    const value = {html: '</script><script>fixture</script>', expression: /abc/gi,
      operation: function increment(n) { return n + 1; }};
    const serialized = serialize(value);
    assert.ok(!serialized.includes('</script>'));
    const decoded = runInNewContext(`(${serialized})`, {}, {timeout: 1000});
    assert.equal(decoded.html, value.html);
    assert.equal(decoded.expression.source, 'abc');
    assert.equal(decoded.operation(3), 4);
  });
  test(`${parent} does not emit script-closing text from function bodies`, () => {
    const serialize = from(parent)('serialize-javascript');
    const serialized = serialize({value: function () { return '</script>'; }});
    assert.ok(!serialized.toLowerCase().includes('</script>'));
    const decoded = runInNewContext(`(${serialized})`, {}, {timeout: 1000});
    assert.equal(decoded.value(), '</script>');
  });
}

test('Express query parser preserves nesting without prototype pollution', () => {
  const qs = from('express')('qs');
  assert.equal(qs.parse('a[b]=c').a.b, 'c');
  qs.parse('__proto__[nexus_polluted]=yes&constructor[prototype][nexus_polluted]=yes');
  assert.equal({}.nexus_polluted, undefined);
  assert.equal(qs.parse(qs.stringify({a: {b: 'c'}})).a.b, 'c');
});

test('SockJS retains the CommonJS UUID v4 contract', () => {
  const uuid = from('sockjs')('uuid');
  const value = uuid.v4();
  assert.equal(uuid.validate(value), true);
  assert.equal(uuid.version(value), 4);
  const output = Buffer.alloc(16);
  assert.equal(uuid.v4(undefined, output, 0), output);
  assert.equal(uuid.validate(uuid.stringify(output)), true);
});

function probe(source) {
  const child = spawnSync(process.execPath, ['-e', source], {
    encoding: 'utf8', timeout: 10000,
  });
  assert.equal(child.error, undefined);
  assert.equal(child.status, 0, child.stderr || child.stdout);
  return child.stdout.trim();
}

test('deep brace patterns are rejected before recursive walkers, including child processes', () => {
  probe(`
    const assert = require('node:assert/strict');
    const braces = require('braces');
    const pattern = '{'.repeat(4500) + 'a,b' + '}'.repeat(4500);
    for (const method of ['parse', 'compile', 'expand', 'stringify']) {
      assert.throws(() => braces[method](pattern), {code: 'DOCS_PATTERN_COMPLEXITY_LIMIT'});
    }
    assert.deepEqual(braces.expand('docs/{en,zh}/{a,b}.md'),
      ['docs/en/a.md', 'docs/en/b.md', 'docs/zh/a.md', 'docs/zh/b.md']);
  `);
});

test('direct brace walker imports reject deep or cyclic ASTs', () => {
  probe(`
    const assert = require('node:assert/strict');
    let tree = {type: 'text', value: 'ok'};
    for (let i = 0; i < 150; i++) tree = {type: 'brace', nodes: [tree]};
    for (const method of ['compile', 'expand', 'stringify']) {
      const walk = require('braces/lib/' + method);
      assert.throws(() => walk(tree), {code: 'DOCS_PATTERN_COMPLEXITY_LIMIT'});
      const cycle = {type: 'brace', nodes: []}; cycle.nodes.push(cycle);
      assert.throws(() => walk(cycle), {code: 'DOCS_PATTERN_COMPLEXITY_LIMIT'});
    }
  `);
});

test('build dependency cache never serves max-stale cookies or proxy-revalidate responses', () => {
  probe(`
    const assert = require('node:assert/strict');
    const Policy = require('http-cache-semantics');
    const req = {url: 'https://example.invalid/package', method: 'GET', headers: {host: 'example.invalid'}};
    const stale = {...req, headers: {...req.headers, 'cache-control': 'max-stale=999999'}};
    for (const headers of [
      {'cache-control': 'max-age=600', 'set-cookie': 'fixture=private'},
      {'cache-control': 'proxy-revalidate, max-age=600'},
      {'cache-control': 'no-cache, stale-while-revalidate=600'},
      {'cache-control': 'public, max-age=600'},
    ]) {
      const policy = new Policy(req, {status: 200, headers}, {shared: true});
      assert.equal(policy.storable(), false);
      assert.equal(policy.satisfiesWithoutRevalidation(stale), false);
      assert.equal(policy.evaluateRequest(stale).response, undefined);
      assert.equal(policy.evaluateRequest(stale).revalidation.synchronous, true);
      const restored = Policy.fromObject(policy.toObject());
      assert.equal(restored.satisfiesWithoutRevalidation(stale), false);
    }
  `);
});

test('official docs entrypoints and their descendants load the guard', () => {
  const {scripts} = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));
  for (const name of ['start', 'start:en', 'build', 'serve', 'check:security']) {
    assert.match(scripts[name], /^node --require \.\/scripts\/dependency-guards\.cjs /);
  }
  assert.equal(probe(`console.log(process.env.NO_UPDATE_NOTIFIER)`), '1');
});

test('audit review rejects unknown advisories, critical severity and version drift', () => {
  const source = `
import copy
import sys
sys.path.insert(0, 'scripts')
from check_dependency_audit import review_findings
url = 'https://github.com/advisories/GHSA-vfj7-8cjw-p6xm'
data = {'vulnerabilities': {'braces': {'severity': 'high', 'nodes': ['node_modules/braces'], 'via': [{'url': url}]}}}
lock = {'packages': {'node_modules/braces': {'version': '3.0.3'}}}
assert not review_findings(data, lock)
unknown = copy.deepcopy(data)
unknown['vulnerabilities']['braces']['via'][0]['url'] = 'https://example.invalid/new-advisory'
assert review_findings(unknown, lock)
critical = copy.deepcopy(data)
critical['vulnerabilities']['braces']['severity'] = 'critical'
assert review_findings(critical, lock)
lock['packages']['node_modules/braces']['version'] = '0.0.0'
assert review_findings(data, lock)
`;
  const child = spawnSync(process.env.PYTHON || 'python', ['-B', '-c', source], {
    encoding: 'utf8', timeout: 10000,
  });
  assert.equal(child.error, undefined);
  assert.equal(child.status, 0, child.stderr);
});

test('audit fails closed when the registry or containment tests fail', () => {
  const child = spawnSync(process.env.PYTHON || 'python', ['-B', '-c', `
import json
import sys
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0, 'scripts')
import check_dependency_audit as audit
clean = json.dumps({'vulnerabilities': {}, 'metadata': {'vulnerabilities': {}}})
for result in [SimpleNamespace(returncode=2, stdout=clean), SimpleNamespace(returncode=0, stdout='not JSON')]:
    with patch.object(audit.subprocess, 'run', return_value=result):
        try:
            audit.main()
        except SystemExit as error:
            assert 'unavailable' in str(error)
        else:
            raise AssertionError('Registry failure accepted')
with patch.object(audit.subprocess, 'run', side_effect=[SimpleNamespace(returncode=0, stdout=clean), SimpleNamespace(returncode=1)]) as run:
    try:
        audit.main()
    except SystemExit as error:
        assert 'containment verification failed' in str(error)
    else:
        raise AssertionError('Failed guards accepted')
    assert run.call_count == 2
`], {encoding: 'utf8', timeout: 10000});
  assert.equal(child.error, undefined);
  assert.equal(child.status, 0, child.stderr);
});
