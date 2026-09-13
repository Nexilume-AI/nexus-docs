---
title: "computer_runtime API"
---

# computer_runtime API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `NexusComputerRuntimeError`

Bases: `RuntimeError`. Inherited behavior is defined on the base class.


## `RuntimeOperationError`

Bases: `NexusComputerRuntimeError`. Inherited behavior is defined on the base class.

### `RuntimeOperationError.__init__`

```text
RuntimeOperationError.__init__(self, code: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `code` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L62)


## `NexusComputerRuntime`

Cross-platform Runtime that executes bounded commands from an outbound WSS.

### `NexusComputerRuntime.__init__`

```text
NexusComputerRuntime.__init__(self, root: Union[Path, str]=DEFAULT_ROOT) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `root` | `Union[Path, str]` | `DEFAULT_ROOT` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L478)

### `NexusComputerRuntime.registration_runtimes`

```text
NexusComputerRuntime.registration_runtimes(self) -> list[tuple[dict[str, str], 'NexusComputerRuntime']]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L570)

### `NexusComputerRuntime.registration_statuses`

```text
NexusComputerRuntime.registration_statuses(self) -> list[dict[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L576)

### `NexusComputerRuntime.registration_runtime`

```text
NexusComputerRuntime.registration_runtime(self, registration_id: str='') -> tuple[dict[str, str], 'NexusComputerRuntime']
```

| Parameter | Type | Default |
| --- | --- | --- |
| `registration_id` | `str` | `''` |

Direct raises (not exhaustive): `NexusComputerRuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L602)

### `NexusComputerRuntime.remove_registration`

```text
NexusComputerRuntime.remove_registration(self, registration_id: str='', *, local_only: bool=False) -> str
```

| Parameter | Type | Default |
| --- | --- | --- |
| `registration_id` | `str` | `''` |
| `local_only` | `bool` | `False` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L618)

### `NexusComputerRuntime.setup`

```text
NexusComputerRuntime.setup(cls, pairing_url: str, *, root: Union[Path, str]=DEFAULT_ROOT, name: str='', ca_file: str='', install: bool=True) -> 'NexusComputerRuntime'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `pairing_url` | `str` | `required` |
| `root` | `Union[Path, str]` | `DEFAULT_ROOT` |
| `name` | `str` | `''` |
| `ca_file` | `str` | `''` |
| `install` | `bool` | `True` |

Direct raises (not exhaustive): `NexusComputerRuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L652)

### `NexusComputerRuntime.detect_capabilities`

```text
NexusComputerRuntime.detect_capabilities(self) -> tuple[dict[str, int], dict[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L847)

### `NexusComputerRuntime.dispatch`

```text
NexusComputerRuntime.dispatch(self, operation: str, required_scope: str, payload: Mapping[str, Any], cancel_event: Optional[threading.Event]=None) -> dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `operation` | `str` | `required` |
| `required_scope` | `str` | `required` |
| `payload` | `Mapping[str, Any]` | `required` |
| `cancel_event` | `Optional[threading.Event]` | `None` |

Direct raises (not exhaustive): `RuntimeOperationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L931)

### `NexusComputerRuntime.run_forever`

```text
async NexusComputerRuntime.run_forever(self) -> None
```

Direct raises (not exhaustive): `NexusComputerRuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1247)

### `NexusComputerRuntime.unpair_cloud`

```text
NexusComputerRuntime.unpair_cloud(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1409)

### `NexusComputerRuntime.close`

```text
NexusComputerRuntime.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1696)

### `NexusComputerRuntime.install_user_service`

```text
NexusComputerRuntime.install_user_service(self) -> str
```

Direct raises (not exhaustive): `NexusComputerRuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1791)

### `NexusComputerRuntime.repair_user_service`

```text
NexusComputerRuntime.repair_user_service(self, *, pairing_succeeded: bool=False) -> dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `pairing_succeeded` | `bool` | `False` |

Direct raises (not exhaustive): `NexusComputerRuntimeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1845)

### `NexusComputerRuntime.service_status`

```text
NexusComputerRuntime.service_status(self) -> dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1875)

### `NexusComputerRuntime.restart_user_service`

```text
NexusComputerRuntime.restart_user_service(self) -> None
```

Direct raises (not exhaustive): `NexusComputerRuntimeError`, `OSError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L1931)

### `NexusComputerRuntime.uninstall_user_service`

```text
NexusComputerRuntime.uninstall_user_service(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L2036)


### `main`

```text
main(argv: Optional[Sequence[str]]=None) -> int
```

| Parameter | Type | Default |
| --- | --- | --- |
| `argv` | `Optional[Sequence[str]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py#L2174)

