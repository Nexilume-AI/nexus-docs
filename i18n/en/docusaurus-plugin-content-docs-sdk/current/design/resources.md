---
title: Files, Computer, Browser and Mobile
sidebar_position: 3
---

# Files, Computer, Browser and Mobile

Resource declarations tell Cloud what a tool needs; they do not grant access. Each Run uses resources actually attached and authorized by its caller. Do not silently substitute the publisher's computer.

## Three different file locations

| Data | API | Location |
| --- | --- | --- |
| Uploaded Run inputs | `ctx.input.files`, `ctx.files.list/download/iter_bytes` | Private Cloud Run files |
| Caller Computer workspace | `ctx.workspace.list/read_text/write_text` | Authorized remote root |
| Local Agent artifact | `ctx.output.upload_file(path)` | Uploaded from Agent host as an immutable reference |

`files.list()` returns metadata, not bytes. Downloads support resume and SHA-256 verification; existing destinations are rejected by default. Keep an upload source unchanged and reuse its resume_id only within the same active Run.

Inside a handler with authorized file inputs:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    for index, reference in enumerate(ctx.input.files):
        destination = Path(directory) / f"input-{index}.bin"
        ctx.files.download(reference, destination)
        # Inspect bytes using your application-specific format and size limits.
```

Do not use caller-supplied filenames directly as local paths. `ctx.output.upload_file(local_path)` returns a protected reference. `output.created/updated/ready` are reporting APIs, not equivalent to uploading file bytes.

## Computer and commands

```python
agent = NexusAgent(
    computer_requirement="required",
    workspace_capabilities=("files.list", "files.read"),
)
```

This fragment replaces the Agent declaration. Attach an online Computer before calling. `workspace.list(".")` returns a tuple of `WorkspaceEntry`; `read_text` returns str. Commands additionally require `command.execute`.

`ctx.terminal.run(command, cwd=".", timeout=30)` returns `CommandResult`; inspect exit_code/stdout/stderr. Workspace path constraints are not an OS sandbox: commands still have the Runtime user's permissions. Never interpolate unchecked input into shell commands.

## Attached Browser

Declare `browser.control`, attach a Computer and install its browser:

```python
browser = ctx.browser.attached_session()
try:
    observation = browser.open("https://example.com")
    observation = browser.locator("a").click()
    ctx.chat.say(observation.title)
finally:
    browser.close()
```

This network fragment requires a real authorized Run. Observations contain URL/title/DOM/revision/image. After page changes, catch `NexusBrowserStaleObservation`, observe again and reconsider the action. `ctx.browser.session()` uses the Agent host browser; `attached_session()` uses the caller's Computer.

## Mobile

Declare `mobile_requirement`, `mobile_capabilities` and tool mobile_scopes for the required actions. `ctx.mobile.status()` returns capability/availability information; observe/capture_screen return observations/screens; tap/type/swipe/open_app perform real device actions. Handle missing bindings, permission denial, busy devices and timeouts separately. Do not blindly retry a click that may already have executed.

See [reporting](../reference/modules/reporting.md), [browser](../reference/modules/browser.md), [files](../reference/modules/files.md) and [workspace](../reference/modules/workspace.md). Mobile example: [edge_caller_mobile_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/edge_caller_mobile_agent.py).
