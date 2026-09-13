---
sidebar_position: 3
title: Create your first Workspace and Project
description: Establish the Nexus organization boundary, project scope, and reusable execution environments.
---

# Create your first Workspace and Project

After this page, the Console header will select one Workspace and one Project. Agents, Providers, access, usage, and charges created next will share that context, avoiding the common “the resource exists but returns 404/403” failure.

## What you need

- Sign in to the enterprise Console supplied by your administrator. This Workspace/Project administration chapter is for enterprise users; self-hosting users should see the [Community quickstart](quickstart.md).
- Permission to create a Workspace. The local superuser is suitable for the first evaluation.

## Three names that are easy to mix up

| Name | Purpose | Request context |
| --- | --- | --- |
| Workspace | Organization, security, billing, and audit boundary; internally a tenant | `X-Nexus-Tenant`, required by most product APIs |
| Project | Resource and collaboration scope inside a Workspace | `X-Nexus-Project`; some lists omit it for All projects |
| Computer Environment | An SSH computer/directory an Agent can use | A Project-owned resource, not a tenant |

Environment is not a `dev/staging/prod` release slot. Agent Runtime has its own deployment state; a Computer does not replace a Project.

## 1. Create the Workspace

1. Open **Settings → Workspace**.
2. Under **Manage workspaces**, enter `Nexus Demo` and click **Create**.
3. The Console switches to it. The first header selector should show `Nexus Demo`.

The second selector may still show **All projects**. That is a cross-project view, not a Project that can own a new resource.

## 2. Create the Project

1. Open **Access** and click **Create project**.
2. Enter `First Project`. A Team is optional for this first walkthrough.
3. Select `First Project` from the header Project selector.

Refresh or reselect the Workspace if the list is stale. A Project always belongs to the current Workspace.

## 3. Verify the context

Open **Settings → Workspace context** and confirm both names. Then open **Agents**. The page should show `First Project`, not **All projects**.

Automation uses UUIDs, not display names:

```http
X-Nexus-Tenant: <workspace-uuid>
X-Nexus-Project: <project-uuid>
```

## Permission boundaries

- Workspace is the highest product isolation boundary. Switching it changes resources, members, Wallet, API Keys, and Audit.
- Project owns resources. The Billing Wallet stays at Workspace level rather than creating a balance per Project.
- Roles can apply to Workspace, Project, or Group. Use Resource Share for one-resource exceptions.
- Workspace deletion is soft deletion but hides its Projects, access, keys, Billing, and Audit context from normal use. Do not use it as a demo reset button.

## Verification

- The header shows both `Nexus Demo` and `First Project`.
- Agents, Providers, and Billing no longer report a missing Workspace.
- A concrete Project, not **All projects**, appears before resource creation.

## Troubleshooting

- **No Create Workspace action:** the account lacks management permission or is anonymous.
- **New Project is absent:** check the selected Workspace; Projects never cross Workspace boundaries.
- **API says the tenant header is required:** supply the Workspace UUID.
- **Known resource returns 404:** compare both headers with the resource owner before recreating it.

## Current limits and next step

The Console currently creates Workspaces in **Settings** and Projects in **Access**, so first setup spans two pages. Continue with the [first Agent workflow](first-agent.md) or read [identity and request paths](../concepts/identity-and-request-path.md).
