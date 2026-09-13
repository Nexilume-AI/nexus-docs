---
sidebar_position: 0
title: 如何升级 SDK
---

# 如何升级 Python SDK

当前仓库没有声明公共 PyPI 发布地址。升级时应使用发布方提供的受信任制品，或从已审核的仓库 tag 安装。

## 升级前

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip freeze | grep -E 'nexus-agent|fastmcp|a2a-sdk|pywin32'
```

锁定应用依赖并运行现有测试。SDK 的基础包没有第三方运行时依赖，但可选集成有独立版本范围。

## 从本地源码升级

```bash
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m pip install --upgrade -e .
```

按需安装额外功能：

```bash
python -m pip install --upgrade -e ".[fastmcp]"
python -m pip install --upgrade -e ".[a2a]"
python -m pip install --upgrade -e ".[windows]"
```

## 验证

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip install pytest
python -m pytest tests -q
```

然后启动一个 Agent 并完成一次普通调用和一次流式调用。升级跨越认证、恢复或 IPv6 变更时，还应在目标路由器版本上做集成测试。

## 回退

重新安装上一个受信任 tag 或 wheel，并恢复依赖锁文件。不要只降级 `fastmcp` 或 `a2a-sdk` 而保留未知组合；先检查本版本在 `pyproject.toml` 中声明的范围。

## GitHub Releases

从[公开发行仓库](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases)下载 wheel，并按[安装指南](../quickstart/installation.md)升级。当前公开安装包为 0.46.2；main 包含尚未随新 Release 发布的 Linux 服务组修复。更新源码不会自动更新已安装的 wheel、addressd 机器运行时或 Cloud 容器。
