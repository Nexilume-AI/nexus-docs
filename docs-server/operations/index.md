---
title: Operations Overview
description: 从当前 Agent 工作区首页继续 Private Run、处理 Inbox 或准备新 Agent。
---

# Operations Overview

当前 Console 首页为 **Your Agent workspace**，围绕继续个人工作和准备 Agent 展开。企业版用户先选择正确的 Organization/Workspace 和 Project；本地安装方式见[社区版启动指南](../getting-started/quickstart.md)。

## 页面怎么看

| 区域或状态 | 下一步 |
| --- | --- |
| Continue your work | 优先打开需要处理的 Work Inbox 项，或继续当前账号可见的 Private Run |
| Bring your first Agent online | 有创建权限时上传第一个 Python Agent |
| Finish preparing this Agent | 补齐 Runtime 设置并验证 Agent |
| Start a new private Run | 为已经就绪的 Agent 发起新任务 |
| Ready when you are | 查看最近 Agent、运行状态或进入完整 Agents 列表 |

首页会根据权限、资源加载情况和 Run 历史选择主操作。看到无权限或加载失败提示时，先处理该错误；不能把它理解为没有待处理工作。

## 推荐检查顺序

1. 确认当前 Workspace/Project。
2. 有待处理事项时进入 [Inbox](inbox.md)，打开源对象处理。
3. 继续 [Private Run](../agents/private-runs.md)，查看输入请求、输出或恢复选项。
4. Agent 尚未就绪时完成 Runtime 配置；调用失败时进入 [Observability](observability.md)，关联 Jobs、资源指标和 Audit。
5. 余额、套餐与用量在 Billing 核对；Provider 健康在 Providers 或 Model Pool 核对。

## 验证

确认首页操作进入正确的 Inbox 项、Agent 或属于当前账号的 Run。首页摘要不代表完整监控结果；执行成功以实际调用结果为准。

## 排错

- **看不到 Agent**：检查范围和资源权限，不要直接判断资源已被删除。
- **Recent Run status is unavailable**：点击 Retry recent Runs，恢复历史查询后再继续。
- **修复后仍显示异常**：等待刷新，在 Observability 的 Activity → Resource lookup 查询具体资源。
- **页面加载失败**：检查登录、租户上下文和 API 请求，见[常见故障排查](../troubleshooting/common.md)。
