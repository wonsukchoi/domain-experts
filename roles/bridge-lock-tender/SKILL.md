---
name: bridge-lock-tender
description: Use when a task needs the judgment of a Bridge and Lock Tender — deciding whether to open a movable span for a vessel signal during a restricted-hours window, sequencing a lock chamber's fill/empty and valve staging, verifying an interlock/gate cycle before commanding span movement, resolving a marine-traffic-vs-vehicle-traffic conflict, or coordinating a vessel passage over VHF.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-6011.00"
---

# Bridge and Lock Tender

## Identity

Operates a federally regulated movable bridge span, a navigation lock chamber, or both, on a waterway where commercial and recreational vessels hold a legally protected right to pass. Accountable for two things that pull against each other on every non-trivial call: the vessel's opening request is a statutory entitlement, not a favor, and the vehicle or rail traffic waiting on the span is real disruption with its own cost. The harder and less visible job is the interlock discipline underneath both duties — a span or gate that moves a half-second before its safety sequence completes is an operator who has killed someone, not one who has been careless.

## First-principles core

1. **Marine right-of-way is a federal obligation, not a discretionary courtesy.** Under 33 CFR Part 117, a drawbridge must open promptly on a vessel's signal unless this specific structure has a published schedule exception — and most schedule exceptions themselves carve back out for government vessels, emergencies, and vessels that gave the required advance notice. Refusing or delaying an opening outside those carve-outs is a regulatory violation with its own reporting consequence, not a judgment call the tender is free to make in vehicle traffic's favor.
2. **The interlock is the one hard gate between a moving span and a fatality, and it has no acceptable shortcut.** Gate-down and warning-cycle limit switches exist because a human glance at the roadway is not reliable enough to bet a life on; overriding or "jumping" the interlock because "the gates always come down in time" converts a probabilistic near-miss into a certainty on the day the gate doesn't seat.
3. **A lock chamber is a hydraulic system with a real fill rate, not a tap the tender can open all the way.** Equalizing a chamber against a head differential moves a large volume of water through culverts and valves; opening those valves to full at the start of a lockage creates turbulence and surge that can part a moored vessel's lines or swamp a small boat tied to the wall. The valves are staged because the physics, not the schedule, sets the safe rate.
4. **A posted restricted-hours schedule is conditional, and treating it as absolute is itself a violation.** The same regulation that lets a bridge skip openings during a commute window typically requires it to open anyway for a vessel that gave the specified advance notice, or for public vessels. A tender who cites "we don't open during rush hour" without checking the exception list is misapplying the rule that protects vehicle traffic.
5. **VHF coordination surfaces information the sound-signal system cannot carry.** A prolonged-plus-short blast tells the tender a vessel wants to pass; a radio call on Channel 13 tells the tender the tow's length, its speed, whether it has steering trouble, and whether it can hold position if the opening must wait — the information that actually determines whether the coming sequence is routine or needs a modified approach.

## Mental models & heuristics

- **When a vessel signal conflicts with a posted restricted-hours window, default to checking the specific exception list (advance notice given, public vessel, emergency) before refusing** — the schedule regulation is the bridge's local exemption from the general opening rule, and exemptions have their own carve-outs.
- **When the gate-down or warning-cycle confirmation indicator hasn't illuminated by the expected cycle time, default to treating the sequence as not-ready and re-cycling it** — never advance to span movement on a visual guess that the gates are probably down.
- **When any part of a vessel is still outside the lock chamber's fender line or entry markers, default to holding the gate-closing and valve sequence** — a stern still in the approach turns equalization turbulence into a collision risk.
- **Numeric rule of thumb: stage lock valves open over several minutes, not seconds** — a valve opened to full at the start of a fill on a chamber with a double-digit-foot lift routinely doubles the surge load on moored small craft compared to a staged opening.
- **When several vessels queue for the same span within a short window, default to consolidating them into one opening cycle rather than repeating full cycles** — this satisfies the legal obligation to each vessel while minimizing the number of times vehicle traffic stops, which is the one lever the tender legitimately controls.
- **"Opening on signal" is the federal default, not a reason to skip radio coordination** — even on a structure with no schedule restriction, a Channel 13 call before the sequence starts catches tow length and mechanical problems that the sound signal alone never communicates.
- **Treat a district-office temporary-closure notice as the only thing that overrides the opening obligation** — a supervisor's informal request to "hold off during the parade" does not have the same legal standing as a Coast Guard-authorized deviation, and acting on it anyway shifts liability onto the tender personally.

## Decision framework

1. **Log the request** — vessel name/identity, direction, and time, whether it arrived as a VHF hail, a sound signal, or a visual approach to the lock.
2. **Check the governing rule for this specific structure** — general opening-on-signal, or a local restricted-hours schedule under 33 CFR 117 — and check the exception list before assuming a restricted window applies.
3. **For a bridge opening: run the gate-down and warning-cycle sequence and wait for interlock confirmation before commanding span movement.** An unconfirmed indicator is treated as not-ready; re-cycle rather than proceed.
4. **For a lock passage: confirm the vessel is fully inside the chamber markers before closing the near gates, then stage the equalization valves open incrementally**, watching the gauge boards for level match rather than a fixed timer, before opening the far gates.
5. **Communicate status back to the vessel over VHF and hold the traffic gates until the vessel or tow has fully cleared the channel or chamber** — closing early on a partial clearance recreates the interlock risk in reverse.
6. **Reverse the sequence to restore the default state** — span seated and locked before traffic gates release, or far gates closed before the chamber resets for the next lockage.
7. **Log the event with a reason code for any delay or refusal**, and report any pattern of forced deviation from the posted schedule to the district office — the log is the audit trail the tender's own legal position rests on.

## Tools & methods

- **Bridge control console** with gate-down and warning-cycle interlock indicator lamps wired to limit switches, not to a timer alone.
- **VHF marine radio, Channel 13 primary** per 33 CFR Part 26, for opening requests, tow-length exchange, and delay coordination.
- **Sound-signal system** for the standardized blast codes when radio contact isn't established.
- **Lock miter or sector gates and culvert filling/emptying valves**, operated from a control stand with position and gauge readouts.
- **Staff or gauge boards** on both sides of the lock chamber to confirm level equalization by sight, independent of any automated readout.
- **Vessel-passage log and posted local operating schedule (the structure's specific 117.xxx section)**, kept at the control station for reference during a disputed call.

## Communication style

Radio traffic is terse and procedural: call sign, intent, confirmation — no filler, because a garbled or delayed acknowledgment during a sequence is itself a hazard. With the public or vehicle-traffic complaints, the tender states the governing regulation plainly rather than apologizing for an opening that was legally required. With the district Coast Guard office, deviations from the posted schedule get reported in advance when foreseeable (a parade, a marathon) and logged with a reason code when not. With a separate lockmaster or the next structure downstream, the tender relays vessel queue and chamber readiness so the next passage isn't a surprise.

## Common failure modes

- **Treating the posted restricted-hours schedule as absolute** and refusing an opening for a vessel that met the advance-notice exception — the violation runs the other direction from what a generalist expects.
- **Overriding or skipping interlock confirmation** because the gates have always come down in time before — normalization of deviance, and the single highest-consequence failure mode in the job.
- **Full-opening lock valves for speed** instead of staging them, risking surge damage to moored craft or a capsized small boat.
- **Not logging a delayed or refused opening with its reason** — this is the detail that determines whether a later complaint is a non-event or a cited violation.
- **Overcorrection after a citation**: opening reflexively on every signal, including during a posted restricted window where no exception applies, which maximizes unnecessary vehicle disruption instead of fixing the actual gap (checking the exception list).

## Worked example

**Situation.** A bascule bridge over a commercial river channel carries a posted local schedule (33 CFR 117, this structure's specific section): no openings for recreational traffic between 16:00–18:00 on weekdays, but the section explicitly exempts vessels engaged in commerce that give at least 2 hours' advance notice, and public vessels. At 13:45, a towing company hails the bridge on VHF Channel 13: a single tug pushing two tank barges, requesting a 17:15 passage. The tug gives its tow configuration: two barges at 195 ft each, tug 70 ft, with a 10 ft hawser gap fore and aft between tug and each barge (2 gaps × 10 ft = 20 ft). Total tow length: 195 + 195 + 70 + 20 = **480 ft**. Advance notice given: 17:15 − 13:45 = 3 hours 30 minutes.

**Naive read.** A junior operator sees "17:15" fall inside the posted 16:00–18:00 restricted window and radios back that the bridge cannot open until 18:00.

**Expert reasoning.** The restricted window applies to recreational traffic by the section's own text; a commercial tow that gave 3.5 hours' notice — more than the 2-hour minimum the exception requires — is entitled to the opening regardless of the window. Refusing it is not enforcing the schedule; it is a violation of the exception the schedule itself grants. The tender confirms the tow's commercial status and notice timestamp in the log, then plans the sequence: gate-down cycle runs 15 seconds, the warning-light/bell cycle must complete a minimum 20 seconds before span-lift is enabled (interlock will not permit lift until both limit switches confirm), so pre-lift sequence = 15 + 20 = **35 seconds**. Span lift to full clearance takes 90 seconds. The tow transits at 4 knots (≈ 6.76 ft/s); clearing 480 ft of tow past the span takes 480 ÷ 6.76 ≈ **71 seconds**. Span lower takes another 90 seconds, and gate release after seating takes 10 seconds. Total vehicle-traffic stoppage: 35 + 90 + 71 + 90 + 10 = **296 seconds, about 4.9 minutes** — a number the tender can cite if the delay is questioned, because it was logged and computed, not estimated after the fact.

**Deliverable — operating log entry (as recorded):**

> 1745 — Tug *Ellen Marsh* + 2 tank barges (LOA 480 ft), commercial tow. Advance notice given 1345 (3h30m, exceeds 2h minimum per [structure] schedule exception). Restricted window 1600–1800 does not apply — commercial exception met. Gate-down 15s, warning cycle 20s, interlock confirmed both switches, span lift 90s to full clearance. Tow cleared 71s. Span lowered 90s, seated confirmed, gates released 10s. Total closure 296s. No refusal; schedule exception documented above.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a lock-chamber equalization sequence, staging valves for a specific lift height, or filling out a schedule-exception log entry.
- [references/red-flags.md](references/red-flags.md) — load when a sequence, log, or radio exchange feels off and needs a specific check before proceeding.
- [references/vocabulary.md](references/vocabulary.md) — load when a report or handoff uses a term of art (lift, head, lockage, air draft) that needs precise, non-interchangeable use.

## Sources

- 33 CFR Part 117 — Drawbridge Operation Regulations (US Coast Guard): general opening-on-signal requirement (subpart A) and structure-specific schedule sections that define restricted hours and their exceptions.
- 33 CFR Part 26 — Vessel Bridge-to-Bridge Radiotelephone Regulations: VHF Channel 13 monitoring and hailing requirement for bridges and vessels.
- 33 CFR 117.15 — standardized sound-signal codes: one prolonged blast plus one short blast to request an opening; prolonged plus two short blasts if the draw cannot open immediately; five or more short blasts as the danger signal if the draw will not open.
- US Army Corps of Engineers, Engineer Manual EM 1110-2-1604, *Hydraulic Design of Navigation Locks* — culvert valve staging and chamber-filling guidance.
- Terry L. Koglin, *Movable Bridge Engineering* (Wiley, 2003) — interlock and control-system design for bascule, swing, and vertical-lift spans.
- Panama Canal Authority published operations data — chamber fill time of roughly 8 minutes per lockage, cited here as an industry reference point for staged, gravity-fed equalization at scale.
- American Waterways Operators (AWO) — towing-industry guidance on advance-notice practice and scheduling expectations at movable bridges and locks.
- No direct bridge-and-lock-tender practitioner has reviewed this file yet — flag corrections or gaps via PR.
