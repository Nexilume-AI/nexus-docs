---
sidebar_position: 3
title: 如何部署生产环境
description: 按可验证顺序部署 Nexus API、Console、后台任务、存储与边缘证书。
---

# 如何部署生产环境

本指南把一套 Nexus Server 部署到单个生产环境。开始前先用[生产就绪架构](../operations/production-readiness.md)决定拓扑、容量和故障域；升级已有环境时改用[升级与回滚](../operations/upgrade-and-rollback.md)。

## 前置条件

- PostgreSQL、Redis、已验证的 Python 3.14、Node.js 24 和 HTTPS 反向代理。
- 可运行 ASGI、Celery Worker 和 Celery Beat 的进程管理器。
- 本地持久卷或 S3-compatible Bucket，用于 Data Assets。
- 独立的生产 Secret、备份位置和恢复负责人。

## 1. 配置生产环境

至少设置：

```dotenv
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=<strong-random-secret>
DJANGO_ALLOWED_HOSTS=nexus.example.com
DATABASE_URL=postgresql://<user>:<password>@<postgres-host>:5432/<database>
NEXUS_PUBLIC_BASE_URL=https://nexus.example.com
NEXUS_SECURE_COOKIES=1
NEXUS_CSRF_TRUSTED_ORIGINS=https://nexus.example.com
REDIS_URL=redis://<redis-host>:6379/0
CELERY_BROKER_URL=redis://<redis-host>:6379/0
CELERY_RESULT_BACKEND=redis://<redis-host>:6379/0
CELERY_TASK_ALWAYS_EAGER=0
```

选择真实运行器和存储后，再设置 `NEXUS_AGENT_RUNTIME_RUNNER`、`NEXUS_PROVIDER_RUNTIME_RUNNER`、`NEXUS_WORKSPACE_SSH_RUNNER` 与 Dataset 存储变量。完整默认值见[配置参考](../reference/configuration.md)。

## 2. 构建 Console

```bash
cd nexus_web
npm ci
npm run build
```

构建结果写入 `nexus_server/static/web/`。同一发布版本的 API 与 Console 必须一起部署。

## 3. 应用数据库与静态资源

```bash
cd nexus_server
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py check --deploy
```

迁移只能由一个发布任务执行。不要让每个 API/Worker 副本同时执行迁移。

## 4. 启动四类进程

```bash
python -m uvicorn config.asgi:application --host 0.0.0.0 --port 8000
celery -A config worker --loglevel=INFO
celery -A config beat --loglevel=INFO
```

第四类是 HTTPS 反向代理。把 Console 与 `/api/` 转到 ASGI；`/ws/` 必须允许 HTTP/1.1 Upgrade，并从外部使用 `wss://`。Worker 执行异步部署、健康、指标和结算任务；Beat 只负责按 `CELERY_BEAT_SCHEDULE` 触发周期任务。生产不能继续使用 eager 模式代替这两个进程。

## 5. 配置存储和 Edge TLS

- `local` Dataset 后端需要跨发布持久保存 `NEXUS_DATASET_STORAGE_ROOT`。
- `s3` 后端需要 Bucket、Endpoint/Region 与最小权限凭据。
- 使用 OpenWrt Edge 时，配置设备 CA、Edge RS256 私钥、云端 mTLS 客户端证书和 CA bundle 映射。
- Secret 和私钥只进入 Secret 管理系统，不进入镜像、Git、日志或文档构建产物。

## 验证

1. `/api/v1/health/` 返回 200，登录后 `/api/v1/auth/whoami/` 返回当前用户。
2. Computer WebSocket 握手返回 101；Swagger 能加载 Schema。
3. 创建一个异步 Health Job，确认 Worker 执行并在 Observability 中完成。
4. 等待一个 Beat 周期，确认周期任务有新时间戳且没有重复调度器。
5. 上传并读取测试 Data Asset；若启用 OpenWrt，再完成一次 Device TLS 验证。
6. 按[备份与恢复](../operations/backup-and-restore.md)生成首份可恢复备份。

## 排错

- **Job 一直 queued**：检查 Worker、Broker URL 和 Redis 网络，不要临时打开 eager 掩盖故障。
- **周期任务不运行或重复**：确认恰好一个 Beat 实例，并核对时钟和 schedule。
- **WebSocket 返回 200**：流量进入了 WSGI/静态上游；改为 ASGI 并传递 Upgrade 头。
- **登录后 403 CSRF**：核对外部 HTTPS Origin、Secure Cookie 和代理转发协议。
- **上传成功但发布后文件消失**：本地存储没有持久卷，或新实例指向了不同目录。

## 权限边界与当前限制

- 生产部署需要主机、数据库、Redis、存储和 Secret 管理权限，不应交给普通 Workspace Admin。
- 本指南不提供云厂商、Kubernetes 或数据库集群的一键模板。
- HA 依赖外部数据库、Redis、存储和反向代理能力；Server 配置本身不替代这些设施。
- 数据库迁移不默认可逆。回滚以已验证备份恢复为安全基线。

## 当前企业版入口与专用后台进程

`config.settings` 保持为企业版兼容入口，加载完整企业配置；不要直接运行 `config.base_settings`。数据库配置只支持 PostgreSQL，优先级为 `DATABASE_URL`、`POSTGRES_*`、已准备的本机配置；没有 SQLite fallback。

除 ASGI、Celery Worker 和 Beat 外，按启用的工作负载监督以下 management commands（从 Server 目录使用 `python manage.py` 调用）。各进程使用同一部署环境和 Secret，设置适当的 `NEXUS_PROCESS_ROLE`；不要因 API health 为 200 就省略实际执行进程。

| Command | Role |
| --- | --- |
| `run_agent_tasks` | Durable Agent execution |
| `run_agent_runtime_reconciler` | Runtime state reconciliation |
| `run_agent_python_builds` | Python upload image builds, when enabled |
| `run_dataset_import_worker` | Dataset import jobs |
| `run_dataset_maintenance` | Dataset maintenance |
| `run_provider_maintenance` | Provider maintenance |
| `run_observability_worker --mode scheduler` | Monitoring scheduling |
| `run_observability_worker --mode delivery` | Monitoring delivery |
| `run_work_inbox_worker` | Work Inbox synchronization/delivery |

Python 构建还需要启用开关、基镜像与经过配置的网络/隔离条件。不要只打开开关便接受不受控上传。根目录 `start-nexus-cloud.ps1` 提供本机多进程生命周期入口，但依赖该环境的基础设施和 TLS 配置，不是任意主机通用的一键生产安装器。
