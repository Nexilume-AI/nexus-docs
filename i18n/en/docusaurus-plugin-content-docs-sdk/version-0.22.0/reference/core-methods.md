---
sidebar_position: 1
title: Core classes and methods
description: Method-level reference for NexusAgent, NexusAgentClient, NexusAgentServer, and IPv6 runtimes.
---

# Core classes and methods

This page covers the main SDK 0.22.0 runtime methods. Signatures are statically extracted from source with Griffe. See [Python API reference](api.md) for all top-level exports.

## `NexusAgent`

The high-level entry point combines a server, client, capability registration, lease renewal, and shutdown cleanup.

```python
NexusAgent(
    *, router: str = "auto", token: str | None = None,
    token_provider: TokenProvider | None = None,
    auth: str | TokenProvider | None = None,
    transaction_token: str | None = None,
    tenant: str = "default", agent_id: str | None = None,
    listen_host: str = "auto", port: int = 0,
    advertise_address: str = "auto", path: str = "/invoke",
    router_ca_file: str | None = None,
    router_cert_file: str | None = None,
    router_key_file: str | None = None,
    router_tls_server_name: str | None = None,
    cert_file: str | None = None, key_file: str | None = None,
    client_ca_file: str | None = None,
    server_tls_name: str = "auto", server_ca_bundle_id: str = "system",
    lease_seconds: int = 300, timeout: float = 10.0,
)
```

| Method | Key parameters and result |
| --- | --- |
| `capability(intent, *, public_ipv6=True, origin=None, version=1, region="local", lease_seconds=None, cost_microunits=0, latency_ms=0, trust=50, pass_envelope=False)` | Normal handler decorator; returns the original handler |
| `stream_capability(...)` | Streaming decorator with the same routing metadata |
| `registrations()` | Returns `tuple[CapabilityRegistration, ...]` without starting |
| `invoke(intent, payload, *, target_agent=None, intent_version=1, task_id=None, hop_limit=8, constraints=None)` | Routed call returning a mapping |
| `invoke_stream(..., resume=True, last_event_id=0, max_reconnects=3, reconnect_delay=0.25)` | Returns `Iterator[SseEvent]`; resume is on by default |
| `start(*, auto_renew=True, renew_fraction=0.6, announce=True, print_fn=print)` | Starts in the background and returns `NexusAgentHandle` |
| `run(**start_options)` | Blocks and returns the published capability tuple |
| `public_ipv6(address, **options)` | Class method creating a `PublicIPv6Agent` |

Do not casually combine `token`, `token_provider`, `auth`, and `transaction_token`. A one-time transaction token cannot resume a stream.

## `NexusAgentClient`

```python
NexusAgentClient(
    base_url: str, *, token: str | None = None,
    token_provider: TokenProvider | None = None,
    transaction_token: str | None = None,
    ca_file: str | None = None, cert_file: str | None = None,
    key_file: str | None = None, tls_server_name: str | None = None,
    use_environment_proxy: bool = True, timeout: float = 10.0,
    user_agent: str = "nexus-agent-sdk-python/0.22.0",
)
```

| Method | Behavior |
| --- | --- |
| `register(registration, *, auto_renew=False, renew_fraction=0.6, health_check=None, reregister_on_not_found=True)` | Returns `AgentLease`; can auto-renew and re-register after 404 |
| `renew(route_id, *, lease_seconds=None, latency_ms=None, load_permille=None, healthy=None, backend_tls=None)` | Updates lease and health metadata; returns `LeaseInfo` |
| `unregister(route_id)` | Withdraws a route; returns `LeaseInfo` |
| `route(envelope)` | Performs route selection only |
| `invoke(envelope)` | Sends a complete Envelope |
| `invoke_intent(intent, payload, *, tenant, source_agent, target_agent=None, intent_version=1, task_id=None, hop_limit=8, constraints=None)` | Builds and invokes an Envelope |
| `invoke_stream(envelope, *, resume=True, last_event_id=0, max_reconnects=3, reconnect_delay=0.25)` | SSE iterator; reconnects up to three times by default |

## `AgentLease`

| Member | Behavior |
| --- | --- |
| `route_id` | Current route ID; it can change after re-registration |
| `public_ipv6` | Router-assigned public IPv6 or `None` |
| `public_endpoint` | Public endpoint with TLS identity or `None` |
| `renew(**updates)` | Manual renewal; healthy routes re-register after 404 by default |
| `start_auto_renew()` | Starts the renewal thread and returns itself |
| `close(unregister=True)` | Stops renewal and withdraws the route by default |

Context-manager exit calls `close()`.

## `NexusAgentServer`

```python
NexusAgentServer(
    host: str = "127.0.0.1", port: int = 0, *, path: str = "/invoke",
    stream_path: str | None = None, auth: ServerAuthPolicy | None = None,
    cert_file: str | None = None, key_file: str | None = None,
    client_ca_file: str | None = None, address_family: str = "auto",
    dual_stack: bool = False, max_request_bytes: int = 65536,
    max_response_bytes: int = 262144, max_stream_event_bytes: int = 65536,
    request_timeout: float = 15.0, resumable_streams: bool = True,
    resume_max_tasks: int = 128, resume_max_events: int = 256,
    resume_max_history_bytes: int = 262144,
    resume_retention_seconds: float = 300.0,
)
```

| Method | Behavior |
| --- | --- |
| `add_handler(intent, handler, *, stream_handler=None)` | Registers a handler explicitly |
| `handler(intent)` / `stream_handler(intent)` | Normal and streaming decorators |
| `remove_handler(intent)` / `has_handler(intent)` | Mutates or queries the handler table |
| `serve_forever(poll_interval=0.25)` | Blocks in the current thread |
| `serve_in_thread(daemon=True)` | Returns a background thread |
| `is_healthy()` | True when the service thread and socket are usable |
| `shutdown()` / `server_close()` | Stops the loop / closes the socket |
| `registered(client, registrations, *, auto_renew=True, renew_fraction=0.6, health_check=None, reregister_on_not_found=True)` | Registration context that closes leases on exit |
| `serve_registered(...)` | Registers and then serves forever |

Defaults are 64 KiB per request, 256 KiB per response, and 64 KiB per stream event. Oversized data fails before business processing.

## Direct IPv6

### `DirectIPv6Agent`

The constructor defaults to HTTPS and a ten-second timeout and accepts only IPv6 addresses without a zone ID. Main methods:

- `from_endpoint(endpoint, **credentials)`: construct from `PublicAgentEndpoint`.
- `plain_http(address, *, token=None, token_provider=None, transaction_token=None, port=7443, timeout=10.0)`: explicit cleartext mode; rejects TLS arguments.
- `invoke(..., tenant, source_agent, hop_limit=8, constraints=None)`: direct call.
- `invoke_stream(..., resume=True, max_reconnects=3)`: direct SSE call.

### `PublicIPv6Agent`

The default port is 9443, the address lease is 300 seconds, and request/response limits match `NexusAgentServer`. `auth` is required. Use `capability()`, `stream_capability()`, `start()`, and `run()`.

Do not use `plain_http()` or `NoServerAuth` in production. See [Direct IPv6 agents](../guides/direct-ipv6.md).
