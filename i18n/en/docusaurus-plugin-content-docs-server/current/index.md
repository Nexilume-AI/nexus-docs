---
slug: /
sidebar_position: 1
title: Nexus Server User Guide
description: Complete user paths from a first Agent call through Providers, access, billing, and production operations.
---

# Nexus Server User Guide

Nexus Server is the cloud control plane. It serves REST APIs, Nexus Console, Mobile APIs, and the Computer WebSocket gateway. Workspaces, Projects, resource permissions, billing, and audit share one identity boundary.

The guide follows “get a result, understand the system, then operate it safely.” Start with a Workspace/Project and the repository sample Agent. Business users can enter an end-to-end tutorial; operators start with production readiness.

## First run

1. Enterprise users open their administrator-provided Console. Self-hosting users follow the [Community quickstart](getting-started/quickstart.md).
2. [Create your first Workspace and Project](getting-started/first-workspace.md) and select a concrete resource/billing context.
3. Use the [Console tour](getting-started/console-tour.md) to understand product areas.
4. Follow the [first Agent tutorial](getting-started/first-agent.md) through sample build, deployment, MCP call, and verification.
5. Use [Environments](environments/index.md) for a Computer or Mobile device. With OpenWrt hardware, [connect its IPv6 Agent](guides/connect-openwrt.md).

## Three end-to-end tutorials

| Goal | Tutorial | Verify in |
| --- | --- | --- |
| Build a model service entry point | [Provider → Model Pool → Router → API](tutorials/provider-router-api.md) | Gateway response, Observability, Provider Pool Usage |
| Manage human access lifecycle | [Invite, authorize, verify, and offboard](tutorials/team-access-lifecycle.md) | Access Explain, recent changes, Audit |
| Publish and reconcile a result | [Marketplace → consumption → Billing](tutorials/marketplace-billing.md) | Deliverable, Spending/Earnings, Order, Audit |

## Core work areas

| Area | What you can do |
| --- | --- |
| [Environments](environments/index.md) | Connect Computers, pair Mobile devices, and give Agents controlled execution access |
| [Agents](agents/index.md) | Create an Agent, choose Docker or OpenWrt, deploy, invoke, and publish it |
| [Data Assets](data-assets/index.md) | Turn Agent traces, memory, and outputs into governed collections and releases |
| [Providers](providers/index.md) | Store upstream credentials and connect runtime capacity to Pool, Router, or Marketplace |
| [Model Pool](model-pool/index.md) | Add Provider Runtimes as sources and control health, cost, and fallback |
| [Routers](routers/index.md) | Route across Pools by priority, cost, latency, health, or custom code |
| [Marketplace](marketplace/index.md) | Discover and acquire public Agents, Data Assets, and Provider capacity |
| [Operations](operations/index.md) | Triage and investigate metrics, jobs, alerts, audit, and production state |
| [Access](access/index.md) | Invite people, assign roles, share resources, and create machine identities |
| [Billing](billing/index.md) | Manage Wallet, plans, Marketplace usage, payments, and invoices |
| [Settings](settings/index.md) | Manage account, Workspace context, API Keys, and SDK examples |

## By role

| Role | Start here |
| --- | --- |
| Platform operator | [Readiness](operations/production-readiness.md), [deployment](guides/production-deployment.md), [backup](operations/backup-and-restore.md), [upgrade](operations/upgrade-and-rollback.md) |
| Workspace administrator | [Access](access/index.md), [Billing](billing/index.md), [Settings](settings/index.md) |
| Agent builder | [First Agent](getting-started/first-agent.md), [Agents](agents/index.md), [Environments](environments/index.md) |
| Provider operator | [Provider→Router tutorial](tutorials/provider-router-api.md), [Providers](providers/index.md), [Model Pool](model-pool/index.md) |
| Marketplace operator | [Marketplace→Billing tutorial](tutorials/marketplace-billing.md), [Marketplace](marketplace/index.md) |
| API developer | [API examples](reference/api.md), [status and errors](reference/statuses-and-errors.md), built-in Swagger |
| Finance or risk | [Billing](billing/index.md), [TokenBank](/tokenbank/) |

## Important boundaries

- Workspace is the tenant, access, Billing, and Audit boundary. Computer Environment is an Agent execution resource.
- Agent, Gateway, Remote CLI, and Service Account credentials are not interchangeable.
- Only a call, purchase, or product-defined consumption action can move platform money. Create, Health, and Publish alone are not Usage.
- TokenBank is an internal credit, control, and settlement system, not a bank, public exchange, insurer, or external cash clearer.
- Production cannot replace PostgreSQL, ASGI, Worker, and Beat with SQLite, a development server, or Celery eager mode.

For login, WebSocket, context, runtime, Provider, storage, billing, or edge TLS failures, start with [troubleshooting](troubleshooting/common.md) and use [status and errors](reference/statuses-and-errors.md).

## Current execution and work queues

- [Private Runs and interaction](agents/private-runs.md): caller-owned display, files, follow-ups and recovery.
- [Work Inbox](operations/inbox.md): personal work and shared role queues for input, approvals and operational issues.

This guide covers enterprise Server. Development also requires PostgreSQL. Computer supports outbound Runtime pairing and SSH; Agents support Python upload builds. Available actions depend on authorization and deployment configuration.
