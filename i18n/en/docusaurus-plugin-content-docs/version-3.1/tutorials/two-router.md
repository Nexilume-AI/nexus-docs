---
sidebar_position: 1
title: Connect two LAN routers
---

# Connect two LAN routers

This tutorial makes a capability on Router A available through Router B. Both routers share one layer-2 LAN, so Relay and Directory are not required.

## What you need

- Two OpenWrt routers running one matching Nexus package batch.
- Administrator access and LAN policy that permits mDNS/umDNS and ARPX sessions.
- At least one local agent registered on Router A.

## 1. Configure Router A

Open **Agent Router → Quick Setup**:

- Enable Agent routing: on
- Router ID: `router-a`
- Agent domain: `lab.example`
- Discover Agent routers on LAN: on
- Publish this router on LAN: on
- LAN admission: `Manual approval`

Save and apply. Overview should report Discovery enabled.

## 2. Configure Router B

Use the same settings, but set Router ID to `router-b`; keep `lab.example` as the domain. Open **Peer Trust**, wait for `router-a`, verify its Router ID and domain, and approve it.

For unattended admission in a lab, set both routers to `Automatically trust same-domain routers`. Before using this in production, make sure the LAN and domain share one administration boundary.

## 3. Verify the session and route

On Router B, confirm:

- ARPX sessions is at least 1.
- Recovery is Healthy.
- Capability Routes contains Router A's capability.

Invoke that capability from Router B's network. A successful response proves discovery, trust, routing, and forwarding.

## Common failures

- **LAN candidate but no ARPX session**: approve the candidate under Peer Trust.
- **Routers do not discover each other**: inspect umDNS, firewall, and layer-2 isolation; guest Wi-Fi commonly blocks discovery.
- **Session is up but no capability route exists**: inspect Router A's local lease and both Policy RIBs.
- **Different sites or NAT**: use [Node + Relay/Directory](../guides/router-roles.md) instead.
