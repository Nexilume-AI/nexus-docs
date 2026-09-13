---
title: "windows_pipe API"
---

# windows_pipe API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

### `validate_pipe_name`

```text
validate_pipe_name(value: str) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `str` | `required` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L43)


### `protect_admin_file`

```text
protect_admin_file(path: str) -> None
```

Restrict an addressd secret/state file to SYSTEM and Administrators.

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L112)


### `protect_admin_tree`

```text
protect_admin_tree(path: str) -> None
```

Restrict a directory tree root to SYSTEM and Administrators.

New children inherit the protected DACL.  The installer calls this before
creating the isolated Windows Service runtime so LocalSystem never imports
executable Python code from a user-writable directory.

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L149)


## `WindowsNamedPipeTransport`

One-request-per-connection addressd transport for Windows Agents.

### `WindowsNamedPipeTransport.__init__`

```text
WindowsNamedPipeTransport.__init__(self, pipe_name: Optional[str]=None, *, timeout: float=5.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `pipe_name` | `Optional[str]` | `None` |
| `timeout` | `float` | `5.0` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L235)

### `WindowsNamedPipeTransport.call`

```text
WindowsNamedPipeTransport.call(self, method: str, parameters: Mapping[str, Any]) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `method` | `str` | `required` |
| `parameters` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L249)


## `AddressdNamedPipeServer`

Threaded Windows Named Pipe server with SID-bound lease ownership.

### `AddressdNamedPipeServer.__init__`

```text
AddressdNamedPipeServer.__init__(self, pipe_name: str, application: Any, *, allowed_group: Optional[str]=DEFAULT_PIPE_GROUP, sweep_interval: float=5.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `pipe_name` | `str` | `required` |
| `application` | `Any` | `required` |
| `allowed_group` | `Optional[str]` | `DEFAULT_PIPE_GROUP` |
| `sweep_interval` | `float` | `5.0` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L319)

### `AddressdNamedPipeServer.serve_forever`

```text
AddressdNamedPipeServer.serve_forever(self, poll_interval: float=0.5) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `poll_interval` | `float` | `0.5` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L367)

### `AddressdNamedPipeServer.shutdown`

```text
AddressdNamedPipeServer.shutdown(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L459)

### `AddressdNamedPipeServer.server_close`

```text
AddressdNamedPipeServer.server_close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py#L489)

