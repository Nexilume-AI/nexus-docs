---
sidebar_position: 3
title: 创建第一个 Workspace 和 Project
description: 建立 Nexus 的组织边界、项目范围和可复用执行环境。
---

# 创建第一个 Workspace 和 Project

完成本页后，Console 顶部会选中一个 Workspace 和一个 Project。后续 Agent、Provider、权限、用量和费用都会在这个上下文中创建，避免“资源明明存在却返回 404/403”。

## 需要准备

- 已登录管理员提供的企业版 Console。本章的 Workspace/Project 管理面向企业版；自行安装的用户参见[社区版本地启动](quickstart.md)。
- 当前用户可以创建 Workspace；首次本地评估可使用刚创建的 superuser。

## 三个容易混淆的名称

| 名称 | 解决什么问题 | 是否出现在请求上下文 |
| --- | --- | --- |
| Workspace | 组织、安全、账单和审计边界；Server 内部对应 tenant | `X-Nexus-Tenant`，业务 API 通常必需 |
| Project | Workspace 内的资源与协作范围 | `X-Nexus-Project`，部分列表可省略以查看 All projects |
| Computer Environment | Agent 可连接的 SSH 计算机与目录 | 作为资源被 Project 管理，不是 tenant |

Environment 也不是 `dev/staging/prod` 发布槽位。Agent Runtime 自己有部署环境状态，不要用 Computer 代替 Project。

## 1. 创建 Workspace

1. 打开 **Settings → Workspace**。
2. 在 **Manage workspaces** 输入 `Nexus Demo`，点击 **Create**。
3. Console 会自动切换到新 Workspace；顶部第一个选择器应显示 `Nexus Demo`。

创建 Workspace 后仍可能显示 **All projects**。这是跨项目查看模式，不是一个可以承载新资源的 Project。

## 2. 创建 Project

1. 打开 **Access**，点击 **Create project**。
2. 输入 `First Project`；首次体验可以不选择 Team。
3. 创建后回到顶部 Project 选择器并选中 `First Project`。

如果页面仍显示旧列表，刷新一次或重新选择 Workspace。Project 必须属于当前 Workspace。

## 3. 验证上下文

打开 **Settings → Workspace context**，确认两个名称正确。随后打开 **Agents**：页面标题下应显示 `First Project`，而不是 **All projects**。

自动化请求使用对应 UUID，而不是显示名称：

```http
X-Nexus-Tenant: <workspace-uuid>
X-Nexus-Project: <project-uuid>
```

## 权限边界

- Workspace 是最高产品隔离边界。切换后资源、成员、Wallet、API Key 和 Audit 都会变化。
- Project 管理资源归属；Workspace Wallet 仍是 Workspace 级，不会为每个 Project 创建独立余额。
- Role 可以在 Workspace、Project 或 Group 范围生效；单资源例外使用 Resource Share。
- 删除 Workspace 是软删除，但会从正常使用中隐藏其 Project、访问、Key、Billing 和 Audit 上下文。不要把它当作清空演示数据按钮。

## 验证

- 顶部选择器同时显示 `Nexus Demo` 和 `First Project`。
- **Agents**、**Providers** 和 **Billing** 打开时不再提示缺少 Workspace。
- 创建资源前，页面显示具体 Project 而非 **All projects**。

## 排错

- **没有 Create Workspace**：当前账号没有相应管理权限，或仍处于匿名模式。
- **Project 创建后不可见**：检查 Workspace 是否切换，Project 不会跨 Workspace 出现。
- **API 返回 `X-Nexus-Tenant header is required`**：自动化请求缺少 Workspace UUID。
- **已知资源返回 404**：优先检查两个请求头与资源实际归属，而不是立即重建资源。

## 当前限制与下一步

Console 当前从 **Settings** 创建 Workspace，从 **Access** 创建 Project，因此首次配置跨两个页面。下一步使用这个上下文完成[第一个 Agent 工作流](first-agent.md)，或先阅读[身份与请求路径](../concepts/identity-and-request-path.md)。
