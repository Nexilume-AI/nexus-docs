import {spawnSync} from 'node:child_process';
import {readFileSync} from 'node:fs';
import {resolve} from 'node:path';
const child = spawnSync(process.execPath, [resolve('node_modules/@docusaurus/core/bin/docusaurus.mjs'), 'build'], {
  stdio: 'inherit', env: {...process.env, NO_UPDATE_NOTIFIER: '1'}
});
if (child.error) throw child.error;
if (child.status !== 0) process.exit(child.status || 1);
for (const locale of ['', 'en/']) {
  const body = readFileSync(resolve('build', locale, 'index.html'), 'utf8');
  for (const product of ['server', 'tokenbank', 'openwrt', 'sdk']) {
    if (!body.includes(`/${product}`)) throw new Error(`Missing ${locale}${product}`);
  }
}
console.log('All four products and both locales built successfully.');
