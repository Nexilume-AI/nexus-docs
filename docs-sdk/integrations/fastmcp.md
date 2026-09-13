---
sidebar_position: 1
title: FastMCP 集成
---

# FastMCP 集成

安装可选依赖：

```bash
python -m pip install -e ".[fastmcp]"
```

`FastMCPBridge` 枚举工具、验证显式映射、把异步结果转换为 Nexus JSON，并负责能力注册与续租。

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

每个对外工具都应显式映射，不要自动暴露整个 MCP 服务。完整示例见 `examples/fastmcp_agent.py`。

先完成[安装](../quickstart/installation.md)。源码命令在独立 SDK 仓库根目录执行；wheel 从 GitHub Releases 下载，当前不使用 PyPI 安装本项目。

无需 Router 的部署见 [Hosted MCP](../guides/hosted-mcp.md)。本页的 bridge 负责连接现有 FastMCP 与 OpenWrt。
