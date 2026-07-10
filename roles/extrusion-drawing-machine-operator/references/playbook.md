# Playbook

## Area-reduction calculation (filled example)

Draw pass: 2.00mm → 1.80mm diameter. Material limit: 18% max single-pass area reduction.

| Step | Value |
|---|---|
| Initial diameter | 2.00mm |
| Final diameter | 1.80mm |
| Diameter-based reduction (naive) | (2.00 − 1.80) / 2.00 = 10.0% |
| Initial area (proportional, d²) | 2.00² = 4.00 |
| Final area (proportional, d²) | 1.80² = 3.24 |
| Actual area reduction | (4.00 − 3.24) / 4.00 = 19.0% |
| Material limit | 18.0% |
| Status | **Exceeds limit — revise pass** |

**Corrected pass:** Solve for the diameter giving exactly 18.0% area reduction: final area = 4.00 × (1 − 0.18) = 3.28; final diameter = √3.28 ≈ 1.811mm.

| Revised pass | Value |
|---|---|
| Final diameter | 1.811mm |
| Final area | 1.811² ≈ 3.28 |
| Area reduction | (4.00 − 3.28) / 4.00 = 18.0% |
| Status | Within the 18.0% limit |

## Cumulative reduction-before-anneal tracker (filled example)

Starting diameter 2.00mm, material's total-before-anneal limit: 60% cumulative area reduction.

| Pass | Diameter after pass | Area (d²) | Area reduction this pass | Cumulative area reduction |
|---|---|---|---|---|
| Start | 2.00mm | 4.00 | — | 0% |
| 1 | 1.811mm | 3.28 | 18.0% | 18.0% |
| 2 | 1.640mm | 2.69 | (3.28−2.69)/3.28 = 18.0% | (4.00−2.69)/4.00 = 32.75% |
| 3 | 1.485mm | 2.21 | (2.69−2.21)/2.69 = 17.8% | (4.00−2.21)/4.00 = 44.75% |
| 4 | 1.345mm | 1.81 | (2.21−1.81)/2.21 = 18.1% | (4.00−1.81)/4.00 = 54.75% |
| 5 (planned) | 1.220mm | 1.49 | (1.81−1.49)/1.81 = 17.7% | (4.00−1.49)/4.00 = 62.75% |

**Result:** Pass 5 would push cumulative reduction to 62.75%, exceeding the 60% total-before-anneal limit — schedule an intermediate anneal after pass 4 (at 54.75% cumulative) rather than proceeding directly to pass 5.

## Die swell compensation worksheet (filled example)

Target final profile width: 25.0mm. Resin's expected die swell at this line speed: 8%.

| Step | Value |
|---|---|
| Target final dimension | 25.0mm |
| Expected die swell | 8% |
| Die opening (compensated) | 25.0 / 1.08 ≈ 23.15mm |
| Result if die sized to naive 25.0mm opening | 25.0 × 1.08 = 27.0mm final profile — 8% oversized |

**Result:** Sizing the die opening at 23.15mm (compensating for the expected 8% swell) produces a finished profile at the correct 25.0mm target; sizing the die directly to 25.0mm produces an oversized 27.0mm profile once swell occurs.
