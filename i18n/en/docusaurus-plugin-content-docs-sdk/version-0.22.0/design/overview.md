---
title: Design an Agent with the SDK
sidebar_position: 0
---

# Design an Agent with the SDK

Start with the input, output and permitted actions, then choose where the Agent runs. The SDK provides protocols, identity, routing and Run resource access. Your application owns model calls, validation, decisions and idempotency for external effects.

## Turn a requirement into a contract

For a document inspector, first return character, word and line counts. Add progress next, then file inputs, confirmation or Computer actions only when needed. Avoid starting with an unrestricted filesystem or arbitrary-command tool.

| Design question | SDK concept |
| --- | --- |
| What does the Agent do? | Intent and function declared with `@agent.capability` |
| How does the caller provide input? | `McpToolDescriptor.input_schema`, plus application validation |
| What does a model see? | Tool name, description and input schema |
| What is returned? | JSON-serializable result, or `SseEvent` for streaming |
| Where does it run? | OpenWrt registration, hosted MCP or direct IPv6 |
| Does it need caller resources? | Computer/Mobile declarations and caller authorization |
| How is progress exposed? | `NexusRunContext` Plan, Trace, Chat and Output |
| How does interrupted work recover? | Checkpoint, Recovery and application idempotency keys |

## Learning path

1. [Declare and test a business Agent](capabilities.md), with a complete downloadable example.
2. [Design interaction and long tasks](interaction.md): Plan, Chat, streaming, follow-up and cancellation.
3. [Use caller resources](resources.md): Run files, Computer workspace, browser and Mobile.
4. [State, recovery and cost](state-and-usage.md): Memory, Checkpoint, external operations, usage and billing.
5. [Detailed API reference](../reference/coverage.md): parameters, types, results, fields and source locations.

## Choose a runtime

| Runtime | Use case | Prerequisite |
| --- | --- | --- |
| `NexusAgentServer` | Local HTTP/SSE or an existing service | Python; no Cloud |
| `NexusAgent(runtime="openwrt")` | LAN services and routed calls | Reachable Agent Access Proxy |
| `NexusAgent(runtime="hosted")` | Self-managed MCP or a Cloud container | `fastmcp`; trusted Run for Cloud features |
| `NexusAgent.public_ipv6(...)` | Direct address-based calls | Working IPv6 and authentication |

`runtime="auto"` uses the edge workflow unless a trusted Cloud launcher selects hosted before import. Discovery failure never switches it to hosted. Keep the Agent and business functions at module scope and `agent.run()` inside the `__main__` guard to reuse an uploaded file.

## Validate three layers

Test business logic first, then actual HTTP/MCP invocation, then authorization, resources and restart recovery in a real Cloud Run. A local test without Cloud cannot establish Caller Computer, billing or Mobile availability. The SDK does not supply a model, model credentials or permission to modify external systems.
