---
sidebar_position: 2
title: Configure an Agent private cloud network
description: Start with one OpenWrt node and establish Agent private-cloud identity, boundaries, discovery, and access.
---

# Configure an Agent private cloud network

This guide turns one OpenWrt device into the first networking node of an Agent private cloud. The result is a small but complete private cloud with a trust domain, Router node identity, Agent registration ingress, and capability routes. You can later add Routers, public IPv6 ingress, or NAT Relay.

“Agent private cloud network” is a user-facing deployment concept, not a new UCI field. It is built from existing settings: **Agent domain is the private-cloud trust domain, and Router ID is a node identity**.

## 1. Open the private-cloud setup entry

Open **Services → Agent Router → Quick Setup**. Quick Setup remains the actual LuCI page name. It configures identity, LAN discovery, and optional Relay. Node, Relay, and Directory roles live on **Router Roles**.

## 2. Create the trust domain and first node

- **Enable Agent routing**: enable it.
- **Router ID**: enter a stable, unique node ID such as `router-a`. It is 1–64 characters, uses lowercase letters, digits, dots, underscores, or hyphens, and starts and ends with a letter or digit.
- **Agent domain**: enter the private-cloud trust domain, such as `lab.example`. Routers that join the same private cloud and use same-domain admission share this value.

Do not treat Router ID as a temporary hostname. Dynamic Peers, capability origins, and operations records refer to it, so keep it stable after deployment.

## 3. Choose the private-cloud boundary

### One node only

When this is the only Router, leave LAN discovery and Relay disabled. Agents can still register, publish capabilities, and invoke each other through this Router.

### Several nodes on one LAN

- **Discover Agent routers on LAN**: discovers other Nexus Routers.
- **Publish this router on LAN**: makes this node discoverable.
- **LAN admission**: start with `Manual approval`; move to `same-domain` or `allowlist` only after identity validation.

DNS-SD creates Router candidates only. It neither discovers individual Agents nor creates capability routes by itself.

### Nodes behind NAT

Enable **Connect through Nexus Directory and Relay** only when an operator supplies a Directory assignment URL and cross-NAT or cross-site access is required. Configure up to four ordered HTTPS failover URLs.

## 4. Save and verify the private-cloud control plane

Select **Save & Apply**, then open **Overview**. Confirm at least:

- **Recovery** is Healthy.
- LAN discovery and Relay match the chosen boundary.
- No “status is unavailable” banner appears.
- Zero ARPX sessions and Relay tunnels is normal for a one-node private cloud.

If Recovery is Degraded, inspect Last error under Recovery domains and run [Collect diagnostics](../troubleshooting/diagnostics.md).

## 5. Join the first Agent

Enable Python SDK registration and Agent invocation under **Agent APIs & Protocols**, then publish an Agent with the [Python SDK quickstart](/sdk/quickstart/first-agent).

Completion means:

1. The Agent lease appears under **Local Agents**.
2. Its intent appears under **Capability Routes**.
3. A real caller receives a response; a green status card alone is not enough.

## 6. Extend private-cloud node roles

Keep **Node only** for normal nodes. Select **Node + Relay** to carry traffic for other sites, or **Node + Directory** to assign trusted Relays. See [Configure private-cloud node roles](../guides/router-roles.md).

Next, use the [communication mode selector](../communication/model.md) to add LAN Peers, per-Agent IPv6, public ingress, SVCB, or NAT Relay only when needed.
