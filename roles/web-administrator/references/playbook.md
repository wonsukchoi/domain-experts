# Playbook

Filled runbooks. Populate the bracketed fields; the sequence and thresholds are the reusable part.

## Runbook: TLS certificate rotation (planned)

| Step | Action | Threshold / detail |
|---|---|---|
| T-30d | Alert fires (info) | Cert expiry in 30 days |
| T-14d | Alert fires (warning), rotation ticket opened | Assign owner, confirm automation target vs. manual |
| T-7d | Rotation executed in staging, validated | Chain, key match, SAN list checked against current domain set |
| T-3d | Alert fires (critical, pages on-call) if not yet rotated in prod | Escalation: on-call + manager |
| T-0 | Prod rotation, verified from 3+ external vantage points | `openssl s_client -connect host:443 -servername host` from outside the network, not just localhost |
| T+1d | Confirm every pinned location updated | Load balancer, CDN origin config, internal service-to-service certs, mobile app cert pins if any |

Failure mode this catches: automation renews the cert but a load balancer or CDN still points at the old cert file/reference — verified only by checking every pinned location, not just "automation ran successfully."

## Runbook: DNS cutover (planned migration)

1. **T-48h to T-24h:** lower TTL on the record(s) being changed to 300s. Confirm the *lowered* TTL has propagated (query from 3+ public resolvers) before proceeding — a TTL change is subject to the *old* TTL just like any other record change.
2. **T-0:** confirm old TTL has fully expired everywhere (wait ≥ old TTL duration from when the 300s change was confirmed live, not from when it was requested).
3. Update the record to the new value.
4. Verify from resolvers in each affected region: `dig +short <host> @<regional-resolver>` — confirm new value, not cached old value.
5. Monitor origin (old) and new target simultaneously for 2x the old TTL duration — traffic should fully shift within that window; residual traffic to the old target past that window means a client is caching DNS at the application layer (not resolver-level), which needs separate investigation.
6. **T+48h:** restore TTL to steady-state value (3600s+).

## Runbook: incident triage (unplanned)

| Order | Check | Why first |
|---|---|---|
| 1 | CDN/edge logs — request volume, status code distribution, by region | Scopes blast radius before touching origin |
| 2 | Load balancer health check status per origin node | Distinguishes "all origins down" from "one bad node taking 33% of traffic" |
| 3 | Recent deploys/config changes (last 2h) | Most incidents correlate with a change; check before assuming external cause |
| 4 | Origin application logs, scoped to the affected path only | Avoid drowning in unrelated log volume |
| 5 | External dependency status (DNS provider, CDN provider, upstream API) pages | Rule out "not us" before deep origin debugging |

Rollback-first rule: if step 3 finds a change in the last 2h and the fix isn't obvious within 10 minutes, roll back the change before continuing to debug — debugging in production while the change stays live spends SLA budget for no diagnostic benefit over debugging after rollback.

## Runbook: CDN cache-key audit (cache-hit ratio below 85% target)

1. Pull a sample of cache-miss requests (100–500) from CDN logs for the affected path.
2. Diff the cache key components across the sample: query string params, cookies, headers included via `Vary`.
3. Common cause ranking: (a) session/auth cookie included in cache key when the response doesn't actually vary by it, (b) tracking query params (`utm_*`, `fbclid`) fragmenting the key for identical content, (c) `Vary: Accept-Encoding` combined with inconsistent encoding negotiation across edge nodes.
4. Fix by narrowing the cache key to only the dimensions that actually change the response body — strip tracking params before the cache lookup (not before analytics logging), and confirm the response truly doesn't vary by the cookie/header before removing it from the key.
5. Re-measure cache-hit ratio 24h after the fix (allow one full cache-fill cycle).

## Table: uptime SLA budget by tier

| SLA | Allowed downtime / month | Allowed downtime / year |
|---|---|---|
| 99.9% | 43.2 min | 8.76 hours |
| 99.95% | 21.6 min | 4.38 hours |
| 99.99% | 4.32 min | 52.6 min |
| 99.999% | 25.9 sec | 5.26 min |
