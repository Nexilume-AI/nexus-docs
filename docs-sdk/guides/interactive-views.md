# Interactive View：交互式网页

任意 Agent 都可以通过 `current_run().views.create(...)` 创建私有交互网页。
Cloud 提供公网入口、一次性链接、访问隔离和 SSE 双向事件通道；Agent 无需
额外配置域名、Web 服务或入站端口。它不依赖模型 API 授权。

## 内置页面

```python
from nexus_agent import current_run

def open_counter():
    count = 0

    def increment(arguments, view):
        nonlocal count
        count += arguments["amount"]
        view.set_state({"metrics": [{"label": "Count", "value": count}]})
        return {"count": count}

    view = current_run().views.create(
        title="Counter",
        state={"metrics": [{"label": "Count", "value": 0}]},
        actions={"increment": {
            "label": "Increment",
            "input_schema": {
                "type": "object",
                "properties": {"amount": {"type": "integer", "minimum": 1,
                                          "maximum": 10, "default": 1}},
                "required": ["amount"], "additionalProperties": False,
            },
        }},
        handlers={"increment": increment},
    )
    return view.public_info
```

页面支持 `summary`、`metrics: [{label,value}]`、`table: {columns,rows}`、
`chart: {label,points}`、`logs`。SDK 根据 action 的 JSON Schema 生成操作表单。
`set_state` 替换整个状态，并通过 SSE 推送给浏览器。

MCP 方法返回后 Agent 进程仍需运行；SDK 后台线程接收操作，调用
`handler(arguments, view)`。处理函数应在 30 秒内返回，耗时工作放入后台任务。
处理函数不会自动继承已经结束的 `current_run()`、模型密钥或发布者账户权限。
只捕获属于当前调用者的工作区资源，并继续使用原有的资源校验和公平队列。

异步入口为 `await current_run().aio.views.create(...)`，返回 handle 支持
`await handle.set_state(...)` 和 `await handle.close()`；action handler 仍为同步函数。

## 自定义网页

向 `views.create` 传入 `html=Path("panel.html").read_text(encoding="utf-8")`：

```html
<button id="increment">Increment</button><output id="count">0</output>
<script>
nexus.onState(state => {
  document.getElementById("count").textContent = state.metrics[0].value;
});
document.getElementById("increment").onclick = async () => {
  const result = await nexus.action("increment", {amount: 1});
  console.log(result.count);
};
</script>
```

平台注入 `window.nexus`，提供 `state`、`onState(callback)` 与
`action(name, arguments)`。操作只允许使用 Agent 声明的名称和参数结构。
自定义 HTML 在独立、不具备同源权限的 sandbox iframe 中执行，不能读取
Nexus 账户 Cookie、父页面或凭据，也不能使用外部脚本和 fetch。

首版接受不超过 256 KiB 的单文件 HTML：CSS/JS 内联，图片使用 data URL。
多文件前端应在构建时打包；暂不托管任意网站目录。模型密钥、工作区凭据等
不得放入 state、操作参数或返回值，因为这些内容会交给网页。

## 鉴权、隔离与生命周期

- 创建必须来自正在运行且通过验证的 Agent 调用；工作区身份来自服务端，
  不接受模型提供的用户 ID。同一个 API Key 是同一个调用者，不同 Key 隔离。
- MCP 只返回 `view.public_info`。运行时独立凭据保存在 SDK handle 内，不应返回给调用者。
- 链接有效期 10 分钟，仅兑换一次。兑换后使用限于当前 View 的 Secure、HttpOnly
  Cookie，原浏览器刷新仍可访问。新链接兑换后取代旧浏览器会话。
- View 默认持续一小时，可设 `ttl_seconds=60..3600`；Key 撤销、Agent 禁用、
  过期或关闭都会使访问失效。链接不会赋予发布者的 Nexus 账户权限。
- 在同一调用者后续 MCP 调用中，`current_run().views.link(view_id)` 获取新链接；
  `current_run().views.close(view_id)` 或 `view.close()` 关闭并撤销访问。
- Agent 断线时浏览器显示离线并禁止新操作；临时网络中断由 SDK 自动重连。
  进程重启会丢失内存 handle，应通过 MCP 重新创建页面。

## 可靠性与限制

浏览器用 EventSource 接收更新，Agent 用出站 SSE 接收操作，不需要轮询。
操作先持久化，再通过 Redis 唤醒连接，重连会重放当前状态和待处理操作。
同一 request ID 的重复提交不会生成新操作；事务租约保证同一操作只被领取一次。
完成结果可重试提交，处理函数不会因结果重试而重复执行。执行结果不明的操作
会超时，不自动重新执行；用户手动重试前应检查实际任务状态。

每个调用者/Agent 最多 8 个活动 View；每个 View 最多 32 个声明操作、16 个待处理
操作、256 次累计操作。状态最多 128 KiB，参数和结果各 32 KiB，Schema 8 KiB，
不支持 Schema 引用和正则表达式。排队最多 120 秒，领取后的执行租约 60 秒。

## Wave 示例

`examples/wave_mcp_agent/interactive_dashboard.py` 使用同样的通用 SDK。
调用 `open_wave_dashboard`，选择 `template="panel"` 或 `"custom"`，即可在网页中
列出文件或查询已有 session 的信号。它复用 Wave 的调用者工作区和公平队列。
每个工作区最多保留两个面板，关闭工作区时关闭面板。原 Surfer/FST 查看器保持可用。
