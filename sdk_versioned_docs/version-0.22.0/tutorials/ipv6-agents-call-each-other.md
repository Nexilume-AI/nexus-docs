---
sidebar_position: 1
title: 两个 IPv6 Agent 互相调用
description: 只使用 Python SDK，为两个 Agent 分配不同 IPv6 地址并完成双向调用。
---

# 两个 IPv6 Agent 互相调用

本教程只使用 `nexus-agent-sdk`：在同一台主机上创建 Agent A 和 Agent B，为它们各租用一个全球 IPv6 `/128`，让 A 按 B 的 IPv6 地址调用 B，再让 B 按 A 的地址调用 A。调用路径中没有 OpenWrt、Router 注册、Directory、AFIB 或 Relay。

完成后你会看到类似结果：

```text
Agent A: [真实 IPv6 A]:9443
Agent B: [真实 IPv6 B]:9443
A → B: demo.hello
B → A: demo.hello
```

## 你需要什么

- Python 3.9 或更高版本；
- 一个确实在链路上可用或已路由到主机的全球 IPv6 `/64`；
- Linux 或 Windows 主机；
- 管理员首次配置 `nexus-agent-addressd` 的权限；
- 用于明文实验的隔离网络。生产网络的安全做法见本教程末尾。

:::warning 地址前提
只有一个运营商 `/128` 不够。SDK 不能凭空生成更多公网地址。`2001:db8::/32` 也是文档保留前缀，不能拿来实际运行。
:::

## 第 1 步：安装 SDK 并准备地址服务

从源码仓库运行：

```bash
cd sdk/nexus-agent-sdk-python
python -m venv .venv
python -m pip install -e .
```

Linux 管理员在单独终端启动受限地址服务，把示例值替换为真实网卡和 `/64`：

```bash
sudo nexus-agent-addressd \
  --interface eth0 \
  --prefix 240e:1234:5678:1200::/64
```

Windows 使用一条命令完成发现、UAC 提权、服务安装和临时 `/128` 自检：

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

首次把用户加入 `Nexus Agent Users` 后，需要注销并重新登录一次。然后验证非管理员路径：

```powershell
nexus-agent ipv6 doctor
```

## 第 2 步：运行 SDK-only 双 Agent 示例

示例使用明文 HTTP 且不使用 JWT，只用于隔离实验网。显式打开实验保护开关后运行：

Linux/macOS：

```bash
export NEXUS_IPV6_LAB=1
python examples/ipv6_agents_call_each_other.py
```

Windows PowerShell：

```powershell
$env:NEXUS_IPV6_LAB = '1'
python examples/ipv6_agents_call_each_other.py
```

到这里已经得到第一次可见结果。输出中的 `agent_a.ipv6` 和 `agent_b.ipv6` 必须不同，而两个 Agent 的端口都可以是 `9443`。

## 第 3 步：读懂地址分配

示例为每个 Agent 调用同一个工厂方法：

```python
agent_a = NexusAgent.public_ipv6(
    "auto",
    address_mode="host-alias",
    auth="none",
    tenant="demo",
    agent_id="agent-a",
    port=9443,
)
```

- `"auto"`：向本地 `addressd` 申请地址，不写死 `/128`；
- `address_mode="host-alias"`：明确使用一 Agent 一地址模式；
- `agent_id`：决定逻辑身份 `agent://demo/agent-a`，也参与稳定地址分配；
- `port=9443`：两个 Agent 能复用端口，因为它们的 IPv6 地址不同；
- `auth="none"`：只适合这次隔离实验。

`start()` 绑定监听地址，确认租约并自动续租；上下文退出时关闭监听并释放 `/128`。

## 第 4 步：读懂 A 到 B、B 到 A

调用端直接使用目标 Agent 的数值 IPv6：

```python
target_b = DirectIPv6Agent.plain_http(
    agent_b.address,
    port=agent_b.endpoint.port,
)

reply = target_b.invoke(
    "demo.hello",
    {"message": "hello from Agent A"},
    tenant="demo",
    source_agent=agent_a.origin,
)
```

这里没有能力发现。`DirectIPv6Agent` 已经知道目标 `/128`、端口和能力名，直接发送 Nexus Envelope。反向调用只需把目标换成 `agent_a.address`，并把 `source_agent` 换成 `agent_b.origin`。

同一进程只是为了让入门示例一次运行完成。拆成两个进程或两台主机时，服务端 API 和调用 API 不变；需要通过配置、Agent Card、DNS SVCB 或可信目录把目标地址交给调用方。

## 第 5 步：验证没有走 Router

这个示例中不应出现以下任何配置：

- `NEXUS_ROUTER_URL`；
- Router 注册令牌；
- LuCI 能力路由；
- AFIB、Directory 或 Relay 地址。

可以在运行时检查地址：

Linux：

```bash
ip -6 address show dev eth0
```

Windows：

```powershell
Get-NetIPAddress -AddressFamily IPv6
```

程序退出后再次检查，两个租用 `/128` 应已被释放。

## 生产环境加固

明文实验把 Envelope、请求和结果暴露在网络上。生产部署至少完成以下工作：

1. 为被调用 Agent 配置 `cert_file`、`key_file`、`tls_server_name` 和 `ca_bundle_id`；
2. 使用 `HmacJwtServerAuth` 或集成方实现的 `ServerAuthPolicy`；
3. 调用端用 `DirectIPv6Agent(...)` 配置证书身份、CA 和短期 token；
4. 用主机防火墙限制入口端口和允许的源前缀；
5. 不把 HS256 共享密钥或 token 写进源代码。

如果需要由路由器统一执行 TLS/JWT、能力选择、跨站点发现和 NAT Relay，请改用 [配置 Agent 私有云网络](/openwrt/getting-started/quick-setup)。这不会否定“一 Agent 一 IP”，只是把地址和策略的托管者从 Agent 主机换成 OpenWrt。

## 常见故障

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| `no usable global on-link IPv6 /64` | 没有可用 `/64` 或选错接口 | 明确传入真实接口和规范 `/64` |
| `address must be a global IPv6 address` | 使用了 ULA、回环或文档地址 | 使用真实全球 IPv6 前缀 |
| `host IPv6 address quota is full` | 地址服务配额耗尽 | 停止无用 Agent 或由管理员调整配额 |
| `cannot bind [IPv6]:9443` | 地址不属于主机、端口受限或防火墙策略冲突 | 运行 doctor，检查地址和端口 |
| 远端不可达但本机可调 | 上游未路由、NDP 或主机防火墙未放行 | 从另一主机测试路由和 TCP 连接 |

## 你构建了什么

你已经用一个 SDK 进程创建两个独立 Agent 网络身份，让它们以各自的 IPv6 `/128` 互相调用，并在退出时自动回收地址。继续阅读[为什么每个 Agent 应有一个 IP](../concepts/one-agent-one-ip.md)理解身份边界，或阅读[直接 IPv6 Agent 指南](../guides/direct-ipv6.md)配置固定地址、TLS 和 JWT。
