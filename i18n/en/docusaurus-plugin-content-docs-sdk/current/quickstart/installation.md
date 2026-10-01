---
sidebar_position: 0
title: Install the Python SDK
---

# Install the Python SDK

The distribution is **`nexilume`**, published on [PyPI](https://pypi.org/project/nexilume/0.47.0/). Imports remain `nexus_agent`; commands remain `nexus-computer` and `nexus-agent`. The PyPI project `nexus-agent-sdk` is unrelated.

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

### 2. Install from PyPI

Install the published 0.47.0 release:

```sh
python -m pip install nexilume==0.47.0
python -c "import nexus_agent; print(nexus_agent.__version__)"
```

Use `python -m pip install --upgrade nexilume` for the latest core SDK.

Install the extras you need:

```sh
python -m pip install "nexilume[computer,browser,fastmcp,a2a]==0.47.0"
```

| Extra | Enables |
| --- | --- |
| `computer` | The outbound Computer Runtime connection to Nexus Cloud |
| `browser` | Browser automation through Playwright; a browser binary is also required |
| `fastmcp` | Hosted MCP tools and the FastMCP bridge |
| `a2a` | Integration with the official A2A SDK |
| `fastmcp-tasks` | Optional FastMCP Tasks integration |
| `windows` | Windows service helpers (Windows only) |

### Migrate from the older wheel

If the same environment contains `nexus-openwrt-agent-sdk`, run `python -m pip uninstall nexus-openwrt-agent-sdk` before installing `nexilume`. Both distributions share the import directory; do not keep both installed. Keep Computer configuration and device keys. Restart existing Runtime processes after installation; see [upgrading](../guides/upgrade.md). Re-pairing is not required.

For offline installation, download the wheel from [PyPI release files](https://pypi.org/project/nexilume/0.47.0/#files) and run `python -m pip install ./nexilume-0.47.0-py3-none-any.whl`. Prepare optional dependencies separately.

### Install from source instead

Use this option to run the repository examples or work with local changes:

```sh
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m pip install ".[computer,browser,fastmcp,a2a]"
```

Use `python -m pip install .` for the core only. Commands below that reference `examples/` run from this repository directory; the wheel does not install the example files into your working directory.
