---
title: Private Run 与交互执行
---

# Private Run 与交互执行

Private Run 把一次调用、交互输入、Computer 和结果文件放在调用者自己的执行上下文中。Console 支持 Agent 的 Private Display 和单次 Run 的独立显示页；只有拥有该 Run 的调用者可以查看其私有展示内容。

## 开始一次 Run

1. 确认 Agent Runtime 已部署且健康，并选中正确 Workspace/Project。
2. 打开 Agent 的 Private Display，选择可用任务及所需的 Computer、Mobile 和文件。
3. 确认授权范围后提交。创建 Run 不代表执行已开始；后台 durable Agent worker 接受任务后才会推进。
4. 查看状态、事件、输出和待输入面板。需要审批或补充输入时，使用对应交互卡片回复。
5. 结束后检查输出文件并按需下载；不要用共享链接代替调用者授权。

## 继续对话与附件

支持继续交互的任务可提供 Queue 或 Steer 模式；以当前 Run 返回的能力为准。后续消息与当前轮次关联。发送成功不等于 Agent 已消费；检查接收状态。排队消息可在仍待处理、未过期时编辑或取消；队列发生变化后先刷新，避免覆盖另一处修改。

文件上传、Computer 文件导入和输出下载使用独立权限检查。已选择的文件必须仍有效，并且属于当前调用者/Run 的可用范围。切换 Computer 会重新检查目标连接及授权，不意味着旧目录、终端票据和文件引用可继续使用。

## 取消与恢复

通过 Cancel 请求取消，不要仅关闭浏览器。Run 的恢复和继续是显式操作：遇到恢复待确认状态，先检查此前是否已产生外部副作用，再按恢复提示处理，避免重复提交同一动作。Worker 重启不承诺自动重放所有外部调用。

## 验证与排错

- Run 卡在开始阶段：检查 Agent Runtime、可用执行容量和 `run_agent_tasks`。
- 等待输入：检查交互卡片是否仍有效，以及 [Inbox](../operations/inbox.md) 的待处理项。
- 文件或终端被拒绝：确认你是调用者、连接在线、授权未撤销，并重新获取当前 Run 的凭据。
- 跟进消息被拒绝：检查任务是否支持继续交互、Run 是否仍在运行、轮次和队列版本是否过期。
- 调查时结合 [Agents](index.md) 的运行状态与 [Observability](../operations/observability.md)，不要把事件摘要误认为无限期原始日志。

API 使用 `agents/{agent_id}/private-runs/` 创建/列出 Run，以及 `agent-runs/{run_id}/display/`、`events/`、`outputs/`、`follow-ups/`、`cancel/`、`recovery/` 和 `resume/`（均位于 `/api/v1/`）。它们与公开 Marketplace 演示不是同一套访问入口。
