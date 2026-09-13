---
title: "auth API"
---

# auth API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `CloudTrustUnavailableError`

Bases: `OSError`. Inherited behavior is defined on the base class.

The router did not provide trust for a private Cloud certificate.


## `CloudTrustVerificationError`

Bases: `OSError`. Inherited behavior is defined on the base class.

The enrolled router trust could not verify the Cloud peer.


## `CloudTrustOriginError`

Bases: `ValueError`. Inherited behavior is defined on the base class.

A Run context exchange escaped the enrolled Cloud origin.


## `CloudTrustPolicy`

One in-memory, enrollment-scoped Cloud TLS policy.

### `CloudTrustPolicy.__init__`

```text
CloudTrustPolicy.__init__(self, *, mode: str, origin: str='', sha256: str='', ca_pem: str='', ca_file: Optional[str]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `mode` | `str` | `required` |
| `origin` | `str` | `''` |
| `sha256` | `str` | `''` |
| `ca_pem` | `str` | `''` |
| `ca_file` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `NexusTokenAcquisitionError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L106)

### `CloudTrustPolicy.validate_exchange_url`

```text
CloudTrustPolicy.validate_exchange_url(self, url: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `url` | `str` | `required` |

Direct raises (not exhaustive): `CloudTrustOriginError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L159)

### `CloudTrustPolicy.validate_cloud_url`

```text
CloudTrustPolicy.validate_cloud_url(self, url: str) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `url` | `str` | `required` |

Direct raises (not exhaustive): `CloudTrustOriginError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L166)


## `StaticCloudTrustResolver`

Advanced explicit Cloud CA override for non-bootstrap deployments.

### `StaticCloudTrustResolver.__init__`

```text
StaticCloudTrustResolver.__init__(self, ca_file: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `ca_file` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L176)

### `StaticCloudTrustResolver.open_cloud_request`

```text
StaticCloudTrustResolver.open_cloud_request(self, request: urllib.request.Request, *, timeout: float, exchange: bool=False) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `request` | `urllib.request.Request` | `required` |
| `timeout` | `float` | `required` |
| `exchange` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L179)


## `TokenProvider`

Bases: `Protocol`. Inherited behavior is defined on the base class.

Return an access token without persisting it to disk.

### `TokenProvider.refreshable`

```text
TokenProvider.refreshable: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L198)

### `TokenProvider.get_token`

```text
TokenProvider.get_token(self, *, force_refresh: bool=False) -> Optional[str]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L201)


### `resolve_environment_token`

```text
resolve_environment_token(environ: Optional[Mapping[str, str]]=None) -> Optional[str]
```

Read the canonical token variable and bounded legacy aliases.

| Parameter | Type | Default |
| --- | --- | --- |
| `environ` | `Optional[Mapping[str, str]]` | `None` |

Direct raises (not exhaustive): `NexusTokenAcquisitionError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L205)


## `StaticTokenProvider`

Advanced/testing provider for one caller-supplied access token.

### `StaticTokenProvider.__init__`

```text
StaticTokenProvider.__init__(self, token: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `token` | `str` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L238)

### `StaticTokenProvider.get_token`

```text
StaticTokenProvider.get_token(self, *, force_refresh: bool=False) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L243)


## `NoTokenProvider`

Explicitly suppress Agent JWT and transaction-token headers.

### `NoTokenProvider.get_token`

```text
NoTokenProvider.get_token(self, *, force_refresh: bool=False) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L253)


## `EnvironmentTokenProvider`

Compatibility provider using NEXUS_AGENT_TOKEN and legacy aliases.

### `EnvironmentTokenProvider.__init__`

```text
EnvironmentTokenProvider.__init__(self, *, required: bool=True, environ: Optional[Mapping[str, str]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `required` | `bool` | `True` |
| `environ` | `Optional[Mapping[str, str]]` | `None` |

Direct raises (not exhaustive): `NexusTokenAcquisitionError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L263)

### `EnvironmentTokenProvider.get_token`

```text
EnvironmentTokenProvider.get_token(self, *, force_refresh: bool=False) -> Optional[str]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L275)


## `RouterBootstrapMetadata`

| Field | Type | Default |
| --- | --- | --- |
| `type` | `str` | `required` |
| `endpoint` | `str` | `required` |
| `token_ttl_seconds` | `int` | `required` |


## `RouterCloudTransportMetadata`

| Field | Type | Default |
| --- | --- | --- |
| `direct_ipv6` | `bool` | `required` |
| `relay` | `bool` | `required` |
| `auto` | `bool` | `required` |


## `RouterCloudMetadata`

| Field | Type | Default |
| --- | --- | --- |
| `connector_enabled` | `bool` | `required` |
| `enrolled` | `bool` | `required` |
| `status_endpoint` | `str` | `required` |
| `transports` | `RouterCloudTransportMetadata` | `required` |
| `manifest_schema_version` | `int` | `1` |
| `run_context_trust_delivery` | `str` | `''` |


## `RouterAuthMetadata`

| Field | Type | Default |
| --- | --- | --- |
| `schema_version` | `int` | `required` |
| `required` | `bool` | `required` |
| `auth_type` | `str` | `required` |
| `issuer` | `Optional[str]` | `required` |
| `audience` | `Optional[str]` | `required` |
| `required_scopes` | `Mapping[str, Sequence[str]]` | `required` |
| `bootstrap` | `Optional[RouterBootstrapMetadata]` | `None` |
| `cloud` | `Optional[RouterCloudMetadata]` | `None` |

### `RouterAuthMetadata.from_dict`

```text
RouterAuthMetadata.from_dict(cls, value: Mapping[str, Any]) -> 'RouterAuthMetadata'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `NexusAuthDiscoveryError`, `TypeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L316)


### `discover_router_auth`

```text
discover_router_auth(router_url: str, *, timeout: float=10.0, ca_file: Optional[str]=None, use_environment_proxy: bool=True) -> RouterAuthMetadata
```

| Parameter | Type | Default |
| --- | --- | --- |
| `router_url` | `str` | `required` |
| `timeout` | `float` | `10.0` |
| `ca_file` | `Optional[str]` | `None` |
| `use_environment_proxy` | `bool` | `True` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L508)


## `OIDCClientCredentialsProvider`

Acquire and refresh short-lived access tokens using OIDC discovery.

### `OIDCClientCredentialsProvider.__init__`

```text
OIDCClientCredentialsProvider.__init__(self, *, issuer: str, client_id: Optional[str]=None, client_secret: Optional[str]=None, client_id_env: str='NEXUS_AGENT_CLIENT_ID', client_secret_env: str='NEXUS_AGENT_CLIENT_SECRET', audience: Optional[str]=None, scopes: Sequence[str]=('agent.route', 'agent.invoke', 'agent.register'), token_endpoint: Optional[str]=None, timeout: float=10.0, refresh_skew_seconds: int=30, ca_file: Optional[str]=None, allow_insecure_http: bool=False, use_environment_proxy: bool=True, environ: Optional[Mapping[str, str]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `issuer` | `str` | `required` |
| `client_id` | `Optional[str]` | `None` |
| `client_secret` | `Optional[str]` | `None` |
| `client_id_env` | `str` | `'NEXUS_AGENT_CLIENT_ID'` |
| `client_secret_env` | `str` | `'NEXUS_AGENT_CLIENT_SECRET'` |
| `audience` | `Optional[str]` | `None` |
| `scopes` | `Sequence[str]` | `('agent.route', 'agent.invoke', 'agent.register')` |
| `token_endpoint` | `Optional[str]` | `None` |
| `timeout` | `float` | `10.0` |
| `refresh_skew_seconds` | `int` | `30` |
| `ca_file` | `Optional[str]` | `None` |
| `allow_insecure_http` | `bool` | `False` |
| `use_environment_proxy` | `bool` | `True` |
| `environ` | `Optional[Mapping[str, str]]` | `None` |

Direct raises (not exhaustive): `NexusTokenAcquisitionError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L543)

### `OIDCClientCredentialsProvider.get_token`

```text
OIDCClientCredentialsProvider.get_token(self, *, force_refresh: bool=False) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L664)


## `RouterLanSessionProvider`

Acquire source-bound, short-lived credentials from a trusted LAN router.

### `RouterLanSessionProvider.__init__`

```text
RouterLanSessionProvider.__init__(self, *, router_url: str, endpoint: str, advertised_ttl_seconds: int, tenant: str, origin: str, scopes: Sequence[str], timeout: float=10.0, ca_file: Optional[str]=None, use_environment_proxy: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `router_url` | `str` | `required` |
| `endpoint` | `str` | `required` |
| `advertised_ttl_seconds` | `int` | `required` |
| `tenant` | `str` | `required` |
| `origin` | `str` | `required` |
| `scopes` | `Sequence[str]` | `required` |
| `timeout` | `float` | `10.0` |
| `ca_file` | `Optional[str]` | `None` |
| `use_environment_proxy` | `bool` | `True` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L680)

### `RouterLanSessionProvider.cloud_trust`

```text
RouterLanSessionProvider.cloud_trust: Optional[CloudTrustPolicy]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L737)

### `RouterLanSessionProvider.get_token`

```text
RouterLanSessionProvider.get_token(self, *, force_refresh: bool=False) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L827)


## `AutoTokenProvider`

Use explicit token, trusted-LAN bootstrap, OIDC, then router no-auth.

### `AutoTokenProvider.__init__`

```text
AutoTokenProvider.__init__(self, router_url: str, *, client_id: Optional[str]=None, client_secret: Optional[str]=None, scopes: Sequence[str]=('agent.route', 'agent.invoke', 'agent.register'), timeout: float=10.0, router_ca_file: Optional[str]=None, issuer_ca_file: Optional[str]=None, use_environment_proxy: bool=True, environ: Optional[Mapping[str, str]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `router_url` | `str` | `required` |
| `client_id` | `Optional[str]` | `None` |
| `client_secret` | `Optional[str]` | `None` |
| `scopes` | `Sequence[str]` | `('agent.route', 'agent.invoke', 'agent.register')` |
| `timeout` | `float` | `10.0` |
| `router_ca_file` | `Optional[str]` | `None` |
| `issuer_ca_file` | `Optional[str]` | `None` |
| `use_environment_proxy` | `bool` | `True` |
| `environ` | `Optional[Mapping[str, str]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L841)

### `AutoTokenProvider.refreshable`

```text
AutoTokenProvider.refreshable: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L872)

### `AutoTokenProvider.metadata`

```text
AutoTokenProvider.metadata: Optional[RouterAuthMetadata]
```

Return metadata captured by the same discovery used for auto auth.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L876)

### `AutoTokenProvider.bind_registration`

```text
AutoTokenProvider.bind_registration(self, *, tenant: str, origin: str) -> None
```

Bind this provider to the first Agent identity registered through it.

| Parameter | Type | Default |
| --- | --- | --- |
| `tenant` | `str` | `required` |
| `origin` | `str` | `required` |

Direct raises (not exhaustive): `NexusTokenAcquisitionError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L883)

### `AutoTokenProvider.get_token`

```text
AutoTokenProvider.get_token(self, *, force_refresh: bool=False) -> Optional[str]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `force_refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L943)

### `AutoTokenProvider.open_cloud_request`

```text
AutoTokenProvider.open_cloud_request(self, request: urllib.request.Request, *, timeout: float, exchange: bool=False) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `request` | `urllib.request.Request` | `required` |
| `timeout` | `float` | `required` |
| `exchange` | `bool` | `False` |

Direct raises (not exhaustive): `CloudTrustUnavailableError`, `CloudTrustVerificationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py#L959)

