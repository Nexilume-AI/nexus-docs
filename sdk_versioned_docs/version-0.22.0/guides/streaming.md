---
sidebar_position: 2
title: 实现流式调用
---

# 实现流式调用

流式能力通过 SSE 逐步发送事件，适合生成、编译、分析等耗时任务。

## 服务端

```python
from nexus_agent import NexusAgent, SseEvent

agent = NexusAgent(tenant="demo", agent_id="worker")

@agent.stream_capability("demo.long-task")
def run(payload):
    yield SseEvent(event="progress", data="started")
    yield SseEvent(event="result", data='{"ok": true}')
```

每个流最终应产生明确的成功或错误终态。事件数据应保持有界，避免把大文件直接塞入单个 SSE 事件。

## 客户端

使用 `NexusAgentClient` 的流式调用接口迭代 `SseEvent`。为连接和任务设置超时，并区分网络中断、认证失败和服务端业务错误。

只有双方都支持恢复协议时才保存并发送恢复标识。恢复失败时，不要无条件重复有副作用的任务；应使用业务幂等键或先查询任务状态。
