---
sidebar_position: 1
title: 连接两台局域网路由器
---

# 连接两台局域网路由器

本教程把 Router A 上的 Agent 能力发布给 Router B。两台路由器处于同一二层局域网，不需要 Relay 或 Directory。

## 你需要

- 两台运行相同 Nexus 软件包批次的 OpenWrt 路由器。
- 两台设备的管理权限，且 LAN 之间允许 mDNS/umDNS 和 ARPX 会话。
- Router A 上至少有一个本地 Agent。

## 1. 配置 Router A

打开 **Agent Router → Quick Setup**：

- Enable Agent routing：启用
- Router ID：`router-a`
- Agent domain：`lab.example`
- Discover Agent routers on LAN：启用
- Publish this router on LAN：启用
- LAN admission：`Manual approval`

保存并应用。打开 Overview，应看到 Discovery enabled。

## 2. 配置 Router B

使用相同设置，但 Router ID 为 `router-b`，Agent domain 仍为 `lab.example`。保存后打开 **Peer Trust**，等待 `router-a` 出现在候选列表中，核对 Router ID 和域后批准。

如果希望无人值守接入，可在实验环境把两端 LAN admission 改成 `Automatically trust same-domain routers`。生产网络使用该模式前，应确认同一 LAN 和 domain 的管理边界一致。

## 3. 验证会话和路由

在 Router B 的 Overview 中确认：

- ARPX sessions 至少为 1。
- Recovery 为 Healthy。
- Capability Routes 中出现 Router A 的能力。

然后从 Router B 所在网络调用该能力。成功响应证明发现、信任、路由和转发均已工作。

## 常见失败

- **只有 LAN candidate，没有 ARPX session**：候选尚未在 Peer Trust 中批准。
- **两端互相看不到**：检查 umDNS、防火墙和二层隔离；访客 Wi-Fi 通常会阻断发现。
- **会话正常但没有能力路由**：检查 Router A 的本地 Agent 租约和双方策略 RIB。
- **跨 NAT 或不同站点**：本教程不适用，改用 [Node + Relay/Directory](../guides/router-roles.md)。
