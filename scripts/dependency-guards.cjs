'use strict';

// Build-only containment for unpatched upstream advisories. Never rename or
// modify installed packages to hide their versions from npm audit.
const {readFileSync} = require('node:fs');
const {resolve} = require('node:path');
const root = resolve(__dirname, '..');
const lock = JSON.parse(readFileSync(resolve(root, 'package-lock.json'), 'utf8'));
const expected = {'braces': '3.0.3', 'http-cache-semantics': '4.2.0'};
const found = new Set();
const fail = () => {
  throw Object.assign(new Error('Documentation glob pattern is too complex'), {
    code: 'DOCS_PATTERN_COMPLEXITY_LIMIT',
  });
};

function checkPattern(input) {
  if (typeof input !== 'string') return;
  if (input.length > 10000) fail();
  // Count opening tokens conservatively (including literals): this also bounds
  // nesting inside malformed/escaped patterns before parse calls stringify.
  let openings = 0;
  for (const char of input) {
    if ((char === '{' || char === '(') && ++openings > 100) fail();
  }
}

function checkTree(ast) {
  const pending = [[ast, 0]];
  let visited = 0;
  while (pending.length) {
    const [node, depth] = pending.pop();
    if (++visited > 10000 || depth > 100) fail();
    if (Array.isArray(node?.nodes)) {
      if (node.nodes.length > 10000) fail();
      for (const child of node.nodes) pending.push([child, depth + 1]);
    }
  }
}

for (const [relative, metadata] of Object.entries(lock.packages)) {
  const name = relative.match(/(?:^|\/)node_modules\/(braces|http-cache-semantics)$/)?.[1];
  if (!name) continue;
  if (metadata.version !== expected[name]) throw new Error(`Review dependency guard for ${name}`);
  const directory = resolve(root, relative);
  const installed = JSON.parse(readFileSync(resolve(directory, 'package.json'), 'utf8'));
  if (installed.version !== metadata.version) throw new Error(`Dependency/lock mismatch: ${name}`);
  found.add(name);
  if (name === 'braces') {
    // Install leaves first so parse/expand retain guarded internal references.
    for (const entry of ['stringify', 'compile', 'expand', 'parse']) {
      const file = require.resolve(resolve(directory, 'lib', `${entry}.js`));
      const original = require(file);
      require.cache[file].exports = function guarded(input, ...args) {
        if (entry === 'parse') checkPattern(input);
        else checkTree(input);
        return original(input, ...args);
      };
    }
  } else {
    const Policy = require(directory);
    // Docs do not need an HTTP response cache. Disable storage and all read
    // paths, including restored entries; request a fresh origin response.
    Policy.prototype.storable = () => false;
    Policy.prototype.satisfiesWithoutRevalidation = () => false;
    Policy.prototype.useStaleWhileRevalidate = () => false;
    Policy.prototype._useStaleIfError = () => false;
    Policy.prototype.evaluateRequest = function evaluateRequest(request) {
      return this._evaluateRequestMissResult(request);
    };
  }
}
if (found.size !== Object.keys(expected).length) throw new Error('Review changed dependency guard targets');
process.env.NO_UPDATE_NOTIFIER = '1';
// Docusaurus build spawns subprocesses/workers. Keep the same protections in
// descendants, with an absolute quoted path that also works on Windows.
const preload = `--require=${JSON.stringify(__filename.replaceAll('\\', '/'))}`;
if (!(process.env.NODE_OPTIONS || '').includes(preload)) {
  process.env.NODE_OPTIONS = `${process.env.NODE_OPTIONS || ''} ${preload}`.trim();
}
