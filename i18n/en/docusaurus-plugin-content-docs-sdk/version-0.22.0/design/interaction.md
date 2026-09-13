---
title: Interaction, streaming and long tasks
sidebar_position: 2
---

# Interaction, streaming and long tasks

Separate transport from lifecycle: SSE carries output; MCP Tasks and Cloud Runs manage work. An HTTP disconnect does not prove that a remote effect stopped.

## Progress and results

| API | Meaning | Result and caveat |
| --- | --- | --- |
| `ctx.plan.set/update` | Visible steps and status | bool reports submission, not business success |
| `ctx.trace.step/tool` | Step/tool context manager | Record a summary with `call.result(...)` |
| `ctx.chat.say` | Send text to the current Run | Does not call a model |
| `ctx.shell.write` | Display terminal output | Does not execute commands; use `ctx.terminal.run` |
| `ctx.report()` | Delivery statistics | Inspect failed/dropped/pending/buffered |

Do not put credentials, entire private files or hidden model reasoning into traces. Async handlers can use `await ctx.aio.plan.set(...)`; consult the reference because not every synchronous helper has an aio equivalent.

## Ask for confirmation

Declare `McpToolDescriptor(task=True, chat=True, interactive=True, continuable=True, ...)` for an interactive capability. Inside its handler, with a real interactive Run:

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

`NexusChatReply` contains value, text and interaction_id. Handle `NexusChatTimeout` and `NexusChatUnavailable` separately; a timeout is not approval. Keep interaction keys stable across replay.

## Stream business output

```python
from nexus_agent import SseEvent

@agent.stream_capability("document.progress")
def progress(payload):
    yield SseEvent(data="validating", event="progress")
    yield SseEvent(data='{"ok": true}', event="result")
```

This fragment requires an existing `agent`. Ordinary invoke results and SSE events use different APIs; see [streaming](../guides/streaming.md). Recovery reuses task_id and event cursors. Expired history, process replacement and single-use transaction tokens limit recovery.

## Long tasks, cancellation and follow-up

Call `ctx.raise_if_cancelled()` between external actions, or `await ctx.aio.raise_if_cancelled()`. Let cancellation propagate to the runtime rather than swallowing it and continuing.

Opt in with `follow_up="steer_and_queue"` on the capability, then read guidance at application-defined safe points:

```python
for instruction in ctx.inbox.receive_pending():
    # Apply instruction.content to application state before acknowledging.
    instruction.acknowledge()
```

Replace the comment with actual processing; do not acknowledge and discard input. For attachments, first configure `ctx.inbox.configure("steer_and_queue", attachments=True)`, process attachments/files, then acknowledge. Use `instruction.reject()` when input cannot be accepted. Deduplicate by message id because delivery can repeat before acknowledgement.

Complete example: [router_follow_up_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/router_follow_up_agent.py). See [reporting](../reference/modules/reporting.md), [inbox](../reference/modules/inbox.md) and [direct tasks](../reference/modules/client.md) for signatures and results.
