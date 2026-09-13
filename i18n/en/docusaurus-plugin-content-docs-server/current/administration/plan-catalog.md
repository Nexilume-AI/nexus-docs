---
title: Plan Catalog
description: Superuser administration of global and Tenant-specific plans, quotas, and Marketplace data pricing.
---

# Plan Catalog

Plan Catalog is the Superuser product catalog. Regular users discover and buy visible plans in [Billing](../billing/index.md). Only users with `is_superuser` can open Plan Catalog; others are redirected to Billing.

## Scope and lifecycle

| Scope | Visibility | Typical use |
| --- | --- | --- |
| Global | Every Workspace/Tenant | Standard public plan |
| Tenant custom | Assigned Tenant only | Negotiated pricing or quotas |

Plan Type is Models, Agents, or Dataset. Status is Active, Disabled, or Archived. **Customize** copies a plan into a Tenant-scoped version, preserving the global plan as a template. Archive removes it from normal catalog use without erasing historical orders.

Edits affect future purchases only. Existing orders retain their captured amount and terms, so investigate historical billing from the Order rather than today's catalog row.

## Configurable capabilities

- **Base pricing:** name, price, currency, scope, type, and status.
- **Agent runtime resources:** image size, memory/CPU, export storage, concurrent runs, per-run/monthly time, monthly runs, Computer, Mobile, Model Pool size, and Service Account/token limits.
- **API token rental:** included tokens, expiry days, overage switch, and price per 1K tokens.
- **Data download pricing:** fixed download, per-GB price, currency, and owner/platform revenue shares.

Use non-negative numeric values. Owner and platform shares are ratios from 0 to 1; validate their combined business rule before publication rather than relying only on input bounds.

## Recommended change workflow

1. Locate the plan with Type, Scope, and Status filters.
2. Edit a standard plan directly, or use Customize for a negotiated Tenant package.
3. Verify currency, quota, and revenue share; save as Disabled for review.
4. Activate it, then use a regular account in the target Tenant to verify Billing visibility and purchase.
5. Create a test order and inspect captured amount, entitlement, usage, and invoice before production sales.

## Security and troubleshooting

- **Plan Catalog is missing:** the account must be Superuser; Tenant Owner alone is insufficient.
- **Tenant cannot see a plan:** inspect scope, Tenant ID, status, and plan type.
- **Old order does not change after an edit:** this is the expected historical snapshot behavior.
- **Entitlement remains after disabling a plan:** disable/archive affects future catalog use; existing rights follow their order lifecycle.
- **Unexpected split or quota:** correlate catalog `quota_json`, Billing order/usage, and [Observability Audit](../operations/observability.md).

Production plan creation, edits, and archive operations should be audited and limited to the smallest practical Superuser set.
