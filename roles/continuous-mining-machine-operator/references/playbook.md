# Continuous Mining Machine Operator — Playbook

Filled reference sequences: cut-tonnage/haulage-matching calculation, methane action-level response, roof-sounding and cut-depth tracking, and permissibility check.

## 1. Cut-tonnage and haulage-matching calculation

Use this to determine whether a shift's production shortfall traces to cutting rate or to haulage — the two most commonly confused causes.

| Input | Typical range | Source/note |
|---|---|---|
| In-place coal density | 75–90 lb/cf (bituminous) | Hartman & Mutmansky; confirm against site-specific seam data — this varies by rank and ash content |
| Continuous miner cutting/loading rate | 3–6 tons/min | stated illustrative range for a modern drum miner; confirm against OEM spec for the specific machine |
| Shuttle car rated capacity | 8–15 tons | site fleet spec |
| Target tram distance before haulage becomes the bottleneck (2-car fleet) | roughly under 400–500 ft | derived from the worked calculation below; longer tram distances need a third car or continuous haulage to keep pace |

**Working steps:**

1. Calculate cut volume: entry width (ft) × seam height (ft) × cut depth (ft, capped by the roof control plan).
2. Convert to tons: volume (cf) × density (ton/cf, from lb/cf ÷ 2,000).
3. Divide tons per cut by the miner's cutting rate (tons/min) to get the cutting-rate-limited time per cut.
4. Calculate each shuttle car's load time: car capacity (tons) ÷ miner's cutting rate (tons/min), since the car fills at the miner's discharge rate.
5. Calculate each car's non-load segment: tram out (loaded) + dump + tram back (empty), from measured or estimated tram speed and distance.
6. Compare load time (step 4) to non-load segment (step 5) for a 2-car alternating fleet: if non-load segment exceeds load time, the miner idles for the difference after every load — that idle time is the haulage penalty.
7. Recalculate delivery rate as car capacity ÷ (load time + idle gap, or non-load segment if greater) and compare against the miner's raw cutting rate — the lower of the two governs actual production.
8. Report the gap between cutting-rate-limited and haulage-limited shift tonnage, with the specific lever (car count, tram distance, dump-point congestion) driving it — see the worked figures in SKILL.md's Worked example section for a full derivation.

## 2. Methane action-level response sequence (30 CFR §75.323)

| Reading (CH4 by volume) | Required action |
|---|---|
| Below 1.0% | Normal operation; continue monitoring trend, not just point reading |
| At or above 1.0% | De-energize all electric equipment in the affected area except the methane monitor circuit; increase ventilation; do not resume power until below 1.0% |
| At or above 1.5% | Withdraw all persons from the affected area except those needed to eliminate the hazard |
| At or above 2.0% (at the machine-mounted monitor) | Automatic machine shutoff triggers per the on-board monitor's required cutoff |

**Working steps:**

1. Confirm the current reading source (fixed on-board monitor vs. handheld) and its calibration status before treating a reading as reliable.
2. At 1.0% or above: de-energize per the table, notify the section foreman by location, and do not restart until a confirmed reading below 1.0% is obtained — not "it dropped for a second."
3. At 1.5% or above: execute withdrawal for all non-essential personnel; only trained personnel addressing the hazard remain.
4. Log the reading, time, location, and action taken in the on-shift examination record immediately, not at end of shift.
5. After returning below threshold, re-verify with a second reading before resuming normal cutting — a single passing reading right after a high reading can reflect transient dilution, not resolution of the source.

## 3. Roof-sounding and cut-depth tracking

**Cut-depth tracking:**

1. Zero the advance counter (or mark the measurement point) at the last row of installed permanent roof support before starting a new cut.
2. Track cumulative sump + shear depth against the roof control plan's stated limit for this section (commonly 20 ft without a mounted temporary roof support system; up to 40 ft with an MSHA-approved one — confirm the specific number in this section's plan, not a general figure).
3. Stop cutting and call for bolting once the plan's limit is reached, regardless of how the roof currently looks or how far ahead cutting could physically continue.
4. Do not resume cutting past the bolted line until the bolt crew has completed and signed off the current row.

**Roof sounding:**

1. At each newly exposed section of roof, strike it with a sounding bar at multiple points across the width, not just center.
2. A solid, ringing tone indicates competent, well-bonded roof; a hollow or dull ("drummy") tone indicates a separation or void above the immediate roof line.
3. On a drummy result: stop cutting/bolting at that location, flag it in the on-shift record with the specific location, and get a roof-control assessment before continuing — do not substitute a visual look for the sounding result.
4. Re-sound after any nearby blasting, heavy equipment vibration, or a multi-shift gap since the area was last checked — roof conditions can change between exposure and bolting.

## 4. Permissibility check

1. Before starting a shift, visually inspect all explosion-proof enclosures, cable connections, and bolted housings on the machine for cracks, missing bolts, or damage.
2. Any defect found — regardless of severity — makes the machine non-permissible immediately; log it in the on-shift examination record with the specific component and defect.
3. In a heading with any current or recent methane potential, stop production and do not restart until the defect is repaired and the machine is confirmed permissible again — do not defer to a scheduled maintenance window.
4. In a heading confirmed free of methane potential by current readings, a defect still requires prompt correction; "no gas right now" is not a basis for extended deferral, since conditions can change with the next cut.
5. Document the repair and the re-inspection that confirmed permissibility before returning the machine to service in any gassy heading.
