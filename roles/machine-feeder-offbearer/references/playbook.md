# Playbook

Filled worksheets a feeder actually runs against a specific station, not descriptions of them — substitute the numbers for the machine in front of you.

## 1. Feed-rate-to-cycle-time worksheet (station capacity check)

Formula: **achievable rate (spm) = 60 ÷ measured feed-and-clear time (sec)**. Time 10 consecutive real cycles under the *current* stock, tooling, and reach configuration — not a one-off best-case cycle — and average them. Compare against nameplate stroke rate; the station's true achievable rate is the lower of the two, never the nameplate figure alone.

| Item | Value |
|---|---|
| Nameplate stroke rate | 20 spm (3.0 sec/stroke) |
| Measured feed-and-clear time (10-cycle average, post-changeover) | 4.1 sec |
| Achievable rate | 60 ÷ 4.1 = 14.6 spm |
| Shortfall vs. nameplate | (20 − 14.6) ÷ 20 = 26.8% |

**Reading the table:** a 26.8% shortfall traced to a measured feed-time increase is a capacity finding, not a pacing complaint — log it and escalate the layout/tooling change that caused it, rather than pushing the feeder to close the gap by hand speed.

**Escalation trigger:** any station where measured feed-and-clear time exceeds the machine's cycle time by more than 10% following a stock, tooling, or layout change — that's an unaddressed capacity limit, and pace pressure to close it is exactly what erodes safeguard margins.

## 2. Minimum safety distance worksheet — two-hand control

Formula: **Ds (in) = K × T**, where K = 63 in/sec (OSHA 1910.217(c) hand-speed constant) and T is the machine's measured stopping time in seconds, from the most recent stop-time monitor reading — not the machine's original spec-sheet value.

| Check point | Value |
|---|---|
| Most recent stop-time monitor reading (T) | 0.30 sec |
| Prior reading, two checks back | 0.24 sec |
| Required Ds = 63 × 0.30 | 18.9 in |
| Measured actual distance, control buttons to point of operation | 14 in |
| Margin | 14 − 18.9 = **−4.9 in (26% short)** |

**Reading the table:** a negative margin means a hand could physically reach the point of operation before the press could complete its stop, even though the two-hand control buttons work electrically and the operator is using them correctly. This is a layout finding, not a device malfunction — fix by moving the controls farther out, reducing T through brake service, or both.

**Stop-time drift note:** a reading trending upward across checks (0.24 → 0.30 sec here) increases the required Ds even if the current reading is still under any regulatory ceiling — recompute Ds at every new reading, don't wait for a violation to appear.

## 3. Minimum safety distance worksheet — presence-sensing device (light curtain)

Formula structure: **Ds = K × (Ts + Tc + Tr) + Dpf**, where Ts is the machine's stopping time, Tc is control system response time, Tr is the device's own response time, and Dpf is an added depth-penetration allowance based on the device's object-sensitivity resolution (per the device manufacturer's rating and ANSI B11.19 tables — a finer resolution requires a smaller Dpf but costs more and is more prone to nuisance trips from debris). Because Dpf depends on the specific device model's certified resolution, pull it from that device's documentation rather than assuming a generic figure — the K × T term is machine-specific and portable across devices; Dpf is not.

| Check point | Source |
|---|---|
| Ts (machine stopping time) | latest stop-time monitor reading |
| Tc + Tr (control and device response) | device and control system documentation |
| Dpf (depth penetration factor) | device's certified object-sensitivity rating, per manufacturer/ANSI B11.19 table |
| Measured installed distance | physical measurement, re-verified after any layout change |

**Escalation trigger:** installed distance below the computed Ds by any margin, or a device resolution/Dpf value that was never re-verified after a device swap or resolution setting change.

## 4. Point-of-operation guard opening-size-vs-distance (fixed barrier check)

For any fixed barrier guard around a feed or discharge opening — not a substitute for the Ds calculations above where a two-hand control or presence-sensing device is the safeguard, but the relevant check where a physical guard is used instead. Selected rows from the OSHA 1910.217 opening-size table (consult the full table for distances not shown):

| Distance of opening from hazard | Maximum opening dimension |
|---|---|
| 1/2 – 1-1/2 in | 1/4 in |
| 2-1/2 – 3-1/2 in | 1/2 in |
| 5-1/2 – 6-1/2 in | 3/4 in |
| 7-1/2 – 12-1/2 in | 1-1/4 in |
| 12-1/2 – 15-1/2 in | 1-1/2 in |
| 17-1/2 – 31-1/2 in | 2-1/8 in |

**Worked check:** a guard opening measures 1 in wide at a standoff of 6 in from the point of operation. The table maximum at 5-1/2–6-1/2 in standoff is 3/4 in — the opening is oversized by 1/4 in, meaning a finger can reach through to the hazard at a distance the guard was supposed to make impossible. Escalate for guard rework; do not accept it because "the guard is present."

## 5. Safeguard selection by hand-path variability

| Hand-path characteristic | Preferred device | Why |
|---|---|---|
| Fixed, repetitive placement point, high cycle rate | Pullback or restraint device | No stop/restart cycle loss per stroke; mechanically ensures hand withdrawal or prevents entry entirely |
| Variable hand position stroke to stroke (different part sizes/orientations) | Presence-sensing (light curtain) | Restraint/pullback assumes one fixed path — doesn't generalize to variable placement |
| Low-to-moderate cycle rate, operator-paced insertion | Two-hand control (concurrent, anti-tie-down, anti-repeat) | Forces both hands to a known safe location for the full hazardous part of the cycle |
| Point of operation partially exposed for tool access, no full barrier feasible | Hand-feeding tools (push stick, tongs, vacuum/magnetic lifter) as supplement | Keeps hands physically outside the point of operation on operations a barrier can't fully enclose — supplements, never substitutes for, an engineered device |

**Reconciling example:** a station switches from stamping identical washers (fixed hand path, high cycle rate — pullback was appropriate) to stamping brackets in three different orientations (hand path now varies by part). Continuing with the pullback device set up for the washer's single path leaves the varying bracket placements uncovered part of the time — the device needs to be reassessed for a light curtain or re-fixtured to restore a single fixed path, not left as-is because "it was fine for the last job."
