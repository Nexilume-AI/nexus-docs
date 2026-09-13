---
sidebar_position: 4
title: 如何升级与回滚 Nexus Server
description: 用可恢复备份、单次迁移和分阶段验证安全发布新版本。
---

# 如何升级与回滚 Nexus Server

升级会同时改变 API、Console、后台任务和数据库 Schema。安全顺序是先证明可以恢复，再发布制品并执行一次迁移；不能把“重新启动旧容器”当作数据库回滚。

## 前置条件

- 已构建并标记新旧 Server/Console 制品。
- 最近一次[备份与恢复](backup-and-restore.md)演练通过。
- 已查看版本变更、迁移文件、配置新增项和 Runtime 兼容性。
- 有停止新写入、排空流量和观察 Job 队列的能力。

## 1. 升级前检查

1. 记录当前版本、数据库迁移、配置和运行实例。
2. 等待重要部署/结算 Job 完成，避免在中间状态切换 Worker。
3. 生成数据库与 Dataset 备份，并验证可读取。
4. 在隔离环境用备份副本执行新版本迁移和冒烟测试。
5. 为新配置提供显式值，尤其是 Secret、存储、运行器和 Celery 设置。

## 2. 执行发布

1. 暂停新的高风险写入，并停止旧 Beat，避免发布期间重复触发。
2. 部署新 Console 静态资源与应用制品，但先不扩大流量。
3. 用单一 Release Job 执行：

   ```bash
   python manage.py migrate --noinput
   python manage.py collectstatic --noinput
   python manage.py check --deploy
   ```

4. 启动新 API 和 Worker，确认正常后只启动一个 Beat。
5. 逐步恢复流量和写入入口。

## 3. 发布后验证

- Health、login/whoami、Workspace/Project 切换和 Swagger。
- Computer WebSocket 101、示例 Agent MCP、Provider→Router 最小请求。
- Worker Job 和 Beat 周期任务各至少一个完成。
- Data Asset 读写、Billing Usage、Audit Request ID。
- 错误率、P95、队列等待、数据库连接和存储错误没有异常上升。

## 回滚决策

| 情况 | 动作 |
| --- | --- |
| 新版本未执行迁移或迁移明确向后兼容 | 排空新实例，恢复旧应用/Console 制品，再验证 |
| 迁移改变了旧代码依赖的 Schema | 停止写入，按演练流程恢复数据库与 Dataset 备份，再部署旧制品 |
| 只有 Worker 故障 | 暂停相关队列，恢复匹配版本 Worker；不要让新旧任务代码长期混跑 |
| Edge/Provider Secret 配置错误 | 回滚配置版本并轮换可能泄露的 Secret，无需盲目回滚数据库 |

## 排错

- **迁移失败**：保持写入关闭，保存错误和迁移状态；不要反复自动重跑非幂等数据迁移。
- **API 正常但旧 Job 失败**：新 Worker 与旧任务 Payload 不兼容；恢复匹配 Worker 或按任务恢复策略重建 Job。
- **Console 出现旧字段错误**：静态资源与 API 版本不一致，清理 CDN/代理缓存并部署同一版本。
- **回滚后数据缺失**：记录实际恢复时间点，比较数据库和 Dataset 快照边界。

## 权限边界与当前限制

只有平台部署者可以迁移或恢复数据库。Workspace Admin 无权决定基础设施回滚。项目不保证所有 Django Migration 可反向执行，也不内置蓝绿或金丝雀发布控制器；这些能力由部署平台实现。
