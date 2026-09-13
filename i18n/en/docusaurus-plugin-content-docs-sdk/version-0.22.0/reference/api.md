---
sidebar_position: 2
title: Python API reference
---

# Python API reference

The following objects are public exports of the top-level `nexus_agent` package. Source docstrings and type annotations define the complete parameters and return types.

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
