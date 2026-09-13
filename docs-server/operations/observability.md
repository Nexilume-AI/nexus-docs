---
title: Observability
description: 查询指标、后台任务、告警、报告、资源状态和审计记录。
---

# Observability

Observability 把“系统是否健康”和“某次变更/任务为什么失败”放在同一工作区。所有结果都受当前 Tenant/Workspace 隔离；资源级指标还会复用该资源的可见性检查。

## 当前工作区入口

| Tab | 用途 |
| --- | --- |
| Overview | 汇总运行状态与需要调查的事件 |
| Activity | 查询 Jobs 和后台操作，查看任务详情与时间线 |
| Automations | 在 Alerts 与 Reports 子页管理告警规则、报告计划和投递 |
| Audit | 查询审计事件与变更详情，需要 audit 权限 |
| Platform | 平台诊断，需要 platform_diagnostics 权限 |

在 Activity 中打开 **Resource lookup**，按精确 Resource Type/ID 查询资源指标；它不是独立的 Resource Explorer 页签。可见入口由当前账号的监控权限决定。

## 调查一次失败

1. 从 **Overview** 或业务页面取得 Resource ID、Job ID 和大致时间。
2. 在 **Activity → Jobs** 按 Resource Type/ID 筛选，打开失败任务，检查 Status、Result 与 Event Timeline。
3. 在 **Activity → Resource lookup** 查询同一资源的健康、调用或用量指标。
4. 在 **Audit** 用 Resource ID 和时间范围定位部署、策略、权限或状态变更。
5. 若问题持续，用 **Automations → Alerts** 建立阈值规则，并用 Test 验证通知链路。

Job 的 `input_json`、`result_json`、事件元数据和 Audit Snapshot 会递归脱敏。密码、Secret、Token、API Key 与 Credential 不应以明文出现；Key Prefix、Public Key、Model Key 与 Idempotency Key 等明确安全字段可保留。

## 告警和报告权限

监控能力接口决定当前账号的操作权限：`read` 控制读取，`manage` 控制告警管理，`financial` 控制 Reports 入口，`reports` 控制报告管理，`audit` 控制审计，`platform_diagnostics` 控制平台诊断。按钮不可用时应核对当前账号、租户和授权。

Alert 支持系统聚合指标，也可读取非系统资源的最新 Metric Snapshot。触发后会创建 Alert Event 并发送邮件；收件人按规则 Email、创建者 Email、租户 Report Schedule Email 的顺序补充。

## 验证与排错

- 创建 Alert 后点击 **Test**，确认生成事件并收到通知；Test 是合成事件，不代表阈值已经真实越界。
- Report 点击 **Send now** 后检查 Delivery 状态和收件地址。
- **资源无指标**：检查 Resource Type/ID、Workspace 和资源授权；某些指标依赖最新 Snapshot。
- **Job 长时间不结束**：检查该任务对应的后台 Worker、队列和资源状态；Agent、Python 构建与数据导入等任务有各自的 Worker，不能仅检查 Celery。
- **Audit 查不到记录**：确认有 audit 权限，扩大时间范围，并使用资源真实 ID，而不是显示名称。

Prometheus Endpoint 需要认证和 Tenant Header，只输出租户聚合指标且不包含 Secret。当前不提供 Remote-write Ingestion、长期指标压缩/保留策略或 Audit Log Retention Policy。

## 执行任务与 Inbox 的关系

需要立即处理的运行失败、输入请求和资源异常可从 [Inbox](inbox.md) 打开源对象；历史指标、Job 和审计仍在本页调查。Private Run 的进度还依赖 durable Agent worker，Python 构建依赖独立 builder，不能仅凭 Celery 或 API 健康断言这些任务已执行。查看 [Private Run](../agents/private-runs.md) 的取消、恢复与后续消息流程。
