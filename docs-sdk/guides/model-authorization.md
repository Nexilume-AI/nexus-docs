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
| 新增第三方 Key、变更第三方授权范围或选择 Configure securely | 托管版可凭有效的短时授权链接免登录填写并确认；Personal 部署仍使用其登录流程。 |
| 客户端不支持表单 | 使用安全网页；支持 URL elicitation 时可提示打开，否则工具返回 `authorization_url`。 |

“对话内确认”指客户端提供的授权表单，不是让用户把 Key 发到聊天里。打开网页或接受 URL 提示本身不构成授权；仍须由提供凭据或 Router 的用户完成服务端校验和明确确认。不同客户端的表单支持和呈现方式可能不同。

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
- **页面提示登录或无权限**：托管版选择 Nexus Cloud 时登录自己的账户并检查 Router 权限；第三方 Key 的免登录链接需未过期且未使用。Personal 部署按其凭据所有者登录流程处理。
- **想看到内部进度**：模型授权与任务进度是独立功能。新 Atrex 任务支持[后台事件推送](./background-events.md)和实时页面，`get_atrex_job` 仍可查询快照。


## 网页中的 Model provider 选择

授权页面通过 **Model provider** 统一选择连接方式，不再提供单独的
“Use my Nexus Router”按钮。页面采用简洁卡片和手机适配布局，没有折叠区域。

在托管版 **cloud.nexilume.com**：

- 选择 **Nexus Cloud**：使用浏览器中真实登录的用户身份，显示该用户有权使用的 Router 和模型；无需填写 Key 或 Endpoint。
- 未登录时显示登录入口，也可直接切换到其他 Provider。
- 选择其他 Provider：凭有效的短时授权链接填写自己的 Endpoint、模型和 Key，无需登录 Nexus。
- 链接从创建起最多有效 5 分钟，授权或取消后不可再次使用；打开链接不会自动确认。
- 链接不授予发布者账户的查看权限。Router 列表来自当前登录用户，费用归属所选 Router 的 Organization / project。
- 切换 Provider 会清空输入的 Key 和确认勾选；提交时再次校验身份、权限和授权范围。

此网页的账户选择与对话内 MCP form elicitation 不同：后者仍使用经认证的 MCP 调用上下文。
Personal 开源部署保留其凭据输入流程，不提供托管版的免登录链接或 Router 临时凭据签发；
选择 Nexus Cloud 时也需提供自己的 Key。


## 可选：在 MCP 客户端配置中显式预授权

托管版和 Personal 开源部署均支持以下 Nexus 请求头扩展。它不是 MCP 工具参数。
不填写这些请求头时，继续使用原有网页授权方式。MCP 连接必须使用可识别所有者的个人凭据，
且管理员已为此 Agent 启用模型授权。

```toml
# Optional upstream model preauthorization for this MCP Agent.
# Environment variables contain keys; never put them in tool arguments.
[mcp_servers.my_agent]
url = "https://cloud.nexilume.com/api/v1/agents/<agent-id>/mcp/"
bearer_token_env_var = "NEXUS_MCP_API_KEY"

[mcp_servers.my_agent.http_headers]
X-Nexus-Tenant = "<tenant-id>"
X-Nexus-Upstream-Preauthorize = "true"
X-Nexus-Upstream-Provider = "custom_openai"
X-Nexus-Upstream-Endpoint = "https://api.example.com/v1"
X-Nexus-Upstream-Model = "<model-id>"
X-Nexus-Upstream-TTL-Seconds = "3600"

[mcp_servers.my_agent.env_http_headers]
X-Nexus-Upstream-Key = "NEXUS_UPSTREAM_API_KEY"
```

Codex 支持 `http_headers` 和从环境变量读取值的 `env_http_headers`
（[官方配置参考](https://developers.openai.com/codex/config-reference/)）。
在运行客户端的进程环境中设置 `NEXUS_MCP_API_KEY` 与 `NEXUS_UPSTREAM_API_KEY`：
前者连接 Nexus MCP，后者访问上游模型，两者用途不同。
其他 HTTP MCP 客户端也可发送这些请求头；不支持环境变量的客户端可以在私有配置中直接填写
`X-Nexus-Upstream-Key`，但不要提交或分享包含真实密钥的文件。
Nexus 不读取 MCP 配置中任意添加的顶层 `endpoint`、`model`、`key` 字段。

| 请求头 | 要求 |
| --- | --- |
| `X-Nexus-Upstream-Preauthorize` | 必须是字符串 `true`，明确允许此 Agent 使用模型凭据并产生模型费用。 |
| `X-Nexus-Upstream-Endpoint` | 必填公共 HTTPS API Base URL，不得包含凭据、查询参数、fragment 或私网 DNS/IP。 |
| `X-Nexus-Upstream-Model` | 必填精确模型标识。 |
| `X-Nexus-Upstream-Key` | 必填上游 Key，与 MCP 的 `Authorization` 分开。 |
| `X-Nexus-Upstream-Provider` | 默认 `custom_openai`；也支持 `custom_anthropic`、`openai`、`anthropic`、`nexus`。预设 Provider 必须使用其固定 Endpoint。 |
| `X-Nexus-Upstream-TTL-Seconds` | 默认 `3600`，范围 `300`–`86400` 秒。 |

配置不完整、未明确确认、未知请求头或非法地址返回 HTTP 400，不会自动启用授权。
只填写 `Preauthorize: false` 等价于不配置；关闭时应同时移除其他上游请求头。

服务端在转发或排队前移除这些请求头，在工具调用通过准入检查时创建加密授权，绑定当前
调用者、Agent、tenant 和 project。初始化与工具发现不会创建授权。
每次携带完整预授权配置的新调用都会产生具有指定有效期的授权，这代表客户端配置中的持续同意，
无需逐次网页确认。运行中的任务沿用原授权，轮询不能延长有效期。
移除配置阻止新调用使用先前配置授权，但不会取消正在运行的任务；要停止已有使用，需撤销授权或取消任务。

`ProviderCredentials.authorize()` 返回 `authorized`、`preauthorized: true` 及非敏感配置。
客户端配置的 Provider、Endpoint 和 Model 优先于工具默认参数，包括 `force_new`。
启动工作时必须使用实际返回的配置。更换配置或 Key 后应获取新的授权引用；旧引用无法用于不同配置。
这类凭据不会出现在网页的已保存凭据列表中；移除上游请求头即可恢复网页授权方式。

密钥不会进入工具参数、MCP 结果、转发给 Agent 的请求头、Run 事件或训练导出。
只有受信任执行端可通过回调在校验范围与有效期后解析凭据。
反向代理和额外 HTTP 日志采集也必须排除 `X-Nexus-Upstream-Key`。

## 同一个 Key 就是同一个调用者

同一个 Nexus API Key 在不同客户端和 MCP 会话中代表同一身份，共享该 Key 范围内
仍然有效的模型授权、工作区和配额。需要独立隔离的用户应使用不同 Key。
`X-Nexus-End-User` 只是追踪标签，不构成服务端验证的身份，也不能绕过配额。
模型授权仍绑定调用者、Agent、租户与项目；不同 Key 不能复用或解析其他 Key 的授权。
到期、撤销、用户确认及每次调用显式预授权的规则继续生效。

Agent 使用 `current_run().caller_identity()` 从已认证的 Cloud Run 回调读取
`version`、`principal_type`、`owner_scope` 和 `quota_scope`。工作区绑定不透明的
`owner_scope`（调用者、租户、项目、Agent）；配额绑定 `quota_scope`（调用者、租户），
避免通过切换会话或项目重置限制。不能使用工具参数或自填请求头替代这些身份。
旧 Cloud 未提供此字段时 SDK 拒绝返回身份；转交线程执行时需保留 Python 上下文。

Wave MCP 示例实现了这一机制：每调用者最多两个临时工作区，服务总共四个；
每调用者一个执行名额，总共两个。等待请求按调用者轮转，同一调用者内先进先出；
每调用者最多八个等待请求，总共 32 个，等待十秒超时后返回明确错误。
客户端收到排队错误应退避重试。这些限制针对单个 Wave bridge 进程，不是 Cloud
为所有 Agent 自动施加的统一调度器。


## 模型连接复用与批量授权（Hosted Cloud）

打开 [Model connections](https://cloud.nexilume.com/api/v1/model-connections/page/)，登录自己的 Nexus 账号，保存模型连接，再一次选择多个 Agent 并确认授权。Nexus Cloud 可直接选择自己有权限使用的 Router 与模型；第三方连接填写公开 HTTPS Endpoint、模型和自己的 API Key。保存连接本身不会授权任何 Agent。

同一 Agent 的工具和新对话会在权限有效期间自动复用。新上架的 Agent 不会自动获得权限。连接和每个 Agent 都可以设置有效期（最长 30 天）与请求次数额度，并可分别撤销。两层额度同时扣减；流式请求算一次，上游失败或超时也计入，修改权限不重置计数。这里的额度是请求次数，不是金额或 Token 预算，费用仍由模型提供方或 Router 计费。

原始上游 Key 仅保存在 Cloud；Agent 运行时获得绑定该 Agent 的 Cloud 代理凭据。开发者继续调用 `ProviderCredentials.authorize()` 和 `resolve_for_runtime()`，必须使用返回的 `provider`、`base_url` 和 `model`，不要硬编码上游地址。显式指定的 Endpoint / 模型必须与保存的连接匹配。运行时凭据最多有效 24 小时；再次调用 authorize 可在仍有效的长期权限下自动取得新凭据，无需再次向用户确认。

撤销会阻止新的模型请求，正在接收的流在后续分块检查撤销状态；已经发送到上游的工作仍可能产生费用。重新批准不会复活旧凭据。已有一次性网页授权和 MCP 配置预授权继续保留，独立旧授权需要在原入口单独撤销。此授权不扩大手机、电脑等其他资源权限。
