---
sidebar_position: 3
title: LuCI interface tour
---

# LuCI interface tour

The illustrations below are drawn from the current LuCI source. They are not screenshots from a running device. Fields, menus, and status cards match `luci-app-agent-router 3.1.0`; theme, language, and viewport change the actual appearance.

## Quick Setup: configure the Agent private cloud

![LuCI Quick Setup illustration](/img/openwrt/luci-quick-setup.svg)

Quick Setup is the actual LuCI entry for creating the private-cloud network. First-time users need four groups:

1. **Identity and service**: enable routing; Agent domain defines the private-cloud trust domain and Router ID identifies this node.
2. **LAN discovery**: choose whether to discover and publish other LAN nodes.
3. **LAN admission**: select manual approval, same-domain trust, or an allowlist.
4. **Cross-network Relay**: enable it only when a Directory operator supplies an assignment URL and NAT traversal is required.

A Router ID is 1–64 characters, uses lowercase letters, digits, dots, underscores, or hyphens, and starts and ends with a letter or digit.

## Overview: verify the private-cloud node

![LuCI Overview illustration](/img/openwrt/luci-overview.svg)

Green does not prove every business call succeeds, but it confirms usable control-plane state:

- **AFIB routes**: selectable capability routes.
- **ARPX sessions**: connected private-cloud node Peers.
- **LAN candidates**: discovered nodes awaiting or receiving admission.
- **Relay tunnels**: cross-NAT Relay tunnels.
- **Public Agent IPv6**: Router-managed public IPv6 leases.
- **Recovery**: successful UCI load; inspect Last error when Degraded.

The page polls bounded metadata every five seconds. It does not read prompts, tool arguments, model output, access tokens, or task bodies.

## Next step

- One-node private cloud: [publish your first Agent](/sdk/quickstart/first-agent).
- Extend the private cloud: [connect two Routers](../tutorials/two-router.md).
- Degraded state: [collect diagnostics](../troubleshooting/diagnostics.md).
