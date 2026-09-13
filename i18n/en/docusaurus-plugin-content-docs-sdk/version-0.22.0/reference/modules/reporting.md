---
title: "reporting API"
---

# reporting API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusComputerError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A caller-owned Computer operation could not be completed.

### `NexusComputerError.__init__`

```text
NexusComputerError.__init__(self, message: str, *, code: str='WORKSPACE_UNAVAILABLE') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `str` | `required` |
| `code` | `str` | `'WORKSPACE_UNAVAILABLE'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L58)


## `NexusMemoryError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A caller-scoped Memory operation could not be completed.


## `NexusMemoryConflict`

Bases: `NexusMemoryError`. Inherited behavior is defined on the base class.

The Memory changed after it was recalled by this Run.

### `NexusMemoryConflict.__init__`

```text
NexusMemoryConflict.__init__(self, *, current_revision: int) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `current_revision` | `int` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L76)


## `NexusMemoryUnavailable`

Bases: `NexusMemoryError`. Inherited behavior is defined on the base class.

The run-scoped Memory service is unavailable or not authorized.


## `NexusRecoveryError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A platform-managed operation could not be journaled or replayed safely.


## `NexusRecoveryDiverged`

Bases: `NexusRecoveryError`. Inherited behavior is defined on the base class.

Replay reached a different operation than the original attempt.


## `NexusChatError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A run-scoped interactive Chat operation failed.


## `NexusChatTimeout`

Bases: `NexusChatError`. Inherited behavior is defined on the base class.

The caller did not answer before the interaction expired.


## `NexusChatUnavailable`

Bases: `NexusChatError`. Inherited behavior is defined on the base class.

Interactive Chat is unavailable for this Run or transport.


## `NexusRunCancelled`

Bases: `NexusChatError`. Inherited behavior is defined on the base class.

The Nexus invocation was cancelled while waiting for input.


## `NexusCheckpointError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A durable run checkpoint could not be read or written.


## `NexusRunContextExchangeError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

An OpenWrt IPv6 invocation could not establish its cloud Run context.

### `NexusRunContextExchangeError.__init__`

```text
NexusRunContextExchangeError.__init__(self, message: str, *, code: str='RUN_CONTEXT_EXCHANGE_FAILED') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `str` | `required` |
| `code` | `str` | `'RUN_CONTEXT_EXCHANGE_FAILED'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L116)


## `NexusRunContextUnavailable`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

The current invocation did not provide its read-only Run context.


## `NexusBillingReportError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A final Agent-reported cost could not be accepted by Nexus Cloud.


## `NexusBillingUnavailable`

Bases: `NexusBillingReportError`. Inherited behavior is defined on the base class.

This Run does not include an Agent-reported billing context.


## `NexusUsageError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

Actual model usage could not be recorded for this Run.


## `NexusUsageUnavailable`

Bases: `NexusUsageError`. Inherited behavior is defined on the base class.

The hosted Run did not provide an authenticated usage endpoint.


## `NexusBillingLineItem`

Bases: `TypedDict`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `code` | `str` | `required` |
| `description` | `str` | `required` |
| `amount` | `Union[Decimal, int, str]` | `required` |


## `NexusMobileError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A caller-owned Mobile operation could not be completed.


## `NexusMobileUnavailable`

Bases: `NexusMobileError`. Inherited behavior is defined on the base class.

No authorized, online Mobile is available for this Run.


## `NexusMobilePermissionRequired`

Bases: `NexusMobileError`. Inherited behavior is defined on the base class.

The caller did not grant the requested Mobile capability.


## `NexusMobileBusy`

Bases: `NexusMobileError`. Inherited behavior is defined on the base class.

Another Run currently owns the selected Mobile control lease.


## `NexusMobileTimeout`

Bases: `NexusMobileError`. Inherited behavior is defined on the base class.

The Mobile command did not finish before its timeout.


## `NexusMobileActionFailed`

Bases: `NexusMobileError`. Inherited behavior is defined on the base class.

The Mobile device rejected or failed an action.

### `NexusMobileActionFailed.__init__`

```text
NexusMobileActionFailed.__init__(self, message: str, *, code: str='MOBILE_ACTION_FAILED') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `str` | `required` |
| `code` | `str` | `'MOBILE_ACTION_FAILED'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L180)


## `NexusMemoryItem`

Bases: `TypedDict`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | `required` |
| `kind` | `str` | `required` |
| `text` | `str` | `required` |
| `content` | `Dict[str, Any]` | `required` |
| `scope` | `str` | `required` |
| `confidence` | `str` | `required` |
| `sensitivity` | `str` | `required` |
| `consent` | `str` | `required` |
| `license` | `str` | `required` |
| `revision` | `int` | `required` |
| `created_at` | `str` | `required` |
| `updated_at` | `str` | `required` |


## `MemoryDeleteResult`

Bases: `TypedDict`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | `required` |
| `deleted` | `bool` | `required` |
| `revision` | `int` | `required` |


## `NexusChatReply`

| Field | Type | Default |
| --- | --- | --- |
| `interaction_id` | `str` | `required` |
| `key` | `str` | `required` |
| `value` | `str` | `required` |
| `text` | `str` | `required` |
| `answered_at` | `str` | `''` |


## `NexusCheckpoint`

| Field | Type | Default |
| --- | --- | --- |
| `stage` | `str` | `required` |
| `data` | `Dict[str, Any]` | `required` |
| `revision` | `int` | `required` |
| `updated_at` | `str` | `''` |


## `ctx.execution`

| Field | Type | Default |
| --- | --- | --- |
| `profile` | `str` | `''` |
| `model` | `str` | `''` |
| `reasoning_effort` | `str` | `''` |
| `context_window` | `Optional[int]` | `None` |


## `ctx.input`

Access through `ctx.input`; do not import the implementation class.

Safe metadata for immutable files attached to the current Run.

### `ctx.input.__init__`

```text
ctx.input.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L234)

### `ctx.input.files`

```text
ctx.input.files: list[Dict[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L238)

### `ctx.input.audio`

```text
ctx.input.audio: list[Dict[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L242)


## `NexusMobileStatus`

| Field | Type | Default |
| --- | --- | --- |
| `enabled` | `bool` | `required` |
| `available` | `bool` | `required` |
| `platform` | `str` | `''` |
| `status` | `str` | `'unavailable'` |
| `capabilities` | `Tuple[str, ...]` | `()` |


## `NexusMobileObservation`

| Field | Type | Default |
| --- | --- | --- |
| `data` | `Dict[str, Any]` | `field(default_factory=dict, repr=False)` |


## `NexusMobileScreen`

| Field | Type | Default |
| --- | --- | --- |
| `content` | `bytes` | `field(repr=False)` |
| `content_type` | `str` | `'image/webp'` |
| `width` | `Optional[int]` | `None` |
| `height` | `Optional[int]` | `None` |


## `NexusMobileCommandResult`

| Field | Type | Default |
| --- | --- | --- |
| `command_id` | `str` | `required` |
| `action` | `str` | `required` |
| `status` | `str` | `required` |
| `result` | `Dict[str, Any]` | `field(default_factory=dict, repr=False)` |


## `NexusReportingConfig`

Bounded, fail-open delivery settings for AG-UI events.

| Field | Type | Default |
| --- | --- | --- |
| `queue_size` | `int` | `256` |
| `request_timeout` | `float` | `3.0` |
| `max_retries` | `int` | `2` |
| `flush_timeout` | `float` | `5.0` |
| `retry_delay` | `float` | `0.25` |
| `control_poll_interval` | `float` | `5.0` |
| `outbox_directory` | `str` | `''` |
| `outbox_max_bytes` | `int` | `8 * 1024 * 1024` |


## `DeliveryReport`

| Field | Type | Default |
| --- | --- | --- |
| `enabled` | `bool` | `required` |
| `sent` | `int` | `required` |
| `failed` | `int` | `required` |
| `dropped` | `int` | `required` |
| `pending` | `int` | `required` |
| `last_error` | `str` | `''` |
| `buffered` | `int` | `0` |


## `ctx.trace`

Access through `ctx.trace`; do not import the implementation class.

### `ctx.trace.__init__`

```text
ctx.trace.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L534)

### `ctx.trace.step`

```text
ctx.trace.step(self, name: str, *, visibility: str='public') -> Iterator[None]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L538)

### `ctx.trace.tool`

```text
ctx.trace.tool(self, name: str, *, arguments: Any=None, visibility: str='public') -> _ToolTrace
```

| Parameter | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `arguments` | `Any` | `None` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L554)


## `ctx.plan`

Access through `ctx.plan`; do not import the implementation class.

### `ctx.plan.__init__`

```text
ctx.plan.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L581)

### `ctx.plan.set`

```text
ctx.plan.set(self, steps: Sequence[Mapping[str, Any]], *, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `steps` | `Sequence[Mapping[str, Any]]` | `required` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L585)

### `ctx.plan.update`

```text
ctx.plan.update(self, step_id: str, *, status: Any=_UNSET, title: Any=_UNSET, detail: Any=_UNSET, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `step_id` | `str` | `required` |
| `status` | `Any` | `_UNSET` |
| `title` | `Any` | `_UNSET` |
| `detail` | `Any` | `_UNSET` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L619)


## `ctx.display`

Access through `ctx.display`; do not import the implementation class.

### `ctx.display.__init__`

```text
ctx.display.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L662)

### `ctx.display.title`

```text
ctx.display.title(self, value: Any, *, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Any` | `required` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L665)


## `ctx.shell`

Access through `ctx.shell`; do not import the implementation class.

### `ctx.shell.__init__`

```text
ctx.shell.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L682)

### `ctx.shell.write`

```text
ctx.shell.write(self, message: Any, *, stream: str='stdout', command_id: str='', visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `Any` | `required` |
| `stream` | `str` | `'stdout'` |
| `command_id` | `str` | `''` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L685)


## `ctx.browser`

Access through `ctx.browser`; do not import the implementation class.

### `ctx.browser.__init__`

```text
ctx.browser.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L719)

### `ctx.browser.frame`

```text
ctx.browser.frame(self, image: Union[str, os.PathLike[str], bytes, bytearray, memoryview], *, url: str='', title: str='', text: str='', content_type: str='', width: Optional[int]=None, height: Optional[int]=None, observation_id: str='', revision: Optional[int]=None, action: str='', action_status: str='', dom_node_count: Optional[int]=None, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `image` | `Union[str, os.PathLike[str], bytes, bytearray, memoryview]` | `required` |
| `url` | `str` | `''` |
| `title` | `str` | `''` |
| `text` | `str` | `''` |
| `content_type` | `str` | `''` |
| `width` | `Optional[int]` | `None` |
| `height` | `Optional[int]` | `None` |
| `observation_id` | `str` | `''` |
| `revision` | `Optional[int]` | `None` |
| `action` | `str` | `''` |
| `action_status` | `str` | `''` |
| `dom_node_count` | `Optional[int]` | `None` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L722)

### `ctx.browser.session`

```text
ctx.browser.session(self, *, viewport: Sequence[int]=(1280, 720)) -> NexusBrowserSession
```

| Parameter | Type | Default |
| --- | --- | --- |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L815)

### `ctx.browser.attached_session`

```text
ctx.browser.attached_session(self, *, viewport: Sequence[int]=(1280, 720)) -> NexusAttachedBrowserSession
```

| Parameter | Type | Default |
| --- | --- | --- |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

Direct raises (not exhaustive): `NexusBrowserUnavailable`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L826)


## `ctx.chat`

Access through `ctx.chat`; do not import the implementation class.

### `ctx.chat.__init__`

```text
ctx.chat.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L870)

### `ctx.chat.enabled`

```text
ctx.chat.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L874)

### `ctx.chat.say`

```text
ctx.chat.say(self, message: Any, *, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `Any` | `required` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L880)

### `ctx.chat.ask`

```text
ctx.chat.ask(self, prompt: str, *, key: str, choices: Optional[Sequence[Mapping[str, Any]]]=None, kind: str='', timeout: int=300, visibility: str='public') -> NexusChatReply
```

| Parameter | Type | Default |
| --- | --- | --- |
| `prompt` | `str` | `required` |
| `key` | `str` | `required` |
| `choices` | `Optional[Sequence[Mapping[str, Any]]]` | `None` |
| `kind` | `str` | `''` |
| `timeout` | `int` | `300` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `NexusChatTimeout`, `NexusChatUnavailable`, `NexusRunCancelled`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L894)


## `NexusExternalOperation`

One optional custom side effect protected by the Run operation journal.

### `NexusExternalOperation.__init__`

```text
NexusExternalOperation.__init__(self, reporter: '_RecoveryReporter', prepared: Mapping[str, Any]) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `reporter` | `'_RecoveryReporter'` | `required` |
| `prepared` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L991)

### `NexusExternalOperation.complete`

```text
NexusExternalOperation.complete(self, result: Optional[Mapping[str, Any]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `result` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1000)


## `ctx.recovery`

Access through `ctx.recovery`; do not import the implementation class.

### `ctx.recovery.__init__`

```text
ctx.recovery.__init__(self, context: 'NexusRunContext', *, managed: bool, attempt: int, is_replay: bool, last_committed_operation: int) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |
| `managed` | `bool` | `required` |
| `attempt` | `int` | `required` |
| `is_replay` | `bool` | `required` |
| `last_committed_operation` | `int` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1005)

### `ctx.recovery.external_operation`

```text
ctx.recovery.external_operation(self, operation_type: str, request: Mapping[str, Any], *, can_reconcile: bool=False) -> Iterator[NexusExternalOperation]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `operation_type` | `str` | `required` |
| `request` | `Mapping[str, Any]` | `required` |
| `can_reconcile` | `bool` | `False` |

Direct raises (not exhaustive): `NexusRecoveryError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1077)

### `ctx.recovery.call`

```text
ctx.recovery.call(self, operation_type: str, request: Mapping[str, Any], callback: Callable[[str], Any], *, can_reconcile: bool=True) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `operation_type` | `str` | `required` |
| `request` | `Mapping[str, Any]` | `required` |
| `callback` | `Callable[[str], Any]` | `required` |
| `can_reconcile` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1097)


## `ctx.aio.recovery`

Access through `ctx.aio.recovery`; do not import the implementation class.

### `ctx.aio.recovery.__init__`

```text
ctx.aio.recovery.__init__(self, sync: _RecoveryReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_RecoveryReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1131)

### `ctx.aio.recovery.managed`

```text
ctx.aio.recovery.managed: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1135)

### `ctx.aio.recovery.attempt`

```text
ctx.aio.recovery.attempt: int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1139)

### `ctx.aio.recovery.is_replay`

```text
ctx.aio.recovery.is_replay: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1143)

### `ctx.aio.recovery.last_committed_operation`

```text
ctx.aio.recovery.last_committed_operation: int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1147)

### `ctx.aio.recovery.call`

```text
async ctx.aio.recovery.call(self, operation_type: str, request: Mapping[str, Any], callback: Callable[[str], Any], *, can_reconcile: bool=True) -> Any
```

| Parameter | Type | Default |
| --- | --- | --- |
| `operation_type` | `str` | `required` |
| `request` | `Mapping[str, Any]` | `required` |
| `callback` | `Callable[[str], Any]` | `required` |
| `can_reconcile` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1150)


## `ctx.checkpoint`

Access through `ctx.checkpoint`; do not import the implementation class.

### `ctx.checkpoint.__init__`

```text
ctx.checkpoint.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1155)

### `ctx.checkpoint.load`

```text
ctx.checkpoint.load(self) -> Optional[NexusCheckpoint]
```

Direct raises (not exhaustive): `NexusCheckpointError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1158)

### `ctx.checkpoint.save`

```text
ctx.checkpoint.save(self, *, stage: str, data: Optional[Mapping[str, Any]]=None, revision: Optional[int]=None) -> NexusCheckpoint
```

| Parameter | Type | Default |
| --- | --- | --- |
| `stage` | `str` | `required` |
| `data` | `Optional[Mapping[str, Any]]` | `None` |
| `revision` | `Optional[int]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1171)


## `ctx.memory`

Access through `ctx.memory`; do not import the implementation class.

### `ctx.memory.__init__`

```text
ctx.memory.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1197)

### `ctx.memory.add`

```text
ctx.memory.add(self, text: str='', *, data: Optional[Mapping[str, Any]]=None, kind: str='fact', confidence: float=1.0, sensitivity: str='internal', consent: str='pending', license: str='unknown', scope: str='caller', visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `''` |
| `data` | `Optional[Mapping[str, Any]]` | `None` |
| `kind` | `str` | `'fact'` |
| `confidence` | `float` | `1.0` |
| `sensitivity` | `str` | `'internal'` |
| `consent` | `str` | `'pending'` |
| `license` | `str` | `'unknown'` |
| `scope` | `str` | `'caller'` |
| `visibility` | `str` | `'public'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1200)

### `ctx.memory.recall`

```text
ctx.memory.recall(self, *, limit: int=50) -> list[NexusMemoryItem]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `limit` | `int` | `50` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1235)

### `ctx.memory.update`

```text
ctx.memory.update(self, memory_id: str, *, revision: int, text: Any=_UNSET, data: Any=_UNSET, kind: Any=_UNSET, confidence: Any=_UNSET, sensitivity: Any=_UNSET, consent: Any=_UNSET, license: Any=_UNSET) -> NexusMemoryItem
```

| Parameter | Type | Default |
| --- | --- | --- |
| `memory_id` | `str` | `required` |
| `revision` | `int` | `required` |
| `text` | `Any` | `_UNSET` |
| `data` | `Any` | `_UNSET` |
| `kind` | `Any` | `_UNSET` |
| `confidence` | `Any` | `_UNSET` |
| `sensitivity` | `Any` | `_UNSET` |
| `consent` | `Any` | `_UNSET` |
| `license` | `Any` | `_UNSET` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1245)

### `ctx.memory.delete`

```text
ctx.memory.delete(self, memory_id: str, *, revision: int) -> MemoryDeleteResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `memory_id` | `str` | `required` |
| `revision` | `int` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1289)


## `NexusImageReference`

Bases: `TypedDict`. Inherited behavior is defined on the base class.

A protected image belonging to the current Run, not a public URL.

| Field | Type | Default |
| --- | --- | --- |
| `asset_id` | `str` | `required` |
| `content_type` | `str` | `required` |


## `ctx.media`

Access through `ctx.media`; do not import the implementation class.

### `ctx.media.__init__`

```text
ctx.media.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1316)

### `ctx.media.read_image`

```text
ctx.media.read_image(self, reference: Mapping[str, Any]) -> bytes
```

Read an input image using the current Run delegate and Cloud TLS.

| Parameter | Type | Default |
| --- | --- | --- |
| `reference` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `NexusChatUnavailable`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1319)


## `ctx.aio.media`

Access through `ctx.aio.media`; do not import the implementation class.

### `ctx.aio.media.__init__`

```text
ctx.aio.media.__init__(self, media: _MediaReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `media` | `_MediaReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1345)

### `ctx.aio.media.read_image`

```text
async ctx.aio.media.read_image(self, reference: Mapping[str, Any]) -> bytes
```

| Parameter | Type | Default |
| --- | --- | --- |
| `reference` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1348)


## `ctx.output`

Access through `ctx.output`; do not import the implementation class.

### `ctx.output.__init__`

```text
ctx.output.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1353)

### `ctx.output.created`

```text
ctx.output.created(self, path: str, **metadata: Any) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1356)

### `ctx.output.upload_file`

```text
ctx.output.upload_file(self, path, **options) -> not annotated; see contract/source
```

Stream a large immutable output to Cloud; never embed its bytes in AG-UI.

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1359)

### `ctx.output.updated`

```text
ctx.output.updated(self, path: str, **metadata: Any) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1363)

### `ctx.output.image`

```text
ctx.output.image(self, image: Union[str, os.PathLike[str], bytes, bytearray, memoryview], *, content_type: str='image/png', title: str='Image', alt: str='') -> Dict[str, Any]
```

Upload a protected Run image directly to Cloud, never through OpenWrt.

Returns a small Nexus JSON asset reference. No public URL or inline
base64 is placed in the event stream or tool result. Cloud validates the
actual raster bytes and binds the asset to this Run and its caller.

| Parameter | Type | Default |
| --- | --- | --- |
| `image` | `Union[str, os.PathLike[str], bytes, bytearray, memoryview]` | `required` |
| `content_type` | `str` | `'image/png'` |
| `title` | `str` | `'Image'` |
| `alt` | `str` | `''` |

Direct raises (not exhaustive): `NexusChatUnavailable`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1366)

### `ctx.output.ready`

```text
ctx.output.ready(self, result: Any=None, *, visibility: str='public') -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `result` | `Any` | `None` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1396)

### `ctx.output.path`

```text
ctx.output.path(self, path: str) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1411)

### `ctx.output.write_text`

```text
ctx.output.write_text(self, path: str, content: str, *, content_type: str='text/plain', **metadata: Any) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |
| `content` | `str` | `required` |
| `content_type` | `str` | `'text/plain'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1417)


## `ctx.computer`

Access through `ctx.computer`; do not import the implementation class.

### `ctx.computer.__init__`

```text
ctx.computer.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1460)

### `ctx.computer.enabled`

```text
ctx.computer.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1465)

### `ctx.computer.bindings`

```text
ctx.computer.bindings(self) -> Tuple[Mapping[str, Any], ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1468)

### `ctx.computer.bind`

```text
ctx.computer.bind(self, connection_id: str, *, make_default: bool=True) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |
| `make_default` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1473)


## `ctx.computer.connections`

Access through `ctx.computer.connections`; do not import the implementation class.

### `ctx.computer.connections.__init__`

```text
ctx.computer.connections.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1485)

### `ctx.computer.connections.list`

```text
ctx.computer.connections.list(self) -> Tuple[SSHWorkspaceConnection, ...]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1488)

### `ctx.computer.connections.get`

```text
ctx.computer.connections.get(self, connection_id: str) -> SSHWorkspaceConnection
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1493)

### `ctx.computer.connections.create`

```text
ctx.computer.connections.create(self, name: str, ssh_host: str, ssh_user: str, *, auth_mode: str='private_key', ssh_port: int=22, workspace_root: str='~/.nexus', private_key: str='', password: str='', metadata: Optional[Mapping[str, Any]]=None) -> SSHWorkspaceConnection
```

| Parameter | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `ssh_host` | `str` | `required` |
| `ssh_user` | `str` | `required` |
| `auth_mode` | `str` | `'private_key'` |
| `ssh_port` | `int` | `22` |
| `workspace_root` | `str` | `'~/.nexus'` |
| `private_key` | `str` | `''` |
| `password` | `str` | `''` |
| `metadata` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1498)

### `ctx.computer.connections.update`

```text
ctx.computer.connections.update(self, connection_id: str, values: Optional[SSHWorkspaceConnectionUpdate]=None, **changes: Any) -> SSHWorkspaceConnection
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |
| `values` | `Optional[SSHWorkspaceConnectionUpdate]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1540)

### `ctx.computer.connections.delete`

```text
ctx.computer.connections.delete(self, connection_id: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1563)

### `ctx.computer.connections.test`

```text
ctx.computer.connections.test(self, connection_id: str) -> SSHTestResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1567)

### `ctx.computer.connections.validate`

```text
ctx.computer.connections.validate(self, **values: Any) -> SSHTestResult
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1574)


## `ctx.terminal`

Access through `ctx.terminal`; do not import the implementation class.

### `ctx.terminal.__init__`

```text
ctx.terminal.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1583)

### `ctx.terminal.run`

```text
ctx.terminal.run(self, command: str, cwd: str='.', timeout: Optional[int]=None, *, display: bool=True) -> CommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `command` | `str` | `required` |
| `cwd` | `str` | `'.'` |
| `timeout` | `Optional[int]` | `None` |
| `display` | `bool` | `True` |

Direct raises (not exhaustive): `NexusComputerError`, `TypeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1586)

### `ctx.terminal.status`

```text
ctx.terminal.status(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1623)


## `ctx.workspace`

Access through `ctx.workspace`; do not import the implementation class.

### `ctx.workspace.__init__`

```text
ctx.workspace.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1631)

### `ctx.workspace.list`

```text
ctx.workspace.list(self, path: str='.') -> Tuple[WorkspaceEntry, ...]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `'.'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1634)

### `ctx.workspace.read_text`

```text
ctx.workspace.read_text(self, path: str) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1639)

### `ctx.workspace.write_text`

```text
ctx.workspace.write_text(self, path: str, content: str) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |
| `content` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1644)


## `ctx.mobile`

Access through `ctx.mobile`; do not import the implementation class.

### `ctx.mobile.__init__`

```text
ctx.mobile.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1674)

### `ctx.mobile.enabled`

```text
ctx.mobile.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1678)

### `ctx.mobile.status`

```text
ctx.mobile.status(self) -> NexusMobileStatus
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1685)

### `ctx.mobile.observe`

```text
ctx.mobile.observe(self, *, timeout: float=120.0) -> NexusMobileObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1697)

### `ctx.mobile.capture_screen`

```text
ctx.mobile.capture_screen(self, *, timeout: float=120.0) -> NexusMobileScreen
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

Direct raises (not exhaustive): `NexusMobileActionFailed`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1701)

### `ctx.mobile.tap_text`

```text
ctx.mobile.tap_text(self, text: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1715)

### `ctx.mobile.tap`

```text
ctx.mobile.tap(self, *, x: float, y: float, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `x` | `float` | `required` |
| `y` | `float` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1718)

### `ctx.mobile.type_text`

```text
ctx.mobile.type_text(self, text: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1723)

### `ctx.mobile.swipe`

```text
ctx.mobile.swipe(self, start_x: float, start_y: float, end_x: float, end_y: float, *, duration_ms: int=300, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `start_x` | `float` | `required` |
| `start_y` | `float` | `required` |
| `end_x` | `float` | `required` |
| `end_y` | `float` | `required` |
| `duration_ms` | `int` | `300` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1726)

### `ctx.mobile.press_back`

```text
ctx.mobile.press_back(self, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1744)

### `ctx.mobile.open_app`

```text
ctx.mobile.open_app(self, package: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `package` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1747)

### `ctx.mobile.wait_for_state`

```text
ctx.mobile.wait_for_state(self, *, text: str, timeout: float=30.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1750)


## `ctx.aio.computer.connections`

Access through `ctx.aio.computer.connections`; do not import the implementation class.

### `ctx.aio.computer.connections.__init__`

```text
ctx.aio.computer.connections.__init__(self, sync: _ConnectionReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_ConnectionReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1829)

### `ctx.aio.computer.connections.list`

```text
async ctx.aio.computer.connections.list(self) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1832)

### `ctx.aio.computer.connections.get`

```text
async ctx.aio.computer.connections.get(self, connection_id: str) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1835)

### `ctx.aio.computer.connections.create`

```text
async ctx.aio.computer.connections.create(self, *args: Any, **kwargs: Any) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1838)

### `ctx.aio.computer.connections.update`

```text
async ctx.aio.computer.connections.update(self, connection_id: str, values=None, **changes: Any) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |
| `values` | `not annotated` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1841)

### `ctx.aio.computer.connections.delete`

```text
async ctx.aio.computer.connections.delete(self, connection_id: str) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1844)

### `ctx.aio.computer.connections.test`

```text
async ctx.aio.computer.connections.test(self, connection_id: str) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1847)

### `ctx.aio.computer.connections.validate`

```text
async ctx.aio.computer.connections.validate(self, **values: Any) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1850)


## `ctx.aio.computer`

Access through `ctx.aio.computer`; do not import the implementation class.

### `ctx.aio.computer.__init__`

```text
ctx.aio.computer.__init__(self, sync: _ComputerReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_ComputerReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1855)

### `ctx.aio.computer.enabled`

```text
ctx.aio.computer.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1860)

### `ctx.aio.computer.bindings`

```text
async ctx.aio.computer.bindings(self) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1863)

### `ctx.aio.computer.bind`

```text
async ctx.aio.computer.bind(self, connection_id: str, *, make_default: bool=True) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `connection_id` | `str` | `required` |
| `make_default` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1866)


## `ctx.aio.workspace`

Access through `ctx.aio.workspace`; do not import the implementation class.

### `ctx.aio.workspace.__init__`

```text
ctx.aio.workspace.__init__(self, sync: _WorkspaceReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_WorkspaceReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1873)

### `ctx.aio.workspace.list`

```text
async ctx.aio.workspace.list(self, path: str='.') -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `'.'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1876)

### `ctx.aio.workspace.read_text`

```text
async ctx.aio.workspace.read_text(self, path: str) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1879)

### `ctx.aio.workspace.write_text`

```text
async ctx.aio.workspace.write_text(self, path: str, content: str) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |
| `content` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1882)


## `ctx.aio.terminal`

Access through `ctx.aio.terminal`; do not import the implementation class.

### `ctx.aio.terminal.__init__`

```text
ctx.aio.terminal.__init__(self, sync: _TerminalReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_TerminalReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1887)

### `ctx.aio.terminal.run`

```text
async ctx.aio.terminal.run(self, command: str, cwd: str='.', timeout: Optional[int]=None, *, display: bool=True) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `command` | `str` | `required` |
| `cwd` | `str` | `'.'` |
| `timeout` | `Optional[int]` | `None` |
| `display` | `bool` | `True` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1890)

### `ctx.aio.terminal.status`

```text
async ctx.aio.terminal.status(self) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1906)


## `ctx.aio.plan`

Access through `ctx.aio.plan`; do not import the implementation class.

### `ctx.aio.plan.__init__`

```text
ctx.aio.plan.__init__(self, sync: _PlanReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_PlanReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1911)

### `ctx.aio.plan.set`

```text
async ctx.aio.plan.set(self, steps: Sequence[Mapping[str, Any]], *, visibility: str='public') -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `steps` | `Sequence[Mapping[str, Any]]` | `required` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1914)

### `ctx.aio.plan.update`

```text
async ctx.aio.plan.update(self, step_id: str, *, visibility: str='public', **changes: Any) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `step_id` | `str` | `required` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1917)


## `ctx.aio.display`

Access through `ctx.aio.display`; do not import the implementation class.

### `ctx.aio.display.__init__`

```text
ctx.aio.display.__init__(self, sync: _DisplayReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_DisplayReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1924)

### `ctx.aio.display.title`

```text
async ctx.aio.display.title(self, value: Any, *, visibility: str='public') -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Any` | `required` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1927)


## `ctx.aio.shell`

Access through `ctx.aio.shell`; do not import the implementation class.

### `ctx.aio.shell.__init__`

```text
ctx.aio.shell.__init__(self, sync: _ShellReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_ShellReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1932)

### `ctx.aio.shell.write`

```text
async ctx.aio.shell.write(self, message: str, *, stream: str='stdout', visibility: str='public') -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `str` | `required` |
| `stream` | `str` | `'stdout'` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1935)


## `ctx.aio.browser`

Access through `ctx.aio.browser`; do not import the implementation class.

### `ctx.aio.browser.__init__`

```text
ctx.aio.browser.__init__(self, sync: _BrowserReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_BrowserReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1942)

### `ctx.aio.browser.frame`

```text
async ctx.aio.browser.frame(self, image: Union[str, os.PathLike[str], bytes, bytearray], **metadata: Any) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `image` | `Union[str, os.PathLike[str], bytes, bytearray]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1945)

### `ctx.aio.browser.session`

```text
ctx.aio.browser.session(self, *, viewport: Sequence[int]=(1280, 720)) -> NexusAsyncBrowserSession
```

| Parameter | Type | Default |
| --- | --- | --- |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1948)

### `ctx.aio.browser.attached_session`

```text
ctx.aio.browser.attached_session(self, *, viewport: Sequence[int]=(1280, 720)) -> NexusAsyncBrowserSession
```

| Parameter | Type | Default |
| --- | --- | --- |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1955)


## `ctx.aio.chat`

Access through `ctx.aio.chat`; do not import the implementation class.

### `ctx.aio.chat.__init__`

```text
ctx.aio.chat.__init__(self, sync: _ChatReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_ChatReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1966)

### `ctx.aio.chat.say`

```text
async ctx.aio.chat.say(self, text: str, *, visibility: str='public') -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `visibility` | `str` | `'public'` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1969)

### `ctx.aio.chat.ask`

```text
async ctx.aio.chat.ask(self, prompt: str, **options: Any) -> NexusChatReply
```

| Parameter | Type | Default |
| --- | --- | --- |
| `prompt` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1972)


## `ctx.project`

Access through `ctx.project`; do not import the implementation class.

### `ctx.project.__init__`

```text
ctx.project.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1977)

### `ctx.project.id`

```text
ctx.project.id: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1985)

### `ctx.project.name`

```text
ctx.project.name: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1989)

### `ctx.project.instructions`

```text
ctx.project.instructions: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1993)

### `ctx.project.revision`

```text
ctx.project.revision: int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L1997)


## `ctx.run`

Access through `ctx.run`; do not import the implementation class.

### `ctx.run.__init__`

```text
ctx.run.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2002)

### `ctx.run.id`

```text
ctx.run.id: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2006)

### `ctx.run.turn_index`

```text
ctx.run.turn_index: int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2010)

### `ctx.run.messages`

```text
ctx.run.messages(self, *, limit: int=200, refresh: bool=False) -> list[Dict[str, Any]]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `limit` | `int` | `200` |
| `refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2013)


## `ctx.aio.run`

Access through `ctx.aio.run`; do not import the implementation class.

### `ctx.aio.run.__init__`

```text
ctx.aio.run.__init__(self, sync: _RunContextReader) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_RunContextReader` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2021)

### `ctx.aio.run.id`

```text
ctx.aio.run.id: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2025)

### `ctx.aio.run.turn_index`

```text
ctx.aio.run.turn_index: int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2029)

### `ctx.aio.run.messages`

```text
async ctx.aio.run.messages(self, *, limit: int=200, refresh: bool=False) -> list[Dict[str, Any]]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `limit` | `int` | `200` |
| `refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2032)


## `ctx.aio.checkpoint`

Access through `ctx.aio.checkpoint`; do not import the implementation class.

### `ctx.aio.checkpoint.__init__`

```text
ctx.aio.checkpoint.__init__(self, sync: _CheckpointReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_CheckpointReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2037)

### `ctx.aio.checkpoint.load`

```text
async ctx.aio.checkpoint.load(self) -> Optional[NexusCheckpoint]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2040)

### `ctx.aio.checkpoint.save`

```text
async ctx.aio.checkpoint.save(self, *, stage: str, data: Mapping[str, Any], revision: Optional[int]=None) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `stage` | `str` | `required` |
| `data` | `Mapping[str, Any]` | `required` |
| `revision` | `Optional[int]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2043)


## `ctx.aio.mobile`

Access through `ctx.aio.mobile`; do not import the implementation class.

### `ctx.aio.mobile.__init__`

```text
ctx.aio.mobile.__init__(self, sync: '_MobileReporter') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `'_MobileReporter'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2050)

### `ctx.aio.mobile.enabled`

```text
ctx.aio.mobile.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2054)

### `ctx.aio.mobile.status`

```text
async ctx.aio.mobile.status(self) -> NexusMobileStatus
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2057)

### `ctx.aio.mobile.observe`

```text
async ctx.aio.mobile.observe(self, *, timeout: float=120.0) -> NexusMobileObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2060)

### `ctx.aio.mobile.capture_screen`

```text
async ctx.aio.mobile.capture_screen(self, *, timeout: float=120.0) -> NexusMobileScreen
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2063)

### `ctx.aio.mobile.tap_text`

```text
async ctx.aio.mobile.tap_text(self, text: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2066)

### `ctx.aio.mobile.tap`

```text
async ctx.aio.mobile.tap(self, *, x: float, y: float, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `x` | `float` | `required` |
| `y` | `float` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2069)

### `ctx.aio.mobile.type_text`

```text
async ctx.aio.mobile.type_text(self, text: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2072)

### `ctx.aio.mobile.swipe`

```text
async ctx.aio.mobile.swipe(self, start_x: float, start_y: float, end_x: float, end_y: float, *, duration_ms: int=300, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `start_x` | `float` | `required` |
| `start_y` | `float` | `required` |
| `end_x` | `float` | `required` |
| `end_y` | `float` | `required` |
| `duration_ms` | `int` | `300` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2075)

### `ctx.aio.mobile.press_back`

```text
async ctx.aio.mobile.press_back(self, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2086)

### `ctx.aio.mobile.open_app`

```text
async ctx.aio.mobile.open_app(self, package: str, *, timeout: float=120.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `package` | `str` | `required` |
| `timeout` | `float` | `120.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2089)

### `ctx.aio.mobile.wait_for_state`

```text
async ctx.aio.mobile.wait_for_state(self, *, text: str, timeout: float=30.0) -> NexusMobileCommandResult
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2092)


## `ctx.billing`

Access through `ctx.billing`; do not import the implementation class.

### `ctx.billing.__init__`

```text
ctx.billing.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2097)

### `ctx.billing.enabled`

```text
ctx.billing.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2101)

### `ctx.billing.report`

```text
ctx.billing.report(self, *, amount: Union[Decimal, int, str], line_items: Sequence[Mapping[str, Any]]=(), idempotency_key: str) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `amount` | `Union[Decimal, int, str]` | `required` |
| `line_items` | `Sequence[Mapping[str, Any]]` | `()` |
| `idempotency_key` | `str` | `required` |

Direct raises (not exhaustive): `NexusBillingReportError`, `NexusBillingUnavailable`, `TypeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2120)


## `ctx.usage`

Access through `ctx.usage`; do not import the implementation class.

### `ctx.usage.__init__`

```text
ctx.usage.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2209)

### `ctx.usage.enabled`

```text
ctx.usage.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2213)

### `ctx.usage.report`

```text
ctx.usage.report(self, *, model: str, input_tokens: int, output_tokens: int, context_window: int, cached_input_tokens: int=0, reasoning_tokens: int=0, primary: bool=True, event_id: str='') -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `model` | `str` | `required` |
| `input_tokens` | `int` | `required` |
| `output_tokens` | `int` | `required` |
| `context_window` | `int` | `required` |
| `cached_input_tokens` | `int` | `0` |
| `reasoning_tokens` | `int` | `0` |
| `primary` | `bool` | `True` |
| `event_id` | `str` | `''` |

Direct raises (not exhaustive): `NexusUsageError`, `NexusUsageUnavailable`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2222)

### `ctx.usage.gateway_headers`

```text
ctx.usage.gateway_headers(self, *, event_id: str='') -> Dict[str, str]
```

Return short-lived attribution headers for a Nexus model gateway call.

| Parameter | Type | Default |
| --- | --- | --- |
| `event_id` | `str` | `''` |

Direct raises (not exhaustive): `NexusUsageUnavailable`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2263)


## `ctx.aio.usage`

Access through `ctx.aio.usage`; do not import the implementation class.

### `ctx.aio.usage.__init__`

```text
ctx.aio.usage.__init__(self, sync: _UsageReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_UsageReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2282)

### `ctx.aio.usage.enabled`

```text
ctx.aio.usage.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2286)

### `ctx.aio.usage.report`

```text
async ctx.aio.usage.report(self, **values: Any) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2289)

### `ctx.aio.usage.gateway_headers`

```text
ctx.aio.usage.gateway_headers(self, *, event_id: str='') -> Dict[str, str]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `event_id` | `str` | `''` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2292)


## `ctx.aio.billing`

Access through `ctx.aio.billing`; do not import the implementation class.

### `ctx.aio.billing.__init__`

```text
ctx.aio.billing.__init__(self, sync: _BillingReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_BillingReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2297)

### `ctx.aio.billing.enabled`

```text
ctx.aio.billing.enabled: bool
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2301)

### `ctx.aio.billing.report`

```text
async ctx.aio.billing.report(self, *, amount: Union[Decimal, int, str], line_items: Sequence[Mapping[str, Any]]=(), idempotency_key: str) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `amount` | `Union[Decimal, int, str]` | `required` |
| `line_items` | `Sequence[Mapping[str, Any]]` | `()` |
| `idempotency_key` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2304)


## `ctx.aio`

Access through `ctx.aio`; do not import the implementation class.

### `ctx.aio.__init__`

```text
ctx.aio.__init__(self, context: 'NexusRunContext') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `'NexusRunContext'` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2320)

### `ctx.aio.raise_if_cancelled`

```text
async ctx.aio.raise_if_cancelled(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2344)

### `ctx.aio.control`

```text
async ctx.aio.control(self, *, refresh: bool=False) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2347)


## `ctx.aio.output`

Access through `ctx.aio.output`; do not import the implementation class.

### `ctx.aio.output.__init__`

```text
ctx.aio.output.__init__(self, sync: _OutputReporter) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `_OutputReporter` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2352)

### `ctx.aio.output.upload_file`

```text
async ctx.aio.output.upload_file(self, path, **options) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2355)

### `ctx.aio.output.image`

```text
async ctx.aio.output.image(self, image, **metadata) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `image` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2358)

### `ctx.aio.output.write_text`

```text
async ctx.aio.output.write_text(self, path, content, **metadata) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `not annotated` | `required` |
| `content` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2361)

### `ctx.aio.output.ready`

```text
async ctx.aio.output.ready(self, result=None, **metadata) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `result` | `not annotated` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2364)


## `ctx`

One Nexus-hosted invocation&#x27;s fail-open AG-UI reporter.

### `ctx.__init__`

```text
ctx.__init__(self, *, run_id: str='', events_url: str='', token: str='', computer_enabled: bool=False, terminal_url: str='', workspace_url: str='', memory_url: str='', workspace_token: str='', workspace_root: str='', output_root: str='', workspace_delegate_url: str='', workspace_delegate_token: str='', workspace_capabilities: Tuple[str, ...]=(), browser_enabled: bool=False, browser_delegate_url: str='', browser_delegate_token: str='', browser_computer_name: str='', mobile_enabled: bool=False, mobile_delegate_url: str='', mobile_delegate_token: str='', mobile_capabilities: Tuple[str, ...]=(), interaction_url: str='', context_url: str='', context_token: str='', checkpoint_url: str='', recovery_url: str='', recovery_managed: bool=False, recovery_attempt: int=0, recovery_is_replay: bool=False, recovery_last_committed_operation: int=0, display_asset_url: str='', interaction_token: str='', interaction_mode: str='', billing_url: str='', billing_token: str='', billing_currency: str='', billing_max_cost: Union[Decimal, int, str]='0', usage_url: str='', execution_profile: str='', execution_model: str='', reasoning_effort: str='', execution_context_window: Optional[int]=None, input_files: Sequence[Mapping[str, Any]]=(), turn_index: int=1, config: Optional[NexusReportingConfig]=None, _event_sink: Optional[Callable[[Mapping[str, Any]], bool]]=None, _interaction_request: Optional[Callable[[str, str, Optional[Mapping[str, Any]]], Dict[str, Any]]]=None, _asset_uploader: Optional[Callable[[bytes, str, str, Optional[int], Optional[int]], Dict[str, Any]]]=None, _cloud_opener: Optional[Callable[..., Any]]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `run_id` | `str` | `''` |
| `events_url` | `str` | `''` |
| `token` | `str` | `''` |
| `computer_enabled` | `bool` | `False` |
| `terminal_url` | `str` | `''` |
| `workspace_url` | `str` | `''` |
| `memory_url` | `str` | `''` |
| `workspace_token` | `str` | `''` |
| `workspace_root` | `str` | `''` |
| `output_root` | `str` | `''` |
| `workspace_delegate_url` | `str` | `''` |
| `workspace_delegate_token` | `str` | `''` |
| `workspace_capabilities` | `Tuple[str, ...]` | `()` |
| `browser_enabled` | `bool` | `False` |
| `browser_delegate_url` | `str` | `''` |
| `browser_delegate_token` | `str` | `''` |
| `browser_computer_name` | `str` | `''` |
| `mobile_enabled` | `bool` | `False` |
| `mobile_delegate_url` | `str` | `''` |
| `mobile_delegate_token` | `str` | `''` |
| `mobile_capabilities` | `Tuple[str, ...]` | `()` |
| `interaction_url` | `str` | `''` |
| `context_url` | `str` | `''` |
| `context_token` | `str` | `''` |
| `checkpoint_url` | `str` | `''` |
| `recovery_url` | `str` | `''` |
| `recovery_managed` | `bool` | `False` |
| `recovery_attempt` | `int` | `0` |
| `recovery_is_replay` | `bool` | `False` |
| `recovery_last_committed_operation` | `int` | `0` |
| `display_asset_url` | `str` | `''` |
| `interaction_token` | `str` | `''` |
| `interaction_mode` | `str` | `''` |
| `billing_url` | `str` | `''` |
| `billing_token` | `str` | `''` |
| `billing_currency` | `str` | `''` |
| `billing_max_cost` | `Union[Decimal, int, str]` | `'0'` |
| `usage_url` | `str` | `''` |
| `execution_profile` | `str` | `''` |
| `execution_model` | `str` | `''` |
| `reasoning_effort` | `str` | `''` |
| `execution_context_window` | `Optional[int]` | `None` |
| `input_files` | `Sequence[Mapping[str, Any]]` | `()` |
| `turn_index` | `int` | `1` |
| `config` | `Optional[NexusReportingConfig]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2371)

### `ctx.from_env`

```text
ctx.from_env(cls, *, headers: Optional[Mapping[str, Any]]=None, environ: Optional[Mapping[str, str]]=None, config: Optional[NexusReportingConfig]=None, _cloud_opener: Optional[Callable[..., Any]]=None) -> 'NexusRunContext'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `headers` | `Optional[Mapping[str, Any]]` | `None` |
| `environ` | `Optional[Mapping[str, str]]` | `None` |
| `config` | `Optional[NexusReportingConfig]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2564)

### `ctx.from_exchange`

```text
ctx.from_exchange(cls, exchange_url: str, exchange_token: str, *, config: Optional[NexusReportingConfig]=None, cloud_opener: Optional[Callable[..., Any]]=None) -> 'NexusRunContext'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `exchange_url` | `str` | `required` |
| `exchange_token` | `str` | `required` |
| `config` | `Optional[NexusReportingConfig]` | `None` |
| `cloud_opener` | `Optional[Callable[..., Any]]` | `None` |

Direct raises (not exhaustive): `NexusRunContextExchangeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L2752)

### `ctx.control`

```text
ctx.control(self, *, refresh: bool=False) -> Dict[str, Any]
```

Read server deadline/lease/cancellation; no-op outside hosted runs.

Network failure does not invent a cancellation acknowledgement. Platform
delegates independently enforce the server lease and permission expiry.

| Parameter | Type | Default |
| --- | --- | --- |
| `refresh` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3276)

### `ctx.raise_if_cancelled`

```text
ctx.raise_if_cancelled(self) -> None
```

Cooperative cancellation point for long loops and between side effects.

Direct raises (not exhaustive): `NexusRunCancelled`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3294)

### `ctx.emit`

```text
ctx.emit(self, event: Any, *, visibility: str='public', event_id: Optional[str]=None) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `event` | `Any` | `required` |
| `visibility` | `str` | `'public'` |
| `event_id` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3303)

### `ctx.replay_pending`

```text
ctx.replay_pending(self) -> int
```

Requeue unacknowledged IDs for this Run while its lease is active.

Does not resurrect completed Runs or acknowledge delivery without a 2xx.
File retention/volume backup remain the operator&#x27;s responsibility.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3396)

### `ctx.flush`

```text
ctx.flush(self, timeout: Optional[float]=None) -> DeliveryReport
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `Optional[float]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3419)

### `ctx.close`

```text
ctx.close(self) -> DeliveryReport
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3436)

### `ctx.report`

```text
ctx.report(self) -> DeliveryReport
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3443)


### `current_run`

```text
current_run() -> NexusRunContext
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3516)


### `set_current_run`

```text
set_current_run(context: NexusRunContext) -> Token
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `NexusRunContext` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3521)


### `reset_current_run`

```text
reset_current_run(token: Token) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `token` | `Token` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3525)


### `managed_run_context`

```text
managed_run_context(*, headers: Optional[Mapping[str, Any]]=None, config: Optional[NexusReportingConfig]=None) -> Iterator[NexusRunContext]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `headers` | `Optional[Mapping[str, Any]]` | `None` |
| `config` | `Optional[NexusReportingConfig]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py#L3530)

