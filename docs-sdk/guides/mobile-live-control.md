---
title: "手机实时画面与控制"
---

# 手机实时画面与控制

SDK 扩展动作使用 PyPI `nexilume>=0.49.0`；Android 实时画面和控制使用
`0.1.2-beta.1` 或更新版本。部署时仍需兼容的 Cloud 和 Web。
旧 PyPI `0.48.0` 和 Android `0.1.1-beta.2` 不包含这些增量。

## SDK 动作

在已经获得 Mobile 授权的 Run 中使用同步或异步 Mobile API：

```python
ctx.mobile.press_home()
ctx.mobile.press_recents()
ctx.mobile.long_press(x=120, y=240, duration_ms=800, coordinate_space="pixels")
await ctx.aio.mobile.press_home()
```

这些动作仍受 Run 授权 scopes、设备能力和设备在线状态限制。
旧 APK 未声明新动作时，Cloud 会明确拒绝，不假装执行成功。
SDK 动作接口与 Web 的实时播放器不是同一接口；SDK 不传输视频帧。

## Web 实时画面

1. 配对手机并开启所需权限。
2. 在 Cloud 手机面板打开实时画面。
3. 在手机上批准 Android 屏幕共享；网页不能绕过这一步。
4. 点击或滑动当前画面；画面断开或旋转后，过期的坐标控制会被拒绝。
5. 停止共享或撤销设备后，视频与后续控制都不可继续。

视频使用 WebRTC，HTTPS API 只交换有界信令，不转发原始媒体。
不同 NAT 网络可能需要 TURN；未配置 TURN 时，不能保证跨 NAT 可达。
社区版可通过 `NEXUS_MOBILE_TURN_URLS` 和受保护的
`NEXUS_MOBILE_TURN_SECRET_FILE` 配置现有 coturn REST 认证服务。
共享密钥留在服务器，客户端只领取短期凭据。

完整部署及 Android 隐私限制见
[Nexus Mobile LIVE_VIDEO](https://github.com/Nexilume-AI/nexus-mobile/blob/main/docs/LIVE_VIDEO.md)。
