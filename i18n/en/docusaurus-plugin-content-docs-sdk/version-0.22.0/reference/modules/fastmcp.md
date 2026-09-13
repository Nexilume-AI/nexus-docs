---
title: "fastmcp API"
---

# fastmcp API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusMCPFeedback`

Mirror request feedback to the MCP client and the private Nexus Display.

### `NexusMCPFeedback.__init__`

```text
NexusMCPFeedback.__init__(self, mcp_context: Any, run: NexusRunContext) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `mcp_context` | `Any` | `required` |
| `run` | `NexusRunContext` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L56)

### `NexusMCPFeedback.progress`

```text
async NexusMCPFeedback.progress(self, progress: float, total: Optional[float]=None, message: str='') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `progress` | `float` | `required` |
| `total` | `Optional[float]` | `None` |
| `message` | `str` | `''` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L82)

### `NexusMCPFeedback.log`

```text
async NexusMCPFeedback.log(self, level: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `level` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L107)


## `NexusMCPContext`

One FastMCP request&#x27;s Nexus run, Workspace, Terminal and feedback APIs.

### `NexusMCPContext.__init__`

```text
NexusMCPContext.__init__(self, mcp_context: Any, run: NexusRunContext) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `mcp_context` | `Any` | `required` |
| `run` | `NexusRunContext` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L127)


### `CurrentNexusMCP`

```text
CurrentNexusMCP(config: Optional[NexusReportingConfig]=None) -> Any
```

Inject a combined FastMCP and Nexus hosted-run context.

| Parameter | Type | Default |
| --- | --- | --- |
| `config` | `Optional[NexusReportingConfig]` | `None` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L145)


### `CurrentNexusRun`

```text
CurrentNexusRun(config: Optional[NexusReportingConfig]=None) -> Any
```

Inject a request-scoped Nexus run into a FastMCP tool.

FastMCP remains optional: its dependency APIs are imported only when this
helper is called.

| Parameter | Type | Default |
| --- | --- | --- |
| `config` | `Optional[NexusReportingConfig]` | `None` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L170)


## `FastMCPBridgeError`

Bases: `Exception`. Inherited behavior is defined on the base class.

FastMCP dependency, configuration, discovery, or lifecycle failure.


## `FastMCPToolError`

Bases: `FastMCPBridgeError`. Inherited behavior is defined on the base class.

A mapped FastMCP tool returned an error.


## `FastMCPToolMapping`

Expose one FastMCP tool as one Nexus capability route.

| Field | Type | Default |
| --- | --- | --- |
| `tool` | `str` | `required` |
| `capability` | `CapabilityRegistration` | `required` |


## `FastMCPTool`

Bounded, JSON-compatible metadata discovered from FastMCP.

| Field | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `title` | `Optional[str]` | `required` |
| `description` | `Optional[str]` | `required` |
| `input_schema` | `Mapping[str, Any]` | `required` |
| `output_schema` | `Optional[Mapping[str, Any]]` | `required` |


### `fastmcp_result_to_json`

```text
fastmcp_result_to_json(result: Any) -> Any
```

Convert a FastMCP ``CallToolResult`` into a JSON response body.

| Parameter | Type | Default |
| --- | --- | --- |
| `result` | `Any` | `required` |

Direct raises (not exhaustive): `FastMCPToolError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L291)


## `FastMCPBridge`

Map enumerated FastMCP tools to Nexus capabilities.

``mappings`` may be a ``tool_name -&gt; CapabilityRegistration`` mapping or
an iterable of :class:`FastMCPToolMapping`.  Only explicitly mapped tools
are exposed to Nexus; unmapped FastMCP tools remain private.

### `FastMCPBridge.__init__`

```text
FastMCPBridge.__init__(self, mcp: Any, server: NexusAgentServer, mappings: Any, *, call_timeout: Optional[float]=30.0, pass_nexus_metadata: bool=True, max_stream_events: int=256, max_progress_message_chars: int=1024, client_factory: Optional[Callable[[Any], Any]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `mcp` | `Any` | `required` |
| `server` | `NexusAgentServer` | `required` |
| `mappings` | `Any` | `required` |
| `call_timeout` | `Optional[float]` | `30.0` |
| `pass_nexus_metadata` | `bool` | `True` |
| `max_stream_events` | `int` | `256` |
| `max_progress_message_chars` | `int` | `1024` |
| `client_factory` | `Optional[Callable[[Any], Any]]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L376)

### `FastMCPBridge.mappings`

```text
FastMCPBridge.mappings: Tuple[FastMCPToolMapping, ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L448)

### `FastMCPBridge.capabilities`

```text
FastMCPBridge.capabilities: Tuple[CapabilityRegistration, ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L452)

### `FastMCPBridge.tools`

```text
FastMCPBridge.tools: Tuple[FastMCPTool, ...]
```

The full FastMCP tool catalog captured during ``start()``.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L456)

### `FastMCPBridge.started`

```text
FastMCPBridge.started: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L462)

### `FastMCPBridge.is_healthy`

```text
FastMCPBridge.is_healthy(self) -> bool
```

Return whether the Tool bridge and Agent listener are both live.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L465)

### `FastMCPBridge.start`

```text
FastMCPBridge.start(self) -> 'FastMCPBridge'
```

Open the in-memory FastMCP client, enumerate, validate, and attach.

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L585)

### `FastMCPBridge.stop`

```text
FastMCPBridge.stop(self) -> None
```

Detach Nexus handlers and close the FastMCP client.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L623)

### `FastMCPBridge.call_tool_sync`

```text
FastMCPBridge.call_tool_sync(self, tool: str, arguments: Mapping[str, Any], *, meta: Optional[Mapping[str, Any]]=None) -> Any
```

Call a mapped FastMCP tool from synchronous application code.

| Parameter | Type | Default |
| --- | --- | --- |
| `tool` | `str` | `required` |
| `arguments` | `Mapping[str, Any]` | `required` |
| `meta` | `Optional[Mapping[str, Any]]` | `None` |

Direct raises (not exhaustive): `FastMCPToolError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L723)

### `FastMCPBridge.call_tool`

```text
async FastMCPBridge.call_tool(self, tool: str, arguments: Mapping[str, Any], *, meta: Optional[Mapping[str, Any]]=None) -> Any
```

Asynchronously call a mapped tool through the shared FastMCP client.

| Parameter | Type | Default |
| --- | --- | --- |
| `tool` | `str` | `required` |
| `arguments` | `Mapping[str, Any]` | `required` |
| `meta` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L740)

### `FastMCPBridge.call_tool_stream`

```text
FastMCPBridge.call_tool_stream(self, tool: str, arguments: Mapping[str, Any], *, meta: Optional[Mapping[str, Any]]=None) -> Iterator[SseEvent]
```

Yield bounded MCP progress notifications and one terminal event.

| Parameter | Type | Default |
| --- | --- | --- |
| `tool` | `str` | `required` |
| `arguments` | `Mapping[str, Any]` | `required` |
| `meta` | `Optional[Mapping[str, Any]]` | `None` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L752)

### `FastMCPBridge.handle`

```text
FastMCPBridge.handle(self, envelope: AgentEnvelope) -> Any
```

Nexus server handler that dispatches an Envelope to its mapped tool.

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `AgentEnvelope` | `required` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L866)

### `FastMCPBridge.handle_stream`

```text
FastMCPBridge.handle_stream(self, envelope: AgentEnvelope) -> Iterator[SseEvent]
```

Nexus SSE handler for one mapped FastMCP Tool call.

| Parameter | Type | Default |
| --- | --- | --- |
| `envelope` | `AgentEnvelope` | `required` |

Direct raises (not exhaustive): `AgentRequestError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L901)

### `FastMCPBridge.registered`

```text
FastMCPBridge.registered(self, client: NexusAgentClient, *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> Iterator[Tuple[AgentLease, ...]]
```

Start the bridge and keep all mapped Nexus routes registered.

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L915)

### `FastMCPBridge.serve_registered`

```text
FastMCPBridge.serve_registered(self, client: NexusAgentClient, *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> None
```

Register mapped capabilities and serve Nexus invokes forever.

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `NexusAgentClient` | `required` |
| `auto_renew` | `bool` | `True` |
| `renew_fraction` | `float` | `0.6` |
| `health_check` | `Optional[Callable[[], bool]]` | `None` |
| `reregister_on_not_found` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L940)


## `NexusMCPServer`

Production-oriented FastMCP facade for Nexus-hosted Docker Agents.

### `NexusMCPServer.__init__`

```text
NexusMCPServer.__init__(self, name: str, *, legacy_sse: bool=False, **options: Any) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `legacy_sse` | `bool` | `False` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1019)

### `NexusMCPServer.fastmcp`

```text
NexusMCPServer.fastmcp: Any
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1033)

### `NexusMCPServer.tool`

```text
NexusMCPServer.tool(self, function: Any=None, *, name: Optional[str]=None, task: bool=False, continuable: bool=False, demo: bool=False, chat: bool=False, interactive: bool=False, mobile_scopes: Optional[Sequence[str]]=None, slash_command: Optional[str]=None, slash_description: Optional[str]=None, execution_profiles: Optional[Sequence[NexusExecutionProfile]]=None, input_modalities: Optional[Sequence[str]]=None, **options: Any) -> Any
```

Register a FastMCP tool and its Nexus execution policy.

| Parameter | Type | Default |
| --- | --- | --- |
| `function` | `Any` | `None` |
| `name` | `Optional[str]` | `None` |
| `task` | `bool` | `False` |
| `continuable` | `bool` | `False` |
| `demo` | `bool` | `False` |
| `chat` | `bool` | `False` |
| `interactive` | `bool` | `False` |
| `mobile_scopes` | `Optional[Sequence[str]]` | `None` |
| `slash_command` | `Optional[str]` | `None` |
| `slash_description` | `Optional[str]` | `None` |
| `execution_profiles` | `Optional[Sequence[NexusExecutionProfile]]` | `None` |
| `input_modalities` | `Optional[Sequence[str]]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1039)

### `NexusMCPServer.nexus_tool_policy`

```text
NexusMCPServer.nexus_tool_policy: Mapping[str, Mapping[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1134)

### `NexusMCPServer.enable_workspace_tools`

```text
NexusMCPServer.enable_workspace_tools(self, scopes: Any) -> 'NexusMCPServer'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `scopes` | `Any` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1137)

### `NexusMCPServer.http_app`

```text
NexusMCPServer.http_app(self, *, legacy_sse: Optional[bool]=None) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `legacy_sse` | `Optional[bool]` | `None` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1271)

### `NexusMCPServer.run`

```text
NexusMCPServer.run(self, *, transport: str='streamable-http', host: str='127.0.0.1', port: int=8000, legacy_sse: Optional[bool]=None, **options: Any) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `transport` | `str` | `'streamable-http'` |
| `host` | `str` | `'127.0.0.1'` |
| `port` | `int` | `8000` |
| `legacy_sse` | `Optional[bool]` | `None` |

Direct raises (not exhaustive): `FastMCPBridgeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/fastmcp.py#L1287)

