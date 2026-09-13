---
sidebar_position: 3
title: 如何备份与恢复 Nexus Server
description: 备份数据库、Data Asset、配置与 Edge PKI，并在隔离环境验证恢复。
---

# 如何备份与恢复 Nexus Server

一次可用备份必须让数据库元数据、Dataset 对象、配置和证书回到同一个时间边界。只复制 PostgreSQL 会留下“Release 存在但文件丢失”的半恢复状态。

## 前置条件

- PostgreSQL 备份工具和数据库恢复权限。
- 本地存储快照能力，或 S3-compatible Bucket 的版本化/复制能力。
- 加密的 Secret/证书备份位置和隔离恢复环境。
- 已记录目标 RPO（最多能丢多久数据）与 RTO（多久恢复服务）。

## 1. 建立备份清单

| 对象 | 必须保存 | 不应进入普通备份日志 |
| --- | --- | --- |
| PostgreSQL | 全库、角色/权限所需元数据、备份时间 | 连接密码 |
| Local Dataset | `NEXUS_DATASET_STORAGE_ROOT` 完整快照 | 用户文件内容和签名 URL |
| S3 Dataset | Bucket 版本、生命周期和目标时间点 | Access Key 明文 |
| 配置 | 非 Secret 环境变量、版本、运行器选择 | Secret 值 |
| PKI/Secret | Django Secret、设备 CA、Edge JWT、mTLS、支付/Provider Secret | 未加密副本 |

## 2. 生成一致备份

先暂停发布、上传、支付和迁移等写入入口，再记录 UTC 时间与应用版本。数据库示例：

```bash
pg_dump --format=custom --file=nexus.dump "$DATABASE_URL"
pg_restore --list nexus.dump
```

随后对本地 Dataset 根目录做同一时间窗口的存储快照，或记录 S3 Bucket 的版本/复制点。最后导出 Secret 管理系统中的版本标识和证书到期信息，而不是把明文写入清单。

## 3. 在隔离环境恢复

1. 创建空 PostgreSQL 数据库、空 Dataset 目标和独立 Redis。
2. 使用与备份匹配的 Server/Console 制品。
3. 恢复数据库：

   ```bash
   pg_restore --clean --if-exists --no-owner --dbname="$RESTORE_DATABASE_URL" nexus.dump
   ```

4. 恢复本地快照或 S3 对象版本，并配置相同的存储后端类型。
5. 从 Secret 管理系统恢复所需 Key/证书；不要复用生产网络入口。
6. 启动 API、Worker 和 Beat 前，先确认恢复环境不会发送真实支付回调、通知或生产 Edge 命令。

## 验证

- 健康与登录成功，Workspace、Project、Role 和 Resource Share 数量合理。
- 抽查 Agent、Provider、Router、Billing Order、Audit 和 Job。
- 抽取至少一个历史 Data Asset，按 Manifest 读取并校验对象。
- 用隔离凭据完成一次示例 Agent 调用和异步 Job。
- 记录实际 RPO/RTO、缺失项和下一次演练日期。

## 排错

- **数据库恢复成功但文件 404**：Dataset 快照时间、Backend 或 Bucket 不一致。
- **所有会话失效**：Django Secret 与备份时不同；这是轮换后的预期结果，重新登录即可。
- **Edge 全部失败**：设备 CA、Edge JWT 私钥、Key ID 或 CA bundle 没有成套恢复。
- **恢复环境产生真实副作用**：立即停 Worker/Beat，隔离网络并轮换受影响凭据。

## 权限边界与当前限制

备份包含用户、权限、账本和可能的用户文件，只允许备份管理员访问并必须加密。Nexus 不内置跨数据库与对象存储的原子快照，也不内置一键恢复；一致时间点、保留策略和异地复制由部署平台负责。
