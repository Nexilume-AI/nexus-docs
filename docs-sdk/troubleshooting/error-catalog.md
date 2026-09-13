---
sidebar_position: 0
title: 错误码与恢复动作
---

# 错误码与恢复动作

先捕获最具体的异常。SDK 会把 HTTP 401 映射为 `NexusAuthenticationError`，403 映射为 `NexusAuthorizationError`，其他结构化非成功响应使用 `NexusHttpError`。

```python
from nexus_agent import (
    NexusAuthenticationError,
    NexusAuthorizationError,
    NexusHttpError,
)

try:
    result = client.invoke_intent(...)
except NexusAuthenticationError:
    # 刷新或重新获取凭据，不要无限重试同一令牌
    raise
except NexusAuthorizationError:
    # 检查 tenant、scope、能力和策略
    raise
except NexusHttpError as error:
    print(error.status, error.code, error.message)
```

## 常见结构化错误

| HTTP / code | 含义 | 用户动作 |
| --- | --- | --- |
| 401 / `AUTHENTICATION_REQUIRED` | 缺少、过期或无效凭据 | 检查令牌来源、issuer、audience 和设备时间 |
| 403 / `INSUFFICIENT_SCOPE` | 身份有效但 scope 不足 | 为该身份授予精确 route/invoke 权限 |
| 404 / route not found | 租约或能力路由不存在 | 检查 Local Agents、Capability Routes 和 Policy RIB |
| 422 / `INPUT_REJECTED` | Agent 业务处理器拒绝输入 | 根据 message 修正 payload，不要重试相同输入 |

code 的具体字符串由网关或 Agent 返回。记录 `status`、`code`、`message`、task ID 和发生时间，不要记录令牌。

## 来自真实测试的恢复行为

- 可刷新的 token provider 遇到 401 时只刷新一次，然后重试一次请求。
- 健康租约续租遇到 404 时，默认重新注册并切换到新的 `route_id`。
- `healthy=False` 的租约不会在 404 后重新注册。
- 健康检查失败时，自动续租会撤销路由并停止。
- SSE 干净断开后，客户端携带 `Last-Event-ID` 恢复，同一任务不会重新执行。
- transaction token 是一次性凭据，不能用于流恢复。

## 参数校验错误

以下问题在发出网络请求前抛出 `ValueError`：

- `target_agent=""`。
- 同时提供 access token 和 transaction token。
- HTTP URL 配置 `tls_server_name`。
- `DirectIPv6Agent` 传入 IPv4、主机名或带 zone ID 的链路本地地址。
- 明文直接 IPv6 模式同时传入 CA、证书或其他 TLS 参数。

## 下一步

运行 [SDK 诊断](diagnostics.md)，然后根据异常类别查看[认证](../guides/authentication.md)、[流式调用](../guides/streaming.md)或[直接 IPv6](../guides/direct-ipv6.md)。
