---
sidebar_position: 2
title: A2A 集成
---

# A2A 集成

安装可选依赖：

```bash
python -m pip install -e ".[a2a]"
```

`NexusA2AAgent` 把 A2A `AgentExecutor` 暴露为 Nexus 能力，并生成所需的 Agent Card；`NexusA2AClient` 用于普通和流式调用。

```python
from nexus_agent.a2a import NexusA2AAgent

agent = NexusA2AAgent(
    executor,
    router="https://router.example:7443",
    identity="agent://demo/a2a-echo-1",
    endpoint="https://agent.example:9443/invoke",
    tenant="demo",
    host="0.0.0.0",
    port=9443,
    cert_file="agent.crt",
    key_file="agent.key",
    card_url="https://router.example/a2a/cards/echo",
)
agent.expose(skill="echo", intent="demo.a2a.echo")
agent.run()
```

完整服务端和客户端示例见 `examples/a2a_agent.py`、`a2a_call.py` 与 `a2a_stream.py`。

先完成[安装](../quickstart/installation.md)，从 PyPI 安装 nexilume 及对应扩展。源码示例命令在独立 SDK 仓库根目录执行。
