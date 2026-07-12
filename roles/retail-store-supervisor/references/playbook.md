# Playbook

Filled operational templates a shift supervisor actually runs — adapt the numbers, keep the structure.

## 1. Daypart staffing model (zone coverage against the traffic curve)

Build this table before writing a schedule, not after. Pull door-count or POS transaction timestamps for the last 4–6 weeks, bucket into 2-hour blocks, and compare each block's share of traffic to its share of scheduled hours.

**Example (mid-size apparel store, 420 weekly labor-hours, 5,000 weekly visits):**

| Block | Share of weekly traffic | Share of weekly hours (current) | Gap | Zone priority |
|---|---|---|---|---|
| Weekday 10am–12pm | 8% | 14% | overstaffed +6pt | 1 register, restock |
| Weekday 12–5pm | 22% | 24% | ~balanced | 2 floor, 1 register |
| Weekday 5–8pm | 18% | 16% | understaffed −2pt | 2 floor, 1 register |
| Sat/Sun 12–4pm | 30% | 4% | understaffed −26pt | fitting room + floor + register, min. 4 |
| All other blocks | 22% | 42% | overstaffed +20pt | 1 floor, 1 register |

**Rule of thumb:** any block more than 10 points out of line between traffic share and hours share gets reallocated before the next posted schedule, not "next time we're doing hours." Zone assignment, not headcount alone, goes on the posted schedule — an associate assigned to "fitting room + register 2" during the 12–4pm peak knows exactly where to be without a huddle.

## 2. Shrink triage sequence

Run this before authorizing loss-prevention surveillance or accusing anyone. Order is cheapest-and-fastest first.

1. **Pull the rolling-quarter shrink rate as % of sales.** Compare to the store's trailing 4-quarter average and to the chain benchmark (NRF's National Retail Security Survey has put industry-wide shrink around 1.5% of sales in recent years — use the current published figure, not this one, for the live comparison).
2. **If shrink is up but under ~2%,** treat it as noise unless a specific SKU/category spike is visible in cycle counts — don't launch an investigation off a single data point.
3. **If shrink exceeds ~2% or has risen 2+ consecutive quarters, audit POS exceptions first:** voids, no-sales, refunds without receipt, and price overrides, sorted by register and by associate, for the period in question. A single register or associate producing a disproportionate share of any one exception type is the fastest, cheapest signal available — cheaper than any camera review.
4. **Cross-check receiving and RTV (return-to-vendor) paperwork** for the same window — mis-keyed receiving counts and un-logged RTVs show up in shrink reports as "unknown loss" and get misattributed to theft.
5. **Only after 3–4 come back clean, escalate to loss-prevention** for camera review or floor surveillance on the specific category/zone the cycle count flagged. Bring the SKU list and time window, not a general "shrink is up" request — a scoped ask gets prioritized faster.
6. **Document the finding either way** (paperwork-error root cause, or LP referral outcome) in the shrink log; a rolling log of causes is what lets next quarter's spike get triaged faster.

## 3. Opening / closing cash-control checklist

**Opening (key holder, before doors):**
- [ ] Walk the sales floor and stockroom for overnight alarm/security exceptions before disarming.
- [ ] Count the opening bank against the prior night's close-out total; discrepancy over $10 gets logged and flagged to the store manager same day, not carried silently to the next count.
- [ ] Confirm registers are set to the correct date and starting float.
- [ ] Check the overnight markdown/price-change log against the POS to confirm nothing posted incorrectly.

**Closing (key holder, after doors):**
- [ ] Each register counted independently by the associate who ran it, then verified by the closing key holder — never counted by one person alone.
- [ ] Over/short beyond $10 per register gets a same-night note (till, associate, amount) — patterns across multiple nights from the same register or associate are the actual signal, not any single shortage.
- [ ] Deposit prepared and logged with two names on the count sheet.
- [ ] Fitting rooms and stockroom swept for unpurchased merchandise before alarm set.
- [ ] Pass-down log written for the opening shift: anything low on the floor, any associate issue, any maintenance/safety item.

## 4. Coaching conversation templates

**In-the-moment correction (30–60 seconds, private):**
"[Specific observed behavior] — [specific expected behavior] — [check for understanding]." Example: *"I noticed you were behind the counter on your phone when the fitting room line built up — when it's busy like that, phones stay in the back and everyone's on the floor. Make sense?"* No apology framing, no accusation, no comparison to other associates.

**Documented corrective conversation (pattern or policy violation):**
```
DATE: _____   ASSOCIATE: _____   SUPERVISOR: _____
BEHAVIOR (specific, observed, dated instances — not "attitude" or "effort"):
  1. _____
  2. _____
EXPECTATION (the specific standard, referenced to the handbook/policy if applicable):
  _____
PRIOR CONVERSATIONS (date of any informal check-in already had):
  _____
NEXT STEP IF UNCHANGED (stated plainly, not implied):
  _____
ASSOCIATE RESPONSE / CONTEXT OFFERED:
  _____
```
Two informal check-ins before this form appears, except for integrity or safety violations, which go straight to documentation on the first occurrence.

## 5. Predictive-scheduling (Fair Workweek) quick reference

For jurisdictions with a statute (Oregon statewide; NYC, San Francisco, Seattle, Chicago, Philadelphia as of their respective ordinances):

| Trigger | Default action |
|---|---|
| Schedule needed >14 days out | Post per statute's notice window (commonly 14 days) |
| Change needed inside the notice window, no true emergency | Voluntary sign-up sheet first; if filled involuntarily, predictability pay applies |
| Weather closure, safety incident, another associate's no-call/no-show | Statute's emergency exception generally applies — document the trigger reason on the schedule-change log same day |
| Associate requests a shift swap voluntarily | Not a statutory "employer-initiated change" in most ordinances — confirm local text, log the swap, no predictability pay owed |
| Back-to-back close-then-open ("clopening") under a required minimum-rest ordinance | Confirm the local rest-period minimum (commonly 9–11 hours) before posting; violations carry a per-instance premium in several ordinances |

Jurisdiction text controls — this table is a starting checklist, not a substitute for the store's actual posted-notice-window and premium-pay figures, which vary by ordinance and get updated by the corporate labor-compliance team.
