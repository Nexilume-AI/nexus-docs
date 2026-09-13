---
sidebar_position: 4
title: Windows 一 Agent 一 IPv6
description: 在 Windows 上安装、验证和排查 Host Alias 地址服务。
---

# Windows 一 Agent 一 IPv6

Windows Host Alias 让同一物理网卡承载多个全球 IPv6 `/128`，每个 Python Agent 租用其中一个地址。`NexusAgentAddressd` 以 LocalSystem 服务运行，普通 Agent 通过受 ACL 保护的 Named Pipe 请求租约。

## 前提

- Windows 主机已有真实可用的全球 IPv6 `/64`；
- Python 3.9+；
- 首次安装可以批准 UAC；
- 选择的 TCP 端口不在 Windows/Hyper-V 排除范围内。

## 一条命令配置

从软件包安装：

```powershell
python -m pip install "./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl[windows]"
nexus-agent ipv6 setup
```

从源码仓库安装：

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

`setup` 会发现可用接口和全球 `/64`、选择未被保留的端口、打开 UAC、配置并启动地址服务，然后创建一个受防火墙临时阻断保护的 `/128` Agent 自检。它不会创建永久公网防火墙放行规则。

如果存在多个候选网络，可明确指定：

```powershell
nexus-agent ipv6 setup `
  --interface "Ethernet" `
  --prefix "240e:1234:5678:1200::/64" `
  --port 9443
```

## 验证普通用户路径

首次加入 `Nexus Agent Users` 后注销并重新登录一次，再运行：

```powershell
nexus-agent ipv6 doctor
```

doctor 检查服务配置、服务状态、全球前缀、Named Pipe、当前用户组成员身份和推荐端口。自动化可使用：

```powershell
nexus-agent ipv6 doctor --json
```

## 运行双 Agent 示例

```powershell
$env:NEXUS_IPV6_LAB = '1'
python examples/ipv6_agents_call_each_other.py
```

输出应包含两个不同的全球 IPv6 地址。两个 Agent 可以同时绑定相同端口，因为 Windows 按“地址 + 端口”区分监听。

## 手工服务管理

企业部署需要固定审批流程时，可使用高级服务命令配置接口、前缀和允许用户。通常优先使用 `nexus-agent ipv6 setup`，因为它还会检查保留端口并执行自检。

运行时位于 `C:\ProgramData\Nexus\addressd-runtimes`。LocalSystem 服务不会从安装用户的 `AppData` 导入 SDK 或 pywin32。保护 `C:\ProgramData\Nexus` 下的配置和密钥，只向指定本地组授予 Named Pipe 使用权。

## 常见故障

- doctor 提示当前用户不在组中：注销并重新登录，不要只重开 PowerShell。
- 端口被 Windows/Hyper-V 保留：重新运行 setup 让它选择端口，或检查 `netsh interface ipv6 show excludedportrange protocol=tcp`。
- 没有找到全球 `/64`：确认上游前缀、接口状态和路由；单个 `/128` 不能用于 Host Alias。
- 本机调用成功、远端失败：检查 Windows 防火墙和上游路由。setup 不会永久开放公网端口。

完整调用流程见[两个 IPv6 Agent 互相调用](../tutorials/ipv6-agents-call-each-other.md)。

先完成[安装](../quickstart/installation.md)。源码命令在独立 SDK 仓库根目录执行；wheel 从 GitHub Releases 下载，当前不使用 PyPI 安装本项目。
