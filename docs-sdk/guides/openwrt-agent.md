---
sidebar_position: 1
title: 连接 OpenWrt Agent
---

# 连接 OpenWrt Agent

前提：已配置 Nexus OpenWrt，启用 Agent 服务，且本机可以访问 Agent Access Proxy。先完成[安装](../quickstart/installation.md)，在源码仓库根目录运行：

```sh
python examples/router_echo_agent.py --router http://192.168.246.1:7446 --self-test
```

替换为实际 Proxy 地址。示例完成注册、调用和退出清理。默认 `--auth auto` 使用路由器支持的 LAN 认证或环境中的凭据；`--auth none` 只适用于明确关闭 JWT 的隔离 LAN 入口。

编写自己的 Agent：

```python
from nexus_agent import NexusAgent

agent = NexusAgent(router="auto", tenant="demo", agent_id="echo-server")

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

if __name__ == "__main__":
    agent.run()
```

SDK 管理注册、续租和正常退出清理。发现失败时设置 `NEXUS_ROUTER_URL`；多网卡机器可用 `NEXUS_AGENT_ADDRESS` 指定路由器实际可达的后端地址。连接配置好的 Access Proxy，不要连接内部 loopback gateway。

认证可使用 `NEXUS_AGENT_TOKEN`，或配置 OIDC 的 `NEXUS_AGENT_CLIENT_ID` 与 `NEXUS_AGENT_CLIENT_SECRET`。将凭据放入运行环境，不要写进上传的 Python 文件。
