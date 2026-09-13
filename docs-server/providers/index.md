---
title: Providers
description: 连接模型服务账号、运行 Provider Runtime，并发布或路由模型容量。
---

# Providers

Providers 把上游模型账号变成 Nexus 可以运行、路由和计费的模型容量。页面使用“Connect → Operate → Publish”流程，但背后有多个独立对象；理解它们可以避免误删凭据或误以为发布 Runtime 就已经进入 Model Pool。

## 对象关系

```mermaid
flowchart LR
  A["Provider Account\n凭据与上游 Endpoint"] --> R["Provider Runtime\n可启动、停止、健康检查"]
  R --> D["Model Pool Source\n显式添加的模型源"]
  D --> P["Community Provider Listing\n可选发布"]
  P --> T["Router Preference\n可选候选顺序"]
```

| 对象 | 保存什么 | 删除影响 |
| --- | --- | --- |
| Provider Account | Provider、账号标识、Endpoint、认证方式、价格 | 依赖 Runtime 可能停止工作 |
| Provider Runtime | Runtime 类型、模型、运行状态和健康 | 不再服务流量；已发布时应先 Unpublish |
| Model Pool Source | Model Group 中的 Provider-backed Source | 从 Pool 移除路由来源，不删除 Provider Account |
| Community Listing | 对外价格、配额、信任和商业信息 | 不再被 Marketplace/Router 发现 |

## 1. Connect：添加 Provider Account

打开 **Providers → Accounts → Add provider account**：

- API Key 模式用于 OpenAI-compatible Endpoint。
- Interactive login 用于需要 Codex Proxy 或 CLIProxyAPI 登录的 Provider。
- Username/password login 会选择 CLIProxyAPI Runtime。

API Key、用户名和密码在 Server 端加密，任何列表和详情响应都不会返回明文或加密字段。创建 Account 会为当前 Console 流程创建第一个 Runtime，但不会自动创建 Model Pool Source。

## 2. Operate：管理 Provider Runtime

在 **Runtimes** 中可以创建、编辑、启动、停止、健康检查和导出访问配置：

| Runtime 类型 | 典型用途 |
| --- | --- |
| Direct API | 直接调用 OpenAI-compatible Provider Endpoint |
| Codex Proxy | 基于交互式账号登录的代理 Runtime |
| CLIProxyAPI | CLI 登录或用户名密码登录的兼容 Runtime |

Start/Login 只让 Runtime 可用，不会自动把它加入 Model Pool。需要路由模型流量时，转到 **Model Pool → Add source**，显式选择 Runtime 和 Model Group。

导出的 `.env` 与 curl 片段可能包含短期或敏感访问材料，只应保存到本地 Secret 管理系统。Computer 工具配置也会通过同一 Credentials Export 流程生成配置，不单独保存 Provider Secret。

## 3. Publish：共享模型容量

Provider Runtime 先成为 Model Pool Source，才能发布到 Community Provider Pool。发布时填写价格、货币、容量、服务区域、能力、SLA、数据保留和合规说明。

Marketplace 只公开运营证据和商业条款，不公开 Provider Credential 与内部 Endpoint。消费者可按 Official、Verified、Health、Quota、成功率、P95 延迟和价格筛选。

## 加入 Router

从 Provider Marketplace 详情点击 **Use in router**：

1. 选择目标 Router。
2. 选择 Preferred、Standard 或 Fallback Priority。
3. 确认价格、健康、Quota 与运营证据。
4. 添加 Preference。

Preference 只改变候选顺序，不保证固定流量比例。实际选择仍由 Router 策略、健康、Quota、价格和其他来源共同决定。

## 健康、信任与计费

- Runtime Health 表示当前可调用性。
- Community Listing 还记录 30 天调用、成功率、延迟、Quota 状态、Trust score/tier 和 Moderation 状态。
- Provider Pool 调用从消费方 Billing Wallet 扣费，并为发布方记录 Earnings。
- 在 [Billing](../billing/index.md) 的 Usage 中切换 Provider Pool 和 Spending/Earnings 查看记录。

## 当前限制

- 不提供 Provider Credential Rotation 工作流；轮换时需要更新 Account。
- 已提供 Claude Messages 兼容入口；实际支持字段以当前模型能力与接口校验为准。
- 不托管、转换 Provider 原生多模态媒体文件。
- 候选选择会考虑可用额度；不要将其等同于所有上游套餐的统一额度承诺。
- 公共 Model Catalog 仍依赖 Workspace/Tenant 上下文。

## 排错顺序

1. 确认 Workspace、Project 和 Provider Account 状态。
2. 对 Runtime 执行 Health Check，检查错误原因。
3. 确认 Runtime 已启动，并且 Model Pool Source 是显式创建的。
4. 发布失败时检查 Source、价格、健康及 Marketplace 要求。
5. Router 未选中该 Provider 时，检查 Preference、策略、健康、Quota 和价格，而不是只看 Priority。

模型调用认证见 [API 约定](../reference/api.md)，Computer 配置见 [Computer Environment](../environments/computer.md)。

## 连接导入与兼容 API

Provider Connections 提供批量导入流程：先获取模板/能力，再 Preview 检查行错误，最后 Commit。预览不等于创建完成；提交后逐条检查连接、登录状态、模型刷新和 Runtime 健康。失败连接使用 Repair 或重新配置，不要反复提交整批来代替调查。导入文件可能含凭据，不能放入公开仓库或截图。

模型访问除原有 Gateway API 外，还提供 `/api/v1/openai/v1/chat/completions`、`/api/v1/openai/v1/responses`、`/api/v1/claude/v1/messages` 以及模型列表入口。图像生成、编辑、变体入口位于 `/api/v1/openai/v1/images/`，实际可用性取决于模型能力与 Provider 配置。兼容入口不代表完整复刻上游所有功能。
