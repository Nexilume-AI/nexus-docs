---
title: 声明、实现与测试能力
sidebar_position: 1
---

# 声明、实现与测试能力

下面是一个不调用模型、不读磁盘的文档检查 Agent。可下载 [document-agent.py](/downloads/sdk/document-agent.py)。先完成[安装](../quickstart/installation.md)。

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

## 本机运行与预期结果

```sh
python document-agent.py --self-test
```

预期打印 `PASS: valid input, empty input, type check and length bound`。这个命令只验证业务逻辑，不要求 Router，也不宣称 Cloud 集成已完成。

在已配置的 OpenWrt 网络执行 `python document-agent.py`，或在 Cloud **Upload Python** 上传同一文件、构建并部署。调用工具 `inspect_document`，传入 `{"text": "hello nexus\nsecond line"}`，结果应为 `{"characters":23,"words":4,"lines":2}`。词数按空白拆分，不是自然语言分词。

## 为什么这样设计

- intent `document.inspect` 是业务能力路由键；tool name `inspect_document` 是 MCP 客户端看到的名字；它们不是 Agent 身份。
- `input_schema` 描述参数，不代替业务验证。直接 Nexus 调用也必须受长度、类型和空内容校验约束。
- 普通函数 `analyze_text` 不依赖网络，便于测试。handler 负责适配输入和当前 Run 的反馈。
- `ctx.enabled` 只说明事件反馈上下文可用，不意味着已获 Computer、Mobile 或计费权限。
- 无需 Computer 的能力不要声明 Computer 必需。以后增加文件读取时只请求 `files.read` 等实际使用的权限。

## 装饰器与输入模型

`@agent.capability` 用于普通返回值，`@agent.stream_capability` 用于生成事件；同步、异步函数及生成器有不同调用形式。使用 `NexusRunContext` 类型标注让 SDK 注入上下文；不要把 ctx 放进 MCP 的输入 schema，也不要从用户 payload 拼接 token。

使用 `pass_envelope=True` 可接收完整 Envelope，包括 intent、tenant、source_agent 和 task_id；一般业务只需要 payload。模型返回值要先转换成 JSON 可序列化对象，不要直接返回 SDK 客户端、文件句柄或异常实例。

完整参数见 [agent API](../reference/modules/agent.md)；声明字段见 [models API](../reference/modules/models.md)。
