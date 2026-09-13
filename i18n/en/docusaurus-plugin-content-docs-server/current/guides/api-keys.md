---
sidebar_position: 1
title: How to create and use an API key
---

# How to create and use an API key

API keys are for Gateway, Agent MCP, and project integrations. Plaintext is shown once.

## Steps

1. Sign in as a tenant or target-project administrator.
2. Open **Settings → API Keys**, choose tenant and optional project, then select `gateway` or `remote_cli` scope.
3. Copy the `sk-nexus-...` secret immediately into a secret manager.
4. Call an API:

```bash
curl http://127.0.0.1:8000/api/v1/agents/ \
  -H "Authorization: Bearer $NEXUS_API_KEY" \
  -H "X-Nexus-Tenant: $NEXUS_TENANT_ID"
```

5. Use **Disable** for a reversible pause and **Revoke** for permanent retirement.

## Verification and troubleshooting

Check `last_used_at` and usage summary. Lists never return the secret again. Tenant/project mismatch errors mean the request headers and key scope differ. `API_KEY_SCOPE_DENIED` means a `remote_cli` key was used for Gateway traffic.

See [Identity and request paths](../concepts/identity-and-request-path.md).
