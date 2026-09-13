---
sidebar_position: 2
title: Publish and invoke Agent APIs
---

# Publish and invoke Agent APIs

An agent registers one or more capabilities with the router. A client discovers a capability and invokes it through the router, which forwards the request to an eligible agent.

## Publish a capability

1. Enable the required endpoint under **Agent APIs & Protocols**.
2. Provision authentication for the agent.
3. Use the SDK to declare capabilities, listener address, and health behavior.
4. Start the agent and wait for registration.
5. Confirm an active lease under **Local Agents** and a route under **Capability Routes**.

Start with [Your first Python agent](/sdk/quickstart/first-agent). For MCP tools, use the [FastMCP integration](/sdk/integrations/fastmcp). For A2A agents, use the [A2A integration](/sdk/integrations/a2a).

## Calls and streaming

A normal call returns one JSON result. Long-running work can return progress and a final result over SSE. Clients should set a timeout, handle authentication errors, and use resume identifiers only when the server advertises support. See [Streaming calls](/sdk/guides/streaming).

## Stop an agent

Let the SDK revoke its lease during an orderly shutdown. After a crash, the router removes routes when the lease expires. Do not use unlimited leases to hide an unavailable agent.
