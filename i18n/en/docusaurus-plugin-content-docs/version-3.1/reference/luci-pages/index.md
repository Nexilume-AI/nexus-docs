---
sidebar_position: 1
title: Pages and workflow
---

# LuCI pages and workflow

Find the menu under **Status → Agent Routing**. The user goal is “configure an Agent private cloud network”; the actual device entry remains named **Quick Setup**.

| Type | Pages | Use |
| --- | --- | --- |
| Private-cloud initialization | [Quick Setup](quick-setup.md), [Router Roles](roles.md) | Create the trust domain and first node, or host Relay/Directory |
| Feature configuration | [Agent APIs & Protocols](protocols.md), [Advanced Settings](advanced-settings.md), [Static Peers](static-peers.md), [Policy RIB](policy-rib.md) | Join Agents; configure public IPv6, discovery, Peers, and policy |
| Status and trust | [Overview](overview.md), [Local Agents](local-agents.md), [Capability Routes](capability-routes.md), [Neighbors & Discovery](neighbors.md), [Peer Trust](peer-trust.md) | Verify nodes, leases, routes, neighbors, and trust |

Recommended order: **Quick Setup → Agent APIs & Protocols → Local Agents → Capability Routes → Overview**. Configure discovery only when adding another node; enter Advanced Settings only for public `/128`, cross-domain, or NAT requirements.

:::tip Saved is not running
Click **Save & Apply** after a change. A valid saved candidate is only the first check; verify services, sessions, leases, and routes on the status pages.
:::
