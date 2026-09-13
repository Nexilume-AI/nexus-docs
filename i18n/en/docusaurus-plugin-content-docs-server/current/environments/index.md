---
title: Environments
description: Manage the Computer and Mobile execution environments that Agents can use.
---

# Environments

Environments is the user-facing name for **Computer** and **Mobile** under the Console Operate group. They connect hardware the user already owns to Nexus and expose files, terminals, or mobile actions to an Agent only after explicit authorization.

- A **Workspace** is the organization, identity, billing, and isolation boundary. It maps to a Server tenant.
- A **Project** scopes resources inside a Workspace.
- An **Environment** is an execution target available to a user or Agent inside a Project.

## Choose an Environment

| Capability | Computer | Mobile |
| --- | --- | --- |
| Target | Linux, macOS or Windows Computer Runtime / SSH host | Android device |
| Connection | Computer Runtime connects outward, or Server connects over SSH | Nexus Mobile pairs with a token and sends heartbeats |
| Interaction | WebSocket terminal, file/command API, tool setup | Observe, screenshot, tap, type, swipe, open app |
| Agent integration | Authorize Computer Runtime for a Private Run, or attach an SSH root during Docker deployment | Connect a device from the Agent Mobile panel |
| Risk control | Authorized root, read-only/read-write, SSH OS permissions | Manual, confirm-high-risk, or automatic approval |

## Recommended workflow

1. Select a Workspace and Project.
2. Pair a [Computer](computer.md) Runtime or create an SSH target or pair a [Mobile](mobile.md) Android device.
3. Confirm connection health and required capabilities.
4. Connect the Environment from [Agents](../agents/index.md).
5. Grant only the required management or use permission in [Access](../access/index.md).
6. Review Agent Activity and Observability after execution.

## Security boundary

- Computer SSH private keys and passwords stay on Server and are never injected into Agent containers.
- A Docker Agent uses a scoped Workspace token and API for one authorized root.
- Read-only blocks writes and commands. Read/write still runs under the SSH user's operating-system permissions.
- Mobile command approval depends on action risk and the device approval mode.
- Workspace, Project, Role, and resource sharing checks still apply to every Environment.

Computer is an SSH terminal and tool workbench, not a hosted remote IDE. Mobile currently supports Android; screenshots are short-lived protected data, not durable file storage.

## Current Computer connectivity

SSH in the table is the retained connection method. New computers can use Nexus Computer Runtime to connect outward to Cloud without inbound SSH. Pairing is followed by directory and capability authorization when used. Computer is under **Operate**; see [Computer](computer.md) for both workflows.
