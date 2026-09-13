---
title: Private Runs and interaction
---

# Private Runs and interaction

A Private Run binds invocation, interactive input, Computer access and output files to the caller. Console provides an Agent Private Display and a standalone per-Run display. Private display content is available only to the caller who owns that Run.

## Start a Run

1. Confirm the Agent Runtime is deployed and healthy, and select Workspace/Project.
2. Open Private Display and select an available task, required Computer/Mobile and files.
3. Confirm scopes and submit. Creation does not mean execution started; the durable Agent worker must accept and advance the task.
4. Inspect state, events, outputs and input requests. Reply using the specific interaction card.
5. After completion, inspect and download outputs as permitted. A shared URL does not replace caller authorization.

## Follow-ups and attachments

Continuable tasks may offer Queue or Steer; use the capabilities returned for the current Run. Messages target the current turn. Accepted submission does not mean the Agent consumed it. Pending, unexpired queued messages can be edited or canceled; refresh after a queue revision change instead of overwriting another edit.

Uploads, Computer imports and output downloads have separate authorization. File references must remain valid and available to this caller/Run. Switching Computer rechecks the target connection and scopes; it does not preserve authority for old directories, terminal tickets or file references.

## Cancel and recover

Use Cancel instead of simply closing the browser. Recovery and resume are explicit actions. When recovery needs confirmation, inspect possible prior external side effects before proceeding. Restarting a worker does not promise automatic replay of every external operation.

## Verification and troubleshooting

- Stuck starting: check Runtime health, execution capacity and `run_agent_tasks`.
- Input required: inspect the current interaction card and [Inbox](../operations/inbox.md).
- File/terminal denied: confirm caller identity, connection health and current scopes; obtain fresh Run credentials.
- Follow-up rejected: check continuability, running state, target turn and queue revision.
- Correlate [Agents](index.md) with [Observability](../operations/observability.md); event summaries are not unlimited raw logs.

Create/list through `agents/{agent_id}/private-runs/`; use `agent-runs/{run_id}/display/`, `events/`, `outputs/`, `follow-ups/`, `cancel/`, `recovery/` and `resume/` under `/api/v1/`. These are separate from public Marketplace demo access.
