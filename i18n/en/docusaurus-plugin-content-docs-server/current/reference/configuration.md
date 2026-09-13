---
sidebar_position: 2
title: Configuration reference
---

# Configuration reference

Common deployment settings are below; `nexus_server/config/settings.py` is authoritative.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DATABASE_URL` | SQLite when unset | PostgreSQL URL |
| `DJANGO_DEBUG` | `1` | Set `0` in production |
| `DJANGO_SECRET_KEY` | insecure dev value | Sessions and HS256 user JWTs; replace in production |
| `DJANGO_ALLOWED_HOSTS` | `*` | Accepted hosts |
| `NEXUS_PUBLIC_BASE_URL` | `http://localhost:8000` | Public base URL |
| `NEXUS_SECURE_COOKIES` | debug `0`, otherwise `1` | Secure cookies |
| `NEXUS_CSRF_TRUSTED_ORIGINS` | empty | Comma-separated trusted origins |
| `NEXUS_AGENT_RUNTIME_RUNNER` | `fake` | Managed Agent runner |
| `NEXUS_PROVIDER_RUNTIME_RUNNER` | `docker` | Provider runner |
| `NEXUS_ROUTER_RUNTIME_RUNNER` | `nsjail` | Custom Router runner |
| `NEXUS_WORKSPACE_SSH_RUNNER` | `fake` | Use `paramiko` for real Computer SSH |
| `NEXUS_DATASET_STORAGE_BACKEND` | `local` | Local or S3 storage |
| `NEXUS_DATASET_STORAGE_ROOT` | `storage/datasets` | Local Dataset root |
| `NEXUS_DATASET_S3_ENDPOINT_URL` | empty | S3-compatible endpoint; leave empty for AWS S3 |
| `NEXUS_DATASET_S3_BUCKET` | empty | Required bucket for S3 backend |
| `NEXUS_DATASET_S3_REGION` | empty | S3 region |
| `NEXUS_DATASET_S3_ACCESS_KEY_ID` | empty | Optional explicit access key; prefer workload identity |
| `NEXUS_DATASET_S3_SECRET_ACCESS_KEY` | empty | Matching secret key |
| `NEXUS_MEDIA_MAX_UPLOAD_BYTES` | `25000000` | Media upload limit |

## Redis and background jobs

| Variable | Default | Purpose |
| --- | --- | --- |
| `REDIS_URL` | `redis://localhost:6379/0` | Default Redis for broker/results |
| `CELERY_BROKER_URL` | `REDIS_URL` | Broker consumed by Workers |
| `CELERY_RESULT_BACKEND` | `REDIS_URL` | Task result backend |
| `CELERY_TASK_ALWAYS_EAGER` | `1` | In-process local mode; production sets `0` and runs Worker/Beat |
| `CELERY_TASK_TIME_LIMIT` | `300` | Hard task time limit in seconds |
| `NEXUS_DEPLOYMENT_HEALTH_INTERVAL_SECONDS` | `300` | Active Deployment health interval |

`CELERY_BEAT_SCHEDULE` also submits Metrics, Alerts, Reports, and TokenBank work. Run exactly one Beat in production. Settings alone do not start Worker or Beat.

## OpenWrt Edge

| Variable | Default | Purpose |
| --- | --- | --- |
| `NEXUS_EDGE_REQUIRE_MTLS_HEADER` | debug `0`, otherwise `1` | Require verified device certificate metadata |
| `NEXUS_EDGE_ALLOW_WITHOUT_MTLS` | debug `1`, otherwise `0` | Local-development bypass only |
| `NEXUS_EDGE_DEVICE_CA_CERT_FILE` | empty | Managed device CA certificate |
| `NEXUS_EDGE_DEVICE_CA_KEY_FILE` | empty | Managed device CA private key |
| `NEXUS_EDGE_CLIENT_CERT_FILE` | empty | Cloud mTLS client certificate for Edge |
| `NEXUS_EDGE_CLIENT_KEY_FILE` | empty | Cloud mTLS client private key |
| `NEXUS_EDGE_CA_FILE` | empty | Default CA used to verify Edge Server |
| `NEXUS_EDGE_CA_BUNDLES` | `{}` | JSON map from bundle id to Server CA file |
| `NEXUS_EDGE_JWT_PRIVATE_KEY_FILE` | empty | Edge RS256 signing key |
| `NEXUS_EDGE_JWT_TTL_SECONDS` | `120` | Edge invocation token lifetime |

Never commit secrets. Re-run [production verification](../guides/production-deployment.md) after changes and include new state in the [backup inventory](../operations/backup-and-restore.md).
