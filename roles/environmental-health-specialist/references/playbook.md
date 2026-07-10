# Playbook

Filled reference tables and worked calculations for the five recurring specialist tasks: temperature danger-zone disposition, food-code violation categorization, pool chlorination dosing, septic percolation/site evaluation, and imminent-health-hazard triage. Numbers are illustrative of the cited source's structure — verify current code edition and jurisdiction-specific amendments before use in an actual enforcement action.

## 1. TCS food temperature danger-zone disposition table

| Cumulative time in 41–135°F zone | Disposition | Notes |
|---|---|---|
| < 2 hours | Re-cool to ≤41°F or reheat to ≥165°F (or product-specific endpoint) and return to holding | Log the discovery time and corrective reading |
| 2–4 hours | Use immediately (cook, serve, or sell) | May not be returned to holding after this window |
| > 4 hours | Discard — mandatory | No corrective action restores the food to compliant status |
| Any duration under a documented TPHC procedure | Follow the written Time as a Public Health Control plan | Requires time-marking at point of removal from temperature control and a written procedure on file; without both, treat as an untracked deviation and apply the table above |

**Cook/reheat reference endpoints (internal temperature, instantaneous unless noted):** poultry and stuffed items 165°F; ground meats and mechanically tenderized product 155°F for 15 seconds; whole-muscle intact beef/pork/seafood 145°F for 15 seconds; reheating of previously cooked TCS food for hot holding 165°F within 2 hours.

## 2. Food-code violation categorization and correction deadlines

| Category | Examples | Typical correction deadline |
|---|---|---|
| Priority item | Cold/hot holding out of range; inadequate cook temperature; confirmed cross-contamination; no handwashing facility available | On-site same-visit correction where feasible; otherwise per the code's stated short window (commonly 24–72 hours) |
| Priority Foundation item | Missing employee health policy documentation; thermometer not calibrated; no consumer advisory posted for undercooked items offered | Commonly 10 calendar days |
| Core item | Physical facility maintenance (torn gasket, missing ceiling tile), non-food-contact equipment cleanliness | Commonly up to 90 days, or by next routine inspection |

**Rule for reading this table:** the category is set by the item's direct relationship to foodborne-illness risk factors, not by how visually alarming the finding is — a cracked floor tile (Core) can look worse than an uncalibrated thermometer (Priority Foundation) but carries materially less illness risk.

## 3. Pool/spa chlorination dosing — worked calc structure

Standard dosing formula: **lbs of 100%-available chlorine = ppm rise × pool volume (million gallons) × 8.34**

| Incident type | Target free chlorine | pH | Min. water temp | Hold time | CT target |
|---|---|---|---|---|---|
| Formed-stool (no diarrhea/vomit) | Routine shock, commonly ≥2 ppm-equivalent FAC | ≤7.5 | No CDC minimum stated | ≥25 minutes | Not CDC-published; routine shock protocol |
| Diarrheal or vomit incident | 20 ppm | 7.2–7.5 | ≥77°F (25°C) | 12.75 hours (765 min) | 15,300 mg·min/L (3-log *Cryptosporidium* inactivation) |

**Worked example (150,000-gal pool, FC 2.0→20 ppm, 12.5% NaOCl):**
- ppm rise needed: 20 − 2.0 = 18 ppm
- lbs 100% chlorine: 18 × 0.150 MG × 8.34 = 22.52 lb
- lbs of 12.5% product: 22.52 ÷ 0.125 = 180.1 lb
- gallons of 12.5% NaOCl (≈10.1 lb/gal): 180.1 ÷ 10.1 ≈ 17.8 gal

**Cyanuric acid (CYA) check before dosing:** if CYA is at or above roughly 50 ppm, the standard 20 ppm/12.75-hour CT target is not practically achievable — published data shows even 40 ppm FC at pH 6.5, 77°F, held 24 hours fails to reach 3-log inactivation at 50 ppm CYA. Default action: partially drain and dilute to bring CYA below the threshold before dosing, or extend hold time substantially and document the deviation with a rationale.

## 4. Septic percolation and site evaluation

| Perc rate (min/inch) | Suitability | Design implication |
|---|---|---|
| < 1 | Too fast — poor treatment, risk of untreated effluent reaching groundwater | Flag for alternative design (e.g., liner, engineered media) |
| 1–5 | Fast, marginal | Standard system possible with reduced loading rate; verify against code minimum |
| 5–30 | Favorable | Standard trench/bed system per code loading-rate table |
| 30–60 | Slow, marginal | Larger absorption field required; verify against code maximum |
| > 60 | Too slow — inadequate infiltration | Flag for alternative system (mound, aerobic treatment unit, or engineered evaluation) |

**Design flow heuristic:** residential design flow commonly estimated at ~120 gal/bedroom/day for absorption field sizing.

**Independent site-limiting conditions to check regardless of perc rate:** seasonal high water table depth below the trench bottom (code-specified separation, commonly 2–4 ft depending on jurisdiction), depth to bedrock or restrictive layer, slope, and setback distances to wells and surface water. A favorable perc rate does not waive any of these — the site fails on whichever constraint is most limiting.

## 5. Imminent-health-hazard triage checklist

Conditions that commonly authorize immediate closure or embargo without waiting for the standard correction-deadline process (verify the exact list against the jurisdiction's code — this is a commonly used structure, not a universal list):

- No operating handwashing facility (no water, no soap, or physically inaccessible) in a food establishment.
- Confirmed sewage backup or overflow into a food-prep, food-storage, or handwashing area.
- Confirmed cross-connection between potable and non-potable water with no backflow prevention.
- Total loss of refrigeration or hot-holding capability with TCS food present and no corrective plan.
- Fire, flood, or other structural event compromising the facility's ability to operate safely.
- Confirmed vector infestation (rodent activity, for example) presenting direct contamination risk to open food.

**Escalation note:** if none of the above apply, default to standard violation categorization and correction deadline (Section 2) even if the finding is serious — imminent-hazard authority is reserved for conditions that make continued operation unsafe *today*, not for findings that are simply high-priority.
