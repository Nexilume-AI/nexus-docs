---
sidebar_position: 1
title: Troubleshooting TokenBank
description: Diagnose by symptom, evidence, root cause, repair, and verification.
---

# Troubleshooting TokenBank

Do not begin with repeated clicks. Capture tenant, user/role, Desk/Queue, Record ID, action, amount/Unit, idempotency key, correlation ID, time, and exact error.

## Symptom-based diagnosis

| Symptom | Possible cause | Query evidence | Repair |
| --- | --- | --- | --- |
| Record or Action missing | wrong tenant, Queue, filter, Capability, or state | URL, tenant, role, status, Console refresh | select correct scope or role; do not bypass permission |
| Balance/reserve/margin insufficient | locked value, wrong Unit, missing payment, or stale state | account available/locked, source event, journal | fund or release the correct source |
| Duplicate or conflict | new key used for a retry or concurrent transition | idempotency key, journal, audit, status | reuse/query original key; reverse true duplicates |
| Approved but not settled | approval is separate or downstream task failed | journal, Scheduled Task, Alert, downstream record | repair task and retry idempotently |
| Market trade stuck | unmatched price, lock inconsistency, or dispute | listing, order, trade, locks, case | resolve the blocking stage before settlement |
| Claim or payout stuck | reserve shortage or external uncertainty | reserve, payable, provider ref, Alert | top up/reconcile; never fabricate completion |
| Totals disagree | mixed Units, omitted source, duplicate, or rounding | source events, journals, statements, checkpoints | reconcile by tenant/Unit and compensate explicitly |

## Verification after repair

Confirm final Record state, expected account and lock values, balanced journal, audit trail, closed/resolved task or Alert, and downstream Trade/Claim/Payable/Statement/external evidence. Repeat the safe retry once to prove idempotency.

## Escalation package

Provide immutable IDs and evidence, not screenshots alone. Include the last known good Checkpoint and whether external payment finality is known.

## Safety boundaries

Never edit balances, delete audit history, reuse another tenant's record, change a settled Statement, or mark an uncertain external payout as paid. Use supported reversal and recovery workflows.

See [automation and external settlement](../reference/automation-and-settlement.md) and the relevant Desk guide.

## Current catalog and concurrency issues

- **Incomplete search results:** inspect queue, scope, status, cursors, and snapshot. Restart at page one after filtering; distinguish loaded_count from total_count.
- **Visible but disabled action:** read its control reason and check selection, Capability, and independent decision requirements.
- **409 conflict:** `MARKET_QUOTE_STALE` requires a new order preview; `TOKENBANK_RECORD_STALE` requires reloading and reconfirming the record. Retain response evidence and idempotency keys.
- **No action on an SLA Case:** switch to Workflow tasks and select the Claim review or settlement task.
- **Funding repayment fails:** check available USD in the Borrower Billing Wallet. External evidence alone does not perform the wallet debit.
