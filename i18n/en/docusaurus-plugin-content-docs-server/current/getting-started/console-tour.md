---
sidebar_position: 2
title: Console tour
description: Understand Nexus Console Workspaces, Projects, and product work areas.
---

# Console tour

The selectors at the top of Nexus Console choose the organization and project in which you are working. The left navigation chooses the kind of resource you want to manage. Confirm the context before you create or change a resource so an Agent, Provider, or charge does not land in the wrong Project.

## Workspace, Project, and Environment

| Name | Console location | Meaning |
| --- | --- | --- |
| Workspace | First top selector | Organization and security boundary; maps to a Server tenant |
| Project | Second top selector | Resource and collaboration scope inside a Workspace; **All projects** provides a cross-project view |
| Environment | Computer and Mobile under the left Workspace group | An execution target an Agent can use, not a `dev/staging/prod` deployment slot |

Changing Workspace also changes the available Projects, resources, permissions, and Billing data. Check both selectors first when a resource appears missing or an operation returns 403.

## Product areas

| Group | Pages | Common tasks |
| --- | --- | --- |
| Overview | Overview | Review health, spend, and suggested next actions |
| Environments | Computer, Mobile | Connect SSH computers, pair Android devices, configure tools, and run protected actions |
| AI resources | Agents, Data Assets | Build Agents and manage runtimes, displays, collections, and releases |
| Model services | Providers, Model Pool, Routers | Connect model accounts, operate capacity, combine sources, and route traffic |
| Marketplace | Agents, Data Assets, Providers | Discover and use published resources |
| Operations | Observability, Billing, TokenBank | Review metrics, audit, platform charges, and financial desks |
| Management | Access, Settings | Manage people, roles, machine identities, API keys, and account security |

## Recommended path

1. If no context exists, [create a Workspace and Project](first-workspace.md), then select both.
2. Use the [first Agent](first-agent.md) to prove deployment, MCP, and audit first.
3. Open [Environments](../environments/index.md) only when external compute is needed.
4. Add models with the [Provider→Router tutorial](../tutorials/provider-router-api.md) after the first Agent result.
5. Use [Access](../access/index.md) for durable roles and **Share** for one-resource access.
6. Confirm usage, charges, jobs, and audit in [Billing](../billing/index.md) and Observability.

## Where to verify an action

| Action | Product state | Independent evidence |
| --- | --- | --- |
| Create/deploy Runtime | Agent/Provider state and Health | Observability Job, Audit |
| Call Agent/Router | Activity/Gateway response | Metrics, Request ID, Billing Usage |
| Invite/grant access | Access lists | Access Explain, recent changes, Audit |
| Publish/consume | Marketplace state and deliverable | Spending/Earnings, Order, Audit |
| Change production config | Service/process health | Worker/Beat, backup ID, restore drill |

Anonymous users see only public Marketplace and product information. Private Workspace, Project, resource, and Billing data loads only after sign-in. See [Identity and request paths](../concepts/identity-and-request-path.md) for browser sessions, JWTs, API keys, service accounts, and edge credentials.

Continue with the [first Agent workflow](first-agent.md). Platform operators start with [production readiness](../operations/production-readiness.md), or use the [user surface map](../reference/user-surfaces.md).

## Current navigation groups

- **Build**: Agents, Data Assets; Model Fabric follows Providers → Model Pool → Routers.
- **Operate**: Computer, [Inbox](../operations/inbox.md), OpenWrt Routers, Mobile, Observability.
- **Discover**: Agent, Data Asset and Provider Runtime marketplaces.
- **Govern**: Access, Billing, Settings, TokenBank and the Superuser-only Plan Catalog.

Legacy `/gateway` and `/playground` redirect to Computer; `/models` and `/deployments` to Model Pool; `/api-keys` to Access Machine identities. The standalone [Private Run display](../agents/private-runs.md) is not a public sharing page.
