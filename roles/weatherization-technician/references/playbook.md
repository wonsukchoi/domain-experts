# Weatherization Technician Playbook

Filled worksheets for the jobs referenced in SKILL.md. Figures reflect DOE WAP Standard Work Specifications, BPI Combustion Appliance Safety test practice, and ASHRAE 62.2 — the specific program's adopted protocol and the locally adopted code edition always govern over the generic figures below.

## SIR priority-list worksheet (fill against a per-unit budget cap)

1. Run baseline diagnostics (blower door, combustion safety, visual insulation/air-seal survey) and enter into the audit tool (NEAT/MHEA or state-approved equivalent).
2. Record every candidate measure's installed cost and the tool's computed SIR.
3. Flag any measure that is health-and-safety mandatory regardless of its SIR (combustion-safety fix, electrical hazard correction) — these fund from the same cap but don't compete on SIR.
4. Sort remaining measures by SIR, descending.
5. Fund top-down: mandatory H&S measures first, then SIR-ranked measures in order, running cumulative cost against the cap.
6. Stop funding at the first measure that would push cumulative cost over the cap, even if a lower-cost, lower-SIR measure further down the list would technically still fit — the ranked order is the funding order, not a bin-packing optimization.
7. Any measure with SIR < 1.0 is excluded outright, regardless of remaining budget headroom, unless it is independently H&S-mandatory.

**Filled example (1,400 sq ft home, $6,500 cap — see SKILL.md worked example for the full test detail):**

| Rank | Measure | Cost | SIR | Cumulative | Funded? |
|---|---|---|---|---|---|
| — | Water heater vent/duct sealing (CAZ fix) | $500 | n/a (H&S-mandatory) | $500 | Yes |
| 1 | Air sealing | $650 | 4.2 | $1,150 | Yes |
| 2 | Programmable thermostat | $120 | 3.5 | $1,270 | Yes |
| 3 | Attic insulation R-11→R-38 | $1,850 | 2.1 | $3,120 | Yes |
| 4 | Wall cavity dense-pack | $2,400 | 1.3 | $5,520 | Yes |
| 5 | Storm windows | $3,000 | 0.6 | — | No (SIR < 1.0) |

Total funded: $5,520 of $6,500 (85% of cap used).

## Combustion safety test sequence (run before work starts, and again after any measure that changes house air-leakage or CAZ pressure)

1. **Ambient CO check.** Measure ambient CO in the combustion appliance zone and living space with a calibrated CO analyzer before firing any appliance. Sustained ambient CO above roughly 9 ppm (the level ASHRAE- and EPA-referenced guidance treats as a caution threshold for extended occupant exposure) is itself a flag independent of the appliance tests below.
2. **Worst-case depressurization setup.** Close all exterior doors and windows, turn on every exhaust fan, clothes dryer, and any air handler that can depressurize the house (per BPI/NCI worst-case test protocol), with the combustion appliance(s) under test initially off.
3. **CAZ pressure reading.** With worst-case conditions running, measure the combustion appliance zone's pressure relative to outdoors with a manometer. A naturally-drafted, Category I appliance sharing a flue commonly fails this test at depressurization beyond roughly -5 Pa (0.02 in. w.c.) under the protocol in use — treat any reading at or beyond the adopted protocol's stated limit as a fail requiring mitigation before the appliance is left in atmospheric-vent service.
4. **Draft and spillage.** Fire the appliance under worst-case conditions; confirm draft establishes (commonly within 60 seconds) and hold a mirror or smoke source at the draft hood relief opening for 5 minutes to confirm no spillage. Spillage at any point in that window is a fail.
5. **Appliance CO.** With draft established, sample flue gas CO at the draft hood. Elevated or climbing CO with an otherwise-passing draft/spillage result still warrants appliance service before certifying the zone safe.
6. **Mitigation on fail.** Options in order of preference: reduce the depressurization (duct sealing correction, dedicated makeup-air path), convert the appliance to sealed-combustion or direct-vent (removes CAZ dependency entirely), or, as a last resort, disconnect and red-tag the appliance until a qualified mitigation is installed — never leave a failed test uncorrected and the job marked complete.
7. **Retest after any pressure-changing measure.** Repeat steps 2–5 after air sealing, duct sealing, or any other measure in scope that changes the CAZ's pressure boundary — the pre-work pass does not carry forward.

## ASHRAE 62.2 whole-house mechanical ventilation worksheet

1. Trigger check: if the post-work CFM50 reduction from baseline meets or exceeds the program's ventilation-assessment trigger (commonly ≥20%), run this worksheet before closeout; otherwise document the trigger check as not met and skip.
2. Compute required continuous ventilation: `Qfan (CFM) = 0.03 × conditioned floor area (sq ft) + 7.5 × (bedrooms + 1)`.
3. Estimate whether post-work natural infiltration alone still supplies adequate air exchange, using the house's post-work ACH50 and the program's stated infiltration-credit range (the specific offset factor and floor ACH50 vary by program guidance — apply the adopted version, not a generic assumption).
4. If infiltration alone falls short of the program's adequacy floor, add continuous or intermittent mechanical ventilation (bath/kitchen exhaust rated and controlled to meet the computed CFM, or a dedicated fresh-air supply) to scope and fund it inside the per-unit budget like any other measure.
5. If infiltration alone is assessed adequate, document the calculation and the "no fan added" determination in the job file — a program monitor will look for this worksheet on any job with a large CFM50 reduction, not just a final blower-door number.

**Filled example (1,400 sq ft, 3 bedroom, post-work 15.3 ACH50 — see SKILL.md worked example):**
`Qfan = 0.03 × 1,400 + 7.5 × 4 = 42 + 30 = 72 CFM` required. Post-work 15.3 ACH50 assessed adequate under this program's infiltration-credit guidance; no fan added, calculation documented in the job file.
