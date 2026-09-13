---
slug: /
sidebar_position: 1
title: Python SDK 用户指南
description: 从一 Agent 一 IPv6 地址到可恢复调用，系统学习 nexus-agent-sdk。
---

# Python SDK 用户指南

`nexus-agent-sdk` 的核心能力是让 Agent 成为真正可寻址的网络节点：一个主机拥有可用 IPv6 `/64` 时，SDK 可以为**每个 Agent 分配一个独立 IPv6 `/128`**，Agent 之间按地址直接调用。它还提供 HTTP/SSE Server、Router 注册租约、认证，以及 FastMCP/A2A 集成。当前版本为 **0.22.0**，支持 Python **3.9+**。

## 第一次运行：只用 SDK

不配置 OpenWrt，也能完成第一个端到端结果：

1. [为每个 Agent 分配一个 IPv6](quickstart/first-agent.md)；
2. [让两个 IPv6 Agent 互相调用](quickstart/call-first-agent.md)；
3. 运行完整的[双 Agent 教程](tutorials/ipv6-agents-call-each-other.md)。

这条 Host Alias 路径需要主机拥有真实可用的全球 IPv6 `/64` 和本地 `nexus-agent-addressd`。它不经过 Router、Directory、AFIB 或 Relay。

## 系统学习路线

1. [为什么每个 Agent 应有一个 IP](concepts/one-agent-one-ip.md)：区分逻辑身份、网络身份、认证身份和能力身份。
2. [SDK 运行时心智模型](concepts/runtime-model.md)：理解 facade、client、server 和 lease 的职责。
3. [Envelope、身份与认证](concepts/envelope-auth.md)：理解调用者能声明什么、服务端必须验证什么。
4. [注册、续租与自愈](concepts/registration-lifecycle.md)：当你引入 OpenWrt 后，理解 route ID、健康撤销和 Router 重启恢复。
5. [流式恢复原理](concepts/streaming-resume.md)：理解 task、route、请求指纹和事件游标。
6. [从 Echo 到可恢复 Agent](tutorials/resilient-agent.md)：组合同步、SSE、Router 租约和短断线恢复。

## 两种部署层次

| 目标 | 从这里开始 |
| --- | --- |
| 两个 Agent 已知彼此地址，直接通信 | [直接 IPv6 Agent](guides/direct-ipv6.md) |
| OpenWrt 统一托管地址、发现、路由和跨 NAT 通信 | [配置 Agent 私有云网络](/openwrt/getting-started/quick-setup) |
| 集成工具或 Agent 协议 | [FastMCP](integrations/fastmcp.md)、[A2A](integrations/a2a.md) |
| 查签名和排错 | [核心方法参考](reference/core-methods.md)、[错误目录](troubleshooting/error-catalog.md)、[诊断工具](troubleshooting/diagnostics.md) |

仓库中的可运行示例位于 `sdk/nexus-agent-sdk-python/examples/`；一 Agent 一 IP 的默认入门示例是 `ipv6_agents_call_each_other.py`。
