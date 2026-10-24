---
title: Agent 集成示例
---

# Agent 集成示例

这些适配器演示如何将原生工具部署为 Nexus Agent。每个目录包含自己的运行依赖、部署说明和限制；SDK 本身不包含模型权重、商业软件许可证或 GPU 驱动。

| 示例 | 用途 |
| --- | --- |
| [Pi](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/pi_chat_agent) | 流式聊天、调用者模型授权与 Attached Computer 工具 |
| [Mobilerun](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/mobilerun_mcp_agent) | 调用者绑定的手机任务、后台进度与交互网页 |
| [OpenEvolve](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/openevolve_mcp_agent) | 模型辅助程序优化 |
| [KernelFoundry](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/kernelfoundry_mcp_agent) | 内核评测与模型辅助优化 |
| [FastVideo](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/fastvideo_mcp_agent) | 蒸馏任务与鉴权权重下载 |
| [DiffSynth-Studio](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/diffsynth_mcp_agent) | LoRA 微调与权重下载 |
| [VBench](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/vbench_mcp_agent) | 视频评测任务与报告 |
| [ChampSim](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/champsim_mcp_agent) | 处理器仿真任务 |
| [Ramulator 2](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/ramulator_mcp_agent) | 存储器仿真任务 |
| [AccelForge](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/accelforge_mcp_agent) | 加速器分析任务 |
| [SST](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/sst_mcp_agent) | 仿真任务 |

## 部署与权限

- 按示例 README 配置自己的路径、运行环境和 Agent 注册信息；不要复制生产凭据。
- 需要模型的 Agent 使用上游模型授权流程，不能默认使用发布者的模型 Key。有效授权只在 Cloud 校验的调用者、Agent 和工作区范围内复用。
- 手机与 Computer 能力取决于调用者绑定的在线设备及 Relay/Runtime 支持；模型授权不会自动授予设备权限。
- Mobilerun 使用 MCP 和 Background/Interactive View；Pi 提供 Chat/Private Display。发布能力决定入口，不要求每个 Agent 都提供聊天页面。
- GPU、原生依赖和模型支持以各示例说明为准。源码发布不代表所有模型都通过完整质量评测；短测试不能证明一般加速收益。

## 长任务与排障

长任务应保留作业 ID，通过事件推送读取进度，并通过鉴权链接获取产物。网络断开不等于任务失败，也不应盲目重试可能产生副作用的设备操作。结束或取消任务后须释放设备占用。

Router 排障应分别记录本地转发、容量等待、首事件、首文本和总耗时。客户端观测的首文本时间包含网络与上游处理，不能直接称为上游排队时间；只有上游提供对应数据时才能进一步区分排队和计算。
