---
title: Agent integration examples
---

# Agent integration examples

These adapters demonstrate deploying native tools as Nexus Agents. Each directory documents its runtime dependencies, deployment and limitations. The SDK does not include model weights, commercial software licenses or GPU drivers.

| Example | Purpose |
| --- | --- |
| [Pi](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/pi_chat_agent) | Streamed chat, caller-owned model authorization and attached Computer tools |
| [Mobilerun](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/mobilerun_mcp_agent) | Caller-bound mobile tasks, background progress and an interactive view |
| [OpenEvolve](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/openevolve_mcp_agent) | Model-assisted program optimization |
| [KernelFoundry](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/kernelfoundry_mcp_agent) | Kernel evaluation and model-assisted optimization |
| [FastVideo](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/fastvideo_mcp_agent) | Distillation jobs and authenticated weight downloads |
| [DiffSynth-Studio](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/diffsynth_mcp_agent) | LoRA fine-tuning and downloadable weights |
| [VBench](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/vbench_mcp_agent) | Video evaluation jobs and reports |
| [ChampSim](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/champsim_mcp_agent) | Processor simulation jobs |
| [Ramulator 2](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/ramulator_mcp_agent) | Memory simulation jobs |
| [AccelForge](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/accelforge_mcp_agent) | Accelerator analysis jobs |
| [SST](https://github.com/Nexilume-AI/nexus-agent-sdk-python/tree/main/examples/sst_mcp_agent) | Simulation jobs |

## Deployment and permissions

- Configure your own paths, runtime and Agent registration according to each README. Do not copy production credentials.
- Agents that need a model use upstream model authorization, never a publisher's default model key. Cloud checks caller, Agent and workspace scope before reusing an active grant.
- Mobile and Computer capabilities require a caller-bound online device and compatible Relay/Runtime. Model authorization does not grant device access.
- Mobilerun exposes MCP with Background/Interactive View; Pi offers Chat/Private Display. Published capabilities determine the available entry points; chat is optional.
- Consult each example for GPU, native dependency and model requirements. Publishing source does not establish full model-quality validation, and a short test cannot establish general acceleration benefits.

## Long jobs and diagnostics

Keep a job ID for long tasks, consume progress events and retrieve artifacts through authenticated links. A broken network connection does not mean the task failed. Avoid blindly retrying device operations with potential side effects. Release device ownership when a task ends or is cancelled.

Measure Router forwarding, capacity wait, first event, first text and total duration separately. Client-observed time to first text includes network and upstream processing; it is not a direct measurement of upstream queue time. Separating upstream queueing from computation requires upstream telemetry.
