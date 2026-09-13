---
sidebar_position: 4
title: One IPv6 per Agent on Windows
description: Install, verify, and troubleshoot the Host Alias address service on Windows.
---

# One IPv6 per Agent on Windows

Windows Host Alias places several global IPv6 `/128` addresses on one physical interface and leases one to each Python Agent. `NexusAgentAddressd` runs as LocalSystem. Ordinary Agents request leases through an ACL-protected Named Pipe.

## Requirements

- the Windows host has a genuinely usable global IPv6 `/64`;
- Python 3.9+;
- the initial setup can approve UAC;
- the selected TCP port is outside Windows/Hyper-V excluded ranges.

## One-command setup

From the package:

```powershell
python -m pip install "./nexus_openwrt_agent_sdk-0.46.2-py3-none-any.whl[windows]"
nexus-agent ipv6 setup
```

From the source repository:

```powershell
python -m pip install -e ".[windows]"
nexus-agent ipv6 setup
```

`setup` discovers a usable interface and global `/64`, selects a non-reserved port, opens UAC, configures and starts the address service, and runs a `/128` Agent self-test protected by a temporary firewall block. It does not create a permanent public firewall allow rule.

When several networks qualify, specify one:

```powershell
nexus-agent ipv6 setup `
  --interface "Ethernet" `
  --prefix "240e:1234:5678:1200::/64" `
  --port 9443
```

## Verify the unprivileged path

After first joining `Nexus Agent Users`, sign out and back in once, then run:

```powershell
nexus-agent ipv6 doctor
```

Doctor checks service configuration, service state, global prefix, Named Pipe, current group membership, and recommended port. Automation can use:

```powershell
nexus-agent ipv6 doctor --json
```

## Run the two-Agent example

```powershell
$env:NEXUS_IPV6_LAB = '1'
python examples/ipv6_agents_call_each_other.py
```

The output should contain two different global IPv6 addresses. Both Agents may bind the same port because Windows distinguishes listeners by address and port.

## Manual service management

An enterprise deployment with a fixed approval process can use the advanced service commands to configure the interface, prefix, and allowed users. Prefer `nexus-agent ipv6 setup` for normal installation because it also checks reserved ports and runs a self-test.

The machine-owned runtime is under `C:\ProgramData\Nexus\addressd-runtimes`. The LocalSystem service does not import the SDK or pywin32 from an installing user's `AppData`. Protect configuration and keys under `C:\ProgramData\Nexus`, and grant Named Pipe access only to approved local groups.

## Common failures

- Doctor says the current user is outside the group: sign out and back in; reopening PowerShell is insufficient.
- Windows/Hyper-V reserves the port: rerun setup to select one, or inspect `netsh interface ipv6 show excludedportrange protocol=tcp`.
- No global `/64` is found: inspect the upstream prefix, interface, and route. A single `/128` cannot support Host Alias.
- Local calls work but remote calls fail: inspect Windows Firewall and upstream routing. Setup never permanently opens a public port.

See [Two IPv6 Agents calling each other](../tutorials/ipv6-agents-call-each-other.md) for the complete call path.

Complete [installation](../quickstart/installation.md) first. Source commands run at the standalone SDK repository root; download wheels from GitHub Releases rather than installing this project from PyPI.
