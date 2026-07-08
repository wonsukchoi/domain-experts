# Playbook

Filled procedures for the four artifacts this role produces most often: a lockout/tagout zero-energy verification, a joint mastering/pulse-count check, a TCP calibration residual check, and a cycle-time segment breakdown. Populate with the actual cell's numbers; the structure and arithmetic below are real and reconcile.

## Lockout/tagout — zero-energy verification checklist

**Cell:** 6-axis robot with servo drive (electrical), torch-cleaning station cylinder (pneumatic), and a counterbalanced J3 (gravitational). Three independent energy sources — verify each, do not infer from one.

| Step | Source | Isolation action | Verification method | Accept value | Measured |
|---|---|---|---|---|---|
| 1 | Electrical (480 VAC main / servo DC bus) | Open and lock/tag main disconnect | Attempt cycle start at pendant with lock applied; meter DC bus terminals | No response; bus < 50 VDC (NFPA 70E touch-safe reference) | No response; 6.2 VDC |
| 2 | Pneumatic (90 psi shop air to torch-cleaner cylinder) | Close and lock/tag isolation valve; open bleed port | Read local pressure gauge downstream of isolation valve | 0 psi | 0 psi |
| 3 | Hydraulic (if present — not on this cell) | Close and lock/tag isolation valve; cycle bleed-down per OEM procedure | Read accumulator gauge | 0 psi/bar | N/A this cell |
| 4 | Gravitational / counterbalanced axis (J3) | Drive to mechanical-stop rest pose before power-down; do not rely on brake alone | Visual confirmation of rest-pose position; attempt to move axis by hand at the flange (should not move) | Axis at rest pose, no movement under manual force | Confirmed |

**Rule:** a single main-disconnect lock does not certify the cell as zero-energy. Every row above must independently pass before physical entry — a passing row 1 with an unchecked row 2 or 4 is an incomplete LOTO, not a conservative one.

## Joint mastering — pulse-count verification

**Encoder:** 17-bit single-turn absolute (131,072 counts/rev), gear reduction N to the joint (varies by axis — use the nameplate value for the specific joint).

**Formula:**
```
Δcounts = current_raw_count − reference_raw_count
Δθ_motor (deg) = Δcounts × (360 / 131,072)
Δθ_joint (deg) = Δθ_motor / N
```

**Worked example (J2, N = 121:1):**
Reference (nameplate/last-good mastering) = 812,304 counts. Current fixture-read = 812,558 counts.
Δcounts = 812,558 − 812,304 = **254**.
Δθ_motor = 254 × (360/131,072) = 254 × 0.0027466° = **0.6976°**.
Δθ_joint = 0.6976 / 121 = **0.00577°**.

**Acceptance table (this robot family's maintenance manual — verify against the actual model manual before use):**

| Δcounts at this encoder resolution | Disposition |
|---|---|
| < 1,000 | Accept fixture (quick) mastering as new reference; log and proceed |
| 1,000 – 5,000 | Investigate before accepting — check encoder cable seating, battery voltage log, and fixture seating before logging as new reference |
| > 5,000 | Reject fixture mastering; perform full zero-position remaster per OEM procedure, not a fixture quick-master |

## TCP calibration — 4-point touch-up residual check

**Method:** jog the TCP to a fixed reference point from 4 distinct arm orientations; the controller's built-in routine computes the pivot point and reports per-touch residual distance from that pivot.

**Worked example:**

| Touch # | Residual (mm) |
|---|---|
| 1 | 0.18 |
| 2 | 0.22 |
| 3 | 0.31 |
| 4 | 0.15 |

Mean = (0.18+0.22+0.31+0.15)/4 = 0.86/4 = **0.215 mm**.
Deviations from mean: −0.035, 0.005, 0.095, −0.065. Squared: 0.001225, 0.000025, 0.009025, 0.004225. Sum = 0.0145. Variance = 0.0145/4 = 0.0036225. σ = √0.0036225 = **0.0602 mm**.

**Pattern check:** plot the 4 residual vectors (not just magnitudes) if the controller reports direction — a cluster offset consistently in one direction (e.g., all touches read +0.3 mm along the same world-frame axis) is a systematic error (mastering or fixture problem); a cluster scattered in different directions at similar magnitude is normal probing variation.

**Acceptance:** compare max individual residual against the process tolerance for the application:

| Process | Typical tolerance (verify against the actual weld/process spec in use) |
|---|---|
| Arc welding | ±0.5 mm |
| Material handling / palletizing | ±1.0–2.0 mm |
| Vision-guided pick | ±0.2–0.3 mm |
| Laser cutting/welding | ±0.1 mm |

Worked example max residual (0.31 mm) against ±0.5 mm arc-welding tolerance: 0.31/0.5 = 62% of tolerance consumed — accept.

## Cycle-time regression — segment breakdown

**Method:** time each program segment independently (servo trend or PLC I/O trace timestamps, not the aggregate HMI cycle counter), compare against the segment's spec baseline, rank by absolute delta.

| Segment | Spec (s) | Measured (s) | Δ (s) | % of total Δ |
|---|---|---|---|---|
| Approach move | 1.8 | 2.1 | +0.3 | 13.0% |
| Weld arc time | 6.2 | 6.2 | 0.0 | 0.0% |
| Retract move | 1.6 | 1.9 | +0.3 | 13.0% |
| Part-present handshake wait | 1.4 | 3.1 | +1.7 | 73.9% |
| Fixed index/clamp (unchanged both) | 1.5 | 1.5 | 0.0 | — (excluded from ranking) |
| **Total** | **12.5** | **14.8** | **+2.3** | **100%** |

**Rule:** rank by seconds (absolute delta), not percentage of the segment's own spec time — a segment that's "only" up 21% but contributes 1.7 of a 2.3 s total delta is the actual driver; a segment up 17% (approach move) contributing 0.3 s is not, even though both look similar as raw percentages of their own baseline.
