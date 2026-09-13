---
sidebar_position: 1
title: 从 Provider 到 Router API 调用
description: 接入模型账号、建立两层路由并完成一次可核对的 OpenAI-compatible 请求。
---

# 从 Provider 到 Router API 调用

你将把一个 OpenAI-compatible Provider Account 变成健康 Runtime，再加入 Model Pool、部署 Router，并用 Router-scoped Key 发起调用。完成后，你能从 Observability 和 Billing 解释请求选中了谁、是否成功以及由谁付费。

## 适用角色与前置条件

- Provider 运营者、Agent 构建者或 Workspace Admin。
- 已选中具体 Workspace 和 Project，并有可用 Billing Wallet。
- 一个有效的 OpenAI-compatible Endpoint、模型名和 API Key。
- 当前用户可管理 Provider、Model Pool、Router 和 Gateway Key。

## 资金与请求路径

```mermaid
flowchart LR
  C["客户端 + Router-scoped Key"] --> R["Router 选择 Model Pool"]
  R --> P["Model Pool 选择 Source"]
  P --> U["Provider Runtime / 上游模型"]
  U --> O["Gateway Log、Metrics、Audit"]
  O --> B["Billing Usage：消费者支出/发布者收益"]
```

创建和健康检查不产生模型调用费。只有实际 Gateway 请求成功进入计量路径后，才应出现 Usage；上游 Provider 仍可能按其账号规则计费。

## 1. 连接并验证 Provider

1. 打开 **Providers → Accounts → Add provider account**。
2. 选择 API Key 模式，填写 Endpoint、模型与凭据。
3. 打开创建出的 Runtime，执行 **Start** 和 **Health**。
4. 看到 Runtime active/healthy 后再继续。

Account 保存凭据，Runtime 表示可调用容量。Start 不会自动创建 Model Pool Source。

## 2. 建立 Model Pool

1. 打开 **Model Pool → Add model source**。
2. 选择刚才的健康 Runtime，填写模型、Endpoint、价格和可见性。
3. 新建或选择一个 Model capability，例如 `demo-chat`。
4. 保存并执行 Source Health Check。

Model Pool 先按自己的策略选 Source；Router 再在多个 Pool 之间选池。这是两层路由。

## 3. 创建和部署 Router

1. 打开 **Routers → Create router**，命名为 `demo_router`。
2. 在 **Configure router → Model Pools** 绑定 `demo-chat`。
3. 首次教程选择 **Priority** 内置策略并 Apply。
4. 上传版本并 **Deploy**，确认 Router 状态为 `deployed`。

自定义 `router.py` 需要单独上传和部署。首次链路不要同时引入自定义沙箱问题。

## 4. 导出并调用

点击 **Export access**，立即保存一次性 Router-scoped Key，并使用面板生成的 Base URL、模型和 Router ID。最小 OpenAI-compatible 请求形如：

```bash
curl "$NEXUS_BASE_URL/api/v1/openai/v1/chat/completions" \
  -H "Authorization: Bearer $NEXUS_ROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"demo-chat","messages":[{"role":"user","content":"Reply with: nexus ready"}]}'
```

以 Export access 生成的 curl 为准，因为它还会绑定 Router Policy。不要用通用远程操作 Key 代替 Gateway/Router Key。

## 状态变化

| 对象 | 成功状态 | 卡住时查看 |
| --- | --- | --- |
| Provider Runtime | active、healthy | Runtime error、Provider Endpoint |
| Model Source | enabled、healthy | Account、Runtime、Health Check |
| Router | deployed | Version、Deployment、Job |
| Gateway Request | succeeded | Gateway Log、fallback/error code |
| Billing Usage | spending/earnings 记录 | Wallet、价格、请求是否成功计量 |

## 权限边界

- Provider Secret 只属于 Account，不会出现在 Marketplace、Router 沙箱或列表响应。
- Export access 创建限制到该 Router 的 Gateway Key；明文只展示一次。
- Resource Share 的只读权限不允许部署 Router 或导出凭据。
- Marketplace Provider Preference 影响候选顺序，不保证固定流量比例。

## 验证

1. curl 返回模型响应，而不是只返回 202/Job ID。
2. **Observability → Metrics/Jobs/Audit** 能按时间和 Request ID 找到调用。
3. Gateway 记录显示目标 Router、Pool、Source、延迟和成功状态。
4. 若配置收费，**Billing → Usage → Provider Pool → Spending/Earnings** 出现对应记录。

## 排错

- **Export access 不可用**：Router 尚未 deployed。
- **`MODEL_NOT_FOUND`**：模型名与 Model capability 不一致，或池内没有健康 Source。
- **Provider 401/403**：检查 Account Key 与 Endpoint，不要轮换 Router Key 来修复上游认证。
- **`BALANCE_NOT_ENOUGH`**：充值 Workspace Wallet 后用同一最小请求重试。
- **成功但无 Usage**：确认请求走的是受计量 Gateway 路径，价格和 Workspace 上下文正确。

## 当前限制与下一步

当前提供 OpenAI Chat Completions、Responses 和 Claude Messages 兼容入口；不能据此推断支持所有上游字段。凭据更新、可用额度和健康状态仍需按 Provider 配置核查。需要复杂选择逻辑时再阅读 [Routers](../routers/index.md) 的自定义运行时；完整字段以 [Swagger](../reference/api.md) 为准。
