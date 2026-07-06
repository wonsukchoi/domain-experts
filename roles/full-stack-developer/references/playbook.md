# Full-Stack Build & Debug Playbook

Filled templates and decision tables for shipping a feature slice. Load when building or reviewing, not for general reasoning (that's SKILL.md).

## The vertical-slice checklist

Order matters — the contract comes before either half, the unhappy paths before the happy one.

1. **Contract** — write the request/response JSON and error shape (below) and paste it where both sides can see it.
2. **State map** — for each value on the page, one row in the state-location table below.
3. **Server** — endpoint + boundary validation + auth check + the query (watch for N+1).
4. **Client** — data fetch through the cache layer, then loading / empty / error / stale states, then the happy path.
5. **Seam test** — real client against real API on a throttled connection (Fast 3G, 4× CPU slowdown in DevTools).
6. **Two-cadence check** — does old client + new server survive the rollout window?

## API contract template

Agree this before writing either side. Concrete example — a "create project" endpoint:

```
POST /api/projects
Request:  { "name": string(1..80), "visibility": "private" | "team" }
Response 201: { "id": string, "name": string, "visibility": string, "createdAt": ISO8601-UTC-string }
Errors (envelope is identical for every endpoint):
  400 { "error": { "code": "VALIDATION", "field": "name", "message": "1–80 chars" } }
  401 { "error": { "code": "UNAUTHENTICATED", "message": "..." } }
  409 { "error": { "code": "DUPLICATE_NAME", "message": "..." } }
```

Rules that prevent seam bugs: timestamps are ISO 8601 UTC strings (never epoch-vs-string ambiguity, never server-local time); money is integer minor units (cents), never a float; one error envelope shape for every endpoint so the client has one error handler, not twenty.

## State-location decision table

Each value gets exactly one owner. Pick the leftmost column that fits.

| Value | Lives in | Why |
|---|---|---|
| Current filter / tab / page number | URL query params | Shareable, survives refresh, back-button works |
| Logged-in user, projects, any DB-backed data | Server cache (React Query/SWR) | Server is source of truth; cache handles staleness |
| Form field being typed | Local component state | Ephemeral, dies on unmount, no one else needs it |
| Theme / sidebar-collapsed | Client persistence (localStorage) | Client preference, never security-relevant |
| Auth token | httpOnly cookie | JS must not be able to read it (XSS defense) |

If a value seems to need two of these, you have a sync bug waiting — pick one owner and derive the rest.

## Rendering-strategy decision table

| Page shape | Strategy | Because |
|---|---|---|
| Marketing / blog / docs, content stable | Static (SSG) | Cheapest, fastest, CDN-cacheable; rebuild on publish |
| Content changes hourly, still public | Incremental static (ISR) or SSG + revalidate | Static speed, bounded staleness |
| Public, personalized or SEO-critical, changes per request | Server-render (SSR) | First paint has real content for crawlers + slow devices |
| Behind auth, not indexed (dashboards, admin) | Client-render (CSR) | No SEO need; ship a shell + fetch, skip SSR's operational cost |

Default: static if it can be, CSR if it's private, SSR only when a public page needs real first-paint content. SSR is the most expensive to operate — make it justify itself.

## Latency budget (mid-tier phone, 4G) — where the 1s goes

| Segment | Target | Common killer |
|---|---|---|
| Network round trips | < 300ms | Waterfall of serial fetches (fix: one combined endpoint) |
| JS bundle parse/execute | < 350ms | 900KB+ bundle (fix: code-split, drop heavy deps) |
| Render | < 400ms | Rendering 500 rows client-side (fix: virtualize/paginate) |
| **First contentful, total** | **< ~1.3s** | |

## Debug order for a slow page (fastest signal first)

1. **Open the Network tab, sort by time.** Is one request slow, or are there many serial ones? Many serial ⇒ waterfall (a client-side collapse, not a DB problem).
2. **Read the slow request's server timing.** API < 200ms means the rest is client-side — stop blaming the database.
3. **Check bundle size** (coverage tab: how much JS is unused on load). > 500KB parsed ⇒ code-split.
4. **Profile the render** (Performance tab). Long task > 50ms ⇒ too many DOM nodes; virtualize.
5. Only after 1–4 point at the server, look at the query plan and indexes.

## Auth handoff template (the boundary that's easy to get wrong)

- Token in an **httpOnly, Secure, SameSite=Lax cookie** — JS can't read it, so an XSS payload can't exfiltrate it.
- Server **verifies on every request** (signature + expiry + revocation check for sensitive actions); never trusts a client-sent user id or role.
- Client treats a 401 as "refresh once, then redirect to login" — a single retry, not an infinite loop.
- CORS: allow only the exact origins you serve; `Access-Control-Allow-Credentials: true` cannot be paired with `Allow-Origin: *` (the browser rejects it) — list origins explicitly.
