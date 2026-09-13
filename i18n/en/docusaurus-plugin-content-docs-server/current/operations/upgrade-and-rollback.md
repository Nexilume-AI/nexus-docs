---
sidebar_position: 4
title: How to upgrade and roll back Nexus Server
description: Release a new version with a recoverable backup, one migration, and staged verification.
---

# How to upgrade and roll back Nexus Server

An upgrade changes API, Console, background jobs, and database schema together. Prove recovery before releasing artifacts and running one migration. Restarting an old container is not a database rollback.

## Prerequisites

- Tagged old and new Server/Console artifacts.
- A recent successful [backup and restore](backup-and-restore.md) drill.
- Reviewed release changes, migrations, new settings, and runtime compatibility.
- The ability to stop new writes, drain traffic, and inspect job queues.

## 1. Pre-upgrade checks

1. Record version, migration state, configuration, and running instances.
2. Let important deployment/settlement Jobs finish before changing Workers.
3. Back up database and Dataset storage and prove the backup is readable.
4. Run the new migration and smoke tests against a restored isolated copy.
5. Supply explicit values for new secret, storage, runner, and Celery settings.

## 2. Release

1. Pause high-risk writes and stop old Beat to prevent duplicate schedules.
2. Place new Console and application artifacts without widening traffic.
3. Run from one release job:

   ```bash
   python manage.py migrate --noinput
   python manage.py collectstatic --noinput
   python manage.py check --deploy
   ```

4. Start new API and Workers; start exactly one Beat after they are healthy.
5. Restore traffic and writes gradually.

## 3. Post-release verification

- Health, login/whoami, Workspace/Project switch, and Swagger.
- Computer WebSocket 101, sample Agent MCP, and a Provider→Router request.
- One completed Worker Job and one Beat-scheduled task.
- Data Asset read/write, Billing Usage, and Audit Request ID.
- Stable error rate, P95, queue wait, database connections, and storage errors.

## Rollback decision

| Situation | Action |
| --- | --- |
| No migration, or schema is explicitly backward compatible | Drain new instances, restore old app/Console artifacts, verify |
| Schema no longer supports old code | Stop writes, restore database and Dataset backup, then deploy old artifacts |
| Worker only is faulty | Pause affected queue and restore a matching Worker; do not run mixed task code indefinitely |
| Edge/Provider secret config is wrong | Restore config version and rotate exposed secrets; do not blindly restore the database |

## Troubleshooting

- **Migration fails:** keep writes closed and preserve the error/state. Do not repeatedly auto-run a non-repeatable data migration.
- **API works but old Jobs fail:** restore a matching Worker or rebuild Jobs using the task recovery policy.
- **Console uses old fields:** API/static versions differ. Clear proxy/CDN cache and deploy one release.
- **Data is missing after rollback:** compare the actual database and Dataset restore timestamps.

## Permission boundaries and current limits

Only platform operators migrate or restore the database. Workspace Admins cannot authorize infrastructure rollback. Nexus does not promise every Django migration is reversible and does not include blue/green or canary orchestration; the deployment platform supplies it.
