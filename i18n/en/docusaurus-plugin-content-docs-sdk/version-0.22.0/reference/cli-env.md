---
sidebar_position: 1
title: CLI and environment
---

# CLI and environment

## Commands

| Command | Purpose |
| --- | --- |
| `nexus-agent` | Windows IPv6 `setup` and `doctor` |
| `nexus-agent-security` | Install and resolve security descriptors |
| `nexus-agent-addressd` | Unix address helper daemon |
| `nexus-agent-addressd-service` | Windows address helper service |

Use `COMMAND --help` for the current version's complete parameters.

## Common environment variables

| Variable | Purpose |
| --- | --- |
| `NEXUS_ROUTER_URL` | Router gateway URL |
| `NEXUS_AGENT_TOKEN` | Default access token |
| `NEXUS_AGENT_ADDRESS` | Published agent address |
| `NEXUS_AGENT_IPV6` | IPv6 compatibility setting |
| `NEXUS_AGENT_CLIENT_ID` | OIDC client ID |
| `NEXUS_AGENT_CLIENT_SECRET` | OIDC client secret |
| `NEXUS_AGENT_SECURITY_PROFILE` | Security descriptor path |
| `NEXUS_AGENT_ADDRESSD_SOCKET` | Unix addressd socket |
| `NEXUS_AGENT_ADDRESSD_PIPE` | Windows addressd named pipe |

Compatibility variables `NEXUS_JWT`, `NEXUS_AGENT_JWT`, and `NEXUS_TOKEN` are still read, but new deployments should use `NEXUS_AGENT_TOKEN`.
