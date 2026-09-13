---
sidebar_position: 2
title: How to use a Mobile Environment
description: Pair Android, set approval policy, run protected actions, and connect an Agent.
---

# How to use a Mobile Environment

Mobile turns an Android device into a protected execution environment. Console can observe device state, request screenshots, and dispatch actions. Agents can use the same controlled tools through Nexus MCP.

## Pair Android

1. Open **Mobile** and click **Pair Android device**.
2. Enter a name and choose an Approval mode.
3. Create and scan the pairing QR in Nexus Mobile.
4. Enable Nexus Mobile Control in Android Accessibility settings.
5. Wait for the first heartbeat and an online state.

The pairing token expires and is shown only during pairing. **Re-pair** or Rotate token creates a new QR and invalidates the old token.

## Lifecycle states

| State | Meaning | Next action |
| --- | --- | --- |
| `awaiting_pairing` | No first device connection | Scan the QR |
| `setup_required` | Paired, Accessibility not enabled | Finish Android setup |
| `online` | Fresh heartbeat and capabilities available | Open Control or connect an Agent |
| `offline` | Heartbeat is stale | Check Nexus Mobile, network, and permission |
| `token_expired` | Pairing was not completed in time | Regenerate the QR |
| `disabled` | An administrator disabled the device | Enable it before use |

## Approval modes

| Mode | Behavior | Recommended use |
| --- | --- | --- |
| Manual | Every action waits for approval | Shared or sensitive devices |
| Confirm high risk | Low/medium actions queue; high-risk actions wait | Default |
| Auto | Every action queues automatically | Trusted test devices only; requires policy admin |

Typing text is high risk. Sensitive tap labels involving payment, sending, or deletion are also promoted to high risk.

## Run actions and connect an Agent

Control supports Observe, Capture screen, Tap text, Tap coordinates, Type text, Swipe, Back, Open app, and Wait for state. Activity tracks `pending_approval`, `queued`, `running`, `succeeded`, `failed`, `rejected`, and `canceled`.

Screenshots require a reported screenshot capability and expire after a short Server-configured TTL. They use `private, no-store` and are not durable audit files.

Connect or disconnect a device under **Agents → Access → Mobile**, or export Mobile MCP configuration for an API-key caller. MCP applies the same risk and approval policy and requires Mobile use or administration permission, Workspace admin, or device ownership.

## Verification and troubleshooting

- Online devices show recent heartbeat, current app, and capabilities.
- Protected actions enter the expected approval path and finish in Activity.
- The Agent Mobile panel lists connected devices.
- `awaiting_pairing` usually means an expired/unreachable pairing URL.
- `setup_required` means Android Accessibility is not enabled.
- Offline means the app, network, background execution, or heartbeat needs attention.

See [Access](../access/index.md) and [Agents](../agents/index.md).
