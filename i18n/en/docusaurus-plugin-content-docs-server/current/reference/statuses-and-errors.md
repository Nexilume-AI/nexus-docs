---
sidebar_position: 4
title: Status and error reference
description: Locate Nexus Server states, error codes, evidence, and recovery paths by product area.
---

# Status and error reference

Regular Nexus API responses use the `{ok, data, error, request_id}` envelope. OpenAI-compatible endpoints keep the OpenAI error shape. Save the HTTP status, `error.code`, `error.message`, response `X-Request-ID`, and time when investigating. Never record tokens, cookies, or secrets.

## Start with the HTTP status

| Status | Usual meaning | Check first |
| --- | --- | --- |
| `400` | A field, state transition, or runtime condition is invalid | Error body, current resource state, Swagger schema |
| `401` | No valid identity | Authorization, cookie, expiry, or revocation |
| `403` | Identity is valid but context or permission is insufficient | Workspace, Project, Role, Resource Share, Key Policy |
| `404` | Resource is absent or invisible in this context | Resource ID and Nexus tenant/project headers |
| `409` | Concurrent operation or uniqueness conflict | Active Job, duplicate name, duplicate binding |
| `429` | Plan, quota, or request limit | Plan, Usage, Wallet, Retry-After |
| `5xx` | Server, runtime, or upstream Provider failure | Jobs, Audit, Runtime Health, server logs |

## Identity, context, and common errors

| Code | Evidence | Common cause | Fix |
| --- | --- | --- | --- |
| `NOT_AUTHENTICATED` | `whoami` returns 401 | Missing or expired session/JWT | Sign in again or rotate the automation credential |
| `AUTHENTICATION_FAILED` | Login returns 403 | Incorrect email or password | Verify the account before retrying |
| `NOT_FOUND` | A known ID returns 404 | Wrong ID, soft deletion, or context mismatch | Switch Console context and verify ownership |
| `API_KEY_SCOPE_DENIED` | API Key is valid but action is rejected | Scope or policy excludes the target | Create a purpose-specific, least-privilege key |

## Agent Runtime

| Code | Evidence | Fix |
| --- | --- | --- |
| `AGENT_RUNTIME_NOT_AVAILABLE` | Deployment, Health, current OpenWrt binding | Deploy a healthy runtime or bind a valid edge registration |
| `AGENT_RUNTIME_OPERATION_IN_PROGRESS` | Jobs for the same Agent | Wait for the current job; retry only after it finishes |
| `AGENT_RUNTIME_ERROR` | Deployment `last_error`, Job, container log | Fix the image, port, `/mcp` contract, or runner configuration |
| `AGENT_POLICY_DENIED` | Agent Key Policy, context, Audit | Use a key scoped to this Agent or adjust explicit access |
| `AGENT_STREAMING_NOT_SUPPORTED` | Runtime type and transport | Use a non-streaming call or a runtime that supports streaming |
| `AGENT_RUNTIME_DEPLOY_FAILED` / `STOP_FAILED` / `HEALTH_CHECK_FAILED` / `MCP_REQUEST_FAILED` | Matching Job error | Inspect Docker/OpenWrt, networking, and the MCP server at that stage |

## Router, Provider, and Gateway

| Code | Evidence | Fix |
| --- | --- | --- |
| `MODEL_NOT_FOUND` | Router bindings, Model Pool, Source health | Use a visible model and restore a healthy Source |
| `PROVIDER_ACCOUNT_NOT_FOUND` | Runtime and Provider Account behind the Source | Restore or rebind the Provider Account |
| `ROUTER_RUNTIME_FAILED` | Router Deployment, runtime error, Audit | Fix and redeploy `router.py`, or switch to a built-in policy |
| `ROUTER_RUNTIME_UNAVAILABLE` | Custom runtime deployment and runner installation | Deploy the runtime and configure a supported runner |
| `ROUTER_RUNTIME_INVALID_DECISION` | Custom output and candidate list | Return only Deployment IDs from this Router's candidates |
| `BALANCE_NOT_ENOUGH` | Billing Wallet and failed Usage/Order | Recharge or reduce the operation cost before retrying |

## Data Assets and Billing

| Code | Evidence | Fix |
| --- | --- | --- |
| `DATASET_QUOTA_EXCEEDED` / `PLAN_QUOTA_EXCEEDED` | Plan, Usage, upload size | Release capacity, reduce input, or buy the right plan |
| `MEDIA_ASSET_NOT_FOUND` | Asset ID, Release Manifest, stored object | Verify context and storage integrity |
| `MEDIA_ASSET_INVALID` | Content type, size, processing log | Use a supported format within the upload limit |
| `UNSUPPORTED_CONTENT_TYPE` / `FILE_TOO_LARGE` | Index Job and configured limit | Convert or reduce the file |
| `DECODE_FAILED` / `READ_FAILED` | Index Job and storage readability | Fix encoding, permission, or corrupt data and re-index |
| `PAYMENT_PROVIDER_UNAVAILABLE` | Payment Order and server config | Fix provider configuration/network and create a new order |
| `PAYMENT_WEBHOOK_INVALID` | Signature log and Request ID | Fix key, certificate, amount, or signature settings; never credit manually |

## Verification

After a fix, repeat the smallest failing operation and verify the HTTP result, state transition, completed Job, and matching Audit Request ID. For calls or purchases, also verify Billing Usage or Ledger.

## Troubleshooting and boundaries

- One HTTP status can map to several business codes; trust the returned `error.code` and current source.
- Job codes describe asynchronous completion. A successful submit response is not the final result.
- TokenBank maintains a separate [status and error reference](/tokenbank/reference/statuses-and-errors); financial workflow states are not duplicated here.
- [Swagger](../reference/api.md) remains authoritative for serializer field errors. Use [common troubleshooting](../troubleshooting/common.md) to collect a complete evidence bundle.
