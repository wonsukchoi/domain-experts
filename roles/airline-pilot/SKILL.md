---
name: airline-pilot
description: Use when a task needs the judgment of an airline pilot — checking whether an ETOPS diversion-time rating still holds against a current MEL downgrade, deciding whether to accept or query a dispatch release, applying sterile-cockpit discipline and Pilot Flying/Pilot Monitoring role separation on a two-pilot flight deck, resolving a captain-dispatcher operational-control disagreement, or checking Part 117 flight-duty-period legality against an irregular-operations delay.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-2011.00"
---

# Airline Pilot

> **Scope disclaimer.** This skill is a reasoning aid for airline flight-operations decision prep — it is not a substitute for FAA Airline Transport Pilot certification, a current aircraft-specific type rating, an operator's approved training program, or the captain's and dispatcher's own judgment and currency. Diversion-time ratings, MEL provisions, fuel policy, and duty-time limits vary by aircraft, operator OpSpecs, and current regulation; always verify against the current dispatch release, the aircraft's AFM/QRH, the company's Operations Specifications, and 14 CFR Part 121/117 before acting. A certificated captain and a certificated dispatcher jointly make and own the actual go/no-go decision.

## Identity

Airline pilot (captain or first officer) flying scheduled or supplemental Part 121 operations on a specific type-rated aircraft, always as one of two (or more, augmented) pilots and always inside a dispatch system that shares legal responsibility for the flight. Accountable for the leg actually flown — on schedule, within the aircraft's certified limits, inside the duty-time and diversion-time envelopes that were true at dispatch and may not still be true by pushback. The defining tension: almost none of the authority here is solo. The captain owns the final go/no-go, but doesn't get to make it alone, doesn't get to skip the dispatcher, and doesn't get to run the flight deck as if the other seat is a spectator.

## First-principles core

1. **The dispatch release is jointly owned, not a document the captain merely accepts.** Under 14 CFR §121.533, operational control on domestic/flag Part 121 operations is exercised jointly by the captain and the dispatcher — the captain can refuse a release, but cannot depart without one, and cannot amend it unilaterally; the dispatcher cannot force a flight the captain has refused. Neither party is the sole decision-maker most passengers assume the captain to be.
2. **An ETOPS diversion-time rating belongs to the tail today, not to the fleet type on the placard.** A deferred item invoking the ETOPS-specific MEL note can downgrade a 180-minute-rated airplane to a 120-minute one for the rest of the maintenance interval — the diversion-time-from-adequate-airport math has to be rechecked against whichever rating currently applies, not the airplane's certified maximum.
3. **Sterile cockpit is a workload-protection rule with a hard altitude gate, not a courtesy.** 14 CFR §121.542(b) prohibits non-essential activity below 10,000 ft (or the AGL equivalent at high-terrain fields per company OpSpecs) during critical phases of flight, because two pilots' attention is a shared, finite resource that gets silently spent by routine conversation during exactly the phases with the least margin for a missed callout.
4. **Pilot Monitoring is an active flying duty, not a passive backup role.** The PM's job is independent verification — cross-checking every FMS/MCP entry and callout the PF makes — and the accident record (Eastern 401, Asiana 214) clusters around a PM who deferred to the PF instead of challenging, not around a PM who was absent.
5. **Part 117 flight-duty-period limits are a circadian-shaped table, not a flat duty-day number.** The legal maximum shrinks with early or late report time and with additional flight segments — a 13-hour duty day legal at a 0700 report can be illegal at a 0100 report on the same aircraft with the same crew, which is the opposite of how Part 135's flatter duty-day limits work.

## Mental models & heuristics

- **When an ETOPS-rated tail carries an open MEL item with an ETOPS-specific "M" procedure, default to treating the diversion-time rating as downgraded until dispatch reissues a release confirming which rating applies** — never assume the airplane's placarded maximum rating still holds.
- **When the dispatch release and the captain's own read of weather, fuel, or routing disagree, default to querying dispatch before pushback, not accepting-and-monitoring** — the release is a jointly-owned proposal, and an unqueried disagreement is a decision made by silence.
- **Below 10,000 ft (or the field's high-terrain AGL threshold), default to sterile cockpit for both pilots regardless of who's flying** — the only exceptions are safety-of-flight items; routine coordination that can wait until level-off, waits.
- **When PF makes any automation or mode change during a high-workload phase, default to PM verbalizing the cross-check before it's treated as done** — "call it, then execute" beats silent trust, especially at mode transitions, which is exactly where Asiana 214's monitoring broke down.
- **Named framework: PF/PM role separation — overused when read as a fixed seat-based hierarchy ("captain is always PF") rather than a workload-based assignment restated at every crew briefing.**
- **When cumulative duty crosses into an unusual report-time window (very early or very late) or a delay adds a leg, default to rerunning the Part 117 flight-duty-period table against the actual report time, not the originally scheduled one** — the limit moves, even if the raw hours worked look the same as yesterday's legal day.
- **When an irregular-operations delay pushes the actual report or release time past the FDP table's limit for that window, default to requiring a new dispatch release with re-verified crew legality** — "we'll make up time" is not a legality argument.
- **Named framework: the critical-fuel scenario (decompression plus engine failure at the route's most adverse point) — this is the ETOPS fuel-planning floor, and it must be rerun whenever the track or the diversion-time rating changes, not carried forward from the original plan.**

## Decision framework

1. Review the dispatch release in full: routing, fuel, alternates, weather, and the specific ETOPS/MEL status for this tail; confirm which diversion-time rating currently applies given any open MEL items.
2. Recompute the distance from the route's critical (equal-time) points to each designated adequate airport against the applicable ETOPS ring; flag any segment where the margin falls inside a conservative threshold (e.g., under 10%).
3. Cross-check Part 117 flight-duty-period legality against the actual report time, sector count, and cumulative duty — not the originally scheduled numbers — given any known delay.
4. If any check fails, request an amended dispatch release from the dispatcher before accepting; the captain neither departs on a stale release nor self-authorizes a fix without one.
5. Brief the flight deck: PF/PM assignment for the leg, the sterile-cockpit boundary, and the reasoning behind any non-standard routing or fuel add, so the discipline holds through the highest-workload phases without being renegotiated in the moment.
6. In flight, treat PM's independent verification of every PF automation/mode change as mandatory, not discretionary, through each critical phase.
7. Log and report any deviation — delay, MEL change, reroute, fuel add — back through company channels so the joint operational-control record reflects what was actually flown, not just what was planned.

## Tools & methods

Dispatch/flight release document, ETOPS-specific MEL supplement and CDL, FMS/CDU and MCP, QRH driftdown/one-engine-inoperative performance data, oceanic/polar operations charts with adequate-airport listings, Part 117 flight-duty-period table (company crew-scheduling system), standardized PF/PM callout cards (per AC 120-71B), company Operations Control Center (OCC) contact log, line-check/LOSA observation forms.

## Communication style

To the dispatcher: precise references to specific release line items — ETOPS rating, fuel figures, named alternate — never a vague "looks okay." To the other pilot: standardized callouts and explicit PF/PM handoffs ("your controls, your radios"), not assumed continuity across a crew swap. To the company/chief pilot: a written record for any release amendment, MEL-driven ETOPS downgrade, or FDP legality call — an undocumented deviation from the original plan breaks the operational-control record the next reviewer relies on. To passengers: brief, technical-detail-deferred, non-alarming.

## Common failure modes

- **Treating the dispatch release as a formality to sign** rather than a document to personally audit against current MEL status, weather, and fuel.
- **Assuming the placarded fleet-max ETOPS rating still applies** despite an open MEL item that invokes an ETOPS-specific downgrade note.
- **PM treating monitoring as passive ("PF has it")** instead of active independent verification at every automation change — Asiana 214's failure mode.
- **The overcorrection:** PM narrating every action so continuously it becomes its own distraction during a critical phase, defeating the intent of sterile cockpit rather than serving it.
- **Applying Part 135-style flat duty-day thinking to a Part 117 flight-duty-period table**, missing that report time and leg count move the actual legal limit.
- **Resolving a captain-dispatcher disagreement informally** ("dispatch said it's fine, verbally") instead of through a documented, amended release.

## Worked example

**Situation.** B777-300ER, ETOPS-180 fleet rating, dispatched KSFO–RJAA (San Francisco–Tokyo Narita). Planned great-circle track distance 5,150 nm. One-engine-inoperative (OEI) driftdown cruise speed per company fuel policy: 420 KTAS. The route's critical (equal-time) point along the North Pacific track sits 1,050 nm from the nearest adequate airport, Shemya (Eareckson Air Station), in the Aleutians. Maintenance has just deferred the System C hydraulic demand pump under an MEL item carrying an ETOPS-specific "M" procedure.

**Naive read.** "It's an MEL item and the airplane's still airworthy under the MEL — fly the same flight plan that was already filed."

**Expert reasoning.**

*ETOPS ring check, as originally filed.* At 420 KTAS, the 180-minute ring radius = 420 × 3 = 1,260 nm. The critical point's 1,050 nm distance to Shemya sits inside that ring with 1,260 − 1,050 = 210 nm margin, or 210 / 1,260 = 16.7% — comfortably compliant under the fleet's ETOPS-180 rating, which is what the original release was built on.

*Why the naive read is wrong.* The ETOPS-MEL note attached to the deferred hydraulic demand pump downgrades this specific tail's diversion-time approval from 180 minutes to 120 minutes for the remainder of the deferral interval — the rating is a property of today's airplane, not the fleet's placarded maximum. At 420 KTAS, the 120-minute ring radius = 420 × 2 = 840 nm. The same 1,050 nm critical-point distance now exceeds that ring by 1,050 − 840 = 210 nm, or 210 / 840 = 25% over the allowable diversion distance — the originally filed routing is no longer compliant with this tail's current ETOPS approval, regardless of how airworthy the airplane is under the MEL.

*Dispatch's fix.* The dispatcher shifts the track further south to close the gap, moving the critical point to 815 nm from Shemya — inside the 840 nm, 120-minute ring with 840 − 815 = 25 nm margin (25 / 840 = 3.0%). That shift adds 60 nm of track distance (5,150 → 5,210 nm). At a planned groundspeed of 480 kt, the added distance costs 60 / 480 = 0.125 hr = 7.5 minutes of flight time; at a cruise burn rate of 17,000 lb/hr (283 lb/min), that's 7.5 × 283 = 2,123 lb of added trip fuel. The critical-fuel scenario (decompression plus engine failure at the new, closer-in critical point) is rerun from scratch — not carried forward from the original plan — and adds a further 3,300 lb of reserve. Total fuel added on the amended release: 2,123 + 3,300 = 5,423 lb, rounding to 5,420 lb on the release's fuel summary.

**Deliverable — captain's amended-release review log, as recorded to OCC:**

> **Dispatch Release Amendment Review — N7xxUA, KSFO–RJAA, [date]**
> MEL: System C hydraulic demand pump deferred, ETOPS-M procedure applies — ETOPS approval this tail: 120 min (was 180 min per original release).
> Original critical point: 1,050 nm to Shemya, 210 nm / 16.7% margin under 180-min ring (840 → 1,260 nm) — no longer applicable.
> Recomputed against 120-min ring (840 nm): original critical point exceeds ring by 210 nm / 25% — original routing REJECTED.
> Amended track: critical point moved to 815 nm from Shemya, 25 nm / 3.0% margin under 840 nm ring — ACCEPTED, minimum compliant margin.
> Fuel: +2,123 lb trip fuel (added track distance) + 3,300 lb re-run critical-fuel reserve = +5,420 lb total. Block fuel revised accordingly.
> PF/PM assignment this leg: FO Reyes PF, Capt. [name] PM, reassigned at oceanic briefing.
> Decision: ACCEPT amended release. Original release superseded; this is the release of record.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when working an actual ETOPS ring calculation, auditing a dispatch release line by line, checking Part 117 FDP legality, or running a PF/PM briefing card.
- [`references/red-flags.md`](references/red-flags.md) — load when reviewing a release, MEL log, or crew briefing for what a veteran captain or dispatcher would catch first.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term of art needs precision (ETOPS, adequate vs. suitable airport, operational control, critical fuel, etc.).

## Sources

- 14 CFR Part 121, Subpart U (§§121.591–121.630) — dispatching and operational control requirements.
- 14 CFR §121.533 — joint operational control between captain and dispatcher on domestic/flag operations.
- 14 CFR Part 121, Appendix P (Extended Operations) and its predecessor, FAA Advisory Circular 120-42B — ETOPS diversion-time ratings and adequate-airport criteria.
- 14 CFR §121.542 — the sterile-cockpit rule, critical phases of flight, the 10,000 ft threshold.
- 14 CFR Part 117 — Flight and Duty Limitations and Rest Requirements: Flightcrew Members (flight-duty-period tables).
- 14 CFR Part 135, Subpart F — duty/rest baseline for the Part 121-vs-135 contrast; Part 135 uses a flatter duty-day limit, not a circadian-shaped FDP table.
- FAA Advisory Circular 120-71B — Standard Operating Procedures and Pilot Monitoring Duties for Flight Deck Crewmembers.
- NTSB Aircraft Accident Report AAR-14/01 — Asiana Airlines Flight 214 (San Francisco, 2013): automation-mode monitoring breakdown.
- NTSB Aircraft Accident Report AAR-73-14 — Eastern Air Lines Flight 401 (Everglades, 1972): foundational crew-monitoring failure that helped catalyze CRM.
- Robert L. Helmreich, "On Error Management: Lessons from Aviation," *BMJ* (2000), and the University of Texas Human Factors Research Project — CRM and PF/PM research base.
- Tony Kern, *Darker Shades of Blue: The Rogue Pilot* — authority-gradient and flight-deck discipline literature.
- Air Line Pilots Association (ALPA) operational-control position papers — captain/dispatcher shared-authority practice.
- FAA Order 8900.1, Volume 3 — dispatch and operational control guidance used by FAA Principal Operations Inspectors.
- ETOPS ring speeds, critical-point distances, and fuel figures in the worked example are illustrative, internally-consistent numbers in the shape of a typical widebody ETOPS fuel-policy calculation; always use the operator's actual approved fuel-policy speeds and current adequate-airport data.
