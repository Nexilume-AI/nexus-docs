---
sidebar_position: 1
title: 为每个 Agent 分配一个 IPv6
description: 不配置 Router，只用 SDK Host Alias 为 Agent 获取独立 IPv6 地址。
---

# 为每个 Agent 分配一个 IPv6

本快速入门不从“注册到一台路由器”开始，而是先验证 Nexus 最直观的能力：**每个 Agent 都可以拥有自己的 IPv6 地址**。你将使用 SDK Host Alias，在一台主机上为两个 Agent 租用两个不同的 `/128`，它们可以共用端口 `9443`。

先完成[安装](../quickstart/installation.md)。以下实验针对可用 `/64` 的 Host Alias 路径；其他地址模式见 [Linux 指南](../guides/linux-ipv6.md)。

## 1. 确认前提

你需要 Python 3.9+，以及一个确实在链路上可用或已路由到主机的全球 IPv6 `/64`。单个运营商 `/128`、ULA 和 `2001:db8::/32` 文档地址都不能完成这个实验。

## 2. 安装

```bash
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m venv .venv
# Linux: . .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
```

Windows 需要额外组件：

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

Linux 使用 systemd 安装流程；前提与 0.46.2 修复见 [Linux IPv6 指南](../guides/linux-ipv6.md)：

```bash
nexus-agent ipv6 setup
nexus-agent ipv6 doctor
```

## 3. 看懂关键代码

每个 Agent 都独立请求 `"auto"` 地址：

```python
from nexus_agent import NexusAgent

agent = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="agent-a",
    port=9443,
)
```

`nexus-agent-addressd` 执行受限的网卡操作；普通 Python 进程只持有地址租约。这里的 `auth="none"` 只用于隔离实验网。

## 4. 运行并验证

Linux：

```bash
export NEXUS_IPV6_LAB=1
python examples/ipv6_agents_call_each_other.py
```

Windows PowerShell：

```powershell
$env:NEXUS_IPV6_LAB = '1'
python examples/ipv6_agents_call_each_other.py
```

输出中 `agent_a.ipv6` 和 `agent_b.ipv6` 应是两个不同的全球 IPv6 地址。程序退出时，SDK 会停止监听、释放租约并移除两个 `/128`。

下一步：[让两个 IPv6 Agent 互相调用](call-first-agent.md)。如需逐行解释、跨主机部署和生产加固，请阅读[完整教程](../tutorials/ipv6-agents-call-each-other.md)。
