---
sidebar_position: 2
title: 配置 Agent 私有云网络
description: 从一台 OpenWrt 节点开始，建立 Agent 私有云的身份、边界、发现和接入能力。
---

# 配置 Agent 私有云网络

本指南把一台 OpenWrt 配置成 Agent 私有云的第一个网络节点。完成后，你会得到一个最小但完整的私有云：它有自己的信任域、Router 节点身份、Agent 注册入口和能力路由表，之后可以继续加入更多 Router、IPv6 公网入口或 NAT Relay。

“Agent 私有云网络”是面向用户的部署概念，不是新增的 UCI 字段。它由现有配置组成：**Agent domain 是私有云信任域，Router ID 是私有云节点身份**。

## 1. 打开私有云网络配置入口

打开 **服务 → Agent Router → Quick Setup**。Quick Setup 是 LuCI 中创建私有云网络的实际页面名。它负责身份、LAN 发现和可选 Relay；Node、Relay、Directory 角色在 **Router Roles** 页面配置。

## 2. 创建信任域和第一个节点

- **Enable Agent routing**：开启。
- **Router ID**：填写稳定且唯一的节点标识，例如 `router-a`。长度为 1–64，只能使用小写字母、数字、点、下划线和连字符，首尾必须是字母或数字。
- **Agent domain**：填写私有云信任域，例如 `lab.example`。需要加入同一私有云且允许同域准入的 Router 使用相同值。

不要把 Router ID 当作设备临时主机名。动态 Peer、能力来源和运维记录都会引用它，投入使用后应保持稳定。

## 3. 选择私有云网络边界

### 只有一个节点

如果当前只有这一台 Router，关闭 LAN discovery 和 Relay 即可。Agent 仍然可以注册、发布能力并通过本 Router 相互调用。

### 同一 LAN 上有多个节点

- **Discover Agent routers on LAN**：发现同 LAN 的 Nexus Router。
- **Publish this router on LAN**：让其他节点发现本机。
- **LAN admission**：首次配置选择 `Manual approval`。验证身份后再按需要改成 `same-domain` 或 `allowlist`。

DNS-SD 只产生 Router 候选，不直接发现 Agent，也不会自动生成能力路由。

### 节点位于 NAT 后

只有 Directory 运营方提供 assignment URL 且需要跨 NAT/站点连接时，才启用 **Connect through Nexus Directory and Relay**。最多配置四个 HTTPS URL，并按顺序故障切换。

## 4. 保存并验证私有云控制面

点击 **Save & Apply**，打开 **Overview**。至少确认：

- **Recovery** 为 Healthy。
- LAN discovery 和 Relay 状态与你选择的网络边界一致。
- 没有 “status is unavailable” 错误横幅。
- 单节点私有云没有 Peer 或 Relay 时，ARPX/Relay 数量为 0 是正常状态。

如果 Recovery 为 Degraded，先查看 Recovery domains 的 Last error，再运行[一键诊断](../troubleshooting/diagnostics.md)。

## 5. 接入第一个 Agent

在 **Agent APIs & Protocols** 中开启 Python SDK registration 和 Agent invocation，然后使用 [Python SDK 快速入门](/sdk/quickstart/first-agent)发布第一个 Agent。

完成标志：

1. **Local Agents** 中出现 Agent 能力租约。
2. **Capability Routes** 中出现对应 intent。
3. 调用方收到真实响应，而不只是页面显示 Healthy。

## 6. 扩展私有云节点角色

普通节点保持 **Node only**。需要为其他站点中继流量时选择 **Node + Relay**；负责分配可信 Relay 时选择 **Node + Directory**。详见[配置私有云节点角色](../guides/router-roles.md)。

下一步可以按[通信模式选择器](../communication/model.md)决定是否增加 LAN Peer、每 Agent IPv6、公网入口、SVCB 或 NAT Relay。
