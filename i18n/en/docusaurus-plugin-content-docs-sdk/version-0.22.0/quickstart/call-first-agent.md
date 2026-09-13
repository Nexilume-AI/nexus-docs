---
sidebar_position: 2
title: Make two IPv6 Agents call each other
description: Use DirectIPv6Agent to call A to B and B to A by exact target IPv6 address.
---

# Make two IPv6 Agents call each other

After the [address quickstart](first-agent.md), each Agent owns a `/128`. No Router lookup is required. The caller gives the target IPv6 address to `DirectIPv6Agent`, then sends a capability and Nexus Envelope.

## 1. Agent A calls Agent B

```python
from nexus_agent import DirectIPv6Agent

target_b = DirectIPv6Agent.plain_http(
    agent_b.address,
    port=agent_b.endpoint.port,
)

a_to_b = target_b.invoke(
    "demo.hello",
    {"message": "hello from Agent A"},
    tenant="demo",
    source_agent=agent_a.origin,
)
```

`agent_b.address` is the destination network identity. `source_agent=agent_a.origin` is the caller's logical identity in the Envelope. They do not replace each other.

## 2. Agent B calls Agent A

```python
target_a = DirectIPv6Agent.plain_http(
    agent_a.address,
    port=agent_a.endpoint.port,
)

b_to_a = target_a.invoke(
    "demo.hello",
    {"message": "hello from Agent B"},
    tenant="demo",
    source_agent=agent_b.origin,
)
```

Running `examples/ipv6_agents_call_each_other.py` executes both directions and prints both addresses and real JSON responses.

## 3. What is absent from this entry example

- no `NEXUS_ROUTER_URL`;
- no OpenWrt configuration;
- no Router registration, capability route, or AFIB;
- no Directory, Relay, or NAT traversal;
- no automatic discovery, because the example passes the target address directly.

That is the SDK-only direct path. The API remains the same across processes or hosts. Use trusted configuration, an Agent Card, DNS SVCB, or a directory to deliver the target address.

## 4. Do not expose the lab mode to the Internet

`plain_http()` and server-side `auth="none"` transmit requests in cleartext and do not authenticate the caller. They are only for an isolated lab. Production uses HTTPS `DirectIPv6Agent(...)`, trusted CA material, short-lived tokens, a server authentication policy, and source-restricted firewall rules.

Continue with [Two IPv6 Agents calling each other](../tutorials/ipv6-agents-call-each-other.md) for environment setup, verification, troubleshooting, and hardening. See [Direct IPv6 Agents](../guides/direct-ipv6.md) for API details.
