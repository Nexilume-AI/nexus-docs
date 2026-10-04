---
title: "Mobile live screen and control"
---

# Mobile live screen and control

Current `main` source adds live video and expanded actions. These additions are
not a claim that the published PyPI `0.48.0` or Android `0.1.1-beta.2` artifacts
contain all of them. Use compatible Cloud, Web, Android and SDK source versions.

## SDK actions

Use the synchronous or asynchronous Mobile API in an authorized Run:

```python
ctx.mobile.press_home()
ctx.mobile.press_recents()
ctx.mobile.long_press(x=120, y=240, duration_ms=800, coordinate_space="pixels")
await ctx.aio.mobile.press_home()
```

Run scopes, device capabilities and online status still apply. Cloud explicitly
rejects new actions an older APK has not advertised. SDK action calls do not
carry video frames and are separate from the Web live player.

## Web live screen

1. Pair the phone and enable the required permissions.
2. Start live screen sharing from its Cloud panel.
3. Approve Android screen sharing on the phone; the Web cannot bypass consent.
4. Click or swipe the current screen. Stale coordinates are rejected after a
   disconnect or geometry change.
5. Stop sharing or revoke the device to end video and subsequent control.

Media uses WebRTC; HTTPS carries bounded signaling, not raw video. Cross-NAT
connections may require TURN and are not guaranteed without it. Community
operators can configure an existing coturn REST service through
`NEXUS_MOBILE_TURN_URLS` and the protected `NEXUS_MOBILE_TURN_SECRET_FILE`.
The shared secret stays on the server; clients receive short-lived credentials.

See [Nexus Mobile LIVE_VIDEO](https://github.com/Nexilume-AI/nexus-mobile/blob/main/docs/LIVE_VIDEO.md)
for deployment and Android privacy restrictions.
