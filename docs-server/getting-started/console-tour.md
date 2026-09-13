---
sidebar_position: 2
title: Console 导览
description: 理解 Nexus Console 的 Workspace、Project 和主要产品工作区。
---

# Console 导览

Nexus Console 的顶部选择“在哪个组织和项目中工作”，左侧导航选择“要管理哪类资源”。先确认上下文，再创建或修改资源，可以避免把 Agent、Provider 或费用记到错误的 Project。

## Workspace、Project 和 Environment

| 名称 | 在 Console 中的位置 | 含义 |
| --- | --- | --- |
| Workspace | 顶部第一个选择器 | 组织与安全边界；对应 Server 的 tenant |
| Project | 顶部第二个选择器 | Workspace 内的资源与协作范围；可选择 **All projects** 查看跨项目资源 |
| Environment | 左侧 Workspace 分组中的 Computer 与 Mobile | Agent 可以连接和使用的执行环境，不是 `dev/staging/prod` 部署槽位 |

切换 Workspace 后，Project 列表、资源、权限和 Billing 数据都会随之变化。遇到“资源不存在”或 403 时，先检查这两个选择器。

## 左侧工作区

| 分组 | 页面 | 常见任务 |
| --- | --- | --- |
| Overview | Overview | 查看健康、费用和下一步建议 |
| Environments | Computer、Mobile | 连接 SSH 计算机、配对 Android 设备、配置工具和执行受保护操作 |
| AI resources | Agents、Data Assets | 构建 Agent，管理运行时、显示运行、数据集合和发布版本 |
| Model services | Providers、Model Pool、Routers | 接入模型账号、运行容量、组合模型源和配置流量策略 |
| Marketplace | Agents、Data Assets、Providers | 发现并使用公开资源 |
| Operations | Observability、Billing、TokenBank | 查看指标、告警、审计、平台费用和金融工作台 |
| Management | Access、Settings | 管理成员、角色、机器身份、API Key 和账户安全 |

## 推荐浏览顺序

1. 没有上下文时先[创建 Workspace 和 Project](first-workspace.md)，再从顶部同时选中二者。
2. 用[第一个 Agent](first-agent.md)先证明部署、MCP 调用和审计路径可用。
3. 需要外部计算资源时打开 [Environments](../environments/index.md)。
4. 需要模型时走 [Provider→Router 教程](../tutorials/provider-router-api.md)，不要在第一次 Agent 调用前引入上游凭据变量。
5. 用 [Access](../access/index.md)分配长期权限，单资源例外使用 **Share**。
6. 在 [Billing](../billing/index.md) 和 Observability 中确认用量、费用、任务和审计事件。

## 一个动作完成后去哪里看

| 你刚做的动作 | 业务状态 | 独立证据 |
| --- | --- | --- |
| 创建或部署 Runtime | Agents/Providers 的状态与 Health | Observability Job、Audit |
| 调用 Agent 或 Router | Activity/Gateway 响应 | Metrics、Request ID、Billing Usage |
| 邀请或授权成员 | Access 列表 | Access Explain、Recent changes、Audit |
| 发布或消费资源 | Marketplace 状态和交付物 | Spending/Earnings、Order、Audit |
| 修改生产配置 | 服务健康与进程状态 | Worker/Beat、备份 ID、恢复演练 |

## 登录前后看到的内容

匿名访问只显示公开 Marketplace 和产品介绍。登录成功后，Server 才加载 Workspace、Project、私有资源和 Billing 数据。浏览器使用会话 Cookie；CLI 与自动化使用 JWT、API Key 或服务账号 Token。凭据区别见[身份与请求路径](../concepts/identity-and-request-path.md)。

## 下一步

继续完成[第一个 Agent 教程](first-agent.md)，平台部署者从[生产就绪架构](../operations/production-readiness.md)开始；也可以按[用户功能地图](../reference/user-surfaces.md)直接进入目标页面。

## 当前导航分组

- **Build**：Agents、Data Assets；Model Fabric 下依次是 Providers → Model Pool → Routers。
- **Operate**：Computer、[Inbox](../operations/inbox.md)、OpenWrt Routers、Mobile、Observability。
- **Discover**：Agents、Data Assets、Provider Runtimes 三个 Marketplace。
- **Govern**：Access、Billing、Settings、TokenBank，以及仅 Superuser 可见的 Plan Catalog。

旧 `/gateway`、`/playground` 会转到 Computer；`/models`、`/deployments` 转到 Model Pool；旧 `/api-keys` 转到 Access 的 Machine identities。独立的 [Private Run 显示页](../agents/private-runs.md) 不应当作公开展示页共享。
