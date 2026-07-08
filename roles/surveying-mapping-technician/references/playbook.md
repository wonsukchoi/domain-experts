# Playbook

## 1. RTK GNSS fix-quality quick reference

| Indicator | Accept as final | Investigate/re-occupy | Reject |
|---|---|---|---|
| Fix type | Fixed | Float, held for <10 sec | Autonomous/DGPS-only |
| PDOP | ≤ 3.0 | 3.0–4.0, re-occupy after geometry change | > 4.0 for control-quality work |
| Baseline to single base | ≤ 10 km | 10–20 km, expect degraded precision, add a check shot | > 20 km on single base — switch to network/VRS or a closer base |
| Epoch count logged | ≥ 15 one-second epochs (or receiver-default averaging window) | 5–14 epochs, repeat occupation | Single instantaneous epoch for control work |
| Horizontal RMS/precision (as displayed) | ≤ 0.03 m for topo/control support | 0.03–0.05 m, note and consider re-occupation | > 0.05 m for anything feeding control |

Baseline-length figures assume single-base RTK; a well-configured network/VRS service extends the reliable range because it interpolates atmospheric error from multiple reference stations rather than depending on distance to one point. Always confirm the specific service's stated service radius rather than assuming the single-base figures apply.

**Re-occupation procedure when a shot is rejected:** move off the obstruction if PDOP is driven by sky blockage; otherwise wait 10–15 minutes for satellite constellation geometry to change, then re-occupy as a fresh, independent observation — not a continuation of the rejected one.

## 2. DR (Direct/Reverse) angle observation procedure

1. Point on the backsight in Direct (Face I) mode, record the horizontal angle.
2. Transit the telescope (rotate 180° in azimuth, flip vertical face) into Reverse (Face II), re-point on the same backsight, record the angle.
3. The two readings should differ by exactly 180° after accounting for the horizontal-circle convention the instrument uses; compute the mean angle.
4. Check agreement against the instrument's stated one-second/reading accuracy:

| Instrument class | Stated accuracy | DR pair agreement allowable |
|---|---|---|
| 1"-reading | 1" | ~2" |
| 2"-reading | 2" | ~4" |
| 5"-reading | 5" | ~10" |
| 10"-reading (construction-grade) | 10" | ~20" |

5. If the pair disagrees beyond the allowable, re-observe the whole pair — do not average a bad pair with a good one to "split the difference."
6. For rough construction layout (grading stakes, not control), a single-face shot is acceptable; state this explicitly in field notes so the office knows no DR check exists for that point.

## 3. Link traverse field closure — fillable procedure

```
Starting control:      CP-1  N ___________  E ___________
Backsight azimuth:     to ___________ , azimuth ___________
Course 1:  Bearing ___________  Distance ___________  ->  ΔN ___________  ΔE ___________
Course 2:  Bearing ___________  Distance ___________  ->  ΔN ___________  ΔE ___________
Course n:  Bearing ___________  Distance ___________  ->  ΔN ___________  ΔE ___________
Sum ΔN: ___________          Sum ΔE: ___________
Computed closing point:  N (start N + sum ΔN) ___________   E (start E + sum ΔE) ___________
Published closing point: CP-2  N ___________  E ___________
Misclosure:  ΔN (published - computed) ___________   ΔE ___________
Linear misclosure = sqrt(ΔN² + ΔE²) = ___________
Total traverse length = ___________
Closure ratio = length / linear misclosure = 1 : ___________
```

Compare the ratio against the day's classification (Section 5). If it fails, identify the course with the largest individual DR disagreement or the shortest, most obstructed sight line — that is almost always the weak leg — and re-observe it before moving off the closing control point.

## 4. Differential leveling loop closure

Third-order (typical engineering/construction-support) allowable closure, one-way distance or loop length in miles (M):

```
Allowable (ft) = 0.05 × sqrt(M)
```

Metric equivalent commonly cited for third-order work: C (mm) = 12 × sqrt(K), K in km. Second-order Class II work (tighter, used for structure settlement monitoring or precise benchmark densification): C (mm) = 8 × sqrt(K).

```
Sum of all backsight readings over the full loop:   ΣBS = ___________
Sum of all foresight readings over the full loop:   ΣFS = ___________
Closure = ΣBS - ΣFS (should be ~0 for a loop returning to the start elevation) = ___________
Allowable = 0.05 × sqrt(loop length in miles) = ___________
Pass/fail: ___________
```

If the loop fails, review individual setups for backsight/foresight distance imbalance greater than roughly 10 m — that setup is the first suspect — before re-running the whole loop.

**Field log — required fields per setup:**
```
Setup #:              3
Turning point ID:     TP-2
Backsight reading:    5.812
Foresight reading:    4.230
BS distance (paced):  ~150 ft
FS distance (paced):  ~145 ft
Rod/bubble checked:   yes
```
A setup missing the turning point ID or a distance estimate is treated as unverifiable, not as a minor omission.

## 5. Closure/tolerance classification by task type

| Task | Angular DR check required | Traverse closure ratio | Leveling order | Stakeout tolerance (typical) |
|---|---|---|---|---|
| Control/topo-control support | Yes | 1:10,000 or better | Third-order (0.05√M ft) | N/A |
| Precise structure/settlement monitoring | Yes | 1:20,000+ | Second-order Class II (8mm√K) | N/A |
| Building corner stakeout | No (single shot acceptable) | N/A | N/A | ±0.05 ft horizontal / ±0.02 ft vertical |
| Utility/grading stakeout | No | N/A | N/A | ±0.10 ft horizontal / ±0.05 ft vertical |
| Rough clearing/grading stakes | No | N/A | N/A | ±0.2 ft or per contract |

These figures are commonly applied field defaults, not a universal code — always confirm against the specific project's contract, spec section, or the party chief's instructions before applying them as the accept/reject line.

## 6. Stakeout verification, live check before setting a permanent hub

```
Design coordinate:     N ___________  E ___________   Elevation ___________
Measured (staked) pt:  N ___________  E ___________   Elevation ___________
ΔN = design - measured;  ΔE = design - measured
Horizontal offset = sqrt(ΔN² + ΔE²)
Vertical difference = design elevation - measured elevation
Compare both to Section 5's tolerance for this task type.
Pass -> set permanent hub/mark. Fail -> pull, adjust, and re-check before permanent.
```
