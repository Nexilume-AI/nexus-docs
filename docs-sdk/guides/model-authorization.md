---
title: MCP 上游模型 API 授权
---

# MCP 上游模型 API 授权

当 MCP Agent 需要调用模型 API 时，可以通过 Nexus Cloud 向当前调用者请求授权。例如，Atrex Kernel Agent 需要模型生成和优化代码。授权由 Cloud 校验和保存，Agent 的受信任执行端在运行时取得凭据；模型和 MCP 工具结果只接触授权引用与非敏感配置。

## 两种凭据不要混淆

| 用途 | 含义 |
| --- | --- |
| MCP 连接凭据 | 证明客户端是谁、能否调用该 Agent；通常由客户端配置中的 Authorization 请求头提供。 |
| 上游模型授权 | 允许 Agent 使用指定 Provider、Endpoint、模型及有效期内的凭据，可能产生模型费用。 |

连接 MCP 成功不等于已授权模型费用。此流程不会自动读取或转交 Codex 等客户端自身的登录令牌，也不会自动配置 GPU 或执行服务。

## 用户确认流程

1. Agent 调用 SDK 的 `ProviderCredentials.authorize()`。Atrex 对外提供 `authorize_atrex_provider` 工具。
2. Cloud 识别当前调用者，并检查是否已有符合范围的有效授权；有则复用。
3. 需要新授权时，根据客户端声明的能力展示确认表单或返回安全网页链接。
4. 用户选择配置、有效期，并明确同意授权及可能产生的模型费用。
5. 客户端读取授权状态；只有 `status: "authorized"` 才可启动需要模型的任务。
6. 执行端检查授权后发起模型请求，密钥不进入对话、MCP 返回值、日志或训练数据。

| 情况 | 确认方式 |
| --- | --- |
| Nexus Cloud，客户端支持 MCP form elicitation | 对话内选择 Router / 模型、有效期并确认，无需输入 Key。 |
| 第三方 Provider，有符合范围的已保存授权 | 支持 form elicitation 时，可在客户端确认使用已授权的 Endpoint / 模型。 |
| 新增第三方 Key、变更第三方授权范围或选择 Configure securely | 在已登录的 Cloud 授权页填写并确认。 |
| 客户端不支持表单 | 使用安全网页；支持 URL elicitation 时可提示打开，否则工具返回 `authorization_url`。 |

“对话内确认”指客户端提供的授权表单，不是让用户把 Key 发到聊天里。打开网页或接受 URL 提示本身不构成授权；仍须由调用者本人完成服务端确认。不同客户端的表单支持和呈现方式可能不同。

## Nexus Cloud：选择 Router，无需 Key 或 Endpoint

选择 `provider: "nexus"` 后，Cloud 提供当前调用者在调用上下文中有权使用的已部署 Router 及其模型输出名称。用户选择 Router / 模型后，Cloud 创建限定该 Router、模型及有效期的临时凭据。

- 无需填写 API Key 或 Base URL。
- 使用量归属所选 Router 的 Organization / project。
- 权限、调用者身份、授权有效期和撤销状态会在模型网关入口重新检查。
- 没有可选 Router 时，先配置 Router 或取得使用权限；不能通过手填 Router ID 绕过权限。
- 该临时凭据签发能力属于 Enterprise / Cloud 组合，不应假定 Personal 部署也提供。

第三方 Provider 支持 `openai`、`anthropic`、`custom_openai`、`custom_anthropic`。预设 Provider 的 Endpoint 固定；自定义 Endpoint 必须是公共 HTTPS API Base URL，不是 `/responses` 或 `/chat/completions` 完整路径。Atrex 的 OpenAI-compatible 后端需要 Responses，Anthropic-compatible 后端需要 Messages。

## Atrex MCP 调用示例

请求 Nexus Cloud 授权；可省略 `model` 让用户选择：

```json
{"provider":"nexus","model":"gpt-6-sol","wait_seconds":15}
```

将以上参数传给 `authorize_atrex_provider`。它返回 `authorization_id`、`status`、`provider`、`base_url`、`model`、`router_id`、`expires_at` 和 `authorization_url` 等元数据，不返回 Key。候选模型必须实际出现在可用 Router 中，示例名称不保证可用。

用户确认后，再调用同一工具查询：

```json
{"authorization_id":"<returned-authorization-id>"}
```

读取返回的最终配置，不要沿用用户确认前的模型猜测。启动 `start_atrex_optimization` 时传入项目凭据、该 `authorization_id`、批准的 `provider` / `model` 和新的 UUID `request_id`；可选 `base_url` 用于断言目标与授权一致。传输重试复用同一个 `request_id`，避免重复提交。

## 重复调用、更换 API 与撤销

| 操作 | 行为 |
| --- | --- |
| 同一调用者、Agent、tenant、project、Provider / Endpoint 下继续使用匹配模型 | 有效授权可以复用，不必每次确认。请求省略模型时可能复用该范围内的已有授权，务必读取返回模型。 |
| 更换 Key、Provider、Endpoint、模型或 Nexus Router | 新一次调用 `authorize_atrex_provider`，设置 `force_new: true`，由用户重新选择并确认。 |
| 只查状态 | 传入 `authorization_id`，不会创建替代授权。 |
| 撤销 | 打开授权页点击 Revoke access；派生自已保存凭据的授权也受原授权撤销约束。 |
| 到期或已撤销 | 重新申请授权；不会静默延长有效期。 |

待确认请求有效期为 **10 分钟**。当前确认界面提供 **5 分钟、1 小时、24 小时**，默认 **1 小时**。`wait_seconds` 只控制本次工具等待确认的时间（0–20 秒，默认 15 秒），不是授权有效期；工具返回 `pending` 后，用户仍可在请求到期前确认，再查询同一个 ID。

```json
{"provider":"nexus","force_new":true,"wait_seconds":15}
```

以上参数跳过已有有效授权的自动复用，进入新的确认流程。新授权不会撤销旧授权，也不会把正在执行的任务切换到新凭据。需要切换现有任务时，取消旧任务后使用新授权和新 `request_id` 提交。Atrex 在执行中检查授权，撤销或到期会阻止后续模型请求并触发任务停止；已经发出的请求及其费用不能撤回。

## SDK 接入

在有效的 HTTPS Cloud Run 上下文中使用：

```python
from nexus_agent import current_run
from nexus_agent.credentials import ProviderCredentials

credentials = ProviderCredentials(current_run())
grant = credentials.authorize("nexus", model="gpt-6-sol", wait_seconds=0)
# 返回 grant 的非敏感元数据给调用者。确认后，在有效调用中查询：
grant = credentials.status(grant["authorization_id"])
# 仅当 grant["status"] == "authorized" 时继续需要模型的工作。
```

`resolve_for_runtime(authorization_id)` 仅供受信任的执行代码调用，不可注册为 MCP 工具。其返回值包含真实凭据，不可返回给模型、写入提示词、日志、产物、Data Assets 或训练导出。只在授权操作的受控内存中使用。

Cloud 运维需要应用 Agent 数据库迁移，配置共享的 `NEXUS_SECRET_ENCRYPTION_KEYS`、公共 HTTPS `NEXUS_PUBLIC_BASE_URL`，并将允许请求模型授权的 Agent UUID 加入 `NEXUS_AGENT_CREDENTIAL_ENABLED_AGENTS`（默认空）。所有服务进程使用同一加密 Keyring，配置变更后重启相应服务。调用者必须可被可靠识别；共享或无法确定所有者的 Key 不支持此授权。

## 常见情况

- **MCP 已连接但无法开始优化**：先检查执行环境就绪，再检查授权状态及实际批准的模型。
- **工具等待结束仍为 pending**：等待用户确认，再查同一授权 ID，不要反复创建请求。
- **需要更换配置但直接复用了旧授权**：使用新的工具调用并设置 `force_new: true`。
- **页面提示登录或无权限**：使用发起 MCP 调用的凭据所有者登录，确认个人调用凭据与组织权限。
- **想看到内部进度**：模型授权与任务进度是独立功能。新 Atrex 任务支持[后台事件推送](./background-events.md)和实时页面，`get_atrex_job` 仍可查询快照。
