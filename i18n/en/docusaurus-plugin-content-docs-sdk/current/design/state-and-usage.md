---
title: State, recovery, usage and billing
sidebar_position: 4
---

# State, recovery, usage and billing

## Give each state mechanism one job

| API | Stores | Does not guarantee |
| --- | --- | --- |
| `ctx.memory` | Reusable caller/workflow facts | Process checkpoints or secret storage |
| `ctx.checkpoint` | Task stage and small recovery data | Rollback of external effects |
| `ctx.recovery` | Managed operation/replay records | Exactly-once behavior in an external service without idempotency |
| Reporting outbox | Undelivered Run events | Complete business execution state |

`memory.add()` returns an event-submission bool; `recall()` returns `NexusMemoryItem` objects. Update/delete require revision. On `NexusMemoryConflict`, read again and merge rather than overwriting unseen changes. Set consent, sensitivity and license deliberately; a model suggestion is not user consent.

## Checkpoint

Inside a handler with a real Cloud Run:

```python
previous = ctx.checkpoint.load()
checkpoint = ctx.checkpoint.save(
    stage="validated", data={"schema_version": 1},
    revision=previous.revision if previous else None,
)
```

Returns `NexusCheckpoint` with stage/data/revision/updated_at. Data is limited to 64 KiB. Store stages and references, not large files, tokens or model client objects. Your application decides how to resume each stage.

## External effects and recovery

`ctx.recovery.call(operation_type, request, callback, can_reconcile=...)` passes a stable idempotency key to the callback and can reuse recorded successful results. Declare reconcilability only when the external service and your implementation support deduplication or querying the outcome.

`external_operation(...)` returns a context manager. Check operation.execute, then call operation.complete(result) after success. Pause to reconcile unknown outcomes instead of blindly repeating a payment, message or write. `NexusRecoveryDiverged` means replay requests disagree with the recorded workflow.

## Model selection and actual usage

Declare supported `NexusExecutionProfile` objects in `McpToolDescriptor.execution_profiles`. Read the selected profile from `ctx.execution`; the SDK does not call that model for you. Declare only models, reasoning efforts and context windows supported by your deployment.

This fragment assumes `response` is an actual response from your model client:

```python
ctx.usage.report(
    model=response.model,
    input_tokens=response.usage.input_tokens,
    output_tokens=response.usage.output_tokens,
    context_window=ctx.execution.context_window,
    event_id="model-call-1",
)
```

Adapt provider-specific field names. context_window must be a known positive integer. Never estimate token counts. Retried reporting of one call keeps its event_id; new calls get new ids. `ctx.usage.gateway_headers()` attributes Nexus model-gateway calls to a Run and contains short-lived credentials: do not log or return it.

## Billing and observability

`ctx.billing.report` reports business charges; `ctx.usage.report` reports model tokens. Check enabled and respect Run currency/budget policy. Amounts use Decimal, integers or strings; see the exact signature and `NexusBillingLineItem` fields.

Use a private persistent outbox directory. After reconnection, `ctx.replay_pending()` resends events for the same active Run. Inspect `ctx.report()` delivery counters. An outbox cannot reopen a completed/fenced Run, and buffered does not mean delivered.

See [reporting API](../reference/modules/reporting.md) for methods, fields and errors, and [models API](../reference/modules/models.md) for execution profiles.
