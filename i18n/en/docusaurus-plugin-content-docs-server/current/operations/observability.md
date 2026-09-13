---
title: Observability
description: Query metrics, background jobs, alerts, reports, resources, and audit history.
---

# Observability

Observability combines health monitoring with investigation of failed changes and jobs. Results are Tenant/Workspace scoped, and resource metrics reuse the resource's visibility checks.

## Current work areas

| Tab | Purpose |
| --- | --- |
| Overview | Summarize operational health and events requiring investigation |
| Activity | Query Jobs and background operations, details, and timelines |
| Automations | Manage alert rules, report schedules, and deliveries in Alerts and Reports |
| Audit | Inspect audit events and changes; requires audit permission |
| Platform | Inspect platform diagnostics; requires platform_diagnostics permission |

Open **Resource lookup** from Activity and supply an exact Resource Type/ID to query metrics. Resource Explorer is no longer a separate tab. Available views depend on the current account's monitoring permissions.

## Investigate a failure

1. Collect the Resource ID, Job ID, and approximate time from Overview or the product page.
2. Filter **Activity → Jobs** by Resource Type/ID and inspect status, result, and event timeline.
3. Query the same resource in **Activity → Resource lookup** for health, invocation, or usage metrics.
4. Search **Audit** by Resource ID and time for deployment, policy, access, or status changes.
5. If it persists, create an alert in **Automations → Alerts** and use Test to verify notification delivery.

Job input/result, event metadata, and audit snapshots are recursively redacted. Passwords, secrets, tokens, API keys, and credentials must not appear in clear text; explicitly safe prefixes, public keys, model keys, and idempotency keys can remain.

## Alert and report permissions

The monitoring capabilities endpoint determines access: `read` allows reading, `manage` controls alert management, `financial` exposes Reports, `reports` controls report management, `audit` exposes Audit, and `platform_diagnostics` exposes Platform. Check the current account, Tenant, and grants when an action is unavailable.

Alerts support system aggregates and the latest Metric Snapshot for non-system resources. A firing rule creates an Alert Event and emails configured rule targets, falling back to the creator and Tenant report recipients.

## Verification and troubleshooting

- Use **Test** after creating an alert and confirm both event and email. A test is synthetic and does not mean the real threshold was crossed.
- Use **Send now** and inspect Report Delivery status and recipient.
- **No resource metrics:** verify type, ID, Workspace, access, and availability of a recent snapshot.
- **Job never completes:** inspect the worker and queue responsible for that task, plus Job and resource state. Agents, Python builds, and data imports have dedicated workers; checking Celery alone is insufficient.
- **No audit entry:** verify `audit` permission, widen the time window, and search by the actual resource ID.

The authenticated Prometheus endpoint emits Tenant aggregates without secrets. Remote-write ingestion, long-term metric compaction/retention, and an audit-log retention policy are current non-goals.

## Execution workers and Inbox

Use [Inbox](inbox.md) to open source objects needing action; investigate historical metrics, Jobs and Audit here. Private Runs also need the durable Agent worker and Python builds need the builder. Healthy Celery/API alone does not prove those tasks executed. See [Private Runs](../agents/private-runs.md) for cancel, recovery and follow-ups.
