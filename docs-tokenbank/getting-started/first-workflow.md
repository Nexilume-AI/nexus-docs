---
sidebar_position: 2
title: 完成第一个授信工作流
description: 用一个 10,000 USD 示例，在 Credit Desk 完成申请、审批和证据验证。
---

# 完成第一个授信工作流

你将提交一笔 10,000 USD 的企业 API 消费授信申请。完成后，你会看到第一条可操作记录，并理解 TokenBank 的基本模式：选择 Workflow 和 Queue，执行 Action，再用业务状态、账本与 Audit 验证结果。

## 需要准备

- 已登录 Nexus，并选择正确 Workspace/Tenant。
- Account Profile 中有公司名称等基础资料。
- 申请人有 Credit Read/Create 权限。
- 若要完成审批，使用另一个具有 Approve 权限的账户；记录返回 `can_approve=false` 时，申请人不能自行审批，需由另一位有权限的成员处理。

## 第 1 步：看到 Applications Queue

从 Nexus 左侧 **Govern → TokenBank** 打开独立窗口，进入 `/tokenbank/credit`。选择 **Credit approval → Applications**。

你应立即看到历史申请或 Empty State。到这里已经验证登录、Tenant Header 和 Credit 基础读取权限。

## 第 2 步：提交 10,000 USD 申请

点击 **Apply for credit**，填写：

| 字段 | 示例值 |
| --- | --- |
| Requested credit amount | `10000` |
| Payment terms days | `30` |
| Currency | `USD` |
| Purpose | `Production API usage working capital` |

在确认摘要中再次核对金额、币种、账期和当前 Tenant，然后提交。成功后 Applications 中会出现新记录，状态应为 `submitted`。

如果记录没有出现，先等待工作台最多 30 秒的自动刷新，或手动刷新；不要重复创建第二份申请。

## 第 3 步：由审批人决定

审批人打开同一 Tenant 的 Credit Desk，选择该 `submitted` 记录并点击 **Approve application**。示例批准额度仍为 `10000`，账期为 `30` 天。

批准会创建或更新 `credit` 类型账户与额度分配。它不会向 Billing Wallet 充值，也不是利息贷款。它只是允许合格 API 用量在余额不足时占用未用信用。

若不批准，使用 **Decline application** 并填写原因。Decline 不应产生授信额度或资金移动。

## 第 4 步：验证四类证据

| 证据 | 预期结果 |
| --- | --- |
| Applications | 状态为 `approved`，显示批准额度与账期 |
| Credit Overview | `credit_limit` 增加；`credit_used` 初始仍为 0 |
| Audit Trail | 有创建/提交/审批动作、操作者和时间 |
| 后续 Usage | 合格 API 消费同步后才增加 `credit_used` 并产生 Receivable |

审批本身设置额度，不代表已经消费，因此此时没有使用类 Ledger Transaction 是正常的。消费同步后再检查 Usage、Receivable、Ledger 和 Audit 是否引用同一业务链。

## 常见失败

- **看不到 Credit Desk**：缺少 `tokenbank.credit.view` 或 Tenant 成员资格。
- **有 Queue 但没有 Apply**：缺少 Create Capability。
- **申请人能看自己的记录但看不到其他申请**：这是 View Own 权限的预期结果。
- **Approve 不可用**：记录不是 `submitted`，或当前用户没有独立审批权限。
- **出现 `TOKENBANK_POLICY_BLOCKED`**：检查 Enterprise Credit Product Policy 与 Approval 要求。
- **提交超时**：用业务记录和 Audit 查询是否创建成功，不要立刻创建新申请。

## 你已经学会什么

你已经完成了 TokenBank 的最小闭环：**Desk → Workflow → Queue → Record → Action → Evidence**。接下来阅读[Console 导览](console-tour.md)、[Credit Desk 深入指南](../desks/credit.md)和[账本与控制模型](../concepts/ledger-and-controls.md)。
