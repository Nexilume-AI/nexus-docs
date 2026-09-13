---
title: 状态、恢复、用量与计费
sidebar_position: 4
---

# 状态、恢复、用量与计费

## 不同状态各司其职

| 接口 | 适合存储 | 不保证什么 |
| --- | --- | --- |
| `ctx.memory` | 调用者/工作流可复用的事实 | 不是进程 checkpoint，也不是密钥保险箱 |
| `ctx.checkpoint` | 当前任务的阶段和小型恢复数据 | 不自动撤销外部操作 |
| `ctx.recovery` | 托管外部操作的执行与重放记录 | 不让不支持幂等的外部服务自动变成 exactly-once |
| `NexusReportingConfig` outbox | 尚未送达的 Run 事件 | 不保存完整业务执行状态 |

`memory.add()` 返回事件提交 bool；`recall()` 返回 `NexusMemoryItem` 列表。update/delete 需要 revision；遇到 `NexusMemoryConflict` 重新读取并合并，不能覆盖未知的新版本。明确 consent、sensitivity、license，不能仅因为模型建议就把用户数据标为已批准。

## Checkpoint

下面是需要真实 Cloud Run 的 handler 片段：

```python
previous = ctx.checkpoint.load()
checkpoint = ctx.checkpoint.save(
    stage="validated", data={"schema_version": 1},
    revision=previous.revision if previous else None,
)
```

返回 `NexusCheckpoint`，含 stage/data/revision/updated_at。data 最大 64 KiB；保存引用和阶段，不存大文件、token 或不可序列化模型对象。应用需要根据阶段决定如何继续。

## 外部副作用与恢复

`ctx.recovery.call(operation_type, request, callback, can_reconcile=...)` 给 callback 提供稳定幂等键；重放已成功操作时可复用记录结果。只有外部系统支持去重/查询且业务实现相应逻辑时，才声明可协调恢复。

`external_operation(...)` 返回上下文管理器；检查 operation.execute，执行后调用 operation.complete(result)。发生异常且结果未知时应让任务暂停协调，不要盲目重复支付、发信或写文件。`NexusRecoveryDiverged` 表示重放请求与已记录流程不一致。

## 模型选择与真实用量

在 `McpToolDescriptor.execution_profiles` 声明可供调用者选择的 `NexusExecutionProfile`。实际选择从 `ctx.execution` 读取；SDK 不会自动调用该模型。只声明你的部署实际支持的模型、reasoning_efforts 与 context_window。

下面的片段假设 `response` 是业务模型客户端已返回的真实响应：

```python
ctx.usage.report(
    model=response.model,
    input_tokens=response.usage.input_tokens,
    output_tokens=response.usage.output_tokens,
    context_window=ctx.execution.context_window,
    event_id="model-call-1",
)
```

不同 provider 的字段需由你的适配层转换；context_window 必须是已知正整数。不要估算 token。重复上报同一次调用保持 event_id 稳定；新的调用使用新 id。Nexus 模型网关可使用 `ctx.usage.gateway_headers()` 归属到 Run，这些头含短期凭据，不能记录或返回给用户。

## 计费与可观测性

`ctx.billing.report` 报告业务账单，`ctx.usage.report` 报告模型 token，用途不同。检查 enabled 并满足 Run 的货币与额度策略；金额使用 Decimal/整数/字符串，参数和 `NexusBillingLineItem` 见参考。

启用 outbox 时使用私有持久目录；同一个活动 Run 恢复后 `ctx.replay_pending()` 重发事件。`ctx.report()` 返回投递统计。completed/fenced Run 不能靠 outbox 重新开启；buffered 不等于已经显示给用户。

完整方法、字段与异常：[reporting API](../reference/modules/reporting.md)；执行配置：[models API](../reference/modules/models.md)。
