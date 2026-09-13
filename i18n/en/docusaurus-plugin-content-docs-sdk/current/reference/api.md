---
sidebar_position: 2
title: Python API reference
---

# Python API reference

The following objects are public exports of the top-level `nexus_agent` package. Source docstrings and type annotations define the complete parameters and return types.

For parameters, results, fields and errors, see the [detailed reference](coverage.md). Learn how to compose these APIs in [Agent design](../design/overview.md).

## Agent and client

- `NexusAgent`: high-level capability declaration, server, registration, renewal, and cleanup.
- `NexusAgentHandle`: lifecycle handle for a running agent.
- `PublishedCapability`: capability published by the high-level runtime.
- `NexusAgentClient`: registration, renewal, discovery, and invocation client.
- `AgentLease`: client-managed registration lease.
- `NexusAgentServer`: HTTP/SSE agent server.
- `AgentRequestError`: malformed request or handler error.
- `CapabilityRegistration`: capability registration model.
- `LeaseInfo`: lease response model.

## Request, response, and endpoint models

- `AgentEnvelope`: normalized request passed to a handler.
- `AgentResponse`: response status, headers, and body.
- `SseEvent`: streaming SSE event.
- `BackendTlsIdentity`: backend TLS identity.
- `PublicAgentEndpoint`: public agent endpoint description.

## Token and client authentication

- `TokenProvider`: token provider protocol.
- `StaticTokenProvider`: fixed token provider.
- `EnvironmentTokenProvider`: environment token provider.
- `AutoTokenProvider`: selects authentication from the environment and router metadata.
- `NoTokenProvider`: explicitly supplies no token.
- `OIDCClientCredentialsProvider`: acquires and caches OIDC client-credentials tokens.
- `RouterAuthMetadata`: router authentication discovery result.
- `discover_router_auth`: reads and validates router authentication metadata.

## Server authentication

- `ServerAuthPolicy`: server authentication policy protocol.
- `NoServerAuth`: no caller validation; isolated development only.
- `HmacJwtServerAuth`: validates HS256 JWTs.
- `AuthenticatedCaller`: verified caller identity and claims.
- `ServerAuthenticationError`: server authentication failure.

## IPv6 and host addressing

- `DirectIPv6Agent`: invokes a known IPv6 agent directly.
- `PublicIPv6Agent`: high-level public IPv6 agent runtime.
- `PublicIPv6AgentHandle`: public IPv6 agent lifecycle handle.
- `HostAliasAllocator`: allocates and releases host alias addresses.
- `HostAliasLease`: host alias lease handle.
- `HostAliasLeaseInfo`: host alias lease information.
- `HostAliasError`: host alias operation failure.
- `LinuxAddressBackend`: Linux address configuration backend.
- `WindowsAddressBackend`: Windows address configuration backend.
- `MemoryAddressBackend`: in-memory test backend.
- `LocalAddressdClient`: local addressd client.
- `UnixAddressdTransport`: Unix socket transport.
- `WindowsNamedPipeTransport`: Windows named pipe transport.
- `default_addressd_transport`: returns the platform-default addressd transport.

## Security descriptors

- `NexusSecurityProfile`: loads and validates a security descriptor.
- `ResolvedIPv6Security`: resolved IPv6 security configuration.
- `install_descriptor`: installs a descriptor and associated material.

## Exceptions

- `NexusAgentError`: SDK exception base class.
- `NexusSecurityConfigurationError`: invalid security configuration.
- `NexusAuthDiscoveryError`: authentication metadata discovery failed.
- `NexusTokenAcquisitionError`: token acquisition failed.
- `NexusHttpError`: unsuccessful HTTP response.
- `NexusAuthenticationError`: caller was not authenticated.
- `NexusAuthorizationError`: caller identity is known but lacks permission.

FastMCP objects live in `nexus_agent.fastmcp`; A2A objects live in `nexus_agent.a2a`. See the [FastMCP integration](../integrations/fastmcp.md).

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
