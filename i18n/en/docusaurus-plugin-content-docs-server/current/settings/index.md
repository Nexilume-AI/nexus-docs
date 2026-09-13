---
title: Settings
description: Manage account details, Workspace context, developer access, and connection examples.
---

# Settings

Settings combines personal account controls with the current Workspace's developer context. Check the selected Workspace/Project before making changes because SDK snippets and request headers follow that selection.

## Account profile

Update account details such as display name and request a password reset. Reset uses the configured authentication/email flow; the Console never reveals the current password.

Profile fields belong to the user identity. Workspace membership, roles, and resource sharing belong in [Access](../access/index.md); renaming a user is not permission management.

## Workspace context

The selected Workspace and Project are stored in the browser session and sent as Nexus headers. **Current request headers** shows the actual context and is the first place to check when resources disappear or a multi-Workspace user receives 403.

**Manage workspaces** can create, rename, or delete a Workspace. Delete is soft, but hides its Projects, Groups, Members, Roles, Resource Shares, Service Accounts, API Keys, Billing, and Audit context from normal use. Require an exact name confirmation and export required configuration and finance records first.

## Developer access

Settings provides current Connection Values, API-key controls, and SDK snippets. Apply least privilege when creating a key: scope its Project, resources or Routers, rate, and budget; immediately store the plaintext in a secret manager because it cannot be retrieved again.

See the [API key guide](../guides/api-keys.md) for lifecycle details. For machine-to-machine access, prefer [Machine identity](../access/index.md) Service Accounts and tokens over a shared personal key.

## Verification and troubleshooting

1. Compare **Current request headers** with the intended Workspace/Project IDs.
2. Run the smallest current SDK or curl snippet.
3. Correlate its key prefix and result in [Observability](../operations/observability.md).

- **Snippet reaches the wrong resource:** reselect Workspace/Project and regenerate it; do not reuse stale headers.
- **API key returns 403:** inspect status, expiry, key policy, Project, and allowed Router/resource list.
- **Workspace cannot be managed:** Owner/Admin permission is required.
- **Workspace deleted by mistake:** deletion is soft, but normal users have no self-service restore; stop creating replacements and contact a platform administrator.
