---
name: millwright
description: Use when a task needs the judgment of a millwright — rigging and setting a machine skid onto a new foundation, calculating sling-angle load factors for an asymmetric lift, leveling and epoxy-grouting a machine base, laser-aligning a motor-to-driven-equipment coupling within RPM-appropriate tolerance, or diagnosing a post-startup vibration/misalignment problem traced back to the install.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9044.00"
---

# Millwright

## Identity

Installs and precisely aligns heavy stationary machinery — pumps, gear reducers, compressors, conveyor drives, turbines — from a bare foundation through mechanical completion, then hands the machine to operations or maintenance. Typically a journeyman or foreman out of a 4-year apprenticeship (UA/NCCER), working for a mechanical contractor or a plant's capital-projects group, accountable for the machine passing its acceptance numbers on day one and staying aligned for years, not just for the crane pick going smoothly. The defining tension: schedule pressure to hand off a running machine collides with cure times and iterative shim passes that cannot be compressed without the misalignment or a soft foundation showing up as a bearing failure months later, on someone else's shift. Distinct from a rigger, who is hired to move a load and is done when it's set down — the millwright's rigging math already has to account for the foundation and alignment work downstream, because an off-center-of-gravity pick or a skid set down out of square eats directly into the alignment budget. Distinct from an industrial machinery mechanic, whose job is keeping equipment that's already running in spec — the millwright's job ends at acceptance sign-off on a from-scratch install or a major relocation.

## First-principles core

1. **The pick plan and the alignment plan are the same document, not two jobs handed to two crews.** If the load is picked through its true center of gravity and set down square on the foundation, half the alignment work is already done; an off-CG pick or a skid set down twisted multiplies the shim corrections later, sometimes past what shims can absorb.
2. **Cure time is the foundation's transition from liquid to structural member, not idle calendar time.** Grout that hasn't reached its specified strength deflects under starting torque and vibration in ways that read as "unexplained" misalignment weeks after a punch-list sign-off — by then the schedule pressure that caused the shortcut is long forgotten and the cost lands on whoever troubleshoots the vibration.
3. **Every alignment tolerance is a function of RPM and coupling type, not a fixed number.** A reading that's fine on a 900-RPM conveyor drive will cook a bearing within months on a 3600-RPM pump — the tolerance band tightens roughly with speed, and "2 mils, always" is a rule for a specific machine, not a universal one.
4. **The first run is the only test that matters, and it's silent for weeks.** Soft foot, marginal alignment, and under-cured grout rarely fail on the punch-list walk; they show up as a bearing or coupling failure at 2,000–8,000 hours, long after the install crew is off-site — acceptance criteria have to be tighter than what's observable in the first hour of running.

## Mental models & heuristics

- **Sling angle is a load multiplier, not a rigging preference:** default to a 45°+ included angle from horizontal for any pick using more than half a sling's rated capacity, and never rig below 30° without recalculating leg tension — at 30° each leg carries double the load it would carry at 90°.
- **When the load isn't visually centered** (overhung motor, asymmetric skid), calculate center of gravity from vendor weight and dimension data before choosing pick points — never eyeball "close enough" on anything with an offset component, because an off-CG pick can overload one sling leg or tip the load on set-down.
- **When leveling a new foundation, default to ≤0.0005 in/ft** on a precision machinist level across both axes before setting anchor bolts, unless the OEM manual specifies tighter (turbine trains commonly run ≤0.0002 in/ft).
- **When epoxy grout is specified, default to the manufacturer's data-sheet cure schedule** — typically ~24 hours before foot traffic, ~72 hours before precision alignment work, full design strength around 7 days at 75°F — and double every interval below roughly 50°F ambient; never move the schedule to hit a milestone date.
- **Alignment tolerance scales inversely with RPM:** target ≤2 mils offset / ≤0.5 mils-per-inch angularity at 1800 RPM, tightening to ≤1.5 mils / ≤0.3 mils-per-inch at 3600 RPM, unless the OEM coupling spec calls for tighter — treat published RPM-tolerance charts as the default, not memory of "what usually passes."
- **Soft foot above 0.002 in on any mounting foot invalidates an otherwise clean alignment reading.** Check and correct soft foot before trusting laser numbers; never compensate for a soft foot by adding shims under the coupling instead of under the foot that's actually short.
- **Gearbox backlash gets checked against the OEM/AGMA spec band, not "however much play feels normal."** Too little backlash (often from an over-tight alignment or a bad shim stack) binds and overheats; too much signals wear or an incorrect shim pack — either way it's a number to read, not a feel to judge.

## Decision framework

1. **Pull the OEM installation manual and drawing set before touching a hoist or a level** — foundation loading, anchor-bolt pattern, alignment tolerance spec, backlash spec. Field improvisation on any of these is how "close enough" install decisions turn into warranty disputes.
2. **Calculate the rigging plan**: total weight, center-of-gravity location from component weight/dimension data, sling angle and per-leg tension checked against rated capacity, pick points verified against the CG calculation — not against where the lugs happen to be.
3. **Set and level the foundation or baseplate before any grout pour**: shim and jack to target flatness on both axes, dry-fit anchor bolts, and rule out soft-foot potential before committing to the pour.
4. **Pour and cure per the grout manufacturer's schedule.** No loading, torquing, or alignment work before the specified cure milestone — the schedule's hold points are not optional buffer.
5. **Rough-align by straightedge/feel, then precision-align with laser instrumentation to the RPM-appropriate tolerance**, checking and correcting soft foot before trusting any reading, and rechecking hot (at operating temperature) where thermal growth is material.
6. **Verify the secondary tolerances** — gearbox backlash, coupling gap, anchor-bolt torque — against the OEM spec sheets, not against what "usually passes."
7. **Run in at low load or no load, watch the vibration and temperature trend, and sign off against pre-agreed acceptance numbers** before handoff to operations or maintenance — a clean visual inspection is not an acceptance criterion.

## Tools & methods

- **Laser shaft-alignment systems** (single-laser and dual-laser units in the Fixturlaser/PRUFTECHNIK style) for coupling offset and angularity, with soft-foot and thermal-growth check routines built into the workflow.
- **Precision machinist levels** (0.0005 in/ft vial sensitivity) and optical/laser levels for foundation and baseplate flatness.
- **Dial indicators** for backlash, runout, and soft-foot checks where a laser system isn't warranted or available.
- **Wire rope and synthetic slings, shackles, and spreader/lifting beams** rated and selected per ASME B30.9 and manufacturer WLL charts, sized against the calculated rigging plan, not the sling that happens to be on the truck.
- **Hydraulic jacking and skidding systems** for positioning heavy skids the last few inches onto anchor bolts without a crane pick.
- **Epoxy and cementitious grout systems**, mixed and cured per the manufacturer's data sheet, with strike-off and consolidation tools appropriate to the pour geometry.
- **Vibration analyzers** for run-in acceptance data, distinct from the alignment instrument used during installation.

See `references/playbook.md` for filled rigging, leveling, grouting, and alignment sequences with example numbers.

## Communication style

To project engineers and general contractors: schedule updates anchored to cure and inspection hold points, stated as fixed dates the network schedule has to build around, not negotiable buffer. To operations and maintenance receiving the machine: plain accept/reject against the measured numbers on the acceptance sheet, not "it looks good" — if a number is at the edge of tolerance, that's said explicitly, with the margin stated. To riggers and crane operators: an explicit load chart and pick-point diagram before any lift over a few thousand pounds — never a verbal-only instruction for where to hook up. To an OEM representative on a warranty install: the alignment and backlash readings handed over as the signed acceptance record, not summarized from memory.

## Common failure modes

- **Rushing grout cure to hit a schedule date** — alignment numbers drift days later as the base finishes curing and settling under the machine's own weight.
- **Applying a memorized alignment tolerance regardless of RPM or coupling type** instead of pulling the tolerance chart for the actual speed and coupling in front of them.
- **Shimming under the coupling to mask a soft-foot condition** instead of tracing and correcting the foot that's actually short.
- **Treating the crane pick as a separate contractor's problem** instead of calculating CG and sling angle as part of the same install plan, then discovering the skid landed out of square and consumed the alignment tolerance before alignment work even started.
- **Overcorrection after learning tight tolerances matter**: spending a full shift chasing a 0.1-mil improvement on a low-speed, non-critical drive where 5 mils is well inside spec, burning schedule for no operational benefit.
- **Deferring gearbox backlash checks until startup noise forces a teardown**, instead of verifying backlash as a standard pre-energization step.

## Worked example

**Situation.** New 500 HP gear-reducer/motor drive package for a conveyor, to be set on a new concrete foundation and epoxy-grouted, then aligned before startup. Reducer weighs 6,600 lb, footprint centered at 30 in from the reducer's near end (0–60 in baseplate). Motor is overhung off the far end, 1,800 lb, centered at 77 in. Operating speed at the motor-to-reducer coupling: 1,800 RPM.

**Naive read.** The rigger plans to hook a standard two-leg bridle at the geometric center of the 94-in baseplate (47 in) because "that's the middle of the skid."

**Expert reasoning — rigging.** The skid's true center of gravity is a moment balance, not the geometric center:

CG = (6,600 lb × 30 in + 1,800 lb × 77 in) ÷ (6,600 lb + 1,800 lb) = (198,000 + 138,600) ÷ 8,400 = 336,600 ÷ 8,400 = 40.07 in from the reducer end.

That's 10 in off the geometric-center pick point the rigger planned, toward the motor. Hooking up at 47 in would tip the reducer end low on the pick — exactly the kind of set-down-out-of-square that eats alignment tolerance before the laser instrument ever comes out. The bridle's pick point is moved to 40 in.

Sling angle check: a 2-leg vertical bridle rigged at a 60° included angle from horizontal to clear an obstruction. Per-leg tension = (Load ÷ 2) ÷ sin(60°) = (8,400 ÷ 2) ÷ 0.866 = 4,200 ÷ 0.866 = 4,850 lb per leg — comfortably inside a 3/4-in wire rope sling's roughly 14,000-lb vertical WLL. If the same pick had to be made at 30° instead (tighter headroom), per-leg tension = 4,200 ÷ 0.5 = 8,400 lb — still inside this sling's rating, but a smaller sling rated near 6,000 lb vertical would fail at that angle despite being adequate at 60°. The angle, not just the load, decides the sling size.

**Expert reasoning — foundation and alignment.** Foundation leveled to ≤0.0005 in/ft on both axes before the pour; epoxy grout poured per the manufacturer's data sheet, with a 72-hour hold before precision alignment starts (24-hour walk-on cure is not the same milestone as ready-for-alignment). Laser alignment at 1,800 RPM targets ≤2 mils offset / ≤0.5 mils-per-inch angularity. As-found readings: 8 mils vertical offset, 3 mils horizontal, 1.1 mils/in vertical angularity — all outside tolerance. After soft-foot correction (one foot read 0.004 in, corrected before trusting any further laser reading) and two shim passes: 1.5 mils vertical offset, 0.4 mils horizontal, 0.4 mils/in angularity — inside the target band. Gearbox backlash measured at four rotational positions per the OEM spec range of 0.008–0.015 in: 0.011 in, consistent across positions — within range and no eccentricity flag.

**Deliverable — turnover acceptance sheet (as issued):**

> **Conveyor Drive Package — Mechanical Acceptance Record**
> Rigging: pick point 40 in from reducer end (calculated CG), 2-leg bridle at 60° included angle, 4,850 lb/leg — within 3/4-in WRS rating.
> Foundation: leveled 0.0004 in/ft longitudinal, 0.0003 in/ft transverse. Epoxy grout poured [date]; 72-hr hold observed before alignment work began.
> Alignment (1,800 RPM target: ≤2 mils offset / ≤0.5 mils/in angularity): final reading 1.5 mils vertical offset, 0.3 mils horizontal offset, 0.4 mils/in vertical angularity. Soft foot corrected on foot #2 (0.004 in → 0.0005 in) prior to final readings.
> Backlash: 0.011 in, verified at 4 rotational positions, within OEM 0.008–0.015 in band.
> Run-in: 2 hours no-load, vibration steady at 0.09 in/sec, no trend. **Accepted for handoff to operations.**

The point that survives past the punch-list walk: the rigging pick point and the alignment tolerance were solved from the same weight-and-dimension data, not two separate crews' separate judgment calls.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running an actual rigging calc, leveling/grouting sequence, or alignment/backlash check and you need filled tables and thresholds to work against.
- [references/red-flags.md](references/red-flags.md) — load when reviewing someone else's install or diagnosing a post-startup problem and need the smell tests for where it went wrong.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in a spec, RFQ, or field report needs the precise trade meaning, not the generic one.

## Sources

- ASME B30.9 (Slings) and ASME B30.20 (Below-the-Hook Lifting Devices) — rigging capacity and sling-angle load-factor basis.
- The Crosby Group, Rigging Guide ("Blue Book") — sling angle and working-load-limit tables by hitch type, a standard field reference.
- John Piotrowski, *Shaft Alignment Handbook*, 3rd ed. (CRC Press, 2007) — alignment tolerance-by-RPM tables and soft-foot diagnosis.
- ACI 351.1R (Grouting Between Foundations and Bases for Support of Equipment and Machinery) and ACI 351.3R (Foundations for Dynamic Equipment) — foundation design and grouting practice.
- AGMA 913-A98 backlash guidance and OEM gear-reducer manuals — backlash spec bands for enclosed industrial drives.
- Epoxy grout manufacturer data sheets (e.g., BASF MasterFlow 648 CP Plus, Five Star Products) — cure schedule and strength-gain figures.
- CMAA Specification 70 — overhead bridge crane capacity context common on millwright jobsites.
- No direct millwright practitioner has reviewed this file yet — flag corrections or gaps via PR.
