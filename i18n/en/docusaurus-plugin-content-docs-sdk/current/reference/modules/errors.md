---
title: "errors API"
---

# errors API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusAgentError`

Bases: `Exception`. Inherited behavior is defined on the base class.

Base SDK error.


## `NexusSecurityConfigurationError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

The local SDK security profile is missing or invalid.


## `NexusAuthDiscoveryError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

Router or OIDC authentication metadata is unavailable or invalid.


## `NexusTokenAcquisitionError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

A short-lived access token could not be acquired safely.


## `NexusHttpError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

Agent Access Proxy returned a non-success HTTP response.

### `NexusHttpError.__init__`

```text
NexusHttpError.__init__(self, status: int, code: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `status` | `int` | `required` |
| `code` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py#L20)


## `NexusAuthenticationError`

Bases: `NexusHttpError`. Inherited behavior is defined on the base class.

The router rejected or could not validate caller authentication.


## `NexusAuthorizationError`

Bases: `NexusHttpError`. Inherited behavior is defined on the base class.

The authenticated caller lacks permission for this operation.


## `NexusCloudRegistrationError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

The router could not publish this LAN Agent to Nexus Cloud.

### `NexusCloudRegistrationError.__init__`

```text
NexusCloudRegistrationError.__init__(self, state: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `state` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py#L38)

