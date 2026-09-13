---
sidebar_position: 2
title: Python API 参考
---

# Python API 参考

以下对象由 `nexus_agent` 顶层包公开。完整参数和返回类型以源码 docstring 与类型标注为准。

## Agent 与客户端

- `NexusAgent`：声明能力并管理服务、注册、续租与清理的高级入口。
- `NexusAgentHandle`：运行中 Agent 的生命周期句柄。
- `PublishedCapability`：高级入口发布后的能力描述。
- `NexusAgentClient`：注册、续租、发现和调用客户端。
- `AgentLease`：客户端管理的注册租约。
- `NexusAgentServer`：HTTP/SSE Agent 服务端。
- `AgentRequestError`：请求格式或业务处理错误。
- `CapabilityRegistration`：能力注册参数模型。
- `LeaseInfo`：租约响应模型。

## 请求、响应与端点模型

- `AgentEnvelope`：传给处理器的规范请求信封。
- `AgentResponse`：响应状态、头和正文模型。
- `SseEvent`：流式 SSE 事件。
- `BackendTlsIdentity`：后端 TLS 身份信息。
- `PublicAgentEndpoint`：公开 Agent 端点描述。

## 令牌与客户端认证

- `TokenProvider`：令牌提供者协议。
- `StaticTokenProvider`：返回固定令牌。
- `EnvironmentTokenProvider`：从环境变量读取令牌。
- `AutoTokenProvider`：基于环境和路由器元数据自动选择认证。
- `NoTokenProvider`：显式不提供令牌。
- `OIDCClientCredentialsProvider`：获取并缓存 OIDC 客户端凭据令牌。
- `RouterAuthMetadata`：路由器认证发现结果。
- `discover_router_auth`：读取并验证路由器认证元数据。

## 服务端认证

- `ServerAuthPolicy`：服务端认证策略协议。
- `NoServerAuth`：不验证调用方，仅限隔离开发环境。
- `HmacJwtServerAuth`：验证 HS256 JWT。
- `AuthenticatedCaller`：已验证调用方身份与声明。
- `ServerAuthenticationError`：服务端认证失败。

## IPv6 与主机地址

- `DirectIPv6Agent`：直接调用已知 IPv6 Agent。
- `PublicIPv6Agent`：公开 IPv6 Agent 的高级运行时。
- `PublicIPv6AgentHandle`：公开 IPv6 Agent 生命周期句柄。
- `HostAliasAllocator`：分配和回收主机别名地址。
- `HostAliasLease`：主机别名租约句柄。
- `HostAliasLeaseInfo`：主机别名租约信息。
- `HostAliasError`：主机别名操作错误。
- `LinuxAddressBackend`：Linux 地址配置后端。
- `WindowsAddressBackend`：Windows 地址配置后端。
- `MemoryAddressBackend`：测试用内存后端。
- `LocalAddressdClient`：本地 addressd 客户端。
- `UnixAddressdTransport`：Unix socket 传输。
- `WindowsNamedPipeTransport`：Windows named pipe 传输。
- `default_addressd_transport`：返回当前平台的默认 addressd 传输。

## 安全描述文件

- `NexusSecurityProfile`：加载并验证安全描述文件。
- `ResolvedIPv6Security`：解析后的 IPv6 安全配置。
- `install_descriptor`：安装安全描述文件及关联材料。

## 异常

- `NexusAgentError`：SDK 异常基类。
- `NexusSecurityConfigurationError`：安全配置无效。
- `NexusAuthDiscoveryError`：认证元数据发现失败。
- `NexusTokenAcquisitionError`：令牌获取失败。
- `NexusHttpError`：HTTP 非成功响应。
- `NexusAuthenticationError`：未通过身份认证。
- `NexusAuthorizationError`：身份已知但权限不足。

FastMCP 对象位于 `nexus_agent.fastmcp`，A2A 对象位于 `nexus_agent.a2a`，参见对应[集成指南](../integrations/fastmcp.md)。
