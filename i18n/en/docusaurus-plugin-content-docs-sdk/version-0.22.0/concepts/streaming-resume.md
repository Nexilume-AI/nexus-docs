---
sidebar_position: 4
title: Why streams resume without re-executing
---

# Why streams resume without re-executing

A network reconnect must not become a new task. Resumable streaming separates the business producer from one HTTP connection. A connection may disappear while the producer continues to create numbered events; the replacement starts after the last acknowledged cursor.

## The first call establishes four facts

1. a stable, non-empty task ID;
2. tenant, source Agent, and intent identity scope;
3. a request fingerprint that prevents changing work under the same ID;
4. the first selected route ID, which resume does not reselect.

The Server assigns increasing numeric IDs starting at 1 and emits `: nexus-stream-complete` after normal completion. The caller advances its cursor only after receiving a complete event.

```mermaid
sequenceDiagram
  participant C as Client
  participant G as Gateway
  participant S as Agent Server
  C->>G: task=T, cursor=0
  G->>S: fixed route R
  S-->>C: id:1, id:2
  Note over C,S: connection breaks; producer continues
  C->>G: task=T, Last-Event-ID:2
  G->>S: same route R
  S-->>C: id:3 ... completion
```

## SDK resume algorithm

`invoke_stream(..., resume=True)` requires a task ID. It tracks the last numeric event ID. On transport failure or a missing completion marker, it resends the same Envelope up to `max_reconnects`, using both HTTP `Last-Event-ID` and `resume_from_event_id`. SSE retry hints can adjust delay.

Without any numeric event ID, the client has no safe cursor. Non-numeric or non-increasing IDs also fail explicitly instead of silently duplicating or reordering data.

## Why transaction tokens cannot resume

A transaction token is one-time. Reusing it during reconnect is token replay, so the SDK rejects resumable reconnect when configured with one. Use an access JWT.

## Explicit boundaries

- missing task or restarted process: 404;
- changed request under one task ID: `STREAM_TASK_CONFLICT`;
- cursor beyond last event: `INVALID_RESUME_CURSOR`;
- first route unavailable: `RESUME_ROUTE_UNAVAILABLE`;
- retained history too old: `EVENT_HISTORY_EXPIRED`.

History has task, event, byte, and retention limits and lives in memory. It solves short disconnects, not durable workflow execution.

Resume avoids handler re-execution and is safer than issuing a fresh invoke. Cross-restart work needs persistent task state rather than blind retry.

Complete [Build a resilient Agent](../tutorials/resilient-agent.md) and see [Streaming calls](../guides/streaming.md).
