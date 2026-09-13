'use strict';

// image-size 2.0.2 has unpatched parser loops (GHSA-w3rx-r6r6-pgpr and
// GHSA-5p2g-fcmc-qvqq). Keep its format support, but never parse on the build
// event loop. This is containment, not a patched or renamed dependency.
const {Worker, isMainThread, parentPort, workerData} = require('node:worker_threads');
const {createRequire} = require('node:module');

if (!isMainThread && workerData?.nexusImageDimensionsWorker === true) {
  require(workerData.parser).imageSizeFromFile(workerData.file).then(
    result => parentPort.postMessage({result}),
    () => parentPort.postMessage({error: 'IMAGE_DIMENSIONS_INVALID'}),
  );
} else {
  function createBoundedReader(parser, {timeout = 2000, concurrency = 4, maxQueued = 256} = {}) {
    let active = 0;
    let closed = false;
    const queue = [];
    const workers = new Set();
    const failures = new Set();
    const error = code => Object.assign(new Error(code), {code});

    function pump() {
      while (!closed && active < concurrency && queue.length) {
        const job = queue.shift();
        active++;
        let worker;
        let timer;
        let finished = false;
        const finish = async (code, result) => {
          if (finished) return;
          finished = true;
          clearTimeout(timer);
          if (code) failures.add(code);
          // Wait for termination before freeing the slot: rejected parsers must
          // not remain alive while more workers are started.
          if (worker) {
            await worker.terminate();
            workers.delete(worker);
          }
          active--;
          if (code) job.reject(error(code));
          else job.resolve(result);
          pump();
        };
        try {
          worker = new Worker(__filename, {
            workerData: {nexusImageDimensionsWorker: true, parser, file: job.file},
            execArgv: [],
            env: {},
            resourceLimits: {maxOldGenerationSizeMb: 32, maxYoungGenerationSizeMb: 8, stackSizeMb: 4},
            stdout: true, stderr: true,
          });
          workers.add(worker);
          // Parser diagnostics are untrusted and may include local paths.
          worker.stdout.resume();
          worker.stderr.resume();
          timer = setTimeout(() => void finish('IMAGE_DIMENSIONS_TIMEOUT'), timeout);
          worker.once('message', message => void finish(message.error, message.result));
          worker.once('error', () => void finish('IMAGE_DIMENSIONS_WORKER_FAILED'));
          worker.once('exit', () => {
            if (!finished) void finish('IMAGE_DIMENSIONS_WORKER_FAILED');
          });
        } catch {
          void finish('IMAGE_DIMENSIONS_WORKER_FAILED');
        }
      }
    }

    const read = file => new Promise((resolve, reject) => {
      if (closed) return reject(error('IMAGE_DIMENSIONS_CLOSED'));
      if (queue.length >= maxQueued) {
        failures.add('IMAGE_DIMENSIONS_QUEUE_FULL');
        return reject(error('IMAGE_DIMENSIONS_QUEUE_FULL'));
      }
      queue.push({file, resolve, reject});
      pump();
    });
    read.assertHealthy = () => {
      if (failures.size) throw error(`Documentation image inspection failed: ${[...failures].sort().join(', ')}`);
    };
    read.stats = () => ({active, queued: queue.length, workers: workers.size});
    read.close = async () => {
      closed = true;
      for (const job of queue.splice(0)) job.reject(error('IMAGE_DIMENSIONS_CLOSED'));
      await Promise.all([...workers].map(worker => worker.terminate()));
    };
    return read;
  }

  let installed;
  function install() {
    // Resolve from the real MDX loader, not a possibly different top-level copy.
    const fromMdx = createRequire(require.resolve('@docusaurus/mdx-loader'));
    const parser = fromMdx.resolve('image-size/fromFile');
    const exports = fromMdx('image-size/fromFile');
    if (installed) {
      if (exports.imageSizeFromFile !== installed) throw new Error('Image inspection guard was replaced');
      return installed;
    }
    if (typeof exports.imageSizeFromFile !== 'function' ||
        !Object.getOwnPropertyDescriptor(exports, 'imageSizeFromFile')?.writable) {
      throw new Error('Unsupported MDX image inspection contract');
    }
    installed = createBoundedReader(parser);
    exports.imageSizeFromFile = installed;
    return installed;
  }

  module.exports = function imageDimensionsGuard() {
    const reader = install();
    return {
      name: 'nexus-bounded-image-dimensions',
      // MDX catches individual image-size errors. Do not let it silently publish
      // an apparently successful build after a timeout, OOM or malformed image.
      postBuild() { reader.assertHealthy(); },
    };
  };
  module.exports.createBoundedReader = createBoundedReader;
  module.exports.install = install;
}
