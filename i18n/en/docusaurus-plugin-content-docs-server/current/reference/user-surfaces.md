---
sidebar_position: 3
title: User surface map
---

# User surface map

Use this map to find a page. Every current core Console entry links to its task guidance, verification, and limits.

| Console page | Main tasks |
| --- | --- |
| [Overview](../operations/index.md) | Health, spend, and next actions |
| [Computer](../environments/computer.md) | Add SSH targets, terminals, tool setup, and Agent attachments |
| [Mobile](../environments/mobile.md) | Pair Android, control approval, run protected actions, and connect Agents |
| [Agents](../agents/index.md) | Build, deploy, invoke, attach Environments, publish, and review Activity |
| [Data Assets](../data-assets/index.md) | Manage collections, Agent assets, immutable releases, and Marketplace deliverables |
| [Providers](../providers/index.md) | Manage accounts, runtimes, Model Pool Sources, and Community listings |
| [Model Pool](../model-pool/index.md) | Manage Provider-backed sources, capability pools, and in-pool routing |
| [Routers](../routers/index.md) | Configure cross-pool strategy, custom router.py, and access export |
| [Marketplace](../marketplace/index.md) | Discover public Agents, Data Assets, and Provider capacity |
| [Observability](../operations/observability.md) | Metrics, alerts, reports, jobs, resources, and audit |
| [Billing](../billing/index.md) | Wallet, plans, spending, earnings, orders, payments, and invoices |
| TokenBank | Credit, funding, financial products, settlement, and risk |
| [Access](../access/index.md) | People, roles, one-resource sharing, machine identities, and access explanations |
| [Settings](../settings/index.md) | Workspace, account security, API keys, and SDK connection values |
| [Plan Catalog](../administration/plan-catalog.md) | Superuser control of global/Tenant plans, quotas, and data download pricing |

The top **Workspace** is the organization/tenant boundary and **Project** scopes resources. This guide uses **Environments** for Computer and Mobile under the left Workspace group; it does not mean the Agent-internal `env=prod` deployment slot.

Visibility does not imply permission to operate. Nexus resolves Workspace/Project, membership, role, resource grant, and machine-identity policy for each request. Use Access or `/api/v1/access/explain/` for a denial explanation. See [TokenBank desks](/tokenbank/reference/desks-and-products).

## Added and relocated entry points

| Console path | Task |
| --- | --- |
| `/inbox` | [Work Inbox](../operations/inbox.md): personal work and shared queues |
| `/openwrt-routers` | Register/manage private Routers and inspect connectivity |
| `/agents/{agentId}/private-display` | Start a [Private Run](../agents/private-runs.md) |
| `/agent-runs/{runId}/display` | Caller-owned Run display and interaction |
| `/access?tab=automation` | Machine identities; destination of legacy `/api-keys` |

Computer now also supports outbound Computer Runtime pairing; SSH Targets in the earlier map describe only the retained SSH method.
