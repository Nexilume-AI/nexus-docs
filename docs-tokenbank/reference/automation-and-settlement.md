---
sidebar_position: 4
title: 自动化与外部结算参考
description: Scheduled Task、Run、Checkpoint、Operational Alert 和 External Settlement 的运行与边界。
---

# 自动化与外部结算参考

TokenBank 把周期任务定义、每次运行、进度和告警分开。这样管理员可以区分“任务应该运行”“任务已经触发”“处理到哪里”和“是否需要人工介入”。

## 四个运营对象

| 对象 | 回答的问题 |
| --- | --- |
| Scheduled Task Definition | 任务做什么、多久运行、默认是否启用、Owner Role 是谁 |
| Task Run | 某次运行何时开始/结束、成功或失败、处理多少记录 |
| Checkpoint | 增量处理进度在哪里，是否长时间不前进 |
| Operational Alert | 哪个失败、Stale、Shortfall 或外部异常需要处理 |

## 任务分类

当前任务覆盖：

- Credit Usage Sync、Invoice Payment Sync、Overdue 和 Bad Debt 候选；
- Prepaid Expiry、Lending Overdue/Risk、Funding Maturity Payout；
- Risk Scoring、Concentration、Stress 与 Market Abuse；
- Derivative Valuation、Pricing、Margin、Surveillance 与 Report；
- Agent/Provider Revenue Settlement；
- Agent/Provider Market Match、Settle、Snapshot 与 Surveillance；
- SLA Monitoring、Impact 与 Auto-claim；
- External Reconciliation、Provider Statement、ERP Watchdog 与 Billing Alert。

每个 Definition 还标记 `mutates_ledger` 和 `external_side_effects`。Run-now 前必须阅读这两个字段；“Sync”不保证只读。

## 手动 Run-now

`POST /api/v1/tokenbank/scheduled-tasks/run-now/` 接收 `task_key`。Console 的 Sync/Run Automation 会调用同一入口。

1. 检查最近 Run 是否仍在执行。
2. 记录当前 Checkpoint。
3. 确认依赖已修复。
4. 运行一次并保存 Request/Run ID。
5. 对比 Result、Checkpoint、Ledger 和 Alert。

调度器使用任务级 Lock 防止同一 Task 并发运行。不要通过多个浏览器重复 Run-now 绕过等待。

## External Settlement

External Settlement 包含：

- Settlement Account：内部 Settlement Account 到外部 Channel 的映射；
- Payment Intent/Event：应收收款意图与标准化确认事件；
- Payout Request：Provider Payable 的外部付款请求；
- Invoice Profile / Tax Rule：元数据；
- Reconciliation Run/Item：比较 Paid Intent/Payout 与 Settlement Event。

`matched` 表示控制面记录有对应 Event；`requires_review` 表示存在 Paid 但无 Event 等差异。当前测试不调用真实银行或支付网络，Tax/Invoice 数据也不会自动生成合法税票。

## 告警处理

1. Acknowledge Alert 并指定处理人。
2. 查看关联 Task/Record 与最近成功 Checkpoint。
3. 修复 Worker、数据、资金或 Adapter 根因。
4. Run-now 验证一次。
5. 只有在指标恢复后 Resolve。

## 安全边界

External Payout Complete、Manual Payment Confirm、Tax Rule Update 和 Ledger 调整属于高风险动作，应使用独立角色、原因记录和双人复核。不要把外部 Provider Secret 放进 Metadata 或 Alert。

日常流程见[运营与风险操作](../guides/admin-operations.md)，任务失败见[常见故障排查](../troubleshooting/common.md)。

## 业务 Case 与计划任务不同

SLA Case 跟踪 `provider_monitoring → impact_calculation → claim_review → compensation_settlement → closed` 阶段。Case 连接 Incident 和业务进度，Workflow Task 指向本阶段需要处理的资源；它不是 Celery Task Run，也不是通用任务领取系统。

当前 `workflow-cases/` 和 `workflow-tasks/` 提供列表 GET。审核和结算仍调用 Claim 的产品 Action，成功后由服务推进待办；不能通过直接把 Task 标为 done 来代替结算。

周期调度通过 Celery 任务包装器和 Beat 运行。当前 Run-now API 在请求中调用注册 runner，返回运行结果；不要一律把 HTTP 201 解释为“已入队，尚未执行”。超时后先查询 Run、Checkpoint 和业务记录，再决定是否重试。另有 `financial_balance_reconciliation` 任务用于内部余额对账，不能代替外部支付对账。
