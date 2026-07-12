# Geothermal Loop Playbook

Filled worksheets and procedures with concrete thresholds. Defaults, not laws — deviate consciously and document why.

## 1. Bore/trench sizing worksheet

**Step 1 — load, not tonnage.** Pull Manual J heating and cooling loads in Btu/h. Convert to tons: Btu/h ÷ 12,000 = tons. The larger of heating/cooling (adjusted for the local balance-point climate) governs. If quoted equipment tonnage exceeds the calculated load by more than ~15–20%, stop and flag the mismatch before sizing the loop against it.

**Step 2 — ground thermal conductivity (k-value).**

| Formation | Typical k (Btu/hr·ft·°F) | Notes |
|---|---|---|
| Dry sand/gravel | 0.4–0.6 | Poor conductor; expect longer bore lengths |
| Wet clay | 0.6–0.9 | Common residential default absent a TRT |
| Saturated sand/gravel | 0.9–1.3 | Groundwater movement improves heat transfer |
| Solid rock (granite, limestone) | 1.0–2.2 | Highly variable — a TRT is worth the cost above ~15 tons |
| Glacial till (mixed) | 0.8–1.0 | Common Midwest/Northeast residential default |

Run a thermal response test (TRT) above the local size threshold (commonly light-commercial and larger); below it, use the closest documented local benchmark and record which one and why in the bore log — never leave the assumption unstated.

**Step 3 — bore length.** `Bore ft = tons × ft/ton benchmark`, where ft/ton scales inversely with k: roughly 250–300 ft/ton for poor-conductivity soils (k ≈ 0.4–0.6), 175–200 ft/ton for moderate (k ≈ 0.8–1.0), 150 ft/ton or less for high-conductivity saturated rock (k ≈ 1.3+). Confirm against sizing software (GLHEPro, GchpCalc) rather than the rule of thumb alone whenever the job is above residential scale.

**Step 4 — configuration and spacing.**

| Configuration | When to default to it | Spacing/depth limit |
|---|---|---|
| Vertical borehole | Lot size or setbacks won't fit horizontal trenching | 15–20 ft on-center minimum; single-bore depth capped by rig and local max (commonly 250–300 ft) |
| Horizontal loop | Adequate open land, lower drilling cost | Trenches typically 4–6 ft deep, spaced 2–4 ft apart within a trench for multi-pipe configs |
| Standing column / open loop | Favorable hydrogeology, adequate well yield, local permitting supports it | Requires separate injection/discharge or return-well permitting — not interchangeable with closed-loop rules |

## 2. Grout selection

| Formation conductivity | Grout target k (Btu/hr·ft·°F) | Typical mix |
|---|---|---|
| Low (k < 0.7) | ≥ 0.75 | Thermally enhanced bentonite with silica sand |
| Moderate (k 0.7–1.1) | ≥ 0.85 | Thermally enhanced bentonite-silica |
| High-conductivity rock (k > 1.1) | ≥ 1.0–1.7 | Silica-sand-heavy or graphite-enhanced grout |

Grout is installed bottom-up through a tremie pipe in a single continuous pour per bore — never poured from the top, which traps air and leaves voids. After the pour, reconcile delivered grout volume against the calculated annular volume (`bore diameter² − pipe bundle cross-section, × depth`); a delivered volume more than ~10% under calculated signals a void or a short pour and is a hold point before backfill.

## 3. Purge and pressure-test procedure — hold points before backfill, in order

1. **Flush.** Run the purge cart at high flow through each circuit individually, then the full field, until no air bubbles are visible at the return sight-glass and flow reaches turbulent velocity (commonly targeted at ≥ 2 ft/sec in the pipe, higher on longer runs) — laminar flow at commissioning silently caps heat transfer even if every other step was done correctly.
2. **Static pressure test.** Pressurize to 1.5× expected operating pressure (commonly around 100 psi for residential HDPE loops) and hold. **Pass: no measurable drop over the hold period** (commonly 30 minutes to 24 hours depending on local/manufacturer spec). Any drop → isolate by section and re-test; do not backfill on a "close enough" result.
3. **Antifreeze charge.** Set propylene glycol (or other approved fluid) concentration to protect to roughly 15°F below the coldest expected design EWT — not a flat percentage regardless of climate or load. Confirm with a refractometer, not by volume estimate alone.
4. **Sign-off.** Purge log and pressure-test record signed by the installing technician before the trench is scheduled for backfill. This record is the only artifact anyone will have once the trench closes.

## 4. Capacity-complaint triage — cheapest, most likely causes first

1. **Pull EWT against design band.** If EWT is inside the design range (commonly EWT design band spans roughly 25–90°F depending on climate and mode), the loop is very likely not the cause — move to the refrigerant/airflow side. If EWT is well outside the band on a design-condition day, the loop or ground is implicated first.
2. **Check flow rate.** Measure GPM per ton at the flow center; below ~2.25–3 GPM/ton, suspect an incomplete purge (air pocket) or an undersized/failing circulator before suspecting the bore itself.
3. **Check delta-T across the heat pump water side.** Compare the field reading to the design delta-T computed from `Btu/h ÷ (500 × GPM)`. A delta-T well above design with low flow points at a flow problem; a delta-T well below design with adequate flow points at an equipment-capacity or refrigerant-side issue, not the loop.
4. **Cross-check equipment tonnage against the original Manual J.** Short-cycling with normal EWT and normal flow is very often an oversized-equipment symptom, not a loop symptom — pull the original load calc before recommending any loop work.
5. **Only after 1–3 rule out the loop: open the refrigerant circuit** (EPA 608-certified work) to check charge and superheat/subcooling against manufacturer spec.
