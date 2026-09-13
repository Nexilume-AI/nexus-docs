---
title: "a2a API"
---

# a2a API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `A2ABridgeError`

Bases: `Exception`. Inherited behavior is defined on the base class.

A2A dependency, configuration, or lifecycle failure.


## `A2ASkillMapping`

Expose one Agent Card skill as one Nexus capability route.

| Field | Type | Default |
| --- | --- | --- |
| `skill` | `str` | `required` |
| `capability` | `CapabilityRegistration` | `required` |


## `A2AResult`

Friendly result returned by :class:`NexusA2AClient`.

| Field | Type | Default |
| --- | --- | --- |
| `message_id` | `str` | `required` |
| `context_id` | `str` | `required` |
| `text` | `str` | `required` |
| `data` | `Any` | `required` |
| `task` | `Optional[Mapping[str, Any]]` | `required` |
| `raw` | `Mapping[str, Any]` | `required` |


## `A2AStreamEvent`

One normalized event from an official A2A streaming task.

| Field | Type | Default |
| --- | --- | --- |
| `kind` | `str` | `required` |
| `task_id` | `str` | `required` |
| `context_id` | `str` | `required` |
| `state` | `str` | `required` |
| `text` | `str` | `required` |
| `last_chunk` | `bool` | `required` |
| `final` | `bool` | `required` |
| `raw` | `Mapping[str, Any]` | `required` |
| `event_id` | `str` | `''` |


## `A2AExecutorBridge`

Run an official A2A ``AgentExecutor`` behind a Nexus Agent Server.

### `A2AExecutorBridge.__init__`

```text
A2AExecutorBridge.__init__(self, executor: Any, server: NexusAgentServer, agent_card: Any, mappings: Mapping[str, CapabilityRegistration], *, task_store: Any=None, timeout: float=30.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `executor` | `Any` | `required` |
| `server` | `NexusAgentServer` | `required` |
| `agent_card` | `Any` | `required` |
| `mappings` | `Mapping[str, CapabilityRegistration]` | `required` |
| `task_store` | `Any` | `None` |
| `timeout` | `float` | `30.0` |

Direct raises (not exhaustive): `TypeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L196)

### `A2AExecutorBridge.capabilities`

```text
A2AExecutorBridge.capabilities: tuple[CapabilityRegistration, ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L237)

### `A2AExecutorBridge.is_healthy`

```text
A2AExecutorBridge.is_healthy(self) -> bool
```

Return whether A2A execution and the Agent listener are live.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L240)

### `A2AExecutorBridge.start`

```text
A2AExecutorBridge.start(self) -> None
```

Direct raises (not exhaustive): `A2ABridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L250)

### `A2AExecutorBridge.invoke`

```text
A2AExecutorBridge.invoke(self, skill: str, envelope: AgentEnvelope) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `skill` | `str` | `required` |
| `envelope` | `AgentEnvelope` | `required` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L342)

### `A2AExecutorBridge.invoke_stream`

```text
A2AExecutorBridge.invoke_stream(self, skill: str, envelope: AgentEnvelope) -> Iterator[Mapping[str, Any]]
```

Yield official ``StreamResponse`` objects one event at a time.

| Parameter | Type | Default |
| --- | --- | --- |
| `skill` | `str` | `required` |
| `envelope` | `AgentEnvelope` | `required` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L364)

### `A2AExecutorBridge.close`

```text
A2AExecutorBridge.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L418)

### `A2AExecutorBridge.registered`

```text
A2AExecutorBridge.registered(self, client: NexusAgentClient, *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> Iterator[tuple[AgentLease, ...]]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L434)


## `NexusA2AClient`

Small official-A2A caller for one router Card/Skill mapping.

It creates the otherwise verbose edge Agent Card, official HTTP client and
``SendMessageRequest`` automatically, then unwraps the Nexus Adapter&#x27;s Task
data part into :class:`A2AResult`.

### `NexusA2AClient.__init__`

```text
NexusA2AClient.__init__(self, router_url: str, *, card_id: str, skill: str, token: Optional[str]=None, transaction_token: Optional[str]=None, ca_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, timeout: float=30.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `router_url` | `str` | `required` |
| `card_id` | `str` | `required` |
| `skill` | `str` | `required` |
| `token` | `Optional[str]` | `None` |
| `transaction_token` | `Optional[str]` | `None` |
| `ca_file` | `Optional[str]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `timeout` | `float` | `30.0` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L627)

### `NexusA2AClient.edge_url`

```text
NexusA2AClient.edge_url: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L661)

### `NexusA2AClient.send`

```text
async NexusA2AClient.send(self, text: str, *, context_id: Optional[str]=None) -> A2AResult
```

Send one text message and return a normalized result.

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `context_id` | `Optional[str]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L721)

### `NexusA2AClient.send_request`

```text
async NexusA2AClient.send_request(self, request: Any) -> A2AResult
```

Send an advanced official ``SendMessageRequest``.

| Parameter | Type | Default |
| --- | --- | --- |
| `request` | `Any` | `required` |

Direct raises (not exhaustive): `A2ABridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L739)

### `NexusA2AClient.stream`

```text
async NexusA2AClient.stream(self, text: str, *, context_id: Optional[str]=None, resume: Optional[bool]=None, max_reconnects: int=3, reconnect_delay: float=0.25) -> AsyncIterator[A2AStreamEvent]
```

Yield A2A events and resume the same message task after a disconnect.

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `context_id` | `Optional[str]` | `None` |
| `resume` | `Optional[bool]` | `None` |
| `max_reconnects` | `int` | `3` |
| `reconnect_delay` | `float` | `0.25` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L753)

### `NexusA2AClient.stream_request`

```text
async NexusA2AClient.stream_request(self, request: Any, *, resume: Optional[bool]=None, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> AsyncIterator[A2AStreamEvent]
```

Stream one official request with bounded automatic reconnection.

| Parameter | Type | Default |
| --- | --- | --- |
| `request` | `Any` | `required` |
| `resume` | `Optional[bool]` | `None` |
| `last_event_id` | `int` | `0` |
| `max_reconnects` | `int` | `3` |
| `reconnect_delay` | `float` | `0.25` |

Direct raises (not exhaustive): `A2ABridgeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L780)

### `NexusA2AClient.close`

```text
async NexusA2AClient.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L862)


## `NexusA2AAgent`

High-level lifecycle wrapper for an official A2A AgentExecutor.

### `NexusA2AAgent.__init__`

```text
NexusA2AAgent.__init__(self, executor: Any, *, router: Union[str, NexusAgentClient], identity: str, endpoint: str, tenant: str, host: str='0.0.0.0', port: int=9443, token: Optional[str]=None, router_ca_file: Optional[str]=None, router_cert_file: Optional[str]=None, router_key_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, card_url: Optional[str]=None, name: str='Nexus A2A Agent', description: str='Official A2A AgentExecutor routed by Nexus', agent_version: str='1.0.0', server: Optional[NexusAgentServer]=None, timeout: float=30.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `executor` | `Any` | `required` |
| `router` | `Union[str, NexusAgentClient]` | `required` |
| `identity` | `str` | `required` |
| `endpoint` | `str` | `required` |
| `tenant` | `str` | `required` |
| `host` | `str` | `'0.0.0.0'` |
| `port` | `int` | `9443` |
| `token` | `Optional[str]` | `None` |
| `router_ca_file` | `Optional[str]` | `None` |
| `router_cert_file` | `Optional[str]` | `None` |
| `router_key_file` | `Optional[str]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `card_url` | `Optional[str]` | `None` |
| `name` | `str` | `'Nexus A2A Agent'` |
| `description` | `str` | `'Official A2A AgentExecutor routed by Nexus'` |
| `agent_version` | `str` | `'1.0.0'` |
| `server` | `Optional[NexusAgentServer]` | `None` |
| `timeout` | `float` | `30.0` |

Direct raises (not exhaustive): `TypeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L884)

### `NexusA2AAgent.expose`

```text
NexusA2AAgent.expose(self, *, skill: str, intent: str, name: Optional[str]=None, description: Optional[str]=None, tags: Sequence[str]=('nexus',), input_modes: Sequence[str]=('text/plain',), output_modes: Sequence[str]=('text/plain', 'application/json'), version: int=1, region: str='local', route_id: Optional[str]=None, cost_microunits: int=0, latency_ms: int=0, trust: int=50, lease_seconds: int=30, public_ipv6: Optional[str]=None) -> 'NexusA2AAgent'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `skill` | `str` | `required` |
| `intent` | `str` | `required` |
| `name` | `Optional[str]` | `None` |
| `description` | `Optional[str]` | `None` |
| `tags` | `Sequence[str]` | `('nexus',)` |
| `input_modes` | `Sequence[str]` | `('text/plain',)` |
| `output_modes` | `Sequence[str]` | `('text/plain', 'application/json')` |
| `version` | `int` | `1` |
| `region` | `str` | `'local'` |
| `route_id` | `Optional[str]` | `None` |
| `cost_microunits` | `int` | `0` |
| `latency_ms` | `int` | `0` |
| `trust` | `int` | `50` |
| `lease_seconds` | `int` | `30` |
| `public_ipv6` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L941)

### `NexusA2AAgent.capabilities`

```text
NexusA2AAgent.capabilities: Tuple[CapabilityRegistration, ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L992)

### `NexusA2AAgent.build_card`

```text
NexusA2AAgent.build_card(self) -> Any
```

Direct raises (not exhaustive): `A2ABridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L995)

### `NexusA2AAgent.registered`

```text
NexusA2AAgent.registered(self, *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> Iterator[tuple[AgentLease, ...]]
```

Install handlers and keep all exposed routes leased.

| Parameter | Type | Default |
| --- | --- | --- |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L1035)

### `NexusA2AAgent.run`

```text
NexusA2AAgent.run(self, *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> None
```

Register every exposed skill, serve, then unregister on exit.

| Parameter | Type | Default |
| --- | --- | --- |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L1055)

### `NexusA2AAgent.stop`

```text
NexusA2AAgent.stop(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/a2a.py#L1076)

