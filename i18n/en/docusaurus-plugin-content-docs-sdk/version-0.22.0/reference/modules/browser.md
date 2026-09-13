---
title: "browser API"
---

# browser API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusBrowserError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

A browser operation could not be completed.


## `NexusBrowserUnavailable`

Bases: `NexusBrowserError`. Inherited behavior is defined on the base class.

Playwright or a usable Chrome installation is unavailable.


## `NexusBrowserComputerRequired`

Bases: `NexusBrowserUnavailable`. Inherited behavior is defined on the base class.

The caller must attach a Computer before browser automation can start.


## `NexusBrowserPermissionRequired`

Bases: `NexusBrowserUnavailable`. Inherited behavior is defined on the base class.

The caller has not granted browser.control for this Run.


## `NexusBrowserTunnelUnavailable`

Bases: `NexusBrowserUnavailable`. Inherited behavior is defined on the base class.

Cloud could not establish the protected CDP tunnel.


## `NexusBrowserActionFailed`

Bases: `NexusBrowserError`. Inherited behavior is defined on the base class.

Chrome rejected or failed an action.


## `NexusBrowserStaleObservation`

Bases: `NexusBrowserActionFailed`. Inherited behavior is defined on the base class.

An element reference belongs to an older page observation.


## `NexusBrowserSessionLost`

Bases: `NexusBrowserError`. Inherited behavior is defined on the base class.

Chrome exited and the Run&#x27;s page state could not be recovered.


## `NexusBrowserNode`

| Field | Type | Default |
| --- | --- | --- |
| `ref` | `str` | `required` |
| `tag` | `str` | `required` |
| `role` | `str` | `''` |
| `name` | `str` | `field(default='', repr=False)` |
| `text` | `str` | `field(default='', repr=False)` |
| `selector` | `str` | `field(default='', repr=False)` |
| `bounds` | `Tuple[float, float, float, float]` | `(0.0, 0.0, 0.0, 0.0)` |
| `disabled` | `bool` | `False` |
| `checked` | `Optional[bool]` | `None` |
| `selected` | `Optional[bool]` | `None` |
| `expanded` | `Optional[bool]` | `None` |


## `NexusBrowserDOMSnapshot`

| Field | Type | Default |
| --- | --- | --- |
| `revision` | `int` | `required` |
| `nodes` | `Tuple[NexusBrowserNode, ...]` | `()` |
| `truncated` | `bool` | `False` |

### `NexusBrowserDOMSnapshot.by_ref`

```text
NexusBrowserDOMSnapshot.by_ref(self, ref: str) -> Optional[NexusBrowserNode]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `ref` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L79)


## `NexusBrowserObservation`

| Field | Type | Default |
| --- | --- | --- |
| `observation_id` | `str` | `required` |
| `revision` | `int` | `required` |
| `url` | `str` | `required` |
| `title` | `str` | `required` |
| `viewport` | `Tuple[int, int]` | `required` |
| `image` | `bytes` | `field(repr=False)` |
| `content_type` | `str` | `'image/jpeg'` |
| `dom` | `NexusBrowserDOMSnapshot` | `field(default_factory=lambda: NexusBrowserDOMSnapshot(0), repr=False)` |

### `NexusBrowserObservation.html`

```text
NexusBrowserObservation.html(self) -> str
```

Return the sanitized, bounded HTML captured with this observation.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L95)


## `NexusBrowserAction`

| Field | Type | Default |
| --- | --- | --- |
| `kind` | `str` | `required` |
| `parameters` | `Mapping[str, Any]` | `field(default_factory=dict, repr=False)` |
| `expected_revision` | `Optional[int]` | `None` |


### `close_browser_worker`

```text
close_browser_worker() -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L416)


## `NexusBrowserLocator`

### `NexusBrowserLocator.__init__`

```text
NexusBrowserLocator.__init__(self, session: 'NexusBrowserSession', target: str, *, is_ref: bool, revision: Optional[int]) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `session` | `'NexusBrowserSession'` | `required` |
| `target` | `str` | `required` |
| `is_ref` | `bool` | `required` |
| `revision` | `Optional[int]` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L506)

### `NexusBrowserLocator.click`

```text
NexusBrowserLocator.click(self, *, timeout: float=30.0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L521)

### `NexusBrowserLocator.fill`

```text
NexusBrowserLocator.fill(self, value: str, *, timeout: float=30.0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `required` |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L528)

### `NexusBrowserLocator.select`

```text
NexusBrowserLocator.select(self, value: str, *, timeout: float=30.0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `required` |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L535)


## `NexusBrowserSession`

### `NexusBrowserSession.__init__`

```text
NexusBrowserSession.__init__(self, *, run_id: str, publisher: Callable[[NexusBrowserObservation, str, str], None], viewport: Sequence[int]=(1280, 720)) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `run_id` | `str` | `required` |
| `publisher` | `Callable[[NexusBrowserObservation, str, str], None]` | `required` |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

Direct raises (not exhaustive): `NexusBrowserUnavailable`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L544)

### `NexusBrowserSession.revision`

```text
NexusBrowserSession.revision: Optional[int]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L559)

### `NexusBrowserSession.open`

```text
NexusBrowserSession.open(self, url: str, *, timeout: float=30.0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `url` | `str` | `required` |
| `timeout` | `float` | `30.0` |

Direct raises (not exhaustive): `NexusBrowserActionFailed`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L577)

### `NexusBrowserSession.observe`

```text
NexusBrowserSession.observe(self) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L604)

### `NexusBrowserSession.locator`

```text
NexusBrowserSession.locator(self, target: str, *, ref: bool=False) -> NexusBrowserLocator
```

| Parameter | Type | Default |
| --- | --- | --- |
| `target` | `str` | `required` |
| `ref` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L607)

### `NexusBrowserSession.element`

```text
NexusBrowserSession.element(self, ref: str) -> NexusBrowserLocator
```

| Parameter | Type | Default |
| --- | --- | --- |
| `ref` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L615)

### `NexusBrowserSession.perform`

```text
NexusBrowserSession.perform(self, action: NexusBrowserAction) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `action` | `NexusBrowserAction` | `required` |

Direct raises (not exhaustive): `NexusBrowserActionFailed`, `NexusBrowserStaleObservation`, `TypeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L618)

### `NexusBrowserSession.click`

```text
NexusBrowserSession.click(self, *, x: float, y: float) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `x` | `float` | `required` |
| `y` | `float` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L680)

### `NexusBrowserSession.scroll`

```text
NexusBrowserSession.scroll(self, *, delta_y: float, delta_x: float=0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `delta_y` | `float` | `required` |
| `delta_x` | `float` | `0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L685)

### `NexusBrowserSession.type`

```text
NexusBrowserSession.type(self, text: str) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L692)

### `NexusBrowserSession.drag`

```text
NexusBrowserSession.drag(self, *, from_x: float, from_y: float, to_x: float, to_y: float, steps: int=10) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `from_x` | `float` | `required` |
| `from_y` | `float` | `required` |
| `to_x` | `float` | `required` |
| `to_y` | `float` | `required` |
| `steps` | `int` | `10` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L697)

### `NexusBrowserSession.close`

```text
NexusBrowserSession.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L718)


## `NexusAttachedBrowserSession`

Bases: `NexusBrowserSession`. Inherited behavior is defined on the base class.

Run-scoped browser hosted by the caller&#x27;s Attached Computer.

### `NexusAttachedBrowserSession.__init__`

```text
NexusAttachedBrowserSession.__init__(self, *, run_id: str, requester: Callable[[str, Mapping[str, Any]], Mapping[str, Any]], viewport: Sequence[int]=(1280, 720)) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `run_id` | `str` | `required` |
| `requester` | `Callable[[str, Mapping[str, Any]], Mapping[str, Any]]` | `required` |
| `viewport` | `Sequence[int]` | `(1280, 720)` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L725)

### `NexusAttachedBrowserSession.open`

```text
NexusAttachedBrowserSession.open(self, url: str, *, timeout: float=30.0) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `url` | `str` | `required` |
| `timeout` | `float` | `30.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L787)

### `NexusAttachedBrowserSession.observe`

```text
NexusAttachedBrowserSession.observe(self) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L790)

### `NexusAttachedBrowserSession.perform`

```text
NexusAttachedBrowserSession.perform(self, action: NexusBrowserAction) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `action` | `NexusBrowserAction` | `required` |

Direct raises (not exhaustive): `TypeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L793)

### `NexusAttachedBrowserSession.close`

```text
NexusAttachedBrowserSession.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L804)


## `NexusAsyncBrowserLocator`

### `NexusAsyncBrowserLocator.__init__`

```text
NexusAsyncBrowserLocator.__init__(self, sync: NexusBrowserLocator) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `NexusBrowserLocator` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L810)

### `NexusAsyncBrowserLocator.click`

```text
async NexusAsyncBrowserLocator.click(self, **options: Any) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L813)

### `NexusAsyncBrowserLocator.fill`

```text
async NexusAsyncBrowserLocator.fill(self, value: str, **options: Any) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L816)

### `NexusAsyncBrowserLocator.select`

```text
async NexusAsyncBrowserLocator.select(self, value: str, **options: Any) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L819)


## `NexusAsyncBrowserSession`

### `NexusAsyncBrowserSession.__init__`

```text
NexusAsyncBrowserSession.__init__(self, sync: NexusBrowserSession) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `NexusBrowserSession` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L824)

### `NexusAsyncBrowserSession.revision`

```text
NexusAsyncBrowserSession.revision: Optional[int]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L828)

### `NexusAsyncBrowserSession.open`

```text
async NexusAsyncBrowserSession.open(self, url: str, **options: Any) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `url` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L831)

### `NexusAsyncBrowserSession.observe`

```text
async NexusAsyncBrowserSession.observe(self) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L834)

### `NexusAsyncBrowserSession.locator`

```text
NexusAsyncBrowserSession.locator(self, target: str, *, ref: bool=False) -> NexusAsyncBrowserLocator
```

| Parameter | Type | Default |
| --- | --- | --- |
| `target` | `str` | `required` |
| `ref` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L837)

### `NexusAsyncBrowserSession.element`

```text
NexusAsyncBrowserSession.element(self, ref: str) -> NexusAsyncBrowserLocator
```

| Parameter | Type | Default |
| --- | --- | --- |
| `ref` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L840)

### `NexusAsyncBrowserSession.perform`

```text
async NexusAsyncBrowserSession.perform(self, action: NexusBrowserAction) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `action` | `NexusBrowserAction` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L843)

### `NexusAsyncBrowserSession.click`

```text
async NexusAsyncBrowserSession.click(self, **options: Any) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L846)

### `NexusAsyncBrowserSession.scroll`

```text
async NexusAsyncBrowserSession.scroll(self, **options: Any) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L849)

### `NexusAsyncBrowserSession.type`

```text
async NexusAsyncBrowserSession.type(self, text: str) -> NexusBrowserObservation
```

| Parameter | Type | Default |
| --- | --- | --- |
| `text` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L852)

### `NexusAsyncBrowserSession.drag`

```text
async NexusAsyncBrowserSession.drag(self, **options: Any) -> NexusBrowserObservation
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L855)

### `NexusAsyncBrowserSession.close`

```text
async NexusAsyncBrowserSession.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py#L858)

