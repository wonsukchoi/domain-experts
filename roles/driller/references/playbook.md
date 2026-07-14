# Driller playbook

Filled calculations and sequences for the three recurring driller decisions: kill-sheet math, trip margin, and drilling-break flow checks. Numbers below are worked examples with plausible field values — substitute the well's actual TVD, mud weight, and shut-in readings.

## Kill-sheet math (Driller's Method)

Constant: hydrostatic gradient = mud weight (ppg) × 0.052 × true vertical depth (ft).

**Step 1 — formation pressure from shut-in readings.**

```
Hydrostatic  = Current MW × 0.052 × TVD
Formation P  = Hydrostatic + SIDPP
```

Example: MW 9.6 ppg, TVD 11,200 ft, SIDPP 280 psi.
Hydrostatic = 9.6 × 0.052 × 11,200 = 5,591.0 psi
Formation P = 5,591.0 + 280 = 5,871.0 psi

**Step 2 — kill mud weight.**

```
Kill MW = Current MW + SIDPP ÷ (0.052 × TVD)
```

Kill MW = 9.6 + 280 ÷ (0.052 × 11,200) = 9.6 + 280 ÷ 582.4 = 9.6 + 0.481 = 10.08 ppg
Check: 10.08 × 0.052 × 11,200 = 5,870.6 psi ≈ 5,871.0 psi formation pressure — reconciles (rounding).
Add site safety margin (0.1–0.3 ppg, per program): final kill MW = 10.08 + 0.2 = **10.28 ppg**, round to mixable increment → 10.3 ppg.

**Step 3 — initial and final circulating pressures (ICP/FCP).**

```
ICP = Slow Circulating Rate (SCR) pressure at kill rate + SIDPP
FCP = SCR pressure at kill rate × (Kill MW ÷ Current MW)
```

Example: SCR pressure at kill pump rate = 620 psi (measured before the well was shut in — always use a pre-kick SCR, never guess it after shut-in).
ICP = 620 + 280 = 900 psi
FCP = 620 × (10.3 ÷ 9.6) = 620 × 1.073 = 665 psi

**Step 4 — drill pipe pressure step-down schedule (Driller's Method, 2nd circulation).**
Step the drill pipe pressure from ICP to FCP in equal decrements over the pump strokes it takes for kill mud to reach the bit, holding casing pressure constant at the choke throughout. Example: 900 psi → 665 psi over 5 steps of 47 psi each as kill mud displaces down the string, casing pressure held flat.

| Step | Strokes pumped | Target drill pipe pressure |
|---|---|---|
| 0 (start) | 0 | 900 psi |
| 1 | 20% of strokes-to-bit | 853 psi |
| 2 | 40% | 806 psi |
| 3 | 60% | 759 psi |
| 4 | 80% | 712 psi |
| 5 (kill mud at bit) | 100% | 665 psi |

After kill mud reaches the bit, hold drill pipe pressure at FCP (665 psi) constant while kill mud displaces up the annulus and out.

## Trip margin table

Trip margin = extra static mud weight (or equivalent swab-safe pipe-speed limit) carried before pulling out of hole, to cover swab pressure from pipe movement.

| Hole condition | Typical trip margin | Notes |
|---|---|---|
| Normally pressured, vertical, gauge hole | 0.2 ppg | Standard baseline per most drilling programs |
| Depleted or known tight-margin zone | 0.4–0.5 ppg | Narrower pore-pressure/frac-gradient window |
| Washed-out or enlarged hole | 0.3 ppg + reduced trip speed | Larger annular clearance changes swab response; margin alone isn't sufficient — pair with speed limit |
| High-angle/extended-reach | 0.3–0.4 ppg + string-friction check | Torque/drag model should confirm pipe isn't being run faster than planned due to reduced hookload feel |

Swab-safe pipe speed: pull the string no faster than the rate the drilling program's swab/surge model clears for the current mud weight and hole geometry — typically stated in ft/min per stand, tightening as trip margin decreases. Never substitute "we've tripped this fast before" for the model's number when hole condition has changed (washout, new mud weight, deeper casing point).

## Drilling-break flow-check sequence

1. **Detect.** ROP increases beyond background trend with no WOB/RPM change (rule of thumb: >2x recent average ROP over the last 2–3 stands, or any step-change without a known cause).
2. **Stop and pick up off bottom.** Stop rotating and pumping only after picking the bit off bottom — don't shut pumps down while still on bottom, which can mask a differential-sticking risk if the well is also trending overbalanced.
3. **Flow-check.** Watch the flow line with pumps off for a fixed observation window (commonly 5–10 minutes, per program) — any sustained flow with pumps off is a positive flow check.
4. **Positive flow check → shut in immediately** per the well's control procedure; negative flow check (no flow) → resume drilling, but log the break and depth for the offset-well record regardless of outcome.
5. **Never resume drilling before the observation window completes** on the assumption "it looked negative already" — early resumption is how a slow kick gets missed on the first check and caught later, bigger.
