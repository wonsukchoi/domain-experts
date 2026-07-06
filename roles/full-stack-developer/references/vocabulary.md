# Vocabulary

Terms of art full-stack work turns on that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Hydration

- **Definition:** attaching client-side JavaScript (event handlers, state) to server-rendered HTML that's already on screen, so the static markup becomes interactive.
- **In use:** "The page paints instantly from SSR but the buttons are dead for 400ms — that's the hydration gap; the bundle has to download and run before it's interactive."
- **Common misuse:** treating SSR as "fast and done." SSR gives a fast *paint*; the page isn't *interactive* until hydration finishes, and a heavy bundle makes that lag (measured as INP now, formerly TBT) — a fast-looking page that ignores taps.

## Optimistic UI

- **Definition:** updating the interface as if a write succeeded before the server confirms, then rolling back if it fails.
- **In use:** "Like is optimistic — the heart fills instantly and we reconcile on the response; if the POST 500s we revert the count."
- **Common misuse:** applying it to values where a wrong-then-corrected number misleads (a balance, an inventory count), or omitting the rollback so a failed write silently leaves the UI lying about the database.

## Idempotency

- **Definition:** a request that produces the same result whether sent once or five times — safe to retry.
- **In use:** "Payment submit sends an idempotency key so a double-click or a network retry doesn't charge the card twice."
- **Common misuse:** assuming GET-is-safe covers it and leaving POST/PATCH un-keyed, so a client retry on a flaky network creates duplicate orders. Retries are normal, not exceptional — the endpoint has to expect them.

## CORS

- **Definition:** a browser security mechanism that blocks a page on origin A from reading responses from origin B unless B's headers opt in.
- **In use:** "The API 200s in curl but the browser blocks it — CORS. The server needs to echo our exact origin and, since we send cookies, `Allow-Credentials: true`."
- **Common misuse:** thinking CORS is a server-side auth control (it isn't — it's browser-enforced and curl/mobile ignore it), or "fixing" it with `Allow-Origin: *`, which the browser refuses to combine with credentialed requests.

## Race condition (client-side)

- **Definition:** two async operations whose result depends on which finishes first — classically, a stale response overwriting a fresh one.
- **In use:** "Typeahead had a race: the 'a' request resolved after 'ab' and clobbered the results. We cancel in-flight requests on each keystroke now."
- **Common misuse:** assuming responses arrive in the order they were sent. They don't; the slower earlier request can land last, so the UI needs cancellation or last-write-wins keyed to the query.

## Source of truth

- **Definition:** the one place a piece of data is authoritative; every other copy is a cache derived from it.
- **In use:** "The database is the source of truth for the cart; the client cart is a cache we invalidate on every mutation."
- **Common misuse:** letting the same value be independently editable in two places (client state and server) with no designated authority, so they drift and "which one is right" becomes a debugging session.

## SSR vs SSG vs CSR

- **Definition:** where and when HTML is built — server-rendered per request (SSR), pre-built at deploy (SSG), or assembled in the browser from JS (CSR).
- **In use:** "Docs are SSG, the dashboard is CSR behind auth, and the public product page is SSR for the crawler."
- **Common misuse:** defaulting everything to SSR "for performance." SSR adds server cost and a hydration gap; a private dashboard gains nothing from it, and static content is faster pre-built.

## N+1 query

- **Definition:** fetching a list (1 query) then firing one more query per item (N), when a single join or batched load would do.
- **In use:** "The feed was an N+1 — 1 query for posts, then one per author. A dataloader batched the authors into a single round trip."
- **Common misuse:** blaming a slow list on "the database needs an index" when the real cost is 200 sequential round trips an ORM issued lazily; an index doesn't fix the trip count.

## Server state vs client state

- **Definition:** server state is data that lives in the backend and is cached in the browser (users, posts); client state is UI-only and never persisted server-side (a modal being open, a filter).
- **In use:** "That doesn't belong in Redux — it's server state; React Query owns it with staleness and refetch built in."
- **Common misuse:** hand-rolling server data into a global store with manual loading flags and cache invalidation, reinventing what a fetch-cache library already handles, and conflating "shared" with "global."

## Content Security Policy (CSP)

- **Definition:** a response header telling the browser which script/style/image sources are allowed to load, limiting the blast radius of XSS.
- **In use:** "We tightened the CSP to drop `unsafe-inline` for scripts, so an injected `<script>` won't execute even if something gets past input sanitizing."
- **Common misuse:** treating CSP as a replacement for output encoding and validation (it's defense in depth, the last layer), or shipping `unsafe-inline`/`unsafe-eval` so broadly the policy stops the browser from blocking anything.
