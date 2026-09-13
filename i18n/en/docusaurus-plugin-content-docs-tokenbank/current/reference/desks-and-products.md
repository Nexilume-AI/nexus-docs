---
sidebar_position: 1
title: Desks and product policy
description: Live Desk routes, queues, actions, default product policy, tenant overrides, and retired routes.
---

# Desks and product policy

## Eight live Desks

| Desk | Route | Core Queues | Deep guide |
| --- | --- | --- | --- |
| Credit | `/tokenbank/credit` | applications, usage billing, overdue, bad debt | [Credit](../desks/credit.md) |
| Funding | `/tokenbank/prepaid` | fund account, lending, returns | [Funding](../desks/funding.md) |
| Derivatives | `/tokenbank/derivatives` | products, indexes, RFQs, quotes, contracts, risk, settlements | [Derivatives](../desks/derivatives.md) |
| Agent Finance | `/tokenbank/agent-finance` | policies, sponsorships, revenue, batches | [Agent Finance](../desks/agent-finance.md) |
| Agent Market | `/tokenbank/agent-market` | assets, listings, orders, trades | [Agent Market](../desks/agent-market.md) |
| Provider Finance | `/tokenbank/provider-finance` | plans, investments, revenue closeout | [Provider Finance](../desks/provider-finance.md) |
| Provider Market | `/tokenbank/provider-market` | assets, listings, orders, trades | [Provider Market](../desks/provider-market.md) |
| SLA | `/tokenbank/sla` | plans, subscriptions, reserves, tasks, cases | [SLA](../desks/sla.md) |

Funding retains the historical `/prepaid` route; the user-facing Desk name is Funding.

## Current default policy

| Default | Products |
| --- | --- |
| Open | `core`, `prepaid_token`, `api_derivative`, `agent_secondary_market`, `api_provider_market` |
| Approval required | `enterprise_credit`, `token_lending`, `price_lock`, `sla_protection`, `agent_financing`, `api_provider_financing` |

These values come from current service policy and tests. Tenant and jurisdiction overrides can make a product stricter or unavailable; the effective policy at action time wins.

## Retired routes

`foundation`, `accounts-ledger`, `risk`, `settlement`, `finance`, `operations`, `policies`, `audit`, and `market-surveillance` are retired routes and redirect to Credit. They are not independent Desks. Ledger, risk, policy, audit, and settlement remain cross-cutting controls inside current workflows.

## Verification

Before documenting or automating a flow, verify the current Console config, effective product policy, user Capabilities, and API schema. Do not infer current availability from a retired URL.

## Boundaries

Product availability is an internal policy fact, not a regulatory approval or external financial license.

## Catalog scope and action availability

Workbench also returns `queue_scopes`, `actor_context`, and applicable market-scope or platform-oversight information. A restricted queue does not mean the platform has no data. `capabilities` governs authorization; relevant actions may remain visible but disabled to explain permission, maker-checker, or state restrictions.

Large catalogs use `admin/catalog/{workbench}/{queue}/` pagination. Inline Workbench arrays are not complete exports. Funding's `/tokenbank/lending` compatibility alias maps to `prepaid`.
