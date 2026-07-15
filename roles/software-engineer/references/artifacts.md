# Engineering artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Architecture decision record (filled — see Worked example in SKILL.md for full narrative)

| Field | Content |
|---|---|
| Decision | Implement auth as an internal module with independent deploy pipeline, not a separate microservice |
| Root cause of reported pain | Deploy coupling: 40 blocked deploys/month, ~30 engineer-hours/month lost, not compute scale (auth = 4% of monolith CPU) |
| Alternative considered | Microservice extraction |
| Cost of alternative | +8ms p50 latency, new all-or-nothing failure mode, ~$65,000/year additional on-call cost |
| Cost of chosen option | Engineering time to define module boundary and independent pipeline (one-time); no added latency, no new failure mode, no new on-call cost |
| Revisit trigger | If a real compute/scale constraint (not deploy coupling) materializes for auth specifically |

## 2. Failure-mode enumeration (filled example, payment webhook handler)

| Scenario | Current behavior | Is this acceptable? |
|---|---|---|
| Downstream call times out | Retries 3x with exponential backoff, then dead-letters | Yes — bounded retry, no infinite loop |
| Webhook received twice (duplicate delivery) | Idempotency key checked, second delivery no-ops | Yes — explicitly handled |
| Two webhooks for the same order arrive concurrently | **Not yet handled — race condition possible** | **No — needs a fix before ship** |
| Downstream write partially succeeds (DB write ok, cache update fails) | Currently silent — no reconciliation | **No — needs explicit handling, flagged for this PR** |

**Rule applied:** every enumerated scenario gets an explicit answer before shipping — "not yet handled" is a blocker to resolve, not a note to leave for later.

## 3. Rollback plan template (filled example)

> **Change:** Migrate `orders` table to add a new required `region` column with a backfill.
> **Rollback plan:** Column is added as nullable first (additive, reversible); application code deployed behind a feature flag reads/writes the new column only when the flag is on. If an issue surfaces, the flag flips off instantly (no deploy needed) and the column is simply unused until the fix ships — no destructive migration to undo.
> **What would NOT be reversible:** dropping the old column or making the new one `NOT NULL` — those steps are deliberately scheduled for a separate, later migration only after the flag has been on in production without issue for 2+ weeks.

## 4. Postmortem action item format (filled example)

> **Incident:** Auth module deploy blocked the checkout team's release for 3 hours during a planned launch window.
> **What happened:** Auth and checkout share a deploy pipeline; an unrelated auth change was mid-review when checkout needed to ship.
> **Root cause:** No independent deploy boundary between auth and other monolith modules.
> **Action items:**
> 1. Implement independent deploy pipeline for the auth module — Owner: [Engineer], Due: [date]. (Not "communicate deploy timing better.")
> 2. Add a pre-deploy check that flags cross-team deploy conflicts before they block a release — Owner: [Engineer], Due: [date].
> **Not included:** any action item that isn't a concrete, owned mechanism — "be more careful about deploy timing" was explicitly rejected as insufficient.
