---
sidebar_position: 1
title: 命令行与环境变量
---

# 命令行与环境变量

## 命令

| 命令 | 用途 |
| --- | --- |
| `nexus-agent` | Windows IPv6 `setup` 与 `doctor` |
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
