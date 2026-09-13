---
sidebar_position: 1
title: Give every Agent an IPv6 address
description: Use SDK Host Alias to obtain a dedicated IPv6 address without configuring a Router.
---

# Give every Agent an IPv6 address

This quickstart does not begin by registering with a router. It first proves the most visible Nexus capability: **every Agent can have its own IPv6 address**. SDK Host Alias leases two different `/128` addresses to two Agents on one host, and both may use port `9443`.

## 1. Check the requirement

You need Python 3.9+ and a global IPv6 `/64` that is genuinely on-link or routed to the host. A single provider `/128`, a ULA, or the `2001:db8::/32` documentation prefix cannot run this exercise.

## 2. Install

```bash
cd sdk/nexus-agent-sdk-python
python -m venv .venv
python -m pip install -e .
```

Windows needs the extra components:

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

On Linux, an administrator starts `nexus-agent-addressd` in a separate terminal with the real interface and `/64`:

```bash
sudo nexus-agent-addressd --interface eth0 --prefix 240e:1234:5678:1200::/64
```

## 3. Understand the key code

Each Agent independently requests an `"auto"` address:

```python
from nexus_agent import NexusAgent

agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="agent-a",
    port=9443,
)
```

`nexus-agent-addressd` performs the restricted interface operation. The ordinary Python process holds only a lease. `auth="none"` is for an isolated lab network only.

## 4. Run and verify

Linux/macOS:

```bash
export NEXUS_IPV6_LAB=1
python examples/ipv6_agents_call_each_other.py
```

Windows PowerShell:

```powershell
$env:NEXUS_IPV6_LAB = '1'
python examples/ipv6_agents_call_each_other.py
```

`agent_a.ipv6` and `agent_b.ipv6` in the output should be two different global IPv6 addresses. On exit, the SDK stops both listeners, releases both leases, and removes both `/128` addresses.

Next: [Make two IPv6 Agents call each other](call-first-agent.md). For line-by-line explanation, cross-host deployment, and production hardening, use the [full tutorial](../tutorials/ipv6-agents-call-each-other.md).
