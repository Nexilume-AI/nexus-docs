# Security

Never include credentials, private keys, pairing links or personal data in public issues. For sensitive reports, use GitHub private vulnerability reporting if enabled; otherwise ask a maintainer for a private channel without disclosing the issue details.

## Known build dependency risk

The 2026-10-03 lockfile audit reports 37 high-severity affected dependency nodes rooted in four advisories. These are not 37 independent defects. No patched upstream versions were published at review time:

- https://github.com/advisories/GHSA-w3rx-r6r6-pgpr
- https://github.com/advisories/GHSA-5p2g-fcmc-qvqq
- https://github.com/advisories/GHSA-vfj7-8cjw-p6xm
- https://github.com/advisories/GHSA-ch52-4w7c-c8xp

The advisories list no patched version. `scripts/image-dimensions.cjs` isolates the actual MDX image parser in bounded workers with timeout, queue and heap limits; malformed parser inputs fail the build. `npm run check:security` exercises malformed ICNS/HEIF/JXL and valid files. This mitigates the website build path; it does not patch image-size for arbitrary callers. Audit warnings are retained, not suppressed. Re-audit before publishing and after dependency changes.

`scripts/dependency-guards.cjs` contains the other two risks in official npm
start/build/serve entrypoints and their Node descendants:

- `braces@3.0.3`, via glob/watch dependencies: reject more than 100 opening
  brace/parenthesis tokens before parsing (conservatively including literals).
  Direct AST walkers also enforce depth and node budgets, including malformed
  or cyclic trees. Rejected inputs stop the build; ordinary glob matching stays
  available. This bounds the unpatched recursive walkers, not all possible glob
  expansion costs.
- `http-cache-semantics@4.2.0`, via Docusaurus update-notifier → latest-version →
  package-json → got → cacheable-request: disable update checks and unnecessary
  HTTP cache storage/reuse, including max-stale and stale-on-error paths. The
  deployed Pages site contains no Node HTTP cache or shared response server.

Use the documented npm scripts, not direct `npx docusaurus` commands which skip
these guards. Guards validate the lockfile and installed versions and do not
edit node_modules. Version changes require review. `check:audit` retains the
full npm vulnerability counts, rejects unknown/critical advisories and version
drift, and requires the containment regression suite to pass. Maintainer-approved
containment is **not** a clean audit or an upstream vulnerability fix. Revisit
these controls when fixed versions become available. Do not expose the local
development server as a production service.

The website is static. CI has read-only permissions by default, uses pinned Actions, and does not deploy pull request code. Pages deployment is a separate manual workflow on the default branch. Do not add pull_request_target workflows that execute untrusted code with secrets.
