---
title: Routers
description: 在多个 Model Pool 之间配置优先级、成本、延迟、健康或自定义路由。
---

# Routers

Router 是跨 Model Pool 的稳定调用入口。它先从绑定的池中选择一个 Model Pool，再由该池自己的策略选择 Provider Source。因此，Router 策略和 [Model Pool](../model-pool/index.md) 策略是两层决策，不应混为一层。

## 创建和绑定

1. 确保至少有一个可用 Model Pool。
2. 打开 **Routers → Create router**，填写名称。
3. 在 **Configure router → Model Pools** 中选择一个或多个池并保存。
4. 选择策略并点击 **Apply**。
5. Router 部署成功后，从列表点击 **Export access** 获取 Router-scoped Endpoint、API Key、`.env` 与 curl 示例。

只有部署状态为 `deployed` 的 Router 可以导出访问材料。Configure 页面故意不展示调用地址和密钥，以便把配置权限与凭据分发分开。

## 策略选择

| Console 选项 | 内部策略 | 适用场景 |
| --- | --- | --- |
| Priority | `manual_priority` | 明确的主池与备池顺序 |
| Lowest cost | `lowest_cost_pool` | 优先降低池级成本 |
| Lowest latency | `lowest_latency_pool` | 优先低延迟池 |
| Best health | `best_health_pool` | 优先健康状态更好的池 |
| Custom router.py | `custom` | 需要按请求和候选元数据编写选择逻辑 |

内置策略不会执行已上传的 `router.py`。选择 Custom 时，必须先在 **Advanced** 上传草稿并 **Deploy**；没有已部署版本时 Console 会阻止应用 Custom 策略。

## 自定义 router.py

入口函数接收 `request`、`candidates` 和 `context`，返回候选 Deployment ID 的有序列表和可选原因。候选只来自 Router 已绑定的 Model Pool。

运行时使用隔离沙箱：每次调用有临时根目录，只有工作目录可写，运行时路径只读；输入中的 Secret 会被脱敏，Provider Credential 不会进入执行环境。多模态请求中的图片 Data URL 和签名 URL 查询串也会在进入沙箱前脱敏。

不要在代码中硬编码 API Key，也不要假设能访问任意网络、文件或未绑定的模型源。

## Marketplace Provider 与共享

从 Provider Marketplace 点击 **Use in router** 可把 Community Provider Capacity 加为 Router Preference。Preference 影响候选优先级，但不承诺固定流量比例；健康、Quota、价格和 Router 策略仍会共同决定选择。

Router 可通过 **Share** 授权给其他成员。只读授权不能上传、部署、修改策略或价格。跨系统分发调用凭据时，应使用 Export access 生成的 Router-scoped Key，而不是通用 Gateway Key。

## 验证与排错

- 在 Router 列表确认绑定数量、策略和 `deployed` 状态。
- 用 Export access 中的 curl 发出最小请求，再到 [Observability](../operations/observability.md) 查看 Job、Metrics 与 Audit。
- **Custom 无法应用**：先上传并 Deploy `router.py`，确认状态是 deployed runtime source。
- **没有候选**：检查 Router 绑定池、池内 Source 的 enabled/health，以及 Community Provider 的 Quota。
- **访问被拒绝**：确认使用的是该 Router 导出的 Key，并检查 Key Policy、Workspace/Project 与 [Access](../access/index.md)。
