---
sidebar_position: 1
title: 页面与使用顺序
---

# LuCI 页面与使用顺序

菜单位于 **状态 → Agent Routing**。面向用户的第一个目标是“配置 Agent 私有云网络”；设备上的实际配置入口仍叫 **Quick Setup**。

| 类型 | 页面 | 何时使用 |
| --- | --- | --- |
| 私有云初始化 | [Quick Setup](quick-setup.md)、[Router Roles](roles.md) | 创建信任域和首个节点，或承载 Relay/Directory |
| 功能配置 | [Agent APIs & Protocols](protocols.md)、[Advanced Settings](advanced-settings.md)、[Static Peers](static-peers.md)、[Policy RIB](policy-rib.md) | 接入 Agent，配置公网 IPv6、发现、Peer 和策略 |
| 状态与信任 | [Overview](overview.md)、[Local Agents](local-agents.md)、[Capability Routes](capability-routes.md)、[Neighbors & Discovery](neighbors.md)、[Peer Trust](peer-trust.md) | 验证节点、租约、路由、邻居和信任状态 |

推荐顺序：**Quick Setup → Agent APIs & Protocols → Local Agents → Capability Routes → Overview**。只有扩展到第二个节点时再处理 discovery/Peer；只有公网 `/128`、跨域或跨 NAT 需求时再进入 Advanced Settings。

:::tip 保存与运行状态
配置页修改后点击 **Save & Apply**。保存成功只表示候选配置通过校验；还应在状态页确认服务、会话、租约和路由已经生效。
:::
