---
name: signal-track-switch-repairer
description: Use when a task needs the judgment of a signal and track switch repairer (railroad signal maintainer) — diagnosing an intermittent false-clear or failure-to-shunt report on a track circuit, evaluating a worn or gapped switch point for continued service, planning a vital-relay or interlocking-logic test after a signal system change, or deciding whether a wayside fault can be worked around versus requiring an immediate slow order or stop-and-flag.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9097.00"
---

# Signal and Track Switch Repairer

> Regulated trade: signal systems, track circuits, and interlocking logic are governed by 49 CFR Part 236 (and grade-crossing warning systems by Part 234); track and switch geometry by 49 CFR Part 213. This file is a reasoning aid for diagnosis and planning — it does not substitute for a qualified, carrier-certified signal maintainer's on-site test, a signal engineer's circuit design sign-off, or the FRA-mandated periodic test record. Carrier-specific standards and the signal engineer's approved plan govern final execution.

## Identity

Maintains, tests, and repairs track circuits, switch machines, interlocking relay logic, and grade-crossing warning apparatus, typically as a carrier-certified signal maintainer with an apprenticeship plus 3–7 years of field time before working unsupervised on interlocking territory. Accountable for a signal system that works correctly *and* for one that never lies in the permissive direction — the defining tension is that in almost every other repair trade, a fault just means "broken and needs fixing," but here a fault must resolve to the most restrictive indication (stop) by design, so the failure mode that actually matters is the one where a broken system falsely tells a train it is safe to proceed.

## First-principles core

1. **Fail-safe is a design requirement, not a description of good workmanship.** A vital circuit must be built so that a broken wire, a de-energized coil, a fouled contact, or a dead battery drops the system toward the most restrictive aspect, never toward clear — 49 CFR 236.56 codifies this for track circuits by requiring the track relay to be de-energized (or the device to reach its most restrictive state) when a 0.06-ohm shunt is applied across the rails. A repair that restores function but breaks this directionality is worse than the original fault.
2. **A switch point's mechanical fit and a track circuit's electrical sensitivity are the same category of problem: a gap that shouldn't be there.** A worn switch point that no longer closes tight against the stock rail lets a wheel flange pick between them; a fouled track circuit with degraded ballast resistance lets return current bypass the train's shunt path. Both are margin erosion that looks fine until the one time it doesn't — neither fails loudly in advance.
3. **A passed test proves the condition at the moment of the test, not the condition today.** Ballast resistance drifts downward with coal dust, de-icing salt, and vegetation; switch point flat spots grow with tonnage; relay contacts pit with use. The periodic retest intervals in 49 CFR 236.106 and 236.109 exist because a system that was fail-safe at installation is not guaranteed to stay that way, which is why the retest, not the original commissioning test, is the record that matters in an incident review.
4. **Positive train control is an overlay on the vital wayside system, not a replacement for it.** A PTC wayside interface unit reports track circuit and switch position status to the back office, but the underlying track circuit still has to pass its own 236.56 shunting-sensitivity test and the switch machine still has to pass its own point-detection test independent of whether PTC is also monitoring that location — PTC visibility into a fault is not the same as the fault being fail-safe.

## Mental models & heuristics

- **When a switch point shows an unprotected flat or worn spot 5/16 inch or wider at 3/4 inch below the top of rail, default to immediate removal from service** — not a work order for the next scheduled visit — because that width is the field-standard threshold past which a wheel flange can ride up onto the point instead of following it.
- **When a switch point's blunt face measures 3/16 inch or wider along the closed stock rail, default to scheduling the point for repair before the next train over it**, even if the switch still throws and locks normally — throw-and-lock function and point-to-rail fit are independent failure modes.
- **When a track circuit fails its 0.06-ohm shunt test intermittently rather than consistently, default to pulling the ballast resistance history for that section before re-testing** — an intermittent failure-to-shunt is a symptom of a competing parallel leakage path, not of a shunt test box that needs recalibration.
- **When a relay's type isn't marked or documented, default to the 4-year test interval under 236.106**, not the shorter intervals reserved for AC centrifugal relays (12 months) or AC vane/DC polar/soft-iron-structure relays (2 years) — assuming the shorter interval covers you is optimistic, and assuming the longer one does is a violation.
- **When troubleshooting requires temporarily defeating a vital circuit, default to a documented, time-boxed alternative method of protection (flagging, restricted speed order) applied before the circuit is defeated, and removed only after the circuit is restored and independently verified** — never leave a vital circuit jumpered "just for a few minutes" without that protection in place first.
- **When a switch heater fails to activate at or above roughly 38°F (3°C) with precipitation present, treat it as an urgent dispatch, not a routine ticket** — a switch that can't fully close due to ice or snow-packed points is a mechanical fail-*open* condition that fail-safe circuit design cannot compensate for, because the hazard is in the steel, not the logic.
- **When a PTC wayside interface unit reports a location as healthy, default to still trusting the location's own 236.56 and switch-point test records over the PTC status alone** — PTC telemetry reflects what the WIU can see, not an independent vital test of the track circuit or switch it's attached to.

## Decision framework

1. **Classify the report as mechanical (switch/point geometry), electrical (track circuit/relay logic), or both** before touching anything — a "switch acting up" ticket that's actually a fouled track circuit wastes a service call adjusting hardware that isn't the problem.
2. **Pull the location's test history**: last shunting-sensitivity test result, last relay test date and type, last switch-point inspection measurement, and any recent track work (surfacing, ballast, rail replacement) that could have disturbed bonding or geometry.
3. **Test the suspect component in place, not on the bench** — a track circuit that shunts correctly with a resistor across the near rail ends may still fail 100 feet into a fouled section; a switch point measured with the switch closed may hide a gap that only opens under load.
4. **If a vital circuit must be defeated to isolate the fault, apply the alternative protection first**, confirm it's in effect, then defeat the circuit — never the reverse order.
5. **Diagnose to the physical cause**, not just to "test now passes" — a relay that tests fine today but is on a documented pitting trend, or ballast resistance that's within spec but trending down, is a scheduled-replacement decision, not a closed ticket.
6. **Restore the circuit, re-verify fail-safe directionality with the same test that found the fault**, and confirm the alternative protection is released only after that re-verification passes.
7. **Log the test result, the physical cause, and the corrective action in the maintenance record** — the next maintainer or an incident investigator needs the trend, not just the day's pass/fail.

## Tools & methods

- **Shunt test box (decade resistance box, calibrated to 0.06 ohm)** for the 236.56 shunting-sensitivity test, applied at multiple points along the track circuit, not only at the signal case.
- **Portable ballast resistance test set** to measure rail-to-rail leakage resistance in ohms per 1,000 feet, compared against the section's design minimum — see `references/playbook.md` for the worked comparison.
- **Switch point inspection gauge (60-degree flange-contact-angle gauge)** to assess wheel-climb risk at a worn point, plus a straightedge/feeler gauge for the flat-spot width and depth measurements against the 5/16-inch and 3/16-inch thresholds.
- **Vital relay test set**, used per the manufacturer's adjustment/test procedure and logged against the 236.106 interval for that relay's construction type.
- **Interlocking test plan / mechanical and electric locking test procedure**, executed per 236 Subpart C intervals and documented per route.
- **Megohmmeter (insulation resistance tester)** for cable and bond wire integrity, and a **track circuit analyzer** for signal-to-noise and code-rate verification on coded track circuits.
- **PTC wayside interface unit (WIU) diagnostic terminal**, used to cross-check reported status against the independent vital test, never as a substitute for it.

## Communication style

To the train dispatcher or control-point operator during active work: exact location, exact circuit or switch identifier, and an explicit statement of what protection is in place and what the train movement authority should assume ("track circuit 4200E is out of service, rule XX flag protection in effect, do not rely on signal indication through this territory"). To a signal supervisor or engineer: the test result with the number, not just "passed" or "failed" — a shunt test that barely passed at 0.058 ohm effective margin is a different conversation than one that passed with headroom. To track department counterparts: specific, numeric asks ("ballast resistance at MP 42.3 measured 0.4 ohms per 1,000 feet against a 2-ohm design minimum, request cleaning or renewal before next shunting test"), not general complaints about track condition. To an incident investigator: the full test history and trend, not just the day-of-event snapshot, because a fail-safe system's failure is almost always the end of a trend, not a single event.

## Common failure modes

- **Treating a passed bench test as proof the field installation is fail-safe**, when ballast fouling, bond wire corrosion, or a gapped switch point only shows up under in-place, in-service conditions.
- **Restoring a vital circuit to service without re-running the same test that found the fault**, on the assumption that fixing the visible cause is sufficient.
- **Defeating a vital circuit before alternative protection is confirmed in effect**, under time or traffic pressure — the single most cited procedural root cause in signal-related close calls.
- **Treating PTC wayside status as a substitute for the underlying 236.56 or switch-point test**, rather than as a second, independent layer that still requires its own vital test.
- **Overcorrecting into re-testing everything at the shortest possible interval "to be safe"**, which burns test hours that could go to sections with an actual degrading trend and doesn't change the regulatory requirement either way.
- **Chasing an intermittent complaint as a hardware defect (relay, contact) before ruling out a competing leakage path (ballast, cross-bonding)**, which wastes a service call replacing parts that were never the cause.

## Worked example

**Situation.** A dispatcher reports that the signal governing entry to a 4,000-foot track circuit (territory identifier TC-4200E) has twice shown a clear indication that a following crew flagged as "no train visible, but signal called for the block to be occupied" — an intermittent failure-to-shunt, not a hard failure. The location's last shunting-sensitivity test, six months ago, passed cleanly with the standard 0.06-ohm test shunt applied at the signal case. The section runs through a coal-loading area; ballast resistance was last formally measured 3 years ago.

**Naive read.** The shop test passed six months ago with the code-mandated 0.06-ohm shunt, so the track circuit itself is fine — the two reports are dismissed as crew misidentification of the block, or a relay contact needing cleaning.

**Expert reasoning — check the competing leakage path before touching the relay.**

- *Design assumption:* a commonly used industry design minimum for reliable DC track circuit ballast resistance is 2 ohms per 1,000 feet. For this 4,000-foot section, resistances in parallel along the length combine roughly as the per-1,000-ft value divided by the number of 1,000-ft segments: 2 ÷ 4 = 0.5 ohms total ballast leakage resistance at the design minimum.
- *Field measurement:* a portable ballast resistance test run today at this location, with coal dust visibly packed in the ballast section, measures 0.4 ohms per 1,000 feet — one-fifth the design minimum. Total for the 4,000-foot section: 0.4 ÷ 4 = 0.1 ohms.
- *Margin comparison, not pass/fail:* the required detectable shunt is 0.06 ohms (236.56). At the design-minimum ballast condition, the shunt-to-leakage ratio is 0.06 ÷ 0.5 = 0.12 — the shunt resistance is only 12% of the leakage resistance, so a train's shunt clearly dominates the parallel circuit and diverts current away from the relay reliably. At today's fouled condition, the ratio is 0.06 ÷ 0.1 = 0.6 — the shunt and the leakage path are now the same order of magnitude, so a meaningful fraction of return current takes the ballast leakage path instead of the train's wheel-axle shunt, reducing the voltage drop the track relay sees. Under exactly the wrong combination of rail moisture and train position, the relay can stay picked (clear) when it should drop (occupied) — which reconciles precisely with two reports of a clear indication with no train visible.
- *Why the six-month-old test missed this:* that test applied 0.06 ohms at the signal case on a section whose ballast resistance hadn't been field-verified in three years — it tested the shunt threshold in isolation, not against the leakage path's actual, degraded value. The test passed because it was correctly run against the wrong assumption about ballast condition.

**Corrective action logged to the maintenance record:**

> **TC-4200E — intermittent failure-to-shunt, resolved to root cause.**
> Ballast resistance measured 0.4 ohms/1,000 ft against a 2 ohms/1,000 ft design minimum (5x below target) — coal dust fouling in the ballast section, MP marker on file. Shunt-to-leakage ratio degraded from 0.12 (design minimum) to 0.6 (measured), consistent with the two reported false-clear events. Track circuit placed out of service under flag protection pending ballast cleaning; 236.56 shunting-sensitivity test to be re-run at three points along the section (near, mid, far) after cleaning, not only at the signal case. Recommend ballast resistance measurement added to this section's next scheduled interval rather than left to a 3-year gap, given the coal-loading exposure.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when running a shunting-sensitivity test, a switch-point inspection, or a vital-relay test cycle: filled worksheets with the threshold numbers and test sequences.
- [`references/red-flags.md`](references/red-flags.md) — load when reviewing a trouble ticket, test record, or switch inspection for a gap before signing off.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term of art is being used loosely in a report or test record in a way that changes what was actually verified.

## Sources

- 49 CFR Part 236 (FRA), *Rules, Standards, and Instructions Governing the Installation, Inspection, Maintenance, and Repair of Signal and Train Control Systems* — §236.56 (shunting sensitivity, 0.06-ohm test shunt, most-restrictive-state requirement), §236.106 (vital relay test intervals: 4 years default, 12 months for AC centrifugal type, 2 years for AC vane/DC polar/soft-iron-structure types), §236.109 (time releases and timing relays, 12-month test interval), and Subpart I (Positive Train Control systems, PTC Safety Plan and interoperability requirements) — the governing federal standard for vital signal logic.
- 49 CFR Part 213 (FRA), Track Safety Standards — §213.135 (Switches): functional fit and worn/chipped switch point repair requirement; the field-applied numeric thresholds (5/16-inch flat spot at 3/4-inch depth; 3/16-inch blunt face) are documented in carrier and AAR field inspection standards implementing this requirement.
- FRA Track Safety Symposium presentation, "Switch Point Inspection & Wheel-Climb Derailment Prevention" (B. Kerchof) — the 60-degree flange-contact-angle inspection gauge and its use in assessing wheel-climb risk at worn switch points.
- *Interface Journal*, "Switch Point Derailments: Is it the point or the wheel?" and "Inspection and Analysis of Switch Derailments" — practitioner-level treatment of split-switch-point derailment causes distinct from wheel-defect causes.
- AREMA (American Railway Engineering and Maintenance-of-way Association) Communications & Signals Manual — track circuit design practice, including the 2-ohms-per-1,000-feet ballast resistance design-minimum convention used in the worked example.
- Switch heater industry practice (e.g., nVent Fastrax ArcticSense precipitation-triggered activation at or below roughly 38°F/3°C) — cited as a representative activation threshold; carrier-specific heater control setpoints vary by climate and system.
- No signal-maintainer practitioner has reviewed this file yet — flag corrections or gaps via PR.
