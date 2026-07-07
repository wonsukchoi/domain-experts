# Soil and Plant Scientist — Playbook

## Soil-test interpretation table (Bray-P1, corn, stated heuristic — confirm against local land-grant guide)

| Soil-test P (ppm) | Category | Recommendation |
|---|---|---|
| 0-10 | Very low | Buildup (9 lb P₂O₅/acre/ppm deficit vs. 25 ppm critical level, split over 3 yr) + full removal-based maintenance |
| 11-20 | Low | Buildup (reduced increment, split over 2 yr) + full removal-based maintenance |
| 21-25 | Marginal | Removal-based maintenance only, no buildup increment |
| 26-40 | Optimum | Removal-based maintenance only; consider a starter-only reduced rate |
| >40 | High/excess | Skip application; re-test in 2 years; if near a water body or tile-drained, run a Phosphorus Index before any further application |

Same category logic applies to K using the CEC-adjusted critical level (roughly 130-150 ppm for CEC 8-15 meq/100g; higher CEC soils tolerate a higher critical level before yield response flattens).

## Lime requirement lookup (buffer-pH / SMP method, stated heuristic)

| Buffer pH reading | Target pH 6.0 (tons ECCE/acre) | Target pH 6.5 (tons ECCE/acre) | Target pH 6.8 (tons ECCE/acre) |
|---|---|---|---|
| 6.8 | 0.5 | 1.0 | 1.4 |
| 6.6 | 1.0 | 1.6 | 2.1 |
| 6.4 | 1.5 | 2.2 | 2.8 |
| 6.2 | 2.1 | 2.9 | 3.6 |
| 6.0 | 2.7 | 3.6 | 4.4 |

ECCE = Effective Calcium Carbonate Equivalent, adjusts for the liming material's purity and particle fineness. A coarser (larger mesh) source needs a higher tonnage of the same nominal material to deliver the same ECCE. Sequence lime 6-12 months ahead of the season it needs to be fully reacted for; a fall application ahead of spring planting is the standard window in temperate row-crop regions.

## Nutrient removal rates (stated heuristics — vary by hybrid/variety and region; confirm against local guide)

| Crop | P₂O₅ removal (lb/unit) | K₂O removal (lb/unit) | Unit |
|---|---|---|---|
| Corn (grain only) | 0.35 | 0.27 | per bushel |
| Corn (silage, whole plant) | 0.85 | 1.25 | per ton (35% DM) |
| Soybean (grain) | 0.80 | 1.30 | per bushel |
| Wheat (grain) | 0.60 | 0.35 | per bushel |
| Alfalfa hay | 12.0 | 50.0 | per ton |

Silage and hay removal rates run several times higher than grain-only harvest because the whole plant — not just the grain — leaves the field. A field switching from grain to silage/hay harvest without adjusting the removal-based maintenance rate will show a K soil-test decline that looks unexplained until the harvest-type change is checked.

## Filled nutrient management plan (excerpt, from the SKILL.md worked example)

```
FIELD: North 40
SOIL TEST: Bray-P1, [Lab Name], sampled [date]
  pH: 5.8 (target 6.0-6.8)
  P: 8 ppm (critical level 25 ppm — Very Low category)
  K: 95 ppm (critical level 140 ppm, CEC-adjusted — Low category)
  CEC: 12 meq/100g
YIELD GOAL: 180 bu/acre corn (field 5-yr average: 176 bu/acre)

RECOMMENDATION:
  Lime:  2.0 tons/acre ECCE, fall application ahead of spring planting.
         Full reaction expected 6-12 months post-application.
  P2O5:  114 lb/acre (51 lb buildup increment, yr 1 of 3-yr plan,
         + 63 lb removal-based maintenance for 180 bu/acre goal).
         Source: DAP (18-46-0) at 247.8 lb/acre.
  K2O:   123.6 lb/acre (75 lb buildup increment, yr 1 of 3-yr plan,
         + 48.6 lb removal-based maintenance).
         Source: potash (0-0-60) at 206 lb/acre.

COST ESTIMATE (Year 1, P/K/lime only — N programmed separately):
  DAP:    247.8 lb/acre x $0.325/lb = $80.54/acre
  Potash: 206 lb/acre x $0.25/lb   = $51.50/acre
  Lime:   2.0 tons/acre x $40/ton  = $80.00/acre
  TOTAL:                             $212.04/acre  ($8,481.60 for 40 acres)

RE-TEST INTERVAL: 3 years. At re-test, if P and K have reached critical
level, shift Year 4 rates to maintenance-only (removal-based, no
buildup increment).
```

## Fallback positions when data is incomplete (in preference order)

1. **Extraction method unknown for a soil-test report.** Contact the lab directly to confirm before applying any recommendation table — do not guess based on the ppm range looking "typical" for one method or another.
2. **No field-specific yield history available.** Use the county-average yield for that soil type/drainage class from NRCS Web Soil Survey, not a whole-farm or state average, and flag the resulting rate as a lower-confidence estimate pending at least one season of yield-monitor data.
3. **No CEC value reported.** Estimate conservatively from soil texture class (sandy soils: assume CEC 5-8 meq/100g; loam: 10-15; clay: 20-30) and apply the more conservative (lower) critical-level threshold and split-application heuristic until a lab CEC value is available.
4. **Grid/zone yield-map data unavailable for a field with known visible variability.** Default to a single composite sample and a flat-rate recommendation, but note explicitly in the plan that a zone-sampling upgrade is recommended before the next application cycle.
