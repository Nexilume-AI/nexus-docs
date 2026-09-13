---
title: Marketplace
description: Discover, evaluate, and acquire public Agents, Data Assets, and Provider capacity.
---

# Marketplace

Marketplace is Nexus's public discovery surface for three governed product classes. Guests can browse public information; invoking, pulling, adding capacity to a Router, or recording usage requires sign-in and a selected Workspace/Project.

| Product | Acquisition result | Primary checks |
| --- | --- | --- |
| Agent | Invoke or deploy a governed Agent Runtime | Runtime type, permissions, version, price, health |
| Data Asset | Access an immutable release manifest | Provenance, redaction/consent/license/scan, size, price |
| Provider | Add Community capacity to a Router preference | Health, quota, success rate, P95, price, SLA, data terms |

## Consumer workflow

1. Choose **Marketplace → Agents / Data Assets / Providers**.
2. Narrow results with search, category, price, health, or product-specific filters.
3. Review publisher, version, operational evidence, commercial terms, and Workspace fit.
4. Sign in and invoke the Agent, pull the release, or choose **Use in router**.
5. Verify charges in [Billing](../billing/index.md) under Usage, Spending/Earnings, Orders, and Invoices.

Marketplace never exposes Provider credentials, internal endpoints, or owner secrets. Public visibility does not grant management rights; actions still enforce Workspace, Project, Wallet, key policy, and resource authorization.

## Publisher workflow

- Agent: deploy and health-check the Runtime, configure publication, then publish from [Agents](../agents/index.md).
- Data Asset: create a gate-compliant immutable release and make the collection public; see [Data Assets](../data-assets/index.md).
- Provider: explicitly add the Runtime to [Model Pool](../model-pool/index.md) as a source before publishing its Community listing; see [Providers](../providers/index.md).

A listing is not a copy of the underlying resource. Unpublishing stops new discovery or acquisition, while existing orders, usage, audit, and immutable delivery records follow their module lifecycles.

## Add a Provider to a Router

Click **Use in router** on Provider detail, then choose the Router and preference. You can create a Router if needed. The preference influences candidates; [Router](../routers/index.md) policy selects the pool and Model Pool policy selects its source.

## Verification and troubleshooting

- **Browse works but use does not:** sign in, select Workspace/Project, and verify Wallet and permission prerequisites.
- **Product is missing:** inspect public visibility, current release/runtime health, publication gates, and moderation.
- **Provider gets no traffic:** inspect Router preference, pool binding, Provider quota/health, and both routing layers.
- **Charge differs from the current listing:** use the plan and price captured on the order; later catalog edits do not rewrite prior orders.

For a denied action, correlate [Access Explain](../access/index.md) with [Observability Audit](../operations/observability.md).
