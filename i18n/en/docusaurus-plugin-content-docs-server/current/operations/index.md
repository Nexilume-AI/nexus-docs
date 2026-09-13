---
title: Operations Overview
description: Continue private work, handle Inbox items, or prepare an Agent from the current Console home page.
---

# Operations Overview

The current Console home is **Your Agent workspace**, focused on continuing personal work and preparing Agents. Enterprise users first select the correct Organization/Workspace and Project. For local installation, see the [Community quickstart](../getting-started/quickstart.md).

## Read the page

| Area or state | Next step |
| --- | --- |
| Continue your work | Open priority Work Inbox items or continue a Private Run visible to the current caller |
| Bring your first Agent online | Upload a Python Agent when creation is allowed |
| Finish preparing this Agent | Complete Runtime setup and verify the Agent |
| Start a new private Run | Start fresh with a ready Agent |
| Ready when you are | Inspect recent Agents, runtime state, or open the full Agents list |

The primary action depends on permissions, resource loading, and Run history. Resolve access or loading errors before interpreting the page as having no pending work.

## Recommended check order

1. Confirm the current Workspace/Project.
2. Open pending [Inbox](inbox.md) items and handle their source objects.
3. Continue a [Private Run](../agents/private-runs.md), inspecting input requests, outputs, or recovery options.
4. Complete Runtime setup for unready Agents. Investigate failures in [Observability](observability.md), correlating Jobs, resource metrics, and Audit.
5. Check balance, entitlements, and usage in Billing; inspect Provider health in Providers or Model Pool.

## Verification

Check that the home action opens the correct Inbox item, Agent, or caller-owned Run. A home summary is not complete monitoring evidence; verify execution with its actual result.

## Troubleshooting

- **No visible Agents:** check scope and resource permissions before assuming deletion.
- **Recent Run status is unavailable:** use Retry recent Runs and restore history access before continuing.
- **An issue remains after a fix:** allow refresh and query the resource through Observability's Activity → Resource lookup.
- **Loading failed:** check login, Tenant context, and API requests; see [Troubleshooting](../troubleshooting/common.md).
