# Playbook

Filled templates a territory rep actually runs. Starting points to adapt with real account numbers, not scripts to read verbatim.

## 1. Incumbent-contract teardown

Run before drafting any proposal against a competitive account. The goal is a true total-cost number for the competitor, not their sticker rate.

**Filled example (waste and recycling, mid-size manufacturer):**

| Line item | Incumbent (Republic) | Your quote |
|---|---|---|
| Base rate — 8yd container, 3x/week | $2,180/mo | $2,050/mo |
| Fuel surcharge | 18% of base, uncapped | 8%, capped |
| Environmental/regulatory fee | $95/mo flat | $65/mo flat |
| Contamination fee (recycling) | $45/pull if triggered, avg 2x/mo | $0 — included in service |
| Contract escalator | CPI + 2%, no cap | CPI, capped at 4%/yr |
| **True monthly total** | **$2,180 + $392 (18%) + $95 + $90 (avg contamination) = $2,757** | **$2,050 + $164 (8%) + $65 = $2,279** |

**Reconstructed annual gap:** ($2,757 − $2,279) × 12 = **$5,736/year**, an 17.3% true reduction — versus the naive base-rate-only comparison, which understates the gap at only 6.0% ($2,180 vs. $2,050).

**Rule:** never present a savings number built from base rate alone. Pull the incumbent's last three invoices if the prospect will share them; if not, quote the fee-stack pattern typical for that vendor and flag it as an estimate to be confirmed against their actual bill.

## 2. Renewal-window timeline

Built the moment a competitive account is identified — this is what determines whether the account is even reachable this cycle.

```
ACCOUNT: [Prospect name]              INCUMBENT: [Vendor]
CONTRACT TERM END:        Dec 1
CANCELLATION NOTICE DUE:  Nov 15 (60 days prior — confirm exact clause)
TODAY:                    Oct 27  →  19 days to notice deadline

Backward schedule from Nov 15:
  Oct 27–31   Discovery + fee-stack teardown
  Nov 1–5     Proposal drafted, internal pricing approval
  Nov 6–10    Presentation to economic buyer + procurement
  Nov 11–13   Redlines / final terms
  Nov 14      Signature (1-day buffer before deadline)
  Nov 15      Prospect files cancellation with incumbent
  Dec 1–5     Install window (coordinate with ops capacity)

VERDICT: reachable, but only with weekly touches starting now —
  monthly-cadence nurture will not clear this window.
```

**Rule:** if the backward schedule doesn't fit inside today's date and the notice deadline, say so internally before promising a close this cycle — a deal quoted as "in progress" past the deadline is dead pipeline, not slow pipeline.

## 3. Save-call script (account gave cancellation notice)

Run within 24 hours of notice. Order matters — discount comes last, if at all.

1. **Open with acknowledgment, not a pitch:** "I saw the cancellation notice — before anything else, can you walk me through what triggered it?" Listen for a specific incident (missed pickup, billing error, late delivery), not a general "not happy."
2. **Pull the account's own service log** — actual missed-pickup count, average replacement/repair time, billing disputes over the last 6 months — before responding, so the fix targets the real number, not the complaint's tone.
3. **Name the root cause back to them and propose a specific fix** tied to that number: "Your last two pickups were 30-90 late because your route driver changed twice this quarter — we're moving you to [driver] permanently and adding a text alert 1 hour before arrival."
4. **Offer a service credit or SLA guarantee before a price discount** — e.g., "if we miss a pickup window in the next 60 days, that month's service is free" — a reliability commitment addresses churn drivers a discount doesn't.
5. **If price is the stated and confirmed root cause** (not a proxy for a service complaint), bring a one-time retention adjustment to a manager for approval — never authorize on the call, and never repeat the same discount at the next renewal without a term extension attached.
6. **Log the save attempt and outcome** regardless of result — a lost save call with documented root cause becomes next quarter's win-back list entry.

## 4. Territory route-density review

Quarterly, before committing quota targets for the next period.

**Filled example (75-stop territory, uniform/facility services):**

| Route | Stops | Revenue/stop/mo | Miles between stops (avg) | Verdict |
|---|---|---|---|---|
| Route A (dense, urban) | 22 | $410 | 1.2 | add stops here first |
| Route B (suburban) | 28 | $365 | 3.8 | add only if within 2mi of existing stop |
| Route C (rural spur) | 12 | $290 | 9.5 | do not add — decline new stops beyond current 12 |

**Rule of thumb:** a new account within ~2 miles of an existing route stop adds revenue at near-zero incremental drive time and should be prioritized in prospecting lists. An account requiring a new spur route needs a minimum committed revenue (route-dependent, confirm with ops — commonly 1.5–2x an in-route account) to clear a positive contribution margin; below that threshold, book it only with ops sign-off on the added drive cost, not by default.
