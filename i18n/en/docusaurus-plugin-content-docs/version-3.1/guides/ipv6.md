---
sidebar_position: 3
title: Configure IPv6 access
---

# Configure IPv6 access

IPv6 can give agents stable, routed addresses across subnets, but “routable” does not mean “safe for public access.” Production deployments require authentication and narrow firewall rules.

## Router checks

1. In OpenWrt **Network → Interfaces**, confirm that the LAN receives a global IPv6 prefix.
2. Confirm that the host has a global unicast address, not only an `fe80::/10` link-local address.
3. Enable the required IPv6 listener under **Agent Router → Advanced Settings**.
4. Permit only expected source addresses and ports through the firewall.
5. Test TCP reachability from another subnet before testing an Agent call.

## Windows agents

The SDK includes a Windows IPv6 command that selects an address and port and runs diagnostics. See [Windows IPv6](/sdk/guides/windows-ipv6).

## Security checklist

- Use TLS and verify the server identity.
- Enable tokens or OIDC; do not expose anonymous administration.
- Do not expose LuCI, ubus, or internal diagnostic ports to the Internet.
- Configure lease and key rotation with a documented revocation path.
