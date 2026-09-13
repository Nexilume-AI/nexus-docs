---
title: "inbox API"
---

# inbox API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusFollowUpUnavailable`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.


## `RunInput`

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | `required` |
| `content` | `str` | `required` |
| `turn_index` | `int` | `required` |
| `attachments` | `tuple[dict, ...]` | `()` |
| `files` | `tuple[dict, ...]` | `()` |

### `RunInput.acknowledge`

```text
RunInput.acknowledge(self) -> None
```

Call only after the instruction has been incorporated at a safe point.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L24)

### `RunInput.reject`

```text
RunInput.reject(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L28)


## `ctx.inbox`

Bounded memory receiver; Cloud retains messages until explicit acknowledgement.

Polling, reconnection and receipt happen independently of business execution.
Call receive_pending at safe points; do not execute tools on the receiver thread.
Unacknowledged input may be returned again. Applications must use the stable ID
when applying an instruction with effects that are not naturally idempotent.

### `ctx.inbox.__init__`

```text
ctx.inbox.__init__(self, context) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L41)

### `ctx.inbox.configure`

```text
ctx.inbox.configure(self, mode: str='steer_and_queue', *, attachments: bool=False) -> None
```

Opt in only when the handler reads RunInput.attachments/files.

Read images with ctx.media.read_image(ref), files with ctx.files.
References are Run-bound; this method never downloads or executes them.

| Parameter | Type | Default |
| --- | --- | --- |
| `mode` | `str` | `'steer_and_queue'` |
| `attachments` | `bool` | `False` |

Direct raises (not exhaustive): `NexusFollowUpUnavailable`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L59)

### `ctx.inbox.receive_pending`

```text
ctx.inbox.receive_pending(self) -> list[RunInput]
```

Direct raises (not exhaustive): `NexusFollowUpUnavailable`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L117)

### `ctx.inbox.acknowledge`

```text
ctx.inbox.acknowledge(self, message_id: str, *, status: str='applied') -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message_id` | `str` | `required` |
| `status` | `str` | `'applied'` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L126)

### `ctx.inbox.close`

```text
ctx.inbox.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L137)


## `AsyncRunInput`

### `AsyncRunInput.__init__`

```text
AsyncRunInput.__init__(self, item: RunInput) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `item` | `RunInput` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L147)

### `AsyncRunInput.acknowledge`

```text
async AsyncRunInput.acknowledge(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L152)

### `AsyncRunInput.reject`

```text
async AsyncRunInput.reject(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L155)


## `ctx.aio.inbox`

### `ctx.aio.inbox.__init__`

```text
ctx.aio.inbox.__init__(self, sync: RunInbox) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `sync` | `RunInbox` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L160)

### `ctx.aio.inbox.configure`

```text
async ctx.aio.inbox.configure(self, mode: str='steer_and_queue', *, attachments: bool=False) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `mode` | `str` | `'steer_and_queue'` |
| `attachments` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L163)

### `ctx.aio.inbox.receive_pending`

```text
async ctx.aio.inbox.receive_pending(self) -> list[AsyncRunInput]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py#L166)

