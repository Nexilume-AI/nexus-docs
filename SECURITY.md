# Security

Never include credentials, private keys, pairing links or personal data in public issues. For sensitive reports, use GitHub private vulnerability reporting if enabled; otherwise ask a maintainer for a private channel without disclosing the issue details.

## Known build dependency risk

The 2026-09-13 lockfile audit reports 19 high-severity affected dependency nodes, all rooted in two image-size parser advisories. These are not 19 independent defects:

- https://github.com/advisories/GHSA-w3rx-r6r6-pgpr
- https://github.com/advisories/GHSA-5p2g-fcmc-qvqq

The advisories list no patched version. `scripts/image-dimensions.cjs` isolates the actual MDX image parser in bounded workers with timeout, queue and heap limits; malformed parser inputs fail the build. `npm run check:security` exercises malformed ICNS/HEIF/JXL and valid files. This mitigates the website build path; it does not patch image-size for arbitrary callers. Audit warnings are retained, not suppressed. Re-audit before publishing and after dependency changes.

The website is static. CI has read-only permissions by default, uses pinned Actions, and does not deploy pull request code. Pages deployment is a separate manual workflow on the default branch. Do not add pull_request_target workflows that execute untrusted code with secrets.
