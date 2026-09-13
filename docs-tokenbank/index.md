---
slug: /
sidebar_position: 1
title: TokenBank 用户指南
description: 从入门到运营，理解并使用 TokenBank 的授信、资金池、结构化产品、融资、内部权利市场与 SLA 工作台。
---

# TokenBank 用户指南

TokenBank 是 Nexus 内部的金融控制与结算层。它把 Billing Wallet、TokenBank Account、双分录账本、审批、产品策略、风险检查、自动任务和审计连接起来，让 AI 服务的资金与权利变化能够被解释、核对和追踪。

它不是银行，也不是公共交易所、保险公司或外部现金清算系统。页面中的“投资”“市场”“衍生品”和“补偿”描述的是 Nexus 内部受控的服务资金或权利流程，不代表存款、证券、保险或法币支付能力。

## 第一次使用

如果你第一次打开 TokenBank，按这个顺序阅读：

1. [Console 导览](getting-started/console-tour.md)：先认识 Desk、Workflow、Queue、Record、Action 和 Detail Panel。
2. [第一个授信工作流](getting-started/first-workflow.md)：用一个 10,000 USD 授信示例完成申请、审批和验证。
3. [账本与控制模型](concepts/ledger-and-controls.md)：理解 Wallet、Account、Balance、Locked、Credit 和双分录。
4. [资金与权利如何流动](concepts/money-and-rights-flow.md)：区分余额移动、资金锁定、内部权利转移和外部结算记录。
5. [选择正确的金融流程](guides/financial-flows.md)：根据业务目标进入正确 Desk。

## 八个工作台

| 工作台 | 解决的问题 | 主要读者 |
| --- | --- | --- |
| [Credit](desks/credit.md) | 先使用 API、后按账期付款 | 申请人、授信审批人、催收与坏账管理员 |
| [Funding](desks/funding.md) | 把 Billing 余额投入共享池并支持受控借款 | 出资人、借款人、资金池运营者 |
| [Derivatives](desks/derivatives.md) | 用 Forward 管理未来 Provider API 价格风险 | 产品管理员、交易操作员、风险与结算人员 |
| [Agent Finance](desks/agent-finance.md) | 为 Agent 提供一次性资金并分配真实使用收入 | Agent 发布者、资金提供者、结算人员 |
| [Agent Market](desks/agent-market.md) | 转让已确认的 Agent 服务/收入权利单位 | 卖方、买方、撮合与结算人员 |
| [Provider Finance](desks/provider-finance.md) | 为 Provider Runtime 提供资金并处理收入与 Payable | Provider、资金提供者、财务运营者 |
| [Provider Market](desks/provider-market.md) | 转让 Provider Finance 形成的内部服务权利 | 卖方、买方、撮合与结算人员 |
| [SLA](desks/sla.md) | Provider 预存准备金，客户购买保障并申请服务补偿 | Provider、客户、风控与 Claim 审核人 |

## 按角色阅读

| 角色 | 建议入口 |
| --- | --- |
| 新用户 | [Console 导览](getting-started/console-tour.md)、[第一个授信工作流](getting-started/first-workflow.md) |
| 业务操作员 | [如何使用工作台](guides/use-desks.md)、对应的 [Desk 指南](desks/credit.md) |
| 财务与风控管理员 | [运营与风险操作](guides/admin-operations.md)、[自动化与外部结算](reference/automation-and-settlement.md) |
| 权限管理员/API 开发者 | [权限与 API](reference/permissions-and-api.md)、[状态与错误码](reference/statuses-and-errors.md) |

## 五条操作原则

1. 先确认 Workspace/Tenant、角色、Workflow 和 Queue，再执行动作。
2. Preview、Refresh 和 Sync 不一定移动资金；Contribute、Fund、Settle、Complete Transfer 通常会产生账本或权利变化。
3. 网络超时后先查询业务记录和 Audit，再用同一个幂等键重试。幂等键就是“同一个业务动作的唯一编号”。
4. Billing Wallet 是充值与多数用户资金动作的入口；TokenBank Account 用于解释业务归属、锁定、信用、准备金与结算。
5. 涉及资金的成功操作应同时留下业务状态、Ledger Transaction 和 Audit 证据。

不知道错误属于权限、策略、状态还是资金条件时，从[常见故障排查](troubleshooting/common.md)开始。

## 使用当前企业版入口

从 Console 的 **Govern → TokenBank** 打开独立工作台，使用当前 Organization/Tenant 身份。TokenBank 不包含在 Cloud 社区版中。八个 Desk 的路由保持不变；Funding 使用 `/tokenbank/prepaid`，`/tokenbank/lending` 是兼容别名。

当前操作需要同时检查目录范围、记录版本和独立审批条件。先阅读 [Console 导览](getting-started/console-tour.md)，API 调用者再阅读 [权限与 API](reference/permissions-and-api.md)。
