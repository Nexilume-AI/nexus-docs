---
sidebar_position: 1
title: 在本机运行第一个 Agent
---

# 在本机运行第一个 Agent

本例只使用本机回环地址，不需要 Router、Cloud 或 IPv6。先完成[安装](installation.md)，保存 `hello_agent.py`：

```python
from nexus_agent import NexusAgentServer

server = NexusAgentServer("127.0.0.1", 9443)

@server.handler("demo.echo")
def echo(envelope):
    return {"message": envelope.payload["message"]}

if __name__ == "__main__":
    try:
        server.serve_forever()
    finally:
        server.server_close()
```

执行 `python hello_agent.py`。在第二个终端激活相同虚拟环境，保存并运行 `call_agent.py`：

```python
import json
from urllib.request import Request, urlopen

request = Request(
    "http://127.0.0.1:9443/invoke",
    data=json.dumps({
        "version": "1.0",
        "intent": "demo.echo",
        "intent_version": 1,
        "task_id": "hello-1",
        "source_agent": "agent://demo/caller",
        "tenant": "demo",
        "hop_limit": 7,
        "payload": {"message": "Hello, Nexus!"},
    }).encode(),
    headers={"Content-Type": "application/vnd.nexus.agent-envelope+json"},
)
with urlopen(request, timeout=10) as response:
    print(json.load(response))
```

预期输出为 `{'message': 'Hello, Nexus!'}`。服务端按 Ctrl+C 退出。本例只监听 `127.0.0.1`；向其他机器开放前需要配置认证和传输安全。

下一步：[连接 OpenWrt](../guides/openwrt-agent.md)、[部署 Hosted MCP](../guides/hosted-mcp.md)，或[配置 Linux IPv6](../guides/linux-ipv6.md)。
