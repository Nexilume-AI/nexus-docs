---
sidebar_position: 1
title: Two IPv6 Agents calling each other
description: Use only the Python SDK to give two Agents distinct IPv6 addresses and make bidirectional calls.
---

# Two IPv6 Agents calling each other

This tutorial uses only `nexilume`. It creates Agent A and Agent B on one host, leases a global IPv6 `/128` to each, calls B from A by B's address, and calls A from B by A's address. The call path contains no OpenWrt, Router registration, Directory, AFIB, or Relay.

You will see a result like this:

```text
Agent A: [real IPv6 A]:9443
Agent B: [real IPv6 B]:9443
A → B: demo.hello
B → A: demo.hello
```

Complete [installation](../quickstart/installation.md) first. This exercise uses the Host Alias /64 path; see [Linux setup](../guides/linux-ipv6.md) for other address modes.

## What you need

- Python 3.9 or later;
- a global IPv6 `/64` that is genuinely on-link or routed to the host;
- a Linux or Windows host;
- administrator access for the initial `nexus-agent-addressd` setup;
- an isolated network for the cleartext lab. Production security is covered at the end.

:::warning Address requirement
A single provider `/128` is not enough. The SDK cannot manufacture more public address space. `2001:db8::/32` is documentation space and cannot be used for the live exercise.
:::

## Step 1: Install the SDK and prepare the address service

From the source repository:

```bash
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m venv .venv
# Linux: . .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
```

On Linux, use the systemd installer. See [Linux IPv6 setup](../guides/linux-ipv6.md) for prerequisites and the 0.46.2 fix:

```bash
nexus-agent ipv6 setup
nexus-agent ipv6 doctor
```

On Windows, one command performs discovery, UAC elevation, service installation, and a temporary `/128` self-test:

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

After the user is first added to `Nexus Agent Users`, sign out and back in once. Then verify the non-administrator path:

```powershell
nexus-agent ipv6 doctor
```

## Step 2: Run the SDK-only two-Agent example

The example deliberately uses cleartext HTTP and no JWT on an isolated lab network. Enable the explicit guard and run it.

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

You now have the first visible result. `agent_a.ipv6` and `agent_b.ipv6` must differ, while both Agents may use port `9443`.

## Step 3: Understand address allocation

The example calls the same factory for each Agent:

```python
agent_a = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="agent-a",
    port=9443,
)
```

- `"auto"` requests an address from local `addressd` instead of hard-coding a `/128`;
- `address_mode="host-alias"` explicitly selects one address per Agent;
- `agent_id` forms `agent://demo/agent-a` and participates in stable allocation;
- both Agents may use `port=9443` because their IPv6 addresses differ;
- `auth="none"` is only for this isolated exercise.

`start()` binds the listener, confirms the lease, and renews it. Leaving the context closes the listener and releases the `/128`.

## Step 4: Understand A to B and B to A

The caller uses the exact target IPv6 address:

```python
target_b = DirectIPv6Agent.plain_http(
    agent_b.address,
    port=agent_b.endpoint.port,
)

reply = target_b.invoke(
    "demo.hello",
    {"message": "hello from Agent A"},
    tenant="demo",
    source_agent=agent_a.origin,
)
```

There is no capability discovery here. `DirectIPv6Agent` already knows the target `/128`, port, and capability, so it sends a Nexus Envelope directly. The reverse call changes the target to `agent_a.address` and the caller to `agent_b.origin`.

One process keeps the first exercise easy to run. The same server and client APIs apply when the Agents run in separate processes or on separate hosts. Configuration, an Agent Card, DNS SVCB, or a trusted directory must then deliver the target address to the caller.

## Step 5: Verify that no Router was used

The example should contain none of these:

- `NEXUS_ROUTER_URL`;
- a Router registration token;
- a LuCI capability route;
- an AFIB, Directory, or Relay address.

Inspect the addresses while the program is running:

Linux:

```bash
ip -6 address show dev eth0
```

Windows:

```powershell
Get-NetIPAddress -AddressFamily IPv6
```

After the program exits, both leased `/128` addresses should be gone.

## Harden a production deployment

The cleartext lab exposes the Envelope, request, and response to the network. At minimum, a production deployment should:

1. configure `cert_file`, `key_file`, `tls_server_name`, and `ca_bundle_id` on the called Agent;
2. use `HmacJwtServerAuth` or an integration-provided `ServerAuthPolicy`;
3. configure certificate identity, CA trust, and a short-lived token in `DirectIPv6Agent(...)`;
4. restrict the ingress port and source prefixes with the host firewall;
5. keep HS256 secrets and tokens out of source code.

If you need centralized TLS/JWT enforcement, capability selection, cross-site discovery, and NAT Relay, use [Configure an Agent private cloud network](/openwrt/getting-started/quick-setup). One Agent can still have one IP; only the address and policy owner changes from the Agent host to OpenWrt.

## Troubleshooting

| Symptom | Cause | Action |
| --- | --- | --- |
| `no usable global on-link IPv6 /64` | no usable `/64`, or wrong interface | specify the real interface and canonical `/64` |
| `address must be a global IPv6 address` | ULA, loopback, or documentation address | use a real global IPv6 prefix |
| `host IPv6 address quota is full` | address-service quota exhausted | stop unused Agents or have an administrator change the quota |
| `cannot bind [IPv6]:9443` | address not owned, port restricted, or policy conflict | run doctor and inspect the address and port |
| remotely unreachable but local calls work | upstream route, NDP, or firewall issue | test routing and TCP from another host |

## What you built

You created two independent Agent network identities with one SDK process, called each Agent through its own IPv6 `/128`, and released both addresses on exit. Continue with [Why every Agent should have an IP](../concepts/one-agent-one-ip.md) for the identity model or [Direct IPv6 Agents](../guides/direct-ipv6.md) for fixed addresses, TLS, and JWT.
