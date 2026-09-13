import assert from 'node:assert/strict';
import {test} from 'node:test';
import {createRequire} from 'node:module';
import {mkdtempSync, writeFileSync, unlinkSync, rmdirSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {spawn} from 'node:child_process';
import {Worker} from 'node:worker_threads';
import {once} from 'node:events';
import guard from './image-dimensions.cjs';

const require = createRequire(import.meta.url);
const fromMdx = createRequire(require.resolve('@docusaurus/mdx-loader'));
const parser = fromMdx.resolve('image-size/fromFile');
test('loading the plugin in an unrelated build Worker does not enter parser mode', async () => {
  const worker = new Worker(new URL('./image-dimensions.cjs', import.meta.url), {execArgv: []});
  const [code] = await once(worker, 'exit');
  assert.equal(code, 0);
});
function fixture(t, data, name = 'image.png') {
  const directory = mkdtempSync(join(tmpdir(), 'nexus-image-guard-'));
  const file = join(directory, name);
  writeFileSync(file, data);
  t.after(() => { unlinkSync(file); rmdirSync(directory); });
  return file;
}
const icns = Buffer.from('69636e73000000106973333200000000', 'hex');
const heif = Buffer.from('00000010667479706176696600000000000000246d657461000000000000000869707270000000146970636f000000006973706500000000000000000000000000000000', 'hex');
const jxl = Buffer.from('0000000c4a584c200d0a870a00000010667479706a786c2000000000000000006a786c7000000000', 'hex');

function reproduce(file) {
  return new Promise((resolve, reject) => {
    // Start the parser deadline after a real child readiness handshake, not
    // before Windows has scheduled Node during a concurrent npm/build workload.
    const child = spawn(process.execPath, ['--max-old-space-size=64', '-e',
      'const parser=require(process.argv[1]); process.stdin.once("data",()=>parser.imageSizeFromFile(process.argv[2]).then(()=>process.exit(0),()=>process.exit(2))); process.stdout.write("parser-ready\\n")',
      parser, file], {stdio: ['pipe', 'pipe', 'pipe']});
    let ready = false;
    let expired = false;
    let startupFailed = false;
    let output = '';
    let timer = setTimeout(() => { startupFailed = true; child.kill(); }, 10_000);
    child.stderr.resume();
    child.stdin.on('error', () => {}); // Child may OOM immediately after dispatch.
    child.stdout.on('data', data => {
      output = (output + data.toString()).slice(-100);
      if (!ready && output.includes('parser-ready')) {
        ready = true;
        clearTimeout(timer);
        timer = setTimeout(() => { expired = true; child.kill(); }, 1500);
        child.stdin.end('parse');
      }
    });
    child.once('error', error => { clearTimeout(timer); reject(error); });
    child.once('close', (status, signal) => {
      clearTimeout(timer);
      resolve({ready, expired, startupFailed, status, signal});
    });
  });
}

for (const [name, data] of Object.entries({icns, heif, jxl})) {
  test(`${name}: actual upstream parser cannot complete the malformed fixture`, async t => {
    const file = fixture(t, data); // Deliberately misleading extension.
    const result = await reproduce(file);
    assert.equal(result.startupFailed, false, 'Startup delays are not parser vulnerability evidence');
    assert.equal(result.ready, true);
    assert.ok(result.expired || result.signal || result.status === 134,
      `Expected bounded reproduction of hang/OOM, got ${result.status}`);
  });

  test(`${name}: isolation bounds the parser, cleans workers and fails the build`, async t => {
    const reader = guard.createBoundedReader(parser, {timeout: 500, concurrency: 1});
    t.after(() => reader.close());
    const file = fixture(t, data);
    let ticks = 0;
    const interval = setInterval(() => ticks++, 10);
    t.after(() => clearInterval(interval));
    await assert.rejects(reader(file), /IMAGE_DIMENSIONS_(TIMEOUT|WORKER_FAILED)/);
    assert.ok(ticks > 2, 'Build event loop must remain responsive');
    assert.deepEqual(reader.stats(), {active: 0, queued: 0, workers: 0});
    assert.throws(() => reader.assertHealthy(), /Documentation image inspection failed/);
  });
}

test('valid SVG, PNG, GIF and ICNS retain dimensions and async API', async t => {
  const reader = guard.createBoundedReader(parser);
  t.after(() => reader.close());
  const inputs = [
    [Buffer.from('<svg xmlns="http://www.w3.org/2000/svg" width="37" height="19"></svg>'), 37, 19],
    [Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScLttAAAAABJRU5ErkJggg==', 'base64'), 1, 1],
    [Buffer.from('47494638396102000300000000', 'hex'), 2, 3],
    [Buffer.from('69636e73000000106973333200000008', 'hex'), 16, 16],
  ];
  const results = await Promise.all(inputs.map(([data]) => reader(fixture(t, data))));
  results.forEach((result, i) => assert.deepEqual([result.width, result.height], inputs[i].slice(1)));
  assert.deepEqual(reader.stats(), {active: 0, queued: 0, workers: 0});
  reader.assertHealthy();
});

test('bounded queue rejects overload and survives a malformed file', async t => {
  const reader = guard.createBoundedReader(parser, {timeout: 500, concurrency: 1, maxQueued: 1});
  t.after(() => reader.close());
  const bad = reader(fixture(t, icns)).catch(error => error);
  const good = fixture(t, '<svg width="7" height="8"></svg>');
  const pending = reader(good);
  await assert.rejects(reader(good), /IMAGE_DIMENSIONS_QUEUE_FULL/);
  assert.equal(reader.stats().active, 1);
  assert.equal(reader.stats().queued, 1);
  assert.match((await bad).code, /TIMEOUT|WORKER_FAILED/);
  assert.equal((await pending).width, 7);
  assert.deepEqual(reader.stats(), {active: 0, queued: 0, workers: 0});
});

test('MDX uses the installed reader even if its transformer was imported first', async t => {
  // Docusaurus captures the exports object before loading some site plugins.
  const transform = require('@docusaurus/mdx-loader/lib/remark/transformImage/index.js').default;
  const captured = fromMdx('image-size/fromFile');
  const original = captured.imageSizeFromFile;
  const plugin = guard();
  assert.notEqual(captured.imageSizeFromFile, original);
  assert.equal(guard.install(), captured.imageSizeFromFile);
  const file = fixture(t, '<svg width="11" height="12"></svg>');
  assert.equal((await captured.imageSizeFromFile(file)).width, 11);
  const {dirname, basename} = await import('node:path');
  const processImage = transform({siteDir: dirname(file), staticDirs: [], onBrokenMarkdownImages: 'throw'});
  const root = {type: 'root', children: [{type: 'image', url: `./${basename(file)}`, alt: 'fixture'}]};
  await processImage(root, {path: join(dirname(file), 'page.md'), data: {compilerName: 'server'}});
  assert.equal(root.children[0].type, 'mdxJsxTextElement');
  assert.equal(root.children[0].attributes.find(item => item.name === 'width').value, '11');
  plugin.postBuild();
  await assert.rejects(captured.imageSizeFromFile(fixture(t, 'not an image')), /IMAGE_DIMENSIONS_INVALID/);
  assert.throws(() => plugin.postBuild(), /IMAGE_DIMENSIONS_INVALID/);
});
