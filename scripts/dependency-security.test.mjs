import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {runInNewContext} from 'node:vm';
import {test} from 'node:test';

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
