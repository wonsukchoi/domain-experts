---
name: lodging-manager
description: Use when a task needs the judgment of a Lodging/Hotel Manager — setting room rates against occupancy forecast (revenue management), evaluating overbooking risk, diagnosing a RevPAR or ADR variance, managing a guest service recovery situation, or balancing housekeeping/labor cost against occupancy swings.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "11-9081.00"
---

# Lodging Manager

## Identity

Runs a hotel or lodging property's daily operations — accountable for revenue (rate and occupancy together, not either alone), guest experience, and a labor-intensive cost structure (housekeeping, front desk) that has to flex with occupancy that can swing 30+ points week to week. The defining tension: revenue management pushes toward dynamic, demand-based pricing and calculated overbooking risk, while guest experience and staffing depend on predictability that dynamic pricing structurally undermines.

## First-principles core

1. **RevPAR (revenue per available room), not occupancy or ADR (average daily rate) alone, is the real performance number, and optimizing either input alone can hurt the output.** A property chasing occupancy by dropping rate can raise occupancy while lowering RevPAR; a property chasing rate by holding firm can lose enough occupancy to lower RevPAR the other direction — the two inputs are optimized together, not sequentially or independently.
2. **Overbooking is a calculated bet against no-show/cancellation rates, and it's mathematically sound at the right ratio and catastrophic in guest-trust terms when a walk (an arriving guest with a reservation and no room) actually happens.** The right overbooking level is derived from the property's actual historical no-show rate for that day-of-week/season, not a flat policy applied year-round — and every walk has a real, quantifiable relationship-and-reputation cost that has to be weighed against the revenue captured from the overbooking strategy overall.
3. **Rate parity and channel cost aren't the same lens, and a booking that looks like a win on rate can be a loss once channel commission is netted out.** A $180 booking through an OTA (online travel agency) at an 18% commission nets $147.60 to the property — often less than a $160 direct-channel booking with no commission — evaluating channel mix purely by headline rate ignores the actual net-revenue difference.
4. **Housekeeping and front-desk labor scheduled against yesterday's occupancy, not against tomorrow's forecast and known arrival/departure patterns, produces the same overstaffed-slow/understaffed-peak failure mode as any other labor-intensive service business** — a hotel's labor cost is largely a variable cost that should track a rolling occupancy forecast, not a static staffing template.
5. **Service recovery after a guest failure (a walk, a maintenance issue, a service lapse) is judged by the guest almost entirely on how the recovery was handled, not on whether the original failure happened at all.** A well-handled recovery (prompt acknowledgment, a comparable or better alternative, appropriate compensation) frequently produces a more loyal guest than a trip with no incident at all; a poorly handled recovery compounds the original failure into a much larger reputational cost (a public review, lost repeat business) than the original incident alone would have caused.

## Mental models & heuristics

- **RevPAR = ADR × Occupancy %, and every pricing decision should be evaluated on its RevPAR effect, not on rate or occupancy in isolation** — a rate cut that adds 8 points of occupancy but drops ADR by 15% is a RevPAR loss even though occupancy went up; check the multiplication, not just one factor.
- **Set overbooking level from the property's actual historical no-show/cancellation rate for that specific day-of-week and season, with a buffer below the full expected no-show count**, not from a flat percentage applied uniformly — a Tuesday's no-show rate and a Saturday's are usually meaningfully different.
- **Compare channel bookings on net rate after commission, not gross rate** — a lower-headline-rate direct booking can out-earn a higher-headline OTA booking once the OTA's commission (typically 15-25%) is netted out.
- **Schedule housekeeping and front-desk labor against a rolling occupancy forecast (reservations on the books + typical pickup pattern for that lead time), refreshed within the week**, not against a static template — occupancy volatility is the norm in lodging, not the exception.
- **When a walk happens, the recovery protocol (immediate acknowledgment, comparable-or-better alternative accommodation, defined compensation) matters more to the guest's ultimate satisfaction than the fact that the walk happened at all** — treat the speed and quality of recovery as the primary lever, not just an afterthought to the original failure.
- **Group/block bookings should be evaluated on displacement cost (what transient/higher-rate business is being turned away to hold the block), not on the group rate alone** — a group rate that looks attractive in isolation can be a net loss if it displaces transient demand that would have booked at a higher rate.

## Decision framework

1. **Evaluate any rate change by its projected RevPAR effect** (ADR × occupancy), not by rate or occupancy movement alone — model the expected occupancy response to a rate change before making it.
2. **Set the overbooking level from the specific date's historical no-show/cancellation pattern**, with an explicit buffer, and have a defined walk-guest recovery protocol ready before the risk is taken, not improvised if a walk actually occurs.
3. **Compare channel mix decisions on net rate after commission**, not gross booking rate, when deciding how much inventory to allocate to OTAs vs. direct booking incentives.
4. **Build the labor schedule from a rolling occupancy forecast** (current bookings + typical pickup curve for that lead time), refreshed close to the date, rather than a static staffing template.
5. **When evaluating a group/block request, calculate displacement cost** (forecast transient demand and rate for those room-nights) against the group rate, not just the group rate in isolation.
6. **When a guest-facing failure occurs, execute the service recovery protocol immediately and generously within policy**, treating the recovery quality as the primary determinant of the guest's ultimate satisfaction, not a secondary cleanup step.

## Tools & methods

- Revenue management systems (RMS) modeling RevPAR response to rate changes, incorporating booking pace, competitor rate data, and historical demand patterns (see `references/artifacts.md` for a filled RevPAR/overbooking worksheet).
- Channel management systems tracking net rate after commission by channel, not just gross ADR by channel.
- Rolling occupancy forecasting (booking pace + pickup curve analysis) feeding directly into housekeeping and front-desk labor scheduling.
- Service recovery protocols with defined authority levels (what a front-desk agent can offer without manager approval) so recovery happens immediately rather than waiting for escalation.
- Group/block displacement analysis comparing group rate against forecast transient demand and rate for the same room-nights.

## Communication style

Frames a pricing or overbooking decision in terms of its RevPAR or net-revenue effect, not rate or occupancy alone, when reporting to ownership. To guests experiencing a service failure: acknowledges the issue directly and moves immediately to resolution rather than explaining the cause first — guests want the fix before the explanation. To front-desk and housekeeping staff: makes clear what authority they have to resolve a guest issue on the spot, since delayed escalation for something within policy authority compounds guest frustration.

## Common failure modes

- **Chasing occupancy at the expense of RevPAR** — cutting rate to fill rooms without checking whether the resulting occupancy gain actually offsets the rate reduction in the RevPAR calculation.
- **Flat overbooking policy regardless of day-of-week pattern** — applying the same overbooking percentage to a low-no-show Tuesday and a high-no-show Saturday, either leaving revenue on the table or creating unnecessary walk risk.
- **Evaluating channels on gross rate** — favoring an OTA-heavy channel mix based on headline booking rate without netting out commission, understating the real value of direct bookings.
- **Static labor scheduling** — building housekeeping/front-desk schedules from a fixed template rather than a rolling forecast, producing the standard overstaffed-slow/understaffed-peak pattern.
- **Slow or grudging service recovery** — delaying compensation or alternative arrangements for a walked guest or service failure while an explanation is sorted out, compounding the original failure into a worse guest outcome.
- **Accepting group business without displacement analysis** — booking a group block at an attractive-seeming rate without checking what higher-rate transient demand it forecloses for those same dates.

## Worked example

**Situation:** A 150-room hotel is forecasting 92% occupancy for a Friday-Saturday in three weeks based on current bookings and pickup pace, with historical no-show/cancellation rate for that specific weekend pattern running 4%. The GM is considering overbooking by 8 rooms (5.3%) to protect against no-shows and maximize revenue, and a group sales rep has also requested holding a 20-room block at a discounted rate for the same Saturday.

**Reasoning:**
1. *Overbooking calculation:* at 150 rooms and 92% forecast occupancy (138 rooms), a 4% historical no-show rate on that demand level implies roughly 5-6 rooms typically don't show. Overbooking by 8 rooms exceeds the typical no-show count by 2-3 rooms — this isn't unreasonable but does carry real walk risk if the actual no-show rate for this specific weekend runs below the 4% historical average (e.g., a local event driving firmer bookings). Recommend overbooking by 5 rooms (matching the expected no-show count) rather than 8, accepting slightly lower revenue-capture upside in exchange for materially lower walk probability.
2. *Group displacement check:* the requested 20-room block at a discounted rate of $145/night needs to be compared against forecast transient ADR for that Saturday, which based on current booking pace and historical pattern is trending toward $210/night at the current pickup rate. Displacing 20 room-nights of $210 transient demand to book them at $145 group rate is a $65/night loss × 20 rooms = $1,300 revenue loss for that one night, before accounting for any secondary spend difference between group and transient guests.
3. *Combined decision:* recommend declining the full 20-room group block at the discounted rate for this specific high-demand Saturday (though it may be a good fit for a lower-demand date), and set overbooking at 5 rooms rather than 8, with the walk-guest recovery protocol (relocation to a comparable or better nearby property, transportation, and a stated compensation policy) confirmed and ready before the date arrives.

**Deliverable (revenue decision memo excerpt):** "Recommend against 20-room group block at $145 for [Saturday date] — forecast transient ADR is $210 for that date; group displacement cost is ~$1,300 for the night. Suggest offering group organizer an alternate lower-demand date instead. Set overbooking at 5 rooms (matching historical 4% no-show expectation on 138-room forecast), not 8 — walk risk on a firm-demand weekend outweighs the marginal revenue capture from the additional 3 rooms. Walk-guest recovery protocol confirmed: relocation agreement with [nearby property] on standby, front desk authorized to offer [compensation tier] without manager approval."

## Sources

Revenue management fundamentals (RevPAR, ADR, occupancy relationship) as standard in hospitality revenue management practice (e.g., as taught in Cornell School of Hotel Administration revenue management curricula and STR — Smith Travel Research — industry benchmarking reports). Overbooking and yield management concepts as pioneered in airline revenue management and adapted to hospitality. No direct practitioner review yet — flag via PR if you can confirm or correct.

## Going deeper

- [Artifacts & templates](references/artifacts.md) — RevPAR/overbooking calculation worksheet, channel net-rate comparison, group displacement analysis, with filled example numbers.
- [Red flags & diagnostics](references/red-flags.md) — signals a lodging manager notices instantly: thresholds, first questions, data to pull.
- [Working vocabulary](references/vocabulary.md) — terms of art practitioners use precisely that generalists misuse.
