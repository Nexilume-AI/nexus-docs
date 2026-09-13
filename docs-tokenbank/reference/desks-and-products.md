---
sidebar_position: 1
title: 工作台与产品参考
description: TokenBank 八个有效 Desk、Queue、Action、详情区域和当前产品策略参考。
---

# 工作台与产品参考

本页描述当前 Console 实际暴露的 8 个 Desk。`foundation`、`accounts-ledger`、`risk`、`settlement`、`finance`、`operations`、`policies`、`audit` 和 `market-surveillance` 是退役路径，访问时会重定向到 Credit，不是独立工作台。

## Desk 目录

| Path | Queues | Console Actions |
| --- | --- | --- |
| `/tokenbank/credit` | applications、usage_billing、overdue_cases、bad_debt_candidates | Apply、Approve/Decline、Sync、Write off、Overdue automation |
| `/tokenbank/prepaid` | fund_account、lending、returns | Contribute、Apply/Approve/Reject Loan、Submit repayment |
| `/tokenbank/derivatives` | products、price_indexes、rfqs、quotes、active_contracts、risk_alerts、settlements | Create Index/Forward、RFQ/Quote、Accept/Cancel、Risk、Margin、Preview/Settle |
| `/tokenbank/agent-finance` | agent_revenue_policies、agent_sponsorships、agent_pending_revenue、agent_settlement_batches | Create Plan、Invest、Confirm、Settle selected/all |
| `/tokenbank/agent-market` | agent_market_assets、agent_market_listings、agent_orders、agent_trades | Open sale、Buy、Cancel、Match、Complete transfer |
| `/tokenbank/provider-finance` | provider_plan_worklist、provider_investment_worklist、provider_revenue_closeout | Create Plan/Investment、Confirm、Approve payout exception |
| `/tokenbank/provider-market` | provider_market_assets、provider_market_listings、provider_orders、provider_trades | Open sale、Buy、Cancel、Match、Complete transfer |
| `/tokenbank/sla` | plans、subscriptions、provider_plans、reserves、workflow_tasks、workflow_cases | Publish/Buy/Top up、Review claim、Settle claim |

## 当前默认产品策略

以下值来自当前 `DEFAULT_PRODUCT_POLICIES` 与测试；Tenant/Jurisdiction Policy 可以覆盖：

| Product Type | Default Mode |
| --- | --- |
| `core`、`prepaid_token`、`api_derivative` | `open` |
| `agent_secondary_market`、`api_provider_market` | `open` |
| `enterprise_credit`、`token_lending`、`price_lock` | `approval_required` |
| `sla_protection`、`agent_financing`、`api_provider_financing` | `approval_required` |

不要根据旧 Phase 文档推断默认值；运行时应查询 Product Policy。`open` 也不跳过 Permission、状态、余额、风险、锁定和争议检查。

## 共同返回结构

Workbench 聚合响应包含：

- `metrics`：当前用户可见的业务汇总；
- `queues`：按 Tenant、角色、资源和状态过滤的记录；
- `recent`：近期活动与运营记录；
- `capabilities`：页面判断 Queue 授权和 Action 可用性的能力树。

Console 每 30 秒自动刷新一次。Queue 为空可能表示没有记录，也可能表示当前角色只能 View Own 或完全没有该 Flow 的 View Capability。

## 共同状态规则

- List/Create 通常使用集合 GET/POST；状态推进使用资源级 POST Action。
- Action 同时受 Capability、允许的 Workflow/Queue、是否选择 Record 和 Record 当前状态约束。
- 资金不足、Product Policy、Approval、Risk Limit、Locked Balance、Expired Quote、Freeze 和 Dispute 都可能阻止写操作。
- `Live` 表示 Console/Server 流程已实现，不代表外部银行、税务、保险或监管连接已经存在。

逐个工作台的流程见 [Credit](../desks/credit.md)、[Funding](../desks/funding.md)、[Derivatives](../desks/derivatives.md)、[Agent Finance](../desks/agent-finance.md)、[Agent Market](../desks/agent-market.md)、[Provider Finance](../desks/provider-finance.md)、[Provider Market](../desks/provider-market.md) 和 [SLA](../desks/sla.md)。

## 目录范围与动作可用性

Workbench 还返回 `queue_scopes`、`actor_context`，以及相应业务的市场范围或平台监督信息。restricted Queue 不应被解释为“全平台无数据”。`capabilities` 控制授权；相关动作可以保持可见并禁用，以解释权限、Maker-checker 或状态限制。

大目录通过 `admin/catalog/{workbench}/{queue}/` 分页查询；Workbench 内联数组不是完整导出。Funding 的 `/tokenbank/lending` 兼容别名映射到 `prepaid`。
