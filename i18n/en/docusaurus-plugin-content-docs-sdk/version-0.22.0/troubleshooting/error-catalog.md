---
sidebar_position: 0
title: Error codes and recovery
---

# Error codes and recovery

Catch the most specific exception first. The SDK maps HTTP 401 to `NexusAuthenticationError`, 403 to `NexusAuthorizationError`, and other structured failures to `NexusHttpError`.

```python
from nexus_agent import (
    NexusAuthenticationError,
    NexusAuthorizationError,
    NexusHttpError,
)

try:
    result = client.invoke_intent(...)
except NexusAuthenticationError:
    # Refresh or reacquire credentials; do not retry one token forever.
    raise
except NexusAuthorizationError:
    # Inspect tenant, scope, capability, and policy.
    raise
except NexusHttpError as error:
    print(error.status, error.code, error.message)
```

## Common structured errors

| HTTP / code | Meaning | User action |
| --- | --- | --- |
| 401 / `AUTHENTICATION_REQUIRED` | Credential is missing, expired, or invalid | Check token source, issuer, audience, and device time |
| 403 / `INSUFFICIENT_SCOPE` | Identity is valid but scope is insufficient | Grant only the required route/invoke permission |
| 404 / route not found | Lease or capability route does not exist | Inspect Local Agents, Capability Routes, and Policy RIB |
| 422 / `INPUT_REJECTED` | Agent business handler rejected input | Correct the payload from the message; do not repeat it unchanged |

The exact code string comes from the gateway or agent. Record `status`, `code`, `message`, task ID, and incident time, never the token.

## Recovery behavior proven by tests

- A refreshable token provider refreshes once after 401, then retries once.
- A healthy lease that receives 404 during renewal re-registers by default and gets a new `route_id`.
- A lease renewed with `healthy=False` does not re-register after 404.
- Failed local health checks withdraw the route and stop auto-renewal.
- After a clean SSE disconnect, the client resumes with `Last-Event-ID` without re-executing the task.
- A transaction token is one-time and cannot resume a stream.

## Parameter validation errors

These raise `ValueError` before any network request:

- `target_agent=""`.
- Access token and transaction token supplied together.
- `tls_server_name` used with an HTTP URL.
- IPv4, hostname, or a scoped link-local value passed to `DirectIPv6Agent`.
- CA or certificate arguments supplied to cleartext direct IPv6 mode.

## Next step

Run [SDK diagnostics](diagnostics.md), then use [Authentication](../guides/authentication.md), [Streaming calls](../guides/streaming.md), or [Direct IPv6](../guides/direct-ipv6.md) based on the exception.
