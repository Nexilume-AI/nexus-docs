---
title: Plan Catalog
description: 供 Superuser 管理全局和 Workspace 专属的产品套餐、配额与 Marketplace 数据定价。
---

# Plan Catalog

Plan Catalog 是 Superuser 管理的产品目录。普通用户在 [Billing](../billing/index.md) 查看和购买可见 Plan；只有 `is_superuser` 用户能进入 Plan Catalog，其他用户会被重定向到 Billing。

## Scope 与生命周期

| Scope | 可见范围 | 典型用途 |
| --- | --- | --- |
| Global | 所有 Workspace/Tenant | 标准公开套餐 |
| Tenant custom | 仅指定 Tenant | 协商价格或专属配额 |

Plan Type 为 Models、Agents 或 Dataset；Status 为 Active、Disabled 或 Archived。**Customize** 会把现有 Plan 复制为 Tenant 版本，适合保留标准模板后修改。Archive 停止正常目录使用，但不抹除历史订单。

Plan 的修改只影响未来购买。既有订单保留购买时捕获的金额和条款，因此排查账单时应查看 Order，而不是用当前 Catalog 反推历史价格。

## 可配置能力

- **基础定价**：Name、Price、Currency、Scope、Type 和 Status。
- **Agent runtime resources**：镜像大小、Memory/CPU、导出空间、并发 Run、单次/月度时长、月度 Run、Computer、Mobile、Model Pool Size、Service Account/Token 上限。
- **API token rental**：Included Tokens、有效天数、Overage 开关及每 1K Token 超额价。
- **Data download pricing**：固定下载价、每 GB 价格、Currency、Owner/Platform Revenue Share。

数值字段应使用非负值。Owner Share 与 Platform Share 使用 0 到 1 的比例；发布前应验证两者是否符合平台分账规则，不要仅依赖表单边界。

## 推荐变更流程

1. 先用 Type、Scope 和 Status Filter 找到目标 Plan。
2. 对标准套餐直接 Edit；对谈判套餐使用 Customize 生成 Tenant 副本。
3. 核对 Currency、Quota 和 Revenue Share，保存为 Disabled 进行复核。
4. 切换为 Active 后，用目标 Tenant 的普通账户在 Billing 验证可见性与购买结果。
5. 创建测试订单并检查捕获金额、Entitlement、Usage 与 Invoice，再开放生产购买。

## 安全与排错

- **看不到 Plan Catalog**：确认账户是 Superuser；Tenant Owner 也不自动拥有此入口。
- **Tenant 用户看不到 Plan**：检查 Scope、Tenant ID、Status 和 Plan Type。
- **改价后旧订单不变**：这是预期的历史快照行为。
- **套餐已停用但仍有 Entitlement**：停用/归档影响未来目录与购买，既有权益按订单生命周期处理。
- **分账或限额异常**：同时检查 Catalog 的 `quota_json`、Billing Order/Usage 和 [Observability Audit](../operations/observability.md)。

对生产 Catalog 的创建、修改和归档都应保留 Audit 记录，并通过最小 Superuser 集合控制变更权限。
