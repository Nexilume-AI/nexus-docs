---
title: Marketplace
description: 发现、评估和获取公开 Agent、Data Asset 与 Provider Capacity。
---

# Marketplace

Marketplace 是 Nexus 的公开发现面，覆盖三类受治理产品。未登录用户可以浏览公开信息；调用、Pull、加入 Router 或产生消费记录前必须登录并选择 Workspace/Project。

| 产品 | 获取后的结果 | 主要风险检查 |
| --- | --- | --- |
| Agent | 调用或部署受治理 Agent Runtime | Runtime 类型、权限、版本、价格、健康 |
| Data Asset | 获得不可变 Release 的文件 Manifest | 来源、Redaction/Consent/License/Scan、大小与价格 |
| Provider | 把 Community Capacity 加入 Router Preference | 健康、Quota、成功率、P95、价格、SLA 与数据条款 |

## 消费者流程

1. 选择 **Marketplace → Agents / Data Assets / Providers**。
2. 使用搜索、分类、价格、健康或其他产品筛选器缩小范围。
3. 打开详情，确认 Publisher、版本、运营证据、商业条款和 Workspace 适用性。
4. 登录并执行产品动作：调用 Agent、Pull Release，或 **Use in router**。
5. 在 [Billing](../billing/index.md) 的 Usage、Spending/Earnings、Orders 与 Invoices 中验证费用。

Marketplace 不公开 Provider Credential、内部 Endpoint 或资源所有者的 Secret。公开可见也不代表获得管理权限；消费动作仍受 Workspace、Project、Wallet、Key Policy 和资源授权约束。

## 发布者流程

- Agent：先完成 Runtime 部署、健康与发布配置，再从 [Agents](../agents/index.md) 发布。
- Data Asset：先创建通过门禁的不可变 Release，再将 Collection 设为 public；见 [Data Assets](../data-assets/index.md)。
- Provider：Runtime 必须先显式加入 [Model Pool](../model-pool/index.md) 成为 Source，之后才能发布 Community Listing；见 [Providers](../providers/index.md)。

每种产品的价格与权益来源不同。不要把 Marketplace Listing 当作底层资源副本：取消发布会停止新的发现或获取，但既有订单、Usage、Audit 和不可变交付记录仍按各模块规则保留。

## Provider 加入 Router

在 Provider 详情中点击 **Use in router**，选择目标 Router 和 Preference。若尚无 Router，可在流程中创建。Preference 只是候选偏好；最终选池由 [Router](../routers/index.md) 策略决定，选源再由 Model Pool 策略决定。

## 验证与排错

- **可以浏览但不能使用**：先登录，确认 Workspace/Project 已选择且 Wallet/权限满足要求。
- **产品未出现在 Marketplace**：检查资源是否 public、当前版本/Runtime 是否健康，以及发布门禁与 Moderation 状态。
- **Provider 已添加但无流量**：检查 Router Preference、绑定池、Provider Quota/Health 和两层路由策略。
- **费用与预期不同**：以购买时捕获的 Plan/价格和 Billing Usage 为准；计划后续变更不回写既有订单。

需要解释某次拒绝时，从 [Access Explain](../access/index.md) 和 [Observability Audit](../operations/observability.md) 同时核对身份与操作记录。
