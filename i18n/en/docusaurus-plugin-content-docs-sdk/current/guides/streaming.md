---
sidebar_position: 2
title: Implement streaming calls
---

# Implement streaming calls

Streaming capabilities send incremental SSE events and suit generation, compilation, and analysis tasks.

## Server

```python
from nexus_agent import NexusAgent, SseEvent

agent = NexusAgent(tenant="demo", agent_id="worker")

@agent.stream_capability("demo.long-task")
def run(payload):
    yield SseEvent(event="progress", data="started")
    yield SseEvent(event="result", data='{"ok": true}')
```

Every stream should end in an explicit success or error state. Keep event data bounded instead of putting a large file in one SSE event.

## Client

Use the streaming interface on `NexusAgentClient` and iterate over `SseEvent` objects. Set connection and task timeouts, and distinguish network interruption, authentication failure, and business errors.

Use a resume identifier only when both sides support the resume protocol. If resumption fails, do not blindly repeat work with side effects; use an idempotency key or query task state first.
