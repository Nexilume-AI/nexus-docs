---
title: Data Assets
description: 把 Agent Trace、Memory 和 Output File 转成受治理的集合、不可变 Release 与 Marketplace 交付物。
---

# Data Assets

Data Assets 使用 Dataset/Collection 作为发布容器。当前产品只接收由 Agent 生成且可追溯的三类资产，并在创建 Release 和公开发布前执行脱敏、授权、许可证与扫描门禁。

| 来源类型 | 导入前置条件 |
| --- | --- |
| Conversation Trace | Run 已完成，系统 Redaction 为 `passed`，存在已脱敏事件 |
| Agent Memory | Consent 为 `approved`，License 为 `approved` 或 `internal` |
| Output File | 系统扫描 `passed`、Policy `approved`、License 合格且文件 Hash 未变化 |

## 创建集合并导入

1. 打开 **Data Assets → My Data Assets → Create collection**。
2. 选择集合，点击 **Import Agent asset**。
3. 选择 Agent、Run 与来源类型。
4. Trace 先执行 **Run redaction**，再导出 approved trace；Output File 先执行 **Scan output**，再 Capture；Memory 只会列出门禁合格的条目。
5. 在 **Current assets** 核对来源、大小、Hash 与治理元数据。

Trace 导出只读取 Server 生成的 `redacted_payload_json`；用户不能自行把原始事件标记为已脱敏。Output File 必须先由 Agent 事件报告，用户不能在导入时手填 Workspace Path、Filename 或 License 结论。

## 创建不可变 Release

**Release readiness** 会列出阻塞项。全部通过后，点击 **Review → Create release**。Release 是当时资产、来源与合规元数据的不可变快照；后续新增 Agent 数据时应创建新 Release，而不是修改旧版本。

Release History 可查看资产组成、总大小、创建时间，以及每个文件的 Source Type、Agent、Run、门禁、Hash 与下载地址。

## 设置与发布

在 **Collection settings** 中管理名称、可见性、Pricing Plan、最大容量 Quota 和删除操作。设置为 `public` 时，Server 会再次验证所有 Agent 资产的发布门禁；不合格文件会阻止发布。

Quota 限制集合上传后的总大小，但当前不等于计费强制。资源共享使用 Share；长期团队权限优先使用 [Access](../access/index.md) 中的 Role。

## 从 Marketplace Pull

打开 **Marketplace → Data Assets**，按关键词、免费/付费和更新时间、名称或大小筛选。详情页会展示 Publisher、Release、格式、来源 Agent 数、许可证、敏感度、价格和文件 Manifest。

登录后点击 **Pull release**。首次获取会建立消费记录并按条款计费；已获取的相同 Release 可用 **Open files** 再次打开。Pull 返回受治理的文件 Manifest 和逐文件下载 URL，不会把 Release 复制成可修改版本。

## 验证与排错

- **Run 可见但不能导出 Trace**：确认 Run 以 `RunFinished` 结束并完成系统 Redaction。
- **Output 不能 Capture**：重新 Scan，检查 Policy/License 状态，并确认文件 Hash 未在扫描后变化。
- **无法创建或发布 Release**：展开 Release readiness，逐项修复门禁；不要尝试通过客户端元数据绕过。
- **Pull 被拒绝**：确认已登录、Workspace 正确、Release 仍公开，并在 [Billing](../billing/index.md) 检查 Wallet/订单。

媒体资产和 Dataset 导入已有专用入口；可用操作以 capabilities、权限和 Release readiness 为准。上传或导入成功不等于可公开发布，也不能跳过容量、扫描和授权检查。
