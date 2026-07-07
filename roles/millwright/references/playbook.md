# Playbook

Filled sequences a millwright actually runs, with real numbers and thresholds. Adapt the numbers to the OEM spec in front of you — these are worked starting points, not universal constants.

## 1. Rigging load calculation

**Step 1 — total weight and center of gravity.** Pull weight and dimension data per component from vendor drawings (never estimate a CG on an asymmetric skid). Moment balance about a reference point:

```
CG (in from reference) = Σ(component weight × distance from reference) ÷ total weight
```

*Example: reducer 6,600 lb centered at 30 in, motor 1,800 lb centered at 77 in, reference at reducer end (0 in):*
`CG = (6,600×30 + 1,800×77) / 8,400 = 336,600 / 8,400 = 40.07 in`

Pick point moves to the calculated CG, not the geometric center of the baseplate.

**Step 2 — sling angle load factor.** Per-leg tension in a multi-leg bridle:

```
Tension per leg = (Load ÷ number of legs) ÷ sin(included angle from horizontal)
```

| Included angle | Load factor (1/sin θ) | 8,400 lb load, 2-leg bridle — tension/leg |
|---|---|---|
| 90° | 1.000 | 4,200 lb |
| 60° | 1.155 | 4,850 lb |
| 45° | 1.414 | 5,940 lb |
| 30° | 2.000 | 8,400 lb |

**Rule:** never rig below 30° without recalculating capacity against the sling's rated WLL at that angle; default target is 45°+ for anything using more than half a sling's rated capacity.

**Step 3 — verify against sling WLL.** Cross-check calculated per-leg tension against the sling tag's rated capacity for the hitch type used (vertical, choker, or basket — each has a different WLL for the same sling per ASME B30.9 / Crosby tables). A sling adequate at 60° can be undersized for the same load at 30°.

## 2. Foundation leveling sequence

1. Rough-set baseplate/skid on leveling wedges or jackscrews.
2. Level to target flatness with a precision machinist level (0.0005 in/ft vial):

| Application | Target flatness |
|---|---|
| General rotating equipment (pumps, fans, conveyor drives) | ≤0.0005 in/ft |
| Turbine trains, precision high-speed rotating equipment | ≤0.0002 in/ft |
| Non-critical structural skids | ≤0.002 in/ft |

3. Dry-fit anchor bolts and check for interference before committing to a grout pour.
4. Check for soft-foot potential at every mounting point (see §4) before pouring — grout locks in any twist that isn't corrected first.

## 3. Grouting sequence and cure schedule (epoxy grout, manufacturer data-sheet example)

| Milestone | Time at 75°F ambient | Time at 50°F ambient |
|---|---|---|
| Walk-on / foot traffic | ~24 hr | ~48 hr |
| Anchor-bolt torque to spec | ~48–72 hr | ~4–6 days |
| Precision alignment work may begin | ~72 hr | ~6 days |
| Full design compressive strength | ~7 days | ~14 days |

**Rule:** below ~50°F ambient, double every interval unless the manufacturer's data sheet states otherwise for that product; never torque anchor bolts or begin alignment before the milestone tied to that action, regardless of schedule pressure.

## 4. Soft-foot check

1. With all anchor bolts finger-tight, place a dial indicator on the machine case near each foot.
2. Loosen one bolt at a time; record indicator movement as that bolt is loosened, then retightened.
3. Any foot moving more than 0.002 in is a soft foot — shim under that foot until movement is under 0.002 in before proceeding to laser alignment.
4. Never shim under the coupling to compensate for an uncorrected soft foot — it will pass a cold check and fail hot.

## 5. Precision alignment tolerance by RPM (offset / angularity, "acceptable" band)

| RPM | Offset (mils) | Angularity (mils/in) |
|---|---|---|
| 900 | ≤4.0 | ≤0.8 |
| 1,800 | ≤2.0 | ≤0.5 |
| 3,600 | ≤1.5 | ≤0.3 |

Tighten to the "excellent" band (roughly half these values) for critical or high-value rotating equipment, or where the OEM coupling spec calls for it explicitly. Always recheck hot (at operating temperature) where thermal growth between casings is material — a cold reading inside tolerance can walk outside it once the machine reaches operating temperature.

## 6. Gearbox backlash verification

1. Rotate the input or low-speed shaft (per OEM instruction) and measure backlash with a dial indicator at the coupling or output flange.
2. Take readings at a minimum of 4 rotational positions, 90° apart, to catch eccentricity or runout masquerading as a single "acceptable" reading.
3. Compare against the OEM spec band — commonly 0.001–0.003 in per inch of pitch diameter for enclosed industrial drives (AGMA 913-A98 guidance), or a direct OEM total-backlash figure (e.g., 0.008–0.015 in for a mid-size reducer).
4. Variation greater than roughly 30% across the four positions indicates eccentricity or shaft runout — flag for OEM review before startup, not a shim adjustment.

## 7. Run-in and acceptance sign-off

- No-load or low-load run for a minimum of 1–2 hours; record vibration (in/sec) and bearing/case temperature at 15-minute intervals.
- Acceptance requires a *flat or declining* vibration trend, not just a value under a generic threshold — a rising trend inside the alarm limit is still a fail-to-accept condition, since it hasn't stabilized yet.
- Sign-off sheet carries the actual measured numbers (rigging tension/angle, flatness, cure-hold timestamps, alignment offset/angularity, backlash) — never a checkbox without the underlying figure.
