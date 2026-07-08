# Playbook

Filled worked calculations for the artifact types this role produces most often: a cutoff-grade determination with grade-tonnage reconciliation, an RMR/Q-based ground support design, and a ventilation quantity calculation. Populate with the actual project's numbers; the structure and arithmetic below are real and reconcile.

## Cutoff grade — mill-limiting vs. mine-limiting (Lane's framework)

**Deposit:** copper porphyry. Metal price $4.00/lb Cu. Metallurgical recovery 88%. Smelter payability 96% of contained Cu, treatment/refining charge (selling cost) $0.15/lb payable Cu. Mining cost $2.20/t mined. Processing cost $8.50/t milled. G&A $1.80/t milled.

**Step 1 — recoverable value per unit grade.** 1% Cu in 1 tonne of ore = 22.0462 lb Cu (1 t = 2,204.62 lb). Net payable price = ($4.00 × 0.96) − $0.15 = $3.84 − $0.15 = **$3.69/lb payable**. Value per tonne per 1% grade, after recovery: 22.0462 lb/t × 0.88 recovery × $3.69/lb = **$71.63 per tonne per 1% Cu**.

**Step 2 — mill-limiting (marginal) cutoff.** Material is already broken; the only decision is mill vs. waste dump, so only incremental costs count: processing $8.50 + G&A $1.80 = **$10.30/t**.

g_mill = $10.30 / $71.63 per %·t = **0.144% Cu** — round to 0.14% Cu for the mill/waste-dump decision.

**Step 3 — mine-limiting (full-cost/breakeven) cutoff.** For long-range planning and reserve conversion, mining cost is also incremental (the choice is whether to move the material at all): $2.20 + $8.50 + $1.80 = **$12.50/t**.

g_mine = $12.50 / $71.63 = **0.174% Cu** — round to 0.17% Cu for reserve/pit-limit definition.

**Deliverable — cutoff-grade memo line:** "Apply 0.14% Cu as the mill/waste-dump cutoff on already-mined material for the remainder of FY; apply 0.17% Cu as the reserve-definition cutoff for the FY+1 pit-limit re-optimization. Re-run both if Cu price moves outside $3.60–$4.40/lb or processing cost moves >10% from the $8.50/t basis."

## Grade-tonnage curve — reading it against the chosen cutoff

| Cutoff (% Cu) | Tonnes above cutoff (Mt) | Avg grade above cutoff (% Cu) | Contained Cu (kt) |
|---|---|---|---|
| 0.10 | 450 | 0.32 | 1,440 |
| 0.15 | 320 | 0.38 | 1,216 |
| 0.20 | 210 | 0.46 | 966 |
| 0.30 | 95 | 0.61 | 580 |
| 0.40 | 40 | 0.78 | 312 |

Contained metal reconciles as tonnage × grade: 320 Mt × 0.0038 = 1,216,000 t = 1,216 kt; 210 Mt × 0.0046 = 966,000 t = 966 kt; 95 Mt × 0.0061 = 579.5 kt ≈ 580 kt; 40 Mt × 0.0078 = 312 kt.

Moving the cutoff from 0.10% to 0.17% (the mine-limiting cutoff derived above, interpolated between the 0.15 and 0.20 rows) trades roughly 40–50% of tonnage for a materially higher average grade — the standard shape of a grade-tonnage curve, and the reason cutoff grade is a scheduling lever, not just a reserve-reporting formality: a higher cutoff front-loads higher-grade, lower-tonnage years.

## Ground support — RMR (Bieniawski) and Q-system cross-check, bolt design

**Given:** a 6 m span underground drift in a fractured metasediment domain. Field/lab data: intact UCS = 90 MPa; RQD = 68%; average discontinuity spacing = 0.4 m; joint condition: slightly rough, slightly weathered, 1–3 mm separation; groundwater: damp.

**Step 1 — RMR (Bieniawski 1989) rating.**

| Parameter | Measured value | Rating |
|---|---|---|
| UCS | 90 MPa | 7 |
| RQD | 68% | 13 |
| Discontinuity spacing | 0.4 m | 10 |
| Discontinuity condition | slightly rough/weathered, 1–3 mm | 20 |
| Groundwater | damp | 7 |
| **RMR (sum)** | | **57** |

RMR = 57 → **Class III, "Fair rock."** Per Bieniawski's empirical support chart for a similar-span opening in Class III ground: systematic rock bolts (fully grouted, 20 mm dia.), 1.5–2 m spacing in crown and walls, plus 50–100 mm shotcrete in the crown, mesh where block sizes warrant it.

**Step 2 — Q-system cross-check.** Q parameters for the same domain: RQD = 68, Jn = 9 (three joint sets), Jr = 1.5 (rough, undulating), Ja = 1.0 (unaltered walls, staining only), Jw = 1.0 (dry to damp excavation), SRF = 1.0 (low stress, near-surface).

Q = (RQD/Jn) × (Jr/Ja) × (Jw/SRF) = (68/9) × (1.5/1.0) × (1.0/1.0) = 7.556 × 1.5 = **11.33** — "good rock" on the Q scale.

**Cross-check via the Bieniawski correlation:** RMR ≈ 9·ln(Q) + 44 = 9 × ln(11.33) + 44 = 9 × 2.427 + 44 = 21.84 + 44 = **65.8**, versus the directly rated RMR of 57 — a gap of about 9 points, within the correlation's normal scatter but on the high side; worth a second look at whether the groundwater or joint-condition rating was scored consistently between the two systems before finalizing the support class.

**Step 3 — bolt length from Q (Barton/Grimstad-Barton relation).** L = 2 + 0.15B/ESR, with span B = 6 m and ESR (Excavation Support Ratio) = 1.6 for a permanent mine opening (Barton's ESR table):

L = 2 + (0.15 × 6) / 1.6 = 2 + 0.9/1.6 = 2 + 0.5625 = **2.56 m** — round up to a practical **3.0 m** bolt.

**Deliverable — ground support spec (as issued):** "Domain GD-3, 6 m span drift: RMR 57 (Class III, Fair), Q 11.33 (Good) — support governed by the RMR empirical chart given the discrepancy noted above. Systematic 20 mm fully grouted rebar, 3.0 m length (Q/ESR-derived), 1.5 m × 1.5 m pattern in crown and upper walls. 75 mm fiber-reinforced shotcrete, crown only. Re-classify at every domain boundary; do not carry this pattern past a mapped structural discontinuity without a separate kinematic check."

## Ventilation quantity — diesel-equipment-governed heading

**Given:** a development heading, cross-section 5 m wide × 5 m high (25 m² = 269.1 ft², using 1 m² = 10.764 ft²). Crew of 6 persons working the face. Equipment operating simultaneously in the same split: one diesel LHD (300 bhp), one diesel haul truck (400 bhp).

**Step 1 — person-based minimum.** 6 persons × 100 cfm/person (metal/nonmetal minimum airflow practice per 30 CFR §57.5015) = **600 cfm**.

**Step 2 — diesel-equipment-based minimum.** 100 cfm per rated bhp × (300 + 400) bhp = 100 × 700 = **70,000 cfm**.

**Step 3 — governing quantity.** max(600, 70,000) = **70,000 cfm** — equipment-governed, as is the near-universal case in a mechanized heading; the person-based minimum almost never binds once diesel equipment is present.

**Step 4 — required face velocity.** Velocity = Q / A = 70,000 cfm / 269.1 ft² = **260 fpm** (1.32 m/s) — well above the practical minimum face velocity (commonly 30–60 fpm for adequate mixing/dilution) used as a lower-bound sanity check, confirming the quantity, not just the total volume, is adequate for this cross-section.

**Step 5 — fan duty with system leakage.** Underground duct/regulator leakage commonly reduces delivered air to 60–70% of what a fan produces; applying a 65% delivery efficiency factor: fan duty = 70,000 cfm / 0.65 = **107,700 cfm** required at the fan to deliver 70,000 cfm to the face.

**Deliverable — ventilation plan line item:** "Heading DH-12: required face airflow 70,000 cfm (diesel-equipment-governed, 700 bhp combined LHD + haul truck), face velocity 260 fpm at the 5 m × 5 m cross-section. Specify fan duty of at least 107,700 cfm at 65% assumed system delivery efficiency; re-verify delivery efficiency by anemometer survey at commissioning and adjust regulator settings if measured face airflow falls below 70,000 cfm."
