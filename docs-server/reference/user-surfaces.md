---
sidebar_position: 3
title: 用户功能地图
---

# 用户功能地图

这张地图用于快速定位页面。每个当前 Console 核心入口都链接到对应的任务文档、验证方法和限制。

| Console 页面 | 主要任务 |
| --- | --- |
| [Overview](../operations/index.md) | 查看健康、支出与下一步操作 |
| [Computer](../environments/computer.md) | 添加 SSH Target、打开终端、配置工具并附加给 Docker Agent |
| [Mobile](../environments/mobile.md) | 配对 Android、设置审批策略、执行受保护操作并连接 Agent |
| [Agents](../agents/index.md) | 创建、发布、部署、绑定 OpenWrt、调用 MCP、连接 Environment、查看 Activity |
| [Data Assets](../data-assets/index.md) | 管理集合、Agent 资产、不可变 Release 和 Marketplace 交付物 |
| [Providers](../providers/index.md) | 配置 Provider Account、Runtime、Model Pool Source 与 Community Listing |
| [Model Pool](../model-pool/index.md) | 管理 Provider-backed Source、能力池和池内路由 |
| [Routers](../routers/index.md) | 配置跨池流量策略、自定义 router.py 与访问导出 |
| [Marketplace](../marketplace/index.md) | 发现公开 Agent、Data Asset 与 Provider Capacity |
| [Observability](../operations/observability.md) | 查看指标、告警、报告、任务、资源和审计记录 |
| [Billing](../billing/index.md) | Wallet、套餐、消费与收益、订单、支付和发票 |
| TokenBank | 授信、资金池、金融产品、结算与风险流程 |
| [Access](../access/index.md) | 成员、角色、单资源共享、机器身份、Access Explain 与撤权 |
| [Settings](../settings/index.md) | Workspace、账户安全、API Key 和 SDK 连接值 |
| [Plan Catalog](../administration/plan-catalog.md) | Superuser 管理全局/Tenant Plan、Quota 和数据下载定价 |

顶部的 **Workspace** 是组织/租户边界，**Project** 是资源范围；左侧 Operate 分组中的 Computer 与 Mobile 在文档中统称 **Environments**。不要把它与 Agent 内部的 `env=prod` 部署槽位混淆。

资源可见不等于可操作。Server 会先确定 Workspace/Project，再计算成员关系、角色、资源级 AccessGrant 和机器身份策略。对某次拒绝需要解释时，使用 Access 页面或 `/api/v1/access/explain/`。

TokenBank 的页面与角色详见 [TokenBank 工作台参考](/tokenbank/reference/desks-and-products)。

## 新增与迁移的入口

| Console 路径 | 任务 |
| --- | --- |
| `/inbox` | [Work Inbox](../operations/inbox.md)：处理个人工作与共享队列 |
| `/openwrt-routers` | 注册和管理私有 Router，检查连接与依赖健康 |
| `/agents/{agentId}/private-display` | [Private Run](../agents/private-runs.md) 的调用入口 |
| `/agent-runs/{runId}/display` | 调用者自己的 Run 展示与交互 |
| `/access?tab=automation` | Machine identities；旧 `/api-keys` 重定向到这里 |

Computer 现在也支持主动配对的 Computer Runtime；旧功能地图中的 SSH Target 只描述保留的 SSH 方式。
