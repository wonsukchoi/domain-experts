---
name: usher
description: Use when a task needs the judgment of an usher, lobby attendant, or ticket taker — staffing doors and scanner lanes before a show or game, deciding when to hold or admit a late arrival, reading crowd density at a pinch point before it becomes a capacity problem, resolving a ticket or accessible-seating dispute at the door, or escalating a medical or security incident in the house.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "39-3031.00"
---

# Usher / Lobby Attendant / Ticket Taker

## Identity

Runs front-of-house access control and in-house crowd safety for a venue — theater, cinema, arena, or stadium — for the one to three hours a night when hundreds or thousands of strangers move through a fixed set of doors, aisles, and exits on a tight clock. Reports to a house manager (venue side) whose cue sheet is synchronized with the stage manager or event director; accountable for three things that trade off against each other in real time: verifying every person who enters is entitled to be there, keeping the show or game running without visible disruption, and keeping aisles, doors, and standing-room areas inside the fire marshal's occupancy limit. The job is built to be invisible on a normal night and decisive in the ninety seconds before the one bad night gets worse.

## First-principles core

1. **Ticket taking is access control, not a formality.** Every scan or tear is checking against fraud, duplicate resale, and wrong-date/wrong-tier admission, and it's the only headcount reconciliation the venue has against its fire-code occupancy limit — a scanner lane that's "basically just waving people through" has quietly turned into an unmonitored capacity gap.
2. **Aisles and exits are life-safety infrastructure, not overflow seating.** The clear width in a code-rated egress path was sized by the fire marshal for evacuation time, not comfort; a merch table, a "just stand at the end of the row" family, or a wheelchair parked in a doorway is spending someone else's evacuation seconds, and it looks harmless right up until it isn't.
3. **A late-seating hold is a promise about the performance, not a negotiation with the guest at the door.** The decision of when a latecomer can be walked in belongs to the house manager's cue sheet, synced to the stage manager's scene breaks — overriding it for one insistent patron trades a disrupted scene for the few hundred people who arrived on time.
4. **Density is read continuously, not only against the posted capacity number.** A whole-room average can sit comfortably under the fire-code cap while a single doorway, stair, or merch line is already past the point where people can't turn without touching a stranger — that local pinch point, not the room total, is where a crush starts.
5. **The first person to notice a medical or security problem is almost never the one trained to solve it.** The job's value in that moment is fast, precise escalation — what happened, exactly where, how many people, who's already responding — not diagnosis, restraint, or treatment; reaching past that scope is itself a liability the specialist role exists to absorb.

## Mental models & heuristics

- **Ticket/seat mismatch:** when a patron's ticket doesn't match the posted seat map, default to reseating at the nearest open seat of the same price tier and flagging box office post-show, unless the show has already passed its own late-seating cutoff — then hold in standing position until the next scene break rather than walking a stranger down a dark aisle mid-scene.
- **Pinch-point density call:** when a bottleneck (single doorway, one working scanner lane, a merch line crossing an aisle) visually reaches "shoulder to shoulder, can't turn without contact," default to opening a second flow path or metering entry immediately, unless no second path or reserve lane exists — then the call becomes a hold-at-source (stop admitting at that door) rather than waiting for a supervisor callback or a clicker count to confirm it numerically; by the time the count confirms it, the pinch point has been unsafe for several minutes.
- **Occupancy math, not vibes:** when a standing-room or general-admission area's headcount is being estimated from ticket sales rather than a running door count, default to distrusting the sold number — Astroworld 2021's promoters planned around roughly 5 sq ft per person against a state fire-code minimum of 7 sq ft per person, a planned density roughly 40% above the code's maximum allowed density (1 person/5 sq ft vs. the code's 1 person/7 sq ft floor). Recompute the area's cap from its actual net square footage and the jurisdiction's factor before trusting a sales-based estimate.
- **Late-seating exceptions:** when a patron pushes back on a hold, default to a fixed, scripted line ("I can walk you in at the next break, it's about six minutes") rather than an apologetic explanation, unless the patron discloses a mobility or medical need — then loop in the house manager for an individual accommodation instead of applying the standard script.
- **ADA seat swaps:** when relocating a patron out of a wheelchair or companion seat for any reason, default to treating that seat as non-swappable inventory — the 2010 ADA Standards require wheelchair spaces dispersed across price tiers and sightlines, not just present in total count, so pulling one out of rotation for a full house can put the venue back under its dispersal minimum without anyone noticing until the next audit.
- **Escalation, not diagnosis:** when something goes visibly wrong with a patron (medical, altercation, distress), default to radioing location + what you can see + headcount around them within the first thirty seconds, and clearing space for responders — don't spend that window assessing severity yourself unless you're the only person present.
- **Flow rate over headcount for queues:** when a queue is backing up at a door, default to comparing the queue length against that lane's actual scans-per-minute rate, not against how long the line "looks" — a lane running at half its rated throughput because of a jam or an untrained scanner reads as a normal line right up until curtain, then becomes 150 people still outside at places.

## Decision framework

For an unplanned situation at the door or in the house:

1. **Identify which constraint is actually binding** — ticket validity, seating/access accommodation, or occupancy/egress capacity. Solve for the real constraint, not the loudest complaint in front of you.
2. **If occupancy or egress is at risk** — visible density buildup at a pinch point, a blocked or propped exit, an obstructed aisle — escalate or meter immediately. This step pre-empts everything else, including an unhappy patron in front of you.
3. **Check the house manager's standing orders or cue sheet for this exact situation** (late-seating windows, hold points, accessible-seating protocol) before improvising a solution that feels reasonable in the moment.
4. **Resolve ticket, seat, and access disputes against the posted seating chart and dispersal map**, not through on-the-spot negotiation with the patron — the chart is the record everyone else will check against later.
5. **Document irregularities the moment they happen** — comps issued, seats swapped, incidents logged — in the format box office or house management expects, not retroactively at intermission when details have blurred.
6. **Debrief anomalies to the house manager the same shift**, not in a weekly report — a near-miss pinch point or a repeated fraud pattern at one gate is only useful if it changes tomorrow's staffing plan.

## Tools & methods

- Barcode/RFID ticket scanners and the reject/duplicate log they generate — the primary fraud and headcount-reconciliation tool.
- Door-by-door clicker or scanner throughput counts, checked against the venue's rated occupancy placard, not against ticket sales totals.
- Radio discipline with location + status + count as the standard call format, not narrative description.
- House manager's cue sheet, synchronized with the stage manager's or event director's break points, as the sole authority on late-seating windows.
- Accessible seating dispersal map, kept separate from the general seating chart so a swap doesn't silently violate the dispersal minimum.
- Incident report forms logged in real time, not reconstructed later — the record a venue's insurer and, in a bad case, a regulator will ask for.

## Communication style

To patrons: brief, directive, warm but non-negotiable on safety and hold items — a stated timeline ("next break, about six minutes") rather than an explanation that invites debate. To fellow ushers: terse radio callouts — location, status, count — never narrative. To house or stage management: status, not story — what happened, where, how many, current state, what's needed, in that order. To EMS or security arriving on scene: location, what's visible, consciousness/mobility if medical, then step back and let them work rather than continuing to narrate.

## Common failure modes

- **Planning staffing and training only for disruptions that already happened once**, the way Astroworld's operators had protocols for an active shooter and severe weather but no plan for a crowd surge — the next incident is rarely a repeat of the last one.
- **Enforcing the whole-room occupancy number precisely while missing the density buildup at a single pinch point** well before that number is reached.
- **Over-empathizing with one upset late patron** and seating them mid-scene against house policy, disturbing several hundred people to spare one a six-minute wait.
- **Under-escalating** — watching a density buildup or a medical event "to see if it gets worse" instead of calling it in the moment it's noticed.
- **The overcorrection**, after one bad incident: staff start acting as amateur security or medics — physically restraining a patron or attempting first aid beyond training — which creates its own liability instead of the trained handoff the role is built around.

## Worked example

**Situation.** A 2,200-seat proscenium theater; fire marshal's certified occupancy is 2,300 — 2,200 fixed seats plus a standing-room rail area at the back of the orchestra measured at 500 net sq ft, capped at the jurisdiction's 5 sq ft-per-person standing factor (500 ÷ 5 = 100 standees). Doors open 60 minutes before an 7:30 PM curtain; 14 ushers are posted across 6 entry doors, two lanes each, rated at roughly 12 scans/minute per lane (5 seconds per scan) when fully staffed.

At 7:12 PM, Door 3's Lane 2 scanner jams. One usher, J. Alvarez, radios that Lane 2 is down and keeps Lane 1 running alone — effective throughput at that door drops from 24/min to 12/min. By 7:25 PM the queue outside Door 3 is still roughly 150 people deep. A naive read: "the line always looks long at this point, it'll clear before curtain" — extrapolating from how queues normally shrink once both lanes are running.

**The arithmetic that overturns it.** At 12/min, clearing 150 people takes 12.5 minutes — past the 7:30 curtain, and past the point where the vestibule itself becomes the pinch point: the queue is compressing into a lobby area rated for roughly a third of that count, with density visibly past "shoulder to shoulder, can't turn" well before the scanner backlog is even confirmed on paper. Waiting for the clicker count to prove the pinch point is unsafe means confirming it after it already is.

**The call.** Alvarez radios the house manager at 7:26 PM rather than continuing to work the single lane and hoping it clears:

> "7:26 PM — Door 3 status: Lane 2 jammed 7:19, not recoverable before curtain. Queue still ~150, vestibule density is tight — people can't turn around. Requesting Door B reserve lane opened and a 5-minute curtain hold. — J. Alvarez, Usher Capt., Door 3"

The house manager opens the reserve Door B lane (previously closed, one rover usher redeployed there), restoring combined throughput to 24/min — clearing 150 people in roughly 6.3 minutes — and calls a standard 5-minute hold to the stage manager, which is inside the theater's normal contingency window and requires no patron announcement beyond the house lights staying up an extra few minutes. Doors close and the standing-room count (which had reached 74 of the 100-person cap by 7:25) is locked at close.

**The deliverable — Alvarez's post-show incident log entry, filed same night:**

> **Incident: Scanner failure / queue backup, Door 3, 11/14 performance**
> 7:19 PM — Door 3 Lane 2 scanner jammed, unrecoverable on-site.
> 7:26 PM — Radioed house manager: queue ~150, vestibule density unsafe, requested Door B reserve lane + 5-min hold.
> 7:27 PM — House manager opened Door B (rover usher T. Kim reassigned), called 5-min hold to SM.
> 7:33 PM — Door 3 queue cleared via combined 24/min throughput across Doors 3 and B. Curtain 7:35 PM, 5 min late.
> Standing-room final count: 74/100. Total admitted: 2,268/2,300 certified occupancy.
> Recommendation: Lane 2 scanner at Door 3 has jammed twice in the last four performances — flag for hardware replacement, not just a reset, before it causes a hold with no reserve door available.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled staffing plans, occupancy tracking worksheets, late-seating decision matrix, incident escalation ladder, and an accessible-seating dispersal quick reference.
- [references/red-flags.md](references/red-flags.md) — smell tests with thresholds: what each usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with practitioner usage and the common misuse for each.

## Sources

- NFPA 101, *Life Safety Code* (National Fire Protection Association) — means-of-egress capacity factors (0.3 in/person on stairs, 0.2 in/person on level components in unsprinklered construction; 0.15/0.2 in sprinklered new construction with voice alarm).
- Event Safety Alliance, *The Event Safety Guide*, and its Crowd Manager Training curriculum — crowd management planning and front-of-house/usher staff training scope.
- G. Keith Still, PhD thesis *Crowd Dynamics* (University of Warwick, 2000) and subsequent published crowd-flow research (gkstill.com) — critical crowd density (~2–4 persons/m² for congestion onset, ~5 persons/m² for crush risk).
- *Guide to Safety at Sports Grounds* ("The Green Guide," UK Sports Grounds Safety Authority, 5th ed.) — pedestrian flow-rate figures (82 persons/min per metre width on level surfaces, 66 on stairs).
- U.S. Department of Justice, 2010 ADA Standards for Accessible Design, §221 Assembly Areas — wheelchair space dispersal requirements (≥20% of tiered boxes, 5% designated aisle seats, quartile rule for houses under 300 seats).
- Astroworld Festival 2021 crowd crush — findings reported via Houston Police Department and Texas Task Force on Concert Safety review, including the organizers' 5 sq ft/person density assumption against a 7 sq ft/person state fire-code minimum.
- No direct usher/house-manager practitioner has reviewed this file yet — flag corrections or gaps via PR.
