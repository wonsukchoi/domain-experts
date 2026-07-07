# Playbook

Filled tables and decision sequences per FAA AC 150/5200-18C (self-inspection), the TALPA RCAM (runway condition), AC 150/5200-33C (wildlife), and AC 150/5210-24 (FOD) unless otherwise noted. Apply against the airport's own Airport Certification Manual (ACM), which can set a stricter local baseline than these references.

## 1. Self-inspection frequency by trigger

| Condition | Minimum frequency | Notes |
|---|---|---|
| Baseline, no adverse condition | At least once daily (14 CFR 139.327) | Most Class I (scheduled air-carrier, large aircraft) airports run this closer to hourly-to-several-times-daily per their own ACM; the regulation sets the floor, not the local schedule. |
| Active precipitation (snow/ice/heavy rain) | Continuous or per ACM winter-ops schedule, commonly every 30–60 min | Frequency escalates with contaminant accumulation rate, not on a fixed clock. |
| Active construction in or adjacent to movement area | Before and after each work period, plus routine schedule | Construction is the highest FOD-generation condition; the walk frequency, not just the inspection frequency, escalates with it. |
| Reported or observed wildlife activity | Immediate inspection at time of report, independent of routine schedule | A strike or sighting report is itself a trigger, not something that waits for the next scheduled pass. |
| Pilot-reported braking action worse than published RwyCC | Immediate re-inspection | The report supersedes the last measurement until confirmed or refuted. |

## 2. RCAM contaminant-to-RwyCC table (abbreviated)

| RwyCC | Braking action term | Representative contaminant/condition |
|---|---|---|
| 6 | Dry | Dry pavement, no contamination. |
| 5 | Good | Frost; wet pavement (1/8 in or less standing water). |
| 4 | Good to Medium | Dry snow, wet snow, or slush, any at 1/8 in depth or less. |
| 3 | Medium | Dry or wet snow greater than 1/8 in depth; dry or wet snow of any depth on top of compacted snow. |
| 2 | Medium to Poor | Slush greater than 1/8 in depth. |
| 1 | Poor | Ice (not wet, not slush-covered). |
| 0 | Nil | Wet ice; slush over ice; water on top of compacted snow; dry or wet snow over ice. |

Report per runway third (touchdown/midpoint/rollout), e.g. `3/6/1` — never collapse to a single runway-wide code.

## 3. Stopping-distance margin check (worked-example method, reusable)

1. Get the aircraft's dry required landing distance for the runway in question (from the operator's performance data or a representative value for the fleet using the field).
2. Apply the dispatch contamination factor for the worst reported RwyCC along the aircraft's stopping path (typically the rollout third governs, not touchdown): approximately ×1.15 at RwyCC 3, ×1.3–1.4 at RwyCC 2, ×1.6 at RwyCC 1. [heuristic — operator-specific tables vary; confirm against the actual performance manual before using as a hard cutoff]
3. Subtract from runway length to get absolute margin in feet, then express as a percentage of runway length.
4. Flag for restriction/closure consideration when the margin percentage drops below the airport's locally defined caution threshold (commonly single digits as a percentage), or immediately if the margin goes negative.

## 4. Wildlife Hazard Assessment (WHA) trigger checklist

Any one of the following, per AC 150/5200-33C, triggers a WHA evaluation — not a judgment call:

- [ ] An air-carrier aircraft experiences a wildlife strike causing damage to the aircraft.
- [ ] An air-carrier aircraft experiences an engine ingestion of wildlife, regardless of resulting damage.
- [ ] Wildlife of a species, size, or quantity observed on or near the airport that poses a potential hazard to aircraft operations.
- [ ] A wildlife strike is reported by a pilot or ground observer involving a species known to cause damage elsewhere (per FAA National Wildlife Strike Database history).

Once triggered: WHA conducted (typically by a qualified wildlife biologist) to identify attractants (food, water, cover) and recommend the Wildlife Hazard Management Plan (WHMP) updates — habitat modification first, active dispersal (hazing, depredation permits) as an ongoing supplement, never a one-time substitute.

## 5. FOD find: immediate closure vs. scheduled removal

| Finding | Action |
|---|---|
| Hard object (metal, fastener, luggage/cargo fragment, pavement chunk) anywhere in the movement area | Immediate closure of the affected surface until physically removed and re-inspected. |
| Object of unknown composition/origin | Treat as hard until visually confirmed otherwise — default to closure, not to "probably soft." |
| Soft, non-ingestible debris (paper, vegetation, plastic sheeting) found during a scheduled walk | Log and remove during the same walk; no closure required. |
| FOD-detection system alarm (radar/camera-based) | Physical verification required before clearing the alarm — an unconfirmed alarm is not a resolved alarm. |
| Debris found immediately after a construction work period | Full walk of the affected surface before returning it to service, regardless of whether the routine walk is already scheduled. |

## 6. NOTAM issuance timing

1. Discover/confirm the hazard during inspection.
2. Originate the NOTAM (FDC or Distant, field-condition/FICON format as applicable) within minutes of confirmation — before completing the rest of the inspection route, not after.
3. State a specific next-inspection or expiration time in the NOTAM text, not an open-ended "until further notice."
4. Confirm the NOTAM posted and reads correctly (self-verify, analogous to a controller's hear-back).
5. Cancel or amend only after a re-inspection confirms the hazard is actually resolved — not on the assumption that a mitigation action (plowing, dispersal, removal) worked.
