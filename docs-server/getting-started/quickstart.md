---
sidebar_position: 1
title: 在本地启动 Nexus 社区版
description: 使用社区版源码和 Docker Compose 启动本地服务，或按 Linux、Windows 原生安装流程运行。
---

:::note 仓库访问范围
本页部分源码或下载链接指向当前仍为私有的产品仓库。用户文档公开不代表产品仓库已经公开；需要其中安装文件的步骤须先获得维护者授权，不能将这些链接视为已开放的公共下载。
:::

# 在本地启动 Nexus 社区版

本章面向自行安装的 **Nexus Cloud Community**。企业版用户直接访问管理员提供的 Console 地址，无需在自己的电脑上启动 Server；企业版工作上下文见[创建第一个 Workspace 和 Project](first-workspace.md)。

社区版采用单 Owner 工作区，不提供企业版 Access 管理、商业计费、TokenBank 或商业 Marketplace。不要照搬企业版的 `config.settings`、数据库或“Access → Create project”操作。

## 1. 准备社区版源码

使用独立的 `nexus-cloud-community` 仓库或维护者提供的干净源码包，进入含 `deploy/community/compose.yaml` 的根目录。仓库当前为私有，需要已获授权的账号；尚无访问权限时请向维护者获取源码包。不要用混合企业版开发仓库作为 Docker 构建目录。

安装 Docker Engine 或 Docker Desktop（Linux containers）及 Compose v2；建议 x86_64、至少 4 GiB 可用内存。Docker 路径不要求宿主机先安装 Python、Node.js、PostgreSQL 或 Redis。

## 2. 一条命令启动

```sh
docker compose -f deploy/community/compose.yaml up -d --build --wait
```

等待服务就绪，打开 [http://127.0.0.1:18090](http://127.0.0.1:18090)。Compose 同时提供社区版 API、编译后的 Console、PostgreSQL、Redis、后台 Worker、durable Agent worker、Beat 和 Relay。

初始账号为 `owner@example.local`。通过以下命令读取自动生成的初始密码（启动日志不会输出它）：

```sh
docker compose -f deploy/community/compose.yaml run --rm --no-deps --entrypoint cat initialize /var/lib/nexus-bootstrap/owner-password
```

登录后在 Settings 中修改密码。重启不会重置密码，保存的 bootstrap 密码只代表初始凭据。无需另启 Vite，也无需手动运行企业版 `createsuperuser`。

## 3. 查看状态与停止

以下命令依次查看服务、读取日志、停止和再次启动：

```sh
docker compose -f deploy/community/compose.yaml ps
docker compose -f deploy/community/compose.yaml logs --tail 100 web worker
docker compose -f deploy/community/compose.yaml down
docker compose -f deploy/community/compose.yaml up -d --wait
```

`down` 保留数据卷；不要添加 `-v`，除非确实要清空安装数据。备份应同时包含 PostgreSQL、`community-state` 和 `bootstrap`，仅有数据库不足以恢复加密内容。

## Linux 原生开发

如需直接运行源码，请按社区版随附的 [Linux 完整安装指南](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/LINUX.md)依次完成：

1. 准备 Python 3.14、Node.js 24 和新 venv；Ubuntu 24.04 默认 Python 3.12 不符合该流程。WSL 使用 Linux 文件系统和 Linux 工具链。
2. 安装 `linux-py314` 哈希锁定依赖，构建 Server wheel；在 `nexus_web` 执行 `npm ci --ignore-scripts` 与 `npm run build:community`。
3. 创建独立 PostgreSQL 角色/数据库和未使用的 Redis 数据库，准备权限受限的 infrastructure JSON。
4. 用 `python -m nexus_personal.install prepare` 指定安装目录、origin 和 `dist/community`，再用 `initialize` 创建 Owner。保留指南设置的 `NEXUS_INSTALLATION` 环境变量。
5. 完成以上初始化后，从源码根目录、激活的 venv 中启动：

```sh
bash ./start-nexus-community.sh start --installation "$NEXUS_INSTALLATION" --local-http
bash ./start-nexus-community.sh status --installation "$NEXUS_INSTALLATION"
bash ./start-nexus-community.sh check --installation "$NEXUS_INSTALLATION" --local-http
bash ./start-nexus-community.sh stop --installation "$NEXUS_INSTALLATION"
```

指南的本地示例访问 [http://127.0.0.1:18080](http://127.0.0.1:18080)。`--local-http` 仅适合回环地址开发，必须与初始化的 origin/端口匹配。启动器不安装数据库、不自动重建 Web，也不提供进程崩溃自动重启；`status` 和 `check` 不能代替真实业务调用验证。

## Windows 原生安装

按 [Host 安装指南](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/HOST.md)使用 `win-py314` 依赖锁、构建社区版 Web，并准备和初始化独立安装目录。若使用指南中的本地回环测试配置，可运行：

```powershell
.\start-nexus-community.ps1 -InstallationDirectory C:\Nexus\Community -LocalHttp
```

使用 `-CheckOnly`、`-StopOnly` 和 `-Restart` 诊断、停止与重启。正式访问需要 HTTPS/WSS 反向代理，并去掉 `-LocalHttp`。

## 验证

- Compose 服务就绪，或原生启动器的进程检查通过。
- Console 可用 Owner 登录，显示社区版工作区和 Agents。
- 实际调用一个已配置的 Agent 后检查 Run 结果；服务启动成功不代表执行环境已就绪。

## 排错

- **源码或指南打不开**：确认私有仓库访问权限，或使用源码包中的同名文件。
- **端口冲突**：首次初始化前同时配置 `NEXUS_PORT` 和匹配的 `NEXUS_ORIGIN`；已有安装不要直接改 origin。
- **数据库或迁移错误**：检查服务日志和独立数据库配置，按安装指南恢复，不要删除迁移状态。
- **Agent 无法运行**：容器执行控制器、Python builder 与外部 Provider 需要另外配置；Compose 不会自动授予宿主机 Docker socket。
- **其他设备无法连接**：默认 HTTP 仅监听本机；远程 Computer 等需要预先配置 HTTPS/WSS，参见 [Docker 部署指南](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/deploy/community/README.md)。

## 下一步

按社区版 [工作流指南](https://github.com/Nexilume-AI/nexus-cloud-community/blob/main/nexus_server/nexus_personal/WORKFLOWS.md)配置第一个 Agent、模型和设备。OpenWrt、Mobile、Python SDK 与 Computer Runtime 单独发行，不包含在此 Cloud 源码包中。企业版用户继续阅读[第一个 Agent 工作流](first-agent.md)。

## 社区版 Relay 自动启动

当前本地实现已将 Relay 加入正常启动流程。首次启动生成本安装独立的设备 CA、Edge 签名密钥和 Relay 证书，重启复用；无需另行检出 OpenWrt 源码。原生启动需安装 Node.js，Docker 镜像已包含运行时。

默认 Relay 隧道只供本机访问，端口为 `27444`。如果要让路由器连接，在首次启动前选择路由器能够访问的服务器 IP：

```powershell
.\start-nexus-community.ps1 -InstallationDirectory C:\Nexus\Community -RelayAddress 192.168.1.10
```

```sh
bash ./start-nexus-community.sh start --installation /srv/nexus-community --relay-address 192.168.1.10
```

Docker 路径在运行 Compose 前设置 `NEXUS_RELAY_ADDRESS=192.168.1.10` 和 `NEXUS_RELAY_BIND=192.168.1.10`。将示例 IP 换成服务器实际地址。`27445` 是要求 mTLS 和 JWT 的 Cloud 内部调用端口，不对外发布。

Relay 就绪不等于公网访问或路由器配对已经完成。Cloud 的 HTTPS、设备 mTLS 入口、Owner 授权及防火墙仍需按部署指南配置；脚本不会自动配置公网 IPv6。已有安装不要直接更换通告 IP 或删除密钥。
