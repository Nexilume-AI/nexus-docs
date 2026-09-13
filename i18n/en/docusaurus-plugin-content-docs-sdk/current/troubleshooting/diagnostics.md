---
sidebar_position: 1
title: SDK diagnostics
---

# SDK diagnostics

By default, the diagnostic script makes no network request. It reports Python, SDK, optional integrations, and whether environment variables are present. It never prints token or client-secret values.

## Run local checks

```bash
python docs-site/static/downloads/nexus-sdk-diagnostics.py
```

## Check router DNS and TCP

```bash
python docs-site/static/downloads/nexus-sdk-diagnostics.py \
  --router https://router.example:7443 --connect
```

`--connect` opens a TCP connection only. It sends no HTTP request or credential and does not prove TLS, authentication, authorization, or Agent routing.

## Read the output

- Whether `nexus_agent` imports and its version.
- Whether `fastmcp`, `a2a`, and `win32api` match your use case.
- Whether `NEXUS_ROUTER_URL`, `NEXUS_AGENT_TOKEN`, and related variables are set; values are never printed.
- Whether DNS returns expected addresses and TCP connects before the timeout.

Review hostnames, usernames, and network addresses before sharing the output.
