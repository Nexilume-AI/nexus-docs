---
sidebar_position: 1
title: "Tutorial: from echo to a resumable Agent"
---

# Tutorial: from echo to a resumable Agent

Build a `demo.course` Agent with synchronous and SSE handlers, automatic registration and renewal, and a stable-task resumable caller. You will see real events within three steps.

## What you need

- Python 3.9+ with `nexus-openwrt-agent-sdk` installed.
- Completed Router [Quick Setup](/openwrt/getting-started/quick-setup).
- An access JWT with registration and invoke permissions. A one-time transaction token cannot resume.

## Step 1: write the Agent

Save `course_agent.py`:

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

Both decorators for one intent use identical route options. The SDK rejects ambiguous declarations.

## Step 2: run and see registration

```bash
export NEXUS_ROUTER_URL=http://192.168.1.1:7443
export NEXUS_AGENT_TOKEN=replace-with-access-jwt
python course_agent.py
```

The SDK prints the Agent, backend, intent, and published route information. Confirm `demo.course` in LuCI.

## Step 3: invoke the resumable stream

Save `watch_course.py`:

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

for event in client.invoke_stream(envelope, resume=True, max_reconnects=3):
    print(event.event_id, event.event, event.data)
```

```bash
python watch_course.py
```

You should see increasing IDs, three progress events, and a result. The SDK considers the stream complete only after the completion marker.

## Step 4: understand a short disconnect

On a short transport break, the SDK preserves the Envelope, task ID, and last event ID. Gateway and Server return to the first route and emit only later events without re-running the handler.

Do not restart the Agent to test this: resume history is in memory. Use the controlled disconnect cases in `tests/test_resume.py` and `tests/test_sdk.py` for repeatable testing.

## Step 5: observe healthy shutdown

Press Ctrl+C in the Agent terminal. `agent.run()` closes the handle, withdraws leases, and stops listening. A forced process exit falls back to lease expiration.

## What you built

You now have a shared sync/stream capability with renewal, health binding, cleanup, and short-disconnect resume. Continue with [registration lifecycle](../concepts/registration-lifecycle.md) and [streaming design](../concepts/streaming-resume.md).

## Troubleshooting

- Decorator options differ: make every route option for the shared intent identical.
- Resume requires access JWT: do not use a transaction token.
- Disconnect before a numeric event: no safe cursor exists, so the SDK fails instead of redoing work.
- Route miss: check lease, verified tenant/source claims, and Policy RIB.
