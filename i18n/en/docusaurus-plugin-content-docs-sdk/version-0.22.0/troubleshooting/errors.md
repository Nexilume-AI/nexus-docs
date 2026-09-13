---
sidebar_position: 1
title: Common SDK errors
---

# Common SDK errors

## Router not found

Set `NEXUS_ROUTER_URL` and confirm that the host can resolve and reach it. Auto-discovery failure can mean that mDNS or the default gateway does not match the deployment, not that the router service is down.

## `NexusAuthenticationError`

The token is missing, expired, or has an unacceptable signature. Check `NEXUS_AGENT_TOKEN`, issuer, audience, and device time.

## `NexusAuthorizationError`

Authentication succeeded, but the tenant, capability, or operation is outside the granted scope. Correct the policy or identity instead of granting universal access.

## TLS verification fails

Confirm that the URL hostname matches a certificate SAN and that the correct CA is loaded. A direct IP connection also requires that IP identity in the certificate, or a DNS name covered by it.

## Agent disappears soon after registration

Check that the renewal thread is running, the process is not blocked, router time is correct, and the network is stable. An orderly shutdown revokes the lease; a crash relies on lease expiry.
