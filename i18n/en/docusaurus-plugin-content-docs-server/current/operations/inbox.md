---
title: Work Inbox
---

# Work Inbox

**Operate → Inbox** (`/inbox`) combines personal work and shared role queues. Use it to find pending input, approvals and operational failures; use Observability for historical investigation.

## Workflow

1. Sign in as a person and select the correct Workspace. Machine identities cannot read a personal Inbox.
2. Filter by Project, Category, Ownership or keyword. Categories are Agent, Background tasks, Approvals and Operations.
3. Prioritize `needs_action` and `failed`. Inspect the item and choose **Open** to return to the actual Run, approval or resource.
4. Use Read, Snooze or Archive to organize your own receipt. These actions do not approve a request, stop execution or delete a resource.
5. After acting on the source page, return to Inbox. Source state and current permissions are rechecked.

## States and receipts

| State | Meaning |
| --- | --- |
| `needs_action` | Input, approval or operational attention is required |
| `in_progress` | Source work is running |
| `failed` | Source work failed |
| `completed` | Source work completed |
| `resolved` | The condition no longer needs attention |
| `canceled` | Source work was canceled |

Read, Snooze and Archive are per-user receipts. Shared role queue visibility is recalculated from current roles and resource access. An Inbox item cannot bypass authorization on its source page. Private Run inputs and outputs remain caller-owned.

## Notifications and verification

Preferences control categories, events and quiet hours. Desktop notifications need browser permission and configured server Web Push. Test checks delivery to the selected subscription, not business-task success. Refresh after a disconnected stream; SSE is not a permanent event archive.

Verify with a real background task or Run awaiting input. Confirm Open reaches the correct source and marking read changes only your receipt. List, summary, preferences and streaming endpoints are `/api/v1/inbox/items/`, `summary/`, `preferences/` and `stream/`.

## Troubleshooting

- Missing item: check Workspace/Project, filters, source state and role changes.
- Open denied: authorization may have been revoked; do not reuse another user's cursor or link.
- Stale items: check `run_work_inbox_worker` and investigate source Jobs in [Observability](observability.md).
- Agent needs input: open the [Private Run](../agents/private-runs.md). Marking read is not a reply.
