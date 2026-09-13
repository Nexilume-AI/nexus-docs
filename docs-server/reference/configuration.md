---
sidebar_position: 2
title: 配置参考
---

# 配置参考

下表列出部署者最常用的配置。完整默认值以 `nexus_server/config/settings.py` 为准。

## 核心与安全

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `DATABASE_URL` | SQLite（未设置时） | PostgreSQL 连接 URL |
| `DJANGO_DEBUG` | `1` | 生产必须设为 `0` |
| `DJANGO_SECRET_KEY` | 开发占位值 | 会话与 HS256 用户 JWT 密钥，生产必须替换 |
| `DJANGO_ALLOWED_HOSTS` | `*` | 允许的 Host |
| `NEXUS_PUBLIC_BASE_URL` | `http://localhost:8000` | 对外基准 URL |
| `NEXUS_SECURE_COOKIES` | 调试时 `0`，否则 `1` | Secure Cookie |
| `NEXUS_CSRF_TRUSTED_ORIGINS` | 空 | 逗号分隔的可信 HTTPS Origin |
| `NEXUS_JWT_ISSUER` | `nexus-server` | 用户 JWT issuer |
| `NEXUS_JWT_AUDIENCE` | `nexus-client-cli` | 用户 JWT audience |

## 运行时与存储

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `NEXUS_AGENT_RUNTIME_RUNNER` | `fake` | Agent 容器运行器；生产 Docker 部署需显式配置 |
| `NEXUS_PROVIDER_RUNTIME_RUNNER` | `docker` | Provider 运行器 |
| `NEXUS_ROUTER_RUNTIME_RUNNER` | `nsjail` | 自定义 Router 运行器 |
| `NEXUS_WORKSPACE_SSH_RUNNER` | `fake` | Computer SSH；真实连接设为 `paramiko` |
| `NEXUS_DATASET_STORAGE_BACKEND` | `local` | `local` 或 S3 后端 |
| `NEXUS_DATASET_STORAGE_ROOT` | `storage/datasets` | 本地 Dataset 根目录 |
| `NEXUS_DATASET_S3_ENDPOINT_URL` | 空 | S3-compatible Endpoint；AWS S3 可留空 |
| `NEXUS_DATASET_S3_BUCKET` | 空 | S3 后端必需 Bucket |
| `NEXUS_DATASET_S3_REGION` | 空 | S3 Region |
| `NEXUS_DATASET_S3_ACCESS_KEY_ID` | 空 | 可选显式 Access Key；优先使用工作负载身份 |
| `NEXUS_DATASET_S3_SECRET_ACCESS_KEY` | 空 | 对应 Secret Key |
| `NEXUS_MEDIA_MAX_UPLOAD_BYTES` | `25000000` | 媒体上传上限 |

## Redis 与后台任务

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `REDIS_URL` | `redis://localhost:6379/0` | Broker/Result 的默认 Redis |
| `CELERY_BROKER_URL` | `REDIS_URL` | Worker 消费任务的 Broker |
| `CELERY_RESULT_BACKEND` | `REDIS_URL` | 任务结果后端 |
| `CELERY_TASK_ALWAYS_EAGER` | `1` | 本地进程内执行；生产必须设为 `0` 并运行 Worker/Beat |
| `CELERY_TASK_TIME_LIMIT` | `300` | 单任务硬时间上限（秒） |
| `NEXUS_DEPLOYMENT_HEALTH_INTERVAL_SECONDS` | `300` | 活跃 Deployment 周期健康检查间隔 |

`CELERY_BEAT_SCHEDULE` 还触发 Metrics、Alerts、Reports 与 TokenBank 周期工作。生产应恰好运行一个 Beat；只改环境变量不会自动启动 Worker 或 Beat。

## OpenWrt Edge

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `NEXUS_EDGE_REQUIRE_MTLS_HEADER` | 调试时 `0`，否则 `1` | 要求反向代理提供已验证设备证书指纹 |
| `NEXUS_EDGE_ALLOW_WITHOUT_MTLS` | 调试时 `1`，否则 `0` | 仅限本地开发的降级开关 |
| `NEXUS_EDGE_DEVICE_CA_CERT_FILE` | 空 | 托管设备证书 CA |
| `NEXUS_EDGE_DEVICE_CA_KEY_FILE` | 空 | 托管设备证书 CA 私钥 |
| `NEXUS_EDGE_DEVICE_CERT_DAYS` | `90` | 设备证书有效期 |
| `NEXUS_EDGE_CLIENT_CERT_FILE` | 空 | 云端访问 Edge 的 mTLS 客户端证书 |
| `NEXUS_EDGE_CLIENT_KEY_FILE` | 空 | mTLS 客户端私钥 |
| `NEXUS_EDGE_CA_FILE` | 空 | 验证 Edge Server 的默认 CA |
| `NEXUS_EDGE_CA_BUNDLES` | `{}` | `ca_bundle_id` 到 Server CA 文件的 JSON 映射 |
| `NEXUS_EDGE_JWT_PRIVATE_KEY_FILE` | 空 | Edge RS256 调用私钥 |
| `NEXUS_EDGE_JWT_TTL_SECONDS` | `120` | Edge 调用 JWT 有效期 |

Secret 不应提交到仓库。修改生产配置后，重新执行[生产部署验证](../guides/production-deployment.md)，并确认[备份清单](../operations/backup-and-restore.md)覆盖新状态。
