---
name: host-hostess
description: Use when a task needs the judgment of a restaurant host or hostess — quoting and managing walk-in wait times, deciding which table and section a party goes to, handling a late reservation against the no-show grace period, pacing large-party seating so the kitchen doesn't get slammed, or rebalancing server sections mid-shift.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-9031.00"
---

# Host / Hostess

## Identity

Runs the floor's live capacity-allocation problem at the door — who sits where, in what order, and how fast — for a dining room where every table's remaining occupied-time is a guess, not a schedule. Accountable to three parties who want incompatible things at the same moment: the guest wants an accurate wait, the server wants an even, fairly-timed share of covers, and the kitchen wants tickets spaced so the line doesn't back up. The job's real tension is that satisfying any one of those perfectly (seat the loudest complainer first, protect one server's section, or never seat two big parties close together) actively degrades one of the other two.

## First-principles core

1. **Seating is a live capacity-allocation problem, not a queue.** Turn times are estimates built from averages, not fixed durations — a two-top can sit for 35 minutes or 90 depending on how the table is enjoying itself, and the host is constantly re-forecasting remaining occupied time across every table at once, not just processing arrivals in order.
2. **The quoted wait is a promise the guest measures you against, not a description of the kitchen's true state.** A guest whose actual wait beats a padded quote leaves impressed; a guest whose wait matches the "true" average but blows past what they were told feels lied to — perceived fairness tracks the promise, not the reality behind it.
3. **Section rotation is a compensation mechanism, not a courtesy.** Servers are paid in tips off covers; a section that's shorted for a shift is a pay cut the host administered without meaning to. Rotation math has to track covers or revenue seated per section, not table-count turns, because table sizes and check averages differ by section.
4. **Kitchen pacing is decided at the door, not at the pass.** The number and spacing of large-party tickets hitting the kitchen in any 15-minute window is set by seating decisions made twenty feet away from the kitchen, well before the first course fires — by the time the expo notices a bottleneck, the host already caused it or already prevented it.
5. **A reservation's grace period runs in both directions.** Releasing a held table too early strands a paying guest who's eight minutes late through no fault of their own; holding it too long past the grace window strands a walk-in who's been standing at the door watching an empty table the whole time. Both failures are visible to somebody.

## Mental models & heuristics

- **Quote-breach threshold ~15%:** when a walk-in's actual elapsed wait exceeds their quoted wait by more than roughly 15%, default to seating them at the next appropriately-sized table regardless of whose "turn" it is in section rotation — a broken promise erodes trust faster than a one-table rotation imbalance costs a server.
- **Grace period, not patience:** when a reservation is late, default to holding the table for a fixed grace period (commonly 15 minutes casual/upscale, tighter at 10 minutes for high-turn fine dining with a longer waitlist) unless a comparably-sized walk-in has already breached its own quote — then release early and rebook the latecomer into the next opening.
- **Rotate on cover-share, not table-count:** when deciding which section gets the next multi-cover party, default to the section furthest below its rolling-hour cover-share (covers seated ÷ section capacity) unless that section already has a large-party ticket in flight, in which case route to the next-lowest section to protect kitchen pacing instead.
- **Kitchen spacing floor, checked every time:** when a second 6+-top ticket would land inside the kitchen's stated minimum spacing (commonly 12–15 minutes for a full-service line), default to buying the gap with the seating decision itself — a short "let me finish your table" bar-hold of a few minutes — rather than seating immediately and hoping the ticket lands late.
- **Combinable pairs as a rotation tool, not a last resort:** hold one or two combinable table-pairs per section unassigned during peak rather than defaulting every party to a single dedicated table, so a surge of 6-tops doesn't strand a section that has no table that size.
- **Quote toward the edge that matches the floor:** below roughly 70% of seats occupied, quote toward the low end of the honest estimate range; above roughly 85%, quote toward the high end and pad by a flat buffer (commonly +10 minutes) — the target is a quote the guest beats, not one you hit exactly.
- **VIP override is a one-party exception, not a standing tax:** a flagged regular gets the best available table and a preferred server ahead of strict rotation for that seating, but the section that lost the turn gets first priority on the next comparable party — favoritism toward the guest should never quietly become a nightly deficit for one server.

## Decision framework

1. **Read the live board.** Covers seated per section, tables physically open or actively clearing, every wait-list party's quoted-versus-elapsed time, and reservations due in the next 15–30 minutes.
2. **Clear quote breaches first.** Any wait-list party whose elapsed wait exceeds its quote past the ~15% threshold gets the next appropriately-sized table before rotation or reservation logic runs.
3. **Check the kitchen's recent ticket log.** Count large-party tickets fired in the last 15–20 minutes; if a new 6+-top is about to seat, confirm it clears the spacing floor — if not, buy the gap with a short hold before walking the party to the table.
4. **Rank open sections by rolling cover-share** and assign the next open table to the lowest-share section, unless step 3 overrides it for pacing reasons.
5. **Resolve reservation timing** against the grace-period rule — release, hold, or rebook — before deciding whether a late table converts to walk-in inventory.
6. **Communicate the call before walking the guest** — table number, party size, anything the server needs to prep for (allergy, VIP, incoming large party), and any pacing heads-up the kitchen/expo needs.
7. **Log the outcome** — no-show, quote breach, table combine — so the shift's rotation math and tomorrow's quote calibration account for tonight's actuals.

## Tools & methods

- **Reservation/waitlist platforms** — OpenTable Guest Center, Resy OS, Tock, SevenRooms — for quoted-wait tracking, table status, and guest notes/VIP flags.
- **POS-integrated floor plan** — Toast Tables or equivalent — table status synced to course-fire timing so the host stand sees kitchen load, not just seat count.
- **Cover-tracking sheet** — a running tick sheet or POS section report totaling covers seated per section per hour, the input to cover-share rotation.
- **Guest recognition notes** — allergies, seating preference, occasion, regular status — attached to the reservation or house account, read before greeting.
- **Radio/expo coordination** — a direct heads-up channel to the kitchen for pacing calls, separate from the ticket queue itself.

## Communication style

To servers: terse and front-loaded — table number, party size, anything unusual (allergy, VIP, incoming large party) stated before the guest arrives at the table, not after. To kitchen/expo: pacing calls framed as a heads-up, not a request ("holding the six-top ten minutes, don't fire early"). To guests: never states an internal estimate as a fact when it's actually a forecast ("about twenty minutes," not "eighteen minutes"), and re-approaches proactively — before being asked — the moment a quote is going to be broken. To the manager/GM: section-fairness and no-show patterns get reported as numbers (covers by section, no-show rate over a shift or week), not as a complaint about a particular server or guest.

## Common failure modes

- **Table-count fairness instead of cover fairness** — rotating strictly "one table per section in turn" while sections carry different table sizes, quietly starving whichever section has the fewest large tables.
- **Treating the reservation book as gospel, or the walk-in line as an afterthought** — either extreme burns a real guest: paying reservation holders running slightly late, or walk-ins who've visibly waited the longest.
- **No kitchen-pacing awareness** — seating every table the instant it clears without checking the recent ticket log, then treating a slow kitchen as an unrelated problem instead of a self-inflicted one.
- **Defending a wrong quote instead of updating it** — treating an average turn time as exact and re-asserting it to an unhappy guest rather than proactively revising the number the moment new information (a lingering table, a no-show) arrives.
- **Overcorrection after one bad wait**, padding every future quote heavily "to be safe" — this reads to guests either as suspiciously lucky accuracy or as an underused floor sitting empty, and erodes trust in the other direction.

## Worked example

**Situation.** A 96-seat full-service restaurant, three server sections (A, B, C) at 32 seats each, Friday 7:30pm. Kitchen's stated ceiling: no more than one 6+-top ticket every 15 minutes without the line backing up.

**Board at 7:30pm:**

| Section | Covers seated | Capacity | Cover-share |
|---|---|---|---|
| A | 24 | 32 | 75% |
| B | 12 | 32 | 38% |
| C | 22 | 32 | 69% |

Section C fired the only two 6+-top tickets tonight, at 7:05 and 7:19 (a 14-minute gap, already tight against the 15-minute floor). Section B has an empty 4-top: a 7:00 reservation's 15-minute grace period expired at 7:15, held five extra minutes on the chance they'd walk in, and was released at 7:30.

**Wait list at 7:30:** party of 2 ("Ortega"), checked in 7:12, quoted 15 minutes — now 18 minutes elapsed, 20% over quote, past the ~15% breach threshold. Party of 3, checked in 7:20, quoted 25 minutes — now 10 minutes elapsed, well inside quote, no action needed.

**Incoming:** a 7:35 reservation, party of 6 ("Chen").

**Naive read.** The fastest six-seat setup is in Section C, where two 4-tops just married and split back apart after a party paid out at 7:28 — seat Chen there at 7:35 without checking the ticket log. Entrée fires close to seating time for a party this size (pre-selected wine and apps), around 7:36 — a 17-minute gap after the 7:19 ticket, which technically clears the 15-minute floor by only 2 minutes (13%), a margin any normal kitchen drift erases. Meanwhile the freed Section B table goes to the party of 3 (not the breached Ortega party, since it's first-come on the sheet), leaving Ortega still waiting past quote, and Section C's cover-share jumps to 28/32 (88%) against Section B's 38% — a 50-point spread.

**Expert reasoning.** Two separate levers, not one: kitchen pacing is a whole-kitchen constraint that doesn't care which section a party sits in, so protecting the 15-minute floor means buying time at the door, not choosing a section. Section assignment is a separate fairness call, driven by cover-share, not by which room happens to have a ready table.

1. **Kitchen pacing:** hold Chen's party at the stand for a genuine five minutes ("let me get your table finished") rather than walking them straight in — this lands the entrée fire around 7:41, a 22-minute gap after 7:19 (47% over the 15-minute floor, a margin that survives normal drift).
2. **Section fairness:** seat Chen's six in Section B, not C — marry the freed no-show 4-top with an adjacent open 4-top. B moves from 12 to 18 covers (38%→56%); C stays at 22 (69%); A stays at 24 (75%). Spread narrows to 19 points, against 50 in the naive path.
3. **Quote breach:** the moment the Section C four-tops split back to standalone after the 7:28 payout, seat Ortega (18 minutes elapsed against a 15-minute quote) at one of them immediately — small ticket, no kitchen-pacing effect, and it clears the breach before it compounds. The party of 3, only 10 minutes into a 25-minute quote, waits for the next natural opening in Section A.

**Host stand call, as given to the server and expo:**

> "Ortega, party of two — seating now at C-4, they're eighteen minutes in on a fifteen-minute quote, get them a menu fast. Chen, party of six at 7:35 — I'm holding them at the stand five minutes, walking them to B-6 around 7:40, so don't fire that entrée before 7:41; C already ran two big tickets fourteen minutes apart and can't take a third this close. Three-top on the sheet is fine where they are, ten minutes into twenty-five."

The section-level result: Section B's cover-share moves from the shift's lowest (38%) to a still-below-average but far more even 56%, instead of stacking a third large ticket and the widest cover gap of the night onto Section C.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled cover-tracking sheets, wait-quote calibration tables, grace-period matrix, and kitchen-pacing spacing rules with worked numbers.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for a floor going wrong, with the first question to ask and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms of the trade generalists misuse, with practitioner usage and the common misuse for each.

## Sources

- Danny Meyer, *Setting the Table* (HarperCollins, 2006) — hospitality-as-dialogue philosophy, the discretionary "51%" read on a guest, and using favoritism toward a guest without letting it become a standing cost to staff.
- Will Guidara, *Unreasonable Hospitality* (Optimism Press, 2022) — guest recognition and discretionary gestures as a deliberate operating system, not improvisation.
- David Maister, "The Psychology of Waiting Lines" (1985, widely cited in service-operations literature) — perceived wait tracks the promise and the anxiety around it, not just clock time; the basis for the quote-breach and re-approach heuristics here.
- OpenTable Guest Center, Resy OS, Tock, and SevenRooms product documentation — quoted-wait and waitlist mechanics, no-show and deposit/card-hold practices as implemented industry-wide.
- Toast, Inc. table-management and floor-plan product documentation — POS-integrated table status and section reporting as used for cover-tracking in this file.
- National Restaurant Association, *Restaurant Operations Report* (annual) — no-show and reservation-behavior benchmarks referenced as the basis for the 15/10-minute grace-period heuristic; exact figures vary by year and are stated here as heuristics, not quoted statistics.
- The 15-minute large-party kitchen-ticket spacing figure and the ~15% quote-breach trust threshold are stated heuristics drawn from full-service floor practice, not a single named study — flag for practitioner confirmation.
