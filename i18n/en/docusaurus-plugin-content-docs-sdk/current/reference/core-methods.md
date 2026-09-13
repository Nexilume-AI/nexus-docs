---
sidebar_position: 1
title: Core classes and methods
---

# Core classes and methods

These signatures are generated statically from current SDK source, including hosted mode, resource declarations and Computer Runtime. Release wheels can lag behind main. For usage, see [runtime modes](../concepts/runtime-model.md) and [Computer Runtime](../guides/computer-runtime.md).

## `NexusAgent`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/agent.py)

```text
def NexusAgent.__init__(self, *, router: str='auto', token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, auth: Optional[Union[str, TokenProvider]]=None, transaction_token: Optional[str]=None, tenant: str='default', agent_id: Optional[str]=None, listen_host: str='auto', port: int=0, advertise_address: str='auto', path: str='/invoke', router_ca_file: Optional[str]=None, auth_ca_file: Optional[str]=None, cloud_ca_file: Optional[str]=None, router_cert_file: Optional[str]=None, router_key_file: Optional[str]=None, router_tls_server_name: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, server_tls_name: str='auto', server_ca_bundle_id: str='system', lease_seconds: int=300, timeout: float=10.0, cloud_publish: bool=True, cloud_name: Optional[str]=None, computer_requirement: str='disabled', workspace_capabilities: Iterable[str]=(), mobile_requirement: str='disabled', mobile_capabilities: Iterable[str]=(), runtime: str='auto') -> None: ...

def NexusAgent.capability(self, intent: str, *, public_ipv6: Optional[bool]=None, origin: Optional[str]=None, version: int=1, region: str='local', lease_seconds: Optional[int]=None, cost_microunits: int=0, latency_ms: int=0, trust: int=50, pass_envelope: bool=False, tool: Optional[Union[McpToolDescriptor, bool]]=None, mobile_scopes: Optional[Iterable[str]]=None, slash_command: Optional[str]=None, slash_description: str='', execution_profiles: Optional[Iterable[NexusExecutionProfile]]=None, input_modalities: Optional[Iterable[str]]=None, follow_up: Optional[str]=None) -> Callable[[BusinessHandler], BusinessHandler]: ...

def NexusAgent.stream_capability(self, intent: str, *, public_ipv6: Optional[bool]=None, origin: Optional[str]=None, version: int=1, region: str='local', lease_seconds: Optional[int]=None, cost_microunits: int=0, latency_ms: int=0, trust: int=50, pass_envelope: bool=False, tool: Optional[Union[McpToolDescriptor, bool]]=None, mobile_scopes: Optional[Iterable[str]]=None, slash_command: Optional[str]=None, slash_description: str='', execution_profiles: Optional[Iterable[NexusExecutionProfile]]=None, input_modalities: Optional[Iterable[str]]=None) -> Callable[[BusinessStreamHandler], BusinessStreamHandler]: ...

def NexusAgent.start(self, *, auto_renew: bool=True, renew_fraction: float=0.6, announce: bool=True, print_fn: Callable[[str], Any]=print) -> NexusAgentHandle: ...

def NexusAgent.run(self, **start_options: Any) -> Any: ...

def NexusAgent.as_mcp_server(self) -> Any: ...

def NexusAgent.invoke(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> Mapping[str, Any]: ...

def NexusAgent.invoke_stream(self, intent: str, payload: Any, *, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]: ...

def NexusAgent.public_ipv6(cls, address: str, **options: Any): ...
```

## `NexusAgentClient`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)

```text
def NexusAgentClient.__init__(self, base_url: str, *, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, auth: Optional[Union[str, TokenProvider]]=None, transaction_token: Optional[str]=None, ca_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, tls_server_name: Optional[str]=None, use_environment_proxy: bool=True, timeout: float=10.0, user_agent: str='nexus-agent-sdk-python/0.35.0') -> None: ...

def NexusAgentClient.register(self, registration: CapabilityRegistration, *, auto_renew: bool=False, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> 'AgentLease': ...

def NexusAgentClient.invoke_intent(self, intent: str, payload: Any, *, tenant: str, source_agent: str, target_agent: Optional[str]=None, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> JsonObject: ...

def NexusAgentClient.invoke_stream(self, envelope: Mapping[str, Any], *, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]: ...
```

## `AgentLease`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/client.py)

```text
def AgentLease.renew(self, **updates: Any) -> LeaseInfo: ...

def AgentLease.close(self, *, unregister: bool=True) -> None: ...
```

## `NexusAgentServer`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/server.py)

```text
def NexusAgentServer.__init__(self, host: str='127.0.0.1', port: int=0, *, path: str='/invoke', stream_path: Optional[str]=None, auth: Optional[ServerAuthPolicy]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, address_family: str='auto', dual_stack: bool=False, max_request_bytes: int=65536, max_response_bytes: int=262144, max_stream_event_bytes: int=65536, request_timeout: float=15.0, resumable_streams: bool=True, resume_max_tasks: int=128, resume_max_events: int=256, resume_max_history_bytes: int=262144, resume_retention_seconds: float=300.0, direct_tasks: bool=True, direct_task_max_tasks: int=128, direct_task_ttl_seconds: float=3600.0, direct_task_heartbeat_seconds: float=10.0, run_context_opener: Optional[Callable[..., Any]]=None) -> None: ...

def NexusAgentServer.handler(self, intent: str) -> Callable[[SyncHandler], SyncHandler]: ...

def NexusAgentServer.stream_handler(self, intent: str) -> Callable[[StreamHandler], StreamHandler]: ...

def NexusAgentServer.serve_forever(self, poll_interval: float=0.25) -> None: ...

def NexusAgentServer.serve_in_thread(self, *, daemon: bool=True) -> threading.Thread: ...

def NexusAgentServer.serve_registered(self, client: NexusAgentClient, registrations: Iterable[CapabilityRegistration], *, auto_renew: bool=True, renew_fraction: float=0.6, health_check: Optional[Callable[[], bool]]=None, reregister_on_not_found: bool=True) -> None: ...

def NexusAgentServer.shutdown(self) -> None: ...

def NexusAgentServer.server_close(self) -> None: ...
```

## `DirectIPv6Agent`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/direct_ipv6.py)

```text
def DirectIPv6Agent.__init__(self, address: str, *, scheme: str='https', server_identity: Optional[str]=None, port: Optional[int]=None, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, transaction_token: Optional[str]=None, ca_file: Optional[str]=None, cert_file: Optional[str]=None, key_file: Optional[str]=None, security_profile: Optional[NexusSecurityProfile]=None, security_profile_file: Optional[Union[str, os.PathLike[str]]]=None, timeout: float=10.0) -> None: ...

def DirectIPv6Agent.plain_http(cls, address: str, *, token: Optional[str]=None, token_provider: Optional[TokenProvider]=None, transaction_token: Optional[str]=None, port: int=7443, timeout: float=10.0) -> 'DirectIPv6Agent': ...

def DirectIPv6Agent.invoke(self, intent: str, payload: Any, *, tenant: str, source_agent: str, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None) -> Dict[str, Any]: ...

def DirectIPv6Agent.invoke_stream(self, intent: str, payload: Any, *, tenant: str, source_agent: str, intent_version: int=1, task_id: Optional[str]=None, hop_limit: int=8, constraints: Optional[Mapping[str, Any]]=None, resume: bool=True, last_event_id: int=0, max_reconnects: int=3, reconnect_delay: float=0.25) -> Iterator[SseEvent]: ...
```

## `PublicIPv6Agent`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/public_ipv6_agent.py)

```text
def PublicIPv6Agent.__init__(self, address: str, *, auth: Union[str, ServerAuthPolicy], port: int=9443, tenant: str='default', agent_id: Optional[str]=None, address_mode: str='auto', allocator: Optional[LocalAddressdClient]=None, interface: str='auto', prefix: str='auto', address_lease_seconds: int=300, cert_file: Optional[str]=None, key_file: Optional[str]=None, client_ca_file: Optional[str]=None, tls_server_name: Optional[str]=None, ca_bundle_id: Optional[str]=None, max_request_bytes: int=65536, max_response_bytes: int=262144, max_stream_event_bytes: int=65536, request_timeout: float=15.0, resumable_streams: bool=True) -> None: ...

def PublicIPv6Agent.start(self, *, announce: bool=True, print_fn: Callable[[str], Any]=print) -> PublicIPv6AgentHandle: ...

def PublicIPv6Agent.run(self, **start_options: Any) -> PublicAgentEndpoint: ...
```

## `NexusComputerRuntime`

[Source](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/computer_runtime.py)

```text
def NexusComputerRuntime.setup(cls, pairing_url: str, *, root: Union[Path, str]=DEFAULT_ROOT, name: str='', ca_file: str='', install: bool=True) -> 'NexusComputerRuntime': ...

def NexusComputerRuntime.close(self) -> None: ...
```
