---
sidebar_position: 3
title: Status and error reference
description: Interpret lifecycle states, HTTP errors, workflow failures, and safe next actions.
---

# Status and error reference

Exact status strings come from the current API. Interpret them by lifecycle category rather than assuming every Desk uses identical words.

## Lifecycle categories

| Category | Meaning | Safe next step |
| --- | --- | --- |
| Draft/Submitted/Pending | record exists; decision or evidence is incomplete | review prerequisites |
| Approved/Confirmed/Active | authorized or effective; settlement may still be separate | inspect locks/journals |
| Matched/Ready/Payable | an obligation exists but final transfer may be pending | preview and settle |
| Settled/Paid/Distributed | recorded value movement completed | reconcile all evidence |
| Rejected/Declined/Cancelled | flow ended without its pending value movement | verify locks released |
| Overdue/Defaulted/Disputed/Frozen | exception control blocks or restricts use | resolve the case first |
| Failed/Exception | task or external step did not complete | inspect Alert and retry safely |

## HTTP and business errors

| Signal | Likely cause | Evidence and response |
| --- | --- | --- |
| `400` | invalid amount, Unit, fields, or transition | correct the request; do not retry unchanged |
| `401` | authentication missing or expired | renew credentials |
| `403` | missing Capability, ownership, or policy denial | verify tenant, role, and effective policy |
| `404` | absent or invisible resource | verify identifier and tenant scope |
| `409` | state changed or idempotency conflict | query the original record/key |
| insufficient balance/reserve/margin | source available value is too low | fund the correct source; never force negative value |

## Verification

After recovery, confirm the business state, lock release/consumption, journal, Audit Event, and task/Alert closure. A cleared UI warning without reconciled value is not resolution.

## Troubleshooting

Preserve the correlation ID, tenant, action, record ID, idempotency key, current state, and exact error. Use them to trace business, journal, task, and external evidence.

## Boundaries

This page explains categories; API/Swagger and the current Record remain authoritative for exact enum values and valid transitions.

Use [common troubleshooting](../troubleshooting/common.md) to collect evidence and repair a failed flow.

## Concurrency conflicts and workflow states

| HTTP / Code | Recovery |
| --- | --- |
| 409 `MARKET_QUOTE_STALE` | Listing price, remaining quantity, or state changed; preview and confirm the order again |
| 409 `TOKENBANK_RECORD_STALE` | Reload the record, inspect its state and actor constraints, then submit |

Workflow Case `lifecycle_status` is `open`, `waiting`, `resolved`, or `cancelled`. Workflow Task `task_status` is `open`, `done`, or `cancelled`. These differ from Scheduled Task Run states `running`, `succeeded`, `failed`, and `skipped`.

Agent Market trades settle from `pending_settlement`. Provider Market trades use `pending`, then `settled`. Do not interchange the two products' state enums.
