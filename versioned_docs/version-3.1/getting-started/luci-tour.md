---
sidebar_position: 3
title: LuCI 界面导览
---

# LuCI 界面导览

下面是根据当前 LuCI 源码绘制的界面示意，不是真实设备截图。字段、菜单和状态卡与 `luci-app-agent-router 3.1.0` 对应；主题、语言和屏幕宽度会改变实际外观。

## Quick Setup：配置 Agent 私有云网络

![LuCI Quick Setup 界面示意](/img/openwrt/luci-quick-setup.svg)

Quick Setup 是创建私有云网络的实际 LuCI 入口。第一次使用需要理解四组设置：

1. **Identity and service**：启用 Agent routing；Agent domain 定义私有云信任域，Router ID 定义当前节点身份。
2. **LAN discovery**：决定是否发现和发布同 LAN 的其他私有云节点。
3. **LAN admission**：选择手工批准、同域自动信任或 allowlist。
4. **Cross-network Relay**：只有 Directory 运营方提供 assignment URL 且需要跨 NAT 时才启用。

Router ID 长度为 1–64，只能使用小写字母、数字、点、下划线和连字符，并以字母或数字开头和结尾。

## Overview：验证私有云节点

![LuCI Overview 界面示意](/img/openwrt/luci-overview.svg)

绿色不代表所有业务调用都成功，但说明对应控制面有可用状态：

- **AFIB routes**：当前可选能力路由数。
- **ARPX sessions**：已建立的私有云节点 Peer 会话数。
- **LAN candidates**：等待审核或自动准入的 LAN 节点候选。
- **Relay tunnels**：跨 NAT Relay 隧道数。
- **Public Agent IPv6**：Router 管理的公网 IPv6 地址租约数。
- **Recovery**：UCI 配置是否成功加载；Degraded 时先看 Last error。

页面每 5 秒轮询有界元数据，不读取 prompt、工具参数、模型输出、访问令牌或任务正文。

## 下一步

- 单节点私有云：继续[发布第一个 Agent](/sdk/quickstart/first-agent)。
- 扩展私有云：完成[双路由器组网](../tutorials/two-router.md)。
- 状态异常：运行[一键诊断](../troubleshooting/diagnostics.md)。
