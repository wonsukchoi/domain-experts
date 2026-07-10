# Playbook

## Pattern shrinkage calculation (filled example)

Steel casting, critical print dimension 20.000", cast steel shrink rule 2.0%.

| Step | Value |
|---|---|
| Print (final part) dimension | 20.000" |
| Alloy shrink rate | 2.0% |
| Pattern dimension | 20.000 × 1.02 = 20.400" |
| Verification: casting result if pattern built to print dimension instead (naive) | 20.000 ÷ 1.02 ≈ 19.608" — undersized ~0.39" |

**Comparison across alloys (same 20.000" print dimension):**

| Alloy | Typical shrink rate | Pattern dimension |
|---|---|---|
| Gray iron | 1.0% | 20.000 × 1.01 = 20.200" |
| Cast steel | 2.0% | 20.000 × 1.02 = 20.400" |
| Aluminum | 1.3% | 20.000 × 1.013 = 20.260" |

Using cast steel's 2.0% rule on an aluminum pattern (or vice versa) would produce a pattern off by roughly 0.14"–0.20" on this dimension alone — the shrink rule must match the actual alloy being poured.

## Riser modulus sizing worksheet (filled example)

Casting section (a cube-like boss): 4" × 4" × 4".

| Step | Value |
|---|---|
| Section volume | 4 × 4 × 4 = 64 in³ |
| Section surface area | 6 × (4 × 4) = 96 in² |
| Section modulus (volume ÷ surface area) | 64 / 96 = 0.667" |
| Riser (cylindrical): diameter 5", height 5" | Volume = π × (2.5)² × 5 = 98.2 in³ |
| Riser surface area (side + two ends) | (π × 5 × 5) + 2 × (π × 2.5²) = 78.5 + 39.3 = 117.8 in² |
| Riser modulus | 98.2 / 117.8 = 0.834" |

**Result:** Riser modulus (0.834") exceeds the casting section's modulus (0.667"), meaning the riser solidifies slower — after the section it feeds — which is the correct relationship. A riser modulus below 0.667" would freeze first and leave shrinkage porosity in the casting section instead.

## Casting yield calculation (filled example)

Comparing two tooling options for the same part.

| Process | Good casting weight | Gates + risers + scrap weight | Total poured weight | Yield |
|---|---|---|---|---|
| Option A (simple tooling, higher scrap rate) | 8.0 lb | 4.5 lb | 12.5 lb | 8.0 / 12.5 = 64.0% |
| Option B (complex tooling, lower scrap rate) | 8.0 lb | 5.2 lb | 13.2 lb | 8.0 / 13.2 = 60.6% |

**Result:** Option B has a lower per-piece scrap rate, but its heavier gating system (larger risers required by the part's geometry) actually produces a lower overall yield than Option A — 60.6% versus 64.0%. Comparing by scrap rate alone would have favored Option B; comparing by actual yield favors Option A.
