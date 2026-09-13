---
sidebar_position: 2
title: Python API 参考
---

# Python API 参考

以下对象由 `nexus_agent` 顶层包公开。完整参数和返回类型以源码 docstring 与类型标注为准。

完整参数、返回、字段与异常见[方法级接口参考](coverage.md)；如何组合这些 API 见[Agent 设计教程](../design/overview.md)。

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

## Current source export index

- `AgentEnvelope` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `AgentLease` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `AgentRequestError` — [`nexus_agent.server`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py)
- `AgentResponse` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `AuthenticatedCaller` — [`nexus_agent.server_auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py)
- `AutoTokenProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `BackendTlsIdentity` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `CapabilityRegistration` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `CloudRegistrationManifest` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `CloudRegistrationStatus` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `CommandResult` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `ComputerRegistrationContract` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `DeliveryReport` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `DirectIPv6Agent` — [`nexus_agent.direct_ipv6`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py)
- `EnvironmentTokenProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `HmacJwtServerAuth` — [`nexus_agent.server_auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py)
- `HostAliasAllocator` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `HostAliasError` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `HostAliasLease` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `HostAliasLeaseInfo` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `LeaseInfo` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `LinuxAddressBackend` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `LocalAddressdClient` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `MOBILE_SCOPES` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `McpToolDescriptor` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `MemoryAddressBackend` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `MemoryDeleteResult` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `MobileRegistrationContract` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `NexusAgent` — [`nexus_agent.agent`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py)
- `NexusAgentClient` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `NexusAgentError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusAgentHandle` — [`nexus_agent.agent`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py)
- `NexusAgentServer` — [`nexus_agent.server`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py)
- `NexusAsyncBrowserSession` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusAttachedBrowserSession` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusAuthDiscoveryError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusAuthenticationError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusAuthorizationError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusBillingLineItem` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusBillingReportError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusBillingUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusBrowserAction` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserActionFailed` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserComputerRequired` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserDOMSnapshot` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserError` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserNode` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserObservation` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserPermissionRequired` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserSession` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserSessionLost` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserStaleObservation` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserTunnelUnavailable` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusBrowserUnavailable` — [`nexus_agent.browser`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/browser.py)
- `NexusChatError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusChatReply` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusChatTimeout` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusChatUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusCheckpoint` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusCheckpointError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusCloudRegistrationError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusComputerError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusComputerRuntime` — [`nexus_agent.computer_runtime`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py)
- `NexusComputerRuntimeError` — [`nexus_agent.computer_runtime`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py)
- `NexusDirectTask` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `NexusDirectTaskError` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `NexusExecutionProfile` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `NexusExecutionSelection` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusExternalOperation` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusFileError` — [`nexus_agent.files`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/files.py)
- `NexusFollowUpUnavailable` — [`nexus_agent.inbox`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py)
- `NexusHttpError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusImageReference` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusInteractionRequest` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `NexusInvokeEvent` — [`nexus_agent.client`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)
- `NexusMemoryConflict` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMemoryError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMemoryItem` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMemoryUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileActionFailed` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileBusy` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileCommandResult` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileObservation` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobilePermissionRequired` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileScreen` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileStatus` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileTimeout` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusMobileUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRecoveryDiverged` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRecoveryError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusReportingConfig` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRunCancelled` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRunContext` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRunContextExchangeError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusRunContextUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusSecurityConfigurationError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusSecurityProfile` — [`nexus_agent.security_profile`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py)
- `NexusTokenAcquisitionError` — [`nexus_agent.errors`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/errors.py)
- `NexusUsageError` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NexusUsageUnavailable` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `NoServerAuth` — [`nexus_agent.server_auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py)
- `NoTokenProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `OIDCClientCredentialsProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `PublicAgentEndpoint` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `PublicIPv6Agent` — [`nexus_agent.public_ipv6_agent`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py)
- `PublicIPv6AgentHandle` — [`nexus_agent.public_ipv6_agent`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py)
- `PublishedCapability` — [`nexus_agent.agent`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py)
- `ResolvedIPv6Security` — [`nexus_agent.security_profile`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py)
- `RouterAuthMetadata` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `RouterBootstrapMetadata` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `RouterCloudMetadata` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `RouterCloudTransportMetadata` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `RouterLanSessionProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `RunInput` — [`nexus_agent.inbox`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/inbox.py)
- `SSHTestResult` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `SSHWorkspaceConnection` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `SSHWorkspaceConnectionCreate` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `SSHWorkspaceConnectionUpdate` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `ServerAuthPolicy` — [`nexus_agent.server_auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py)
- `ServerAuthenticationError` — [`nexus_agent.server_auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server_auth.py)
- `SseEvent` — [`nexus_agent.models`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/models.py)
- `StaticTokenProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `TokenProvider` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `UnixAddressdTransport` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `WindowsAddressBackend` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `WindowsNamedPipeTransport` — [`nexus_agent.windows_pipe`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/windows_pipe.py)
- `WorkspaceEntry` — [`nexus_agent.workspace`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/workspace.py)
- `current_run` — [`nexus_agent.reporting`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/reporting.py)
- `default_addressd_transport` — [`nexus_agent.host_alias`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/host_alias.py)
- `discover_router_auth` — [`nexus_agent.auth`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/auth.py)
- `install_descriptor` — [`nexus_agent.security_profile`](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py)
