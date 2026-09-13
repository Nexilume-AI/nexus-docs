---
sidebar_position: 3
title: How to back up and restore Nexus Server
description: Back up the database, Data Assets, configuration, and Edge PKI, then prove recovery in isolation.
---

# How to back up and restore Nexus Server

A useful backup returns database metadata, Dataset objects, configuration, and certificates to one time boundary. Copying PostgreSQL alone can leave a Release whose files no longer exist.

## Prerequisites

- PostgreSQL backup tools and restore permission.
- Local volume snapshots or versioning/replication for an S3-compatible bucket.
- Encrypted secret/certificate storage and an isolated recovery environment.
- Defined RPO (maximum data loss) and RTO (recovery time).

## 1. Build the inventory

| Object | Preserve | Keep out of ordinary logs |
| --- | --- | --- |
| PostgreSQL | Full database, required role metadata, backup time | Connection password |
| Local Dataset | Complete `NEXUS_DATASET_STORAGE_ROOT` snapshot | User content and signed URLs |
| S3 Dataset | Bucket versions, lifecycle, target point | Access key plaintext |
| Configuration | Non-secret variables, version, runner choices | Secret values |
| PKI/secrets | Django, device CA, Edge JWT, mTLS, payment/Provider secrets | Unencrypted copies |

## 2. Create a consistent backup

Pause publication, upload, payment, and migration writes, then record UTC time and application version.

```bash
pg_dump --format=custom --file=nexus.dump "$DATABASE_URL"
pg_restore --list nexus.dump
```

Snapshot the local Dataset root in the same window, or record the S3 version/replication point. Record secret version IDs and certificate expiry, not plaintext, in the manifest.

## 3. Restore in isolation

1. Create an empty PostgreSQL database, Dataset target, and Redis instance.
2. Use Server and Console artifacts matching the backup.
3. Restore the database:

   ```bash
   pg_restore --clean --if-exists --no-owner --dbname="$RESTORE_DATABASE_URL" nexus.dump
   ```

4. Restore the volume snapshot or S3 versions and select the same backend type.
5. Restore keys/certificates from secret management without exposing production ingress.
6. Before starting Worker/Beat, block real payment callbacks, notifications, and production Edge commands.

## Verification

- Health and login succeed; Workspace, Project, Role, and Share counts are plausible.
- Sample Agents, Providers, Routers, Billing Orders, Audit, and Jobs.
- Read and verify at least one historical Data Asset from its Manifest.
- Complete one sample Agent call and asynchronous Job with isolated credentials.
- Record measured RPO/RTO, gaps, and the next drill date.

## Troubleshooting

- **Database works but files return 404:** snapshot time, backend, or bucket does not match.
- **All sessions expire:** the Django secret changed. Reauthentication is expected after rotation.
- **All Edge calls fail:** restore device CA, Edge JWT key/ID, and CA bundles as a set.
- **Recovery causes production side effects:** stop Worker/Beat, isolate networking, and rotate affected credentials.

## Permission boundaries and current limits

Backups contain users, permissions, ledgers, and possibly user files. Encrypt them and restrict them to backup operators. Nexus has no atomic database/object-store snapshot or one-click recovery; the deployment platform owns consistency, retention, and off-site copies.
