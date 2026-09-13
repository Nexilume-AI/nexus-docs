---
sidebar_position: 3
title: 直接 IPv6 Agent
description: 使用固定地址或 Host Alias 发布 Agent，并按数值 IPv6 直接调用。
---

# 直接 IPv6 Agent

直接模式由两个类组成：`NexusAgent.public_ipv6(...)` 在 Agent 自己持有的全球 IPv6 上发布能力；`DirectIPv6Agent` 按已知数值 IPv6 调用目标。它们不要求 OpenWrt 注册、AFIB 选路、Directory 或 Relay。

## 一 Agent 一 IP：Host Alias

主机拥有真实可用 `/64` 且已配置 `nexus-agent-addressd` 时，让 SDK 为 Agent 租用 `/128`：

```python
from nexus_agent import NexusAgent

agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="echo-1",
    port=9443,
)

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

agent.run()
```

`start()` 成功后可从 `agent.address` 读取压缩后的 IPv6，从 `agent.endpoint` 读取 scheme、address、port 和 URL。关闭 `PublicIPv6AgentHandle` 会停止服务并释放地址租约。

## 使用主机已有地址

如果全球 IPv6 已属于主机，显式传入并保留 `auth` 参数：

```python
agent = NexusAgent.public_ipv6(
    "240e:1234:5678:1200::20",
    address_mode="existing",
    auth="none",
    tenant="demo",
    agent_id="echo-1",
    port=9443,
)
```

SDK 只绑定已有地址，不添加地址、不修改防火墙，也不执行自动发现。地址不能带 `%scope`，必须被 Python `ipaddress` 判定为全球 IPv6，并确实属于本机。

## 隔离实验网中的明文调用

```python
from nexus_agent import DirectIPv6Agent

target = DirectIPv6Agent.plain_http(
    "240e:1234:5678:1200::20",
    port=9443,
)
result = target.invoke(
    "demo.echo",
    {"message": "hello"},
    tenant="demo",
    source_agent="agent://demo/caller-a",
)
```

`plain_http()` 是显式选择；HTTPS 失败时 SDK 不会自动降级。明文模式会暴露 token、Envelope 和业务数据，只用于隔离实验。

## HTTPS 与 JWT 调用

服务端使用证书，并把稳定 DNS 名作为 TLS 身份：

```python
import os
from nexus_agent import HmacJwtServerAuth, NexusAgent

auth = HmacJwtServerAuth(
    os.environ["NEXUS_AGENT_JWT_SECRET"],
    issuer="https://issuer.private.example",
    audience="echo-agent",
)
agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth=auth,
    tenant="demo",
    agent_id="echo-1",
    port=9443,
    cert_file="agent-fullchain.pem",
    key_file="agent-key.pem",
    tls_server_name="echo-1.private.example",
    ca_bundle_id="private-agent-ca",
)
```

调用端仍以数值 IPv6 建立 TCP 连接，但使用稳定 DNS 身份做 SNI 和证书名称验证：

```python
target = DirectIPv6Agent(
    "240e:1234:5678:1200::20",
    port=9443,
    server_identity="echo-1.private.example",
    token=short_lived_jwt,
    ca_file="private-agent-ca.pem",
)
result = target.invoke(
    "demo.echo",
    {"message": "secure hello"},
    tenant="demo",
    source_agent="agent://demo/caller-a",
)
```

`HmacJwtServerAuth` 只验证 HS256 共享密钥 token，并校验 issuer、audience、有效期、`agent.invoke` scope、tenant 和 `source_agent`。它不等价于 OIDC/JWKS 验证。跨组织部署应使用合适的服务端策略和密钥管理。

## 发现与直连的边界

`DirectIPv6Agent` 不发现目标。调用方必须从配置、Agent Card、DNS SVCB 或可信 Directory 获得地址、端口、TLS 身份和 CA 标签。发现解决“到哪里”，TLS/JWT 解决“是否可信和是否允许”，不要把两者合并。

客户端禁用环境 HTTP proxy，避免字面 IPv6 请求静默绕行代理。目标不可达时调用直接失败，不会自动改走 Router 或 Relay。

## 关键参数

### `NexusAgent.public_ipv6(address, ...)`

| 参数 | 约束 / 默认值 | 作用 |
| --- | --- | --- |
| `address` | 全球 IPv6 或 `"auto"` | 固定绑定或申请 Host Alias |
| `auth` | 必填；`"none"` 或 `ServerAuthPolicy` | 服务端调用认证 |
| `port` | `9443`，范围 1–65535 | 监听端口 |
| `address_mode` | `"auto"`、`"existing"`、`"host-alias"` | 地址来源；Host Alias 要求 `address="auto"` |
| `interface` / `prefix` | `"auto"` | 限定 addressd 租约请求 |
| `address_lease_seconds` | `300` | Host Alias 租期 |
| `cert_file` / `key_file` | 成对使用 | 启用 HTTPS |
| `tls_server_name` / `ca_bundle_id` | HTTPS 时必填 | 发布稳定证书身份和 CA 标签 |

### `DirectIPv6Agent(address, ...)`

| 参数 | 约束 / 默认值 | 作用 |
| --- | --- | --- |
| `address` | 数值 IPv6，不允许 scope ID | TCP 目标 |
| `scheme` | `"https"` | `https` 或显式 `http` |
| `server_identity` | HTTPS 必需，除非安全配置文件可解析 | SNI 和证书名称验证 |
| `port` | HTTPS 默认为 `7443` | 目标端口；Host Alias 示例通常显式用 `9443` |
| `token` / `token_provider` | 互斥 | 调用凭据 |
| `ca_file`、`cert_file`、`key_file` | 可选 | CA 信任与调用端 mTLS |
| `timeout` | `10.0` 秒 | 请求超时 |

先运行[两个 IPv6 Agent 互相调用](../tutorials/ipv6-agents-call-each-other.md)，再阅读[认证指南](authentication.md)。OpenWrt 托管地址的差异见[地址归属模型](/openwrt/communication/addressing)。
