---
sidebar_position: 1
title: SDK 诊断
---

# SDK 诊断

诊断脚本默认不发起网络请求，只报告 Python、SDK、可选集成和环境变量是否存在。它不会打印令牌或客户端密钥的值。

## 运行本地检查

```bash
python docs-site/static/downloads/nexus-sdk-diagnostics.py
```

## 检查路由器 DNS 和 TCP

```bash
python docs-site/static/downloads/nexus-sdk-diagnostics.py \
  --router https://router.example:7443 --connect
```

`--connect` 只建立 TCP 连接，不发送 HTTP 请求或凭据。它不能证明 TLS、认证、授权或 Agent 路由正常。

## 输出中应关注

- `nexus_agent` 是否可导入及其版本。
- `fastmcp`、`a2a`、`win32api` 是否与使用场景匹配。
- `NEXUS_ROUTER_URL`、`NEXUS_AGENT_TOKEN` 等是否“已设置”；脚本不会显示值。
- DNS 解析是否返回预期地址，TCP 是否在超时内建立。

分享输出前仍应人工检查主机名、用户名和网络地址是否属于敏感信息。
