---
sidebar_position: 1
title: How to use a Computer Environment
description: Add an SSH target, open a terminal, configure tools, and attach it to an Agent.
---

# How to use a Computer Environment

Computer supports outbound Nexus Computer Runtime connections and legacy Server-initiated SSH Targets. Their credentials and authorization boundaries differ.

## Recommended: pair Computer Runtime

1. In **Operate → Computer**, select the Project and create a pairing code.
2. Install a compatible Nexus Computer Runtime as the current user on the target. It connects outward to Cloud; no SSH password or inbound port is required.
3. Use the generated `nexus-computer setup` command or pairing link. Codes are single-use and expire; do not share them.
4. Confirm the workspace directory and scopes on the device, then check that Console shows it online.
5. Select it in Marketplace Attach or Private Display and approve the required scopes. Pairing alone does not grant every Agent access.

Revoked devices must pair again. Run terminal, file and browser actions retain caller/Run/scope checks. Existing SSH Targets use the separate workflow below; their administrator-terminal rules do not describe all Computer Runtime access.

## SSH Target prerequisites


- Select the target Workspace and Project.
- Have Computer management permission. Terminal access currently normally requires a Workspace administrator.
- Run SSH on the target and allow Nexus Server to reach its host and port.
- Set `NEXUS_WORKSPACE_SSH_RUNNER=paramiko` for real SSH operation.

## Add an SSH target

1. Open **Computer** and add a target.
2. Enter name, host, port, and SSH user.
3. Choose private-key or password authentication.
4. Validate the connection and review the host-key fingerprint.
5. Save and run Test. Health should be succeeded.

Server encrypts the key or password and never returns plaintext in list or detail responses. Leaving a secret blank while editing keeps the existing secret.

## Open a terminal

Select a target and open a Session. Console connects to `/ws/workspace-terminals/{session_id}/`, and Server opens the SSH shell.

- A successful WebSocket upgrade is HTTP `101 Switching Protocols`.
- Linux and macOS use the target user's shell; Windows OpenSSH prefers PowerShell.
- Sessions in `created` or `active` can be resumed; **End session** closes one explicitly.
- Terminal output is not persisted by default. Audit stores lifecycle events, not transcripts.

## Configure Codex or Claude Code

With a live Session, click **Configure tools**:

1. Detect the remote `codex` and `claude` commands.
2. Select a [Provider Runtime](../providers/index.md) for model API configuration.
3. Select an [Agent](../agents/index.md) for MCP configuration.
4. Preview and apply, or use Rollback to restore the latest backup.

Codex writes `$CODEX_HOME/nexus.config.toml` and launches with `codex --profile nexus`; it does not overwrite the base `config.toml`. Provider and MCP operations remain independent.

## Attach Computer to an Agent

1. Open **Agents → Runtime → Deploy**.
2. Select the Computer under **Workspace attachment**.
3. Set an Authorized root such as `~/project` or `D:/work/customer-a`.
4. Choose `Read only` or `Read/write`.
5. Deploy the Docker runtime.

The container receives a Workspace API URL, scoped token, root, and mode. It never receives the SSH secret or a mounted directory. File paths and command working directories must be relative to the authorized root; absolute paths and `..` traversal are rejected.

:::warning Command execution boundary
Read/write allows remote shell commands. The authorized root constrains Workspace API paths, but the command still runs with the SSH user's OS permissions. Attach write access only to trusted Agents and use a restricted SSH account.
:::

## Verification and troubleshooting

- Target Test succeeds, a Session becomes active, and tool detection reports non-secret path/version facts.
- An attached Agent deployment shows the Computer, authorized root, and access mode.
- WebSocket HTTP 200 means the backend used the wrong server; run Uvicorn with `config.asgi:application`.
- WebSocket 403 points to session, Workspace permission, or Origin validation.
- Workspace API denial usually means an invalid relative path, access mode, or expired scoped token.

See [Production deployment](../guides/production-deployment.md) and [Troubleshooting](../troubleshooting/common.md).
