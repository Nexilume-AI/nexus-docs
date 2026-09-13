---
sidebar_position: 2
title: 让两个 IPv6 Agent 互相调用
description: 使用 DirectIPv6Agent 按目标 IPv6 地址完成 A 到 B、B 到 A 的调用。
---

# 让两个 IPv6 Agent 互相调用

完成[地址快速入门](first-agent.md)后，两个 Agent 已分别拥有一个 `/128`。调用不需要 Router 查表：调用方把目标 IPv6 地址交给 `DirectIPv6Agent`，再发送能力名和 Nexus Envelope。

## 1. Agent A 调用 Agent B

```python
from nexus_agent import DirectIPv6Agent

target_b = DirectIPv6Agent.plain_http(
    agent_b.address,
    port=agent_b.endpoint.port,
)

a_to_b = target_b.invoke(
    "demo.hello",
    {"message": "hello from Agent A"},
    tenant="demo",
    source_agent=agent_a.origin,
)
```

`agent_b.address` 是目标网络身份；`source_agent=agent_a.origin` 是 Envelope 中的调用方逻辑身份。二者不能互相替代。

## 2. Agent B 调用 Agent A

```python
target_a = DirectIPv6Agent.plain_http(
    agent_a.address,
    port=agent_a.endpoint.port,
)

b_to_a = target_a.invoke(
    "demo.hello",
    {"message": "hello from Agent B"},
    tenant="demo",
    source_agent=agent_b.origin,
)
```

运行 `examples/ipv6_agents_call_each_other.py` 会连续执行这两个方向，并打印双方地址和真实 JSON 响应。

## 3. 这个入门例子没有什么

- 没有 `NEXUS_ROUTER_URL`；
- 没有 OpenWrt 配置；
- 没有 Router 注册、能力路由或 AFIB；
- 没有 Directory、Relay 或 NAT 穿透；
- 没有自动发现，目标地址由示例直接传给调用方。

这正是 SDK-only 直连模式。跨进程或跨主机时 API 不变，只需用安全配置、Agent Card、DNS SVCB 或可信目录传递目标地址。

## 4. 不要把实验模式带到公网

`plain_http()` 和服务端 `auth="none"` 会明文传输请求，且不验证调用者。它们只用于隔离实验。生产环境改用 HTTPS `DirectIPv6Agent(...)`、可信 CA、短期 token 和服务端认证策略，并限制防火墙来源。

继续阅读[两个 IPv6 Agent 互相调用](../tutorials/ipv6-agents-call-each-other.md)完成环境、验证、故障处理和生产加固；API 细节见[直接 IPv6 Agent](../guides/direct-ipv6.md)。
