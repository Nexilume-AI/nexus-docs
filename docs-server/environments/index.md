---
title: Environments
description: 管理 Agent 可以连接和使用的 Computer 与 Mobile 执行环境。
---

# Environments

Environments 对应 Nexus Console 左侧的 Operate 产品区域，包含 **Computer** 和 **Mobile**。它们把用户已有的计算机与移动设备安全地接入 Nexus，让 Agent 在明确授权后使用文件、终端或移动操作能力。

这里的 Environment 不等于顶部的 Workspace：

- **Workspace** 是组织、身份、计费和数据隔离边界，对应 Server tenant。
- **Project** 是 Workspace 内的资源范围。
- **Environment** 是 Project 中可供用户或 Agent 使用的执行目标。

## 选择哪一种 Environment

| 能力 | Computer | Mobile |
| --- | --- | --- |
| 目标 | Linux、macOS 或 Windows Computer Runtime / SSH 主机 | Android 设备 |
| 连接方式 | Computer Runtime 主动连接 Cloud，或 Server 通过 SSH 连接目标 | Nexus Mobile 使用配对 Token 和心跳连接 Server |
| 交互 | WebSocket 终端、文件与命令 API、工具配置 | 观察、截图、点击、输入、滑动、打开 App |
| Agent 接入 | Private Run 授权使用 Computer Runtime，或 Docker 部署时附加 SSH 目录 | 在 Agent 的 Mobile 面板连接设备 |
| 风险控制 | 授权根目录、只读/读写、SSH 账号权限 | 手动审批、高风险确认或自动审批 |

## 推荐工作流

1. 在顶部选择具体 Workspace 和 Project。
2. 配对 [Computer](computer.md) Runtime 或创建 SSH Target，或配对 [Mobile](mobile.md) Android Device。
3. 确认连接健康及需要的能力已经可用。
4. 打开 [Agents](../agents/index.md)，将 Environment 连接给目标 Agent。
5. 在 [Access](../access/index.md) 中只授予需要的管理或使用权限。
6. 在 Agent Activity 与 Observability 中核对执行记录。

## 安全边界

Environment 不会让 Agent 自动获得整台设备的所有权限：

- Computer 的 SSH 私钥或密码只由 Server 保存，绝不注入 Agent 容器。
- Docker Agent 只能通过短期 Workspace Token 访问授权根目录下的 Workspace API。
- `Read only` 禁止写文件和命令执行；`Read/write` 仍受 SSH 账号的操作系统权限约束。
- Mobile 命令根据风险等级和设备 Approval mode 决定是否等待人工批准。
- 所有资源继续受 Workspace、Project、角色和资源级共享约束。

## 当前范围

Computer 提供 Runtime 连接与 SSH 终端/工具工作台，不提供远程 IDE 托管。Mobile 当前支持 Android；截图是短期受保护数据，不作为长期文件存储。具体状态和操作见 [Computer](computer.md) 与 [Mobile](mobile.md)。

## 当前 Computer 接入方式

上表中的 SSH 是保留的连接方式。新计算机可通过 Nexus Computer Runtime 主动连接 Cloud，无需开放 SSH 入站端口；完成配对后，在每次使用中继续验证目录和能力授权。Computer 位于 **Operate** 导航组。完整流程见 [Computer](computer.md)。
