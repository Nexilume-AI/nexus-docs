---
title: "server_auth API"
---

# server_auth API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `ServerAuthenticationError`

Bases: `Exception`. Inherited behavior is defined on the base class.

Authentication failure suitable for a bounded HTTP response.

### `ServerAuthenticationError.__init__`

```text
ServerAuthenticationError.__init__(self, code: str, message: str, *, status: int=401) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `code` | `str` | `required` |
| `message` | `str` | `required` |
| `status` | `int` | `401` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L17)


## `AuthenticatedCaller`

| Field | Type | Default |
| --- | --- | --- |
| `subject` | `Optional[str]` | `required` |
| `scopes` | `Tuple[str, ...]` | `()` |
| `claims` | `Mapping[str, Any]` | `field(default_factory=dict)` |


## `ServerAuthPolicy`

Bases: `Protocol`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `mode` | `str` | `required` |

### `ServerAuthPolicy.authenticate`

```text
ServerAuthPolicy.authenticate(self, authorization: Optional[str], envelope: AgentEnvelope) -> AuthenticatedCaller
```

| Parameter | Type | Default |
| --- | --- | --- |
| `authorization` | `Optional[str]` | `required` |
| `envelope` | `AgentEnvelope` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L34)


## `NoServerAuth`

Explicitly accept direct calls without an Authorization header.

### `NoServerAuth.authenticate`

```text
NoServerAuth.authenticate(self, authorization: Optional[str], envelope: AgentEnvelope) -> AuthenticatedCaller
```

| Parameter | Type | Default |
| --- | --- | --- |
| `authorization` | `Optional[str]` | `required` |
| `envelope` | `AgentEnvelope` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L47)


## `HmacJwtServerAuth`

Dependency-free HS256 validation for a self-hosted direct Agent.

This mode is intended for deployments where the caller and Agent share a
dedicated 256-bit secret. OIDC/JWKS asymmetric validation remains a future
server policy rather than silently treating an access token as trusted.

### `HmacJwtServerAuth.__init__`

```text
HmacJwtServerAuth.__init__(self, secret: str, *, issuer: str, audience: str, required_scope: str='agent.invoke', clock_skew_seconds: int=30, max_lifetime_seconds: int=3600, bind_tenant: bool=True, bind_source_agent: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `secret` | `str` | `required` |
| `issuer` | `str` | `required` |
| `audience` | `str` | `required` |
| `required_scope` | `str` | `'agent.invoke'` |
| `clock_skew_seconds` | `int` | `30` |
| `max_lifetime_seconds` | `int` | `3600` |
| `bind_tenant` | `bool` | `True` |
| `bind_source_agent` | `bool` | `True` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L95)

### `HmacJwtServerAuth.authenticate`

```text
HmacJwtServerAuth.authenticate(self, authorization: Optional[str], envelope: AgentEnvelope) -> AuthenticatedCaller
```

| Parameter | Type | Default |
| --- | --- | --- |
| `authorization` | `Optional[str]` | `required` |
| `envelope` | `AgentEnvelope` | `required` |

Direct raises (not exhaustive): `ServerAuthenticationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L124)

### `HmacJwtServerAuth.issue`

```text
HmacJwtServerAuth.issue(self, *, subject: str, tenant: str, source_agent: str, expires_in: int=300, scopes: Tuple[str, ...]=('agent.invoke',), now: Optional[int]=None) -> str
```

Issue a bounded HS256 token for local/testing deployments.

| Parameter | Type | Default |
| --- | --- | --- |
| `subject` | `str` | `required` |
| `tenant` | `str` | `required` |
| `source_agent` | `str` | `required` |
| `expires_in` | `int` | `300` |
| `scopes` | `Tuple[str, ...]` | `('agent.invoke',)` |
| `now` | `Optional[int]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py#L202)

