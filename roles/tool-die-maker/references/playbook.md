# Playbook

## Springback compensation calculation (filled example)

Station 4, 90° bend, 0.060" (16-gauge) mild steel, print tolerance ±0.5°.

| Step | Value |
|---|---|
| Print-called bend angle | 90° |
| Expected springback for this material/thickness | 2.5° |
| Punch angle without compensation | 90° (naive) |
| Resulting formed angle (naive, no compensation) | 90 + 2.5 = 92.5° — **0.5° tolerance exceeded by 2.0°** |
| Compensated punch angle | 90 − 2.5 = 87.5° |
| Resulting formed angle (compensated) | 87.5 + 2.5 = 90.0° (theoretical) |
| First-off sample measured actual | 90.1° — within ±0.5° tolerance |

## Die clearance reference table (filled example)

Punch-die clearance as a percentage of material thickness per side, mild steel.

| Material thickness | Clearance % per side | Clearance value (in.) |
|---|---|---|
| 0.030" (22 ga.) | 5% | 0.0015" |
| 0.060" (16 ga.) | 6% | 0.0036" |
| 0.125" (1/8") | 8% | 0.010" |
| 0.250" (1/4") | 10% | 0.025" |

Rule applied: clearance percentage increases with thickness because thicker stock needs more clearance to shear cleanly without excessive tonnage; using the 5% value from thin stock on 0.250" material would risk punch galling and premature die wear.

## Progressive die carrier-web layout (filled example)

6-station progressive die, strip width 2.000", minimum carrier web requirement: 15% of strip width (0.300") at any station.

| Station | Operation | Material removed at station | Remaining web width | Meets minimum (0.300")? |
|---|---|---|---|---|
| 1 | Pilot hole pierce | Minimal | 1.950" | Yes |
| 2 | Main blank pierce | Large | 0.450" | Yes |
| 3 | Notch | Moderate | 0.380" | Yes |
| 4 | 90° bend (forming, no material removed) | None | 0.380" (unchanged) | Yes |
| 5 | Trim | Large | 0.280" | **No — below 0.300" minimum** |
| 6 | Cutoff (part separation) | Full separation | 0 (part separates) | N/A |

Station 5's web falls below the 0.300" minimum before the part is meant to separate at station 6 — redesign station 5's trim geometry or move some of its material removal to station 4/6 rather than releasing the die for build as-is.
