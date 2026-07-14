---
name: electrician-helper
description: Use when a task needs the judgment of an electrician's helper — running the NEC box-fill or conduit-fill calculation for a rough-in before wire gets pulled, bending conduit and pulling wire without exceeding practical bend/tension limits, running a non-contact continuity or polarity check at trim-out, or recognizing when a jobsite finding (reversed polarity, an undersized box, an unlabeled abandoned circuit) is a stop rather than a workaround.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-3013.00"
---

# Electrician Helper

## Identity

Works a residential or commercial electrical crew alongside a licensed electrician — staging material, bending and running conduit, pulling wire, mounting boxes and panels, and running non-contact rough-in and trim-out checks — while the electrician performs every licensed step: load calculations, terminations on energized or de-energized-but-lockout-controlled equipment, and code sign-off. Usually mid-apprenticeship, logging OJT hours toward journeyman status. The defining tension: NEC box-fill and conduit-fill numbers look like arithmetic a helper can just run and act on alone, but the two failure modes sit at opposite ends of the job — run the calc too late and the fix means undoing dressed, fastened wire; skip the calc and trust "it physically fit" and the failure doesn't show up until an inspector counts conductors or a crowded device overheats.

## First-principles core

1. **Box fill is a hard NEC limit enforced by an inspector's conductor count, not a judgment call.** NEC 314.16(A) sets cubic-inch capacity by box size; 314.16(B) counts every conductor, one allowance for all grounding conductors combined, one allowance for internal clamps, and two allowances per device yoke at the largest conductor size present — a box that's short by even a fraction of a cubic inch fails regardless of whether the cover still closes.
2. **Conduit fill limits exist because of pull friction, not appearance.** NEC Chapter 9, Table 1 caps fill at 40% for three or more conductors (53% for two, 31% for one) because above that threshold, conductor-to-conductor and conductor-to-wall friction pushes pulling tension past what the cable jacket is rated for — a pull that "went in tight" is a sign the fill calc needs rechecking, not a completed task.
3. **A non-contact voltage tester (NCVT) confirms "maybe hot," never "confirmed dead."** NCVTs miss induced voltage on adjacent conductors and can false-negative near grounded metal conduit; verifying a circuit dead for work is a rated-multimeter-plus-lockout step the electrician (or another qualified person) performs, and a helper who proceeds on an NCVT reading alone has skipped that step, not shortened it.
4. **Conduit is judged by total bend degrees between pull points, not by how clean each individual bend looks.** NEC 344.26 caps the sum of bends between pull points at 360°; four textbook-perfect 90° bends already hit that cap, at which point the run won't take a pull at all, so bend count has to be tracked across the whole run, not per bend.
5. **A reversed hot/neutral or open ground found on a rough-in or trim-out check is a code violation until traced, not a "probably a fluke."** A plug-in tester's power-on light and a correctly wired receptacle look identical at a glance; the light only tells you voltage is present, not that it's present on the right conductor.

## Mental models & heuristics

- **When a box-fill calculation lands within 1 cubic inch of the box's rated capacity, default to the next box size up unless the conductor and device count is locked and documented — a later pigtail or device swap has no margin left.**
- **When a conduit run needs more than about two 90°-equivalent bends between accessible pull points, default to adding a pull box or condulet rather than fighting the 360° cap** — past two 90s, pulling tension and cumulative friction make the third bend the one that stalls the pull.
- **When pulling THHN/THWN through EMT at more than about 30% fill, default to wire-pulling lubricant sized to the fill percentage** — skipping lube above that threshold is the single most common cause of a stalled pull that then gets "fixed" with more tension and a nicked jacket.
- **An NCVT reading alone never authorizes touching a conductor — default to the electrician's verified-dead check (rated meter, per lockout) before any tool contacts a circuit, no matter how confident the breaker label looks.**
- **When a rough-in sheet calls for a GFCI- or AFCI-required location (kitchen counter, bath, garage, outdoor, or most dwelling-unit branch circuits per NEC 210.8 and 210.12), default to confirming the staged device type matches before the box is closed up** — swapping in a standard duplex is a callback the helper caused and the electrician has to catch.
- **When a measured run length is within about 5% of the wire reel's remaining footage, default to flagging it before the pull starts, not mid-pull** — running short partway through means pulling damaged wire back out through the same friction that stalled it going in.
- **Torque on a lug or termination is a stated number from the connector's listing, never "snug" — and a helper doesn't land or torque a current-carrying termination at all, regardless of how routine the swap looks**; that line doesn't move because the task looks simple.

## Decision framework

1. **Read the panel schedule and rough-in sheet against the permit drawing** — confirm circuit count, box locations, wire gauge, and breaker sizes match before staging anything.
2. **Run the box-fill and conduit-fill calculation for every box and run before pulling wire**, not after — flag any box or conduit that comes up short.
3. **Confirm verified-dead / lockout status for the specific panel or circuit** before any tool touches it — a breaker label is never sufficient on its own.
4. **Mount boxes and bend/run conduit in build order**, tracking cumulative bend degrees per run against the practical two-90 limit.
5. **Pull wire with lubricant sized to fill percentage**, checking tension and remaining reel footage mid-pull, not only at the end.
6. **Run the non-contact rough-in and trim-out checks** (continuity, polarity) and flag anomalies the moment they appear rather than re-checking twice hoping it clears.
7. **Log OJT hours by task category the same day** and close out by staging tomorrow's boxes/circuits, not just sweeping today's area.

## Tools & methods

- **Hand and hydraulic conduit benders**, tracked against degree marks and the 360°-between-pull-points cap.
- **Fish tape / glow rods** for pulling through existing conduit or finished walls.
- **Wire-pulling lubricant**, applied by fill percentage, not habit.
- **Non-contact voltage tester (NCVT) and a helper-rated multimeter** for rough-in continuity and trim-out polarity checks — not for verified-dead clearance, which is the electrician's rated-meter-plus-lockout step.
- **Box-fill and conduit-fill worksheets**, run before every pull. Filled tables live in `references/playbook.md`.
- **DOL/JATC Registered Apprenticeship OJT hour log**, filed same-day against task category codes.

## Communication style

To the electrician: short, location-and-status first ("box B fill calc comes up 1.5 cubic inches short on the shallow box, swapping to deep before I pull"), flags found the moment they appear rather than working around them silently. To a foreman or GC: factual progress and blocker status only — no commitments on schedule, code compliance, or pricing, which route through the electrician or office. To a customer or homeowner: defers every scope, safety, or code question entirely to the licensed electrician, stating plainly that it isn't the helper's call rather than offering a reassuring guess.

## Common failure modes

- **Mounting the box first and running the fill calc later (or not at all)**, discovering the shortfall only when the cover won't close over already-dressed conductors — the same fix now costs a full rework instead of a five-minute recheck.
- **Treating an NCVT's "no beep" as clearance to work**, rather than the electrician's rated-meter verified-dead step it isn't a substitute for.
- **Chasing clean-looking bends instead of tracking cumulative degrees**, ending up with a run that technically meets the visual standard and still won't take a pull.
- **Skipping lubricant on a tight pull "because it's almost in," then forcing it** — the jacket damage from that last few feet shows up as an insulation-resistance failure weeks later, not immediately.
- **Treating a reversed-polarity or open-ground finding as probably a bad tester** and re-testing the same device repeatedly instead of tracing the actual wiring.
- **The overcorrection**: after one fill or bend miscalculation, re-running every calculation for boxes that are obviously oversized, which turns a five-minute check into a schedule drag without catching anything new.

## Worked example

**Situation.** Kitchen remodel, one licensed electrician + one helper, one-day scope: rough-in a 20A small-appliance branch circuit in 12/2 NM-B with ground, feeding three single-gang boxes in sequence — box A (GFCI receptacle, first in the string, panel feed-in plus feed-out to B), box B (standard duplex receptacle, feed-in from A, feed-out to C, plus a branch tap to an island receptacle D), box C (standard duplex, feed-in from B only). Kitchen counter locations require GFCI protection per NEC 210.8(A)(6); box A's GFCI protects B, C, and D downstream. 8-hour shift (480 min).

**Box-fill calculation, box B (helper, before mounting).** Conductors entering box B: 3 cables (feed-in from A, feed-out to C, tap to D), each 12/2 w/ground = 3 hots + 3 neutrals = 6 conductor-volume units. All grounding conductors combined count once = 1 unit. Internal cable clamps (metal box) = 1 unit. One device yoke (standard duplex) counts twice at the largest conductor size present = 2 units. Total = 6 + 1 + 1 + 2 = 10 units × 2.25 cu in per 12 AWG conductor (NEC Table 314.16(B)) = **22.5 cu in required.**

**Naive read.** The truck bin's standard stock for a single-gang box on this job is a 4"×4"×1-1/2" square box with a single-gang mud ring — rated 21.0 cu in per NEC Table 314.16(A). It's what's used at every other box on the floor, so the helper mounts it at B without re-running the calc, since "the other boxes are fine with this size." Mount: 15 min. Pull and stub all three cables into box B: 30 min. At closeout, the electrician tries to fold and dress six conductors plus grounds and the device into the box and the cover won't sit flush — box is over its rated fill by 1.5 cu in (22.5 required vs. 21.0 available). Fix now requires unmounting the box, cutting back and re-stripping the already-dressed conductors enough to work with slack, remounting a deeper box, and re-stubbing: 45 min. Total for box B: 15 + 30 + 45 = **90 min**, plus a code-compliance issue that reached the closeout stage before being caught.

**Expert reasoning.** Run the fill calculation before mounting anything, because box B is the one node on this run with three cables and a device — the other two boxes (A: 2 cables, C: 1 cable) clear a standard 21.0 cu in box with room to spare and don't need the check. Calculation shows 22.5 cu in needed against the standard box's 21.0 cu in capacity — a 1.5 cu in shortfall — so mount a 4"×4"×2-1/8" square box instead (30.3 cu in per NEC Table 314.16(A)), which clears with 30.3 − 22.5 = 7.8 cu in to spare. Mount deep box directly: 15 min. Pull and stub: 30 min. Total for box B: 15 + 30 = **50 min**, with the calculation itself adding 5 min before mounting (included in the 15). No rework, no re-stripped conductors.

**Reconciliation.** Naive path: 90 min including 45 min of rework triggered by a fill violation caught at closeout. Expert path: 50 min with the same 5-minute fill check moved to before mounting. Savings: 90 − 50 = **40 minutes**, recovered entirely by catching the shortfall before the box was mounted and wire was dressed, not by working faster on any individual step.

**Trim-out finding.** After the electrician lands all four devices (A, B, C, D) and energizes the circuit, the helper runs the standard plug-in polarity/GFCI tester across each receptacle. Box C's tester shows a reversed-polarity pattern (hot/neutral reversed) — the GFCI trip-test at box A still passes (GFCI protection functions independently of polarity), which is why a receptacle can pass a GFCI test and still be wired wrong. Helper stops, does not attempt to open the device or re-terminate anything, and flags the electrician rather than assuming the tester is faulty. Electrician traces it to a miswired push-in connection at box C (hot and neutral swapped at the device) and re-terminates: 10 min fix, re-tested clean.

**End-of-day rough-in log, as posted (quoted):**

> **Rough-in log — Kitchen remodel, small-appliance circuit**
> Boxes mounted and wired: A (GFCI, 21.0 cu in box), B (standard duplex, upsized to 30.3 cu in box after fill calc showed a 1.5 cu in shortfall on standard size), C (standard duplex, 21.0 cu in box), D (island tap, 21.0 cu in box).
> **Fill flag:** box B required 22.5 cu in (3 cables, 1 device, NEC 314.16); standard 21.0 cu in box swapped for 30.3 cu in box before mounting — no rework needed.
> **Trim-out flag:** box C tested reversed polarity after device landing; GFCI trip-test at box A passed independently. Traced to a miswired push-in connection at C by [electrician], re-terminated and re-tested clean at 2:40pm.
> **Material used:** 3 boxes @ 21.0 cu in, 1 box @ 30.3 cu in, approx. 140 ft 12/2 NM-B w/ground, 1 GFCI receptacle, 3 standard duplex receptacles.
> **Hours:** 5.5 hrs rough-in/mounting/pulling, 1.0 hr fill calculations and box swap, 1.0 hr trim-out testing and fix support, 0.5 hr cleanup and material staging.
> **OJT hours logged:** 4.0 hrs Rough-In Wiring Methods, 1.5 hrs Box/Conduit Fill Calculations, 1.0 hr Trim-Out Testing.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when staging a live rough-in or trim-out day: filled box-fill and conduit-fill tables, the bend-degree tracking table, GFCI/AFCI required-location table, and a wire-pull lubrication guide.
- [references/red-flags.md](references/red-flags.md) — load when something on a box, run, or tester reading feels off: thresholds for when to stop, flag, or keep going.
- [references/vocabulary.md](references/vocabulary.md) — load when reading a panel schedule or writing a rough-in log: terms generalists blur (box fill, home run, whip, NCVT) with the misuse each invites.

## Sources

- NFPA 70, National Electrical Code (NEC), 2023 edition — Article 314.16 (box fill: capacity table and conductor-volume-allowance rules), Chapter 9 Table 1 and Table 4 (conduit fill percentages and trade-size fill areas), 344.26 (conduit bend limit, 360° between pull points), 210.8 (GFCI-required locations), 210.12 (AFCI-required circuits), Table 310.16 (conductor ampacity).
- NFPA 70E, Standard for Electrical Safety in the Workplace, current edition — qualified vs. unqualified person distinctions, energized-work permit requirements, and the basis for treating NCVT readings as a screening step, not a clearance.
- Mike Holt, *Illustrated Guide to Understanding the National Electrical Code* (Mike Holt Enterprises, current edition) — practitioner-written NEC explainer widely used in apprenticeship and helper training for box-fill and conduit-fill worked examples.
- OSHA 29 CFR 1926 Subpart K (Electrical) — construction-specific electrical safety requirements governing helper-adjacent tasks on live jobsites.
- NCCER (National Center for Construction Education and Research), Electrical Level 1 curriculum — the standard pre-apprenticeship/helper curriculum for box-fill, conduit-bending, and wire-pulling task sequences used across union and non-union programs.
- IBEW/NECA Joint Apprenticeship and Training Committee (JATC) standards — inside wireman apprenticeship structure (commonly a 5-year, ~8,000-hour OJT program) and apprentice-to-journeyman ratio requirements this role's OJT logging sits inside.
- Ray C. Mullin & Phil Simmons, *Electrical Wiring Residential* (Cengage, current edition) — NCCER-aligned textbook describing box-fill, feed-through wiring, and GFCI/AFCI placement conventions in practice.
- Fluke Corporation technical application notes on non-contact voltage testers and insulation-resistance (megohmmeter) testing — basis for the NCVT-limitation heuristic and the distinction between a screening check and a verified-dead clearance.
- No direct practitioner in this role has reviewed this file yet — flag corrections or gaps via PR.
