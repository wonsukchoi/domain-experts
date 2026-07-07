# Reservation and Transportation Ticket Agent — Playbook

## Denied-boarding compensation tier table (DOT 14 CFR Part 250)

| Delay vs. original scheduled arrival | Compensation | Cap |
|---|---|---|
| 0–1 hour | $0 (no compensation required) | — |
| 1–2 hours (domestic) / 1–4 hours (international) | 200% of one-way fare | $775 |
| Over 2 hours (domestic) / over 4 hours (international) | 400% of one-way fare | $1,550 |

Caps are inflation-indexed by DOT periodically — confirm current figures against the latest published rule before quoting a passenger; the table above reflects the standard formula structure, not necessarily today's exact cap.

Payment must be offered in cash/check equivalent by default; travel credit is only valid if the passenger affirmatively chooses it over cash after being told the cash amount.

## Voluntary-solicitation auction sequence

1. Announce the oversell and the number of seats needed.
2. Open with a below-cap offer (e.g., $400–$500 credit + rebooking) — most oversells clear here.
3. If insufficient volunteers, raise in $100–$200 increments every 2–3 minutes.
4. Stop raising once enough volunteers accept; do not average or split the offer across all volunteers — each accepted volunteer gets the offer live at their acceptance.
5. If departure is under 30 minutes away, skip incremental raising and open at a higher anchor (e.g., $700–$800) — time to fill the gap is now the binding constraint, not compensation cost.
6. If still short after solicitation closes, move to involuntary denial using the boarding-priority list.

## IROP (irregular operations) rebooking sequence

| Step | Action | Note |
|---|---|---|
| 1 | Identify disruption code | Weather/ATC, mechanical, crew, or oversell — each has a different waiver policy |
| 2 | Check carrier's IROP waiver matrix | Some codes authorize fare-class-cross rebooking with no fee; others don't |
| 3 | Re-search live inventory | Never reuse an itinerary quoted more than a few minutes earlier |
| 4 | Rebook in same cabin first | Only downgrade/upgrade cabin if same-cabin inventory is genuinely unavailable |
| 5 | Log disruption code + fare basis + any waiver applied | Reservation note must support the decision without re-asking the passenger |

## Boarding-priority list (example structure)

| Priority tier | Criteria |
|---|---|
| 1 (protected — never denied) | Unaccompanied minors, passengers with documented medical/disability needs requiring this specific flight |
| 2 | Highest fare class, earliest check-in |
| 3 | Elite frequent-flyer status, mid-tier fare class |
| 4 | Standard fare class, ranked by check-in time (earliest protected first) |
| 5 (first denied if involuntary needed) | Lowest fare class, latest check-in time |

Deviating from the published list without a documented reason (e.g., a tier-1 protected passenger) is the single most common trigger for a discrimination complaint — the list exists precisely so no individual agent judgment call is required in the moment.

## Fare-change fee lookup discipline

Before quoting a change fee or waiver, always check the specific fare-basis code on the ticket being changed — not the route, not the general "economy" bucket. The same route on the same day can carry three different fare-basis codes with three different change-fee amounts, because they were sold from different inventory buckets at different times.
