# Technical Writer — Playbook

## Documentation coverage audit (filled example)

| Step | Method | Output |
|---|---|---|
| 1. Inventory | Diff OpenAPI/GraphQL spec against docs-repo page list | Endpoint × doc-page matrix |
| 2. Accuracy pass | Execute every documented request example against staging | Pass/fail per example |
| 3. Gap classification | Undocumented (no page) vs. stale (page exists, example fails) | Two gap buckets, not one |
| 4. Ticket correlation | Match last 30–90 days of support tickets to gap endpoints by name/path | Ticket count per gap endpoint |
| 5. Cost estimate | (gap-endpoint avg handle time − accurate-endpoint avg handle time) × ticket count | Hours/month recoverable |
| 6. Prioritize | Rank by ticket-correlated cost, not raw gap count | Fix order |

Worked numbers (see SKILL.md worked example): 60 endpoints, 45 documented (34 accurate / 11 stale), 15 undocumented. 71 of 214 tickets (33.2%) trace to the 26-endpoint gap; 62 of those 71 (87.3%) trace to the 11 stale endpoints, not the 15 undocumented ones. Fix order: stale first.

## Diátaxis quadrant mapping (filled example)

| Page | Reader intent | Current type | Correct type | Action |
|---|---|---|---|---|
| `POST /webhooks` reference | "What params does this take?" | Mixed reference + tutorial | Reference | Strip the walkthrough prose; move it to a linked how-to |
| "Getting started with webhooks" | "Get a working webhook in 10 min" | Reference (parameter table with no narrative) | Tutorial | Rewrite as numbered steps with one worked example |
| "Why webhooks retry with backoff" | "I don't understand the retry behavior" | Buried as a footnote on the reference page | Explanation | Extract to its own page, link from both reference and tutorial |
| "Migrating from API v1 to v2" | "What do I need to change?" | How-to | How-to (correct) | No change — this is the one page already matching its Diátaxis type |

Diagnostic: a page mixing more than one Diátaxis type is not automatically wrong, but it should be a deliberate exception (small audience, explicitly requested) — not the default.

## Docs-as-code workflow (filled example)

```
1. Engineer opens PR changing POST /users/{id}/roles behavior
2. CI check: "docs-required" label auto-applied if endpoint path
   appears in the diff and no corresponding docs/ file changed
3. Writer (or engineer, for small changes) adds/updates docs/ page
   in the same PR
4. CI runs documented-example-execution test against a staging
   build of the PR branch — build fails if the example 4xx/5xx's
5. Feature owner reviews docs changes as part of normal PR review
   (not a separate downstream review after merge)
6. Merge — docs and code ship atomically, same version
```

Fallback when full docs-as-code isn't feasible (e.g., docs owned by a separate CMS): weekly automated diff of the API spec against the doc site's endpoint list, posted to the docs team's channel, with any new/changed endpoint older than 5 business days flagged as overdue.

## Before/after procedure rewrite (filled example)

**Before (prose-first, task-buried):**
> To authenticate, you'll need to first register an application in the developer console, which will generate a client ID and client secret. These credentials are used in an OAuth 2.0 client credentials flow to obtain an access token, which must then be included as a Bearer token in the Authorization header of subsequent requests. Tokens expire after 3600 seconds.

**After (task-first, example-led):**
> **Get an access token**
> 1. Register an app in the [developer console](/) → copy the Client ID and Client Secret.
> 2. Request a token:
>    ```
>    curl -X POST https://api.example.com/oauth/token \
>      -d "grant_type=client_credentials" \
>      -d "client_id=YOUR_CLIENT_ID" \
>      -d "client_secret=YOUR_CLIENT_SECRET"
>    ```
>    Response: `{"access_token": "...", "expires_in": 3600}`
> 3. Use the token: add header `Authorization: Bearer YOUR_ACCESS_TOKEN` to every request.
>
> Tokens expire after 3600 seconds (1 hour) — request a new one before then, or handle a `401` by re-requesting.
