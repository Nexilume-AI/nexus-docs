---
sidebar_position: 1
title: Configure authentication and TLS
---

# Configure authentication and TLS

The SDK separates client credential acquisition from server-side caller verification. Production deployments should verify the router, the agent server, and caller authorization.

## Client tokens

The simplest option is `NEXUS_AGENT_TOKEN`. `EnvironmentTokenProvider` reads it, while `AutoTokenProvider` can choose an available method from the environment and router metadata. Use `StaticTokenProvider` for an explicitly supplied token and `OIDCClientCredentialsProvider` for OIDC client credentials.

```python
from nexus_agent import NexusAgentClient, OIDCClientCredentialsProvider

provider = OIDCClientCredentialsProvider(
    "https://issuer.example/token",
    client_id_env="NEXUS_AGENT_CLIENT_ID",
    client_secret_env="NEXUS_AGENT_CLIENT_SECRET",
)
client = NexusAgentClient("https://router.example:7443", token_provider=provider)
```

## TLS

Supply a trusted CA when connecting to the router. For mutual TLS, also provide a client certificate and private key. Agent servers use `cert_file` and `key_file`. Never disable certificate verification in production.

## Direct-call authentication

`NoServerAuth` is only for isolated development. Public IPv6 or cross-domain calls should use `HmacJwtServerAuth` or an integration-specific verified policy with strict issuer, audience, lifetime, and clock-skew checks.
