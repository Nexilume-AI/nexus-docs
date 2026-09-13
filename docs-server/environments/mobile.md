---
sidebar_position: 2
title: 如何使用 Mobile Environment
description: 配对 Android 设备、设置审批策略、运行操作并连接 Agent。
---

# 如何使用 Mobile Environment

Mobile 把 Android 设备作为受保护执行环境。Console 可以观察设备状态、请求截图并派发操作；Agent 也可以通过 Nexus 的 MCP 接口使用同一组受控工具。

## 配对 Android 设备

1. 打开 **Mobile**，点击 **Pair Android device**。
2. 输入设备名称，选择 Approval mode。
3. 创建配对 QR，并在 Nexus Mobile 中扫描。
4. 在 Android 上启用 Nexus Mobile Control 的 Accessibility 权限。
5. 返回 Console，等待首次心跳。状态变为 online 后即可打开 Control。

配对 Token 有有效期且只显示在配对流程中。过期后使用 **Re-pair** 或 Rotate token 生成新的 QR；旧 Token 随即失效。

## 生命周期状态

| 状态 | 含义 | 下一步 |
| --- | --- | --- |
| `awaiting_pairing` | 尚未收到设备首次连接 | 扫描配对 QR |
| `setup_required` | 已配对，但 Accessibility 未启用 | 在 Android 完成权限设置 |
| `online` | 心跳新鲜且能力可用 | 打开 Control 或连接 Agent |
| `offline` | 心跳超过允许间隔 | 打开 Nexus Mobile，检查网络和权限 |
| `token_expired` | 未完成配对且 Token 已过期 | 重新生成配对 QR |
| `disabled` | 设备被管理员禁用 | 重新启用后再使用 |

## 审批策略

| 模式 | 行为 | 建议用途 |
| --- | --- | --- |
| Manual | 所有操作等待管理员批准 | 共享设备或敏感生产设备 |
| Confirm high risk | 低、中风险直接排队，高风险等待批准 | 默认选择 |
| Auto | 所有操作自动排队 | 仅限可信测试设备；需要 Mobile policy admin |

输入文本属于高风险操作；包含支付、发送、删除等敏感词的点击也会提升为高风险。审批人可以 Approve 或 Reject，尚未完成的操作可以 Cancel。

## 运行受保护操作

在设备 Drawer 的 **Control** 中可以执行：Observe、Capture screen、Tap text、Tap coordinates、Type text、Swipe、Back、Open app 和 Wait for state。

每个操作都有状态：`pending_approval`、`queued`、`running`、`succeeded`、`failed`、`rejected` 或 `canceled`。在 **Activity** 中检查参数摘要、风险、审批人、结果和错误。

截图只在设备声明 screenshot 能力时可用，并按 Server 配置的短 TTL 保存。响应使用 `private, no-store`，不应当作长期审计文件。

## 连接 Agent 或 MCP 客户端

- 在 **Agents → Access → Mobile** 中连接或断开设备。
- 或在 Mobile 设备设置中导出 MCP 配置，使用 Nexus API Key 调用该设备的 MCP Endpoint。

MCP 暴露与 Console 相同的受控工具，不绕过风险策略。调用者仍需 `mobile.use`、Mobile 管理权限、Workspace 管理权限或设备创建者权限之一。

## 验证

- Device 状态为 online，并显示最近心跳、当前 App 与能力。
- Control 能创建操作；需要批准的操作先进入 `pending_approval`。
- Activity 中能看到最终状态和非敏感错误。
- 连接到 Agent 后，Agent Mobile 面板显示该 Device。

## 排错

- **一直 awaiting pairing**：确认 QR 未过期，Mobile 使用的 Server URL 可从设备访问。
- **setup required**：打开 Android Accessibility 设置并启用 Nexus Mobile Control。
- **offline**：检查 App 是否运行、网络是否可达、系统是否限制后台心跳。
- **操作无法派发**：设备必须 online；检查 Approval mode、权限及操作参数。
- **截图不可用**：设备必须上报 screenshot capability，且截图可能已经超过 TTL。

访问控制见 [Access](../access/index.md)，Agent 连接见 [Agents](../agents/index.md)。
