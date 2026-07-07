# Vocabulary

### Origin shield
A single designated CDN layer that sits between edge nodes and the origin server, consolidating cache-miss requests from many edges into one origin request instead of one-per-edge.
**In use:** "Enable origin shield in the region closest to origin so a cold cache doesn't turn into 40 simultaneous origin hits from 40 edge nodes."
**Common misuse:** Assuming origin shield improves cache-hit ratio for end users — it doesn't; it only protects origin from thundering-herd misses. Hit ratio is still determined by cache-key design.

### Stale-while-revalidate
A cache directive that serves a stale (expired) response immediately while asynchronously fetching a fresh copy in the background, rather than making the user wait for revalidation.
**In use:** "Add `stale-while-revalidate=60` so a slow origin response during revalidation doesn't show up as latency to the user."
**Common misuse:** Treating it as a substitute for correct cache invalidation — it hides revalidation latency, it doesn't make stale content correct to serve indefinitely; still needs a real `max-age`.

### HSTS preload
Submission of a domain to browser vendors' hardcoded preload list, so browsers enforce HTTPS-only even on the very first visit, before any HSTS header has been seen.
**In use:** "We can't preload this domain until every subdomain is HTTPS-only, since preload is a permanent, package-shipped commitment, not a header we can just remove next week."
**Common misuse:** Enabling the `preload` directive in the HSTS header without actually submitting to and being accepted by the preload list — the directive alone does nothing; submission is a separate step, and removal after acceptance can take months to propagate through browser releases.

### Cache-key partitioning
The set of request attributes (URL, query params, headers, cookies) a cache uses to decide whether two requests get the same cached response.
**In use:** "The leak wasn't the cache TTL, it was cache-key partitioning — the key didn't include the auth cookie, so two different users got the same cached response."
**Common misuse:** Assuming a shorter TTL is the fix for stale or leaked per-user content — a TTL of zero on a badly-partitioned key still returns the wrong content within its zero-second window; the key, not the duration, is the correctness surface.

### Time to First Byte (TTFB)
The interval between a client request and the first byte of the response arriving, capturing DNS + connection + server processing time before any content transfer.
**In use:** "TTFB jumped 400ms after the last deploy — that's server processing, not network, since DNS and connection time are unchanged."
**Common misuse:** Treating TTFB as the whole performance picture — a fast TTFB with a slow, unoptimized asset payload still produces a slow page for the user; TTFB isolates server-side latency, not perceived load time.

### WAF (Web Application Firewall) mode: log-only vs. blocking
Log-only records what a rule would have matched without taking action; blocking actively rejects matching requests.
**In use:** "Run the new rule in log-only for a full week of real traffic before flipping it to blocking — that's how we catch the false-positive rate before it costs us users."
**Common misuse:** Skipping the log-only period because a rule "looks safe" in isolation — the false-positive rate against real traffic is empirical, not something a rule's logic alone predicts.

### Content-hashed filename (cache busting)
A build convention where a static asset's filename includes a hash of its content, so any content change produces a new URL, making long-lived immutable caching safe.
**In use:** "Set `max-age=604800, immutable` on `/assets/*` — filenames are content-hashed, so a stale cache just means an old build's assets, never wrong content under the same URL."
**Common misuse:** Applying the same long `max-age` to non-hashed filenames (e.g. `logo.png` referenced by a static path) — without a hash in the name, a long cache means users see stale content after a legitimate update with no way to invalidate short of a manual cache purge.

### Known Exploited Vulnerabilities (KEV) catalog
A CISA-maintained list of CVEs with confirmed active exploitation in the wild, used to prioritize patch urgency independent of raw CVSS severity score.
**In use:** "This CVE is only a 6.5, but it's in the KEV catalog — that overrides the score, patch window is days, not the usual quarter."
**Common misuse:** Prioritizing patches purely by CVSS score — a high score with no known exploitation can reasonably wait for a normal patch cycle; KEV presence is the stronger urgency signal.

### Rate limiting vs. throttling
Rate limiting rejects requests outright once a threshold is exceeded within a window; throttling delays or degrades service (slower responses, reduced quality) without outright rejection.
**In use:** "Throttle the search endpoint under load instead of rate limiting it outright — a slow search result is a better user outcome than a hard 429."
**Common misuse:** Using the terms interchangeably in an incident writeup when the actual client-visible behavior (hard rejection vs. degraded response) differs and matters for root-cause analysis.

### Synthetic monitoring
Automated checks that simulate user requests from external vantage points on a schedule, distinct from real-user monitoring (RUM) which observes actual traffic.
**In use:** "Synthetic monitoring from the EU region caught the outage 4 minutes before any real-user alert fired, since traffic there was light at that hour."
**Common misuse:** Relying on synthetic checks alone and assuming they represent real user experience — a single synthetic check path (e.g. homepage only) can stay green while a real, less-monitored user flow is broken.
