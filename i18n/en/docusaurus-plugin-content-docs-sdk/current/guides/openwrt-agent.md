---
sidebar_position: 1
title: Connect an agent to OpenWrt
---

# Connect an agent to OpenWrt

You need a reachable Nexus OpenWrt **Agent Access Proxy**, with Agent services enabled. From the source checkout, run the registration and round-trip example:

```sh
python examples/router_echo_agent.py --router http://192.168.246.1:7446 --self-test
```

Replace the URL with your router's configured Agent Access Proxy address. The example registers an agent, calls it and cleans up its registration. Authentication defaults to `auto`, using the router's supported LAN authentication or your configured credentials. Use `--auth none` only for an isolated LAN entry point explicitly configured without JWT.

For your own application, the higher-level API handles registration, lease renewal and shutdown cleanup:

```python
from nexus_agent import NexusAgent

agent = NexusAgent(router="auto", tenant="demo", agent_id="echo-server")

@agent.capability("demo.echo")
def echo(payload):
    return {"echo": payload}

if __name__ == "__main__":
    agent.run()
```

Set `NEXUS_ROUTER_URL` if discovery cannot find your router. Set `NEXUS_AGENT_ADDRESS` when the host has multiple interfaces and the automatically selected address is not reachable from the router. Use the configured proxy entry point, not an internal loopback gateway listener.

Credentials belong in your environment or deployment configuration. Supported options include `NEXUS_AGENT_TOKEN`, or `NEXUS_AGENT_CLIENT_ID` and `NEXUS_AGENT_CLIENT_SECRET` for configured OIDC authentication. Never put credentials in uploaded Python files.
