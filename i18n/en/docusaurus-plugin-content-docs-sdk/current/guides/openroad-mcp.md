---
title: Remote EDA with OpenROAD MCP
---

# Remote EDA with OpenROAD MCP

The SDK's OpenROAD example discovers and registers complete MCP tool schemas and
descriptions. It supports interactive OpenROAD and Yosys sessions, asynchronous
EDA jobs, chunked RTL uploads, stage/log polling and artifact downloads with
size and SHA-256 verification.

Deploy the pinned MCP image and SDK bridge on a Linux Docker host connected to a
Nexus OpenWrt Router. The MCP container communicates through a Unix socket; the
bridge registers the agent and asks the paired Router to publish it to Cloud.
Use Relay when inbound access is blocked. Marketplace listing is a separate step.

For long flows, create a project, upload inputs and start a job. Save the returned
job ID, poll progress and logs, wait for finalization, then list and download
artifacts. A client disconnect does not require submitting a second job. Downloads
can use authenticated Cloud files or bounded MCP chunks; streaming does not remove
transport size limits or client timeouts.

Use Yosys Tcl sessions for synthesis and OpenROAD Tcl sessions for physical design.
Do not split a Tcl command's arguments across newlines. Isolate mutually untrusted
designers in separate deployments because interactive interpreters are not a
multi-tenant sandbox.

See the [deployable OpenROAD example](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/openroad_mcp_agent)
for Compose, the SDK registration check, CLI commands, resource limits and backup guidance.
