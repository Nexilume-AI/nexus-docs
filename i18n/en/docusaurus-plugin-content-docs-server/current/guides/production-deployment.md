---
sidebar_position: 3
title: How to deploy production
description: Deploy the Nexus API, Console, background tasks, storage, and edge certificates in a verifiable order.
---

# How to deploy production

This guide deploys one production Nexus Server environment. Use [production readiness](../operations/production-readiness.md) to choose topology and failure domains first. For an existing installation, follow [upgrade and rollback](../operations/upgrade-and-rollback.md).

## Prerequisites

- PostgreSQL, Redis, the validated Python 3.14 and Node.js 24 toolchain, and an HTTPS reverse proxy.
- A process supervisor for ASGI, Celery Worker, and Celery Beat.
- Persistent local storage or an S3-compatible bucket for Data Assets.
- Production-only secrets, a backup destination, and a named recovery owner.

## 1. Configure production

Set at least:

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

After choosing real runtimes and storage, set the Agent, Provider, SSH runner, and Dataset variables. See [configuration](../reference/configuration.md) for source-backed defaults.

## 2. Build the Console

```bash
cd nexus_web
npm ci
npm run build
```

The build writes to `nexus_server/static/web/`. Deploy API and Console artifacts from the same release.

## 3. Apply database and static changes

```bash
cd nexus_server
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py check --deploy
```

Run migrations from one release job. Do not let every API or Worker replica migrate concurrently.

## 4. Start the four process types

```bash
python -m uvicorn config.asgi:application --host 0.0.0.0 --port 8000
celery -A config worker --loglevel=INFO
celery -A config beat --loglevel=INFO
```

The fourth type is the HTTPS reverse proxy. Route the Console and `/api/` to ASGI. Permit HTTP/1.1 Upgrade for `/ws/` and expose it as `wss://`. Workers execute asynchronous deployment, health, metric, and settlement jobs. Beat submits entries from `CELERY_BEAT_SCHEDULE`. Production must not use eager mode as a replacement for either process.

## 5. Configure storage and Edge TLS

- A `local` Dataset backend needs a persistent `NEXUS_DATASET_STORAGE_ROOT` across releases.
- An `s3` backend needs a bucket, endpoint/region, and least-privilege credentials.
- OpenWrt Edge requires the device CA, Edge RS256 key, cloud mTLS client certificate, and CA bundle mapping.
- Keep secrets and private keys in secret management, never in images, Git, logs, or docs artifacts.

## Verification

1. Health returns 200 and authenticated `whoami` returns the user.
2. A Computer WebSocket returns 101 and Swagger loads the schema.
3. Submit an asynchronous Health Job and confirm a Worker completes it in Observability.
4. Wait through a Beat interval and confirm a new timestamp without duplicate schedulers.
5. Upload and read a test Data Asset; if Edge is enabled, also verify Device TLS.
6. Create the first recoverable backup with [backup and restore](../operations/backup-and-restore.md).

## Troubleshooting

- **Job stays queued:** inspect Worker, broker URL, and Redis networking. Do not hide the fault by enabling eager mode.
- **Schedules stop or duplicate:** run exactly one Beat and verify clock and schedule.
- **WebSocket returns 200:** traffic reached a WSGI/static upstream. Route to ASGI and forward Upgrade headers.
- **Login returns CSRF 403:** verify external HTTPS origin, secure cookie, and forwarded protocol.
- **Files disappear after a release:** the local root is not persistent or instances use different roots.

## Permission boundaries and current limits

Production deployment requires host, database, Redis, storage, and secret privileges. It is not a Workspace Admin task. This guide does not ship a cloud-specific or Kubernetes template. HA comes from the surrounding database, Redis, storage, and proxy. Database migrations are not assumed reversible; a tested restore is the rollback baseline.

## Current enterprise entrypoint and dedicated workers

`config.settings` remains the enterprise compatibility entrypoint. Do not run `config.base_settings` directly. Database selection supports PostgreSQL only, in order: `DATABASE_URL`, `POSTGRES_*`, prepared local configuration. There is no SQLite fallback.

In addition to ASGI, Celery Worker and Beat, supervise these management commands for the workloads you enable (invoke with `python manage.py` from Server). Use the same deployment environment/Secret and appropriate `NEXUS_PROCESS_ROLE`. API health 200 does not replace execution workers.

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

Python builds also require enablement, a base image and configured network/isolation prerequisites. The root `start-nexus-cloud.ps1` manages the local stack lifecycle but depends on its infrastructure/TLS setup; it is not a universal production installer.
