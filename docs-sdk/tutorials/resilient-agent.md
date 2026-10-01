---
sidebar_position: 1
title: 教程：从 Echo 到可恢复 Agent
---

# 教程：从 Echo 到可恢复 Agent

你将构建一个同时支持同步和 SSE 的 `demo.course` Agent，启动后自动注册与续租，再用稳定 task ID 调用可恢复流。前三步内会看到真实事件。

## 你需要

- Python 3.9+ 和已安装的 `nexilume`；
- 完成 Router [快速配置](/openwrt/getting-started/quick-setup)；
- 有注册和调用权限的 access JWT；可恢复流不能使用一次性 transaction token。

## 第 1 步：编写 Agent

保存为 `course_agent.py`：

```python
import time

from nexus_agent import NexusAgent, SseEvent

agent = NexusAgent(
    router="auto",
    tenant="demo",
    agent_id="course-agent",
    advertise_address="auto",
)

@agent.capability("demo.course", trust=60, latency_ms=20)
def run_once(payload):
    return {"mode": "sync", "input": payload}

@agent.stream_capability("demo.course", trust=60, latency_ms=20)
def run_stream(payload):
    for step in range(1, 4):
        time.sleep(0.2)
        yield SseEvent(event="progress", data=f"step {step}/3")
    yield SseEvent(event="result", data=str({"input": payload}))

if __name__ == "__main__":
    agent.run()
```

同步与流式装饰器对同一 intent 使用完全相同的路由选项，否则 SDK 会拒绝含糊声明。

## 第 2 步：运行并看到注册结果

```bash
export NEXUS_ROUTER_URL=http://192.168.1.1:7443
export NEXUS_AGENT_TOKEN=replace-with-access-jwt
python course_agent.py
```

SDK 会打印 Agent、backend、intent、route ID/公共地址等发布信息。在 LuCI 中确认 `demo.course` 路由存在。

## 第 3 步：调用可恢复流

保存为 `watch_course.py`：

```python
import os

from nexus_agent import NexusAgentClient

client = NexusAgentClient(
    os.environ["NEXUS_ROUTER_URL"],
    token=os.environ["NEXUS_AGENT_TOKEN"],
)

envelope = {
    "version": "1.0",
    "intent": "demo.course",
    "intent_version": 1,
    "task_id": "course-demo-001",
    "source_agent": "agent://demo/course-caller",
    "tenant": "demo",
    "hop_limit": 8,
    "constraints": {},
    "payload": {"chapter": "routing"},
}

for event in client.invoke_stream(
    envelope,
    resume=True,
    max_reconnects=3,
):
    print(event.event_id, event.event, event.data)
```

运行：

```bash
python watch_course.py
```

你会看到递增事件 ID、三个 progress 和一个 result。SDK 只有在收到 completion marker 后才认为流正常完成。

## 第 4 步：理解短断线行为

若调用方与 Router 之间发生短暂传输中断，SDK 会保留同一 Envelope、task ID 和最后事件 ID，最多重连三次。Gateway 和 Server 会回到首次 route，并只发送游标之后的事件，handler 不重新执行。

不要通过重启 Agent 测试这个特性：恢复历史在内存中，进程重启后应得到 task not found。要做可重复的自动测试，请运行仓库 `tests/test_resume.py` 和 `tests/test_sdk.py` 中的断线场景。

## 第 5 步：观察健康下线

在 Agent 终端按 Ctrl+C。`agent.run()` 会关闭 handle、撤销 lease 并停止监听。LuCI 中路由应消失；若进程被强制终止，则由 lease 到期兜底。

## 你构建了什么

你现在有一个同步/流式共用能力、自动续租、健康绑定、正常清理和短断线恢复的 Agent。接下来阅读[注册、续租与自愈](../concepts/registration-lifecycle.md)和[流式恢复原理](../concepts/streaming-resume.md)。

## 常见问题

- 装饰器报选项不同：确保同一 intent 的 public IPv6、版本、region、租期和指标完全一致。
- 可恢复流要求 access JWT：不要使用 transaction token。
- 没有事件 ID 就断开：SDK 无安全游标，会明确失败而不是重做任务。
- 404 route miss：检查 lease、tenant/source claims 和 Policy RIB。
