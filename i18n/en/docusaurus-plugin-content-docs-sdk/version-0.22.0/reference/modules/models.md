---
title: "models API"
---

# models API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusExecutionProfile`

Publisher-declared execution choice exposed to a private Run caller.

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | `required` |
| `label` | `str` | `required` |
| `model` | `str` | `required` |
| `reasoning_efforts` | `Tuple[str, ...]` | `()` |
| `default_reasoning_effort` | `str` | `''` |
| `context_window` | `Optional[int]` | `None` |
| `is_default` | `bool` | `False` |

### `NexusExecutionProfile.to_dict`

```text
NexusExecutionProfile.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L93)


## `McpToolDescriptor`

Bounded MCP metadata published with one capability lease.

| Field | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `title` | `Optional[str]` | `None` |
| `description` | `Optional[str]` | `None` |
| `input_schema` | `Mapping[str, Any]` | `field(default_factory=lambda: {'type': 'object', 'additionalProperties': True})` |
| `task` | `bool` | `False` |
| `continuable` | `bool` | `False` |
| `demo` | `bool` | `False` |
| `chat` | `bool` | `False` |
| `interactive` | `bool` | `False` |
| `mobile_scopes` | `Tuple[str, ...]` | `()` |
| `slash_command` | `Optional[str]` | `None` |
| `slash_description` | `Optional[str]` | `None` |
| `execution_profiles` | `Tuple[NexusExecutionProfile, ...]` | `()` |
| `input_modalities` | `Tuple[str, ...]` | `('text',)` |

### `McpToolDescriptor.to_dict`

```text
McpToolDescriptor.to_dict(self, *, intent: str, intent_version: int) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `intent_version` | `int` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L213)


### `normalize_workspace_capabilities`

```text
normalize_workspace_capabilities(values: Iterable[str]) -> Tuple[str, ...]
```

Validate and order Workspace scopes exactly like Nexus Cloud.

| Parameter | Type | Default |
| --- | --- | --- |
| `values` | `Iterable[str]` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L241)


### `normalize_mobile_capabilities`

```text
normalize_mobile_capabilities(values: Iterable[str]) -> Tuple[str, ...]
```

Validate and order Caller Mobile scopes exactly like Nexus Cloud.

| Parameter | Type | Default |
| --- | --- | --- |
| `values` | `Iterable[str]` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L253)


## `ComputerRegistrationContract`

Computer requirement declared by the Agent and enforced by Cloud.

| Field | Type | Default |
| --- | --- | --- |
| `requirement` | `str` | `'disabled'` |
| `workspace_capabilities` | `Tuple[str, ...]` | `()` |

### `ComputerRegistrationContract.is_default`

```text
ComputerRegistrationContract.is_default: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L285)

### `ComputerRegistrationContract.to_dict`

```text
ComputerRegistrationContract.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L288)


## `MobileRegistrationContract`

Caller Mobile requirement declared by the Agent and enforced by Cloud.

| Field | Type | Default |
| --- | --- | --- |
| `requirement` | `str` | `'disabled'` |
| `mobile_capabilities` | `Tuple[str, ...]` | `()` |

### `MobileRegistrationContract.is_default`

```text
MobileRegistrationContract.is_default: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L319)

### `MobileRegistrationContract.to_dict`

```text
MobileRegistrationContract.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L322)


## `CloudRegistrationManifest`

Agent-level Cloud intent attached to one local capability registration.

| Field | Type | Default |
| --- | --- | --- |
| `publish` | `bool` | `required` |
| `agent_name` | `str` | `required` |
| `tool` | `Optional[McpToolDescriptor]` | `None` |
| `computer` | `Optional[ComputerRegistrationContract]` | `None` |
| `mobile` | `Optional[MobileRegistrationContract]` | `None` |
| `manifest_digest` | `Optional[str]` | `None` |

### `CloudRegistrationManifest.to_dict`

```text
CloudRegistrationManifest.to_dict(self, *, intent: str, intent_version: int) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `intent_version` | `int` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L355)


## `CloudRegistrationStatus`

Non-secret Cloud publication state returned by the trusted LAN router.

| Field | Type | Default |
| --- | --- | --- |
| `state` | `str` | `required` |
| `origin` | `str` | `''` |
| `registration_id` | `Optional[str]` | `None` |
| `agent_id` | `Optional[str]` | `None` |
| `runtime_id` | `Optional[str]` | `None` |
| `transport` | `Optional[str]` | `None` |
| `mcp_url` | `Optional[str]` | `None` |
| `manifest_digest` | `Optional[str]` | `None` |
| `message` | `str` | `''` |

### `CloudRegistrationStatus.ready`

```text
CloudRegistrationStatus.ready: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L394)

### `CloudRegistrationStatus.from_dict`

```text
CloudRegistrationStatus.from_dict(cls, value: Mapping[str, Any]) -> 'CloudRegistrationStatus'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L398)


## `BackendTlsIdentity`

Lease-bound connection metadata for an SDK-managed HTTPS Agent.

| Field | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |
| `port` | `int` | `required` |
| `tls_server_name` | `str` | `required` |
| `ca_bundle_id` | `str` | `'system'` |
| `certificate_sha256` | `Optional[str]` | `None` |

### `BackendTlsIdentity.to_dict`

```text
BackendTlsIdentity.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L451)


## `CapabilityRegistration`

| Field | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `origin` | `str` | `required` |
| `endpoint` | `str` | `required` |
| `tenant` | `str` | `required` |
| `version` | `int` | `1` |
| `region` | `str` | `'local'` |
| `route_id` | `Optional[str]` | `None` |
| `cost_microunits` | `int` | `0` |
| `latency_ms` | `int` | `0` |
| `trust` | `int` | `50` |
| `load_permille` | `int` | `0` |
| `hop_count` | `int` | `0` |
| `lease_seconds` | `int` | `30` |
| `public_ipv6` | `Optional[str]` | `None` |
| `backend_tls` | `Optional[BackendTlsIdentity]` | `None` |
| `cloud` | `Optional[CloudRegistrationManifest]` | `None` |

### `CapabilityRegistration.to_dict`

```text
CapabilityRegistration.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L497)


## `PublicAgentEndpoint`

Portable descriptor for a router-managed or Agent-owned IPv6 endpoint.

| Field | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |
| `port` | `int` | `required` |
| `tls_server_name` | `Optional[str]` | `None` |
| `ca_bundle_id` | `Optional[str]` | `None` |
| `scheme` | `str` | `'https'` |

### `PublicAgentEndpoint.url`

```text
PublicAgentEndpoint.url: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L549)

### `PublicAgentEndpoint.to_dict`

```text
PublicAgentEndpoint.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L552)

### `PublicAgentEndpoint.to_json`

```text
PublicAgentEndpoint.to_json(self, *, indent: Optional[int]=2) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `indent` | `Optional[int]` | `2` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L560)

### `PublicAgentEndpoint.from_dict`

```text
PublicAgentEndpoint.from_dict(cls, value: Mapping[str, Any]) -> 'PublicAgentEndpoint'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L564)

### `PublicAgentEndpoint.connect`

```text
PublicAgentEndpoint.connect(self, **credentials: Any) -> not annotated; see contract/source
```

Create a DirectIPv6Agent using caller-supplied credentials/CA file.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L582)


## `LeaseInfo`

| Field | Type | Default |
| --- | --- | --- |
| `route_id` | `str` | `required` |
| `generation` | `int` | `required` |
| `lease_seconds` | `int` | `required` |
| `removed` | `bool` | `False` |
| `public_ipv6` | `Optional[str]` | `None` |
| `public_endpoint` | `Optional[PublicAgentEndpoint]` | `None` |


## `SseEvent`

| Field | Type | Default |
| --- | --- | --- |
| `data` | `str` | `required` |
| `event` | `Optional[str]` | `None` |
| `event_id` | `Optional[str]` | `None` |
| `retry_ms` | `Optional[int]` | `None` |


## `AgentEnvelope`

A validated inbound Nexus Agent Envelope.

| Field | Type | Default |
| --- | --- | --- |
| `version` | `str` | `required` |
| `intent` | `str` | `required` |
| `intent_version` | `int` | `required` |
| `task_id` | `str` | `required` |
| `source_agent` | `str` | `required` |
| `tenant` | `str` | `required` |
| `hop_limit` | `int` | `required` |
| `payload` | `Any` | `required` |
| `constraints` | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `target_agent` | `Optional[str]` | `None` |
| `route_id` | `Optional[str]` | `None` |
| `resume_from_event_id` | `int` | `0` |
| `raw` | `Mapping[str, Any]` | `field(default_factory=dict, repr=False)` |
| `authenticated_subject` | `Optional[str]` | `None` |
| `authenticated_scopes` | `Tuple[str, ...]` | `()` |
| `auth_claims` | `Mapping[str, Any]` | `field(default_factory=dict, repr=False)` |
| `run_context` | `Any` | `field(default=None, repr=False, compare=False)` |

### `AgentEnvelope.protocol`

```text
AgentEnvelope.protocol: Optional[str]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L630)

### `AgentEnvelope.selector`

```text
AgentEnvelope.selector: Optional[str]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L638)

### `AgentEnvelope.protocol_request`

```text
AgentEnvelope.protocol_request: Optional[Mapping[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py#L646)


## `AgentResponse`

Optional explicit status and headers for a synchronous Agent reply.

| Field | Type | Default |
| --- | --- | --- |
| `body` | `Any` | `required` |
| `status` | `int` | `200` |
| `headers` | `Mapping[str, str]` | `field(default_factory=dict)` |

