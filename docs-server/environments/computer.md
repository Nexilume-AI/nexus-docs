---
sidebar_position: 1
title: 如何使用 Computer Environment
description: 添加 SSH Target、打开终端、配置工具并安全附加给 Agent。
---

# 如何使用 Computer Environment

Computer 支持主动连接 Cloud 的 Nexus Computer Runtime，也保留 Server 发起连接的 SSH Target。两种连接方式的凭据和权限边界不同。

## 推荐方式：配对 Computer Runtime

1. 在 **Operate → Computer** 选择当前 Project 并创建配对码。
2. 在目标计算机以当前用户安装兼容的 Nexus Computer Runtime；它向 Cloud 主动建立连接，不需要提供 SSH 密码或开放入站端口。
3. 使用页面生成的 `nexus-computer setup` 命令或配对链接。配对码一次性使用并有过期时间，不能复制给其他人。
4. 在设备端确认工作目录和能力范围；回到 Console 检查连接在线。
5. 在 Marketplace Attach 或 Private Display 中选择该 Computer，逐项确认所需权限。配对成功不等于所有 Agent 自动获得访问权。

撤销后设备应重新配对。Run 的终端、文件和浏览器交互继续按调用者、Run 与授权范围校验。已有 SSH Target 使用下面的独立流程；不要把它的管理员终端权限套到所有 Computer Runtime 场景。

## SSH Target 前置条件


- 选择了目标 Workspace 和 Project。
- 你拥有 Computer 管理权限；当前实现中终端访问通常要求 Workspace 管理员。
- 目标主机运行 SSH Server，Nexus Server 能访问其主机和端口。
- 真实 SSH 环境的 Server 配置为 `NEXUS_WORKSPACE_SSH_RUNNER=paramiko`。

## 添加 SSH Target

1. 打开 **Computer**，点击添加 Target。
2. 填写名称、Host、Port、SSH User。
3. 选择 Private key 或 Password 认证并输入凭据。
4. 先执行连接验证，核对主机密钥指纹。
5. 保存后再次执行 Test；健康状态应为 succeeded。

私钥和密码由 Server 加密保存，列表与详情不会返回明文。更新 Target 时，留空凭据表示保留现有 Secret。

## 打开与恢复终端

选择 Target 后点击打开 Session。Console 通过 `/ws/workspace-terminals/{session_id}/` 建立 WebSocket，再由 Server 打开 SSH Shell。

- 成功的 WebSocket 握手是 HTTP `101 Switching Protocols`。
- Linux/macOS 默认使用目标用户 Shell。
- Windows OpenSSH 目标会优先使用 PowerShell。
- `created` 或 `active` Session 可以从页面恢复；点击 **End session** 显式关闭。
- 终端输出默认不持久化，Audit 只记录 Target 与 Session 生命周期事件。

## 配置 Codex 或 Claude Code

打开一个活动 Session，点击 **Configure tools**：

1. 检测远端是否安装 `codex` 或 `claude`。
2. 从 [Providers](../providers/index.md) 选择 Provider Runtime，生成模型 API 配置。
3. 从 [Agents](../agents/index.md) 选择 Agent，添加、替换或删除 MCP 配置。
4. 预览后应用；需要时使用 Rollback 恢复最近备份。

Codex 配置写入 `$CODEX_HOME/nexus.config.toml`，使用 `codex --profile nexus` 启动，不覆盖基础 `config.toml`。API Provider 与 MCP 配置相互独立，修改其中一项不应清除另一项。

## 将 Computer 附加给 Agent

1. 打开 **Agents → Runtime → Deploy**。
2. 在 **Workspace attachment** 选择 Computer Target。
3. 设置 Authorized root，例如 `~/project` 或 `D:/work/customer-a`。
4. 选择：
   - `Read only`：列目录和读文件。
   - `Read/write`：还可以写文件和运行命令。
5. 部署 Docker Runtime。

容器收到 `NEXUS_WORKSPACE_API_URL`、`NEXUS_WORKSPACE_TOKEN`、授权根目录和访问模式，不会收到 SSH Secret，也不会挂载远程目录。文件路径和命令工作目录必须相对 Authorized root，绝对路径和 `..` 穿越会被拒绝。

:::warning 命令执行边界
`Read/write` 允许 Agent 通过远程 Shell 运行命令。Authorized root 限制 Workspace API 的默认工作目录，但命令本身仍以 SSH User 的操作系统权限执行。只把读写环境连接给可信 Agent，并使用权限受限的 SSH 账号。
:::

## 验证

- Target Test 显示 succeeded，并记录最近验证时间。
- 终端状态为 active，Shell 能返回命令输出。
- 工具检测显示命令路径和版本，且不包含 Secret。
- Agent 部署详情显示已附加的 Computer、Authorized root 和 Access mode。

## 排错

| 现象 | 处理 |
| --- | --- |
| Target 保存后仍不健康 | 检查 Server 到 SSH Host 的网络、端口、用户名、Secret 和主机指纹 |
| WebSocket 返回 200 | 后端误用 `manage.py runserver`；改为运行 `config.asgi:application` 的 Uvicorn |
| WebSocket 返回 403 | 检查登录会话、Workspace、管理员权限和可信 Origin |
| Agent 文件访问被拒绝 | 检查相对路径、Authorized root、Access mode 和 Workspace Token 是否仍有效 |
| Windows 命令异常 | 确认 OpenSSH 默认 Shell 和目标探测结果；不要求安装 `sh`、`tar` 或 Node.js |

部署端配置见[生产部署](../guides/production-deployment.md)，完整请求路径见[常见故障排查](../troubleshooting/common.md)。
