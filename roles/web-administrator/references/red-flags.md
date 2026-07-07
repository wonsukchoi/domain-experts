# Red Flags

### TLS certificate expiring in under 3 days with no rotation ticket open
- **Usually means:** expiry alerting is misconfigured or firing into a channel nobody watches; second most likely — automation target (LB/CDN) differs from the automation's assumed target.
- **First question:** who owns the rotation for this specific cert, and has automation actually run against production or only staging?
- **Data to pull:** cert expiry monitoring history for this domain, automation run logs for the last successful renewal.

### CDN cache-hit ratio under 85% on a path marked cacheable
- **Usually means:** over-specific cache key (session/auth cookie or tracking query params included); second most likely — `max-age` too short for the actual content change frequency.
- **First question:** what's in the cache key besides the URL path?
- **Data to pull:** sample of cache-miss requests with full request headers and query strings.

### 5xx error rate over 1% for more than 5 consecutive minutes
- **Usually means:** recent deploy or config change; second most likely — a dependency (database, upstream API, DNS resolution) degraded.
- **First question:** what changed in the last 2 hours?
- **Data to pull:** deploy/change log timestamped against the error-rate graph, origin logs scoped to the 5xx responses.

### DNS query volume to authoritative servers up more than 3x baseline with no traffic increase
- **Usually means:** a TTL was set too low and left there, or a resolver/client is not honoring TTL (aggressive re-query); second most likely — a misconfigured client retrying failed lookups.
- **First question:** did we change a TTL recently and forget to restore it?
- **Data to pull:** TTL change history for the zone, query logs broken down by resolver source.

### WAF/rate-limiter false-positive reports from more than 0.1% of legitimate sessions
- **Usually means:** a rule went from log-only to blocking mode without a traffic-sample validation period; second most likely — a legitimate traffic pattern (bot-like but real, e.g. a partner integration) matches an attack signature.
- **First question:** was this rule ever run in log-only mode against real traffic before blocking was enabled?
- **Data to pull:** blocked-request sample with matched rule ID, cross-referenced against known partner/integration IP ranges.

### Origin server CPU or connection count pinned above 80% while CDN reports normal traffic
- **Usually means:** cache-hit ratio dropped (more requests reaching origin than expected) or a non-cacheable endpoint is being hit at unusually high volume; second most likely — a scraping/bot pattern bypassing cache via randomized query params.
- **First question:** has the cache-hit ratio changed in the last hour, and is the origin load concentrated on one path?
- **Data to pull:** CDN cache-hit ratio trend, origin access log top-paths-by-request-count for the current hour.

### A load balancer health check passes but user reports say the service is down
- **Usually means:** health check endpoint doesn't exercise the actual failing dependency (checks `/health` which returns 200 regardless of database connectivity); second most likely — the failure is regional/CDN-edge-specific and not visible from the health check's vantage point.
- **First question:** does the health check endpoint touch the same dependency that's failing for users?
- **Data to pull:** health check endpoint implementation, synthetic monitoring results from the affected region specifically.

### Certificate chain validates on the server but fails in some clients
- **Usually means:** intermediate certificate missing from the served chain (works in browsers that cache the intermediate, fails in clients/API consumers that don't); second most likely — an outdated root store on the client side.
- **First question:** is the full chain (leaf + intermediate) being served, or just the leaf?
- **Data to pull:** `openssl s_client -showcerts` output against the live endpoint, compared to the CA's published chain.

### Redirect chain longer than 2 hops on a high-traffic path
- **Usually means:** an old migration redirect was never cleaned up and is stacking with a newer one; second most likely — HTTP-to-HTTPS and www-to-apex (or reverse) redirects both firing in sequence.
- **First question:** how many of these hops are still necessary today?
- **Data to pull:** full redirect chain trace (`curl -IL`) for the affected URL pattern.

### Backup restore test hasn't been run in over 90 days
- **Usually means:** backups are being taken but nobody has verified they're restorable; second most likely — restore process depends on infrastructure/credentials that have since changed.
- **First question:** when was the last successful test restore, and did it use the current restore procedure?
- **Data to pull:** backup job success logs (not the same as restore success), last test-restore date and outcome.
