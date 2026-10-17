---
title: Relay 流式调用
---

# Relay 流式调用

IPv6 或直接入站访问受限时，可通过 Relay 传递 MCP 流式响应。升级时应同时更新 Cloud runtime adapter、Relay 服务和 OpenWrt agent gateway。客户端同时接受 JSON 和 SSE 时初始化可返回 JSON，工具调用通过 SSE 传递进度和原生 MCP 结果。

消费缓存数据后补充响应 credit，以背压限制排队数据，避免大响应受初始 credit 窗口阻塞。示例 Cloud ingress 响应上限为 1 MiB。请求、单事件大小和超时限制仍然有效；超限会明确失败。更大数据应使用分页、产物分块或认证文件下载。

Agent 心跳为绿色只确认注册/presence，不代表客户端 MCP 初始化和工具调用全部成功。应分别检查 initialize、tools/list 和一个小型 tools/call，保存错误正文并区分额度、上游不可用和传输超时。流式传输不会增加账号额度，也不能恢复上游撤下的模型。

[OpenROAD SDK 示例](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/openroad_mcp_agent) 展示异步任务、进度查询和产物续传。
