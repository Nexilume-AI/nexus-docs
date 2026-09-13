---
sidebar_position: 2
title: 部署 Hosted MCP Agent
---

# 部署 Hosted MCP Agent

安装 `fastmcp` 扩展后，可以在没有 OpenWrt 的环境运行 MCP：

```python
from nexus_agent import NexusAgent

agent = NexusAgent(runtime="hosted", cloud_name="Echo Agent")

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

if __name__ == "__main__":
    agent.run()
```

`runtime="hosted"` 不发现 Router，不注册边缘租约，也不启动边缘 Agent listener；声明的能力导出为 MCP tools。自管应用可使用 `agent.as_mcp_server()` 集成服务。

## 在 Nexus Cloud 部署同一个文件

使用 [dual_runtime_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/dual_runtime_agent.py)，在 **Agent → Runtime → Upload Python** 上传、构建，再部署验证后的版本。Cloud launcher 在导入前设置 hosted 模式。

Agent 必须在模块顶层声明，`agent.run()` 保留在 `if __name__ == "__main__":` 内。不要在模块导入阶段解析命令行或执行网络操作。显式 `runtime="openwrt"` 的脚本仍只用于边缘；Router 发现失败不会自动切换到 hosted。

部署 Python profile 需要 SDK 0.46.0+ 和 `fastmcp`。额外依赖、模型密钥和资源权限在部署环境配置。Computer/Mobile 声明在成功部署后生效，调用者仍需绑定并授权自己的资源。运行在 Cloud 不会自动取得调用者文件权限。

Plan、Chat、Files、Browser 等通过 `NexusRunContext` 反馈给当前 Run。较长任务应声明 task/continuable，并在外部操作之间检查取消状态；同一份源码不代表边缘实例与 Cloud 实例自动故障切换。
