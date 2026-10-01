---
sidebar_position: 0
title: 如何升级 SDK
---

# 如何升级 Python SDK

SDK 0.47.0 以 `nexilume` 发布到 [PyPI](https://pypi.org/project/nexilume/0.47.0/)，导入名称与 CLI 名称保持不变。

## 从 PyPI 升级

激活原来安装 SDK 的环境。若安装过旧包，先执行 `python -m pip uninstall nexus-openwrt-agent-sdk`，再安装新包。保留 Computer 配置和设备密钥，无需重新配对。

```sh
python -m pip install --upgrade "nexilume[computer,browser]==0.47.0"
nexus-computer restart
nexus-computer status
```

仅使用核心 SDK 时执行 `python -m pip install --upgrade nexilume`；Hosted MCP 使用 `nexilume[fastmcp]`。升级后，正在运行的 Agent 进程也需要重启。

## 升级前

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip freeze | grep -E 'nexilume|nexus-agent|fastmcp|a2a-sdk|pywin32'
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

旧版 wheel 保留在 [GitHub Releases](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases)。当前 0.47.0 从 PyPI 安装；Linux 服务组修复已包含在 0.46.3 及后续版本中。更新 Python 包不会自动替换已部署的 addressd 服务或 Cloud 容器；按各自部署流程更新并验证。
