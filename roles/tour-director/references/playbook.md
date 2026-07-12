# Tour Director — Playbook

## Pre-departure reconciliation (filled example, 10-day / 34-pax motorcoach tour)

| Document | Check | Result | Action if mismatched |
|---|---|---|---|
| Passenger manifest | Total headcount | 34 confirmed pax + TD + driver = 36 | N/A |
| Rooming list | Occupancy codes sum to manifest count | 15 doubles (30) + 4 singles (4) = 34 | Recount before submitting to hotel |
| Hotel confirmations | Voucher/confirmation number on file for all 9 nights | 9/9 confirmed | Call hotel direct for any missing night |
| Motorcoach contract | Seating capacity ≥ manifest + 2 (driver, TD) | 49-seat coach for 36 pax — headroom for late add | Flag if capacity is exact or under |
| Step-on/local guide bookings | Confirmed for each scheduled city, with a named contact and phone number | 6/6 confirmed | Reconfirm 48 hours ahead if unconfirmed |
| Restaurant reservations (group meals) | Confirmed headcount and any table-turn time limit noted | 4/4 confirmed, 2 with hard turn times noted | Note turn-time constraint on daily schedule sheet |
| Documents wallet | Insurance certs, emergency contacts, guest document photocopies | Complete | Do not depart without this |

A rooming list's primary sort should carry a high tag number for the TD and driver so they sort to the bottom, and doubles/twins should be sequenced before triples, then singles — this is what the hotel uses to block rooms before arrival, so errors here surface at check-in with zero slack to fix them.

## Vendor-chain contingency map (filled example)

| Disruption | Trigger | Downstream commitments to re-check | Fallback |
|---|---|---|---|
| Coach mechanical failure | Breakdown or delay >60 min en route | Same-day hotel check-in window, any same-day step-on guide, same-day group meal reservation | Call operator ops desk if delay affects lodging; for a single-city delay, recompute usable time against each downstream booking's own hard constraint (not the original schedule) before canceling anything |
| Hotel overbooking on arrival | Rooming list confirmed but hotel has no matching block | Same-night lodging for full group | Call operator ops desk immediately — this is above TD spending authority; do not personally guarantee alternate rooms on a card |
| Step-on/local guide no-show or unavailable | No guide at confirmed meeting point past 15 min | That city's cultural/historical content coverage | TD delivers available written/prepared content as a walking commentary; report the no-show to operator for that vendor relationship, not just this trip |
| Border-crossing document issue (single guest) | Passport/visa problem flagged at crossing | That guest's ability to continue same-day | Operator's or consulate's stated procedure; the rest of the group continues on schedule with a rejoin point identified, guest does not travel alone without operator sign-off |
| Restaurant table-turn conflict | Group arrival time now closer to reservation than the required turn window | That meal's start time and any activity scheduled directly before it | Recompute actual slack (not planned slack) between the last activity and the reservation before assuming a change is needed — see SKILL.md worked example |

## Gratuity and per-diem reconciliation (filled example, 10-day / 34-pax tour, 2 guests depart after day 6)

Operator guideline: TD gratuity $8/person/day; driver gratuity $3/person/day (stated heuristic, operator policy controls).

| Line | Calculation | Amount |
|---|---|---|
| Full-trip guests (32 pax × 10 days) — TD | 32 × 10 × $8 | $2,560 |
| Full-trip guests (32 pax × 10 days) — driver | 32 × 10 × $3 | $960 |
| Early-departure guests (2 pax × 6 days served) — TD | 2 × 6 × $8 | $96 |
| Early-departure guests (2 pax × 6 days served) — driver | 2 × 6 × $3 | $36 |
| **TD gratuity pool total** | $2,560 + $96 | **$2,656** |
| **Driver gratuity pool total** | $960 + $36 | **$996** |

The naive approach — dividing a flat suggested total ($8 × 34 × 10 = $2,720) evenly across all 34 names on the manifest — over-collects from guests who never asked to be billed for 10 days of service they didn't receive, and creates a dispute if anyone checks the math. Prorating by person-days actually served (6 days for the pair who departed, 10 for everyone else) is the number that reconciles to what was actually delivered, and it's the number the TD should be prepared to show if asked.

## Day-one briefing checklist (structure, not verbatim script)

1. Itinerary shape: number of days, cities, one distinguishing highlight per city — not the full stop-by-stop detail.
2. Safety and headcount protocol: when counts happen (every coach loading, every hotel departure), what a guest does if separated.
3. Money handling: per diem schedule and form (cash vs. card), gratuity guideline and collection method (envelope, timing), optional-excursion menu with prices and what's already included in the base tour.
4. Communication channel: how to reach the TD off-schedule (room phone extension, messaging app), and what counts as an emergency versus a question that can wait for the next scheduled briefing.
5. Seat rotation policy: pattern and frequency, and how a guest with a mobility need can request an exception.

## Disruption-announcement template (structure)

1. State what happened (one sentence, factual, no apology-first framing).
2. State the new plan (what changes, what stays the same).
3. Name what's preserved or how the loss is mitigated (a written handout, a self-guided alternative, an unaffected reservation explicitly called out so the group isn't left guessing).
4. Invite questions only after 1–3 are delivered.
