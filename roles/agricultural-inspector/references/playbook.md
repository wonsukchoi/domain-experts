# Agricultural Inspector — Playbook

## Grade defect tolerance and sub-tolerance check (filled example)

| Step | Value |
|---|---|
| Lot size | 480 cartons (~28,800 lbs) fresh tomatoes |
| Sample size drawn | 100 units |
| Defects tallied | 5 serious damage, 2 insect injury, 2 decay = 9 total |
| Aggregate defect rate | 9/100 = 9% (vs. 10% overall tolerance — passes) |
| Decay sub-tolerance rate | 2/100 = 2% (vs. 1% decay sub-tolerance — **fails**) |
| **Result** | Lot fails U.S. No. 1 on the decay sub-tolerance despite passing the aggregate tolerance; downgrade to U.S. No. 2 |

**Use:** Always tally by defect category, not just in aggregate — a sub-tolerance (decay, serious damage) can fail a lot that passes the overall percentage, because progressive/contagious defects are capped independently.

## Acceptance sampling by lot size (illustrative schedule)

| Lot size (cartons) | Sample size | Acceptance number (max defective units to still pass) |
|---|---|---|
| Up to 90 | 13 | 1 |
| 91–280 | 32 | 2 |
| 281–500 | 50 | 3 |
| 501–1,200 | 80 | 5 |
| 1,201–3,200 | 125 | 7 |

**Use:** Pull the sample size and acceptance number from the schedule matched to the actual lot size before drawing a single unit — resampling the same lot after a fail, or drawing a convenience sample smaller than the schedule requires, invalidates the statistical basis of the finding.

## Agricultural water quality — geometric mean and statistical threshold value worksheet (filled example)

| Sample # | Generic *E. coli* (CFU/100 mL) |
|---|---|
| 1 | 100 |
| 2 | 150 |
| 3 | 400 |
| 4 | 600 |

**Geometric mean:** GM = (100 × 150 × 400 × 600)^(1/4) = (3,600,000,000)^(1/4) ≈ **245 CFU/100 mL**.

| Metric | Result | Limit | Status |
|---|---|---|---|
| Geometric mean | 245 CFU/100 mL | 126 CFU/100 mL | **Exceeds by ~94%** |
| Statistical threshold value (90th percentile, log-based) | Not required once GM already exceeds its limit | 410 CFU/100 mL | N/A — GM failure alone is sufficient |

**Use:** Compute the rolling geometric mean first; if it already exceeds the limit, the source fails regardless of the statistical threshold value. If the geometric mean is within limit, compute the statistical threshold value before clearing the source — a single high reading inside an otherwise low dataset frequently fails the STV check even when the GM passes.

## Pesticide tolerance cross-check (commodity-chemical pair)

| Residue detected | Commodity | Result (ppm) | Tolerance for this commodity-chemical pair (ppm) | Status |
|---|---|---|---|---|
| Chlorpyrifos | Tomatoes | 0.03 | No tolerance established for tomatoes (tolerance revoked for this commodity) | **Violation — any detectable residue is a violation absent an established tolerance** |
| Azoxystrobin | Tomatoes | 0.4 | 3.0 | Within tolerance — not a violation |

**Use:** Never evaluate a detected residue against a memorized "typical" ppm ceiling — pull the tolerance table entry for that exact commodity-chemical pair. A residue can be a violation at a low ppm value if no tolerance exists for that commodity, and compliant at a much higher value if the established tolerance for that pair is high.

## Preharvest interval (PHI) check

| Pesticide application date | Labeled PHI (days) | Harvest date | Days elapsed | Status |
|---|---|---|---|---|
| June 1 | 14 | June 10 | 9 | **Violation — harvested 5 days before PHI cleared** |
| June 1 | 14 | June 16 | 15 | Compliant |

**Use:** Compare the actual harvest date against application date + labeled PHI, not against a general "seems like enough time" judgment — PHI is set per product label and is a hard cutoff, not a guideline.

## Traceability records request — Key Data Elements / Critical Tracking Events

| Critical Tracking Event (CTE) | Key Data Elements (KDEs) required | Response window |
|---|---|---|
| Harvesting | Location, harvest date, commodity, traceability lot code | 24 hours from request |
| Cooling | Location, date, lot code | 24 hours from request |
| Packing | Location, date, lot code, quantity | 24 hours from request |
| Shipping | Ship-from/ship-to location, date, lot code, quantity | 24 hours from request |

**Use:** The 24-hour window applies to producing the records, not to resolving the underlying issue. A facility that eventually locates the records after 30 hours has already committed a recordkeeping violation regardless of what the records ultimately show.

## Stop-sale order vs. corrective-action letter decision table

| Finding type | Response |
|---|---|
| Confirmed pesticide-tolerance exceedance | Stop-sale order |
| Decay/contamination sub-tolerance failure | Stop-sale order |
| Agricultural water quality standard not met, direct-contact use | Stop-sale order (for affected use) pending corrective measure |
| Grade-marking or labeling discrepancy, no food-safety component | Corrective-action letter |
| Missing or incomplete traceability documentation, product otherwise compliant | Corrective-action letter with records deadline |

**Use:** Default to stop-sale whenever the finding touches food safety (adulteration, confirmed residue exceedance, decay/contamination); reserve corrective-action letters strictly for documentation, labeling, or administrative gaps with no food-safety component.

## Inspection finding — filled example

> **Inspection Finding — Lot #480-TOM, [Packing House], [Date]**
> Grade result: Sample of 100 units shows 9% total defects (within the 10% U.S. No. 1 overall tolerance) but 2% decay, exceeding the standard's 1% decay sub-tolerance. **Lot fails U.S. No. 1; downgraded to U.S. No. 2 pending re-sort.**
> Water finding: Rolling geometric mean of generic *E. coli*, field source [ref], computed at 245 CFU/100 mL against the 126 CFU/100 mL limit — **agricultural water quality standard not met.**
> Action: Re-sort and re-present the lot for grade re-inspection on a newly drawn sample. Water source use for direct-contact irrigation is suspended pending a documented corrective measure (treatment or a verified die-off interval) and a new confirmatory sampling round.
> **Corrective action deadline: 15 days from this notice.**
