---
sidebar_position: 3
title: 连接 Computer Runtime
---

# 连接 Computer Runtime

Computer Runtime 以当前系统用户运行，通过出站 WSS 连接 Nexus Cloud，不要求公网 IP 或入站 SSH 端口。

## 配对并验证

先[安装](../quickstart/installation.md) `computer` 扩展；浏览器操作另需 `browser`。在 Nexus Cloud 工作区创建 Computer 配对链接，以普通用户运行：

```sh
python -m pip install "nexilume[computer,browser]==0.47.0"
nexus-computer setup "<pairing-url-from-nexus-cloud>"
nexus-computer status
```

等待注册显示 `connected`。调用者在 Run 中绑定 Computer 并授权文件、命令或浏览器权限，Agent 才能使用对应能力。每个注册有独立的工作区根目录、设备身份和重连循环。同一台电脑可对多个工作区分别执行 setup。

```sh
nexus-computer logs
nexus-computer restart
nexus-computer repair
nexus-computer unpair --registration <registration-id>
```

`repair` 修复已有注册的自启动；`unpair` 撤销指定注册。不要删除设备密钥或恢复屏障文件来重试未确认的配置写入。私有 Cloud 的配对链接可携带公开 CA 信任锚，setup 验证后保存；`--ca-file` 是管理员恢复覆盖选项。

## Linux 浏览器

可安装系统 Chrome/Chromium，或使用 Playwright 下载：

```sh
python -m playwright install chromium
```

最小系统可能还需 `python -m playwright install-deps chromium` 安装系统库，该步骤可能请求管理员权限。

对 Playwright 下载或自定义位置的浏览器，配置服务环境：

```sh
systemctl --user edit nexus-computer.service
```

```ini
[Service]
Environment="NEXUS_BROWSER_EXECUTABLE=/absolute/path/to/chrome"
Environment="NEXUS_BROWSER_HEADLESS=true"
```

将路径替换为真实浏览器可执行文件，再执行：

```sh
systemctl --user daemon-reload
nexus-computer restart
```

仅安装 Playwright Python 包不会安装浏览器；在交互 shell 中设置环境变量也不会更新已启动的 systemd 服务。无桌面的 Linux 使用 headless 模式。

## Attached Computer 二进制文件（待发布）

开发版 SDK 和配套 Cloud 已增加二进制 Workspace API；当前 PyPI 版本尚未包含。
使用前需更新 Cloud 与 Computer Runtime，Runtime 必须声明 `workspace.binary.v1`。
旧版不支持时明确返回错误，SDK 不会降级为文本写入。

```python
# 操作调用者 Attach 的 Computer，不是 Agent 所在主机。
data = ctx.workspace.read_bytes("images/input.png")
ctx.workspace.write_bytes("images/result.png", data)

# 大文件：Agent 本地文件 ↔ Attached Computer Workspace。
ctx.workspace.upload("/agent-local/result.zip", "exports/result.zip")
ctx.workspace.download("exports/result.zip", "/agent-local/download.zip")

# 同步接口均有 ctx.aio.workspace 的异步对应接口。
data = await ctx.aio.workspace.read_bytes("images/input.png")
await ctx.aio.workspace.write_bytes("images/result.png", data)
```

需要已有 `files.read` / `files.write` 授权。内存读写上限 16 MiB；文件流式传输上限
1 GiB，按 256 KiB 分块，通过 HTTPS 传输内容，WSS 仅携带命令控制信息。
空文件、非 UTF-8 内容和中文文件名均支持。SHA-256 校验通过后才原子替换目标，
提交前失败不覆盖原文件；空闲 15 分钟后清理临时句柄，Runtime 重启后需重新传输。
提交响应丢失时先检查目标摘要；连接错误不会自动重放写入。

相对路径以开始传输时的 Run Workspace folder 为准；后续切换 folder 不移动正在
传输的文件。`ctx.files` 是 Cloud Run 输入/产物接口，不是 Attached Computer
Workspace；本接口不会自动把文件归档为 Run Output。

## 验收与排错

Ubuntu 24.04 / Python 3.12 / WSL2 systemd 已实测配对、WSS、Cloud 命令队列、UTF-8 文件读写、命令执行、路径越界拒绝、Chromium 点击与截图，以及重启后身份保留和自动重连。

若状态一直 reconnecting，检查 `logs`、Cloud 可达性和 TLS 信任。社区版截图上传失败时，服务器应将 Django `MEDIA_ROOT` 指向实例的可写媒体目录；只读源码目录不能用于存储截图。此服务端修复已在本地验收环境验证，不代表旧安装包已经包含修复。

上述验收不是所有 Linux 发行版或 macOS 的认证。`computer` 扩展使用 cryptography 50.x；Intel macOS 需要独立验证源码构建工具链。
