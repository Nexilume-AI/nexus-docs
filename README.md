# Nexus Documentation

Public user documentation for **Nexus Server, TokenBank, OpenWrt and the Python SDK**, in Simplified Chinese and English. This repository contains documentation, website code and downloadable examples, not the Server or TokenBank application source.

## Run locally

Use Node.js 22 LTS and Python 3.12+. From a fresh checkout:

```sh
npm ci --ignore-scripts
npm run check:docs
npm start
```

Open the address printed by Docusaurus. Use `npm run start:en` for English.

```sh
npm run check:security
npm run build
npm run serve
```

The build writes `build/`, includes both languages and all four products, and fails on broken links. No database, Cloud account, tokens or private source checkout is needed.

## Hosting

Set `DOCS_URL` to the HTTPS origin and `DOCS_BASE_URL` to `/` for a root site or `/nexus-docs/` for a project site, then run `npm run build`. Upload only `build/` to a static host.

The Pages workflow is manual, restricted to the default branch, and uses the `github-pages` environment. Enable Pages with GitHub Actions in repository settings before running it. Set repository variables `DOCS_URL` and `DOCS_BASE_URL` for a custom destination. Pull requests build without deployment privileges.

## SDK documentation maintenance

Normal builds do not require SDK source. To regenerate/check API references, clone the public SDK as `sdk-source`, check out the reviewed SDK commit, install `requirements-docs.txt`, and run `npm run check:api`. Alternatively set `NEXUS_SDK_SOURCE` to its `src` directory. For the runnable design test install that SDK with its `fastmcp` extra and run `npm run check:sdk-design`.

Current docs describe published SDK 0.46.2 plus the Linux fix on main. Release-package availability and local test scope are stated on the relevant pages. OpenWrt 3.1 and SDK 0.22.0 retain their URLs but show the same current documentation. Run `npm run sync:versions` after editing current docs; `check:docs` rejects drift.

## Contribute and report problems

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Do not include credentials or personal deployment data in issues.

## License

[Apache-2.0](LICENSE), carried forward from the source documentation tree. Third-party components retain their own licenses. Publishing documentation does not license separately distributed proprietary application code or grant rights to third-party trademarks.

## Version content synchronization

All existing version URLs follow current documentation. Run `npm run sync:versions` after edits and `npm run check:versions` to verify content parity. Version labels are not promises of older software compatibility.
