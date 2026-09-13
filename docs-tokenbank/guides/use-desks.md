---
sidebar_position: 1
title: 如何使用 TokenBank 工作台
description: 用统一方法阅读 Desk、Workflow、Queue、Record、Action 和 Detail Panel。
---

# 如何使用 TokenBank 工作台

八个 Desk 的业务不同，但操作骨架相同。掌握这套骨架后，你不需要记住所有按钮，也能判断下一步为什么出现或为什么被阻止。

## 前置条件

- 已登录并选择正确 Workspace/Tenant。
- 拥有目标 Desk 的 Read 权限。
- 知道自己是申请人、资金提供者、审批人、风险人员还是结算人员。

## 操作步骤

1. **选择 Desk。** Desk 对应一类业务责任，例如 Credit 管授信，SLA 管 Provider 服务保障。
2. **选择 Workflow。** Workflow 是一个端到端阶段，例如 Credit Approval 或 Overdue Collections。
3. **选择 Queue。** Queue 是当前角色可见、等待阅读或处理的业务记录集合，不是任意数据库表。
4. **选择 Record。** 阅读 Summary、Risk、Financials、Settlement 和 Audit Trail，确认金额、状态、归属和前置条件。
5. **检查 Action。** 相关 Action 可以保持可见但禁用；查看 Capability、选中记录和状态限制说明。
6. **阅读确认摘要。** 明确动作是否移动资金、锁定余额、改变权利、触发后台任务或仅做 Preview。
7. **执行并验证。** 刷新 Queue，核对状态、Ledger Reference、Audit 和相关 Task Run。

## 判断动作是否移动资金

| 动词 | 通常行为 | 仍需确认什么 |
| --- | --- | --- |
| Preview / Refresh | 计算、估值或风险刷新，不移动资金 | 是否会创建 Margin Call/Alert |
| Sync / Run automation | 运行后台同步，可能间接创建账本或业务记录 | Task 是否标记 `mutates_ledger` |
| Apply / Submit | 创建申请或订单，部分流程会锁定资金 | 确认摘要是否写明 Lock/Premium |
| Contribute / Fund / Add margin | 从 Wallet 或 Account 移动资金 | Source、Destination、Amount、Unit |
| Approve | 可能只改状态，也可能同时 Disburse/Settle | 当前 Desk 的具体说明 |
| Settle / Complete transfer | 形成最终资金或权利变动 | 幂等键、短缺、争议和最新状态 |

## 为什么按钮不出现

按这个顺序检查：

1. Tenant 与资源是否匹配；
2. 是否有该 Queue 的 View Capability；
3. 是否有该 Action 的写 Capability；
4. Record 状态是否允许动作；
5. Product Policy 是否 Open 或已满足 Approval；
6. Wallet、Balance、Locked、Margin、Reserve 是否满足；
7. 是否存在 Freeze、Dispute、Expired Quote 或已处理的并发变更。

修改浏览器状态不能绕过 Server 检查。UI 显示 `Live` 只表示工作台已经实现，不代表每个 Tenant 都启用了所有写操作。

## 验证

成功写操作至少应留下业务状态和 Audit。涉及资金时还应有 Ledger Transaction；涉及权利时应有 Transfer/Registry；涉及自动化时应有 Task Run、Checkpoint 或 Alert。

## 排错

- **Toast 成功但 Queue 没变化**：等待 30 秒自动刷新或手动刷新，再用 Request ID 查 Observability。
- **403**：区分普通 Permission Denied 和 `TOKENBANK_POLICY_BLOCKED`。
- **400/409**：检查状态是否已被其他操作员推进，以及是否错误更换了幂等键。
- **连续失败三次**：停止点击，保存 Request ID、Record ID、Tenant、时间和脱敏错误码。

完整 Queue/Action 列表见[工作台与产品参考](../reference/desks-and-products.md)，状态含义见[状态与错误码](../reference/statuses-and-errors.md)。
