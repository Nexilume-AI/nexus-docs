---
sidebar_position: 1
title: 核心类与方法
description: NexusAgent、NexusAgentClient、NexusAgentServer 和 IPv6 运行时的方法级参考。
---

# 核心类与方法参考

本页记录 SDK 0.22.0 的主要运行时方法。签名由 Griffe 从源码静态提取；顶层导出对象总表见 [Python API 参考](api.md)。

## `NexusAgent`

高级入口，组合服务端、客户端、能力注册、续租和退出清理。

```python
NexusAgent(
    *, router: str = "auto", token: str | None = None,
    token_provider: TokenProvider | None = None,
    auth: str | TokenProvider | None = None,
    transaction_token: str | None = None,
    tenant: str = "default", agent_id: str | None = None,
    listen_host: str = "auto", port: int = 0,
    advertise_address: str = "auto", path: str = "/invoke",
    router_ca_file: str | None = None,
    router_cert_file: str | None = None,
    router_key_file: str | None = None,
    router_tls_server_name: str | None = None,
    cert_file: str | None = None, key_file: str | None = None,
    client_ca_file: str | None = None,
    server_tls_name: str = "auto", server_ca_bundle_id: str = "system",
    lease_seconds: int = 300, timeout: float = 10.0,
)
```

| 方法 | 关键参数与返回值 |
| --- | --- |
| `capability(intent, *, public_ipv6=True, origin=None, version=1, region="local", lease_seconds=None, cost_microunits=0, latency_ms=0, trust=50, pass_envelope=False)` | 普通处理器装饰器；返回原处理器 |
| `stream_capability(...)` | 流式处理器装饰器，注册同一组路由元数据 |
| `registrations()` | 返回 `tuple[CapabilityRegistration, ...]`，不启动服务 |
| `invoke(intent, payload, *, target_agent=None, intent_version=1, task_id=None, hop_limit=8, constraints=None)` | 通过路由器调用并返回 mapping |
| `invoke_stream(..., resume=True, last_event_id=0, max_reconnects=3, reconnect_delay=0.25)` | 返回 `Iterator[SseEvent]`；默认尝试恢复 |
| `start(*, auto_renew=True, renew_fraction=0.6, announce=True, print_fn=print)` | 后台启动，返回 `NexusAgentHandle` |
| `run(**start_options)` | 阻塞运行，返回发布的能力元组 |
| `public_ipv6(address, **options)` | 创建 `PublicIPv6Agent` 的类方法 |

`token`、`token_provider`、`auth` 和 `transaction_token` 不应随意混用。一次性 transaction token 不能用于自动流恢复。

## `NexusAgentClient`

```python
NexusAgentClient(
    base_url: str, *, token: str | None = None,
    token_provider: TokenProvider | None = None,
    transaction_token: str | None = None,
    ca_file: str | None = None, cert_file: str | None = None,
    key_file: str | None = None, tls_server_name: str | None = None,
    use_environment_proxy: bool = True, timeout: float = 10.0,
    user_agent: str = "nexus-agent-sdk-python/0.22.0",
)
```

| 方法 | 行为 |
| --- | --- |
| `register(registration, *, auto_renew=False, renew_fraction=0.6, health_check=None, reregister_on_not_found=True)` | 返回 `AgentLease`；可自动续租并在 404 时重新注册 |
| `renew(route_id, *, lease_seconds=None, latency_ms=None, load_permille=None, healthy=None, backend_tls=None)` | 更新租约和健康元数据，返回 `LeaseInfo` |
| `unregister(route_id)` | 撤销路由，返回 `LeaseInfo` |
| `route(envelope)` | 只执行路由决策，返回 JSON object |
| `invoke(envelope)` | 发送完整 Envelope |
| `invoke_intent(intent, payload, *, tenant, source_agent, target_agent=None, intent_version=1, task_id=None, hop_limit=8, constraints=None)` | 构造并调用 Envelope |
| `invoke_stream(envelope, *, resume=True, last_event_id=0, max_reconnects=3, reconnect_delay=0.25)` | SSE 迭代器；干净断开后最多重连 3 次 |

## `AgentLease`

| 成员 | 行为 |
| --- | --- |
| `route_id` | 当前路由 ID；重新注册后可能改变 |
| `public_ipv6` | 路由器分配的公开 IPv6，未启用时为 `None` |
| `public_endpoint` | 带 TLS 身份的公开端点，未提供时为 `None` |
| `renew(**updates)` | 手动续租；健康路由 404 时默认重新注册 |
| `start_auto_renew()` | 启动续租线程并返回自身 |
| `close(unregister=True)` | 停止续租，默认撤销路由 |

作为上下文管理器使用时，退出会调用 `close()`。

## `NexusAgentServer`

```python
NexusAgentServer(
    host: str = "127.0.0.1", port: int = 0, *, path: str = "/invoke",
    stream_path: str | None = None, auth: ServerAuthPolicy | None = None,
    cert_file: str | None = None, key_file: str | None = None,
    client_ca_file: str | None = None, address_family: str = "auto",
    dual_stack: bool = False, max_request_bytes: int = 65536,
    max_response_bytes: int = 262144, max_stream_event_bytes: int = 65536,
    request_timeout: float = 15.0, resumable_streams: bool = True,
    resume_max_tasks: int = 128, resume_max_events: int = 256,
    resume_max_history_bytes: int = 262144,
    resume_retention_seconds: float = 300.0,
)
```

| 方法 | 行为 |
| --- | --- |
| `add_handler(intent, handler, *, stream_handler=None)` | 显式注册处理器 |
| `handler(intent)` / `stream_handler(intent)` | 普通/流式装饰器 |
| `remove_handler(intent)` / `has_handler(intent)` | 修改或查询处理器表 |
| `serve_forever(poll_interval=0.25)` | 当前线程阻塞运行 |
| `serve_in_thread(daemon=True)` | 返回后台线程 |
| `is_healthy()` | 服务线程和 socket 可用时为真 |
| `shutdown()` / `server_close()` | 停止循环 / 关闭 socket |
| `registered(client, registrations, *, auto_renew=True, renew_fraction=0.6, health_check=None, reregister_on_not_found=True)` | 注册上下文，退出时关闭租约 |
| `serve_registered(...)` | 注册并阻塞服务 |

默认请求上限 64 KiB、响应上限 256 KiB、单个流事件上限 64 KiB。超过限制会在业务处理前失败。

## 直接 IPv6

### `DirectIPv6Agent`

构造函数默认 `https`，默认端口由实现选择，超时 10 秒；只接受无 zone ID 的 IPv6 地址。主要方法：

- `from_endpoint(endpoint, **credentials)`：从 `PublicAgentEndpoint` 创建。
- `plain_http(address, *, token=None, token_provider=None, transaction_token=None, port=7443, timeout=10.0)`：显式明文模式；不接受 TLS 参数。
- `invoke(..., tenant, source_agent, hop_limit=8, constraints=None)`：直接调用。
- `invoke_stream(..., resume=True, max_reconnects=3)`：直接 SSE 调用。

### `PublicIPv6Agent`

默认端口 9443，地址租约 300 秒，请求/响应上限与 `NexusAgentServer` 相同。`auth` 是必填参数；可使用 `capability()`、`stream_capability()`、`start()` 和 `run()`。

生产环境不要用 `plain_http()` 或 `NoServerAuth`。部署步骤见[直接 IPv6 Agent](../guides/direct-ipv6.md)。
