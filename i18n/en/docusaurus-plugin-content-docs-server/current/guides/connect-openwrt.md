---
sidebar_position: 2
title: How to connect an OpenWrt IPv6 Agent
---

# How to connect an OpenWrt IPv6 Agent

After pairing, an Agent can run on user-owned OpenWrt IPv6 instead of a rented Docker host.

## Prerequisites

The router has Nexus packages and global IPv6; the Server is reachable and production mTLS/Edge keys are configured; your Nexus role can register private Routers.

## Steps

1. Open **Workspace → OpenWrt Routers**, select **Register Router**, choose a Project or the whole Workspace, and create a one-time pairing code. The Router is private to the user identity that created the code.
2. Enter the Server URL and code on OpenWrt. Prefer a managed device certificate: the router creates its private key and CSR locally; the Server returns only the signed certificate.
3. Wait for the router to publish an Agent registration. The Server accepts numeric global IPv6, a valid TLS server name, allowed ports, and increasing generations.
4. Open an Agent, choose **OpenWrt IPv6**, and bind an available registration from one of your Routers. The Agent and a Project-scoped Router must share a Project; a Workspace Router may serve your Agents in any Project.
5. Run a health check or MCP call. The cloud connects to the IPv6 address while verifying TLS SNI and hostname against the registered server name.

## Verification

The Router appears online under **Workspace → OpenWrt Routers** with a confirmed certificate; the registration becomes an active Agent deployment; runtime type is `openwrt_ipv6` and no container id exists.

For failures, verify global IPv6, lease renewal, firewall, SNI, `ca_bundle_id`, and the reverse proxy's verified client-certificate header. See the [OpenWrt quick setup](/openwrt/getting-started/quick-setup) and [configuration reference](../reference/configuration.md).
