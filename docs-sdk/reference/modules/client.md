---
title: "client API"
---

# client API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `NexusDirectTaskError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

A router-to-router Direct Task failed or became unavailable.


## `NexusInteractionRequest`

| Field | Type | Default |
| --- | --- | --- |
| `key` | `str` | `required` |
| `prompt` | `str` | `required` |
| `kind` | `str` | `'text'` |
| `choices` | `tuple` | `()` |


## `NexusInvokeEvent`

| Field | Type | Default |
| --- | --- | --- |
| `seq` | `int` | `required` |
| `event` | `str` | `required` |
| `data` | `Any` | `required` |

### `NexusInvokeEvent.input_required`

```text
NexusInvokeEvent.input_required: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L54)

### `NexusInvokeEvent.interaction`

```text
NexusInvokeEvent.interaction: Optional[NexusInteractionRequest]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L58)

### `NexusInvokeEvent.reply`

```text
NexusInvokeEvent.reply(self, value: Any) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Any` | `required` |

Direct raises (not exhaustive): `NexusDirectTaskError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L68)


## `NexusDirectTask`

Handle for one private Direct Invoke task.

The task token is intentionally excluded from repr and public status
payloads.  It is only sent to task-scoped control endpoints.

| Field | Type | Default |
| --- | --- | --- |
| `client` | `'NexusAgentClient'` | `field(repr=False)` |
| `task_id` | `str` | `required` |

### `NexusDirectTask.status`

```text
NexusDirectTask.status(self) -> Mapping[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L119)

### `NexusDirectTask.events`

```text
NexusDirectTask.events(self, *, after: int=0, follow: bool=False, poll_interval: float=0.25) -> Iterator[NexusInvokeEvent]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `after` | `int` | `0` |
| `follow` | `bool` | `False` |
| `poll_interval` | `float` | `0.25` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L128)

### `NexusDirectTask.reply`

```text
NexusDirectTask.reply(self, *, key: str, value: Any) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `key` | `str` | `required` |
| `value` | `Any` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L161)

### `NexusDirectTask.cancel`

```text
NexusDirectTask.cancel(self) -> Mapping[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L174)

### `NexusDirectTask.asset`

```text
NexusDirectTask.asset(self, asset_id: str) -> bytes
```

Download one private Browser asset produced by this task.

| Parameter | Type | Default |
| --- | --- | --- |
| `asset_id` | `str` | `required` |

Direct raises (not exhaustive): `NexusDirectTaskError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L183)

### `NexusDirectTask.result`

```text
NexusDirectTask.result(self, timeout: float=300.0) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `300.0` |

Direct raises (not exhaustive): `NexusDirectTaskError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L219)


## `NexusAgentClient`

Synchronous client for an Agent Access Proxy endpoint.

### `NexusAgentClient.__init__`

```text
NexusAgentClient.__init__(self, base_url: str, *, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, auth: Optional[Union[str, TokenProvider]]=None, transaction_token: Optional[str]=None, ca_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, tls_server_name: Optional[str]=None, use_environment_proxy: bool=True, timeout: float=10.0, user_agent: str='nexus-agent-sdk-python/0.35.0') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `base_url` | `str` | `required` |
| `token` | `Optional[str]` | `None` |
| `token_provider` | `Optional[TokenProvider]` | `None` |
| `auth` | `Optional[Union[str, TokenProvider]]` | `None` |
| `transaction_token` | `Optional[str]` | `None` |
| `ca_file` | `Optional[str]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `tls_server_name` | `Optional[str]` | `None` |
| `use_environment_proxy` | `bool` | `True` |
| `timeout` | `float` | `10.0` |
| `user_agent` | `str` | `'nexus-agent-sdk-python/0.35.0'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L277)

### `NexusAgentClient.router_auth_metadata`

```text
NexusAgentClient.router_auth_metadata(self, *, tenant: str, origin: str) -> Optional[RouterAuthMetadata]
```

Reuse automatic-auth discovery without acquiring or exposing a token.

| Parameter | Type | Default |
| --- | --- | --- |
| `tenant` | `str` | `required` |
| `origin` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L378)

### `NexusAgentClient.register`

```text
NexusAgentClient.register(self, registration: CapabilityRegistration, *, auto_renew: bool=False, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> 'AgentLease'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `registration` | `CapabilityRegistration` | `required` |
| `auto_renew` | `bool` | `False` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L558)

### `NexusAgentClient.renew`

```text
NexusAgentClient.renew(self, route_id: str, *, lease_seconds: Optional[int]=None, latency_ms: Optional[int]=None, load_permille: Optional[int]=None, healthy: Optional[bool]=None, backend_tls: Optional[BackendTlsIdentity]=None, endpoint: Optional[str]=None) -> LeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `route_id` | `str` | `required` |
| `lease_seconds` | `Optional[int]` | `None` |
| `latency_ms` | `Optional[int]` | `None` |
| `load_permille` | `Optional[int]` | `None` |
| `healthy` | `Optional[bool]` | `None` |
| `backend_tls` | `Optional[BackendTlsIdentity]` | `None` |
| `endpoint` | `Optional[str]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L583)

### `NexusAgentClient.unregister`

```text
NexusAgentClient.unregister(self, route_id: str) -> LeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `route_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L608)

### `NexusAgentClient.cloud_status`

```text
NexusAgentClient.cloud_status(self, *, tenant: str, origin: str) -> CloudRegistrationStatus
```

Return this trusted-LAN identity&#x27;s asynchronous Cloud state.

| Parameter | Type | Default |
| --- | --- | --- |
| `tenant` | `str` | `required` |
| `origin` | `str` | `required` |

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L613)

### `NexusAgentClient.route`

```text
NexusAgentClient.route(self, envelope: Mapping[str, Any]) -> JsonObject
```

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L636)

### `NexusAgentClient.invoke`

```text
NexusAgentClient.invoke(self, envelope: Mapping[str, Any]) -> JsonObject
```

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L640)

### `NexusAgentClient.invoke_async`

```text
NexusAgentClient.invoke_async(self, envelope: Mapping[str, Any]) -> NexusDirectTask
```

Start a router-to-router Direct Task without blocking the caller.

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `NexusDirectTaskError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L644)

### `NexusAgentClient.invoke_interactive`

```text
NexusAgentClient.invoke_interactive(self, envelope: Mapping[str, Any]) -> Iterator[NexusInvokeEvent]
```

Stream one interactive Direct Invoke.

Every yielded interaction event carries a private task handle so
``event.reply(value)`` can resume the waiting Agent handler.

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `NexusDirectTaskError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L662)

### `NexusAgentClient.invoke_intent`

```text
NexusAgentClient.invoke_intent(self, intent: str, payload: Any, *, tenant: str, source_agent: str, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> JsonObject
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `tenant` | `str` | `required` |
| `source_agent` | `str` | `required` |
| `target_agent` | `Optional[str]` | `None` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L721)

### `NexusAgentClient.invoke_stream`

```text
NexusAgentClient.invoke_stream(self, envelope: Mapping[str, Any], *, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]
```

Invoke an SSE capability and resume safely after transport loss.

P8.9 Agents assign monotonic event IDs and retain a bounded task
history.  Reconnects reuse the original task_id and send both the
standard ``Last-Event-ID`` header and the routed Envelope cursor.

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `Mapping[str, Any]` | `required` |
| `resume` | `bool` | `True` |
| `last_event_id` | `int` | `0` |
| `max_reconnects` | `int` | `3` |
| `reconnect_delay` | `float` | `0.25` |

Direct raises (not exhaustive): `NexusAgentError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L757)


## `AgentLease`

A registered route lease with optional background renewal.

### `AgentLease.__init__`

```text
AgentLease.__init__(self, client: NexusAgentClient, info: LeaseInfo, *, registration: Optional[CapabilityRegistration]=None, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `info` | `LeaseInfo` | `required` |
| `registration` | `Optional[CapabilityRegistration]` | `None` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L888)

### `AgentLease.route_id`

```text
AgentLease.route_id: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L916)

### `AgentLease.public_ipv6`

```text
AgentLease.public_ipv6: Optional[str]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L921)

### `AgentLease.public_endpoint`

```text
AgentLease.public_endpoint: Optional[PublicAgentEndpoint]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L926)

### `AgentLease.renew`

```text
AgentLease.renew(self, **updates: Any) -> LeaseInfo
```

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L940)

### `AgentLease.start_auto_renew`

```text
AgentLease.start_auto_renew(self) -> 'AgentLease'
```

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L1000)

### `AgentLease.close`

```text
AgentLease.close(self, *, unregister: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `unregister` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py#L1056)

