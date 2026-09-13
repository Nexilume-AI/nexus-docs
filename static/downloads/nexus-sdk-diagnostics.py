"""Safe, read-only diagnostics for nexus-agent-sdk.

The script never prints credential values. Network access is opt-in with --connect
and performs a TCP connection only.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import platform
import socket
import sys
from urllib.parse import urlsplit


ENVIRONMENT_NAMES = (
    "NEXUS_ROUTER_URL",
    "NEXUS_AGENT_TOKEN",
    "NEXUS_AGENT_CLIENT_ID",
    "NEXUS_AGENT_CLIENT_SECRET",
    "NEXUS_AGENT_ADDRESS",
    "NEXUS_AGENT_IPV6",
    "NEXUS_AGENT_SECURITY_PROFILE",
)


def module_status(name: str) -> str:
    return "available" if importlib.util.find_spec(name) is not None else "not installed"


def router_target(value: str) -> tuple[str, int]:
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("router must be an absolute http or https URL")
    return parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only nexus-agent-sdk diagnostics")
    parser.add_argument("--router", help="Router URL; defaults to NEXUS_ROUTER_URL")
    parser.add_argument("--connect", action="store_true", help="Perform a TCP-only connectivity check")
    parser.add_argument("--timeout", type=float, default=3.0, help="TCP timeout in seconds (default: 3)")
    args = parser.parse_args()

    print("== runtime ==")
    print(f"python={platform.python_version()}")
    print(f"implementation={platform.python_implementation()}")
    print(f"platform={platform.platform()}")

    print("\n== modules ==")
    for name in ("nexus_agent", "fastmcp", "a2a", "win32api"):
        print(f"{name}={module_status(name)}")
    try:
        import nexus_agent
        print(f"nexus_agent_version={nexus_agent.__version__}")
    except Exception as error:  # Import failures are the diagnostic result.
        print(f"nexus_agent_import_error={type(error).__name__}: {error}")

    print("\n== environment presence ==")
    for name in ENVIRONMENT_NAMES:
        print(f"{name}={'set' if os.environ.get(name) else 'not set'}")

    router = args.router or os.environ.get("NEXUS_ROUTER_URL")
    if not router:
        print("\nrouter_check=skipped (no --router or NEXUS_ROUTER_URL)")
        return 0

    try:
        host, port = router_target(router)
        addresses = sorted({item[4][0] for item in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)})
        print("\n== router target ==")
        print(f"host={host}")
        print(f"port={port}")
        print(f"resolved_addresses={','.join(addresses)}")
        if args.connect:
            with socket.create_connection((host, port), timeout=args.timeout):
                print("tcp_connect=ok")
        else:
            print("tcp_connect=skipped (use --connect)")
    except Exception as error:
        print(f"router_check_error={type(error).__name__}: {error}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
