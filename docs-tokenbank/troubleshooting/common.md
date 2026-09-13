---
sidebar_position: 1
title: 常见故障排查
description: 按现象、证据和修复步骤排查 TokenBank 权限、策略、状态、资金、结算和自动任务问题。
---

# 常见故障排查

排错前记录 Tenant、Desk、Workflow、Queue、Record ID、Request ID、时间和脱敏错误码。不要附带 Token、Cookie、支付 Secret 或完整金融请求正文。

## 看不到 Desk、Queue 或 Record

**可能原因：**登录失效、Tenant 错误、缺少基础 Read、只有 View Own、Resource Grant 限制，或 Queue 当前没有符合状态的记录。

**证据：**检查 Current Tenant Header、Workbench `capabilities`、自己的 Role，以及同一 Record 是否能通过产品 API 查询。

**修复：**切回正确 Tenant；由管理员分配最小 View Capability；不要用 Owner 权限掩盖角色配置错误。

退役路径 `accounts-ledger`、`risk`、`settlement` 等会重定向到 Credit，这是预期行为。

## Action 不可用

**可能原因：**缺少写 Capability、Record 状态不允许、Queue/Workflow 不匹配、Quote 过期、记录已被另一操作员处理。

**证据：**查看 Detail 状态、Action 的 Unavailable Reason、最新 Audit 和刷新后的 Queue。

**修复：**不要修改浏览器状态。使用正确角色和状态流转；并发处理时以 Server 最新状态为准。

## `TOKENBANK_POLICY_BLOCKED`

**可能原因：**Product Policy 为 `disabled`；为 `approval_required` 但没有有效 Approval；目标 Account/Product 未激活。

**证据：**查询当前 Tenant 的 Product Policy、Approval 状态/资源、Account 与 Product Status。

**修复：**由有权人员调整 Policy 或完成审批。不要通过基础 Ledger Transfer 绕过产品工作流。

## 余额足够但提示资金不足

**可能原因：**余额已锁定、Unit/币种不同、用了错误 Wallet/Account、不允许使用 Credit、Margin/Reserve 属于另一合同，或结算预览出现 Shortfall。

**证据：**比较 `balance`、`locked_balance`、`credit_limit`、`credit_used`、Unit、Source ID 和 Preview。

**修复：**充值正确 Billing Wallet、释放无效 Lock、补充对应 Margin/Reserve，或改用正确账户。不要手工改余额。

## 超时后不知道是否成功

**可能原因：**Server 已过账但响应丢失，或 Task 仍在运行。

**证据：**按原幂等键、业务 Reference、Record ID 查询 Transaction、Audit 与 Task Run。

**修复：**确认未成功前不要生成新 Key。需要重试时复用原 Key，让 Server 返回已有结果。

## 结算或权利转移被阻止

**可能原因：**Contract/Trade 状态错误、未完成 Match、Dispute/Freeze、最新估值缺失、Margin/Reserve Shortfall、Product Policy 或 Approval 不满足。

**证据：**先运行可用的 Preview/Risk Refresh，查看 Trade/Contract Detail、Lock、Margin Call、Registry 与 Audit。

**修复：**按业务原因补资金、解决争议、更新估值或完成前序状态；不要跳过 Match/Review 直接调用 Settle。

## 自动任务停滞

**可能原因：**Task Disabled、Celery Worker/Beat 不运行、分布式 Lock 未释放、Checkpoint Stale、依赖数据或 External Adapter 失败。

**证据：**查看 Definition、最近 Run、Checkpoint、Operational Alert 和 Worker Log。

**修复：**修复依赖后 Run-now 一次，核对处理数量与 Checkpoint，再恢复长期调度。详见[自动化与外部结算](../reference/automation-and-settlement.md)。

## 页面显示成功但数据未变化

Workbench 默认每 30 秒刷新。先手动刷新，再检查 Network Response、Audit 和实际 API。Toast 不是财务最终证据；涉及资金时必须能找到 Ledger Transaction。

## 当前目录与并发问题

- **搜索结果不完整**：检查 Queue、scope、status、分页游标和 snapshot；改变筛选后从第一页查询，区分 loaded_count 与 total_count。
- **按钮可见但禁用**：读取控制原因，检查选中记录、Capability 与独立审批条件；不要用管理员账号绕过业务状态。
- **409 版本冲突**：`MARKET_QUOTE_STALE` 需要重新预览订单；`TOKENBANK_RECORD_STALE` 需要重新加载记录并确认。保留请求结果与幂等键用于核对。
- **SLA Case 无操作按钮**：切换 Workflow tasks，选择指向 Claim 的审核或结算待办。
- **Funding 还款失败**：检查 Borrower Billing Wallet 的可用 USD 余额；上传外部证明不会自动完成钱包扣款。
