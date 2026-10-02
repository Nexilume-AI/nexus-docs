# 真实界面采集

[English](capture-notes.md) · **简体中文**

这组素材于 2026 年 10 月 1 日在运行中的企业版采集，使用独立演示账号和真实 Docker
Agent。它验证的是 Python 上传、部署、Plan、内联问题和文件产物流程，不是模型智能或
Computer/Mobile/OpenWrt 验收。界面未伪造，未修改状态或填入预制对话；图中企业菜单不属于
社区版开源承诺。当前宽度展示的是响应式 Live / Context 分栏导航。这些素材是截图，不是视频。

示例源码：[readme_launch_agent.py](../../examples/readme_launch_agent.py)。

复现时上传上面的 Python 文件，部署后发送发布清单需求，选择 **Self-hosting operators**，
等待完成后，先在 **Data Assets → Import assets → Agent assets → Output files & images**
选择本次 Run 和产物，执行 **Scan output**。扫描通过才允许预览或归档；本次安装不会自动
跳过该步骤。返回 **Context → Files** 预览文件。不需要密钥、额外依赖或个人设备。示例通过
私有文件上传接口传送容器产物，不使用要求 Attached Computer 的 `output.write_text()`。
