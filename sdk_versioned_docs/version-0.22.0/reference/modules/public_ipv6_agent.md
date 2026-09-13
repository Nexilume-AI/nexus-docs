---
title: "public_ipv6_agent API"
---

# public_ipv6_agent API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `PublicIPv6AgentHandle`

Running Agent-owned IPv6 listener.

### `PublicIPv6AgentHandle.__init__`

```text
PublicIPv6AgentHandle.__init__(self, owner: 'PublicIPv6Agent', thread: threading.Thread) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `owner` | `'PublicIPv6Agent'` | `required` |
| `thread` | `threading.Thread` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L24)

### `PublicIPv6AgentHandle.wait`

```text
PublicIPv6AgentHandle.wait(self, timeout: Optional[float]=None) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `Optional[float]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L30)

### `PublicIPv6AgentHandle.close`

```text
PublicIPv6AgentHandle.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L34)


## `PublicIPv6Agent`

Serve capabilities directly from a host-owned global IPv6 address.

### `PublicIPv6Agent.__init__`

```text
PublicIPv6Agent.__init__(self, address: str, *, auth: Union[str, ServerAuthPolicy], port: int=9443, tenant: str='default', agent_id: Optional[str]=None, address_mode: str='auto', allocator: Optional[LocalAddressdClient]=None, interface: str='auto', prefix: str='auto', address_lease_seconds: int=300, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, tls_server_name: Optional[str]=None, ca_bundle_id: Optional[str]=None, max_request_bytes: int=65536, max_response_bytes: int=262144, max_stream_event_bytes: int=65536, request_timeout: float=15.0, resumable_streams: bool=True) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |
| `auth` | `Union[str, ServerAuthPolicy]` | `required` |
| `port` | `int` | `9443` |
| `tenant` | `str` | `'default'` |
| `agent_id` | `Optional[str]` | `None` |
| `address_mode` | `str` | `'auto'` |
| `allocator` | `Optional[LocalAddressdClient]` | `None` |
| `interface` | `str` | `'auto'` |
| `prefix` | `str` | `'auto'` |
| `address_lease_seconds` | `int` | `300` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `client_ca_file` | `Optional[str]` | `None` |
| `tls_server_name` | `Optional[str]` | `None` |
| `ca_bundle_id` | `Optional[str]` | `None` |
| `max_request_bytes` | `int` | `65536` |
| `max_response_bytes` | `int` | `262144` |
| `max_stream_event_bytes` | `int` | `65536` |
| `request_timeout` | `float` | `15.0` |
| `resumable_streams` | `bool` | `True` |

Direct raises (not exhaustive): `NexusAgentError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L58)

### `PublicIPv6Agent.capability`

```text
PublicIPv6Agent.capability(self, intent: str, *, pass_envelope: bool=False) -> Callable[[BusinessHandler], BusinessHandler]
```

Expose a synchronous function on the direct IPv6 endpoint.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `pass_envelope` | `bool` | `False` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L192)

### `PublicIPv6Agent.stream_capability`

```text
PublicIPv6Agent.stream_capability(self, intent: str, *, pass_envelope: bool=False) -> Callable[[BusinessStreamHandler], BusinessStreamHandler]
```

Expose a streaming function on the direct IPv6 endpoint.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `pass_envelope` | `bool` | `False` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L214)

### `PublicIPv6Agent.start`

```text
PublicIPv6Agent.start(self, *, announce: bool=True, print_fn: Callable[[str], Any]=print) -> PublicIPv6AgentHandle
```

| Parameter | Type | Default |
| --- | --- | --- |
| `announce` | `bool` | `True` |
| `print_fn` | `Callable[[str], Any]` | `print` |

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L236)

### `PublicIPv6Agent.run`

```text
PublicIPv6Agent.run(self, **start_options: Any) -> PublicAgentEndpoint
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py#L275)

