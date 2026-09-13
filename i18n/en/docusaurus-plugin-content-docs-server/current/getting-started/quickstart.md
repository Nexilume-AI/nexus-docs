---
sidebar_position: 1
title: Start Nexus Community locally
description: Start Community with Docker Compose or follow the Linux and Windows native installation workflows.
---

:::note Repository access
This page references a product source/download repository that is currently private. Publishing these user docs does not make that repository public. Installation steps requiring its files need maintainer-granted access; public downloads are not yet available through those links.
:::

# Start Nexus Community locally

This chapter is for self-hosted **Nexus Cloud Community**. Enterprise users open the Console URL supplied by their administrator and do not need to run a local Server. For enterprise context setup, see [your first Workspace and Project](first-workspace.md).

Community uses a single-owner workspace. Enterprise Access administration, commercial billing, TokenBank, and commercial Marketplaces are excluded. Do not copy enterprise `config.settings`, databases, or the “Access → Create project” procedure.

## 1. Obtain Community source

Use the independent `nexus-cloud-community` repository or a clean source archive supplied by its maintainer. Start in the root containing `deploy/community/compose.yaml`. The repository is currently private and requires authorized access; request a source archive if you do not have access. The mixed enterprise development checkout is not a valid Docker build context.

Install Docker Engine or Docker Desktop with Linux containers and Compose v2. An x86_64 machine with at least 4 GiB available memory is recommended. This Docker workflow does not require Python, Node.js, PostgreSQL, or Redis installed on the host.

## 2. Start with one command

```sh
docker compose -f deploy/community/compose.yaml up -d --build --wait
```

Wait for readiness and open [http://127.0.0.1:18090](http://127.0.0.1:18090). Compose provides the Community API, compiled Console, PostgreSQL, Redis, background workers, durable Agent worker, Beat, and Relay.

The initial account is `owner@example.local`. Retrieve its generated initial password explicitly; startup logs do not print it:

```sh
docker compose -f deploy/community/compose.yaml run --rm --no-deps --entrypoint cat initialize /var/lib/nexus-bootstrap/owner-password
```

Change the password in Settings after signing in. Restarting does not reset it; the bootstrap password remains only the initial credential. There is no separate Vite process or enterprise `createsuperuser` step.

## 3. Inspect and stop

These commands inspect services, read logs, stop, and start again:

```sh
docker compose -f deploy/community/compose.yaml ps
docker compose -f deploy/community/compose.yaml logs --tail 100 web worker
docker compose -f deploy/community/compose.yaml down
docker compose -f deploy/community/compose.yaml up -d --wait
```

`down` retains volumes. Do not add `-v` unless you intend to erase the installation. Back up PostgreSQL, `community-state`, and `bootstrap` together; the database alone cannot recover encrypted content.

## Linux native development

Follow the bundled [complete Linux guide](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/LINUX.md) in order:

1. Prepare Python 3.14, Node.js 24, and a fresh venv. Ubuntu 24.04's default Python 3.12 is too old for this workflow. In WSL, use Linux tools and the Linux filesystem.
2. Install the hashed `linux-py314` dependencies and build the Server wheel. Run `npm ci --ignore-scripts` and `npm run build:community` in `nexus_web`.
3. Provision a dedicated PostgreSQL role/database and an unused Redis database; create the permission-restricted infrastructure JSON.
4. Run `python -m nexus_personal.install prepare` with the installation directory, origin, and `dist/community`, then `initialize` to create the owner. Retain the guide's `NEXUS_INSTALLATION` environment variable.
5. After initialization, run from the source root with the venv activated:

```sh
bash ./start-nexus-community.sh start --installation "$NEXUS_INSTALLATION" --local-http
bash ./start-nexus-community.sh status --installation "$NEXUS_INSTALLATION"
bash ./start-nexus-community.sh check --installation "$NEXUS_INSTALLATION" --local-http
bash ./start-nexus-community.sh stop --installation "$NEXUS_INSTALLATION"
```

The guide's local example opens [http://127.0.0.1:18080](http://127.0.0.1:18080). `--local-http` is for loopback development and must match the initialized origin/port. The launcher does not provision databases, rebuild Web, or restart crashed processes. `status` and `check` do not replace a real workload test.

## Windows native installation

Follow the [Host guide](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/HOST.md), using the `win-py314` dependency locks, compiled Community Web, and a prepared and initialized dedicated installation. For the guide's local loopback test configuration:

```powershell
.\start-nexus-community.ps1 -InstallationDirectory C:\Nexus\Community -LocalHttp
```

Use `-CheckOnly`, `-StopOnly`, and `-Restart` for diagnostics and lifecycle management. Production access requires an HTTPS/WSS reverse proxy without `-LocalHttp`.

## Verification

- Compose services are ready, or native launcher process checks pass.
- The owner can sign in and see the Community workspace and Agents.
- Invoke a configured Agent and inspect its Run result. Successful startup does not prove execution infrastructure is ready.

## Troubleshooting

- **Source or guide inaccessible:** check private repository access or read the same files in the source archive.
- **Port conflict:** set both `NEXUS_PORT` and matching `NEXUS_ORIGIN` before first initialization. Do not simply change an existing installation's origin.
- **Database or migration failure:** inspect logs and the dedicated database configuration; follow recovery instructions instead of deleting migration state.
- **Agent cannot execute:** container controllers, Python builders, and external Providers require separate configuration. Compose does not implicitly grant the host Docker socket.
- **Another device cannot connect:** default HTTP is loopback-only. Remote Computers require HTTPS/WSS configured in advance; see the [Docker guide](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/deploy/community/README.md).

## Next steps

Use the Community [workflow guide](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/WORKFLOWS.md) to configure Agents, models, and devices. OpenWrt, Mobile, the Python SDK, and Computer Runtime are separate releases, not bundled Cloud source. Enterprise users can continue to the [first Agent workflow](first-agent.md).

## Automatic Community Relay startup

The current local implementation includes Relay in normal startup. First start generates installation-owned device CA, Edge signing keys and Relay credentials; restarts reuse them. An OpenWrt checkout is not required. Native launchers need Node.js; the Docker image includes it.

The default tunnel is local-only on port `27444`. To accept routers, select the server IP reachable from those routers on first start:

```powershell
.\start-nexus-community.ps1 -InstallationDirectory C:\Nexus\Community -RelayAddress 192.168.1.10
```

```sh
bash ./start-nexus-community.sh start --installation /srv/nexus-community --relay-address 192.168.1.10
```

For Docker, set `NEXUS_RELAY_ADDRESS=192.168.1.10` and `NEXUS_RELAY_BIND=192.168.1.10` before Compose startup. Replace the example with the actual server IP. Port `27445` is an internal Cloud endpoint requiring mTLS and JWT and is not published.

Relay readiness does not establish public access or completed router pairing. Cloud HTTPS, verified-device-mTLS ingress, owner authorization and firewall setup remain deployment prerequisites. Public IPv6 is not configured automatically. Do not directly change an enrolled installation's advertised IP or delete its credentials.
