---
sidebar_position: 2
title: 如何接入 OpenWrt IPv6 Agent
---

# 如何接入 OpenWrt IPv6 Agent

接入后，Nexus Agent 可以选择用户自有的 OpenWrt IPv6 运行节点，不必创建或租用 Docker 容器。

## 前置条件

- Router 已安装 Nexus OpenWrt 组件并拥有全球单播 IPv6。
- Server 对 Router 可达，生产环境已配置设备 CA、边缘签名密钥和反向代理 mTLS。
- 你是目标租户管理员。

## 操作步骤

1. 在 Nexus Console 的 Agent 运行时区域创建一次性配对码。配对码默认用于一个租户和可选项目，且只能兑换一次。
2. 在 OpenWrt 的云端连接页填写 Server 地址与配对码。推荐选择**托管设备证书**：Router 本地生成私钥和 CSR，Server 只返回签发证书，不传输设备私钥。
3. 等待 Router 发布 Agent 注册。Server 只接受数字形式的全球 IPv6、可信 TLS server name、允许的端口和单调递增 generation。
4. 在 **Agents** 中创建或打开 Agent，选择 **OpenWrt IPv6**，再选择未绑定的注册。
5. 执行运行时健康检查或 MCP 调用。云端会按 IPv6 连接，同时用注册的 TLS server name 完成 SNI 与主机名验证。

## 验证

- **Edge nodes** 显示设备在线且证书已确认。
- **Available registrations** 中目标注册消失，并出现在 Agent 的 active deployment。
- Agent 状态页显示 `runtime_type=openwrt_ipv6`，没有 container id。

## 排错

- 注册被拒绝：确认地址不是 ULA、链路本地地址或文档地址。
- TLS 失败：确认 `ca_bundle_id` 已映射到 Server 本地 CA 文件，证书 SAN 包含 `tls_server_name`。
- `mTLS required`：生产反向代理必须删除客户端自带的证书指纹头，只在验证设备证书后写入该头。
- 注册过期：检查 Router 的续租、系统时间和到 Server 的出站连接。

Router 侧步骤见 [OpenWrt 快速配置](/openwrt/getting-started/quick-setup)；完整安全配置见[配置参考](../reference/configuration.md)。
