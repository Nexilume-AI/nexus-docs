#!/bin/sh

# Read-only diagnostic collector for Nexus Agent Router on OpenWrt.
# Review the output before sharing it outside your organization.

section() {
    printf '\n===== %s =====\n' "$1"
}

redact() {
    sed -E 's/((token|secret|password|authorization|private[_ -]?key)[=: ]+)[^ ,;]+/\1[REDACTED]/Ig'
}

section "collector"
printf 'generated_utc='; date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date
printf 'hostname='; uname -n

section "system board"
ubus call system board 2>&1

section "capacity"
df -h 2>&1
free 2>&1

section "installed nexus packages"
apk info 2>/dev/null | grep -E '^(agentd|agent-gw|agent-adapter|agent-cardd|agent-netd|luci-app-agent-router|nexus-agent)' || true

section "service state"
for service in agentd agent-gw agent-adapter agent-netd nexus-relayd nexus-directoryd; do
    if [ -x "/etc/init.d/$service" ]; then
        printf '%s enabled=' "$service"
        /etc/init.d/"$service" enabled >/dev/null 2>&1 && printf 'yes' || printf 'no'
        printf ' running='
        /etc/init.d/"$service" running >/dev/null 2>&1 && printf 'yes\n' || printf 'no\n'
    else
        printf '%s installed=no\n' "$service"
    fi
done

section "safe uci summary"
for item in \
    agent.main.enabled \
    agent.main.router_id \
    agent.main.domain_id \
    agent.main.discovery_enabled \
    agent.main.discovery_publish_enabled \
    agent.main.lan_auto_promotion_mode \
    agent.main.relay_enabled \
    agent.main.max_routes; do
    value="$(uci -q get "$item" 2>/dev/null || true)"
    printf '%s=%s\n' "$item" "${value:-[unset]}"
done

section "ubus objects"
ubus list 'agent*' 2>&1

for method in stats recovery policy addresses; do
    section "ubus agent $method"
    ubus call agent "$method" 2>&1 || true
done

section "recent redacted logs"
logread 2>/dev/null | grep -E 'agentd|agent-gw|agent-adapter|agent-netd|nexus-relay|nexus-directory' | tail -n 200 | redact

section "end"
printf 'Review this output before sharing. Configuration secrets and private key files are intentionally not collected.\n'
