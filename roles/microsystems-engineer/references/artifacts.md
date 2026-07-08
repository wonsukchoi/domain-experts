# Artifacts

Filled worksheets and memo templates for the deliverables a microsystems engineer produces at design review, layout freeze, and pilot-lot failure analysis. Numbers below extend the SKILL.md worked example (5-layer poly-Si accelerometer, g = 2.4 µm sense gap) plus independent worked cases for the templates that example doesn't exercise.

## 1. Pull-in / travel-budget worksheet

Formula: `x_pi (pull-in limit) = g / 3`, where g is the physical sense/actuation gap. Usable design travel should sit at 70-80% of x_pi, leaving margin for the mechanical stop.

| Device | Physical gap g | Pull-in limit x_pi = g/3 | Stop placement (75% of x_pi) | Usable signal range |
|---|---|---|---|---|
| Accelerometer proof mass (worked example) | 2.4 µm | 0.80 µm | 0.60 µm | 0-0.60 µm before stop contact |
| Comb-drive resonator (lateral) | 3.0 µm | 1.00 µm | 0.75 µm | 0-0.75 µm |
| RF MEMS switch (vertical) | 1.5 µm | 0.50 µm | 0.375 µm | 0-0.375 µm |
| Micromirror torsion actuator | 4.0 µm | 1.33 µm | 1.00 µm | 0-1.00 µm |

**Check order at design review:** (1) confirm g is the *as-fabricated* gap from the process's sacrificial-layer thickness spec, not the drawn/nominal gap; (2) compute x_pi; (3) confirm stop placement is strictly less than x_pi with the 20-25% margin above, never placed past x_pi "to gain range"; (4) if the design needs more than x_pi of travel, flag for leveraged or charge-controlled actuation — do not solve it by moving the stop.

**Template line for a design-review comment:**
"Gap g = [N] µm → pull-in limit x_pi = [N/3] µm. Stop currently specified at [N] µm, which is [inside/past] the pull-in limit. [Approve as-is / Move stop to [0.75 × x_pi] µm before layout freeze.]"

## 2. Process-capability checklist, by foundry production tier

DRIE aspect-ratio capability is tier-dependent — check the layout against the tier the part will actually ship on, not the foundry's best demonstrated number.

| Parameter | R&D tier | Development tier | Mass-production tier |
|---|---|---|---|
| DRIE aspect ratio (max) | ~80:1 | ~60:1 | ~40:1 |
| Typical yield expectation at rated AR | Not tracked (single-lot) | 70-85% | >95% |
| Minimum feature size (named 5-layer poly-Si process) | 1.5 µm | 2.0 µm | 2.0 µm |
| Structural layer count available | Up to 5 (full stack) | 5 | 3-5 (customer-selectable) |
| CD (critical dimension) tolerance | ±0.25 µm (uncontrolled) | ±0.15 µm | ±0.10 µm, SPC-tracked |

**Layout-freeze gate (run every item before releasing to fab):**
1. Pull the target lot's declared production tier from the fab quote, not the PDK's headline capability number.
2. For every DRIE feature, compute drawn aspect ratio = trench depth / trench width. Compare against the tier's max AR with a 15% design margin (e.g., mass-production 40:1 → design ceiling 34:1).
3. Confirm minimum feature size against the tier column, not the process's absolute floor.
4. Cross-check CD tolerance against the design's stated mechanical tolerance stack-up (e.g., a spring constant that assumes ±0.05 µm CD will not hold at ±0.10 µm production tolerance — recompute stiffness sensitivity before freeze).
5. If any item fails at the target tier but passes at R&D tier, the design is **not** ready for that lot type — route back to layout, do not waive on the R&D number.

## 3. Qualification test-plan skeleton (shock + thermal cycling + hermeticity)

Built to JEDEC JESD22-B104 (shock) / JESD22-A104 (temperature cycling) and MIL-STD-883 Method 1014 (hermeticity), filled for a representative automotive-grade MEMS accelerometer program.

```
QUALIFICATION TEST PLAN — [Device], [Program/Lot ID]

1. MECHANICAL SHOCK (JESD22-B104, Condition [X])
   Peak acceleration:      1,500 g
   Pulse duration:         0.5 ms, half-sine
   Axes:                   6 (±X, ±Y, ±Z)
   Shocks per axis:        5
   Pass criterion:         Post-shock offset drift < 2% FSO; no self-test failure

2. TEMPERATURE CYCLING (JESD22-A104, Condition [X])
   Range:                  -40°C to +125°C
   Ramp rate:               ≥10°C/min
   Dwell at extremes:       15 min minimum
   Cycles:                  500 (automotive-grade default; 1,000 for safety-critical)
   Pass criterion:         Parametric drift within datasheet limits; no delamination

3. HERMETICITY (MIL-STD-883 Method 1014, He-bomb)
   Bomb condition:          [pressure/time per method table, by cavity volume]
   Cavity volume (actual):  [N] cm³
   Method resolution floor: ~5e-11 atm·cm³/s
   Pass criterion:          Measured leak rate < method's calculated reject limit
   >>> If cavity volume < 1e-3 cm³: flag resolution-floor gap explicitly (see
       artifact 4) and specify a confirmatory higher-resolution method
       (accumulation or tracer-gas) on a subsample before closing hermeticity.

4. DUTY-CYCLE / SUSTAINED-ACTUATION LIFE TEST (supplements peak-voltage-only qual)
   Drive pattern:           Field-representative asymmetric duty cycle (not 50/50)
   Temperature:             Operating max, sustained (not transient)
   Duration:                [N] equivalent field-years, accelerated per Arrhenius model
   Pass criterion:          Hinge/flexure residual set < [N]% of stroke at test end

SIGN-OFF: Reliability engineer + design owner, both required before lot release.
```

## 4. Hermeticity resolution-floor cross-check

Method 1014's He-bomb resolution floor (~5×10⁻¹¹ atm·cm³/s) is fixed regardless of cavity size — the risk is that a fixed-resolution test under-resolves a small cavity's actual leak-rate requirement.

| Cavity volume | Method 1014 resolution floor | Leak rate needed to matter (order-of-magnitude) | Floor vs. requirement |
|---|---|---|---|
| 5×10⁻⁴ cm³ (worked example) | 5×10⁻¹¹ atm·cm³/s | ~5×10⁻¹² atm·cm³/s | Floor is ~10x coarser — flag |
| 5×10⁻³ cm³ | 5×10⁻¹¹ atm·cm³/s | ~5×10⁻¹¹ atm·cm³/s | Floor roughly matches — acceptable |
| 5×10⁻² cm³ | 5×10⁻¹¹ atm·cm³/s | ~5×10⁻¹⁰ atm·cm³/s | Floor resolves with margin — no flag |

**Rule of thumb applied above:** for cavities under ~10⁻³ cm³, treat a Method 1014 pass as necessary but not sufficient; require either a confirmatory higher-resolution method or a getter/desiccant plus tightened seal spec independent of the pass result.

## 5. Failure-analysis / design-change memo (format + skeleton)

The filled, as-issued example memo lives in SKILL.md's Worked Example section (same pilot-lot accelerometer case) — see that file for the literal issued text rather than a second copy here. Below is the reusable skeleton with the field-by-field intent explained.

**Template skeleton for a new memo (fill every field, never leave a bracket in the issued version):**

```
FAILURE ANALYSIS & DESIGN CHANGE MEMO — [Device], [Lot ID], [Date]

Finding:        [Failure rate]% on [test] traced to [mechanism], computed as
                 [formula with actual numbers] against [spec/limit].
Change:         [Specific dimensional/process change with margin stated].
Secondary
finding:        [Any co-occurring risk, e.g. test-method resolution gap].
Cost note:      [Mask-only revision vs. process-deviation vs. new qual — dollar figure].
Verification
plan:           [Re-test method, target pass rate, and what closes the finding].
```

## 6. MPW shuttle vs. dedicated lot — decision worksheet

| Factor | MPW shuttle | Dedicated lot |
|---|---|---|
| Typical NRE | Shared maskset cost, ~$5k-15k per design slot | ~$50k+ for a 3-5 wafer lot |
| Per-wafer cost | Bundled into slot fee | ~$10k/wafer additional |
| Process flexibility | Locked to foundry's standard process/PDK | Can deviate (custom layer, thickness, material) |
| Schedule | Fixed shuttle calendar (may be months out) | Scheduled to program need |
| Best fit | First prototype, process-standard design, cost-sensitive validation | Design needs a non-standard process step, or shuttle schedule doesn't fit program |

**Decision rule applied:** default to MPW for a first prototype unless the design requires a process deviation the foundry's standard shuttle offering doesn't support — in that case the dedicated lot's cost is the price of the deviation, not a discretionary choice.
