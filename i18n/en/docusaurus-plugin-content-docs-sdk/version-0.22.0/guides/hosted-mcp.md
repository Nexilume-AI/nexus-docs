---
sidebar_position: 2
title: Deploy a hosted MCP agent
---

# Deploy a hosted MCP agent

Install the `fastmcp` extra. Set `runtime="hosted"` to run without OpenWrt discovery or registration:

```python
from nexus_agent import NexusAgent

agent = NexusAgent(runtime="hosted", cloud_name="Echo Agent")

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

if __name__ == "__main__":
    agent.run()
```

For a Nexus Cloud deployment, use [dual_runtime_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/dual_runtime_agent.py): upload the file through **Agent > Runtime > Upload Python**, build it, and deploy the verified version. The Cloud launcher selects hosted mode and exports the tools over MCP. Keep the agent at module scope and `agent.run()` behind the `__main__` guard.

The deployment's Python profile must include SDK 0.46.0+ and the `fastmcp` extra. Model credentials, additional dependencies and resource permissions must be configured in that deployment. Hosted mode alone does not grant access to a caller's files or computer.
