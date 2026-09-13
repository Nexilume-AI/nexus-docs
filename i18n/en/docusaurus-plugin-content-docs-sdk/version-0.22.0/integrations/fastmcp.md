---
sidebar_position: 1
title: FastMCP integration
---

# FastMCP integration

Install the optional dependency:

```bash
python -m pip install -e ".[fastmcp]"
```

`FastMCPBridge` enumerates tools, validates explicit mappings, converts asynchronous results to Nexus JSON, and manages registration and renewal.

```python
from nexus_agent import CapabilityRegistration, NexusAgentClient, NexusAgentServer
from nexus_agent.fastmcp import FastMCPBridge

bridge = FastMCPBridge(
    mcp,
    NexusAgentServer("0.0.0.0", 9443, cert_file="agent.crt", key_file="agent.key"),
    {
        "lint_verilog": CapabilityRegistration(
            intent="chip.verilog.verify.lint",
            origin="agent://demo/fastmcp-linter",
            endpoint="https://agent.example:9443/invoke",
            tenant="demo",
        )
    },
)
bridge.serve_registered(NexusAgentClient("https://router.example:7443"))
```

Map every public tool explicitly instead of exposing the whole MCP server. See `examples/fastmcp_agent.py` for a complete example.
