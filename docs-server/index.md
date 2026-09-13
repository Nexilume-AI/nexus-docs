---
slug: /
sidebar_position: 1
title: Nexus Server 用户指南
description: 从首次 Agent 调用到 Provider、访问、计费和生产运维的完整用户路径。
---

# Nexus Server 用户指南

Nexus Server 是 Nexus 的云端控制面。它提供 REST API、Nexus Console、移动设备 API 和 Computer WebSocket 网关，并把 Workspace、Project、资源权限、计费与审计放在同一个身份边界内。

文档按“先得到结果，再理解系统，最后安全运营”组织。第一次使用先建立 Workspace/Project，再运行仓库内的示例 Agent；业务用户可以直接进入端到端教程，部署者从生产就绪清单开始。

## 第一次运行

1. 企业版用户打开管理员提供的 Console；自行安装的用户按[社区版本地启动](getting-started/quickstart.md)操作。
2. [创建第一个 Workspace 和 Project](getting-started/first-workspace.md)，选中明确的资源与费用上下文。
3. 用[Console 导览](getting-started/console-tour.md)理解各产品工作区。
4. 跟随[第一个 Agent 教程](getting-started/first-agent.md)，构建示例镜像，完成部署、MCP 调用和验证。
5. Agent 需要远程计算机或 Android 时进入 [Environments](environments/index.md)；已有 OpenWrt 时按[接入 OpenWrt IPv6 Agent](guides/connect-openwrt.md)使用自有 IPv6 节点。

## 三条端到端教程

| 目标 | 教程 | 成功后验证 |
| --- | --- | --- |
| 建立模型服务入口 | [Provider → Model Pool → Router → API](tutorials/provider-router-api.md) | Gateway 响应、Observability、Billing Provider Pool |
| 管理人员访问全生命周期 | [邀请、授权、验证与离职撤权](tutorials/team-access-lifecycle.md) | Access Explain、Recent changes、Audit |
| 发布并核对商业结果 | [Marketplace 发布 → 消费 → Billing 对账](tutorials/marketplace-billing.md) | 交付物、Spending/Earnings、Order、Audit |

## 核心工作区

| 工作区 | 你可以完成什么 |
| --- | --- |
| [Environments](environments/index.md) | 连接 Computer、配对 Mobile，并把执行环境交给 Agent 使用 |
| [Agents](agents/index.md) | 创建 Agent，选择 Docker 或 OpenWrt Runtime，部署、调用和发布 |
| [Data Assets](data-assets/index.md) | 把 Agent Trace、Memory 和 Output 变成受治理的 Collection 与 Release |
| [Providers](providers/index.md) | 保存上游凭据，运行 Provider Runtime，并加入 Model Pool、Router 或 Marketplace |
| [Model Pool](model-pool/index.md) | 把 Provider Runtime 作为模型源，配置健康、成本与池内回退 |
| [Routers](routers/index.md) | 在多个 Model Pool 之间配置优先级、成本、延迟、健康或自定义路由 |
| [Marketplace](marketplace/index.md) | 发现和获取公开 Agent、Data Asset 与 Provider Capacity |
| [Operations](operations/index.md) | 用 Overview 分诊，并调查指标、任务、告警、审计和生产状态 |
| [Access](access/index.md) | 邀请成员、分配角色、共享单个资源和创建机器身份 |
| [Billing](billing/index.md) | 查看钱包、套餐、Marketplace 用量、支付订单和发票 |
| [Settings](settings/index.md) | 管理账户、Workspace 上下文、API Key 与 SDK 示例 |

## 按角色进入

| 角色 | 建议入口 |
| --- | --- |
| 平台部署者 | [生产就绪](operations/production-readiness.md)、[部署](guides/production-deployment.md)、[备份恢复](operations/backup-and-restore.md)、[升级回滚](operations/upgrade-and-rollback.md) |
| Workspace 管理员 | [Access](access/index.md)、[Billing](billing/index.md)、[Settings](settings/index.md) |
| Agent 构建者 | [第一个 Agent](getting-started/first-agent.md)、[Agents](agents/index.md)、[Environments](environments/index.md) |
| Provider 运营者 | [Provider→Router 教程](tutorials/provider-router-api.md)、[Providers](providers/index.md)、[Model Pool](model-pool/index.md) |
| Marketplace 运营者 | [Marketplace→Billing 教程](tutorials/marketplace-billing.md)、[Marketplace](marketplace/index.md) |
| API 开发者 | [API 约定与示例](reference/api.md)、[状态与错误](reference/statuses-and-errors.md)、内置 Swagger |
| 财务与风控 | [Billing](billing/index.md)、[TokenBank 用户指南](/tokenbank/) |

## 重要边界

- Workspace 是 tenant、权限、Billing 和 Audit 边界；Computer Environment 是 Agent 使用的执行资源。
- Agent Key、Gateway Key、Remote CLI Key 和 Service Account Token 用途不同，不能互换。
- 只有实际调用、购买或产品定义的消费动作才可能移动平台资金；Create、Health 和 Publish 本身不等于已计费。
- TokenBank 是内部授信、控制与结算系统，不是银行、公共交易所、保险或外部现金清算机构。
- 生产不能用 SQLite、开发服务器或 Celery eager 代替 PostgreSQL、ASGI、Worker 和 Beat。

出现登录、WebSocket、上下文、Runtime、Provider、存储、费用或 Edge TLS 问题时，从[常见故障排查](troubleshooting/common.md)开始，并用[状态与错误参考](reference/statuses-and-errors.md)解释错误码。

## 当前执行与待办流程

- [Private Run 与交互执行](agents/private-runs.md)：调用者自己的展示、文件、后续消息和恢复。
- [Work Inbox](operations/inbox.md)：个人待办和共享角色队列，处理输入、审批与运维异常。

本指南对应企业版 Server。开发启动同样要求 PostgreSQL；Computer 支持 Runtime 主动配对与 SSH 两种接入方式，Agents 支持 Python 上传构建。所有入口以当前用户权限和部署配置为准。
