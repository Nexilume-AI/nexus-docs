---
sidebar_position: 3
title: 状态与错误码参考
description: 阅读 TokenBank 常见生命周期、状态转换、错误码和恢复动作。
---

# 状态与错误码参考

TokenBank 不使用一个全局状态枚举。Application、Contract、Order、Trade、Claim、Task 和 External Settlement 各有自己的生命周期。操作时以 Record Detail 和 OpenAPI Schema 为准。

## 常见生命周期词汇

| 状态 | 通常含义 | 下一步 |
| --- | --- | --- |
| `draft` | 尚未提交或发布 | 补齐字段后 Submit/Publish |
| `submitted` | 等待审批或报价 | Approve/Reject/Quote |
| `approved` | 已批准，但可能尚未 Disburse/Settle | 检查具体业务证据 |
| `pending` | 等待下一阶段或人工处理 | 查看 Workflow/Unavailable Reason |
| `active` | 合同、Plan、Account 或 Coverage 正在生效 | 监控 Usage/Risk/Expiry |
| `locked` / `funded` | 资金已预留或 Margin 已补充 | 等待 Match/Settle/Release |
| `pending_settlement` | 交易已形成，尚未最终交割 | 检查短缺、争议和结算权限 |
| `settled` / `completed` | 最终资金/权利动作已完成 | 核对 Ledger、Registry 与 Audit |
| `paid` | Receivable/Invoice 已支付 | 核对 External Event 与 Credit Used |
| `overdue` | 超过付款或履约日期 | Collection、Margin 或 Default 流程 |
| `defaulted` | 合同或债务进入违约 | Freeze、Recovery、Write-off/Closeout |
| `written_off` | 已核销 | 保留历史证据，不等于收到付款 |
| `rejected` / `cancelled` | 被拒或主动取消 | 检查是否释放 Lock/Reserve |
| `frozen` | 风险、争议或逾期阻止操作 | 解决原因后由授权角色恢复 |

## 产品策略状态

- `open`：产品门禁放行，其他检查仍然执行。
- `approval_required`：需要匹配的已批准 Approval。
- `disabled`：产品写操作被关闭。

Product Policy 与 Record Status 是两层状态。一个 Active Contract 仍可能因为 Product Disabled 而不能 Settle。

## HTTP 与错误码

| 错误 | 常见原因 | 恢复动作 |
| --- | --- | --- |
| 401 | Token/Cookie 失效 | 重新登录，避免复用过期 Bearer Token |
| 403 Permission Denied | 缺少 Permission/Capability | 分配最小角色或改用正确操作员 |
| 403 `TOKENBANK_POLICY_BLOCKED` | Policy、Approval 或 Account/Product Active 条件不满足 | 查询 Product Policy、Approval 和状态 |
| 404 `NOT_FOUND` | 不存在、其他 Tenant、View Own/Grant 不可见 | 核对 Tenant 与资源授权 |
| 400 `TOKENBANK_INSUFFICIENT_BALANCE` | Available Balance/Credit/Reserve 不足 | 检查 Locked、Unit、Source 和 Preview |
| 400 Validation Error | 字段、金额、状态、Quote、Margin、业务关系不合法 | 按字段错误和 Detail 修正 |
| 409 Conflict | 并发推进、重复动作或状态已变化 | 刷新 Record，查询幂等结果 |

## 状态变化后的证据

不要只看 Status Badge：

- `approved` Credit 应伴随 Credit Limit；
- `active` Derivative Contract 应有双方、Quote 与 Margin Context；
- `settled` Trade 应有 Ledger 和 Transfer Registry；
- `paid` Receivable 应有 Payment/Settlement Event；
- `completed` Task 应有 Result、Checkpoint 和处理数量。

## 排错顺序

先确认 Tenant 和权限，再确认 Product Policy，再确认 Record Status，最后检查资金与风险条件。完整步骤见[常见故障排查](../troubleshooting/common.md)。

## 并发冲突与业务待办状态

| HTTP / Code | 处理方法 |
| --- | --- |
| 409 `MARKET_QUOTE_STALE` | 挂牌价格、剩余数量或状态已变；重新预览并确认订单 |
| 409 `TOKENBANK_RECORD_STALE` | 记录已更新；重新读取详情，核对状态与操作者，再提交 |

Workflow Case 的 `lifecycle_status` 为 `open`、`waiting`、`resolved`、`cancelled`；Workflow Task 的 `task_status` 为 `open`、`done`、`cancelled`。它们与 Scheduled Task Run 的 `running`、`succeeded`、`failed`、`skipped` 是不同对象。

Agent Market Trade 的可结算状态是 `pending_settlement`；Provider Market Trade 使用 `pending`，完成后为 `settled`。不要把两个产品的状态枚举混用。
