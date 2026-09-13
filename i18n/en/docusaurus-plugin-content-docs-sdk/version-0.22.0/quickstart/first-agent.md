---
sidebar_position: 1
title: Give every Agent an IPv6 address
description: Use SDK Host Alias to obtain a dedicated IPv6 address without configuring a Router.
---

# Give every Agent an IPv6 address

This quickstart does not begin by registering with a router. It first proves the most visible Nexus capability: **every Agent can have its own IPv6 address**. SDK Host Alias leases two different `/128` addresses to two Agents on one host, and both may use port `9443`.

Complete [installation](../quickstart/installation.md) first. This exercise uses the Host Alias /64 path; see [Linux setup](../guides/linux-ipv6.md) for other address modes.

## 1. Check the requirement

You need Python 3.9+ and a global IPv6 `/64` that is genuinely on-link or routed to the host. A single provider `/128`, a ULA, or the `2001:db8::/32` documentation prefix cannot run this exercise.

## 2. Install

```bash
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m venv .venv
# Linux: . .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
```

Windows needs the extra components:

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

On Linux, use the systemd installer. See [Linux IPv6 setup](../guides/linux-ipv6.md) for prerequisites and the 0.46.2 fix:

```bash
nexus-agent ipv6 setup
nexus-agent ipv6 doctor
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

Linux:

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
