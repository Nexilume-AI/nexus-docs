---
sidebar_position: 2
title: Complete your first credit workflow
description: Apply for 10,000 USD of service credit, approve it, and verify business, ledger, and audit evidence.
---

# Complete your first credit workflow

This tutorial uses a `10,000 USD` enterprise credit application to teach the shared TokenBank pattern: Desk → Queue → Record → Action → Evidence.

## Requirements and example

Use an applicant who can read and apply in Credit Desk, plus a separate approver for the approval step. Confirm the tenant and company profile. The example requests `10,000 USD` for 30 days of Nexus API service.

## 1. Submit as the applicant

Open **Govern → TokenBank → Credit**, select the **Applications** Queue, choose **Apply for credit**, enter the limit, Unit, term, and purpose, review the summary, and submit.

Expected state: `Submitted` or the equivalent current API value. No spendable credit should exist merely because the form was opened.

## 2. Decide as the approver

Open the pending Record, verify tenant, applicant, existing exposure, requested Unit, purpose, and risk evidence, then choose **Approve**. A decline closes the application without creating available credit.

Approval creates or updates the credit account and limit allocation. It does not generate cash.

## 3. Add usage and payment evidence

After real Nexus usage exists, run **Sync spending & invoices**. If `3,200 USD` is synchronized, `credit_used` should be `3,200 USD` and available credit `6,800 USD`. A later `2,000 USD` payment should reduce the receivable and `credit_used` to `1,200 USD`.

## Verification

Check the approved application, account limit/used/available values, usage and receivable record, balanced Journal Entry, applicant and approver Audit Events, and stable idempotency key. Retrying the same sync must not create a second receivable.

## Troubleshooting

| Symptom | Evidence | Fix |
| --- | --- | --- |
| Approve is hidden | role, Capability, tenant, status | use an authorized approver and valid pending record |
| Usage sync says insufficient credit | available credit, payments, Unit | post the valid payment or adjust approved limit |
| Response timed out | idempotency key, journal, audit | query the original event before retrying |
| Totals do not reconcile | source usage, receivable, journal lines | repair/reverse the source event; do not edit balance |

## Boundaries

This is internal Nexus service credit, not a bank loan. Continue with the [Console tour](console-tour.md), [Credit deep guide](../desks/credit.md), and [ledger model](../concepts/ledger-and-controls.md).
