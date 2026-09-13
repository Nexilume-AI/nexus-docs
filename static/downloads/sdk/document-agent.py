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
