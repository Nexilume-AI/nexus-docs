---
title: Billing
description: Manage the platform wallet, plans, Marketplace usage, payment orders, and invoices.
---

# Billing

Billing is the Nexus platform metering and payment area: fund a Workspace Wallet, buy plans, inspect spending and earnings, and track orders and invoices. TokenBank is separate; it covers credit, liquidity, financial products, settlement, and risk workflows.

## Billing tabs

| Tab | Content |
| --- | --- |
| Overview | Wallet balance, capability summary, latest Payment and Invoice |
| Plans | Models, Agents, and Dataset plans |
| Usage | Provider Pool, public Agents, and public Data Assets as Spending or Earnings |
| Transactions | Billing Orders, Payment Orders, and Invoices |

Billing belongs to the selected Workspace/Tenant. Changing Workspace changes Wallet and all Billing records. Projects attribute resources and usage but do not create separate wallets.

## Fund the Wallet

Open **Billing → Overview → Recharge**, enter an amount, select an available Stripe, Alipay, or WeChat Pay provider, then complete its redirect or QR action. Creating the Payment Order does not credit the Wallet. Balance changes only after a signed webhook passes signature, amount, currency, and duplicate-event checks.

## Buy a plan

Filter **Plans** by Models, Agents, or Dataset, review price and capabilities, and click Buy. A successful purchase creates a paid Billing Order, deduct Ledger Entry, and Invoice. Insufficient balance returns `BALANCE_NOT_ENOUGH`, records a failed Order, and does not change the Wallet.

:::info Current plan boundary
Plans and quotas can be purchased and displayed, but general quota enforcement, plan cancellation, and automatic renewal are not implemented. A displayed allowance does not mean every resource module blocks overage today.
:::

## Review spending and earnings

Usage covers Provider Pool, public Agents, and public Data Assets. Switch to **Spending** for consumer charges or **Earnings** for publisher revenue. Empty results mean no matching usage, not a Wallet or runtime failure.

## Transaction records

| Record | Meaning |
| --- | --- |
| Billing Order | Business record for recharge or plan purchase |
| Payment Order | Third-party checkout, QR, or redirect state |
| Invoice | Record issued after a Wallet-backed plan purchase |

The latest cards are shortcuts; full history lives in Transactions. Invoices are records only: there is no tax calculation or PDF generation.

## Billing versus TokenBank

| Billing | TokenBank |
| --- | --- |
| Platform Wallet and ledger | Token accounts and internal ledgers |
| Recharge, checkout, plan purchase | Credit, lending, liquidity, and financial products |
| Marketplace spending and earnings | Clearing, settlement, risk approvals, and rights markets |
| Payment Orders and Invoices | Credit, Liquidity, and Settlement desks |

Start in Billing for normal platform charges. Use the [TokenBank guide](/tokenbank/) for credit, funding, settlement, or financial contracts. Both share Nexus identity and Workspace context, but have different ledgers and operator roles.

## Security and limits

- Billing requires a valid identity and `X-Nexus-Tenant`; writes require Billing permission.
- Payment webhooks do not use a user session but must verify provider signatures.
- Provider secrets, webhook secrets, merchant keys, and certificates never belong in API responses.
- Refunds, tax calculation, invoice PDFs, plan cancellation, recurring renewal, and general quota enforcement are not implemented.

See [Configuration](../reference/configuration.md) for payment settings and [Providers](../providers/index.md) for Provider Pool commerce.
