---
sidebar_position: 1
title: Why every Agent should have an IP
description: Understand the boundaries between Agent identity, IPv6 identity, authentication, and routing policy.
---

# Why every Agent should have an IP

Traditional services often distinguish processes with one host IP and many ports. Nexus can instead lease a distinct `/128` to every Agent from a genuinely usable IPv6 `/64`. The network-layer destination is then the Agent, not a port on a host.

```text
240e:1234:5678:1200::a1  → agent://demo/agent-a
240e:1234:5678:1200::b1  → agent://demo/agent-b
```

Both Agents may listen on the same port because they bind different IPv6 addresses. Firewall policy, traffic accounting, diagnostics, and future DNS publication become easier to reason about.

## Do not collapse four identities into one

| Layer | Example | Question it answers |
| --- | --- | --- |
| Logical Agent identity | `agent://demo/agent-a` | Who does the Envelope claim is calling? |
| IPv6 network identity | `240e:...::a1/128` | Which Agent receives the packet? |
| TLS/JWT identity | certificate SAN, issuer, audience, scope | Is the peer trusted and authorized? |
| Capability identity | `demo.hello` | What should this request execute? |

A dedicated IPv6 address gives exact addressing, but **reachability is not authorization**. Public or cross-trust-domain deployments still need TLS and an authentication policy. Knowing an IP address is not a credential.

## How SDK-only Host Alias works

```text
Agent process
  └─ NexusAgent.public_ipv6("auto")
       └─ requests a lease over local IPC
            └─ nexus-agent-addressd
                 └─ adds one /128 from the allowed /64
```

`nexus-agent-addressd` is a narrow privileged helper. An administrator configures the allowed interface, `/64`, local users, and quota once. Unprivileged Agent processes can only allocate, confirm, renew, and release their own leases. Stopping an Agent releases its lease and removes the address.

This path needs no OpenWrt Router, Directory, AFIB, Relay, capability registration, or callback mapping. When a caller knows the target IPv6 address and port, `DirectIPv6Agent` connects directly.

## Where the addresses come from

`address="auto"` does not manufacture IPv6 address space. One of these conditions must hold:

- the `/64` is usable on the Agent host's link; or
- an upstream router routes the `/64` to the Agent host.

If a provider gives the host only one `/128`, the SDK cannot expand it into many addresses. Use different ports on one address, or let OpenWrt manage Agent `/128` addresses from an available prefix.

## Two one-Agent-one-IP paths

| Mode | Address owner | Call path | Best fit |
| --- | --- | --- | --- |
| SDK Host Alias | Agent host | direct `DirectIPv6Agent` call | single-host labs, edge hosts, servers with a `/64` |
| Router-managed `/128` | OpenWrt | exact Router ingress and AFIB | centralized admission, routing policy, protocol adaptation, and cross-site governance |

Start with [Two IPv6 Agents calling each other](../tutorials/ipv6-agents-call-each-other.md) to see two real `/128` addresses, then use the [OpenWrt address ownership model](/openwrt/communication/addressing) to choose a production path.
