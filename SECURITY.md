# Security

Never include credentials, private keys, pairing links or personal data in public issues. For sensitive reports, use GitHub private vulnerability reporting if enabled; otherwise ask a maintainer for a private channel without disclosing the issue details.

## Dependency review — 2026-10-17

The lockfile updates patched image-size (2.0.4), http-cache-semantics (4.3.0),
compression, proxy-addr, shell-quote, joi and source-map-js. Explicit overrides
select tinypool 2.1.2, KaTeX 0.18.2 and postcss-selector-parser 7.1.6 where parent
ranges otherwise retain vulnerable versions. Worker builds, formula rendering,
CSS minification and both documentation locales are covered by build checks.

The current npm audit has **no critical, moderate or low findings**, but still
reports **30 high affected dependency nodes** rooted in the single unpatched
braces advisory: https://github.com/advisories/GHSA-vfj7-8cjw-p6xm . These are
transitive effects, not 30 distinct vulnerabilities or a clean audit.

Existing containment for braces@3.0.3 remains unchanged: official npm entrypoints
and their descendants reject excessive opening tokens before parsing and bound
AST depth/node counts, including malformed or cyclic trees. It bounds recursive
walkers, not every possible glob expansion cost. Rejected inputs stop the build.

Image parsing remains in workers with deadline, queue and heap limits even after
the upstream fixes. Regression tests require malformed ICNS/HEIF/JXL to be
rejected promptly, plus a separate stalled-parser test verifies worker cleanup
and event-loop responsiveness. HTTP cache reuse and update checks remain disabled
as defense in depth with the patched cache library.

Use the documented npm scripts, not direct `npx docusaurus` commands. Guards
validate installed versions against the lockfile. `check:audit` rejects unknown
advisories, any critical finding, version drift and failed containment tests.
The old exceptions for image-size and http-cache-semantics were removed; the
remaining braces exception was not expanded. Do not expose the development
server as a production service. Re-audit before each publication.

The website is static. CI has read-only permissions by default, uses pinned Actions, and does not deploy pull request code. Pages deployment is a separate manual workflow on the default branch. Do not add pull_request_target workflows that execute untrusted code with secrets.
