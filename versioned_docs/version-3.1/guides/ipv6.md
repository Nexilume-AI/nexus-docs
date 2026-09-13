---
sidebar_position: 3
title: 配置 IPv6 访问
---

# 配置 IPv6 访问

IPv6 可让 Agent 在不同网段间获得稳定、可路由的地址，但“可路由”不等于“可公开访问”。生产环境必须同时配置认证和最小化防火墙规则。

## 路由器侧检查

1. 在 OpenWrt **网络 → 接口** 中确认 LAN 获得全局 IPv6 前缀。
2. 确认目标主机获得全局单播地址，而不只是 `fe80::/10` 链路本地地址。
3. 在 **Agent Router → 高级设置** 中启用所需 IPv6 监听。
4. 仅对预期源地址和端口放行防火墙。
5. 从另一网段测试 TCP 连通性，再测试 Agent 调用。

## Windows Agent

Windows 主机可使用 SDK 的 IPv6 配置命令选择地址、端口并运行诊断。参见 [Windows IPv6 指南](/sdk/guides/windows-ipv6)。

## 安全清单

- 使用 TLS 并验证服务端身份。
- 启用令牌或 OIDC，不允许匿名管理接口。
- 不向互联网暴露 LuCI、ubus 或内部诊断端口。
- 配置租约和密钥轮换，并保留撤销路径。
