---
sidebar_position: 4
title: 状态与错误参考
description: 按产品域定位 Nexus Server 状态、错误码、证据和修复入口。
---

# 状态与错误参考

Nexus API 的普通响应使用 `{ok, data, error, request_id}` envelope；OpenAI 兼容接口保持 OpenAI 错误格式。排错时同时保存 HTTP 状态、`error.code`、`error.message`、响应头 `X-Request-ID` 和发生时间。不要记录 Token、Cookie 或 Secret。

## HTTP 状态先告诉你什么

| 状态 | 通常含义 | 先检查 |
| --- | --- | --- |
| `400` | 字段、状态流转或运行条件不满足 | 响应错误、当前资源状态、Swagger Schema |
| `401` | 没有有效身份 | Authorization、Cookie、Token 是否过期或撤销 |
| `403` | 身份有效，但上下文或权限不足 | Workspace、Project、Role、Resource Share、Key Policy |
| `404` | 资源不存在，或当前上下文不可见 | 资源 ID、`X-Nexus-Tenant`、`X-Nexus-Project` |
| `409` | 并发操作或唯一性冲突 | 当前 Job、重复名称、重复绑定 |
| `429` | 套餐、配额或调用速率限制 | Plan、Usage、Wallet、Retry-After |
| `5xx` | Server、Runtime 或上游 Provider 失败 | Observability Job、Audit、Runtime Health、Server 日志 |

## 身份、上下文和通用错误

| 错误码 | 现象与证据 | 常见原因 | 修复 |
| --- | --- | --- | --- |
| `NOT_AUTHENTICATED` | `whoami` 返回 401 | 缺少或失效的会话/JWT | 重新登录或轮换自动化凭据 |
| `AUTHENTICATION_FAILED` | Login 返回 403 | 邮箱或密码不正确 | 校验账号，避免反复重试触发外围防护 |
| `NOT_FOUND` | 已知 ID 返回 404 | ID 错误、软删除或 Workspace/Project 不匹配 | 切换 Console 上下文并核对资源归属 |
| `API_KEY_SCOPE_DENIED` | API Key 身份有效但动作被拒绝 | Key scope 或 Policy 不允许目标资源 | 创建用途正确、权限更小的新 Key |

## Agent Runtime

| 错误码 | 查询证据 | 修复 |
| --- | --- | --- |
| `AGENT_RUNTIME_NOT_AVAILABLE` | Deployment、Health、当前 OpenWrt 绑定 | 部署并健康检查 Runtime，或重新绑定有效边缘注册 |
| `AGENT_RUNTIME_OPERATION_IN_PROGRESS` | **Observability → Jobs** 中同一 Agent 的运行任务 | 等待当前任务结束；失败后按 Job error 重试 |
| `AGENT_RUNTIME_ERROR` | Deployment `last_error`、Job、容器日志 | 修复镜像、端口、MCP `/mcp` 契约或运行器配置 |
| `AGENT_POLICY_DENIED` | Agent Key Policy、Workspace/Project、Audit | 使用匹配 Agent 的 Key，或调整显式资源授权 |
| `AGENT_STREAMING_NOT_SUPPORTED` | Runtime 类型与调用 transport | 改用非流式调用，或换用支持流式转发的 Runtime |
| `AGENT_RUNTIME_DEPLOY_FAILED` / `STOP_FAILED` / `HEALTH_CHECK_FAILED` / `MCP_REQUEST_FAILED` | 对应 Job 的 `error_code` 和 `error_message` | 按失败阶段检查 Docker/OpenWrt、网络和 MCP Server |

## Router、Provider 与 Gateway

| 错误码 | 查询证据 | 修复 |
| --- | --- | --- |
| `MODEL_NOT_FOUND` | Router 绑定、Model Pool、Source enabled/health | 使用可见模型名，恢复至少一个健康 Source |
| `PROVIDER_ACCOUNT_NOT_FOUND` | Source 对应 Runtime 和 Provider Account | 恢复或重新绑定 Provider Account |
| `ROUTER_RUNTIME_FAILED` | Router Deployment、runtime error、Audit | 修复并重新部署 `router.py`，或临时切回内置策略 |
| `ROUTER_RUNTIME_UNAVAILABLE` | 自定义 Runtime 是否部署、运行器是否安装 | 部署 Runtime；生产节点安装并配置受支持运行器 |
| `ROUTER_RUNTIME_INVALID_DECISION` | 自定义 Router 输出和候选列表 | 只返回当前 Router 候选中的 Deployment ID |
| `BALANCE_NOT_ENOUGH` | Billing Wallet、失败 Usage/Order | 充值或降低本次调用/购买成本后重试 |

## Data Assets 与 Billing

| 错误码 | 查询证据 | 修复 |
| --- | --- | --- |
| `DATASET_QUOTA_EXCEEDED` / `PLAN_QUOTA_EXCEEDED` | Plan、当前 Usage、上传大小 | 释放容量、降低输入或购买合适套餐 |
| `MEDIA_ASSET_NOT_FOUND` | Asset ID、Release Manifest、存储对象 | 核对 Workspace/Project 和存储对象完整性 |
| `MEDIA_ASSET_INVALID` | Content type、大小、处理日志 | 使用支持格式并满足上传上限 |
| `UNSUPPORTED_CONTENT_TYPE` / `FILE_TOO_LARGE` | Index Job 与配置上限 | 转换格式或减小文件 |
| `DECODE_FAILED` / `READ_FAILED` | Index Job、对象存储可读性 | 修复编码、权限或损坏对象后重新索引 |
| `PAYMENT_PROVIDER_UNAVAILABLE` | Payment Order、Server 配置 | 检查支付 Provider 配置和网络，再创建新订单 |
| `PAYMENT_WEBHOOK_INVALID` | Webhook 验签日志与 Request ID | 校准密钥、证书、金额和签名配置；不要手工入账 |

## 验证

修复后不要只看弹窗。重复最小操作，并确认：HTTP 成功、资源状态推进、对应 Job 完成、Audit 中 Request ID 一致；涉及调用或购买时再核对 Billing Usage/Ledger。

## 排错与边界

- 同一 HTTP 状态可能对应不同业务码，以响应和源码中的实际 `error.code` 为准。
- Job 失败码描述异步阶段；同步 API 可能只返回提交成功，最终结果要看 Job。
- TokenBank 有独立的[状态与错误码参考](/tokenbank/reference/statuses-and-errors)，本页不复制金融工作流状态。
- 未列出的 Serializer 字段错误以 [Swagger](../reference/api.md) 为准；从[常见故障排查](../troubleshooting/common.md)收集完整证据。
