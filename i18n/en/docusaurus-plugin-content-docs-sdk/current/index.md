---
slug: /
sidebar_position: 1
title: Python SDK user guide
---

# Python SDK user guide

These docs track SDK 0.46.2 and the Linux fix on main. The distribution is `nexus-openwrt-agent-sdk`; import `nexus_agent`. The core wheel supports Python 3.9+; use Python 3.12 for optional integrations. Existing version URLs remain available and all show current documentation.

- [Installation](quickstart/installation.md)
- [Local HTTP/SSE agent](quickstart/local-serving.md)
- [Connect to OpenWrt](guides/openwrt-agent.md)
- [Hosted MCP](guides/hosted-mcp.md)
- [Computer Runtime](guides/computer-runtime.md)
- [Linux IPv6](guides/linux-ipv6.md)
- [Windows IPv6](guides/windows-ipv6.md)
- [Authentication](guides/authentication.md)
- [API reference](reference/api.md)


:::note Documentation version policy
All version entries show current documentation. Version labels preserve existing URLs; they do not guarantee that every documented feature works on that older software release. Check the software versions and prerequisites stated on each page.
:::


## Design an Agent for your application

Start with the [design path](design/overview.md), run the downloadable example, then add interaction, resources, recovery and usage. See [API coverage](reference/coverage.md) for detailed methods.
