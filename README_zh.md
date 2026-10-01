<div align="center">

# Nexus Documentation

**Choose a goal. Follow a guide. Build with Nexus.**

[![Python SDK on PyPI](https://img.shields.io/pypi/v/nexilume.svg)](https://pypi.org/project/nexilume/)
[![License: Nexus Community](https://img.shields.io/badge/License-Nexus_Community-17251d.svg)](LICENSE)
[![文档](https://img.shields.io/badge/Read-the_docs-b8ef73.svg)](README_GUIDE.md)
[![引用项目](https://img.shields.io/badge/Cite-this_software-e8e9e4.svg)](#引用)
[![Repository checks](https://github.com/Nexilume-AI/nexus-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/Nexilume-AI/nexus-docs/actions/workflows/ci.yml)

`Guides` · `English / 中文` · `Docusaurus`

[English](README.md) · **简体中文**

[功能](#从目标开始) · [快速开始](#快速开始) · [项目生态](#项目生态) · [参与贡献](#参与贡献) · [引用](#引用)

</div>

Nexus Server、OpenWrt、Python SDK 与 TokenBank 的中英文用户指南、教程和参考。

![Nexus Documentation 流程示意图](docs/media/overview.svg)

*这是流程示意图，不是产品截图。实际连接需要完成下文的安装、配置与授权。*

## 产品实景

**Enterprise 企业版 · 2026 年 10 月 1 日实机采集。** 展示 Python Agent 从内联提问到生成
私有 Markdown 文件的流程。示例真实运行在 Docker 中，采用确定性逻辑，不调用外部模型，
不连接个人设备。

![Private Display 在对话中展示 Agent 问题](docs/media/enterprise-inline-question.jpg)

<details>
<summary>查看文件产物预览</summary>

![Run Files 中预览生成的发布清单](docs/media/enterprise-file-preview.jpg)

</details>

[采集说明与可复现源码](docs/media/capture-notes.md)。这些是真实截图，不是设计稿；这里展示的企业版菜单
与商业功能，不会因为出现在文档中就成为社区版功能。

## 从目标开始

| 我想…… | 阅读 |
| --- | --- |
| 部署和使用 Cloud | [Server 指南](docs-server) |
| 开发 Python Agent | [SDK 指南](docs-sdk) |
| 配置边缘路由 | [OpenWrt 指南](docs-openwrt) |
| 了解 TokenBank | [TokenBank 文档](docs-tokenbank) |
| 改进或部署文档站 | [构建参考](README_GUIDE.md) |

本仓库是中英文文档、网站代码与示例，**不是 Server 或 TokenBank 应用源码**。公开企业功能文档不代表企业实现开源。

## 快速开始

本地构建需要 Node.js 22 LTS 与 Python 3.12+：

```sh
npm ci --ignore-scripts
npm run check:docs
npm start
```

打开 Docusaurus 打印的地址。英文站使用 `npm run start:en`。普通构建不需要 Cloud 账号、数据库或私有源码。

Python SDK 已以 [`nexilume`](https://pypi.org/project/nexilume/) 发布，导入名保持 `nexus_agent`。安装核心 SDK：

```sh
python -m pip install --upgrade nexilume
```

安装 extras、旧包迁移及 Computer 连接见[SDK 安装指南](docs-sdk/quickstart/installation.md)。

## 文档维护

- 根据实际安装的组件版本选择文档，不混用历史快照。
- [静态构建与托管](README_GUIDE.md#hosting)：部署者配置自己的 HTTPS 域名与路径。
- [SDK API 文档维护](README_GUIDE.md#sdk-documentation-maintenance)：只有再生成 API 参考才需要额外源码。
- [贡献指南](CONTRIBUTING.md)：修复示例、链接或翻译时保留版本上下文。

此首页使用仓库内入口，不假定一个尚未确认可访问的公开文档域名。

## 项目生态

| 项目 | 职责 |
| --- | --- |
| [Cloud Community](https://github.com/Nexilume-AI/nexus-cloud-community) | Server、Web Console 与配套 Cloud Relay |
| [Python SDK](https://github.com/Nexilume-AI/nexus-agent-sdk-python) | Agent 应用与主动出站的 Computer Runtime |
| [OpenWrt](https://github.com/Nexilume-AI/nexus-openwrt) | 边缘注册、发现与能力路由 |
| [Mobile](https://github.com/Nexilume-AI/nexus-mobile) | 已授权的 Android 设备接入 |
| [Documentation](https://github.com/Nexilume-AI/nexus-docs) | 中英文教程与参考 |

设备组件独立安装与发布；是否可安装取决于仓库访问、发行包及版本兼容性。Cloud 启动不会自动安装它们。

## 参与贡献

请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎修复问题、改进教程和补充翻译。

问题反馈请附组件版本与脱敏复现步骤，不要上传凭据、个人文件或真实设备配置。安全问题遵循 [SECURITY.md](SECURITY.md)。 CI 通过不等于所有平台均已完成生产验收。

## 引用

在研究或工程工作中使用 Nexus 时，可以引用对应仓库，并注明实际使用的 release 或 commit。[CITATION.cff](CITATION.cff) 提供机器可读元数据；这是软件引用，不代表已有论文或 DOI。

```bibtex
@misc{nexus_docs,
  author       = {{Nexus contributors}},
  title        = {Nexus Documentation},
  howpublished = {\url{https://github.com/Nexilume-AI/nexus-docs}},
  note         = {Software; specify the release or commit used}
}
```

## 许可证

Nexus 自有代码采用 [Nexus Community License 1.0](LICENSE)。第三方组件保留各自许可证与声明；公开文档不授予独立企业版实现的使用权。

### 许可条件

本项目采用源码可用许可，并非未经修改的 Apache-2.0 或经 OSI 批准的开源许可。多租户服务运营及移除现有 Nexus 界面品牌标识须事先取得书面授权。此前的 Apache-2.0 授权和第三方许可证保持不变。贡献者须明确同意允许商业使用及未来重新许可的贡献协议。许可说明：[LICENSING.md](LICENSING.md)。授权联系：**cary.nexilume@outlook.com**。
