---
sidebar_position: 0
title: How to upgrade the SDK
---

# How to upgrade the Python SDK

SDK 0.47.0 is published as `nexilume` on [PyPI](https://pypi.org/project/nexilume/0.47.0/). Import and CLI names are unchanged.

## Upgrade from PyPI

Activate the original SDK environment. If it contains the older distribution, run `python -m pip uninstall nexus-openwrt-agent-sdk` before installing the new package. Keep Computer configuration and device keys; re-pairing is not required.

```sh
python -m pip install --upgrade "nexilume[computer,browser]==0.47.0"
nexus-computer restart
nexus-computer status
```

Use `python -m pip install --upgrade nexilume` for the core SDK, or `nexilume[fastmcp]` for hosted MCP. Restart running Agent processes after upgrading.

## Before upgrading

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip freeze | grep -E 'nexilume|nexus-agent|fastmcp|a2a-sdk|pywin32'
```

Lock application dependencies and run existing tests. The base SDK has no third-party runtime dependency, while optional integrations have their own version ranges.

## Upgrade from local source

```bash
git clone https://github.com/Nexilume-AI/nexus-agent-sdk-python.git
cd nexus-agent-sdk-python
python -m pip install --upgrade -e .
```

Install extras as needed:

```bash
python -m pip install --upgrade -e ".[fastmcp]"
python -m pip install --upgrade -e ".[a2a]"
python -m pip install --upgrade -e ".[windows]"
```

## Verify

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip install pytest
python -m pytest tests -q
```

Start an agent and complete one normal and one streaming call. When an upgrade crosses authentication, resume, or IPv6 changes, run integration tests against the target router release.

## Roll back

Reinstall the previous trusted tag or wheel and restore the dependency lock. Do not downgrade only `fastmcp` or `a2a-sdk` into an unknown combination; check the ranges in this version's `pyproject.toml`.

## GitHub Releases

Historical wheels remain in [GitHub Releases](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases). Install 0.47.0 from PyPI. The Linux service group fix shipped in 0.46.3 and is included in later versions. Updating the Python package does not replace deployed addressd services or Cloud containers; update and verify those using their deployment procedures.
