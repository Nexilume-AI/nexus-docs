---
title: MCP upstream model API authorization
---

# MCP upstream model API authorization

An MCP Agent can request the current caller's permission to use a model API through Nexus Cloud. Atrex Kernel Agent, for example, needs a model to generate and optimize code. Cloud validates and stores the authorization; trusted execution code obtains credentials at runtime. Models and MCP tool results receive only authorization references and non-secret configuration.

## Two separate credentials

| Purpose | Meaning |
| --- | --- |
| MCP connection credential | Identifies the client and permits Agent invocation, typically through the Authorization header in client configuration. |
| Upstream model authorization | Permits the Agent to use a specific provider, endpoint, model and credential for a limited time. Model usage may incur charges. |

Connecting to MCP does not authorize model charges. This flow does not automatically read or forward a client's own login tokens, including Codex login tokens, or provision a GPU/execution service.

## User confirmation flow

1. The Agent calls SDK `ProviderCredentials.authorize()`. Atrex exposes this as `authorize_atrex_provider`.
2. Cloud identifies the caller and reuses an eligible active grant when available.
3. When approval is needed, Cloud presents a confirmation form or secure page link according to the client's declared capabilities.
4. The user selects configuration and lifetime, and explicitly consents to access and possible model charges.
5. The client checks the grant. Only `status: "authorized"` permits starting work that needs a model.
6. Trusted execution code validates the grant before making model requests. Secrets stay out of conversations, MCP results, logs and training data.

| Situation | Confirmation |
| --- | --- |
| Nexus Cloud with MCP form elicitation support | Select a Router / model and lifetime, then confirm inside the client. No key entry. |
| Third-party provider with an eligible saved authorization | Form-capable clients can confirm the already-authorized endpoint / model. |
| New third-party key, changed third-party scope, or Configure securely | On the hosted service, enter and confirm through a valid short-lived link without signing in. Personal deployments keep their sign-in flow. |
| Client without form support | Use the secure page. URL elicitation can prompt navigation; otherwise the tool returns `authorization_url`. |

In-conversation confirmation means a client authorization form, not pasting a key into chat. Opening a URL or accepting a navigation prompt does not grant access: the user supplying the credential or Router must still complete server-validated approval. Form support and presentation vary between clients.

## Nexus Cloud: choose a Router without a key or endpoint

For `provider: "nexus"`, Cloud lists deployed Routers the caller can use in the calling context and their output model names. Approval issues a temporary credential limited to the selected Router, model and lifetime.

- No API key or Base URL entry is required.
- Usage belongs to the selected Router's Organization / project.
- Gateway admission rechecks permissions, caller identity, expiry and revocation.
- If no Router is available, configure one or obtain use permission. Entering a Router ID cannot bypass access checks.
- This temporary credential issuer belongs to the Enterprise / Cloud composition; do not assume a Personal deployment offers it.

Third-party providers support `openai`, `anthropic`, `custom_openai` and `custom_anthropic`. Presets have fixed endpoints. Custom endpoints require a public HTTPS API Base URL, not a complete `/responses` or `/chat/completions` path. Atrex requires Responses for OpenAI-compatible backends and Messages for Anthropic-compatible backends.

## Atrex MCP examples

Request Nexus Cloud authorization; omit `model` to let the user choose:

```json
{"provider":"nexus","model":"gpt-6-sol","wait_seconds":15}
```

Pass these arguments to `authorize_atrex_provider`. It returns metadata including `authorization_id`, `status`, `provider`, `base_url`, `model`, `router_id`, `expires_at` and `authorization_url`, never a key. The model must actually exist in an accessible Router; the example name does not guarantee availability.

After confirmation, call the same tool to check:

```json
{"authorization_id":"<returned-authorization-id>"}
```

Read the final approved configuration instead of assuming the original model selection. Submit `start_atrex_optimization` with project credentials, this `authorization_id`, the approved `provider` / `model` and a fresh UUID `request_id`. Optional `base_url` asserts the authorized destination. Reuse the same request ID on transport retries to avoid duplicate submission.

## Reuse, changing APIs and revocation

| Action | Behavior |
| --- | --- |
| Continue with the same caller, Agent, tenant, project, provider / endpoint and matching model | An active grant can be reused without confirmation on every call. Omitting the model may reuse an existing grant within that scope; always read the returned model. |
| Change key, provider, endpoint, model or Nexus Router | Make a new `authorize_atrex_provider` call with `force_new: true`, then let the user select and approve the configuration. |
| Check status only | Supply `authorization_id`; this does not create a replacement grant. |
| Revoke | Open the authorization page and select Revoke access. Derived grants also depend on their saved source authorization remaining valid. |
| Expired or revoked grant | Request new approval. Grants are not silently extended. |

Pending requests expire after **10 minutes**. Confirmation interfaces offer **5 minutes, 1 hour or 24 hours**, defaulting to **1 hour**. `wait_seconds` controls only how long the tool waits for confirmation (0–20 seconds, default 15), not the grant lifetime. A `pending` result can still be approved before request expiry; then check the same ID.

```json
{"provider":"nexus","force_new":true,"wait_seconds":15}
```

This skips automatic active-grant reuse and starts another confirmation flow. New approval neither revokes existing grants nor changes credentials in a running job. To switch an existing job, cancel it and submit with the new grant and a new `request_id`. Atrex checks authorization during execution; revocation or expiry blocks subsequent model requests and triggers job termination. Requests already sent and their charges cannot be undone.

## SDK integration

Use a valid HTTPS Cloud Run context:

```python
from nexus_agent import current_run
from nexus_agent.credentials import ProviderCredentials

credentials = ProviderCredentials(current_run())
grant = credentials.authorize("nexus", model="gpt-6-sol", wait_seconds=0)
# Return non-secret grant metadata. After approval, check in a valid invocation:
grant = credentials.status(grant["authorization_id"])
# Continue model-dependent work only when grant["status"] == "authorized".
```

`resolve_for_runtime(authorization_id)` is exclusively for trusted execution code and must never be registered as an MCP tool. Its result contains real credentials: never return it to a model or include it in prompts, logs, artifacts, Data Assets or training exports. Use it only in controlled memory for the authorized operation.

Cloud operators must apply Agent migrations, configure shared `NEXUS_SECRET_ENCRYPTION_KEYS` and a public HTTPS `NEXUS_PUBLIC_BASE_URL`, and allow the relevant Agent UUIDs in `NEXUS_AGENT_CREDENTIAL_ENABLED_AGENTS` (empty by default). All serving processes need the same encryption keyring; restart affected services after configuration changes. Caller ownership must be verifiable; shared or unidentified keys cannot authorize provider access.

## Troubleshooting

- **MCP connects but optimization cannot start:** check execution readiness, grant status and the actual approved model.
- **The tool finishes waiting with pending:** let the user approve, then check the same ID instead of repeatedly creating requests.
- **Changing configuration unexpectedly reuses a grant:** make a fresh tool call with `force_new: true`.
- **The page requires sign-in or denies access:** on the hosted service, sign in to your own account for Nexus Router selection and check Router permissions. Login-free third-party key links must be unexpired and unused. Personal deployments use their credential-owner sign-in flow.
- **You need internal progress:** model authorization is separate from job monitoring. New Atrex jobs support [background events](./background-events.md) and a live page; `get_atrex_job` remains available for snapshots.


## Model provider selection on the web page

**Model provider** is the single connection selector. There is no separate
“Use my Nexus Router” button. The compact page adapts to mobile screens and does
not use expandable sections.

On hosted **cloud.nexilume.com**:

- Choose **Nexus Cloud** to use the actual signed-in browser user's permitted Routers and models, without entering a key or endpoint.
- If signed out, the page offers sign-in. Other providers remain selectable.
- For other providers, a valid short-lived authorization link allows users to enter their own endpoint, model, and key without signing in to Nexus.
- Links expire within five minutes of creation and are consumed by approval or cancellation. Opening a link is not consent.
- The link does not grant access to the publisher's account. Router choices belong to the signed-in user; usage is billed to the selected Router's Organization or project.
- Switching providers clears the entered key and consent. Submission rechecks identity, permissions, and authorization scope.

This browser account selection is separate from in-client MCP form elicitation,
which continues to use the authenticated MCP caller context. The open-source
Personal host retains its credential-entry flow and does not provide hosted
login-free links or Router delegation key issuance. Selecting Nexus Cloud on a
Personal host still requires the user's own key.


## Optional preauthorization in MCP client configuration

Both the hosted service and Personal host accept explicit upstream configuration
on Agent MCP requests. This is a Nexus HTTP-header extension, not a standard MCP
tool argument. Existing web authorization remains available when these headers
are omitted. Use a personal, owner-bound MCP connection credential and an Agent
enabled for model authorization by the host administrator.

```toml
# Optional upstream model preauthorization for this MCP Agent.
# Environment variables contain keys; never put them in tool arguments.
[mcp_servers.my_agent]
url = "https://cloud.nexilume.com/api/v1/agents/<agent-id>/mcp/"
bearer_token_env_var = "NEXUS_MCP_API_KEY"

[mcp_servers.my_agent.http_headers]
X-Nexus-Tenant = "<tenant-id>"
X-Nexus-Upstream-Preauthorize = "true"
X-Nexus-Upstream-Provider = "custom_openai"
X-Nexus-Upstream-Endpoint = "https://api.example.com/v1"
X-Nexus-Upstream-Model = "<model-id>"
X-Nexus-Upstream-TTL-Seconds = "3600"

[mcp_servers.my_agent.env_http_headers]
X-Nexus-Upstream-Key = "NEXUS_UPSTREAM_API_KEY"
```

Codex supports static `http_headers` and environment-sourced `env_http_headers`
([official configuration reference](https://developers.openai.com/codex/config-reference/)).
Set `NEXUS_MCP_API_KEY` and `NEXUS_UPSTREAM_API_KEY` in the environment of the
process running the MCP client. The first authenticates to Nexus; the second is
the upstream model credential. They serve different purposes. Other HTTP MCP
clients can send the same headers. A client without environment-backed headers
can supply `X-Nexus-Upstream-Key` directly in its private header configuration;
do not commit or share a configuration containing a real key. Arbitrary top-level
`endpoint`, `model`, or `key` fields are not read by the Nexus MCP endpoint.

| Header | Requirement |
| --- | --- |
| `X-Nexus-Upstream-Preauthorize` | Must be the string `true`; explicitly permits this Agent to use the supplied model credential and incur model charges. |
| `X-Nexus-Upstream-Endpoint` | Required public HTTPS API base; no credentials, query, fragment, or private DNS/IP destinations. |
| `X-Nexus-Upstream-Model` | Required exact model identifier. |
| `X-Nexus-Upstream-Key` | Required upstream API key, separate from MCP `Authorization`. |
| `X-Nexus-Upstream-Provider` | Optional; defaults to `custom_openai`. Also supports `custom_anthropic`, `openai`, `anthropic`, and `nexus`. Preset providers require their fixed endpoint. |
| `X-Nexus-Upstream-TTL-Seconds` | Optional; defaults to `3600`, allowed `300`–`86400`. |

Incomplete configuration, missing explicit consent, unknown upstream headers,
and invalid endpoints fail closed with HTTP 400 rather than silently enabling
access. `Preauthorize: false` alone is equivalent to no configuration; remove
all other upstream headers when disabling it.

The gateway strips these headers before forwarding or queueing a request. It
creates an encrypted, caller/Agent/tenant/project-scoped grant when a tool
invocation is admitted. Initialization and discovery do not create grants.
Each new invocation carrying the complete explicit configuration creates a new
grant with the selected lifetime; this is standing client consent, not an
additional web confirmation on each call. A running job keeps its original
authorization and cannot extend it by polling. Removing configuration prevents
new invocations from using a previous configured grant, but does not cancel
already running jobs; revoke the grant or cancel the job to stop existing use.

`ProviderCredentials.authorize()` returns `authorized` with `preauthorized: true`
and the selected non-secret configuration. The configured provider, endpoint,
and model take priority over tool defaults, including `force_new`. Always use
the returned configuration to start work. Changing any of these values or the
key requires obtaining a fresh authorization reference; old references fail
against a different invocation configuration. No configured grant is offered as
a saved web credential. Calls without configuration continue the existing web
approval flow. To return to web approval, remove the upstream headers.

Keys are kept out of MCP arguments/results, Agent-forwarded headers, Run events,
and training exports. Only the trusted execution callback resolves the encrypted
credential after scope and lifetime checks. Reverse proxies and operator-added
HTTP instrumentation must also exclude `X-Nexus-Upstream-Key` from header logs.

## One Key represents one caller

The same Nexus API Key is one identity across clients and MCP sessions. Those
clients share its eligible, unexpired model grants, workspaces and quotas. Use
different Keys for independent callers. `X-Nexus-End-User` is a tracing label,
not a verified identity or a way around limits. Model grants remain bound to the
caller, Agent, tenant and project; another Key cannot reuse or resolve them.
Expiry, revocation, user confirmation and explicit invocation preauthorization
continue to apply.

Agents call `current_run().caller_identity()` to obtain `version`,
`principal_type`, `owner_scope` and `quota_scope` from the authenticated Cloud Run
callback. Bind workspaces to the opaque owner scope (caller, tenant, project,
Agent) and quotas to the quota scope (caller, tenant). Changing sessions or
projects cannot reset these limits. Never substitute tool arguments or unverified
headers for this identity. Old Cloud versions fail closed. Preserve Python context
variables when dispatching calls to threads.

The Wave MCP example enforces two temporary workspaces per caller and four total;
one active call per caller and two total. Pending requests are FIFO per caller
and round-robin between callers, with eight waiting requests per caller, 32 total
and a ten-second queue deadline. Clients should back off before retrying queue
errors. These limits apply to one Wave bridge process, not to every Agent
automatically through a global Cloud scheduler.


## Reusable model connections and batch authorization (Hosted Cloud)

Open [Model connections](https://cloud.nexilume.com/api/v1/model-connections/page/), sign in to your own account, save a model destination, select multiple Agents and explicitly confirm. Choose your own available Nexus Router/model without entering a key, or supply your own external provider endpoint/model/key. Saving a connection alone grants no Agent permission; new Marketplace Agents are not automatically included.

An approved Agent can reuse access across tools and new conversations. Set connection-wide and per-Agent request allowances and expiry (up to 30 days), then revoke an individual permission or the whole connection at any time. Both counters apply atomically. A stream counts once; upstream failures/timeouts also count. Editing permission never resets usage. Request allowances are not monetary or token budgets.

The original upstream key stays in Cloud. Trusted execution receives an Agent-scoped proxy capability. Existing SDK authorize/resolve calls work without an API change: consume the returned provider, base_url and model instead of hard-coding the original destination. Explicit endpoint/model requests must match. Runtime capabilities last at most 24 hours; authorize again to obtain a fresh capability under a still-valid permission without another user confirmation.

Revocation blocks new requests and is checked on subsequent stream chunks. Already-dispatched upstream work may still incur charges. Reapproval never revives old tokens. Existing one-time browser grants and explicit MCP preauthorization remain separate; revoke independent older grants at their original pages. Model permissions do not broaden mobile/computer access.
