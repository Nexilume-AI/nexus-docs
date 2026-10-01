---
sidebar_position: 2
title: A2A integration
---

# A2A integration

Install the optional dependency:

```bash
python -m pip install -e ".[a2a]"
```

`NexusA2AAgent` exposes an A2A `AgentExecutor` as a Nexus capability and produces its Agent Card. `NexusA2AClient` supports normal and streaming calls.

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

See `examples/a2a_agent.py`, `a2a_call.py`, and `a2a_stream.py` for complete server and client examples.

Complete [installation](../quickstart/installation.md) first, using nexilume and the relevant extras from PyPI. Source examples run at the standalone SDK repository root.
