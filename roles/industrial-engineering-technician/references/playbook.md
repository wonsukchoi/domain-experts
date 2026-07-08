# Playbook — worksheets and audit templates

Filled examples, not descriptions. Numbers are illustrative but internally consistent and arithmetically checked; swap in real observations and re-run the same formulas.

## 1. Time-study worksheet (continuous method)

Job: manual carton taping. Target 95% confidence, ±5% precision. Raw retained cycles (foreign elements already screened and logged separately — see §2).

| Cycle | E1 fold flaps (s) | E2 tape pass (s) | E3 stack to pallet (s) |
|---|---|---|---|
| 1 | 5.0 | 7.8 | 4.0 |
| 2 | 4.8 | 10.2 | 3.9 |
| 3 | 5.1 | 8.5 | 4.1 |
| 4 | 4.9 | 9.6 | 4.0 |
| 5 | 5.2 | 9.0 | 3.8 |
| 6 | 4.7 | 8.1 | 4.2 |
| 7 | 5.0 | 10.5 | 4.0 |
| 8 | 5.3 | 8.8 | 3.9 |
| 9 | 4.9 | 9.3 | 4.1 |
| 10 | 5.1 | 7.6 | 4.0 |
| 11 | 4.8 | 10.8 | 3.8 |
| 12 | 5.0 | 8.4 | 4.2 |
| 13 | 5.2 | 9.7 | 4.0 |
| 14 | 4.9 | 8.9 | 3.9 |
| 15 | 5.0 | 9.1 | 4.1 |
| 16 | 4.8 | 8.6 | 4.0 |
| 17 | 5.1 | 10.1 | 3.9 |
| 18 | 5.0 | 8.3 | 4.1 |
| 19 | 4.9 | 9.4 | 4.0 |
| 20 | 5.3 | 9.3 | 4.0 |
| **Σ** | 100.0 | 182.0 | 80.0 |
| **n** | 20 | 20 | 20 |
| **Mean (OT)** | 5.00 | 9.10 | 4.00 |

**Minimum-cycles check, N' = [(40·√(N·Σx² − (Σx)²)) / Σx]²** — run on the highest-variance element (E2). Σx² (sum of squared cycle times) = 1670.86.

N' = [(40 × √(20×1670.86 − 182.0²)) / 182.0]² = [(40 × √293.2) / 182.0]² = [(40 × 17.123) / 182.0]² = [684.9 / 182.0]² = 3.763² = **14.16 → N' = 15**.

20 retained cycles clears N'=15. E1 (range 4.7–5.3) and E3 (range 3.8–4.2) show tighter spread than E2 — same formula would return N' well under 10 for both; not recomputed since the study already exceeds it.

**Rating and normal time:**

| Element | OT (s) | Rating | NT = OT × Rating (s) |
|---|---|---|---|
| E1 | 5.00 | 1.00 | 5.00 |
| E2 | 9.10 | 0.95 | 8.65 |
| E3 | 4.00 | 1.05 | 4.20 |
| **Total** | | | **17.85** |

**Standard time** = NT × (1 + allowance). At the validated 33% allowance (see §3): ST = 17.85 × 1.33 = **23.74 s/cycle**.

## 2. Foreign-element / outlier log

Every exclusion needs a row here before it's dropped from the mean — no exclusion without one.

| Element | Raw reading (s) | Threshold exceeded | Documented cause | Disposition |
|---|---|---|---|---|
| E2, cycle 7 (raw) | 15.4 | Mean(9.10) + 3σ(0.85×3≈2.55) = 11.65 | Tape-gun jam, cleared by tech, logged in downtime sheet | Excluded, re-timed as cycle 21 |
| E2, cycle 15 (raw) | 14.8 | Same threshold | Carton dropped, restacked | Excluded, re-timed as cycle 22 |

Rule applied: mean ± 3σ on the running element mean, OR a logged assignable cause (jam, interruption, material short) — either alone is sufficient grounds; neither alone is optional documentation.

## 3. Work-sampling worksheet (pilot → sized study → result)

Question: what fraction of the shift is the carton-taping operator away from the station (material delay, changeover, personal)?

**Pilot** (50–100 observations, random-interval): 60 observations, 21 "away" → p̂(pilot) = 0.35.

**Sample size for full study**, target 95% confidence, ±4% precision:
n = z²·p(1−p)/e² = 1.96² × 0.35 × 0.65 / 0.04² = 3.8416 × 0.2275 / 0.0016 = 0.8740/0.0016 = **546.2 → n = 547**.

**Full study**, random-interval schedule, 5 shifts over 2 weeks, 547 total observations:

| Category | Count | % |
|---|---|---|
| Actively taping | 368 | 67.3% |
| Away — material delay | 94 | 17.2% |
| Away — changeover | 51 | 9.3% |
| Away — personal | 34 | 6.2% |
| **Total away** | **179** | **32.7%** |

p̂ = 179/547 = 0.327. CI half-width: e = 1.96 × √(0.327 × 0.673 / 547) = 1.96 × √0.0004026 = 1.96 × 0.02006 = **0.0393 (±3.93%)**.

**95% CI: [28.8%, 36.6%]** — does not contain the book allowance (15%). Recommend a working allowance of 33% (mid-CI, rounded), and route the material-delay share (17.2% of the 32.7%, the largest single component) to the industrial engineer of record as a methods-improvement candidate — a chute-jam rate this high is a process finding, not a labor-allowance finding.

## 4. Line-balance audit template

Purpose: verify an engineer's balanced line is still holding on the floor. Technician re-times; does not rebalance.

Reference balance (from the industrial-engineer's line-rebalance readout): 3 stations, bottleneck cycle time 65.0 s, takt 67.5 s.

| Station | Assigned standard (s) | Re-timed avg, n=5 cycles (s) | Delta vs. standard | Flag (>10% over standard, 2+ consecutive shifts) |
|---|---|---|---|---|
| St.1 (T1+T2) | 65.0 | 66.2 | +1.8% | OK |
| St.2 (T3+T4) | 65.0 | 71.4 | +9.8% | Watch — 1 shift so far |
| St.3 (T5+T6) | 65.0 | 74.0 | +13.8% | **Flag — over 10% two consecutive shifts, escalate to IE of record** |

St.3's re-timed average now exceeds takt (67.5 s), meaning this station — not just the assigned standard — is the binding constraint on the shift's output; escalation note should say so explicitly rather than just reporting the percentage over standard.
