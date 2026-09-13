---
sidebar_position: 1
title: 为什么每个 Agent 应有一个 IP
description: 理解 Agent 逻辑身份、IPv6 网络身份、认证身份和路由策略之间的边界。
---

# 为什么每个 Agent 应有一个 IP

传统服务常用“一个主机 IP + 多个端口”区分进程。Nexus 还支持从一个真实可用的 IPv6 `/64` 中，为每个 Agent 租用独立 `/128`。这样，网络层看到的目标就是 Agent，而不是“某台主机上的某个端口”。

```text
240e:1234:5678:1200::a1  → agent://demo/agent-a
240e:1234:5678:1200::b1  → agent://demo/agent-b
```

两个 Agent 可以监听同一个端口，因为它们绑定不同的 IPv6 地址。这对防火墙、流量统计、故障定位和未来的 DNS 发布都更直观。

## 四层身份不要混为一谈

| 层次 | 示例 | 回答的问题 |
| --- | --- | --- |
| Agent 逻辑身份 | `agent://demo/agent-a` | Envelope 声明“谁在调用” |
| IPv6 网络身份 | `240e:...::a1/128` | 数据包发往哪个 Agent |
| TLS/JWT 认证身份 | 证书 SAN、issuer、audience、scope | 对端是否可信、是否获准调用 |
| 能力身份 | `demo.hello` | 这次请求要执行什么 |

独立 IPv6 地址能精确寻址，但**地址可达不等于授权通过**。公网或跨信任域部署仍应使用 TLS 和认证策略；不要把“知道 IP”当成访问凭据。

## SDK-only Host Alias 如何工作

```text
Agent 进程
  └─ NexusAgent.public_ipv6("auto")
       └─ 本地 IPC 请求租约
            └─ nexus-agent-addressd
                 └─ 在允许的接口和 /64 中添加一个 /128
```

`nexus-agent-addressd` 是最小特权辅助服务。管理员只配置一次允许的网卡、`/64`、本地用户和地址配额；普通 Agent 进程只能申请、确认、续租和释放自己的地址。Agent 停止后，租约释放，地址随之移除。

这条路径不需要 OpenWrt Router、Directory、AFIB、Relay、能力注册或回调映射。调用方已知目标 IPv6 和端口时，使用 `DirectIPv6Agent` 直接连接。

## 地址从哪里来

`address="auto"` 不会创造 IPv6 地址空间。必须满足以下条件之一：

- `/64` 已在 Agent 主机所在链路上可用；
- 上游已把该 `/64` 路由到 Agent 主机。

如果运营商只给主机一个 `/128`，SDK 不能把它扩展成多个地址。此时可选择同 IP 不同端口，或让 OpenWrt 从可用前缀托管 Agent `/128`。

## 两条“一 Agent 一 IP”路径

| 模式 | 地址由谁持有 | 调用路径 | 适合场景 |
| --- | --- | --- | --- |
| SDK Host Alias | Agent 主机 | `DirectIPv6Agent` 直连 | 单机实验、边缘主机、已有 `/64` 的服务器 |
| Router-managed `/128` | OpenWrt | Router 精确入口和 AFIB | 需要统一准入、路由策略、协议适配和跨站点治理 |

建议先完成 [两个 IPv6 Agent 互相调用](../tutorials/ipv6-agents-call-each-other.md)，亲眼看到两个 `/128`，再阅读 [OpenWrt 地址归属模型](/openwrt/communication/addressing)选择生产路径。
