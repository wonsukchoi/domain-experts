# Artifacts

Filled templates, not descriptions of templates. Populate with real project numbers; the structures below are already valid.

## 1. Goal-and-scope memo (LCA)

```markdown
Project: Corrugated vs. molded-pulp tray for retail produce packaging
Functional unit: packaging sufficient to deliver 1,000 kg of tomatoes to retail,
  intact, over the current distribution network
System boundary: cradle-to-gate (tray production) + distribution to retail;
  EXCLUDES retail refrigeration and consumer disposal (rationale: internal
  material-selection decision, not a public comparative claim — cradle-to-grave
  and critical review required if this becomes a marketing claim)
Allocation method: system expansion for the pulp mill's fiber co-products
  (credit the avoided virgin-fiber alternative); mass allocation as fallback
  if the avoided-product model can't be built with available data
Impact assessment method: TRACI 2.1 (US EPA), primary category GWP-100,
  secondary categories eutrophication and fossil resource depletion tracked
  to catch a category tradeoff
Data sources: ecoinvent 3.9 background data; primary data from the mill's
  2025 energy and water metering (pedigree score: 2/5 on ecoinvent's
  reliability axis — supplier-reported, not third-party verified)
Cutoff rule: flows contributing under 1% of any tracked impact category
  may be excluded; excluded flows must be listed, not silently dropped
Sign-off: [name], packaging director — scope approved [date]
```

## 2. Material flow balance (plant-level, filled)

Single-line pulp mill, monthly basis. Balance must close within tolerance before any downstream LCIA runs.

| Flow | Direction | Quantity (t/month) | Measurement basis |
|---|---|---|---|
| Wood chips (input) | in | 4,200 | Weighbridge, all deliveries |
| Process water (input) | in | 38,000 | Flow meter, continuous |
| Pulp product (output) | out | 1,850 | Production log, scale |
| Bark/wood waste (output) | out | 1,050 | Weighbridge, hauler tickets |
| Black liquor solids to recovery boiler (output) | out | 1,180 | Lab assay, weekly composite |
| Wastewater discharge (output) | out | 36,900 | Flow meter, continuous |
| **Balance check** | — | in 42,200 vs out 40,980 | **gap = 1,220 t (2.9% of throughput)** |

Gap of 2.9% is inside the ~5% tolerance heuristic — proceed, but flag the gap as evaporative water loss (cooling towers, steam venting) and confirm with the site's water balance before treating any remaining discrepancy as a genuine unaccounted flow. A gap over ~5–10% would block sign-off until traced to a specific meter or measurement point.

## 3. Industrial-symbiosis feasibility screen (filled)

Candidate exchange: cement plant waste heat (kiln exhaust, ~300°C) to an adjacent greenhouse operation.

| Screen criterion | Threshold (heuristic) | This case | Pass/fail |
|---|---|---|---|
| Entity count in network | ≥3 entities for true symbiosis (Chertow 3-2); 2 entities = bilateral trade, still worth doing but don't market it as a "symbiosis network" | 2 (cement plant, greenhouse) | Bilateral only — proceed as a trade, not a network claim |
| Distance | <50 km trucking radius for low-value bulk flows; heat/steam pipeline typically <5 km to avoid excessive loss and capital cost | 1.8 km, direct pipeline feasible | Pass |
| Value density of exchanged resource | Low (waste heat, ash, water) tolerates short radius only; high-value flows (solvents, metals) justify longer haul | Low (waste heat) | Consistent with distance threshold |
| Continuity risk | Exchange must have a contracted minimum-volume and price-adjustment clause, not an MOU alone, before capital is committed | Draft term sheet includes 10-year minimum-offtake clause | Pass, pending signature |
| Counterfactual check | Would the heat be recovered/used anyway (e.g., existing waste-heat boiler)? If yes, claimed savings must net that out | No existing recovery system at kiln | Full credit supportable |

**Recommendation:** proceed to detailed engineering. Do not describe this in external materials as "industrial symbiosis" (2 entities, below the 3-2 threshold) — describe it as a byproduct energy-supply agreement; reserve "symbiosis" language for when a third participant (e.g., a district-heating loop or a second industrial heat user) joins the network.

## 4. Allocation decision applied to a co-product case

Refinery-adjacent biodiesel process yields biodiesel (primary product) and glycerin (co-product), 100 t feedstock in, 88 t biodiesel out, 9 t crude glycerin out (3 t process loss, within the 5% balance tolerance).

| Step | Method tried | Outcome |
|---|---|---|
| 1. System expansion | Model crude glycerin as displacing petrochemical glycerin production | Feasible — market glycerin substitution data available in ecoinvent; use this |
| 2. Mass allocation (fallback, not used here) | 88/97 = 90.7% burden to biodiesel, 9/97 = 9.3% to glycerin | Not used — system expansion data was available, so the hierarchy stops here |
| 3. Economic allocation (last resort, not used here) | Biodiesel $1.05/kg, glycerin $0.15/kg → 96.4% biodiesel, 3.6% glycerin | Rejected — glycerin price is volatile quarter to quarter; would make the biodiesel footprint swing with a market price that has nothing to do with the process |

Documented choice: **system expansion**, crediting the avoided petrochemical glycerin production against the process's total burden before allocating the remainder to biodiesel by energy content. Rationale recorded in the project file per ISO 14044's allocation-avoidance-then-hierarchy requirement.
