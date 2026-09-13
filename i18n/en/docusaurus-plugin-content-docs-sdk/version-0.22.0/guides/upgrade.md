---
sidebar_position: 0
title: How to upgrade the SDK
---

# How to upgrade the Python SDK

The repository does not currently declare a public PyPI release URL. Upgrade from a trusted artifact supplied by the publisher, or from a reviewed repository tag.

## Before upgrading

```bash
python -c "import nexus_agent; print(nexus_agent.__version__)"
python -m pip freeze | grep -E 'nexus-agent|fastmcp|a2a-sdk|pywin32'
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

Download a wheel from [GitHub Releases](https://github.com/Nexilume-AI/nexus-agent-sdk-python/releases) and follow [installation](../quickstart/installation.md). The published package is 0.46.2; main includes a Linux service group fix not yet shipped in a new release. Updating source does not update an installed wheel, the staged addressd runtime or a Cloud container.
