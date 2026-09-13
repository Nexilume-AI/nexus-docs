---
sidebar_position: 1
title: 命令行与环境变量
---

# 命令行与环境变量

## 命令

| 命令 | 用途 |
| --- | --- |
| `nexus-agent` | Linux / Windows IPv6 `setup` 与 `doctor` |
| `nexus-agent-security` | 安装和解析安全描述文件 |
| `nexus-agent-addressd` | Unix 地址辅助守护进程 |
| `nexus-agent-addressd-service` | Windows 地址辅助服务 |

使用 `COMMAND --help` 查看当前版本的完整参数。

## 常用环境变量

| 变量 | 用途 |
| --- | --- |
| `NEXUS_ROUTER_URL` | 路由器网关 URL |
| `NEXUS_AGENT_TOKEN` | 默认访问令牌 |
| `NEXUS_AGENT_ADDRESS` | Agent 对外发布地址 |
| `NEXUS_AGENT_IPV6` | IPv6 地址兼容配置 |
| `NEXUS_AGENT_CLIENT_ID` | OIDC 客户端 ID |
| `NEXUS_AGENT_CLIENT_SECRET` | OIDC 客户端密钥 |
| `NEXUS_AGENT_SECURITY_PROFILE` | 安全描述文件路径 |
| `NEXUS_AGENT_ADDRESSD_SOCKET` | Unix addressd socket |
| `NEXUS_AGENT_ADDRESSD_PIPE` | Windows addressd named pipe |

兼容变量 `NEXUS_JWT`、`NEXUS_AGENT_JWT` 与 `NEXUS_TOKEN` 仍可读取，但新部署应统一使用 `NEXUS_AGENT_TOKEN`。

## Computer Runtime and hosted mode

| Command / variable | 用途 |
| --- | --- |
| `nexus-computer setup/status/logs/repair/restart/update/unpair` | 配对、状态与服务管理；使用 `--help` 查看参数 |
| `NEXUS_AGENT_RUNTIME_MODE` | 可信 launcher 在导入前选择 hosted 模式 |
| `NEXUS_BROWSER_EXECUTABLE` | 实际浏览器可执行文件路径 |
| `NEXUS_BROWSER_HEADLESS` | 无桌面 Linux 设置为 true |
| `NEXUS_AGENT_OUTBOX_DIR` | 可选的私有持久事件缓冲目录 |

[Computer Runtime 配置](../guides/computer-runtime.md)；[Linux IPv6 setup](../guides/linux-ipv6.md)。
