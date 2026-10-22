---
title: 公网波形查看器
---

# 公网波形查看器

Wave MCP 可以返回直接在浏览器打开的波形链接。11 上的 worker 保持无网络、无主机挂载的隔离配置；桥接服务通过 Run Files 上传选定的 FST 快照，Cloud 提供带独立鉴权的 Surfer 页面。不需要 SSH 隧道，也不需要开放 worker 的入站端口。

## 使用步骤

1. 调用 `create_wave_workspace(sample=true)`，保留 `workspace_id` 和 `workspace_key`。
2. 调用 `open_wave_view`，传入工作区凭据、`fst_paths: ["/work/sample/dump.vcd"]` 和 `signals: [{"path": "top_tb.u_counter.count"}]`。VCD 会自动转换为 FST。
3. 在浏览器打开返回的完整 `url`。页面会显示波形，并提供私有 FST 下载。
4. 调用 `update_wave_view` 修改信号、游标、范围或标记；页面通过 SSE 接收更新。修改后的画布会重新加载。注释使用 `annotation: {"markdown": "说明文字"}`，页面以安全的纯文本显示。
5. `get_view_state` 返回浏览器加载状态和新链接；`close_wave_view` 关闭并撤销访问。

两份波形会并排显示，各自按文件的时间单位换算游标和标记。浏览器就绪表示渲染器加载了波形；不代表所有输入的信号名都存在。

## 链接与身份

- 链接有效期为 10 分钟，只能兑换一次；票据位于 URL 的 `#` 片段，不写入请求路径。
- 页面移除地址中的票据后，兑换仅限当前查看页的 Secure、HttpOnly、SameSite=Strict Cookie。
- 浏览器会话自查看页创建起最多持续一小时，同一浏览器可以刷新。
- 调用 `get_view_state` 或 `list_wave_views` 可以在这一小时内获取新链接。兑换新链接后，旧浏览器会话失效。
- 查看链接只允许访问选定的波形快照，不提供发布者账号、Router、API Key 或其他文件的权限，也不要求登录 Nexus。
- 一个 API Key 对应一个调用者。不同 Key 即使知道工作区 ID 和私密 key，也不能读取、更新或关闭别人的查看页。
- 明确关闭查看页或工作区会撤销浏览器访问。撤销调用者 API Key、禁用 Agent 也会拒绝访问。
- worker 空闲回收或重启后，已上传的 Cloud 快照保留至独立的一小时期限；文件仍遵循 Run Files 的保留策略。

请将尚未兑换的完整链接视为私密凭据。

## 部署

Cloud 线上版使用 Agent 迁移 `0066_agent_wave_view`，开源 Personal 版使用 `0008_agent_wave_view`。安装与 SDK 示例 `OPTIONALS.md` 指定版本一致的 `surfer.js` 和 `surfer_bg.wasm` 到 `/opt/nexus-wave-viewer`，或通过 Django 设置 `NEXUS_WAVE_ASSET_ROOT` 指定目录。保留 Surfer 的 EUPL 许可证、源码版本和构建记录。

`NEXUS_PUBLIC_BASE_URL` 必须是 HTTPS 公网地址，Redis 用于事件推送。同步 SDK 的 `nexus_agent.wave_views`、Wave 桥接程序及 worker 后，公开工具数为 45；私有 `_nexus_export_wave_view` 不得注册到 Marketplace。

每个查看页最多两份文件，每份不超过 256 MiB；工作区总存储仍为 256 MiB。每工作区最多四个查看页，同一调用者与 Agent 范围最多八个未过期查看页。FSDB 仍需另行提供兼容的专有 FsdbReader 库。

开源 Personal 版使用其自身已验证的账号身份，并检查调用记录关联的托管 Agent 凭据和设备绑定。它不接受线上版 Enterprise API Key。
