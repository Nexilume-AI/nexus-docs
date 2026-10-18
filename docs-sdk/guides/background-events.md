---
title: 后台任务与事件推送
---

# 后台任务与事件推送

Atrex 的新任务返回 `job_id` 和 `view_url`。任务在 11 的隔离执行容器中运行，原 MCP 请求结束或客户端断线不会取消任务。

## 实时页面

用发起任务的凭据所有者账号登录 Cloud，打开 `view_url`。平铺页面显示执行状态、耗时、模型请求次数、执行时间线、实时日志及产物下载。基准测量和优化阶段来自 Worker 实际输出；不推测百分比或承诺加速效果。性能对比以下载的官方报告为准。

网页使用 SSE 接收事件，不定时调用 `get_atrex_job`。页面断线会重连并从最后收到的事件序号补发。取消任务是显式操作；关闭页面不取消任务。产物在执行结束并上传校验通过后可下载，失败或取消任务也可能保留产物。

## MCP 流式监听

向 `watch_atrex_job` 传入项目凭据、`job_id` 和 `after`（初始为 0）。客户端需要接受 SSE，并在 MCP `tools/call` 参数的 `_meta.progressToken` 提供进度标识：

```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "watch_atrex_job",
    "arguments": {
      "project_id": "<project-id>",
      "access_key": "<private-project-key>",
      "job_id": "<job-id>",
      "after": 0
    },
    "_meta": {"progressToken": "watch-42"}
  }
}
```

Cloud 将进度转为 `notifications/progress`。`progress` 是事件序号，`message` 是包含 `kind`、`data`、`time` 的事件 JSON，不是完成百分比。单次监听最多 45 秒；结束或断线后，使用最后收到的序号继续监听，不要重新提交优化任务。调用返回的 `after` 可用于下一次监听。

仅接受 JSON 的客户端获得任务快照和 `view_url`，可打开页面接收连续推送。`get_atrex_job` 仍可查询快照、读取已保存日志；`read_atrex_artifact` 仍可通过 MCP 分块下载。本实现没有宣称支持 MCP Tasks 订阅扩展。

## 传递与恢复

- MCP 工具调用继续通过已有 OpenWrt / Cloud Relay。
- Broker 将有序事件保存到本地日志，并通过带单任务凭据的出站 HTTPS 回调主动上传；不开放新的入站端口。
- Cloud 先持久化事件再确认，接受内容相同的重复序号，拒绝冲突或缺号。
- Redis 唤醒 SSE 订阅者；订阅先于历史回放建立，避免订阅期间漏事件。
- 浏览器使用 Last-Event-ID 补发；短连接轮换会重新检查访问身份。
- 事件通道的凭据只能上报该任务、上传其清单内产物并接收取消命令，不能调用模型或下载数据。
- 模型授权检查、容器安全检查仍独立进行；进度推送不延长模型授权。

## 部署与边界

Cloud 需要 Agent 数据库迁移 0063、可用 Redis 和更新的后台任务接口。11 需要更新 Broker、`job_events.py`、Agent 和 SDK。当前进行中的旧任务没有事件通道；新提交的任务才返回进度页。

每个任务最多 12,000 个事件 / 24 MiB，最多 256 个产物 / 64 MiB，单文件最多 16 MiB。日志转发达到限额会停止继续记录日志事件，已保存的 `optimizer.log` 仍按原有限额保留。页面仅渲染日志尾部。

产物保存在公共媒体目录之外，仅通过鉴权下载接口提供。默认目录为 `BASE_DIR.parent/private-agent-jobs`，可通过 Django setting `NEXUS_PRIVATE_JOB_ROOT` 调整。运维应一起备份数据库、私有产物和 Broker 日志；事件投递凭据文件为 0600 权限。本功能不安装自动删除策略，应按部署方的保留策略清理已完成任务。

模型 API 授权见 [MCP 上游模型 API 授权](./model-authorization.md)。
