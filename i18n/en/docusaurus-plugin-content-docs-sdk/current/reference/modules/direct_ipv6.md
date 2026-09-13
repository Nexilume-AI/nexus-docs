---
title: "direct_ipv6 API"
---

# direct_ipv6 API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `DirectIPv6Agent`

Invoke one exact router-managed or Agent-owned endpoint over IPv6.

The TCP authority is the literal IPv6 address. ``server_identity`` is the
stable certificate identity used for SNI and hostname verification. The
client disables environment proxies so the request cannot silently leave
the direct IPv6 path through an HTTP proxy.

### `DirectIPv6Agent.__init__`

```text
DirectIPv6Agent.__init__(self, address: str, *, scheme: str='https', server_identity: Optional[str]=None, port: Optional[int]=None, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, transaction_token: Optional[str]=None, ca_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, security_profile: Optional[NexusSecurityProfile]=None, security_profile_file: Optional[Union[str, os.PathLike[str]]]=None, timeout: float=10.0) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |
| `scheme` | `str` | `'https'` |
| `server_identity` | `Optional[str]` | `None` |
| `port` | `Optional[int]` | `None` |
| `token` | `Optional[str]` | `None` |
| `token_provider` | `Optional[TokenProvider]` | `None` |
| `transaction_token` | `Optional[str]` | `None` |
| `ca_file` | `Optional[str]` | `None` |
| `cert_file` | `Optional[str]` | `None` |
| `key_file` | `Optional[str]` | `None` |
| `security_profile` | `Optional[NexusSecurityProfile]` | `None` |
| `security_profile_file` | `Optional[Union[str, os.PathLike[str]]]` | `None` |
| `timeout` | `float` | `10.0` |

Direct raises (not exhaustive): `TypeError`, `ValueError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L23)

### `DirectIPv6Agent.from_endpoint`

```text
DirectIPv6Agent.from_endpoint(cls, endpoint: PublicAgentEndpoint, **credentials: Any) -> 'DirectIPv6Agent'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `endpoint` | `PublicAgentEndpoint` | `required` |

Direct raises (not exhaustive): `TypeError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L108)

### `DirectIPv6Agent.plain_http`

```text
DirectIPv6Agent.plain_http(cls, address: str, *, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, transaction_token: Optional[str]=None, port: int=7443, timeout: float=10.0) -> 'DirectIPv6Agent'
```

Connect without TLS; any supplied JWT and payload use cleartext.

| Parameter | Type | Default |
| --- | --- | --- |
| `address` | `str` | `required` |
| `token` | `Optional[str]` | `None` |
| `token_provider` | `Optional[TokenProvider]` | `None` |
| `transaction_token` | `Optional[str]` | `None` |
| `port` | `int` | `7443` |
| `timeout` | `float` | `10.0` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L124)

### `DirectIPv6Agent.invoke`

```text
DirectIPv6Agent.invoke(self, intent: str, payload: Any, *, tenant: str, source_agent: str, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> Dict[str, Any]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `tenant` | `str` | `required` |
| `source_agent` | `str` | `required` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L169)

### `DirectIPv6Agent.invoke_intent`

```text
DirectIPv6Agent.invoke_intent(self, *args: Any, **kwargs: Any) -> Dict[str, Any]
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L192)

### `DirectIPv6Agent.invoke_stream`

```text
DirectIPv6Agent.invoke_stream(self, intent: str, payload: Any, *, tenant: str, source_agent: str, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]
```

| Parameter | Type | Default |
| --- | --- | --- |
| `intent` | `str` | `required` |
| `payload` | `Any` | `required` |
| `tenant` | `str` | `required` |
| `source_agent` | `str` | `required` |
| `intent_version` | `int` | `1` |
| `task_id` | `Optional[str]` | `None` |
| `hop_limit` | `int` | `8` |
| `constraints` | `Optional[Mapping[str, Any]]` | `None` |
| `resume` | `bool` | `True` |
| `last_event_id` | `int` | `0` |
| `max_reconnects` | `int` | `3` |
| `reconnect_delay` | `float` | `0.25` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py#L195)

