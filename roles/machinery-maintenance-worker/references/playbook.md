# Playbook

Filled worksheets a route worker actually runs, not descriptions of them — adapt the numbers to the point in front of you.

## 1. Duty-cycle-adjusted relube interval worksheet

Start from the OEM/nameplate baseline interval (usually stated in operating hours for a "normal duty" environment — light contamination, ambient temperature, no shock load). Apply one multiplier per adverse factor actually present; multipliers compound.

| Adverse factor present | Threshold that triggers it | Multiplier |
|---|---|---|
| Normal duty (none of the below) | — | 1.0 |
| Elevated ambient/housing temperature | >150°F (65°C) at the bearing | ×0.5 |
| Heavy contamination (dust, moisture, washdown) | Visible dust/moisture ingress at seal or housing | ×0.5 |
| Shock load / vibration-prone mounting | Known impact loading or mounted on a vibrating structure | ×0.3 |
| Continuous/near-continuous duty | >16 hr/day operation | ×0.7 |

**Example — conveyor drive motor NDE bearing, corrugate-dust environment, 20 hr/day:**

1. OEM baseline: 2,000 operating hours.
2. Adverse factors present: heavy contamination only (×0.5). Not shock-loaded, not over 150°F at baseline.
3. Effective interval: 2,000 × 0.5 = 1,000 hours.
4. Run-hours per week: 20 hr/day × 7 days = 140 hr/week.
5. Calendar interval: 1,000 ÷ 140 ≈ 7.1 weeks — round to **every 7 weeks**, not the OEM's default 90-day (≈12.9-week) calendar schedule, which would let the bearing run to ≈1,800 hours — 80% past the adjusted interval.

If two adverse factors apply (e.g., contamination and continuous duty), multiply both: 2,000 × 0.5 × 0.7 = 700-hour effective interval.

## 2. Grease quantity worksheet

Formula: **G (grams) ≈ 0.005 × D (housing/bearing OD, mm) × B (bearing width, mm)**. This is a per-service shot size, not a "top up until it purges" endpoint — visible purge at a shielded/sealed bearing's seal is itself a sign of over-lubrication, not confirmation of a complete service.

| Bearing OD (mm) | Width (mm) | Calculated grease shot (g) | Approx. household measure |
|---|---|---|---|
| 62 | 15 | ≈4.7 g | ~1 tsp |
| 85 | 19 | ≈8.1 g | ~2 tsp |
| 110 | 27 | ≈14.9 g | ~1 tbsp |
| 150 | 35 | ≈26.3 g | ~1.75 tbsp |

Convert grams to gun strokes using the specific grease gun's rated output per stroke (commonly 1–2 g/stroke for a standard manual gun — check the gun's spec, don't assume). A 15 g shot on a 1.5 g/stroke gun is 10 strokes, not "a few pumps."

## 3. Belt deflection and tension check

Deflection target: **1/64 inch of deflection per inch of span length**, measured at the belt's midpoint under a perpendicular force, then checked against the belt section's force chart — deflection alone confirms geometry, the force reading confirms actual tension.

| Span length | Target deflection | Typical A-section force range (lbf) | Typical B-section force range (lbf) |
|---|---|---|---|
| 24 in | 0.375 in | 4–6 | 6–9 |
| 36 in | 0.5625 in | 5–7 | 7–10 |
| 48 in | 0.75 in | 6–9 | 9–13 |
| 60 in | 0.9375 in | 7–10 | 10–14 |

**Worked check — 36 in span, A-section fan belt:** deflect the belt 9/16 in (0.5625 in) at midspan; gauge should read 5–7 lbf at that deflection. A reading of 3 lbf at correct deflection means the belt is under-tensioned (retension); a reading of 12 lbf means over-tensioned (back off — over-tension shortens bearing life on both pulleys, not just belt life). Glazing or a squeal under load with a force reading inside spec points to a worn/glazed sheave groove, not tension — that's a basic-adjustment-scope call to inspect the sheave, not just retension again.

## 4. Basic-adjustment vs. escalation decision table

| Finding | In scope (correct now) | Out of scope (escalate) |
|---|---|---|
| Belt deflection/force reading off spec, sheave grooves clean | Retension to spec, log before/after reading | — |
| Belt glazed, cracked, or same tension deviation 3 visits running | — | Escalate: possible sheave wear or misalignment |
| Filter ΔP at or past rated change-out spec | Replace with cross-referenced correct part, log old/new ΔP | — |
| Filter housing shows metal debris or unusual residue | — | Escalate: possible internal component wear upstream |
| Sight glass level low, correct oil grade available | Top off to full mark, log quantity added | — |
| Sight glass milky, discolored, or level dropping between visits with no add | — | Escalate: possible seal failure or water ingress |
| Housing temp within own 5-visit baseline band | Log reading, no action | — |
| Housing temp >15°C (27°F) above own baseline, or absolute >180°F (82°C) | — | Escalate with baseline comparison and reading |
| New rattle/growl not present last visit | — | Escalate: describe sound, location, since-when |
| Grease point due per corrected interval, no anomaly | Relube to calculated quantity, log | — |

## 5. PM-compliance tracking example

Track two numbers, not one: **schedule compliance** (points serviced on or before their due date ÷ points scheduled that period) and **escalation closure rate** (escalations resolved within the agreed window ÷ escalations raised). SMRP's Body of Knowledge cites best-in-class PM schedule compliance at roughly 90%+; a facility running 70% compliance with a growing backlog of deferred high-criticality points is a worse position than 85% compliance with only low-criticality deferrals — track *which* points are behind, not just the percentage.

Example weekly rollup for a 60-point route: 57/60 points serviced on schedule (95%) — but the 3 missed are 2 low-criticality lube points (deferred to next week, logged) and 1 high-criticality belt inspection (should have been pulled forward, not left last). The percentage looks fine; the composition doesn't — flag the high-criticality miss to the supervisor even though the headline number clears the 90% bar.
