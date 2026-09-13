---
title: Agents
description: 创建、连接 Runtime、部署、授权、观察并发布 Nexus Agent。
---

# Agents

Agent 是 Nexus 中可调用、可授权和可发布的 AI 能力。商业 Console 以用户自有 Runtime 为中心：Docker 镜像运行 MCP HTTP Server，或由 OpenWrt IPv6/Relay 节点托管 Agent 进程。Nexus 管理身份、部署、访问、观测和 Marketplace，不在浏览器中编辑 Agent 源代码。

## Agent 工作区

打开一个 Agent 后，主要操作分为以下页面：

| 区域 | 用途 |
| --- | --- |
| Overview | 查看当前 Runtime 与建议下一步 |
| Runtime | 注册 Docker Image 或绑定 OpenWrt，部署、停止和健康检查，可附加 Computer |
| Access | 创建 Agent Key、导出 MCP、连接 Mobile、查看最近访问事件 |
| Observability | 查看 Run、部署、Runtime、访问和配置事件 |
| Publication | 配置可见性、价格与 Marketplace 发布 |
| Settings | 修改名称、Project、状态和资源默认值 |

## 创建 Agent

1. 选择具体 Workspace 和 Project。
2. 打开 **Agents → Create agent**。
3. 输入 MCP 安全名称：以字母开头，只含字母、数字、`_` 或 `-`，最长 64 个字符。
4. 创建后先保持 private，再连接 Runtime。

创建 Agent 只建立产品身份，不会自动创建容器、OpenWrt 进程或模型 Provider。

## 选择 Runtime

### Docker

适合已有容器基础设施或需要隔离运行的 Agent：

1. 注册 Registry Image reference，或上传 `docker save` tar。
2. 把目标 Image 设置为 Current。
3. 点击 Deploy；Server 在创建部署前重新验证当前 Image。
4. 运行 Health，确认 deployment `active` 且 health `healthy`。

Private Registry Secret 是写入字段，不会从 API 返回。当前版本不提供完整 Registry 凭据生命周期管理，也不支持 Kubernetes 或远程编排器部署。

### OpenWrt IPv6

适合复用用户已有 Router 或边缘设备，避免租用 Docker Runtime：

1. 创建一次性 Edge 配对码。
2. 让 OpenWrt 向 Server 发布 IPv6 Agent 注册。
3. 在 Agent Runtime 中选择未绑定注册并 Bind。
4. 运行 Health 或 MCP 调用验证 IPv6、JWT 和 mTLS 路径。

OpenWrt 负责远端进程生命周期；Nexus 的 Stop 对这类 Runtime 表示断开绑定。完整步骤见[接入 OpenWrt IPv6 Agent](../guides/connect-openwrt.md)。

## 连接 Environment

- **Computer**：Docker Runtime 可在部署时附加 SSH Target、Authorized root 和只读/读写模式；Computer Runtime 还可在调用者的 Private Run 中按授权接入。文件通过 Workspace API 访问，不做目录挂载。
- **Mobile**：在 Agent 的 Mobile 面板连接已配对设备。Mobile 的 Approval mode 和风险判断继续生效。

先阅读 [Environments](../environments/index.md)，并按需要选择 [Computer](../environments/computer.md) 或 [Mobile](../environments/mobile.md)，再授予 Agent 最小访问范围。

## MCP 与 Agent Key

在 **Access** 中创建 Agent Key 并导出 MCP 配置。明文 Key 只显示一次，应立即保存到 Secret 管理系统。Agent `use` 权限允许调用，不允许部署、停止或修改设置；管理操作需要更高权限。

不要把以下凭据混为一类：

- Agent Key：调用单个 Agent。
- Gateway API Key：调用模型 Gateway。
- Service Account Token：CI、后台任务或集成身份。
- OpenWrt Device Token/Certificate：边缘设备注册与续租。

## 状态与生命周期

| 对象 | 常见状态 |
| --- | --- |
| Agent | active、disabled、archived |
| Runtime deployment | deploying、active、stopped、failed |
| Health | unknown、healthy、unhealthy |
| Publication | draft/unpublished、published、suspended |

Archive 或 Delete 前，先确认调用方、Environment Attachment、Marketplace Listing 和计费影响。删除使用软删除语义，不应当作 Secret 撤销的替代操作。

## 发布与计费

发布前配置 Visibility、价格与资源默认值，并确保 Runtime 健康。公开调用会写入 Agent Usage：消费方支出和发布方收益都可以在 [Billing](../billing/index.md) 的 Usage 中查看。公开说明不得包含 Image Registry Secret、Provider Credential、Workspace Token 或用户数据。

## 当前限制

- 不托管真实 Git Repository，旧 Repo API 只保留兼容元数据。
- 不提供 Runtime Log Streaming；Activity 与 Agent Log 是事件记录。
- 文件、Dataset 与执行容量按各自接口校验；以具体错误和限制配置为准。
- 不管理 Registry Credential Rotation。
- 不提供 Kubernetes/远程编排部署；事件重放与恢复能力以具体 Run API 为准。

## 排错顺序

1. 检查顶部 Workspace 和 Project。
2. 检查 Agent 状态、Current Image 或 Edge Registration。
3. 查看部署 Job 和 Health reason。
4. 查看 Agent Activity 与 Observability Audit。
5. 对 403 使用 [Access → Check access](../access/index.md#检查某次访问为什么允许或拒绝)。

首次完整操作见[第一个 Agent 工作流](../getting-started/first-agent.md)。

## Python 源码构建与当前操作页

Agent 页面当前分为 Overview、Runtime、Access、Observability、Publication 和 Settings。Runtime 支持镜像供应，也支持上传一个含顶层 FastMCP 实例的 Python 文件。普通脚本或工厂函数不是可选入口；当前源码语法校验目标为 Python 3.12，不等同于 Cloud 自身的 Python 版本。

上传源文件上限 1 MiB，requirements 文本上限 32 KiB；依赖只能使用允许的包声明，不能夹带 pip 参数、URL、本地路径或 VCS 安装。构建阶段依次为 Queued、Dependencies、Image、Verify tools、Ready。只有构建成功才可选中镜像并部署；构建成功本身不意味着 Runtime 已运行。

构建服务默认受配置开关控制，需要管理员准备基镜像、隔离条件和 `run_agent_python_builds`。在 Runtime 中检查构建失败原因，可删除无镜像的失败记录后重新上传。OpenWrt Runtime 还包括 Relay 连接方式，不能只按 IPv6 地址判断可用性。

交互调用、后续消息、文件与恢复见 [Private Run](private-runs.md)。待回复或失败事项也会进入 [Inbox](../operations/inbox.md)。Agent 自有事件记录不等于无限期容器日志；文件和 Dataset 操作有各自授权、大小及资源限制，不能把旧文档的“无通用 Quota”理解为可绕过这些检查。
