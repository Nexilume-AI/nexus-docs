---
slug: /
sidebar_position: 1
title: Python SDK user guide
description: Learn nexus-agent-sdk from one IPv6 address per Agent to resumable calls.
---

# Python SDK user guide

The defining capability of `nexus-agent-sdk` is to make an Agent a directly addressable network node. When a host has a usable IPv6 `/64`, the SDK can give **every Agent its own IPv6 `/128`**, and Agents can call each other by address. The SDK also provides HTTP/SSE servers, Router registration leases, authentication, and FastMCP/A2A integrations. Version **0.22.0** supports Python **3.9+**.

## First run: SDK only

Reach an end-to-end result without configuring OpenWrt:

1. [Give every Agent an IPv6 address](quickstart/first-agent.md).
2. [Make two IPv6 Agents call each other](quickstart/call-first-agent.md).
3. Work through the full [two-Agent tutorial](tutorials/ipv6-agents-call-each-other.md).

This Host Alias path requires a genuinely usable global IPv6 `/64` on the host and local `nexus-agent-addressd`. It bypasses Router, Directory, AFIB, and Relay.

## Structured learning path

1. [Why every Agent should have an IP](concepts/one-agent-one-ip.md): separate logical, network, authentication, and capability identity.
2. [SDK runtime mental model](concepts/runtime-model.md): understand facade, client, server, and lease responsibilities.
3. [Envelope, identity, and authentication](concepts/envelope-auth.md): understand what callers declare and what servers verify.
4. [Registration, renewal, and self-healing](concepts/registration-lifecycle.md): after adding OpenWrt, understand route IDs, health withdrawal, and Router-restart recovery.
5. [Streaming resume design](concepts/streaming-resume.md): understand task, route, request fingerprint, and event cursor.
6. [From echo to a resumable Agent](tutorials/resilient-agent.md): combine sync, SSE, Router leases, and short-disconnect recovery.

## Choose a deployment layer

| Goal | Start here |
| --- | --- |
| Two Agents know each other's address and call directly | [Direct IPv6 Agents](guides/direct-ipv6.md) |
| OpenWrt centrally manages addresses, discovery, routing, and cross-NAT calls | [Configure an Agent private cloud network](/openwrt/getting-started/quick-setup) |
| Integrate tool or Agent protocols | [FastMCP](integrations/fastmcp.md), [A2A](integrations/a2a.md) |
| Look up signatures or diagnose failures | [Core methods](reference/core-methods.md), [error catalog](troubleshooting/error-catalog.md), [diagnostics](troubleshooting/diagnostics.md) |

Runnable examples live in `sdk/nexus-agent-sdk-python/examples/`. The default one-Agent-one-IP entry example is `ipv6_agents_call_each_other.py`.
