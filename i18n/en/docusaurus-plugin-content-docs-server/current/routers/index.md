---
title: Routers
description: Route across Model Pools by priority, cost, latency, health, or custom Python.
---

# Routers

A Router is a stable entry point across Model Pools. It chooses a pool first, then that pool uses its own policy to choose a Provider source. Router policy and [Model Pool](../model-pool/index.md) policy are two distinct routing layers.

## Create and bind a Router

1. Make sure at least one Model Pool is available.
2. Open **Routers → Create router** and enter a name.
3. Under **Configure router → Model Pools**, select one or more pools and save.
4. Select a strategy and click **Apply**.
5. After deployment, click **Export access** to obtain the Router-scoped endpoint, API key, `.env`, and curl example.

Only a `deployed` Router can export access. Configure intentionally excludes endpoints and keys so configuration rights stay separate from credential distribution.

## Choose a strategy

| Console option | Internal strategy | Use case |
| --- | --- | --- |
| Priority | `manual_priority` | Explicit primary and fallback pool order |
| Lowest cost | `lowest_cost_pool` | Minimize pool-level cost |
| Lowest latency | `lowest_latency_pool` | Prefer low-latency pools |
| Best health | `best_health_pool` | Prefer healthier pools |
| Custom router.py | `custom` | Choose using request and candidate metadata |

Built-in strategies never execute an uploaded `router.py`. For Custom, open **Advanced**, upload a draft, and **Deploy** it first. The Console blocks Custom if no deployed version exists.

## Custom router.py

The entry point receives `request`, `candidates`, and `context`, and returns ordered Deployment IDs plus an optional reason. Candidates come only from Model Pools bound to the Router.

Execution is sandboxed: each invocation gets a temporary root; only the work directory is writable; runtime paths are read-only; secrets in input are redacted; and Provider credentials are not present in the environment. Image data URLs and signed URL query strings are redacted before multimodal requests enter the sandbox.

Do not hard-code API keys or assume access to arbitrary networks, files, or unbound model sources.

## Marketplace Providers and sharing

**Use in router** on a Provider Marketplace detail page adds Community capacity as a Router preference. A preference influences candidate order but does not guarantee a traffic share; health, quota, price, and Router policy still apply.

Use **Share** for delegated Router access. A read grant cannot upload, deploy, or change policy or price. Distribute the Router-scoped key from Export access, not an unrestricted Gateway key.

## Verification and troubleshooting

- Confirm binding count, strategy, and `deployed` status in the Router list.
- Run the minimal curl from Export access and correlate Jobs, Metrics, and Audit in [Observability](../operations/observability.md).
- **Custom cannot be applied:** upload and deploy `router.py`; verify it is a deployed runtime source.
- **No candidates:** inspect bound pools, source enabled/health, and Community Provider quota.
- **Access denied:** use the key exported for this Router and inspect its policy, Workspace/Project, and [Access](../access/index.md).
