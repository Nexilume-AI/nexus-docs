---
title: Router source recovery
---

# Router source recovery

Provider health describes the provider runtime/account. Router health also depends
on each bound source endpoint and advertised model. A healthy Provider therefore
does not prove that every Router source can serve a request.

Managed runtime restarts can change their bound ports. On runtime start and during
periodic health refresh, Nexus synchronizes eligible Provider and source endpoints
with the runtime's current endpoint. Only actual endpoint changes are saved, and
source health checks are queued after the transaction commits. The periodic sweep
provides a fallback if an immediate check cannot be scheduled.

One failed source check does not stop checks for the rest of the Router. Disabled
sources and stopped/deleted runtimes are not automatically reactivated. Removed,
pending or unhealthy model offers remain unavailable until an upstream refresh
and subsequent health checks confirm recovery.

If an upstream model disappears, keep its binding when you intend to wait for it.
Nexus does not silently replace that model with another. Automatic checks can
recover it when the upstream supplies it again; they cannot restore a model the
upstream has withdrawn or replenish an exhausted account quota.

For diagnosis, compare the Provider runtime endpoint with each Router source,
then inspect source error details and the upstream model catalog. Confirm worker
and periodic-task health before relying on background recovery. Cancellation or
an incomplete client stream is handled separately from a verified account/quota
failure, avoiding false account-unavailable states.
