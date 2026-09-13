---
sidebar_position: 3
title: Direct IPv6 Agents
description: Publish an Agent with a fixed address or Host Alias and invoke it by literal IPv6.
---

# Direct IPv6 Agents

Direct mode has two classes. `NexusAgent.public_ipv6(...)` publishes capabilities on a global IPv6 address owned by the Agent host. `DirectIPv6Agent` invokes a known literal IPv6 target. Neither requires OpenWrt registration, AFIB selection, Directory, or Relay.

## One Agent, one IP with Host Alias

When the host has a genuinely usable `/64` and `nexus-agent-addressd` is configured, let the SDK lease a `/128`:

```python
from nexus_agent import NexusAgent

agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="echo-1",
    port=9443,
)

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

agent.run()
```

After `start()` succeeds, `agent.address` contains the compressed IPv6 address and `agent.endpoint` contains the scheme, address, port, and URL. Closing `PublicIPv6AgentHandle` stops the server and releases the address lease.

## Use an existing host address

If the global IPv6 address already belongs to the host, pass it explicitly and keep the required `auth` argument:

```python
agent = NexusAgent.public_ipv6(
    "240e:1234:5678:1200::20",
    address_mode="existing",
    auth="none",
    tenant="demo",
    agent_id="echo-1",
    port=9443,
)
```

The SDK binds the existing address. It does not add an address, change the firewall, or discover peers. The address must have no `%scope`, must be considered global by Python `ipaddress`, and must belong to the host.

## Cleartext calls on an isolated lab network

```python
from nexus_agent import DirectIPv6Agent

target = DirectIPv6Agent.plain_http(
    "240e:1234:5678:1200::20",
    port=9443,
)
result = target.invoke(
    "demo.echo",
    {"message": "hello"},
    tenant="demo",
    source_agent="agent://demo/caller-a",
)
```

`plain_http()` is explicit. The SDK never downgrades after an HTTPS failure. Cleartext exposes tokens, Envelopes, and business data, so use it only in an isolated lab.

## HTTPS and JWT calls

The server uses a certificate and publishes a stable DNS TLS identity:

```python
import os
from nexus_agent import HmacJwtServerAuth, NexusAgent

auth = HmacJwtServerAuth(
    os.environ["NEXUS_AGENT_JWT_SECRET"],
    issuer="https://issuer.private.example",
    audience="echo-agent",
)
agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth=auth,
    tenant="demo",
    agent_id="echo-1",
    port=9443,
    cert_file="agent-fullchain.pem",
    key_file="agent-key.pem",
    tls_server_name="echo-1.private.example",
    ca_bundle_id="private-agent-ca",
)
```

The caller opens TCP to the literal IPv6 address but uses the stable DNS identity for SNI and certificate-name verification:

```python
target = DirectIPv6Agent(
    "240e:1234:5678:1200::20",
    port=9443,
    server_identity="echo-1.private.example",
    token=short_lived_jwt,
    ca_file="private-agent-ca.pem",
)
result = target.invoke(
    "demo.echo",
    {"message": "secure hello"},
    tenant="demo",
    source_agent="agent://demo/caller-a",
)
```

`HmacJwtServerAuth` validates only HS256 shared-secret tokens, including issuer, audience, lifetime, `agent.invoke` scope, tenant, and `source_agent`. It is not OIDC/JWKS validation. Cross-organization deployments need an appropriate server policy and key management.

## Discovery versus direct calls

`DirectIPv6Agent` does not discover a target. Configuration, an Agent Card, DNS SVCB, or a trusted Directory must deliver the address, port, TLS identity, and CA label. Discovery answers where to connect. TLS and JWT answer whether the peer is trusted and authorized.

The client disables environment HTTP proxies so a literal IPv6 request cannot silently leave the direct path. An unreachable target fails directly and does not fall back to Router or Relay.

## Key parameters

### `NexusAgent.public_ipv6(address, ...)`

| Parameter | Constraint / default | Purpose |
| --- | --- | --- |
| `address` | global IPv6 or `"auto"` | bind an existing address or request Host Alias |
| `auth` | required; `"none"` or `ServerAuthPolicy` | server-side caller authentication |
| `port` | `9443`, range 1–65535 | listener port |
| `address_mode` | `"auto"`, `"existing"`, `"host-alias"` | address source; Host Alias requires `address="auto"` |
| `interface` / `prefix` | `"auto"` | constrain the addressd lease request |
| `address_lease_seconds` | `300` | Host Alias lease lifetime |
| `cert_file` / `key_file` | used together | enable HTTPS |
| `tls_server_name` / `ca_bundle_id` | required with HTTPS | publish stable certificate identity and CA label |

### `DirectIPv6Agent(address, ...)`

| Parameter | Constraint / default | Purpose |
| --- | --- | --- |
| `address` | literal IPv6, no scope ID | TCP destination |
| `scheme` | `"https"` | `https`, or explicit `http` |
| `server_identity` | required for HTTPS unless a security profile resolves it | SNI and certificate-name verification |
| `port` | HTTPS default `7443` | target port; Host Alias examples explicitly use `9443` |
| `token` / `token_provider` | mutually exclusive | invocation credential |
| `ca_file`, `cert_file`, `key_file` | optional | CA trust and caller mTLS |
| `timeout` | `10.0` seconds | request timeout |

Run [Two IPv6 Agents calling each other](../tutorials/ipv6-agents-call-each-other.md), then read [Authentication](authentication.md). See the [address ownership model](/openwrt/communication/addressing) for OpenWrt-managed addresses.
