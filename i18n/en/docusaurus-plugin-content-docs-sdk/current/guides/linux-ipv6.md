---
sidebar_position: 4
title: Configure Linux Agent IPv6
---

# Configure Linux Agent IPv6

Two paths are available: OpenWrt can manage an agent's address, or a Linux host can run the SDK address service to allocate per-agent `/128` addresses on a suitable IPv6 network.

For host-managed addresses, Linux needs systemd, `iproute2`, administrator permission for initial setup, and a network that supports the selected addressing mode. An IPv6 address by itself does not establish inbound Internet routing.

```sh
nexus-agent ipv6 setup
nexus-agent ipv6 doctor
```

Setup discovers supported configurations and requests elevation for system changes. Supported modes include `routed-prefix`, `upstream-relay` and `dhcpv6-ia-na`; use `nexus-agent ipv6 setup --help` to select an interface or mode explicitly. Only specify a prefix routed or delegated to your deployment.

The source checkout also includes a user-local installer:

```sh
sh install-linux.sh --wheel /path/to/downloaded.whl --install-only
```

Omit `--install-only` to continue into IPv6 setup. Run the installer as your normal user, without `sudo`.

**Known issue in the published 0.46.2 wheel:** the generated Linux address service can fail to assign its Unix socket group. The fix adds `Group=nexus-agent` to the systemd service and has passed local validation, but has not yet shipped in a new release. For an affected installation, add this service override:

```sh
sudo systemctl edit nexus-agent-addressd.service
```

```ini
[Service]
Group=nexus-agent
```

```sh
sudo systemctl daemon-reload
sudo systemctl restart nexus-agent-addressd.service
nexus-agent ipv6 doctor
```

This applies after setup has created the service and group. Keep the existing capability restrictions intact. If setup added your user to a group, start a new login session before using the address service as that user.

## Validation scope

Local acceptance on **Ubuntu 24.04, Python 3.12, WSL2 with systemd** verified:

- HTTP Agent Serving and SSE streaming.
- Hosted MCP tool discovery and invocation.
- Real headless Chromium navigation, clicking and screenshots.
- Computer Runtime enrollment, WSS transport, file operations and command execution through a local Community Cloud.
- Non-root IPv6 allocation, JWT invocation and address release in an isolated network namespace.
- Automatic service recovery, identity retention and Cloud reconnection after restarting the Linux environment.

The SDK regression suite reported **354 passed and 17 skipped**. IPv6 acceptance used the service group fix above. Cloud screenshot acceptance also required the Community server's Django `MEDIA_ROOT` to point to its configured writable media storage directory.

Public Internet IPv6 ingress, real upstream DHCPv6 and bare-metal Linux acceptance remain separate checks. These results do not certify every Linux distribution or every optional integration. macOS has not received equivalent end-to-end acceptance; Intel macOS users also need to account for the `computer` extra's cryptography source-build requirements.
