---
sidebar_position: 1
title: SDK 常见错误
---

# SDK 常见错误

## 找不到路由器

设置 `NEXUS_ROUTER_URL`，并确认主机能解析或访问该地址。自动发现失败不代表路由器服务异常，可能只是 mDNS 或默认网关不符合预期。

## `NexusAuthenticationError`

令牌缺失、过期或签名不被接受。确认 `NEXUS_AGENT_TOKEN`、签发方、受众和设备时间。

## `NexusAuthorizationError`

身份认证成功，但租户、能力或操作不在授权范围内。不要通过扩大所有权限来绕过，应修正策略或使用正确身份。

## TLS 验证失败

确认 URL 主机名与证书 SAN 匹配，并使用正确 CA。IP 地址直连时，证书也必须包含该 IP 身份，或使用证书覆盖的 DNS 名称。

## Agent 注册后很快消失

检查续租线程是否仍在运行、进程是否被阻塞、路由器时间是否正确，以及网络是否周期性中断。正常退出应撤销租约；崩溃则等待租约超时。
