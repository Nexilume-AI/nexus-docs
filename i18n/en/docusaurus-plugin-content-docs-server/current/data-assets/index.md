---
title: Data Assets
description: Turn Agent traces, memory, and output files into governed collections, immutable releases, and Marketplace deliverables.
---

# Data Assets

Data Assets uses Dataset collections as publishing containers. The current product accepts three traceable Agent-generated asset types and enforces redaction, consent, license, scan, and policy gates before release or publication.

| Source type | Import gate |
| --- | --- |
| Conversation Trace | Run completed, system redaction `passed`, redacted events available |
| Agent Memory | Consent `approved`; license `approved` or `internal` |
| Output File | Scan `passed`, policy `approved`, eligible license, unchanged file hash |

## Create a collection and import assets

1. Open **Data Assets → My Data Assets → Create collection**.
2. Select it and click **Import Agent asset**.
3. Select the Agent, Run, and source type.
4. For traces, run **Run redaction** before export. For output files, use **Scan output** before Capture. Only eligible memory items are listed.
5. Verify provenance, size, hash, and governance metadata under **Current assets**.

Trace export reads only Server-generated `redacted_payload_json`; clients cannot mark raw events as redacted. Output files must be reported by Agent events, and users cannot supply a workspace path, filename override, or license decision during import.

## Create an immutable release

**Release readiness** lists every blocker. When all checks pass, choose **Review → Create release**. A release is an immutable snapshot of assets, provenance, and compliance metadata. Export new Agent data into a new release instead of modifying an old one.

Release History shows composition, size, creation time, and a manifest with source type, Agent, Run, gates, hash, and download URL.

## Settings and publication

Use **Collection settings** for name, visibility, pricing plan, maximum-size quota, and deletion. Setting visibility to `public` reruns publication gates over all Agent assets.

Quota limits total collection size but is not currently billing enforcement. Use Share for exceptions and [Access](../access/index.md) roles for durable team permissions.

## Pull from Marketplace

Under **Marketplace → Data Assets**, filter by query, free/paid, update time, name, or size. Details show publisher, release, formats, source Agent count, license, sensitivity, price, and file manifest.

Sign in and click **Pull release**. The first acquisition creates a usage record and may charge under the displayed terms; **Open files** reopens an already acquired release. Pull returns a governed manifest and per-file download URLs, not a mutable copy.

## Verification and troubleshooting

- **A completed Run cannot export a trace:** confirm it ended with `RunFinished` and passed system redaction.
- **Output cannot be captured:** rescan it, check policy/license, and confirm its hash did not change.
- **Release or publication is blocked:** expand Release readiness and fix each gate; client metadata cannot override it.
- **Pull is rejected:** confirm sign-in, Workspace, public release status, and Wallet/order state in [Billing](../billing/index.md).

Media assets and Dataset imports have dedicated entrypoints. Available operations depend on capabilities, authorization and Release readiness. Upload/import success does not imply publication approval or bypass capacity, scanning and access checks.
