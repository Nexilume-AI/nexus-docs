---
title: OpenROAD MCP 远程 EDA
---

# OpenROAD MCP 远程 EDA

SDK 示例自动发现并注册完整 MCP 工具描述和参数 Schema，支持 OpenROAD/Yosys 交互会话、异步 EDA 任务、RTL 分块上传、阶段进度、增量日志和带 SHA-256 校验的产物下载。

在 Linux Docker 主机部署固定摘要的 MCP 镜像和 SDK 桥接服务，并接入 Nexus OpenWrt Router 所在网络。MCP 容器通过 Unix socket 通信；桥接服务注册 Agent 并请求配对 Router 发布到 Cloud。入站访问受限时使用 Relay，Marketplace 上架单独操作。

长流程先创建项目、上传输入，再启动任务并保存 job ID。轮询阶段和日志，等待产物归档完成后列出、下载文件。客户端断线后继续查询同一个任务，不要重复提交已执行的命令。下载支持认证 Cloud 文件或 MCP 分块传输，并校验大小与 SHA-256。

逻辑综合使用 Yosys Tcl 会话，物理设计使用 OpenROAD Tcl 会话。不要把 Tcl 命令参数拆成多行。不同信任域的设计者使用独立部署，交互式解释器不是多租户隔离边界。

[可部署示例](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/openroad_mcp_agent) 包含 Compose、注册检查、远程流程 CLI、资源限制和备份说明。
