# Playbook

## Alloy addition calculation accounting for recovery rate (filled example)

Target Mn 1.20%, current assay 0.40%, melt weight 50,000 kg, established Mn recovery 90%.

| Step | Value |
|---|---|
| Needed Mn increase | 1.20% − 0.40% = 0.80 percentage points |
| Effective Mn to recover into melt | 50,000 kg × 0.0080 = 400 kg |
| Recovery rate | 90% |
| Required elemental Mn addition | 400 ÷ 0.90 = 444.4 kg |
| Result if naive 400 kg charged instead | 400 × 0.90 = 360 kg actually recovered |
| Actual increase from naive addition | 360 ÷ 50,000 = 0.72 percentage points |
| Resulting final Mn (naive) | 0.40 + 0.72 = 1.12% |
| Shortfall vs. 1.20% target | 1.20 − 1.12 = 0.08 points (10% short of the intended 0.80-point increase) |

**Comparison across recovery rates (same 400 kg effective target, same 50,000 kg melt):**

| Recovery rate | Required elemental addition | If naive 400 kg charged, actual recovered | Resulting shortfall |
|---|---|---|---|
| 95% | 400 ÷ 0.95 = 421.1 kg | 400 × 0.95 = 380 kg | 20 kg short (5%) |
| 90% | 400 ÷ 0.90 = 444.4 kg | 400 × 0.90 = 360 kg | 40 kg short (10%) |
| 80% | 400 ÷ 0.80 = 500.0 kg | 400 × 0.80 = 320 kg | 80 kg short (20%) |

Lower recovery rates require proportionally larger elemental additions to hit the same effective target — and produce proportionally larger shortfalls if the naive full-recovery assumption is used instead.

## Slag basicity reference for refining reactions (filled example)

| Refining reaction | Required slag condition | Typical basicity target |
|---|---|---|
| Desulfurization | High basicity, reducing conditions | Basicity ratio (CaO/SiO2) ≥ 2.5–3.0 |
| Dephosphorization | High basicity, oxidizing conditions | Basicity ratio ≥ 2.0, with controlled oxygen potential |
| General deoxidation | Moderate basicity | Basicity ratio ~1.5–2.0 |

**Applied check:** A slag practice tuned for dephosphorization (oxidizing conditions) run on a heat that actually needs desulfurization (reducing conditions) won't achieve the desired sulfur removal even at correct basicity ratio numbers — the oxidation state, not just the basicity ratio alone, has to match the specific reaction targeted.
