---
title: Work Inbox
---

# Work Inbox

**Operate → Inbox**（`/inbox`）聚合个人工作和共享角色队列，帮助你找到需要回复、审批或排错的事项。它与 Observability 的历史调查互补。

## 使用流程

1. 使用个人账号登录并选中正确的 Workspace；机器身份不能读取个人 Inbox。
2. 按 Project、Category、Ownership 或关键词过滤。分类包括 Agent、Background tasks、Approvals、Operations。
3. 优先处理 `needs_action` 和 `failed`，打开详情后用 **Open** 回到真正的 Run、审批或资源页面。
4. 使用 Read、Snooze 或 Archive 整理自己的收件箱；这些操作不会替你批准请求、停止任务或删除业务资源。
5. 完成源页面操作后返回 Inbox；条目会重新检查源对象状态和当前访问权限。

## 状态与个人回执

| 状态 | 含义 |
| --- | --- |
| `needs_action` | 等待输入、审批或运维处理 |
| `in_progress` | 源任务仍在进行 |
| `failed` | 源任务失败，需要调查 |
| `completed` | 源任务已完成 |
| `resolved` | 原先需要处理的情况已解除 |
| `canceled` | 源任务已取消 |

Read、Snooze、Archive 是当前用户的回执状态。共享角色队列的可见性随角色和资源权限重新计算；看到条目不代表能越过源页面授权。Private Run 的输入和结果仍属于调用者。

## 通知与验证

在 Inbox 设置中选择分类、事件和安静时间；桌面通知需要浏览器许可及服务端 Web Push 配置。Test 只验证所选订阅的通知发送，不代表后台任务成功。流式更新断线后以刷新查询为准，不把 SSE 当作永久事件存档。

验证时创建一个真实后台任务或待回复 Run，确认条目可以打开正确源页面；标为已读后确认只改变自己的回执。列表、摘要、偏好和事件流分别使用 `/api/v1/inbox/items/`、`summary/`、`preferences/`、`stream/`。

## 排错

- 条目消失：检查 Workspace/Project、过滤条件、源对象状态和角色变更。
- Open 被拒绝：当前权限可能已撤销；不要复用另一用户的链接或游标。
- 长时间无更新：检查 `run_work_inbox_worker`，并在 [Observability](observability.md) 调查源 Job。
- 需要回复 Agent：进入 [Private Run](../agents/private-runs.md)，不要把标为已读当作回复。
