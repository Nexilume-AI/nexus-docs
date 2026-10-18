---
title: Background jobs and push events
---

# Background jobs and push events

New Atrex jobs return `job_id` and `view_url`. The isolated execution container runs independently of the original MCP request. Disconnecting a client does not cancel the task.

## Live page

Sign in to Cloud as the initiating credential owner and open `view_url`. The flat page shows state, elapsed time, model request counts, an execution timeline, live output and artifact downloads. Reference measurement and optimizer stages come from actual Worker output. No completion percentages or speedups are inferred; use the official report artifacts to assess performance.

The page receives events over SSE without periodically calling `get_atrex_job`. Reconnection replays events after the last received sequence. Cancellation is explicit; closing the page does not cancel execution. Downloads become available after execution and verified upload. Failed or cancelled tasks may also retain outputs.

## MCP stream subscription

Call `watch_atrex_job` with project credentials, `job_id` and `after` (initially 0). Clients must accept SSE and supply `_meta.progressToken` in MCP `tools/call` parameters:

```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "watch_atrex_job",
    "arguments": {
      "project_id": "<project-id>",
      "access_key": "<private-project-key>",
      "job_id": "<job-id>",
      "after": 0
    },
    "_meta": {"progressToken": "watch-42"}
  }
}
```

Cloud forwards `notifications/progress`. The `progress` value is an event sequence; `message` contains event JSON with `kind`, `data` and `time`, not a completion percentage. A subscription lasts up to 45 seconds. Resume with the last received sequence after completion or interruption; do not resubmit optimization to reconnect. The returned `after` value can seed the next subscription.

JSON-only clients receive a snapshot and `view_url`; open the page for continuous push updates. `get_atrex_job` still provides snapshots and saved log pages, and `read_atrex_artifact` still supports paged MCP downloads. This implementation does not advertise the MCP Tasks subscription extension.

## Delivery and recovery

- MCP tool calls continue through existing OpenWrt / Cloud Relay.
- The broker journals ordered events locally and uploads them through an outbound HTTPS callback with a single-job credential. No new inbound host port is required.
- Cloud persists events before acknowledgement, accepts identical retries, and rejects conflicting duplicates or sequence gaps.
- Redis wakes SSE subscribers. Subscription precedes historical replay to avoid missing events during connection setup.
- Browser reconnection uses Last-Event-ID. Short stream rotations revalidate access.
- The delivery credential can only report that job, upload manifest-listed artifacts and receive cancellation commands. It cannot invoke models or download data.
- Model authorization and container safety checks remain independent. Streaming does not extend model authorization.

## Deployment and limits

Cloud requires Agent migration 0063, working Redis and the updated background-job endpoints. Host 11 requires the updated broker, `job_events.py`, Agent and SDK. Legacy running jobs have no event channel; newly submitted jobs receive the live page URL.

Each job permits 12,000 events / 24 MiB and 256 artifacts / 64 MiB, with 16 MiB per file. Log forwarding stops recording further log events at its quota; the saved `optimizer.log` retains the existing size limit. Browser rendering is bounded to a log tail.

Artifacts are stored outside public media and served only by authenticated download routes. The default directory is `BASE_DIR.parent/private-agent-jobs`, configurable with Django setting `NEXUS_PRIVATE_JOB_ROOT`. Back up the database, private artifacts and broker journal together. Delivery credential files use mode 0600. No automatic deletion policy is installed; apply the deployment's retention policy to completed jobs.

For model access, see [MCP upstream model API authorization](./model-authorization.md).
