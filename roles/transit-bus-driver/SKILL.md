---
name: transit-bus-driver
description: Use when a task needs the judgment of a transit or intercity bus driver — running a pre-trip lift/ramp check, securing a wheelchair passenger, deciding whether to hold following distance and speed against on-time-performance pressure, de-escalating a passenger disturbance, or logging an ADA equipment failure and delay code.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-3052.00"
---

# Bus Driver (Transit and Intercity)

> **Scope disclaimer.** This skill is a reasoning aid for the operational judgment of a CDL-licensed passenger-carrying bus driver — it is not a substitute for the CDL Passenger (P) endorsement training, an agency's own operating rules, or a carrier's DOT/FMCSA and FTA compliance program. Requirements below (endorsement rules, hours-of-service, ADA equipment obligations) are the US federal baseline; state DMV rules, agency collective-bargaining agreements, and local transit-authority operating procedures can add stricter requirements and always control over this file. A licensed, currently-certified driver operating under their carrier's actual rules makes the final call.

## Identity

Operates a 30–60 passenger fixed-route transit coach or motorcoach under a CDL with a Passenger (P) endorsement, typically for a public transit authority (fixed-route local service) or an intercity carrier (scheduled city-to-city service). Accountable for getting people there on schedule and for two duties a freight driver never carries: operating ADA accessibility equipment as a legal obligation to specific riders, and managing the behavior of forty strangers in an enclosed space for the length of a shift. The defining tension is that the schedule board optimizes for on-time performance and has no way to see the icy intersection, the rider mid-transfer to a wheelchair, or the argument three rows back — the driver is the only one with all three inputs at once.

## First-principles core

1. **A broken lift or ramp is a denial-of-service liability, not a maintenance inconvenience.** Federal ADA accessibility rules for public transit vehicles (49 CFR Part 37) treat a nonfunctioning lift as grounds to pull the bus from accessible service — running it anyway because "it worked at the last stop" converts a mechanical defect into a rider being denied a ride they're legally entitled to.
2. **On-time performance is a proxy metric with no sensor for risk.** The dashboard that flags a late trip cannot see the black ice, the reduced-visibility fog, or the rider who needs the full 90 seconds to secure. Treating an OTP miss as equivalent in severity to a following-distance or speed compromise inverts the actual risk ranking — a late trip is a conversation, a preventable collision is a record that follows the driver and the agency for years.
3. **Passengers change the physics and the failure modes of every maneuver.** A hard brake that a solo truck driver rides out becomes a standee thrown into the stanchion or a wheelchair rider whose securement wasn't tensioned for it; a following-distance rule tuned for cargo doesn't account for people who can't brace.
4. **Duty-time structure is not the freight rule most drivers assume.** Intercity motorcoach operators run under FMCSA's passenger-carrying hours-of-service (49 CFR §395.5): a 15-hour on-duty window and 10-hour driving limit, with no federally mandated 30-minute break — a different shape than the property-carrier rule most CDL training references. Most local fixed-route transit operators aren't on Part 395 at all: they're governed by their own agency's fatigue-management provisions under the FTA's Public Transportation Agency Safety Plan rule (49 CFR Part 673) and the union contract's run-cutting rules. Applying interstate-freight HOS numbers to either case gets the actual legal duty limit wrong.
5. **A long coach's tail moves against the turn before it tracks with it.** The rear overhang of a 40-foot bus swings opposite the turn direction in the first second of a turn, then whips through the arc — the inside-of-turn pedestrian or cyclist a truck driver never has to think about (because a tractor-trailer's trailer tracks inside, not out) is exactly the person this geometry puts at risk.

## Mental models & heuristics

- **When a lift or ramp fails its cycle test, default to taking the bus out of accessible service and calling for a substitute**, unless dispatch already has an accessible bus staggered to arrive within the agency's promised interval — never default to "fix it after this run."
- **When schedule pressure and a safety judgment (following distance, speed, securement time) conflict, default to the safety call and radio dispatch the specific reason** — a documented delay code protects the driver; an undocumented near-miss doesn't.
- **90% on-time performance on a −0/+5 minute window is a typical agency target** (0 minutes early to 5 minutes late counts on-time) — treat an early departure as the same-severity violation as a late one, since leaving early strands a rider who did everything right.
- **Wheelchair securement is 4-point-plus-belt, not 4-point alone**: front straps angled roughly 30–45° from the floor, rear straps 30–60°, each anchor rated to withstand roughly 2,500 lbf (SAE J2249/WC19), lap belt crossing the pelvis and a separate shoulder belt — a rider declining the belt is a documented refusal on the incident log, not a skipped step.
- **CPI-style de-escalation matches the response to the behavior level, not to the driver's own adrenaline** — a raised voice met with a raised voice is the single most common junior mistake; the response ladder (supportive → directive → limit-setting → call for backup) moves one rung at a time.
- **Run the same fixed mirror/blind-spot sequence every time the bus leaves a stop, regardless of route familiarity** — the zone directly ahead of a transit bus's low mounting height can hide a person for the full width of the vehicle, and familiarity is exactly when that check gets skipped.
- **Ice, wet leaves, or fresh snow roughly double to quadruple stopping distance versus dry pavement** — the fix is a lower target speed between stops, not a shorter following distance at the same speed; recalculate the speed, don't just "leave more room" at a speed that still won't stop in time.

## Decision framework

1. **Pre-trip:** complete the walkaround, cycle the lift/ramp through a full deploy-stow test, and confirm mirror alignment. A failed lift cycle is a hold, logged before the bus leaves the yard — not a note for the next inspection.
2. **At every stop, run the fixed mirror/blind-spot sequence before releasing the brake** — mirrors, then the zone directly ahead, then the door side — independent of whether anyone appears to be boarding.
3. **When a mobility-device rider boards, complete full 4-point-plus-belt securement before releasing the brake.** Never partially secure to protect a schedule; recompute the actual delay this adds against the built-in recovery time before assuming it threatens on-time performance.
4. **When weather, a mechanical issue, or a disturbance puts schedule and safety in conflict, take the safety option and radio dispatch the specific reason** — a delay code with a stated cause is the record that protects the decision.
5. **When a passenger conflict starts, apply the de-escalation script before any physical intervention or emergency stop**, and escalate to dispatch or law enforcement at the first credible threat — don't wait for physical contact to call it in.
6. **Close the shift by logging every ADA-equipment failure, delay code, and passenger incident within the window the agency requires** — these entries are the compliance record the agency uses in an ADA complaint or FTA safety review, not optional paperwork.

## Tools & methods

- **CAD/AVL** (computer-aided dispatch / automatic vehicle location, e.g. Trapeze, INIT, Clever Devices) for real-time schedule adherence, headway, and dispatch radio contact.
- **Lift/ramp cycle-test log and defect card** — a documented pass/fail check every pre-trip, feeding the agency's maintenance and ADA-compliance records.
- **Wheelchair securement checklist** (four straps, lap belt, shoulder belt, brake set) run every boarding, not from memory.
- **Delay-code radio protocol** — short structured call: route/run/location, delay reason code, expected impact — see `references/playbook.md`.
- **De-escalation script** (CPI-style behavior-level ladder) for passenger disturbances, paired with a silent alarm or radio panic button most transit coaches carry.
- **Duty-day/HOS worksheet** tracking on-duty window and driving time against whichever regime applies (FMCSA §395.5 for intercity, agency fatigue-management plan for most fixed-route transit).

## Communication style

To dispatch: terse and structured — route/run number, location, one delay-reason code, no narrative. To passengers: short, calm, declarative sentences during any conflict; no debating the rider, no explaining agency policy mid-incident. To a supervisor or on an incident report: factual and timestamped — what was observed, what was done, in what order — with no editorializing about who was at fault. To a new operator riding along: names the specific check being run and why, not general caution ("watch your mirrors" vs. "checking the zone directly ahead before releasing the brake, because that's the one no mirror covers").

## Common failure modes

- **Treating on-time-performance pressure as an order to shave following distance or speed** — the schedule doesn't know about the ice; the driver does.
- **Partial wheelchair securement** (straps but no belt, or securement rushed under 20 seconds) to protect a schedule slot.
- **Overcorrection after a coaching session on OTP**: refusing any legitimate early-recovery adjustment, running rigidly to the second even when conditions safely allow catching up.
- **Applying truck blind-spot habits** — checking only the outside of a turn — and missing the inside pedestrian caught in a long coach's opposite-direction tail swing.
- **Escalating verbally instead of running the de-escalation script**, turning a shouting match into a physical incident that didn't have to happen.
- **Treating delay-code entry and lift-defect logging as optional** — the absence of a log entry is read, in an ADA complaint or FTA audit, as the failure never having been reported, which is worse than the failure itself.

## Worked example

**Situation.** Route 42, scheduled 12-minute headway, terminal recovery (layover) time built into the schedule at 15 minutes. At Stop 14 (scheduled arrival 2:38 p.m.), the driver is already 6 minutes behind (actual arrival 2:44 p.m.) after a signal delay upstream. Snow has started; the road surface is going from wet to icy. A rider using a manual wheelchair is waiting to board.

**Naive read.** The driver is worried about compounding the 6-minute deficit before it hits the terminal, and a junior operator's instinct is to do a fast, partial securement (straps only, skip the shoulder belt "since it's a short ride to the next stop") and hold normal following distance and speed to try to claw back time.

**Expert reasoning.**

*Securement time, reconciled:* ramp deploy 20 sec + position wheelchair 15 sec + four-point tie-down 40 sec + lap/shoulder belt 15 sec + ramp stow 10 sec = 100 seconds (1:40). Added to the existing 6:00 deficit, the bus is now 7:40 behind at Stop 14's departure. Against the 15:00 terminal recovery buffer, that leaves 15:00 − 7:40 = **7:20 of recovery time still intact** — the full, correctly-secured stop costs nothing that recovery time doesn't already absorb. There is no OTP case for rushing the belt.

*Following distance, reconciled:* at the posted 20 mph (≈29 ft/sec) on dry pavement, a standard following/stopping allowance for a 40-foot coach is roughly 50 feet. Icy conditions carry a roughly 3–4x stopping-distance penalty, meaning the same 50-foot allowance now requires either ~150–200 feet of following distance at 20 mph, or a lower target speed. The driver drops to 12 mph between Stop 14 and Stop 15, which brings the effective stopping allowance back down near the original ~50-foot dry-pavement figure — the correct fix is the speed change, not just opening a bigger gap at the same speed.

*Net effect:* full securement (100 sec) + reduced speed segment (adds roughly 45 sec over that block at 12 mph vs. 20 mph) brings the deficit to about 8:25 by Stop 15 — still 6:35 inside the 15-minute recovery buffer.

**Deliverable — radio call to dispatch, as transmitted:**

> "Dispatch, Route 42 Run 8. Currently 8 minutes down at Stop 15, account of full wheelchair securement at Stop 14 and reduced speed for road conditions between 14 and 15. Terminal recovery intact, no additional resource needed. Will advise if that changes."

The point for a coaching conversation afterward: the driver didn't lose the schedule to the wheelchair stop or the weather — the 15-minute recovery buffer exists precisely to absorb exactly this kind of stack of ordinary delays, and the radio call turns the decision into a documented, defensible record instead of a guess a supervisor has to reconstruct later.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for filled templates: pre-trip/lift cycle-test checklist, wheelchair securement sequence, 8-point mirror/blind-spot check, de-escalation response ladder, delay-code radio format, duty-day worksheet.
- [references/red-flags.md](references/red-flags.md) — load when triaging an operator's performance, an ADA complaint, or a safety review and need the specific smell tests and what to pull.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (headway, recovery time, deadhead, WC19, complementary paratransit) needs a precise definition and the misuse to avoid.

## Sources

- FMCSA, 49 CFR §395.5 — hours-of-service limits specific to drivers of passenger-carrying commercial motor vehicles (15-hour on-duty window, 10-hour driving limit, 60/70-hour 7/8-day limits).
- FMCSA, 49 CFR Part 383 Subpart F — CDL Passenger (P) endorsement knowledge and skills test requirements (emergency exits, railroad-highway crossings, passenger management, use of accessibility equipment).
- U.S. DOT, 49 CFR Part 37 — ADA transportation regulations: accessible vehicle requirements, lift/ramp maintenance and out-of-service obligations (§37.161–37.165), complementary paratransit service criteria (§§37.121–37.139).
- SAE J2249 / ANSI-RESNA WC19 — wheelchair securement and occupant-restraint system standard referenced by transit-vehicle securement point design and anchorage load ratings.
- Federal Transit Administration, Public Transportation Agency Safety Plan rule, 49 CFR Part 673 (effective 2020) — requires transit agencies to maintain their own safety/fatigue-management plans, the mechanism by which most fixed-route transit driver duty limits are actually set (rather than FMCSA Part 395).
- Crisis Prevention Institute (CPI), Nonviolent Crisis Intervention training model — behavior-level/response-ladder framework widely adopted by transit agency security/operator training programs (e.g., WMATA, King County Metro).
- American Public Transportation Association (APTA) — on-time-performance measurement conventions and recommended practices for bus operations and safety/security training.
- No direct transit-bus-driver practitioner has reviewed this file yet — flag corrections or gaps via PR.
