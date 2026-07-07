# Food Scientist — Playbook

## Accelerated shelf-life test (ASLT) design worksheet

| Parameter | Value | Note |
|---|---|---|
| Product | Fruit-filled snack bar | Composite food, moisture-migration risk |
| Failure mode hypothesis | Texture (staling) vs. oxidative rancidity | Determines which Q10 range applies |
| Test conditions | 30°C, 35°C, 40°C + 25°C real-time control | Minimum two accelerated points to fit a curve, not extrapolate from one |
| Sampling schedule | Days 3, 7, 10, 14, 21 (accelerated); monthly (real-time) | Denser near expected failure window |
| Endpoint test | Triangle test vs. day-0 control, trained panel n=24 | Forced-choice — harder to game than hedonic scale |
| Instrumental proxy | Texture analyzer (compression force, N) | Cross-check panel result against an objective measure |

**Q10 selection table:**

| Degradation mechanism | Typical Q10 range | Example failure modes |
|---|---|---|
| Lipid oxidation (chemical) | 2.5–4.0 | Rancidity, off-flavor in fats/oils |
| Non-enzymatic browning / Maillard (chemical) | 2.0–3.0 | Color darkening, flavor drift |
| Vitamin degradation (chemical) | 2.0–3.0 | Nutrient-claim failure |
| Moisture migration / staling (physical, diffusion) | 1.5–2.0 | Texture loss in composite/multi-component foods |
| Starch retrogradation (physical) | 1.5–2.0 | Bread/bakery firming |

**Extrapolation arithmetic (fill per study):**
Failure day at test temp T_test → SL(T_storage) = Day_fail × Q10^((T_test − T_storage)/10)
Printed shelf life = SL(T_storage) × 0.70–0.80 (safety margin fraction; use the lower end when lot-to-lot variability data is limited).

## HACCP hazard-analysis / CCP table (excerpt, one line item)

| Process step | Hazard | Likelihood | Severity | Is this a CCP? | Control action | Critical limit | Monitoring | Corrective action |
|---|---|---|---|---|---|---|---|---|
| Baking | Biological — pathogen survival (Salmonella) | Moderate (raw flour input) | High | **Yes** | Bake to internal temp/time | ≥165°F (74°C) for ≥15 sec, core probe | Core-temp check every batch, logged | Hold batch, re-bake or reject if limit not met |
| Metal detection | Physical — metal fragment from mixing equipment | Low | High | **Yes** | In-line metal detector | Reject any signal ≥2.0mm ferrous / 2.5mm non-ferrous | Continuous, verified hourly with test wand | Isolate rejected units, inspect detector calibration |
| Ingredient receiving (nuts) | Biological/Allergen — undeclared allergen cross-contact | Moderate | High (allergen) | **Yes** | Verify supplier COA + dedicated storage | 100% COA match, zero shared storage with non-allergen line | Every receiving lot | Reject lot if COA mismatch; quarantine if storage breach |
| Mixing | Physical — foreign material from open room | Low | Low | **No** | — | — | GMP/housekeeping controls suffice; no measurable CCP action available at this step | — |

The last row is the standard trap: a plausible hazard exists (open-room contamination), but there's no specific, monitorable control action distinct from general good manufacturing practice — so it isn't a CCP, and forcing one onto the plan produces a monitoring step nobody can actually execute or audit.

## Sensory test protocol selection

| Question | Test | Panel size / type | Output |
|---|---|---|---|
| Is there *any* detectable difference? | Triangle test | n≥24, untrained OK | Pass/fail vs. chance (p<0.05 threshold) |
| Which sample do you prefer? | Duo-trio or paired preference | n≥30, untrained | Directional preference |
| *What* changed and by how much? | Descriptive analysis (QDA) | n=8-12, trained (10+ hrs calibration) | Attribute-intensity scores, e.g. "staleness: 2.1 → 6.4 on a 15-pt scale" |
| Do consumers still like it? | 9-point hedonic scale | n≥75, untrained consumers | Mean liking score, not a difference test |

Never substitute a hedonic scale result for a difference-test conclusion — a liking score can hold steady even after a detectable change, because "different" and "worse" are not the same finding.
