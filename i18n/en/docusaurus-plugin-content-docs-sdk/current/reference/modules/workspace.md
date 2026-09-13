---
title: "workspace API"
---

# workspace API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `SSHWorkspaceConnection`

Bases: `_Record`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `id` | `str` | `required` |
| `name` | `str` | `required` |
| `ssh_host` | `str` | `required` |
| `ssh_port` | `int` | `required` |
| `ssh_user` | `str` | `required` |
| `auth_mode` | `str` | `required` |
| `workspace_root` | `str` | `required` |
| `status` | `str` | `required` |
| `last_test_status` | `str` | `''` |
| `last_test_error` | `str` | `''` |
| `last_test_at` | `Optional[str]` | `None` |
| `metadata` | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `connection_type` | `str` | `'ssh'` |
| `created_at` | `str` | `''` |
| `updated_at` | `str` | `''` |

### `SSHWorkspaceConnection.from_dict`

```text
SSHWorkspaceConnection.from_dict(cls, value: Mapping[str, Any]) -> 'SSHWorkspaceConnection'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py#L43)


## `SSHWorkspaceConnectionCreate`

| Field | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `ssh_host` | `str` | `required` |
| `ssh_user` | `str` | `required` |
| `auth_mode` | `str` | `'private_key'` |
| `ssh_port` | `int` | `22` |
| `workspace_root` | `str` | `'~/.nexus'` |
| `private_key` | `str` | `field(default='', repr=False)` |
| `password` | `str` | `field(default='', repr=False)` |
| `metadata` | `Mapping[str, Any]` | `field(default_factory=dict)` |


## `SSHWorkspaceConnectionUpdate`

| Field | Type | Default |
| --- | --- | --- |
| `name` | `Optional[str]` | `None` |
| `ssh_host` | `Optional[str]` | `None` |
| `ssh_port` | `Optional[int]` | `None` |
| `ssh_user` | `Optional[str]` | `None` |
| `auth_mode` | `Optional[str]` | `None` |
| `workspace_root` | `Optional[str]` | `None` |
| `private_key` | `Optional[str]` | `field(default=None, repr=False)` |
| `password` | `Optional[str]` | `field(default=None, repr=False)` |
| `metadata` | `Optional[Mapping[str, Any]]` | `None` |


## `SSHTestResult`

Bases: `_Record`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `status` | `str` | `required` |
| `facts` | `Mapping[str, Any]` | `field(default_factory=dict)` |
| `checks` | `tuple[Mapping[str, Any], ...]` | `()` |
| `error` | `str` | `''` |

### `SSHTestResult.from_dict`

```text
SSHTestResult.from_dict(cls, value: Mapping[str, Any]) -> 'SSHTestResult'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py#L111)


## `WorkspaceEntry`

Bases: `_Record`. Inherited behavior is defined on the base class.

| Field | Type | Default |
| --- | --- | --- |
| `name` | `str` | `required` |
| `path` | `str` | `required` |
| `kind` | `str` | `required` |
| `size` | `int` | `0` |
| `modified_at` | `Optional[str]` | `None` |

### `WorkspaceEntry.from_dict`

```text
WorkspaceEntry.from_dict(cls, value: Mapping[str, Any]) -> 'WorkspaceEntry'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py#L129)


## `CommandResult`

Bases: `dict`. Inherited behavior is defined on the base class.

Typed command result that remains ``dict`` compatible with SDK 0.24.

### `CommandResult.from_dict`

```text
CommandResult.from_dict(cls, value: Mapping[str, Any]) -> 'CommandResult'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py#L143)

