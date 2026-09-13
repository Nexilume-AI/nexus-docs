---
title: Settings
description: 管理账户资料、Workspace 上下文、开发者访问与连接示例。
---

# Settings

Settings 同时包含个人账户设置和当前 Workspace 的开发者上下文。修改前先看清顶部 Workspace/Project；SDK Snippet 和 Request Header 会随当前选择变化。

## Account profile

可更新显示名称等账户资料，并请求 Password Reset。重置动作通过已配置的认证/邮件流程完成，Console 不会回显现有密码。

账户资料属于用户身份；Workspace 成员关系、Role 和资源共享属于 [Access](../access/index.md)，不要用改名替代权限管理。

## Workspace context

选中的 Workspace 与 Project 保存在当前浏览器 Session，并作为 Nexus Header 发送。**Current request headers** 用于核对实际请求上下文；当同一用户属于多个 Workspace 时，这是排查“资源消失”或 403 的第一步。

在 **Manage workspaces** 中可以创建、重命名或删除 Workspace。删除是软删除，但会从正常使用中隐藏其 Projects、Groups、Members、Roles、Resource Shares、Service Accounts、API Keys、Billing 与 Audit Context。只有在名称确认框完全匹配时执行，并先导出需要保留的配置与财务记录。

## Developer access

页面提供当前上下文的 Connection Values、API Key 管理入口和 SDK Snippet。创建 API Key 时遵循最小权限：限定 Project、允许的资源/Router、速率或预算策略，并把明文 Key 立即保存到 Secret Manager；之后只能通过 Prefix 识别，不能再次取回原值。

更完整的 Key 生命周期见 [API Key 指南](../guides/api-keys.md)。机器到机器访问优先使用 [Machine identity](../access/index.md) 的 Service Account 与 Token，而不是共享个人 Key。

## 验证与排错

1. 对照 **Current request headers** 确认 Workspace/Project ID。
2. 复制当前 SDK 或 curl Snippet 发出最小请求。
3. 在 [Observability](../operations/observability.md) 的 Metrics/Audit 核对 Key Prefix 与请求结果。

- **Snippet 调到错误资源**：重新选择 Workspace/Project，再生成 Snippet；不要复用旧页面中的 Header。
- **API Key 返回 403**：检查状态、过期时间、Key Policy、Project 与允许的 Router/资源。
- **无法管理 Workspace**：需要相应 Owner/Admin 权限。
- **误删 Workspace**：这是软删除但 Console 不提供普通用户自助恢复；停止创建同名替代资源并联系平台管理员。
