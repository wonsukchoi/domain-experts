# Red Flags

Cross-stack smell tests. Format per flag: what it usually means, the first question to ask, the check to run.

## Validation exists in the UI but the endpoint accepts anything

- **Usually means:** the limit (quantity, price, role, file size) was enforced in the form only, so a crafted request bypasses it. The second most likely cause: the server "validates" by trusting a field the client sent (`isAdmin`, `userId`).
- **First question:** "What happens if I POST this endpoint directly with curl and a value the form would reject?"
- **Check:** hit the endpoint with the client removed — an out-of-range value, a missing auth cookie, another user's id. If any succeeds, the real validation was never on the server.

## Page makes 10+ requests before it shows anything

- **Usually means:** a request waterfall — components fetch on mount so round trips run serially — or an N+1 where a list renders one request per row.
- **First question:** "Are these requests parallel or does each wait for the one above it?"
- **Check:** Network tab, waterfall view. Staircase shape ⇒ serialize into one combined endpoint. Same URL pattern repeated per row ⇒ N+1; batch it server-side.

## API is fast (<200ms) but the page still takes seconds

- **Usually means:** the cost is client-side — bundle parse or render — not the backend everyone is about to optimize.
- **First question:** "How big is the JS bundle, and how many DOM nodes does this page mount?"
- **Check:** Coverage tab for unused JS on load (>500KB parsed ⇒ code-split); Performance tab for long tasks (>50ms render ⇒ virtualize the list). Do this before touching the query plan.

## Dates or amounts are wrong by a timezone or a rounding cent

- **Usually means:** a serialization mismatch at the boundary — server-local time sent instead of UTC, or money stored/sent as a float so 0.1 + 0.2 = 0.30000000000000004.
- **First question:** "Is this an ISO 8601 UTC string end to end, and is money an integer in minor units?"
- **Check:** inspect the raw JSON on the wire (not the rendered value). A timestamp without `Z`/offset, or a monetary value with a decimal point, is the bug.

## TypeScript types are green but production throws on real API data

- **Usually means:** the type is asserted at the boundary (`as ResponseType`, or an unchecked generic on the fetch) with no runtime validation, so malformed or null data crashes three layers deep instead of being rejected at the door.
- **First question:** "Is there a runtime schema parsing this response, or is the type a hope?"
- **Check:** grep the fetch layer for `as ` casts and untyped `.json()`. Add a Zod/valibot parse at the edge; the crash moves to a clear boundary error.

## "It works locally" but breaks in production only

- **Usually means:** an environment gap — CORS origin, a cookie's Secure/SameSite flag, an env var, or an absolute `localhost` URL that shipped.
- **First question:** "What is different between local and prod for this request — origin, protocol, cookie flags, base URL?"
- **Check:** the browser console for the CORS/cookie error text (it's specific), and grep for hardcoded `http://localhost`. `SameSite=Lax` cookies won't send on cross-site prod requests that worked same-origin locally.

## State shown in the UI disagrees with the database

- **Usually means:** two owners for one value — an optimistic update that never reconciled, or a client cache never invalidated after a write.
- **First question:** "Who is the source of truth for this value, and what invalidates the client copy after a mutation?"
- **Check:** trace the write path — does it invalidate/refetch the affected cache key on success? If the UI updates optimistically and there's no rollback on error, a failed write leaves a lie on screen.

## Bundle grew by hundreds of KB after a small feature

- **Usually means:** a heavy dependency pulled in whole — a date library (~70KB), an entire utility package for one function, or a charting lib imported eagerly instead of lazily.
- **First question:** "What did this feature add to the bundle, and does it need to load on first paint?"
- **Check:** a bundle analyzer (source-map-explorer / the framework's analyze mode). Move rarely-used heavy libs behind a dynamic import; replace whole-package imports with the single function or a lighter dep.

## Auth token readable from JavaScript

- **Usually means:** the token is in localStorage or a non-httpOnly cookie, so any XSS payload can read and exfiltrate it — session theft, not just a defaced page.
- **First question:** "Can `document.cookie` or `localStorage` see the session token in the console right now?"
- **Check:** open the console on a logged-in page and read them. If the token is there, move it to an httpOnly Secure cookie; the client should never need to read it.
