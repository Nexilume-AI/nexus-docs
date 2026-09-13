---
sidebar_position: 0
title: 安装 Python SDK
---

# 安装 Python SDK

发行包名称为 **`nexus-openwrt-agent-sdk`**，Python 导入保持 `nexus_agent`。目前从 [GitHub Releases](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases) 下载 wheel；尚未发布到 PyPI。PyPI 的 `nexus-openwrt-agent-sdk` 属于其他项目。

推荐使用 Python 3.12 完成全部入门流程。无第三方运行依赖的核心 wheel 支持 Python 3.9+；源码构建需要 Python 3.10+，可选扩展还受各自依赖的 Python 与平台要求约束。

## 创建虚拟环境

Linux/macOS：

```sh
python3 -m venv .venv
. .venv/bin/activate
```

Windows PowerShell：

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

Ubuntu 若提示缺少 `ensurepip`，先安装系统的 `python3-venv`。

## 安装下载的 wheel

```sh
python -m pip install ./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl
python -c "import nexus_agent; print(nexus_agent.__version__)"
```

将文件名替换成实际下载文件。需要可选功能时，在本地 wheel 路径后添加 extras：

```sh
python -m pip install "./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl[computer,browser,fastmcp,a2a]"
```

| 扩展 | 功能 |
| --- | --- |
| `computer` | Computer Runtime 到 Cloud 的出站连接 |
| `browser` | Playwright 浏览器自动化，另需浏览器程序 |
| `fastmcp` | Hosted MCP 与 FastMCP bridge |
| `a2a` | 官方 A2A SDK 集成 |
| `fastmcp-tasks` | 可选 FastMCP Tasks 集成 |

## 从源码安装与运行示例

```sh
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m pip install ".[computer,browser,fastmcp,a2a]"
```

只使用核心功能时运行 `python -m pip install .`。后续 `examples/` 命令在独立仓库根目录执行；wheel 不会把示例复制到你的工作目录。

下一步：[在本机运行第一个 Agent](local-serving.md)。SDK 不会安装 OpenWrt、Cloud 或 Relay 服务器。
