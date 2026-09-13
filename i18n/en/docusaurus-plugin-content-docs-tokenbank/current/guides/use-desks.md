---
sidebar_position: 1
title: Use TokenBank desks
description: Understand the Desk, Workflow, Queue, Record, Action, and Detail Panel operating model.
---

# Use TokenBank desks

All eight Desks use the same operating grammar.

| Layer | Question it answers |
| --- | --- |
| Desk | Which financial domain am I operating? |
| Workflow | Which business lifecycle is in scope? |
| Queue | Which records need the same kind of attention now? |
| Record | Which application, trade, claim, or settlement am I handling? |
| Action | What transition is permitted from the current state? |
| Detail Panel | What terms, money, rights, journal, and audit evidence explain it? |

## Operating sequence

1. Confirm tenant, role, Desk, and Unit.
2. Choose the Queue by current state.
3. Read the entire Record before selecting an Action.
4. Distinguish a decision, lock, value movement, automation trigger, and external-evidence update.
5. Record a reason for approval, rejection, manual recovery, or high-risk action.
6. Verify business, ledger, and audit evidence after completion.

## Safe retries

When a request times out, keep its idempotency key, refresh the record, and search the journal/audit trail before retrying. A second key means a second business event.

## Verification

The Queue should show the expected new state, but that is only the first check. Confirm balances/locks or rights, journal, audit event, and downstream record.

## Troubleshooting

Missing action: inspect Capability and state. Missing record: inspect tenant, filters, and refresh. Ambiguous value movement: consult the deep Desk page and stop before repeating the action.

## Boundaries

The Console does not replace accounting reconciliation or external settlement confirmation. Use the [Desk and product reference](../reference/desks-and-products.md) and [status reference](../reference/statuses-and-errors.md).
