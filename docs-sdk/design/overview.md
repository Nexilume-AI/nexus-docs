---
title: 用 SDK 设计 Agent
sidebar_position: 0
---

# 用 SDK 设计 Agent

设计 Agent 时，先明确输入、输出和允许执行的动作，再选择运行位置。SDK 负责协议、身份、路由和 Run 资源访问；你的业务代码负责模型调用、校验、决策与外部操作的幂等性。

## 从需求到接口

以“检查用户提交的文档”为例：第一版只返回字符、词和行数；第二版增加进度；之后才增加文件上传、人工确认或操作 Computer。不要一开始就把整个工作目录和任意命令暴露成一个工具。

| 设计问题 | SDK 中的对应概念 |
| --- | --- |
| Agent 做什么 | `@agent.capability` 的 intent 与业务函数 |
| 调用者如何填写输入 | `McpToolDescriptor.input_schema`；业务层仍需校验 |
| 给模型展示什么 | tool name、description、输入 schema |
| 一次调用返回什么 | JSON 可序列化结果；流式调用使用 `SseEvent` |
| 在哪里运行 | OpenWrt 注册、hosted MCP 或直接 IPv6 |
| 是否需要调用者资源 | Computer/Mobile 声明与调用者授权 |
| 如何反馈工作过程 | `NexusRunContext` 的 Plan、Trace、Chat、Output |
| 如何恢复中断 | Checkpoint、Recovery 与业务幂等键 |

## 推荐学习顺序

1. [声明并测试第一个业务 Agent](capabilities.md)：完整可下载示例。
2. [设计交互与长任务](interaction.md)：Plan、Chat、流式、后续输入与取消。
3. [使用调用者资源](resources.md)：区分 Run 文件、Computer 工作区、浏览器和 Mobile。
4. [状态、恢复与成本](state-and-usage.md)：Memory、Checkpoint、外部操作、用量与计费。
5. [完整接口参考](../reference/coverage.md)：参数、类型、返回值、字段与源码定位。

## 选运行方式

| 方式 | 适用场景 | 前提 |
| --- | --- | --- |
| `NexusAgentServer` | 本机验证 HTTP/SSE 或集成现有服务 | Python，无需 Cloud |
| `NexusAgent(runtime="openwrt")` | 局域网服务、Router 注册和跨网调用 | 可达的 Agent Access Proxy |
| `NexusAgent(runtime="hosted")` | 自管 MCP 或 Cloud 容器 | `fastmcp` 扩展；Cloud 能力需要可信 Run |
| `NexusAgent.public_ipv6(...)` | 已知地址的直接调用 | 可用 IPv6 与认证配置 |

`runtime="auto"` 默认走边缘流程，可信 Cloud launcher 可在导入前选择 hosted。Router 发现失败不会变成 hosted。业务函数、Agent 声明放在模块顶层，`agent.run()` 放在 `__main__` guard 内，才能复用同一个上传文件。

## 三层验证

先用普通单元测试验证业务函数；再测试实际 HTTP/MCP 工具调用；最后到真实 Cloud Run 验证授权、资源和重启恢复。没有 Cloud 的本机测试无法证明 Caller Computer、计费或 Mobile 可用。SDK 不自动提供模型、模型密钥或外部系统的写入权限。
