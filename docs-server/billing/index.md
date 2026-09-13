---
title: Billing
description: 管理平台钱包、套餐、Marketplace 用量、支付订单和发票。
---

# Billing

Billing 是 Nexus 平台的商业计量与支付工作区：充值 Workspace Wallet、购买套餐、查看消费与收益、跟踪订单和发票。它与 TokenBank 相邻但不相同；TokenBank 处理授信、流动性、金融产品、结算和风险流程。

## Billing 页面

| Tab | 内容 |
| --- | --- |
| Overview | Wallet 余额、能力摘要、最近 Payment 和 Invoice |
| Plans | Models、Agents、Dataset 套餐及购买动作 |
| Usage | Provider Pool、公开 Agents、公开 Data Assets 的 Spending 与 Earnings |
| Transactions | Billing Orders、Payment Orders 和 Invoices |

Billing 数据属于当前 Workspace/Tenant。切换顶部 Workspace 会切换 Wallet、Plans、Usage 和 Transactions；Project 主要用于资源与用量归属，不创建独立 Wallet。

## 充值 Wallet

1. 打开 **Billing → Overview → Recharge**。
2. 输入金额并选择 Stripe、Alipay 或 WeChat Pay 等已配置 Provider。
3. 创建 Payment Order 后，打开 Redirect URL 或扫描 QR。
4. 支付成功后等待签名验证的 Provider Webhook。
5. 刷新 Overview，确认 Wallet 余额和 Payment 状态。

创建 Recharge Order 不会立即增加余额。只有金额、货币、签名和事件唯一性全部验证通过的 Webhook 才会写入 Wallet Ledger；重复回调不会重复入账。

## 购买套餐

在 **Plans** 中按 Models、Agents 或 Dataset 筛选：

1. 检查价格、货币和能力/Quota 描述。
2. 确认 Wallet 余额足够。
3. 点击 Buy。
4. 成功后生成 paid Billing Order、deduct Ledger Entry 和 Invoice。

余额不足会返回 `BALANCE_NOT_ENOUGH`，生成 failed Order，但不会扣款或创建 Ledger Entry。

:::info 当前套餐边界
当前 Billing 可以购买套餐并展示 Quota，但通用 Quota Enforcement、套餐取消和自动续费尚未实现。文档中的套餐额度不应被理解为所有模块都已强制阻断超额调用。
:::

## 查看消费与收益

Usage 支持三类 Marketplace 资源：

- Provider Pool；
- Public Agents；
- Public Data Assets。

每一类都可以切换：

- **Spending**：当前 Workspace 作为消费者产生的费用。
- **Earnings**：当前 Workspace 作为发布方获得的收益。

价格、Token、调用次数、数据量和资源字段随资源类型变化。空表只表示当前筛选条件下没有 Usage，不代表 Wallet 或 Runtime 故障。

## 理解三类交易记录

| 记录 | 含义 |
| --- | --- |
| Billing Order | 充值或套餐购买的业务订单 |
| Payment Order | 第三方支付渠道的 Checkout/QR/Redirect 状态 |
| Invoice | Wallet 套餐购买完成后生成的发票记录 |

Overview 中的 Latest payment 和 Latest invoice 是快捷摘要；完整历史在 Transactions。当前 Invoice 是记录，不提供税务计算或 PDF 发票生成。

## Billing 与 TokenBank 的边界

| Billing | TokenBank |
| --- | --- |
| 平台 Wallet 与 Ledger | Token 账户和内部账本 |
| 充值、Checkout、套餐购买 | 授信、借贷、资金池和金融产品 |
| Marketplace 消费与收益 | 清算、结算、风险审批与权益市场 |
| Payment Order 与 Invoice | Credit、Liquidity、Settlement Desk |

普通平台费用从 Billing 开始；涉及授信、资金调度或金融合约时进入 [TokenBank 用户指南](/tokenbank/)。两者共享 Nexus 用户、Workspace 和权限上下文，但产品账本与操作角色不同。

## 权限与安全

- 查看和写入 Billing API 都需要有效身份和 `X-Nexus-Tenant`。
- 充值和购买要求 Billing 权限；Workspace Owner/Admin 默认满足。
- Payment Webhook 不使用用户会话，但必须验证支付渠道签名。
- 支付密钥、Webhook Secret、商户私钥和证书永远不能出现在 API 响应或文档示例中。

## 当前限制

- 不支持 Tax Calculation 或 Invoice PDF。
- 不支持 Refund。
- 不支持 Plan Cancellation 和 Recurring Renewal。
- 不提供跨所有资源模块的统一 Quota Enforcement。

Payment 配置见[配置参考](../reference/configuration.md)，Provider Pool 的商业流程见 [Providers](../providers/index.md)。
