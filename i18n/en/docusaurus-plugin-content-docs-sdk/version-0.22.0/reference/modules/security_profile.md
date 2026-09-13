---
title: "security_profile API"
---

# security_profile API

Generated from current source: parameters, return annotations, fields, direct raises and original docstrings. See [Agent design](../../design/overview.md) for semantics, prerequisites and composition examples. Unannotated return types are not guessed; transport layers can raise additional errors. Underscore constructor arguments are internal test/adapter hooks, not application APIs.

## `ResolvedIPv6Security`

Complete connection inputs selected for one literal IPv6 address.

| Field | Type | Default |
| --- | --- | --- |
| `ipv6_prefix` | `str` | `required` |
| `port` | `int` | `required` |
| `tls_server_name` | `str` | `required` |
| `ca_bundle_id` | `str` | `required` |
| `ca_file` | `str` | `required` |
| `cert_file` | `str` | `required` |
| `key_file` | `str` | `required` |


## `NexusSecurityProfile`

Validated, immutable SDK security configuration.

Route selection uses IPv6 longest-prefix matching.  The caller certificate
is machine/workload identity and therefore global to the profile; target
trust is selected by ``ca_bundle_id`` for each prefix.

### `NexusSecurityProfile.__init__`

```text
NexusSecurityProfile.__init__(self, *, routes: Tuple[_RouteBinding, ...], trust_bundles: Mapping[str, str], cert_file: str, key_file: str, source_file: Optional[Path]=None) -> None
```

| Parameter | Type | Default |
| --- | --- | --- |
| `routes` | `Tuple[_RouteBinding, ...]` | `required` |
| `trust_bundles` | `Mapping[str, str]` | `required` |
| `cert_file` | `str` | `required` |
| `key_file` | `str` | `required` |
| `source_file` | `Optional[Path]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L81)

### `NexusSecurityProfile.default_path`

```text
NexusSecurityProfile.default_path() -> Path
```

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L97)

### `NexusSecurityProfile.load`

```text
NexusSecurityProfile.load(cls, path: Optional[Union[str, os.PathLike[str]]]=None) -> 'NexusSecurityProfile'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `path` | `Optional[Union[str, os.PathLike[str]]]` | `None` |

Direct raises (not exhaustive): `NexusSecurityConfigurationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L110)

### `NexusSecurityProfile.from_dict`

```text
NexusSecurityProfile.from_dict(cls, value: Mapping[str, Any], *, profile_directory: Union[str, os.PathLike[str]], source_file: Optional[Union[str, os.PathLike[str]]]=None) -> 'NexusSecurityProfile'
```

| Parameter | Type | Default |
| --- | --- | --- |
| `value` | `Mapping[str, Any]` | `required` |
| `profile_directory` | `Union[str, os.PathLike[str]]` | `required` |
| `source_file` | `Optional[Union[str, os.PathLike[str]]]` | `None` |

Direct raises (not exhaustive): `NexusSecurityConfigurationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L127)

### `NexusSecurityProfile.resolve`

```text
NexusSecurityProfile.resolve(self, address: Union[str, ipaddress.IPv6Address]) -> ResolvedIPv6Security
```

| Parameter | Type | Default |
| --- | --- | --- |
| `address` | `Union[str, ipaddress.IPv6Address]` | `required` |

Direct raises (not exhaustive): `NexusSecurityConfigurationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L194)


### `install_descriptor`

```text
install_descriptor(descriptor_file: Union[str, os.PathLike[str]], *, ca_file: Union[str, os.PathLike[str]], client_cert_file: Union[str, os.PathLike[str]], client_key_file: Union[str, os.PathLike[str]], output_file: Optional[Union[str, os.PathLike[str]]]=None) -> Path
```

Install or update one LuCI-exported IPv6 route binding.

This is an administrative provisioning operation.  It records absolute
paths to existing credentials; it never copies or embeds private keys.
Existing bindings for other prefixes and trust bundles are preserved.

| Parameter | Type | Default |
| --- | --- | --- |
| `descriptor_file` | `Union[str, os.PathLike[str]]` | `required` |
| `ca_file` | `Union[str, os.PathLike[str]]` | `required` |
| `client_cert_file` | `Union[str, os.PathLike[str]]` | `required` |
| `client_key_file` | `Union[str, os.PathLike[str]]` | `required` |
| `output_file` | `Optional[Union[str, os.PathLike[str]]]` | `None` |

Direct raises (not exhaustive): `NexusSecurityConfigurationError`.

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L225)


### `main`

```text
main(argv: Optional[Sequence[str]]=None) -> int
```

| Parameter | Type | Default |
| --- | --- | --- |
| `argv` | `Optional[Sequence[str]]` | `None` |

[Implementation](https://github.com/Nexilume-AI/nexus-agent-sdk-python/blob/main/src/nexus_agent/security_profile.py#L329)

