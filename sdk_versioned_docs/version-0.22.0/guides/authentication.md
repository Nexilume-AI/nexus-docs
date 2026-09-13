---
sidebar_position: 1
title: 配置认证与 TLS
---

# 配置认证与 TLS

SDK 把客户端凭据获取与服务端调用验证分开处理。生产环境应同时验证路由器身份、Agent 服务端身份和调用方权限。

## 客户端令牌

最简单的方式是设置 `NEXUS_AGENT_TOKEN`。`EnvironmentTokenProvider` 会读取该变量；`AutoTokenProvider` 可以结合路由器元数据选择可用方式。固定令牌可使用 `StaticTokenProvider`，OIDC 客户端凭据使用 `OIDCClientCredentialsProvider`。

```python
from nexus_agent import NexusAgentClient, OIDCClientCredentialsProvider

provider = OIDCClientCredentialsProvider(
    "https://issuer.example/token",
    client_id_env="NEXUS_AGENT_CLIENT_ID",
    client_secret_env="NEXUS_AGENT_CLIENT_SECRET",
)
client = NexusAgentClient("https://router.example:7443", token_provider=provider)
```

## TLS

连接路由器时传入可信 CA；使用双向 TLS 时再传客户端证书和私钥。Agent 服务端使用 `cert_file` 与 `key_file`。生产环境不要使用跳过证书验证的临时配置。

## 直接调用认证

`NoServerAuth` 仅适合隔离的开发环境。公网 IPv6 或跨管理域调用应使用 `HmacJwtServerAuth` 或集成方提供的受验证策略，并限制 issuer、audience、有效期和时钟偏差。
