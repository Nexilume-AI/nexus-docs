---
sidebar_position: 1
title: API 约定与可执行示例
description: 认证、Workspace/Project 上下文、响应、Request ID、Agent MCP 和 Router 调用。
---

# API 约定与可执行示例

所有产品 API 位于 `/api/v1/`。本页解释请求路径和关键契约；完整路径、字段、枚举与 Schema 始终以运行中的 Server 为准：

- Swagger：`/api/v1/docs/swagger/`
- Redoc：`/api/v1/docs/redoc/`
- OpenAPI：`/api/v1/schema/`

## 认证方式不要混用

| 身份 | 格式 | 用途 |
| --- | --- | --- |
| Browser Session | HttpOnly Cookie + CSRF | Nexus Console |
| User JWT | `Bearer <access_token>` | 用户脚本和短期 CLI 会话 |
| API Key | `Bearer sk-nexus-...` | Gateway、Agent 或 Remote CLI；由 scope/policy 决定 |
| Service Account | `Bearer sa-nexus-...` | 无人值守自动化 |

Agent Key、Router/Gateway Key 与 `remote_cli` Key 不能互换。使用错误的 Key 往往返回 403，而不是 401。

## 示例 1：登录并验证身份

```bash
export NEXUS_BASE_URL=http://127.0.0.1:8000

curl -sS "$NEXUS_BASE_URL/api/v1/auth/login/" \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"replace-me"}'
```

非 Web Client 的成功响应在 `data.access_token` 与 `data.refresh_token` 返回 Token。浏览器 Console 会发送 `X-Nexus-Client: web`，建立 Session 且不把 Token 放入响应。

```bash
export NEXUS_ACCESS_TOKEN=<access_token>
curl -sS "$NEXUS_BASE_URL/api/v1/auth/whoami/" \
  -H "Authorization: Bearer $NEXUS_ACCESS_TOKEN"
```

不要把密码或 Token 写进 shell history、CI 日志或工单。本地示例只展示请求形状。

## Workspace 和 Project 上下文

```http
Authorization: Bearer <credential>
X-Nexus-Tenant: <workspace UUID>
X-Nexus-Project: <project UUID, optional>
X-Request-ID: <caller correlation ID, optional>
```

`X-Nexus-Tenant` 是 Workspace UUID，绝大多数业务 API 必需。Project 头缩小资源范围；省略时只有明确支持跨项目列表的接口才表示 **All projects**。不要把 Workspace 显示名称、Computer Environment ID 或 OpenWrt Device ID 放进 Tenant 头。

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

Server 会在响应头和 envelope 的 `request_id` 回显/生成 Request ID。

## 响应 envelope

普通成功响应：

```json
{"ok":true,"data":{},"error":null,"request_id":"docs-..."}
```

普通错误响应：

```json
{"ok":false,"data":null,"error":{"code":"NOT_FOUND","message":"..."},"request_id":"docs-..."}
```

OpenAI-compatible Gateway 使用 OpenAI 兼容响应/错误形状，不包普通 Nexus envelope。排错时仍保存响应头 `X-Request-ID`。

## 示例 2：调用 Router

先在 **Routers → Export access** 获取一次性 Router-scoped Key。只有 deployed Router 可以导出。

```bash
export NEXUS_ROUTER_KEY=sk-nexus-...

curl -sS "$NEXUS_BASE_URL/api/v1/openai/v1/chat/completions" \
  -H "Authorization: Bearer $NEXUS_ROUTER_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Request-ID: router-docs-001" \
  -d '{"model":"demo-chat","messages":[{"role":"user","content":"hello"}]}'
```

Export 面板生成的 curl 还包含正确模型/Router 约束，应优先复制该版本。完整教程见 [Provider→Router API](../tutorials/provider-router-api.md)。

## 示例 3：调用 Agent MCP

MCP Streamable HTTP 需要 Session 协议，推荐使用导出的 MCP 配置或 Nexus CLI，而不是手写多个 curl：

```bash
nexus tenant use <workspace-uuid>
nexus project use <project-uuid>
nexus agent mcp export <agent-uuid>
nexus agent mcp call <agent-uuid> --task "first call" --context "source=api-docs" --mode verify
```

Server 代理路径是 `/api/v1/agents/<agent_id>/mcp/`，Runtime 契约是容器内部 `:8000/mcp`。Agent-scoped Key 只允许目标 Agent。

## 公共端点

| 方法与路径 | 用途 |
| --- | --- |
| `GET /api/v1/health/` | 健康检查 |
| `GET /api/v1/public/bootstrap/` | 匿名 Console 启动信息和 CSRF Cookie |
| `POST /api/v1/auth/login/` | 用户 Token 或浏览器 Session |
| `POST /api/v1/auth/logout/` | 注销当前 Session |
| `GET /api/v1/auth/whoami/` | 验证当前身份 |
| `GET /api/v1/schema/` | OpenAPI Schema |
| `GET /api/v1/edge/.well-known/jwks.json` | Edge 调用 JWT 公钥 |

## 重试、幂等和异步结果

- Nexus Server 没有全局 `Idempotency-Key` Header 契约。只有 Swagger 明确包含 `idempotency_key` 字段的产品动作才按其规则去重；TokenBank 的幂等语义见其独立文档。
- POST 超时后先用 Request ID、资源列表或 Job 查询结果，不要盲目重复创建。
- 返回 Job/202/201 只表示已提交时，最终状态在 Observability Job 和目标资源上；同步成功不代表异步工作已完成。
- 对 429/5xx 使用有上限的指数退避，并避免重试不可确认的高风险写操作。

## 验证

- `whoami` 返回预期用户和 Workspace，两个上下文头对应同一资源范围。
- Router 或 Agent 调用产生可匹配的 Request ID、Audit/Activity 和必要的 Billing Usage。
- 自动化使用最小权限、可独立撤销且有过期时间的凭据。

## 排错与当前边界

- 401 查认证；403 查 scope/policy/Role；404 先查上下文；409 查重复绑定或进行中 Job。
- Schema 字段、分页和枚举不在本页复制，避免与代码漂移。
- 认证 URL 当前公开 login/logout/whoami；浏览器优先使用 HttpOnly Session。
- 错误证据与修复入口见[状态与错误](statuses-and-errors.md)和[常见故障](../troubleshooting/common.md)。

## 当前交互与待办 API

以下路径均以 `/api/v1/` 开头，并保留登录、Workspace/Project 和资源授权检查。Private Run 内容要求调用者身份；Inbox 要求个人用户，不能用任意机器凭据替代。

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


任务路径和交互语义见 [Private Run](../agents/private-runs.md)，回执与源对象区别见 [Inbox](../operations/inbox.md)。

## 模型兼容接口

OpenAI 风格客户端的 Base URL 为 `/api/v1/openai/v1`，可用路由包括 `models`、`chat/completions`、`responses` 和 `images/generations`、`images/edits`、`images/variations`。Claude 风格客户端使用 `/api/v1/claude/v1` 下的 `messages` 与 `models`。使用导出的受限 Gateway 凭据；有效模型、输入类型、流式行为和限制以所选 Provider 的能力及当前 Schema 为准。
