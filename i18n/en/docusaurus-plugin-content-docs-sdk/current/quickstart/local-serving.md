---
sidebar_position: 1
title: Run an agent locally
---

# Run an agent locally

This example runs entirely on your computer. Save it as `hello_agent.py`:

```python
from nexus_agent import NexusAgentServer

server = NexusAgentServer("127.0.0.1", 9443)

@server.handler("demo.echo")
def echo(envelope):
    return {"message": envelope.payload["message"]}

if __name__ == "__main__":
    try:
        server.serve_forever()
    finally:
        server.server_close()
```

Start it:

```sh
python hello_agent.py
```

In a second terminal using the same virtual environment, save and run `call_agent.py`:

```python
import json
from urllib.request import Request, urlopen

request = Request(
    "http://127.0.0.1:9443/invoke",
    data=json.dumps({
        "version": "1.0",
        "intent": "demo.echo",
        "intent_version": 1,
        "task_id": "hello-1",
        "source_agent": "agent://demo/caller",
        "tenant": "demo",
        "hop_limit": 7,
        "payload": {"message": "Hello, Nexus!"},
    }).encode(),
    headers={"Content-Type": "application/vnd.nexus.agent-envelope+json"},
)
with urlopen(request, timeout=10) as response:
    print(json.load(response))
```

Expected output: `{'message': 'Hello, Nexus!'}`. Press Ctrl+C in the server terminal to stop it. This example binds only to loopback; configure authentication and transport security before exposing an agent to other machines.

Next: [Connect to OpenWrt](../guides/openwrt-agent.md).
