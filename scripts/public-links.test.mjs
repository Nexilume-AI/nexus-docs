import assert from 'node:assert/strict';
import {test} from 'node:test';
import {assertPublicRepositoryLinks} from './public-links.mjs';

test('official repository URLs and third-party dependencies remain valid', () => {
  assert.doesNotThrow(() => assertPublicRepositoryLinks(
    'https://github.com/Nexilume-AI/nexus-docs https://github.com/facebook/docusaurus'));
});

test('personal product links are rejected without embedding a real old identity', () => {
  for (const suffix of ['', '/blob/main/README.md', '#readme', '?tab=readme']) {
    assert.throws(() => assertPublicRepositoryLinks(
      `https://github.com/personal-owner/nexus-docs${suffix}`), /Unexpected public repository owner/);
  }
});
