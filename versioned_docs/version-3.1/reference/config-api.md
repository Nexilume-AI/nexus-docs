---
sidebar_position: 3
title: UCI、ubus 与诊断
---

# UCI、ubus 与诊断

LuCI 最终写入 UCI 配置，并通过 OpenWrt 服务与 ubus 操作运行时。自动化脚本应优先使用项目定义的 UCI 和 ubus 接口，不要直接修改运行时生成文件。

## 常用只读命令

```bash
uci show agentd
ubus list | grep agent
logread | grep -E 'agentd|agent-gw|agent-adapter'
```

具体字段与方法以仓库中的内部参考为准：

- `docs/UCI_CONFIG.md`
- `docs/UBUS_API.md`
- `docs/AUTHENTICATION.md`
- `docs/SECURITY.md`

这些文件面向开发与集成；在自动化写配置前，应在目标固件版本上确认字段存在。修改后用 `uci changes` 检查差异，并通过服务重载或 LuCI 的 **保存并应用** 生效。
