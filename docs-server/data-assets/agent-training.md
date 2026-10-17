---
title: Agent 训练数据
---

# Agent 训练数据

在 Data Assets 中选择私有数据集，打开 **Agent training**，可收集对话、工具调用轨迹，标注成功/失败反馈，并导出不可变训练版本。导出不等于 Marketplace 发布，也不会自动启动模型训练。

## 收集完整轨迹

客户端记录用户消息、模型回复、工具定义、调用参数及实际结果，然后显式提交 `nexus.trajectory.v1` JSON。可使用 Python SDK 的 `nexus_agent.training.TrainingClient` 和 `TrainingTrajectory`。Codex、TCagent 等客户端需要接入 SDK 或导出 JSON；MCP 服务端不能从工具日志补造用户提示或模型对话。

同一任务和会话应复用 `task_id`、`session_id`。提交需要确认数据使用权；重试使用相同 `request_key` 和内容，不同内容复用同一个键会被拒绝。单条轨迹最多 1 MiB、1000 条消息、256 个工具定义。二进制产物单独保存。

也可从已有 Agent 运行中一次收集最多 20 条已结束且完成脱敏的记录。缺少工具结果、定义或其他结构信息时保留警告，不能批准用于训练。运行成功与任务结果成功分别记录，外部提交默认结果为 `unknown`。

## 审核与修正

审核消息顺序和工具参数/结果，选择 `success`、`failure` 或 `unknown`，记录评分、反馈及来源。选择需要训练的 assistant 步骤：选中步骤 `weight: 1`，其余上下文 `weight: 0`。系统保存审核者和版本，避免并发覆盖。

修正会产生关联原始 SHA-256 的新样本，原始内容保持不变；新样本需要重新审核。私有数据集才能写入、审核和导出训练数据，已有公开数据集需先取消发布。

## 导出和下载

默认导出已批准且结果成功的样本；失败样本需要显式选择。导出包含 `train.jsonl`、`validation.jsonl`、`test.jsonl`（空分组不生成文件）和 `manifest.jsonl`。Manifest 记录来源、摘要、审核版本、分组和跳过原因，不是训练样本。

相同任务、会话、内容重复及修正关系不会跨越训练/验证/测试分组。按种子确定性划分，比例是目标而非精确数量。小数据集可先使用 0% 验证和测试。当前单次导出最多 500 条轨迹、32 MiB SFT 数据，下载需要认证和数据集权限。

公开 API 路由：

- `GET/POST /api/v1/datasets/{id}/training/samples/`
- `GET/PATCH /api/v1/datasets/{id}/training/samples/{sample_id}/`
- `POST /api/v1/datasets/{id}/training/import-runs/`
- `GET/POST /api/v1/datasets/{id}/training/exports/`

[SDK 示例与完整格式](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/docs/agent-training-data.md) 提供调用方法。训练前仍需审核数据并适配训练框架的工具调用与 loss mask 格式。
