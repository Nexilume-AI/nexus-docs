---
sidebar_position: 4
title: Linux 一键配置 Agent IPv6
---

# Linux 一键配置 Agent IPv6

Linux 可以运行本机 addressd，为普通用户的 Agent 分配独立 `/128`。它与 OpenWrt 管理地址是两条不同路径。先完成[安装](../quickstart/installation.md)，准备 systemd、`iproute2` 与首次配置所需的管理员权限。

```sh
nexus-agent ipv6 setup
nexus-agent ipv6 doctor
```

setup 发现配置并在系统操作阶段请求提权，安装受限的 `nexus-agent-addressd.service`。业务 Agent 以普通用户持有地址租约，不需要 root。首次加入 `nexus-agent` 组后，重新登录使组成员关系生效。

## 选择适合网络的模式

| 模式 | 使用场景 |
| --- | --- |
| `auto` | 由发现流程选择支持的配置 |
| `routed-prefix` | 主机拥有实际可用的路由前缀 |
| `upstream-relay` | 支持的上游 RA/邻居发现网络 |
| `dhcpv6-ia-na` | 上游 DHCPv6 服务允许独立地址租约 |

执行 `nexus-agent ipv6 setup --help` 查看接口、前缀与模式参数。只指定分配给当前部署的真实前缀。单个 IPv6 地址不等于拥有整段 `/64`；公网入站还取决于上游路由、防火墙和传输认证。

源码仓库中的安装脚本也可使用：

```sh
sh install-linux.sh --wheel /path/to/downloaded.whl --install-only
```

以普通用户运行，不要给安装脚本加 sudo。省略 `--install-only` 会继续进入 IPv6 setup。

## 已发布 0.46.2 的服务组修复

0.46.2 wheel 生成的服务可能因缺少主组而无法设置 Unix socket 权限。0.46.3 及后续发行版（包括 nexilume 0.47.0）已为新生成的服务增加 `Group=nexus-agent`。已运行 setup 并创建服务和组的安装，可加 systemd override：

```sh
sudo systemctl edit nexus-agent-addressd.service
```

```ini
[Service]
Group=nexus-agent
```

```sh
sudo systemctl daemon-reload
sudo systemctl restart nexus-agent-addressd.service
nexus-agent ipv6 doctor
```

保留现有 capability 限制，不需要增加 `CAP_CHOWN`。

## 当前验收范围

Ubuntu 24.04 / Python 3.12 / WSL2 systemd 已通过真实 setup、普通用户 `/128` 分配、JWT 调用、地址释放与服务重启恢复。完整 SDK 回归为 **354 passed、17 skipped**。

IPv6 验收使用无外部接口、无默认路由的隔离网络命名空间，使用上述组修复。公网 IPv6 入站、真实上游 DHCPv6 和裸机 Linux 留待单独验收，不能把本机调用成功解释为公网可达。

下一步：[两个 IPv6 Agent 互相调用](../tutorials/ipv6-agents-call-each-other.md)。
