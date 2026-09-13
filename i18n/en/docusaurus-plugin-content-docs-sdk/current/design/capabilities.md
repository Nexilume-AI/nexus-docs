---
title: Declare, implement and test capabilities
sidebar_position: 1
---

# Declare, implement and test capabilities

This document inspector does not call a model or read the filesystem. Download [document-agent.py](/downloads/sdk/document-agent.py) after completing [installation](../quickstart/installation.md).

```python
"""One file for edge execution or Nexus Cloud Upload Python.

Run `python document-agent.py --self-test` for local business-logic checks.
The SDK must already be installed. Cloud Run features need a trusted Run context.
"""
import sys
from nexus_agent import NexusAgent, NexusRunContext, McpToolDescriptor


def analyze_text(text: str) -> dict:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")
    if len(text) > 20000:
        raise ValueError("text must be at most 20000 characters")
    return {"characters": len(text), "words": len(text.split()),
            "lines": len(text.splitlines())}


agent = NexusAgent(cloud_name="Document Inspector")


@agent.capability("document.inspect", tool=McpToolDescriptor(
    name="inspect_document",
    description="Count characters, whitespace-separated words and lines.",
    input_schema={"type": "object", "properties": {
        "text": {"type": "string", "minLength": 1, "maxLength": 20000}},
        "required": ["text"], "additionalProperties": False},
))
def inspect_document(payload, ctx: NexusRunContext):
    # Runtime validation also protects direct Nexus calls.
    result = analyze_text(payload.get("text"))
    if ctx.enabled:
        ctx.plan.set([{"id": "inspect", "title": "Inspect document", "status": "running"}])
        ctx.raise_if_cancelled()
        with ctx.trace.step("count-document"):
            ctx.chat.say(f"Counted {result['words']} whitespace-separated words.")
        ctx.plan.update("inspect", status="completed")
    return result


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        assert analyze_text("hello nexus\nsecond line") == {
            "characters": 23, "words": 4, "lines": 2}
        for invalid in ("", None, "x" * 20001):
            try:
                analyze_text(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError("Invalid input was accepted")
        print("PASS: valid input, empty input, type check and length bound")
    else:
        agent.run()

```

## Run locally and check the result

```sh
python document-agent.py --self-test
```

Expected: `PASS: valid input, empty input, type check and length bound`. This checks business logic only; it does not require a Router or claim Cloud integration acceptance.

Run `python document-agent.py` on a configured OpenWrt network, or upload the same file through Cloud **Upload Python**, build and deploy. Call `inspect_document` with `{"text": "hello nexus\nsecond line"}`. Expect `{"characters":23,"words":4,"lines":2}`. Words are whitespace-separated tokens, not language-aware segmentation.

## Why this structure works

- Intent `document.inspect` is the capability routing key; `inspect_document` is the MCP tool name. Neither is the Agent identity.
- The schema describes input; application validation still protects direct Nexus calls.
- `analyze_text` is network-independent business logic. The handler adapts input and reports to the current Run.
- `ctx.enabled` means event reporting is available, not that Computer, Mobile or billing access is authorized.
- Do not require a Computer for a tool that needs none. When adding file access, request only scopes such as `files.read` that the implementation uses.

## Decorators and input

Use `@agent.capability` for ordinary results and `@agent.stream_capability` for event generators. Sync and async handlers/generators have distinct calling conventions. Annotate the context as `NexusRunContext` for injection; never add ctx to the MCP input schema or construct credentials from user payloads.

`pass_envelope=True` exposes the full Envelope, including intent, tenant, source_agent and task_id. Most business functions only need payload. Convert model results into JSON-serializable values; do not return clients, file handles or exception objects.

See [agent API](../reference/modules/agent.md) for parameters and [models API](../reference/modules/models.md) for declaration fields.
