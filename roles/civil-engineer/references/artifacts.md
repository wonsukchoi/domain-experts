# Civil engineering artifacts — templates with real structure

Filled examples for the 3.2-acre commercial site development referenced in `SKILL.md`'s worked example. Numbers are illustrative and internally consistent with that example; treat unit systems, ordinance thresholds, and code editions as jurisdiction-specific inputs to swap out, not fixed values.

## 1. Stormwater drainage report — calc package skeleton

**Cover block (every report):** project name/address, jurisdiction and adopted stormwater ordinance edition, design storm(s) required (commonly 2-yr, 10-yr, 25-yr, and 100-yr for the primary/emergency system split), hydrology method used and why, engineer of record and stamp block, revision log.

**Section A — Hydrology inputs**

| Parameter | Pre-development | Post-development |
|---|---|---|
| Drainage area | 3.2 ac | 3.2 ac |
| Land cover | Wooded/pasture | 70% impervious (roof, pavement) |
| Runoff coefficient (C) | 0.30 | 0.85 |
| Time of concentration (tc) | 20 min (overland sheet flow) | 10 min (curb/gutter + storm pipe) |
| Rainfall intensity, 10-yr (i) | 6.0 in/hr | 7.5 in/hr |
| Peak flow, rational method (Q=CiA) | 5.76 cfs | 20.4 cfs |

**Section B — Detention requirement**

- Allowable release rate: pre-development 10-yr peak = 5.76 cfs (per [Jurisdiction] Stormwater Ordinance §4.2, matching pre- to post-development peak for the 2-, 10-, and 25-yr storms).
- Critical storm duration for storage sizing: post-development tc = 10 min → triangular hydrograph base = 2×tc = 20 min.
- Required active storage: 0.5 × (Q_post − Q_pre) × base(hr) × 3,600 = 0.5 × (20.4 − 5.76) × 0.333 × 3,600 = **8,780 ft³**.
- Provided storage: Basin DB-1, 5,500 ft² footprint × 1.6 ft average depth = **8,800 ft³**. Margin: +0.2%, essentially exact — flag for a second reviewer if margin exceeds ±15% in either direction (too tight = no construction tolerance; too loose = usually a units or duration error).
- Freeboard: 1.0 ft above routed 100-yr WSEL (El. 412.3 → basin rim El. 413.3 minimum).
- Emergency spillway: sized independently for the 100-yr, 24-hr event (NRCS Type II distribution), invert set at the 1.0 ft freeboard elevation, riprap-lined, minimum 3:1 side slopes.

**Section C — Outlet structure**

| Component | Value |
|---|---|
| Control structure type | Riser with orifice plate |
| Orifice diameter | 8 in, centered at El. 409.0 |
| Discharge at design head (2.5 ft) | 5.7 cfs (within 1% of 5.76 cfs target — acceptable) |
| Trash rack | Yes, clear opening ≥ 2× orifice area |
| Low-flow/2-yr control | Secondary 3 in orifice at El. 408.2 |

**Section D — Conclusion (stamped language)**

> "Detention Basin DB-1 provides 8,800 ft³ of active storage against a calculated requirement of 8,780 ft³ for the 10-year, 20-minute critical duration storm, releasing at a controlled rate of 5.76 cfs. Basin includes 1.0 ft of freeboard above the routed 100-yr WSEL and an emergency spillway sized independently for the 100-yr, 24-hour event. This analysis assumes the tributary drainage area and land cover shown on Sheet C-201; any change to tributary area, imperviousness, or upstream contribution requires re-analysis before construction."

## 2. Bearing-capacity check memo

**Header:** project, footing ID, date, geotechnical report reference number, engineer of record.

| Item | Value | Source |
|---|---|---|
| Footing | F-3, interior column | Structural drawing S-301 |
| Applied load (DL + LL) | 165 kips | Structural load takeoff, Rev. 3, dated [date] |
| Net allowable bearing pressure (qa) | 2,500 psf | Geotechnical Report GEO-2024-118, p.14, Table 3 |
| Ultimate bearing capacity (qult), for reference | ≈7,500 psf | Same report; qa already = qult ÷ FS(3.0) — do not re-divide |
| Footing size, as originally drawn | 6'-0" × 6'-0" (36 ft²) | — |
| Bearing pressure as drawn | 165,000 / 36 = 4,583 psf | Exceeds qa by 83% — **reject** |
| Revised footing size | 9'-0" × 9'-0" (81 ft²) | — |
| Bearing pressure, revised | 165,000 / 81 = 2,037 psf | Below qa (2,500 psf) — **accept** |
| Effective FS on revised footing | 7,500 / 2,037 = 3.68 | Above the 2.5–3.0 report target — acceptable, not excessive for this soil class |

**Memo conclusion:**

> "Footing F-3 as shown on S-301 (6'-0" sq.) is undersized against the allowable bearing pressure in GEO-2024-118 and is revised to 9'-0" sq. Revised bearing pressure of 2,037 psf produces an effective factor of safety of 3.68 against the report's ultimate capacity, consistent with the report's stated design intent. No additional factor of safety has been applied beyond the report's allowable value. Structural drawings to be revised to reflect the 9'-0" sq. footing and coordinated reinforcing before issue for construction."

## 3. RFI response template

| Field | Entry |
|---|---|
| RFI # | 014 |
| Date received | [date] |
| Submitted by | [Contractor], Superintendent |
| Drawing/detail referenced | C-401, Detail 6 (storm pipe bedding) |
| Field condition | Groundwater encountered at 4 ft below proposed pipe invert, 3 ft shallower than geotechnical report boring B-4 indicated. |
| Question | Can pipe bedding proceed as detailed, or is dewatering/bedding revision required? |

**Engineer's response (dated, referenced, no verbal substitute):**

> "Response to RFI-014: Groundwater at El. [X] is above the pipe invert elevation shown on C-401. Per Detail 6 note 3, bedding material below the water table shall be revised from Class I to Class IC (crushed stone, per Section 33 05 00) and dewatering per Section 31 23 19 shall be maintained until bedding and initial backfill are complete. No change to pipe slope or size. This response supersedes Detail 6 for this station range (12+00 to 14+50) only; all other stations proceed as drawn. Contractor to submit dewatering plan for review prior to excavation below El. [X]."

**Rule embedded in the template:** every response names the exact drawing/detail/section affected, states the scope of the change (station range, not "the project"), and requires a follow-up submittal where the change has downstream implications (dewatering plan here). A response that doesn't name a scope boundary is treated as changing the whole drawing set — expensive and usually wrong.

## 4. Value-engineering request evaluation

Standard intake for a contractor/owner cost-reduction request touching a stamped design element:

| Question | Answer required before evaluating |
|---|---|
| What specific stamped calculation does this change touch? | e.g., detention volume, pipe capacity, footing size |
| What new supporting data justifies the change? | New geotech boring, revised hydrology, updated load takeoff — not "the old number was conservative" |
| Does the change reduce freeboard, FS, or emergency-event capacity? | If yes, requires explicit written acceptance from owner and, where code-mandated, jurisdictional variance — not an engineer's unilateral approval |
| Net cost/risk tradeoff, stated in one line | e.g., "Reducing pipe from 18 in to 15 in saves $4,200 in material but drops the 10-yr capacity margin from 12% to 1%" |

Requests that reduce a code-minimum margin (freeboard, FS, discharge rate) to exactly the minimum, with no new supporting data, are declined by default — see `red-flags.md`.
