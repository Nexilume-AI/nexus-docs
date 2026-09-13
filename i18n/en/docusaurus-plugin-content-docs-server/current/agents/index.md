---
title: Agents
description: Create an Agent, connect a runtime, deploy, grant access, observe, and publish it.
---

# Agents

An Agent is an invokable, permissioned, and publishable AI capability. The commercial Console is runtime-first: a user-owned Docker image runs an MCP HTTP Server, or an OpenWrt IPv6/Relay node hosts the Agent process. Nexus manages identity, deployment, access, observability, and Marketplace; it does not edit Agent source in the browser.

## Agent work area

| Area | Purpose |
| --- | --- |
| Overview | Current Runtime and recommended next action |
| Runtime | Register Docker images or bind OpenWrt, deploy, stop, check health, and attach Computer |
| Access | Create an Agent key, export MCP, connect Mobile, and review access events |
| Observability | Review Runs, deployment, runtime, access and configuration events |
| Publication | Visibility, pricing and Marketplace publication |
| Settings | Name, project, state and resource defaults |

## Create an Agent

Select a Workspace and Project, open **Agents → Create agent**, and enter a name beginning with a letter and containing only letters, digits, `_`, or `-`, up to 64 characters. Creation establishes a private Agent identity. It does not create a container, OpenWrt process, or model Provider.

## Choose a runtime

### Docker

Register a Registry image or upload a `docker save` tar, set the image Current, deploy it, then run Health. A ready deployment is `active` and `healthy`. Private Registry secrets are write-only. Nexus currently does not provide full Registry credential management, Kubernetes, or remote orchestrator deployment.

### OpenWrt IPv6

Create an edge pairing code, let OpenWrt publish a registration, bind an available registration, and run Health or MCP. OpenWrt owns the remote process lifecycle; Stop disconnects the binding. See [Connect an OpenWrt IPv6 Agent](../guides/connect-openwrt.md).

## Connect an Environment

- Attach a [Computer](../environments/computer.md) to a Docker deployment with one authorized root and read-only/read-write mode. Files use the Workspace API; there is no directory mount.
- Connect a paired [Mobile](../environments/mobile.md) from the Agent Mobile panel. Device approval and action-risk rules continue to apply.

Use the [Environments overview](../environments/index.md) to choose between Computer and Mobile before granting access.

## MCP and credentials

Create an Agent key under **Access**, save the one-time plaintext, and export MCP configuration. Agent `use` permits invocation, not deployment or settings changes.

Keep credential purposes separate: Agent keys invoke one Agent; Gateway API keys call models; service-account tokens identify automation; OpenWrt tokens and certificates identify edge devices.

## Lifecycle

| Object | Common states |
| --- | --- |
| Agent | active, disabled, archived |
| Runtime deployment | deploying, active, stopped, failed |
| Health | unknown, healthy, unhealthy |
| Publication | unpublished/draft, published, suspended |

Before archive or delete, check callers, Environment attachments, Marketplace listing, and billing effects. Soft deletion does not replace credential revocation.

## Publishing and billing

Set visibility, price, and resource defaults only after the runtime is healthy. Public calls create Agent usage records for consumer spending and publisher earnings in [Billing](../billing/index.md). Never put Registry, Provider, Workspace, or user secrets in public metadata.

## Current limits

- No real Git repository hosting; legacy Repo APIs preserve compatibility metadata only.
- Event records are not unlimited runtime log streaming; file, Dataset and execution-capacity checks depend on the specific API and configured limits.
- No full Registry credential lifecycle, Kubernetes deployment, or remote orchestration. Event replay and recovery depend on the specific Run API.

## Troubleshooting order

Check Workspace/Project, Agent state and Current image or edge registration, deployment Job and Health reason, Activity and Observability Audit, then use [Access → Check access](../access/index.md#explain-an-access-decision) for 403 responses.

Follow the [first Agent workflow](../getting-started/first-agent.md) for an end-to-end example.

## Python source builds and current sections

Current sections are Overview, Runtime, Access, Observability, Publication and Settings. Runtime accepts container images and a Python file exposing a top-level FastMCP instance. Ordinary scripts and factories are not supported entrypoints. Source syntax is currently validated against Python 3.12, independently of the Cloud host's Python version.

Source uploads are limited to 1 MiB and requirements text to 32 KiB. Requirements accept allowed package declarations, not pip options, URLs, local paths or VCS installs. Stages are Queued, Dependencies, Image, Verify tools and Ready. Select and deploy the resulting image after success; a successful build is not a running deployment.

Building requires administrator-configured enablement, base image, isolation and `run_agent_python_builds`. Inspect failures in Runtime; failed records without images can be deleted before another upload. OpenWrt Runtime also supports Relay connectivity, so an IPv6 address alone is not the availability test.

See [Private Runs](private-runs.md) for interaction, follow-ups, files and recovery, and [Inbox](../operations/inbox.md) for pending input and failures. Agent events are not unlimited container logs. File/Dataset operations have their own authorization and resource limits; older statements about no general quota enforcement do not bypass those checks.
