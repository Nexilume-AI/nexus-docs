---
slug: /
sidebar_position: 1
title: TokenBank User Guide
description: Learn and operate Nexus internal credit, funding, market, settlement, and SLA controls.
---

# TokenBank User Guide

TokenBank is Nexus's internal control and settlement system. It connects Billing Wallets, purpose-specific accounts, double-entry journals, approvals, product policy, workflow tasks, and audit evidence. It is not a bank, public exchange, insurer, external cash clearer, or legal contract enforcement platform.

## Choose a learning path

### New user

1. Take the [Console tour](getting-started/console-tour.md).
2. Complete the [first credit workflow](getting-started/first-workflow.md).
3. Learn the [ledger and control model](concepts/ledger-and-controls.md).
4. Trace [how money and rights flow](concepts/money-and-rights-flow.md).

### Business operator

1. Learn [how to use desks](guides/use-desks.md).
2. Use the [financial-flow selector](guides/financial-flows.md).
3. Open the guide for your desk below.

### Administrator or auditor

1. Read [admin operations](guides/admin-operations.md).
2. Review [permissions and API contracts](reference/permissions-and-api.md).
3. Keep [status and error](reference/statuses-and-errors.md) and [automation](reference/automation-and-settlement.md) references nearby.

## Product map

| Need | Desk | Deep guide |
| --- | --- | --- |
| Use services now and pay later | Credit | [Credit](desks/credit.md) |
| Contribute to a pool or borrow internally | Funding | [Funding](desks/funding.md) |
| Lock a future Provider service price | Derivatives | [Derivatives](desks/derivatives.md) |
| Fund an Agent and share real usage revenue | Agent Finance | [Agent Finance](desks/agent-finance.md) |
| Transfer an Agent service/revenue right | Agent Market | [Agent Market](desks/agent-market.md) |
| Fund a Provider Runtime | Provider Finance | [Provider Finance](desks/provider-finance.md) |
| Transfer a Provider service/revenue right | Provider Market | [Provider Market](desks/provider-market.md) |
| Reserve-backed service compensation | SLA | [SLA](desks/sla.md) |

## Safety boundaries

- A successful API response is not sufficient evidence by itself: verify the business record, journal, account, and audit event.
- Preview, reconciliation, risk refresh, matching, and approval do not necessarily move value.
- Reuse one stable idempotency key when retrying the same financial event.
- Never resolve an inconsistency by editing a balance directly; repair or reverse the source event.
- Product defaults may be changed by tenant or jurisdiction policy.

For incidents, start with [symptom-based troubleshooting](troubleshooting/common.md).

## Current enterprise entry

Open **Govern → TokenBank** from the Console to launch its standalone workspace under the current Organization/Tenant identity. TokenBank is excluded from Cloud Community. The eight Desk routes remain; Funding uses `/tokenbank/prepaid`, with `/tokenbank/lending` as a compatibility alias.

Check catalog scope, record versions, and independent decision requirements before acting. Start with the [Console tour](getting-started/console-tour.md); API clients should also read [Permissions and API](reference/permissions-and-api.md).
