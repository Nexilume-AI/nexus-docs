---
title: "server API"
---

# server API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `AgentRequestError`

Bases: `Exception`. Inherited behavior is defined on the base class.

A bounded application error that may be returned to the caller.

### `AgentRequestError.__init__`

```text
AgentRequestError.__init__(self, status: int, code: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `status` | `int` | `required` |
| `code` | `str` | `required` |
| `message` | `str` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L83)


## `NexusAgentServer`

Serve Nexus Envelope invokes and dispatch them by exact intent.

### `NexusAgentServer.__init__`

```text
NexusAgentServer.__init__(self, host: str='127.0.0.1', port: int=0, *, path: str='/invoke', stream_path: Optional[str]=None, auth: Optional[ServerAuthPolicy]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, address_family: str='auto', dual_stack: bool=False, max_request_bytes: int=65536, max_response_bytes: int=262144, max_stream_event_bytes: int=65536, request_timeout: float=15.0, resumable_streams: bool=True, resume_max_tasks: int=128, resume_max_events: int=256, resume_max_history_bytes: int=262144, resume_retention_seconds: float=300.0, direct_tasks: bool=True, direct_task_max_tasks: int=128, direct_task_ttl_seconds: float=3600.0, direct_task_heartbeat_seconds: float=10.0, run_context_opener: Optional[Callable[..., Any]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `host` | `str` | `'127.0.0.1'` |
| `port` | `int` | `0` |
| `path` | `str` | `'/invoke'` |
| `stream_path` | `Optional[str]` | `None` |
| `auth` | `Optional[ServerAuthPolicy]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `client_ca_file` | `Optional[str]` | `None` |
| `address_family` | `str` | `'auto'` |
| `dual_stack` | `bool` | `False` |
| `max_request_bytes` | `int` | `65536` |
| `max_response_bytes` | `int` | `262144` |
| `max_stream_event_bytes` | `int` | `65536` |
| `request_timeout` | `float` | `15.0` |
| `resumable_streams` | `bool` | `True` |
| `resume_max_tasks` | `int` | `128` |
| `resume_max_events` | `int` | `256` |
| `resume_max_history_bytes` | `int` | `262144` |
| `resume_retention_seconds` | `float` | `300.0` |
| `direct_tasks` | `bool` | `True` |
| `direct_task_max_tasks` | `int` | `128` |
| `direct_task_ttl_seconds` | `float` | `3600.0` |
| `direct_task_heartbeat_seconds` | `float` | `10.0` |
| `run_context_opener` | `Optional[Callable[..., Any]]` | `None` |

Direct raises (not exhaustive): `TypeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L293)

### `NexusAgentServer.add_handler`

```text
NexusAgentServer.add_handler(self, intent: str, handler: SyncHandler, *, stream_handler: Optional[StreamHandler]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `handler` | `SyncHandler` | `required` |
| `stream_handler` | `Optional[StreamHandler]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L446)

### `NexusAgentServer.handler`

```text
NexusAgentServer.handler(self, intent: str) -> Callable[[SyncHandler], SyncHandler]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L460)

### `NexusAgentServer.stream_handler`

```text
NexusAgentServer.stream_handler(self, intent: str) -> Callable[[StreamHandler], StreamHandler]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L466)

### `NexusAgentServer.remove_handler`

```text
NexusAgentServer.remove_handler(self, intent: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L475)

### `NexusAgentServer.has_handler`

```text
NexusAgentServer.has_handler(self, intent: str) -> bool
```

Return whether an exact synchronous intent handler is installed.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L480)

### `NexusAgentServer.serve_forever`

```text
NexusAgentServer.serve_forever(self, poll_interval: float=0.25) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `poll_interval` | `float` | `0.25` |

Direct raises (not exhaustive): `RuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1258)

### `NexusAgentServer.is_healthy`

```text
NexusAgentServer.is_healthy(self) -> bool
```

Return whether the local Agent listener is actively serving.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1267)

### `NexusAgentServer.serve_in_thread`

```text
NexusAgentServer.serve_in_thread(self, *, daemon: bool=True) -> threading.Thread
```

| Parameter | Type | Default |
| --- | --- | --- |
| `daemon` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1276)

### `NexusAgentServer.shutdown`

```text
NexusAgentServer.shutdown(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1282)

### `NexusAgentServer.server_close`

```text
NexusAgentServer.server_close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1285)

### `NexusAgentServer.registered`

```text
NexusAgentServer.registered(self, client: NexusAgentClient, registrations: Iterable[CapabilityRegistration], *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> Iterator[Tuple[AgentLease, ...]]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `registrations` | `Iterable[CapabilityRegistration]` | `required` |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1293)

### `NexusAgentServer.serve_registered`

```text
NexusAgentServer.serve_registered(self, client: NexusAgentClient, registrations: Iterable[CapabilityRegistration], *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `registrations` | `Iterable[CapabilityRegistration]` | `required` |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py#L1321)

