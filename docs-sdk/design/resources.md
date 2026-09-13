---
title: 文件、Computer、Browser 与 Mobile
sidebar_position: 3
---

# 文件、Computer、Browser 与 Mobile

资源声明让 Cloud 知道工具需要什么；声明本身不授予权限。每次 Run 使用当前调用者实际绑定并授权的资源，不能用 Agent 发布者的机器偷偷兜底。

## 区分三种文件

| 数据 | 接口 | 所在位置 |
| --- | --- | --- |
| 上传到当前 Run 的输入文件 | `ctx.input.files`、`ctx.files.list/download/iter_bytes` | Cloud 私有 Run 文件 |
| 调用者 Computer 的工作区 | `ctx.workspace.list/read_text/write_text` | 被授权的远端根目录 |
| Agent 本地产物 | `ctx.output.upload_file(path)` | 从 Agent 本地上传成不可变引用 |

`ctx.files.list()` 返回元数据，不返回文件内容。`download` 支持断点续传并校验 SHA-256；目标已存在默认拒绝覆盖。`upload` 的源文件在上传中必须保持不变；恢复使用同一个活动 Run 的 resume_id。

在已获文件输入的 handler 中：

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    for index, reference in enumerate(ctx.input.files):
        destination = Path(directory) / f"input-{index}.bin"
        ctx.files.download(reference, destination)
        # Inspect bytes using your application-specific format and size limits.
```

不要把用户传入的文件名直接当本地路径。输出使用 `ctx.output.upload_file(local_path)` 返回的受保护引用；`ctx.output.created/updated/ready` 是报告接口，不等同于把文件字节上传到 Cloud。

## Computer 与命令执行

```python
agent = NexusAgent(
    computer_requirement="required",
    workspace_capabilities=("files.list", "files.read"),
)
```

这是替换 Agent 声明的片段。调用前绑定在线 Computer；读取前确认上下文与授权可用。`ctx.workspace.list(".")` 返回 `WorkspaceEntry` 元组，`read_text` 返回 str；命令需要额外 `command.execute`。

`ctx.terminal.run(command, cwd=".", timeout=30)` 返回 `CommandResult`，检查 exit_code/stdout/stderr。工作区路径限制不是操作系统沙箱；shell 命令仍有 Runtime 用户权限。不要把未经校验的用户输入拼接进 shell。

## Attached Browser

声明 `browser.control`，绑定 Computer 并安装浏览器后：

```python
browser = ctx.browser.attached_session()
try:
    observation = browser.open("https://example.com")
    observation = browser.locator("a").click()
    ctx.chat.say(observation.title)
finally:
    browser.close()
```

此网络片段需要真实已授权的 Run。`observation` 含 URL/title/DOM/revision/image。页面变化后旧节点可能失效，捕获 `NexusBrowserStaleObservation` 后重新 observe，再做业务判断。`ctx.browser.session()` 使用 Agent 主机本地浏览器，`attached_session()` 使用调用者 Computer，不能混为一谈。

## Mobile

通过 Agent 的 `mobile_requirement`、`mobile_capabilities` 以及工具声明 mobile_scopes 请求实际动作。`ctx.mobile.status()` 返回能力与在线状态；observe/capture_screen 返回观察与截图；tap/type/swipe/open_app 等执行真实设备动作。没有绑定、未授权、设备忙和超时分别处理；不要对可能已执行的点击盲目重试。

签名与动作列表：[reporting](../reference/modules/reporting.md)、[browser](../reference/modules/browser.md)、[files](../reference/modules/files.md)、[workspace](../reference/modules/workspace.md)。Mobile 示例：[edge_caller_mobile_agent.py](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/examples/edge_caller_mobile_agent.py)。
