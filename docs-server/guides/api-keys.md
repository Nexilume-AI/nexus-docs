---
sidebar_position: 1
title: 如何创建和使用 API Key
---

# 如何创建和使用 API Key

API Key 适合 Gateway、Agent MCP 和项目集成。明文只在创建响应中出现一次。

## 前置条件

你已登录 Nexus Console，且是租户管理员或目标项目管理员。

## 操作步骤

1. 打开 **Settings → API Keys**，选择租户和可选项目。
2. 创建 Key，并选择 `gateway` 或 `remote_cli` scope。
3. 立即复制 `sk-nexus-...`，保存到密码管理器或 Secret 管理系统。
4. 发送请求：

```bash
curl http://127.0.0.1:8000/api/v1/agents/ \
  -H "Authorization: Bearer $NEXUS_API_KEY" \
  -H "X-Nexus-Tenant: $NEXUS_TENANT_ID"
```

5. 暂停使用时选择 **Disable**；确认永久废弃时选择 **Revoke**。被撤销的 Key 不能重新启用。

## 验证

在 Key 详情中检查 `last_used_at` 和 usage summary。列表接口只返回前缀和哈希后的身份信息，不会再次返回明文。

## 排错

- `Invalid API key`：明文错误或 Key 不存在。
- `API key tenant mismatch`：请求头租户与 Key 所属租户不同。
- `API key project mismatch`：项目级 Key 被用于另一个项目。
- `API_KEY_SCOPE_DENIED`：`remote_cli` Key 被用于 Gateway。

认证模型见[身份与请求路径](../concepts/identity-and-request-path.md)。
