---
title: "files API"
---

# files API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `NexusFileError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.

### `NexusFileError.__init__`

```text
NexusFileError.__init__(self, message, *, file_id=None) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `message` | `not annotated` | `required` |
| `file_id` | `not annotated` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L15)


## `ctx.files`

### `ctx.files.__init__`

```text
ctx.files.__init__(self, context) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `context` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L21)

### `ctx.files.list`

```text
ctx.files.list(self) -> not annotated; see contract/source
```

List the current Run&#x27;s input references (no file bytes).

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L50)

### `ctx.files.iter_bytes`

```text
ctx.files.iter_bytes(self, reference, *, offset=0, chunk_size=256 * 1024) -> not annotated; see contract/source
```

Read a private input/output with bounded chunks. Caller owns iteration.

| Parameter | Type | Default |
| --- | --- | --- |
| `reference` | `not annotated` | `required` |
| `offset` | `not annotated` | `0` |
| `chunk_size` | `not annotated` | `256 * 1024` |

Direct raises (not exhaustive): `NexusFileError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L54)

### `ctx.files.download`

```text
ctx.files.download(self, reference, destination, *, resume=True, overwrite=False, progress=None) -> not annotated; see contract/source
```

Download to a file, verify SHA-256, then atomically publish the result.

| Parameter | Type | Default |
| --- | --- | --- |
| `reference` | `not annotated` | `required` |
| `destination` | `not annotated` | `required` |
| `resume` | `not annotated` | `True` |
| `overwrite` | `not annotated` | `False` |
| `progress` | `not annotated` | `None` |

Direct raises (not exhaustive): `FileExistsError`, `NexusFileError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L75)

### `ctx.files.upload`

```text
ctx.files.upload(self, path, *, content_type='application/octet-stream', resume_id=None, progress=None, timeout=1800) -> not annotated; see contract/source
```

Upload an output in idempotent chunks; return its immutable reference.

Supply resume_id after a process restart to continue a prior upload in
the same active Run. The source file must not change during upload.

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `not annotated` | `required` |
| `content_type` | `not annotated` | `'application/octet-stream'` |
| `resume_id` | `not annotated` | `None` |
| `progress` | `not annotated` | `None` |
| `timeout` | `not annotated` | `1800` |

Direct raises (not exhaustive): `NexusFileError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L113)


## `ctx.aio.files`

### `ctx.aio.files.__init__`

```text
ctx.aio.files.__init__(self, files) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `files` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L170)

### `ctx.aio.files.list`

```text
async ctx.aio.files.list(self) -> not annotated; see contract/source
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L173)

### `ctx.aio.files.download`

```text
async ctx.aio.files.download(self, reference, destination, **kwargs) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `reference` | `not annotated` | `required` |
| `destination` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L176)

### `ctx.aio.files.upload`

```text
async ctx.aio.files.upload(self, path, **kwargs) -> not annotated; see contract/source
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `not annotated` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py#L179)

