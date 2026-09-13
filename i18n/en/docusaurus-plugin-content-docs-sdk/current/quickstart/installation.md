---
sidebar_position: 0
title: Install the Python SDK
---

# Install the Python SDK

Use **Python 3.12** for the easiest path through the optional integrations. The dependency-free core wheel supports Python 3.9+. Building from source requires Python 3.10+; optional dependencies can require newer Python versions.

### 1. Create a virtual environment

Linux or macOS:

```sh
python3 -m venv .venv
. .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

On Ubuntu, install `python3-venv` if creating the environment reports that `ensurepip` is unavailable.

### 2. Install a release wheel

Download the `.whl` file from [GitHub Releases](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases), then install it in your environment. For the published 0.46.2 release:

```sh
python -m pip install ./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl
python -c "import nexus_agent; print(nexus_agent.__version__)"
```

Replace the filename with the wheel you downloaded. This project currently distributes installation packages through GitHub Releases; **PyPI publication is not yet available**. The PyPI package named `nexus-openwrt-agent-sdk` belongs to a different project.

To include optional features, add extras to the local wheel path:

```sh
python -m pip install "./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl[computer,browser,fastmcp,a2a]"
```

| Extra | Enables |
| --- | --- |
| `computer` | The outbound Computer Runtime connection to Nexus Cloud |
| `browser` | Browser automation through Playwright; a browser binary is also required |
| `fastmcp` | Hosted MCP tools and the FastMCP bridge |
| `a2a` | Integration with the official A2A SDK |
| `fastmcp-tasks` | Optional FastMCP Tasks integration |

### Install from source instead

Use this option to run the repository examples or work with local changes:

```sh
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m pip install ".[computer,browser,fastmcp,a2a]"
```

Use `python -m pip install .` for the core only. Commands below that reference `examples/` run from this repository directory; the wheel does not install the example files into your working directory.
