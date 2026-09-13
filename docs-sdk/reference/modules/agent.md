---
title: "agent API"
---

# agent API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

### `resolve_router_url`

```text
resolve_router_url(router: str='auto') -> str
```

Resolve the local Agent Access Proxy URL with bounded zero config.

Resolution order is explicit URL, ``NEXUS_ROUTER_URL``, the resolvable
``nexus-router.local`` name, the Linux default IPv4 gateway, then a
reachable Router on a Windows on-link IPv4 subnet.

| Parameter | Type | Default |
| --- | --- | --- |
| `router` | `str` | `'auto'` |

Direct raises (not exhaustive): `NexusAgentError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L411)


### `resolve_advertise_address`

```text
resolve_advertise_address(value: str='auto', *, router_url: Optional[str]=None) -> str
```

Resolve the address placed in the router&#x27;s backend endpoint.

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `'auto'` |
| `router_url` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `NexusAgentError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L560)


## `PublishedCapability`

One registered capability and its router-managed public address.

| Field | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `origin` | `str` | `required` |
| `backend_endpoint` | `str` | `required` |
| `route_id` | `str` | `required` |
| `public_ipv6` | `Optional[str]` | `required` |
| `public_endpoint` | `Optional[PublicAgentEndpoint]` | `required` |

### `PublishedCapability.public_url`

```text
PublishedCapability.public_url: Optional[str]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L640)


## `NexusAgentHandle`

Running high-level Agent; closes leases and listener as one unit.

### `NexusAgentHandle.__init__`

```text
NexusAgentHandle.__init__(self, owner: 'NexusAgent', thread: threading.Thread, leases: Tuple[AgentLease, ...], published: Tuple[PublishedCapability, ...]) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `owner` | `'NexusAgent'` | `required` |
| `thread` | `threading.Thread` | `required` |
| `leases` | `Tuple[AgentLease, ...]` | `required` |
| `published` | `Tuple[PublishedCapability, ...]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L661)

### `NexusAgentHandle.wait`

```text
NexusAgentHandle.wait(self, timeout: Optional[float]=None) -> bool
```

Wait for the listener; return ``True`` if it has stopped.

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `Optional[float]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L675)

### `NexusAgentHandle.cloud_status`

```text
NexusAgentHandle.cloud_status(self) -> CloudRegistrationStatus
```

Return this Agent&#x27;s router-managed Nexus Cloud state.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L681)

### `NexusAgentHandle.wait_for_cloud`

```text
NexusAgentHandle.wait_for_cloud(self, timeout: float=60.0, *, poll_interval: float=1.0) -> CloudRegistrationStatus
```

Wait for managed Cloud publication without affecting the LAN lease.

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `60.0` |
| `poll_interval` | `float` | `1.0` |

Direct raises (not exhaustive): `NexusCloudRegistrationError`, `TimeoutError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L689)

### `NexusAgentHandle.close`

```text
NexusAgentHandle.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L719)


## `NexusAgent`

Friendly facade that turns decorated Python functions into capabilities.

### `NexusAgent.public_ipv6`

```text
NexusAgent.public_ipv6(cls, address: str, **options: Any) -> not annotated; see contract/source
```

Create an Agent-owned public IPv6 server without router registration.

| Parameter | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L747)

### `NexusAgent.__init__`

```text
NexusAgent.__init__(self, *, router: str='auto', token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, auth: Optional[Union[str, TokenProvider]]=None, transaction_token: Optional[str]=None, tenant: str='default', agent_id: Optional[str]=None, listen_host: str='auto', port: int=0, advertise_address: str='auto', path: str='/invoke', router_ca_file: Optional[str]=None, auth_ca_file: Optional[str]=None, cloud_ca_file: Optional[str]=None, router_cert_file: Optional[str]=None, router_key_file: Optional[str]=None, router_tls_server_name: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, server_tls_name: str='auto', server_ca_bundle_id: str='system', lease_seconds: int=300, timeout: float=10.0, cloud_publish: bool=True, cloud_name: Optional[str]=None, computer_requirement: str='disabled', workspace_capabilities: Iterable[str]=(), mobile_requirement: str='disabled', mobile_capabilities: Iterable[str]=(), runtime: str='auto') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `router` | `str` | `'auto'` |
| `token` | `Optional[str]` | `None` |
| `token_provider` | `Optional[TokenProvider]` | `None` |
| `auth` | `Optional[Union[str, TokenProvider]]` | `None` |
| `transaction_token` | `Optional[str]` | `None` |
| `tenant` | `str` | `'default'` |
| `agent_id` | `Optional[str]` | `None` |
| `listen_host` | `str` | `'auto'` |
| `port` | `int` | `0` |
| `advertise_address` | `str` | `'auto'` |
| `path` | `str` | `'/invoke'` |
| `router_ca_file` | `Optional[str]` | `None` |
| `auth_ca_file` | `Optional[str]` | `None` |
| `cloud_ca_file` | `Optional[str]` | `None` |
| `router_cert_file` | `Optional[str]` | `None` |
| `router_key_file` | `Optional[str]` | `None` |
| `router_tls_server_name` | `Optional[str]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `client_ca_file` | `Optional[str]` | `None` |
| `server_tls_name` | `str` | `'auto'` |
| `server_ca_bundle_id` | `str` | `'system'` |
| `lease_seconds` | `int` | `300` |
| `timeout` | `float` | `10.0` |
| `cloud_publish` | `bool` | `True` |
| `cloud_name` | `Optional[str]` | `None` |
| `computer_requirement` | `str` | `'disabled'` |
| `workspace_capabilities` | `Iterable[str]` | `()` |
| `mobile_requirement` | `str` | `'disabled'` |
| `mobile_capabilities` | `Iterable[str]` | `()` |
| `runtime` | `str` | `'auto'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L754)

### `NexusAgent.backend_endpoint`

```text
NexusAgent.backend_endpoint: str
```

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L938)

### `NexusAgent.capability`

```text
NexusAgent.capability(self, intent: str, *, public_ipv6: Optional[bool]=None, origin: Optional[str]=None, version: int=1, region: str='local', lease_seconds: Optional[int]=None, cost_microunits: int=0, latency_ms: int=0, trust: int=50, pass_envelope: bool=False, tool: Optional[Union[McpToolDescriptor, bool]]=None, mobile_scopes: Optional[Iterable[str]]=None, slash_command: Optional[str]=None, slash_description: str='', execution_profiles: Optional[Iterable[NexusExecutionProfile]]=None, input_modalities: Optional[Iterable[str]]=None, follow_up: Optional[str]=None) -> Callable[[BusinessHandler], BusinessHandler]
```

Decorate a sync/async handler; opt in to cooperative Cloud follow-up.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `public_ipv6` | `Optional[bool]` | `None` |
| `origin` | `Optional[str]` | `None` |
| `version` | `int` | `1` |
| `region` | `str` | `'local'` |
| `lease_seconds` | `Optional[int]` | `None` |
| `cost_microunits` | `int` | `0` |
| `latency_ms` | `int` | `0` |
| `trust` | `int` | `50` |
| `pass_envelope` | `bool` | `False` |
| `tool` | `Optional[Union[McpToolDescriptor, bool]]` | `None` |
| `mobile_scopes` | `Optional[Iterable[str]]` | `None` |
| `slash_command` | `Optional[str]` | `None` |
| `slash_description` | `str` | `''` |
| `execution_profiles` | `Optional[Iterable[NexusExecutionProfile]]` | `None` |
| `input_modalities` | `Optional[Iterable[str]]` | `None` |
| `follow_up` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L992)

### `NexusAgent.stream_capability`

```text
NexusAgent.stream_capability(self, intent: str, *, public_ipv6: Optional[bool]=None, origin: Optional[str]=None, version: int=1, region: str='local', lease_seconds: Optional[int]=None, cost_microunits: int=0, latency_ms: int=0, trust: int=50, pass_envelope: bool=False, tool: Optional[Union[McpToolDescriptor, bool]]=None, mobile_scopes: Optional[Iterable[str]]=None, slash_command: Optional[str]=None, slash_description: str='', execution_profiles: Optional[Iterable[NexusExecutionProfile]]=None, input_modalities: Optional[Iterable[str]]=None) -> Callable[[BusinessStreamHandler], BusinessStreamHandler]
```

Decorate a generator as an SSE capability for the same intent.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `public_ipv6` | `Optional[bool]` | `None` |
| `origin` | `Optional[str]` | `None` |
| `version` | `int` | `1` |
| `region` | `str` | `'local'` |
| `lease_seconds` | `Optional[int]` | `None` |
| `cost_microunits` | `int` | `0` |
| `latency_ms` | `int` | `0` |
| `trust` | `int` | `50` |
| `pass_envelope` | `bool` | `False` |
| `tool` | `Optional[Union[McpToolDescriptor, bool]]` | `None` |
| `mobile_scopes` | `Optional[Iterable[str]]` | `None` |
| `slash_command` | `Optional[str]` | `None` |
| `slash_description` | `str` | `''` |
| `execution_profiles` | `Optional[Iterable[NexusExecutionProfile]]` | `None` |
| `input_modalities` | `Optional[Iterable[str]]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1102)

### `NexusAgent.registrations`

```text
NexusAgent.registrations(self) -> Tuple[CapabilityRegistration, ...]
```

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1220)

### `NexusAgent.invoke`

```text
NexusAgent.invoke(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> Mapping[str, Any]
```

Invoke another Agent using this Agent&#x27;s identity by default.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `target_agent` | `Optional[str]` | `None` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1255)

### `NexusAgent.invoke_async`

```text
NexusAgent.invoke_async(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> not annotated; see contract/source
```

Start an in-network Direct Task and return its private handle.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `target_agent` | `Optional[str]` | `None` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1311)

### `NexusAgent.invoke_interactive`

```text
NexusAgent.invoke_interactive(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> not annotated; see contract/source
```

Stream a Direct Invoke and allow replies to Chat interactions.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `target_agent` | `Optional[str]` | `None` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1335)

### `NexusAgent.invoke_stream`

```text
NexusAgent.invoke_stream(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]
```

Stream another Agent and automatically preserve caller identity.

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `target_agent` | `Optional[str]` | `None` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |
| `resume` | `bool` | `True` |
| `last_event_id` | `int` | `0` |
| `max_reconnects` | `int` | `3` |
| `reconnect_delay` | `float` | `0.25` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1359)

### `NexusAgent.start`

```text
NexusAgent.start(self, *, auto_renew: bool=True, renew_fraction: float=0.6, announce: bool=True, print_fn: Callable[[str], Any]=print) -> NexusAgentHandle
```

Start listening, register all capabilities, and return a handle.

| Parameter | Type | Default |
| --- | --- | --- |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `announce` | `bool` | `True` |
| `print_fn` | `Callable[[str], Any]` | `print` |

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1394)

### `NexusAgent.as_mcp_server`

```text
NexusAgent.as_mcp_server(self) -> Any
```

Export the same declared handlers as MCP without Router discovery.

Requires hosted mode (selected automatically by Python upload) and the
optional fastmcp dependency. No tool is invoked during export.

Direct raises (not exhaustive): `NexusAgentError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1528)

### `NexusAgent.run`

```text
NexusAgent.run(self, **start_options: Any) -> Any
```

Run the selected transport; edge shutdown also unregisters leases.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py#L1541)

