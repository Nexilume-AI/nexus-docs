---
title: "host_alias API"
---

# host_alias API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `HostAliasError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

A bounded local IPv6 allocation error.


## `HostAliasLeaseInfo`

| Field | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |
| `address` | `str` | `required` |
| `prefix` | `str` | `required` |
| `interface` | `str` | `required` |
| `tenant` | `str` | `required` |
| `agent_id` | `str` | `required` |
| `state` | `str` | `required` |
| `lease_seconds` | `int` | `required` |
| `expires_at` | `float` | `required` |

### `HostAliasLeaseInfo.from_dict`

```text
HostAliasLeaseInfo.from_dict(cls, value: Mapping[str, Any]) -> 'HostAliasLeaseInfo'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L41)

### `HostAliasLeaseInfo.to_dict`

```text
HostAliasLeaseInfo.to_dict(self) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L67)


## `AddressBackend`

Bases: `Protocol`. Inherited behavior is defined on the base class.

### `AddressBackend.prefix_ready`

```text
AddressBackend.prefix_ready(self, interface: str, prefix: ipaddress.IPv6Network) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `prefix` | `ipaddress.IPv6Network` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L72)

### `AddressBackend.add_address`

```text
AddressBackend.add_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L75)

### `AddressBackend.remove_address`

```text
AddressBackend.remove_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L78)

### `AddressBackend.has_address`

```text
AddressBackend.has_address(self, interface: str, address: ipaddress.IPv6Address) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L81)


## `MemoryAddressBackend`

Deterministic non-privileged backend for tests and dry runs.

### `MemoryAddressBackend.__init__`

```text
MemoryAddressBackend.__init__(self, prefixes: Iterable[Tuple[str, str]]) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `prefixes` | `Iterable[Tuple[str, str]]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L88)

### `MemoryAddressBackend.prefix_ready`

```text
MemoryAddressBackend.prefix_ready(self, interface: str, prefix: ipaddress.IPv6Network) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `prefix` | `ipaddress.IPv6Network` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L96)

### `MemoryAddressBackend.add_address`

```text
MemoryAddressBackend.add_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L99)

### `MemoryAddressBackend.remove_address`

```text
MemoryAddressBackend.remove_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L106)

### `MemoryAddressBackend.has_address`

```text
MemoryAddressBackend.has_address(self, interface: str, address: ipaddress.IPv6Address) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L110)


## `LinuxAddressBackend`

Bases: `_CommandAddressBackend`. Inherited behavior is defined on the base class.

Bounded Linux backend using argument-vector iproute2 operations.

### `LinuxAddressBackend.prefix_ready`

```text
LinuxAddressBackend.prefix_ready(self, interface: str, prefix: ipaddress.IPv6Network) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `prefix` | `ipaddress.IPv6Network` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L160)

### `LinuxAddressBackend.add_address`

```text
LinuxAddressBackend.add_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L173)

### `LinuxAddressBackend.remove_address`

```text
LinuxAddressBackend.remove_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L192)

### `LinuxAddressBackend.has_address`

```text
LinuxAddressBackend.has_address(self, interface: str, address: ipaddress.IPv6Address) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L197)


## `WindowsAddressBackend`

Bases: `_CommandAddressBackend`. Inherited behavior is defined on the base class.

Windows backend using fixed netsh verbs without a command shell.

### `WindowsAddressBackend.interface_index`

```text
WindowsAddressBackend.interface_index(self, interface: str) -> int
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L209)

### `WindowsAddressBackend.prefix_ready`

```text
WindowsAddressBackend.prefix_ready(self, interface: str, prefix: ipaddress.IPv6Network) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `prefix` | `ipaddress.IPv6Network` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L226)

### `WindowsAddressBackend.add_address`

```text
WindowsAddressBackend.add_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L243)

### `WindowsAddressBackend.remove_address`

```text
WindowsAddressBackend.remove_address(self, interface: str, address: ipaddress.IPv6Address) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L274)

### `WindowsAddressBackend.has_address`

```text
WindowsAddressBackend.has_address(self, interface: str, address: ipaddress.IPv6Address) -> bool
```

| Parameter | Type | Default |
| --- | --- | --- |
| `interface` | `str` | `required` |
| `address` | `ipaddress.IPv6Address` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L282)


### `system_address_backend`

```text
system_address_backend() -> AddressBackend
```

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L291)


## `HostAliasAllocator`

Thread-safe `/128` lease allocator used inside addressd.

### `HostAliasAllocator.__init__`

```text
HostAliasAllocator.__init__(self, *, backend: AddressBackend, interface: str, prefix: Optional[str], allocation_secret: bytes, max_addresses: int=256, default_lease_seconds: int=300, reservation_seconds: int=15, now: Any=time.time) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `backend` | `AddressBackend` | `required` |
| `interface` | `str` | `required` |
| `prefix` | `Optional[str]` | `required` |
| `allocation_secret` | `bytes` | `required` |
| `max_addresses` | `int` | `256` |
| `default_lease_seconds` | `int` | `300` |
| `reservation_seconds` | `int` | `15` |
| `now` | `Any` | `time.time` |

Direct raises (not exhaustive): `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L308)

### `HostAliasAllocator.sweep`

```text
HostAliasAllocator.sweep(self) -> int
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L392)

### `HostAliasAllocator.allocate`

```text
HostAliasAllocator.allocate(self, *, owner: str, tenant: str, agent_id: str, interface: Optional[str]=None, prefix: Optional[str]=None, lease_seconds: Optional[int]=None) -> HostAliasLeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `owner` | `str` | `required` |
| `tenant` | `str` | `required` |
| `agent_id` | `str` | `required` |
| `interface` | `Optional[str]` | `None` |
| `prefix` | `Optional[str]` | `None` |
| `lease_seconds` | `Optional[int]` | `None` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L411)

### `HostAliasAllocator.confirm`

```text
HostAliasAllocator.confirm(self, lease_id: str, *, owner: str) -> HostAliasLeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |
| `owner` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L516)

### `HostAliasAllocator.renew`

```text
HostAliasAllocator.renew(self, lease_id: str, *, owner: str) -> HostAliasLeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |
| `owner` | `str` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L530)

### `HostAliasAllocator.release`

```text
HostAliasAllocator.release(self, lease_id: str, *, owner: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |
| `owner` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L553)

### `HostAliasAllocator.list`

```text
HostAliasAllocator.list(self, *, owner: Optional[str]=None) -> Tuple[HostAliasLeaseInfo, ...]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `owner` | `Optional[str]` | `None` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L558)

### `HostAliasAllocator.snapshot`

```text
HostAliasAllocator.snapshot(self) -> List[Dict[str, Any]]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L568)

### `HostAliasAllocator.restore`

```text
HostAliasAllocator.restore(self, values: Iterable[Mapping[str, Any]]) -> int
```

| Parameter | Type | Default |
| --- | --- | --- |
| `values` | `Iterable[Mapping[str, Any]]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L583)


## `AddressdTransport`

Bases: `Protocol`. Inherited behavior is defined on the base class.

### `AddressdTransport.call`

```text
AddressdTransport.call(self, method: str, parameters: Mapping[str, Any]) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `method` | `str` | `required` |
| `parameters` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L654)


## `UnixAddressdTransport`

### `UnixAddressdTransport.__init__`

```text
UnixAddressdTransport.__init__(self, socket_path: Optional[str]=None, *, timeout: float=5.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `socket_path` | `Optional[str]` | `None` |
| `timeout` | `float` | `5.0` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L659)

### `UnixAddressdTransport.call`

```text
UnixAddressdTransport.call(self, method: str, parameters: Mapping[str, Any]) -> Mapping[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `method` | `str` | `required` |
| `parameters` | `Mapping[str, Any]` | `required` |

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L669)


### `default_addressd_transport`

```text
default_addressd_transport() -> AddressdTransport
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L708)


## `LocalAddressdClient`

### `LocalAddressdClient.__init__`

```text
LocalAddressdClient.__init__(self, transport: Optional[AddressdTransport]=None, *, owner: Optional[str]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `transport` | `Optional[AddressdTransport]` | `None` |
| `owner` | `Optional[str]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L717)

### `LocalAddressdClient.allocate`

```text
LocalAddressdClient.allocate(self, *, tenant: str, agent_id: str, interface: str='auto', prefix: str='auto', lease_seconds: int=300) -> 'HostAliasLease'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `tenant` | `str` | `required` |
| `agent_id` | `str` | `required` |
| `interface` | `str` | `'auto'` |
| `prefix` | `str` | `'auto'` |
| `lease_seconds` | `int` | `300` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L726)

### `LocalAddressdClient.confirm`

```text
LocalAddressdClient.confirm(self, lease_id: str) -> HostAliasLeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L745)

### `LocalAddressdClient.renew`

```text
LocalAddressdClient.renew(self, lease_id: str) -> HostAliasLeaseInfo
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L751)

### `LocalAddressdClient.release`

```text
LocalAddressdClient.release(self, lease_id: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `lease_id` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L757)


## `HostAliasLease`

### `HostAliasLease.__init__`

```text
HostAliasLease.__init__(self, client: LocalAddressdClient, info: HostAliasLeaseInfo) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `client` | `LocalAddressdClient` | `required` |
| `info` | `HostAliasLeaseInfo` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L764)

### `HostAliasLease.address`

```text
HostAliasLease.address: str
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L774)

### `HostAliasLease.confirm`

```text
HostAliasLease.confirm(self) -> HostAliasLeaseInfo
```

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L777)

### `HostAliasLease.renew`

```text
HostAliasLease.renew(self) -> HostAliasLeaseInfo
```

Direct raises (not exhaustive): `HostAliasError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L784)

### `HostAliasLease.start_auto_renew`

```text
HostAliasLease.start_auto_renew(self, *, fraction: float=0.6) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `fraction` | `float` | `0.6` |

Direct raises (not exhaustive): `HostAliasError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L791)

### `HostAliasLease.close`

```text
HostAliasLease.close(self) -> None
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py#L814)

