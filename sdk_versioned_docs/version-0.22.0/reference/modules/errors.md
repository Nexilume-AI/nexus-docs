---
title: "errors API"
---

# errors API

本页从当前源码生成参数、返回类型、字段、直接抛出的异常和原始 docstring。运行条件、语义与组合示例见 [Agent 设计](../../design/overview.md)。未标注返回类型的接口不猜测类型；下层传输还可能抛出其他异常。构造函数中的下划线参数是内部测试/适配钩子，应用不要依赖。

## `NexusAgentError`

Bases: `Exception`. Inherited behavior is defined on the base class.

Base SDK error.


## `NexusSecurityConfigurationError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

The local SDK security profile is missing or invalid.


## `NexusAuthDiscoveryError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

Router or OIDC authentication metadata is unavailable or invalid.


## `NexusTokenAcquisitionError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

A short-lived access token could not be acquired safely.


## `NexusHttpError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

Agent Access Proxy returned a non-success HTTP response.

### `NexusHttpError.__init__`

```text
NexusHttpError.__init__(self, status: int, code: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `status` | `int` | `required` |
| `code` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py#L20)


## `NexusAuthenticationError`

Bases: `NexusHttpError`. Inherited behavior is defined on the base class.

The router rejected or could not validate caller authentication.


## `NexusAuthorizationError`

Bases: `NexusHttpError`. Inherited behavior is defined on the base class.

The authenticated caller lacks permission for this operation.


## `NexusCloudRegistrationError`

Bases: `NexusAgentError`. Inherited behavior is defined on the base class.

The router could not publish this LAN Agent to Nexus Cloud.

### `NexusCloudRegistrationError.__init__`

```text
NexusCloudRegistrationError.__init__(self, state: str, message: str) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `state` | `str` | `required` |
| `message` | `str` | `required` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py#L38)

