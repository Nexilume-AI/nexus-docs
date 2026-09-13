---
sidebar_position: 1
title: API conventions and runnable examples
description: Authentication, Workspace/Project context, responses, Request ID, Agent MCP, and Router calls.
---

# API conventions and runnable examples

Product APIs live under `/api/v1/`. This page explains request paths and key contracts. The running Server remains authoritative for routes, fields, enums, and schemas:

- Swagger: `/api/v1/docs/swagger/`
- Redoc: `/api/v1/docs/redoc/`
- OpenAPI: `/api/v1/schema/`

## Do not mix credential types

| Identity | Form | Use |
| --- | --- | --- |
| Browser Session | HttpOnly Cookie + CSRF | Nexus Console |
| User JWT | `Bearer <access_token>` | User scripts and short CLI sessions |
| API Key | `Bearer sk-nexus-...` | Gateway, Agent, or Remote CLI according to scope/policy |
| Service Account | `Bearer sa-nexus-...` | Unattended automation |

Agent, Router/Gateway, and `remote_cli` keys are not interchangeable. The wrong valid key usually returns 403 rather than 401.

## Example 1: sign in and verify identity

```bash
export NEXUS_BASE_URL=http://127.0.0.1:8000

curl -sS "$NEXUS_BASE_URL/api/v1/auth/login/" \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"replace-me"}'
```

A non-Web client receives `data.access_token` and `data.refresh_token`. Console sends `X-Nexus-Client: web`, creates a Session, and does not expose tokens in the response.

```bash
export NEXUS_ACCESS_TOKEN=<access_token>
curl -sS "$NEXUS_BASE_URL/api/v1/auth/whoami/" \
  -H "Authorization: Bearer $NEXUS_ACCESS_TOKEN"
```

Do not put passwords or tokens in shell history, CI logs, or support tickets. The local example only shows request shape.

## Workspace and Project context

```http
Authorization: Bearer <credential>
X-Nexus-Tenant: <workspace UUID>
X-Nexus-Project: <project UUID, optional>
X-Request-ID: <caller correlation ID, optional>
```

`X-Nexus-Tenant` is the Workspace UUID and is required by most product APIs. Project narrows resource scope. Omission means **All projects** only on endpoints that explicitly support cross-project lists. Never place a Workspace display name, Computer ID, or OpenWrt Device ID in the tenant header.

```bash
export NEXUS_WORKSPACE_ID=<workspace-uuid>
export NEXUS_PROJECT_ID=<project-uuid>
export NEXUS_REQUEST_ID=docs-$(date +%s)

curl -sS "$NEXUS_BASE_URL/api/v1/auth/whoami/" \
  -H "Authorization: Bearer $NEXUS_ACCESS_TOKEN" \
  -H "X-Nexus-Tenant: $NEXUS_WORKSPACE_ID" \
  -H "X-Nexus-Project: $NEXUS_PROJECT_ID" \
  -H "X-Request-ID: $NEXUS_REQUEST_ID"
```

Server returns Request ID in both the response header and regular envelope.

## Response envelope

Regular success:

```json
{"ok":true,"data":{},"error":null,"request_id":"docs-..."}
```

Regular error:

```json
{"ok":false,"data":null,"error":{"code":"NOT_FOUND","message":"..."},"request_id":"docs-..."}
```

OpenAI-compatible Gateway responses keep the OpenAI shape rather than the Nexus envelope. Preserve the `X-Request-ID` response header for investigation.

## Example 2: call a Router

Get the one-time Router-scoped key from **Routers → Export access**. Only a deployed Router can export.

```bash
export NEXUS_ROUTER_KEY=sk-nexus-...

curl -sS "$NEXUS_BASE_URL/api/v1/openai/v1/chat/completions" \
  -H "Authorization: Bearer $NEXUS_ROUTER_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Request-ID: router-docs-001" \
  -d '{"model":"demo-chat","messages":[{"role":"user","content":"hello"}]}'
```

Prefer the generated curl because it includes the correct model/Router policy. See [Provider→Router API](../tutorials/provider-router-api.md).

## Example 3: call Agent MCP

MCP Streamable HTTP is session-based. Use exported MCP config or Nexus CLI rather than manually reproducing several curl exchanges:

```bash
nexus tenant use <workspace-uuid>
nexus project use <project-uuid>
nexus agent mcp export <agent-uuid>
nexus agent mcp call <agent-uuid> --task "first call" --context "source=api-docs" --mode verify
```

The Server proxy is `/api/v1/agents/<agent_id>/mcp/`; the container contract is `:8000/mcp`. An Agent-scoped key permits only its target Agent.

## Public endpoints

| Method and path | Use |
| --- | --- |
| `GET /api/v1/health/` | Health check |
| `GET /api/v1/public/bootstrap/` | Anonymous Console bootstrap and CSRF cookie |
| `POST /api/v1/auth/login/` | User tokens or browser Session |
| `POST /api/v1/auth/logout/` | End current Session |
| `GET /api/v1/auth/whoami/` | Verify current identity |
| `GET /api/v1/schema/` | OpenAPI schema |
| `GET /api/v1/edge/.well-known/jwks.json` | Edge-call JWT public keys |

## Retries, idempotency, and asynchronous results

- Nexus has no global `Idempotency-Key` header contract. Only actions whose Swagger body includes `idempotency_key` deduplicate according to that product. TokenBank documents its semantics separately.
- After a POST timeout, inspect Request ID, resource lists, or Jobs before repeating a create.
- A Job/202/201 submit response is not necessarily final. Verify the target resource and Observability Job.
- Use bounded exponential backoff for 429/5xx and avoid blind retries of uncertain high-risk writes.

## Verification

- `whoami` returns the expected user/Workspace and context matches the target resource.
- Router or Agent calls create matching Request ID, Audit/Activity, and required Billing Usage.
- Automation credentials are least-privilege, independently revocable, and expiring.

## Troubleshooting and current boundaries

- Investigate authentication for 401, policy/Role for 403, context for 404, and active work/duplicates for 409.
- This page does not duplicate schema fields, pagination, or enums.
- Public authentication routes are login/logout/whoami; browsers should prefer HttpOnly Session.
- See [status and errors](statuses-and-errors.md) and [common troubleshooting](../troubleshooting/common.md).

## Current interaction and work APIs

All paths below are under `/api/v1/`, retaining login, Workspace/Project and resource checks. Private Run content is caller-owned; Inbox requires a person rather than arbitrary machine credentials.

| Path | Purpose |
| --- | --- |
| `computers/`, `computers/pairing-codes/` | Computer Runtime inventory and pairing |
| `computers/{id}/revoke/` | Revoke a paired Computer |
| `agents/{id}/runtime/python-builds/` | Build configuration, history and upload |
| `agents/{id}/private-runs/` | Create/list private executions |
| `agent-runs/{id}/follow-ups/` | Continuation messages |
| `agent-runs/{id}/cancel/`, `recovery/`, `resume/` | Explicit execution control |
| `inbox/items/`, `inbox/summary/` | Work Inbox list/summary |
| `inbox/preferences/`, `inbox/stream/` | Personal preferences and change stream |


See [Private Runs](../agents/private-runs.md) for execution semantics and [Inbox](../operations/inbox.md) for receipts versus source actions.

## Model compatibility endpoints

The OpenAI-style base URL is `/api/v1/openai/v1`, with `models`, `chat/completions`, `responses`, `images/generations`, `images/edits` and `images/variations`. Claude-style clients use `messages` and `models` under `/api/v1/claude/v1`. Use exported scoped Gateway credentials. Valid models, input types, streaming behavior and limits depend on Provider capabilities and current Schema.
