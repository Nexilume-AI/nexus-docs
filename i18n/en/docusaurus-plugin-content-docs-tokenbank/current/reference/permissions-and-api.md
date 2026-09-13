---
sidebar_position: 2
title: Permissions and API contracts
description: Roles, Capabilities, tenant visibility, write boundaries, idempotency, and schema sources.
---

# Permissions and API contracts

TokenBank authorizes by tenant context, resource relationship, role/Capability, product policy, and record state. Seeing a Record does not imply permission to act on it.

## Role patterns

| Role pattern | Typical scope |
| --- | --- |
| Applicant/Customer | submit own applications, buy eligible products, read own records |
| Publisher/Provider | create plans for owned Agent/Runtime/Provider resources |
| Investor/Market participant | use authorized Billing Wallet and own rights |
| Approver/Risk/Reviewer | decide eligible pending records without owning their source data |
| Operator/Settlement | run billing, matching, settlement, closeout, and recovery actions |
| Auditor | read business, ledger, policy, and audit evidence without financial writes |

## Capability checks

Write APIs require the specific Capability for the action. The server must also verify tenant, object ownership or participation, product policy, status transition, Unit, sufficient available value, and idempotency.

## API contract conventions

- Treat `400` as invalid input or transition, `401` as missing/invalid authentication, `403` as authorization/policy denial, `404` as inaccessible or absent resource, and `409` as state/idempotency conflict.
- Use one stable idempotency key for one financial intent.
- Do not treat HTTP success as proof of downstream settlement; query the resulting record and evidence.
- Swagger/Redoc is authoritative for exhaustive fields and current serializer schema. These guides explain workflow and critical contracts, not every field.

## Verification

Test at least allowed role, denied role, wrong tenant, wrong state, insufficient balance, and repeated idempotency key. Verify denied requests create no financial journal.

## Troubleshooting

For unexpected `403`, compare Capability and effective product policy. For `404`, check tenant visibility before assuming deletion. For `409`, query by idempotency key and current status before retrying.

## Boundaries

UI visibility is not a security boundary; all enforcement must occur server-side. Tenant override cannot bypass ledger balance or Unit invariants.

See [status and errors](statuses-and-errors.md) for response and lifecycle interpretation.

## Catalog and version APIs

Paths below are relative to `/api/v1/tokenbank/`; they do not introduce new Console Desks:

| Method and path | Current purpose |
| --- | --- |
| `GET admin/catalog/{workbench}/{queue}/` | Query an authorized catalog; 50 rows by default, maximum `limit` 100 |
| `POST market/quote-preview/` | Preview using `market` (agent/provider), `listing_id`, `quantity`, and `limit_price` |
| `GET workflow-cases/` | List current-Tenant cases filtered by `product_type` and `lifecycle_status` |
| `GET workflow-tasks/` | List current-Tenant workflow tasks filtered by `product_type` and `task_status` |

Catalog responses include `items`, `loaded_count`, `total_count`, `count_is_exact`, `next_cursor`, `previous_cursor`, `snapshot`, and applied `filters`. With `include_total=false`, the total may be null, not zero. Search `q` is limited to 200 characters. Sort, price, Publisher, and Model filters depend on the catalog. `snapshot` is an update-time cutoff, not a permanently preserved database snapshot.

Preview a sale before buying, check remaining quantity, minimum price, and `maximum_order_value`, then include its `quote_version` in the order. The preview's `valid_until` does not reserve inventory or guarantee a price; the Server revalidates listing state and funds.

Actions supporting concurrency checks should carry the latest `record_version` (the record's `updated_at`); quote generation can also use `rfq_version`. These are not idempotency keys. On 409, reload and reconfirm rather than omitting the version to bypass the conflict.
