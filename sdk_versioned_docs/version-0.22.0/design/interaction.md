---
title: 交互、流式与长任务
sidebar_position: 2
---

# 交互、流式与长任务

先区分“传输正在输出”与“业务仍在运行”：SSE 是输出通道，MCP Task/Cloud Run 是任务生命周期。HTTP 断开不证明远端操作已取消。

## 进度与结果

| 接口 | 意义 | 返回与注意事项 |
| --- | --- | --- |
| `ctx.plan.set/update` | 用户可见的步骤与状态 | bool 表示反馈提交结果，不是业务操作成功 |
| `ctx.trace.step/tool` | 步骤/工具上下文管理器 | 用 `call.result(...)` 记录结果摘要 |
| `ctx.chat.say` | 向当前 Run 发送文本 | 不是调用模型 |
| `ctx.shell.write` | 展示终端输出 | 不执行 shell；实际执行是 `ctx.terminal.run` |
| `ctx.report()` | 事件投递统计 | 检查 failed/dropped/pending/buffered |

不要把密钥、完整私人文件或模型内部推理当成 Trace 内容。异步 handler 中可以使用 `await ctx.aio.plan.set(...)` 等异步接口；具体异步接口以参考为准，不是所有同步 helper 都有 aio 对应物。

## 人工确认

在需要用户选择的能力声明中配置 `McpToolDescriptor(task=True, chat=True, interactive=True, continuable=True, ...)`。下面是 handler 内部片段，需要真实的交互 Run：

```python
reply = ctx.chat.ask(
    "Create the report?", key="confirm-report",
    choices=[{"value": "yes", "label": "Create"},
             {"value": "no", "label": "Cancel"}],
)
if reply.value != "yes":
    return {"status": "cancelled"}
ctx.raise_if_cancelled()
```

`NexusChatReply` 包含 value/text/interaction_id 等字段。超时与无可用交互上下文分别使用 `NexusChatTimeout`、`NexusChatUnavailable`。不要把超时当同意。重复运行时保持交互 key 稳定。

## 流式业务

```python
from nexus_agent import SseEvent

@agent.stream_capability("document.progress")
def progress(payload):
    yield SseEvent(data="validating", event="progress")
    yield SseEvent(data='{"ok": true}', event="result")
```

此片段依赖已声明的 `agent`。普通 invoke 的返回和 SSE 的事件不是同一个接口；详见[流式指南](../guides/streaming.md)。客户端恢复复用 task_id 和事件游标；过期历史、进程重启或一次性 transaction token 不能当作无限恢复承诺。

## 长任务、取消与后续消息

每次外部动作前后调用 `ctx.raise_if_cancelled()`；异步使用 `await ctx.aio.raise_if_cancelled()`。取消异常应传播到运行时，不要吞掉后继续执行。

需要用户引导当前工作时，能力显式声明 `follow_up="steer_and_queue"`，并在应用定义的安全点读取：

```python
for instruction in ctx.inbox.receive_pending():
    # Apply instruction.content to application state before acknowledging.
    instruction.acknowledge()
```

示例中的注释必须替换成业务处理；不能直接复制后丢弃消息。需要附件时先 `ctx.inbox.configure("steer_and_queue", attachments=True)`，处理 `instruction.attachments/files` 后再确认；无法接受时 `instruction.reject()`。确认前可能重投，按消息 id 去重。

完整可用例子：[router_follow_up_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/router_follow_up_agent.py)。签名与返回见 [reporting](../reference/modules/reporting.md)、[inbox](../reference/modules/inbox.md)、[direct tasks](../reference/modules/client.md)。
