# Playbook

Filled thresholds and formulas a rebar worker actually runs against. Verify against the project's placing drawings, bar-bending schedule, and governing specification in front of you — these are the code/standard floors, not a substitute for the engineered detail.

## 1. Bar size reference (ASTM A615/A706)

| Bar size | Diameter (db) | Area |
|---|---|---|
| #3 | 0.375 in | 0.11 in² |
| #4 | 0.500 in | 0.20 in² |
| #5 | 0.625 in | 0.31 in² |
| #6 | 0.750 in | 0.44 in² |
| #7 | 0.875 in | 0.60 in² |
| #8 | 1.000 in | 0.79 in² |
| #9 | 1.128 in | 1.00 in² |
| #10 | 1.270 in | 1.27 in² |
| #11 | 1.410 in | 1.56 in² |
| #14 | 1.693 in | 2.25 in² |
| #18 | 2.257 in | 4.00 in² |

## 2. Concrete cover requirements (ACI 318 Table 20.5.1.3.1, excerpt)

| Exposure condition | Bar size | Minimum cover |
|---|---|---|
| Cast against and permanently exposed to earth | All sizes | 3 in |
| Exposed to weather or in contact with ground (formed) | #6–#18 | 2 in |
| Exposed to weather or in contact with ground (formed) | #5 and smaller | 1.5 in |
| Not exposed to weather/ground — slabs, walls, joists | #14–#18 | 1.5 in |
| Not exposed to weather/ground — slabs, walls, joists | #11 and smaller | 3/4 in |
| Not exposed to weather/ground — beams, columns (primary reinforcement, ties, stirrups) | All sizes | 1.5 in |

**Rule:** cover is measured to the nearest surface of the bar, not the tie wire or the chair — and the exposure condition, not the element type alone, sets which row applies.

## 3. Development length (ld) — simplified equation (ACI 318 §25.4.2)

**ld = (fy × ψt × ψe) / (divisor × λ × √f'c) × db**

| Bar size | Spacing/cover condition | Divisor |
|---|---|---|
| #6 and smaller | Clear spacing ≥ 2db and clear cover ≥ db (favorable) | 25 |
| #6 and smaller | Other cases | 20 |
| #7 and larger | Clear spacing ≥ 2db and clear cover ≥ db (favorable) | 20 |
| #7 and larger | Other cases | 15 |

**ψ-factors:**
- **ψt (top-bar factor):** 1.3 if horizontal reinforcement is placed with more than 12 in of fresh concrete cast below the bar's development length or splice; 1.0 otherwise.
- **ψe (epoxy factor):** 1.5 if clear cover < 3db or clear spacing < 6db; 1.2 otherwise; 1.0 for uncoated bar. ψt × ψe need not exceed 1.7.
- **λ (lightweight factor):** 1.0 normal-weight concrete; 0.75 lightweight (unless splitting-tensile strength is specified, then an intermediate value applies).

*Example: #6 bottom bar (db = 0.75 in), epoxy-coated, Grade 60 (fy = 60,000 psi), f'c = 5,000 psi, favorable spacing/cover (divisor 25), ψt = 1.0, ψe = 1.5, λ = 1.0. √5,000 = 70.7. ld = (60,000 × 1.0 × 1.5) / (25 × 1.0 × 70.7) × 0.75 = 90,000 / 1,767.5 × 0.75 = 50.9 × 0.75 = 38.2 in.*

**Rule:** ld scales linearly with fy — a grade substitution (e.g., Grade 60 → Grade 75) requires recomputing, not reusing, the drawing's stated length; see §5.

## 4. Lap splice classification and length

| Class | Multiplier | When it applies |
|---|---|---|
| Class A | 1.0 × ld | ≤50% of bars spliced within the required lap length **and** area of steel provided ≥ 2× area required |
| Class B | 1.3 × ld | All other cases — the default when the percentage-spliced or area check hasn't been confirmed |

*Example continued: Class B splice for the #6 bar above = 1.3 × 38.2 = 49.6 in → round up to 50 in.*

**Rule:** Class B is the safe default; downgrading to Class A requires actively confirming both conditions, not just assuming a low splice percentage.

## 5. Grade substitution scaling

Because ld ∝ fy, substituting a higher grade at the same bar size and condition scales the required lap length by the grade ratio:

*Example: same #6 bar, Grade 75 substituted for specified Grade 60. ld scales by 75,000/60,000 = 1.25×: 38.2 × 1.25 = 47.75 in. Class B = 1.3 × 47.75 = 62.075 → round up to 63 in — 13 in longer than the Grade 60 lap (50 in).*

**Rule:** never tie a substituted higher-grade bar at the original grade's lap length — recompute, and flag the substitution to the engineer of record regardless of direction (grade up or down).

## 6. Bar grade mill-mark identification (ASTM A615/A706)

Mark order on the bar: producer's mill mark → bar size number → bar type → grade mark.

| Type | Grade | Mill-mark grade indicator |
|---|---|---|
| A615 (deformed billet-steel) | Grade 60 | No grade mark, or numeral "60" |
| A615 | Grade 75 | One continuous longitudinal line, or numeral "75" |
| A615 | Grade 80 | Two continuous lines, or numeral "80" |
| A615 | Grade 100 | Three continuous lines, or numeral "100" |
| A706 (low-alloy, weldable) | Grade 60 | Marked "W", no grade line |
| A706 | Grade 80 | Marked "W", one continuous line |

**Rule:** read the mark on the bar itself before tying a splice — delivery tickets and bundle tags describe what was ordered, not necessarily what's in the bundle.

## 7. Bar supports (chairs/bolsters) — CRSI standard types

| Type | Use | Typical stock heights |
|---|---|---|
| SB (Slab Bolster) | Continuous support, single (bottom) mat in slabs | 3/4 in–2 in, in 1/4–1/2 in increments |
| SBU (Slab Bolster Upper) | Upper-mat support in two-mat slabs | Same range as SB |
| HC (Individual High Chair) | Point support for top mat, low-congestion areas | 3 in–15 in, 1 in increments |
| CHC (Continuous High Chair) | Continuous top-mat support, congested or heavy mats | Same range as HC |
| BB / BBU (Beam Bolster / Upper) | Beam bottom/top mat support | Sized to beam cover requirement |

**Spacing:** CRSI default is 4 ft o.c. for standard slab bolsters under #5 and smaller bars in low-traffic pours; tighten to 3 ft o.c. or less for #6 and larger bottom mats, elevated decks, or pump-hose traffic — sag between supports shifts cover during the pour, not before it.

**Height selection:** required chair height = slab (or member) thickness − required cover on that face − bar diameter (adjust for opposing-face bar layers where applicable). When the exact height isn't a stock size, round to the next size that **increases** cover, never the size that reduces it.

*Example: 8 in slab, top cover 1.5 in required, top bar #5 (db = 0.625 in). Required CHC height = 8 − 1.5 − 0.625 = 5.875 in. Stock options 5.75 in and 6 in: 5.75 in gives 8 − 5.75 − 0.625 = 1.625 in cover (acceptable); 6 in gives 8 − 6 − 0.625 = 1.375 in cover (deficient by 0.125 in). Specify 5.75 in.*

## 8. Epoxy-coating damage thresholds (ASTM A775/D3963, CRSI field practice)

- **Individual holiday/damage spot:** patch any area of exposed steel exceeding roughly 0.1 in² with a compatible epoxy patch compound before placement.
- **Cumulative damage:** patch repair required once total damaged area on a bar exceeds roughly 2 in² per linear foot.
- **Outright rejection:** reject the bar if damage exceeds roughly 5% of surface area within any 12 in section, or if damage is clustered densely enough that patch repair cannot restore full coverage.
- **Handling:** use padded/nylon-covered slings and cushioned supports for coated bundles; where a coated bar rests on an uncoated steel chair, use a plastic-tipped or coated chair contact point to avoid abrading the coating at the support.

**Rule:** these figures are commonly applied industry practice, not a universal numeric code limit — confirm the governing project specification's exact repair/rejection thresholds before a large rejection call.

## 9. Standard hook and minimum bend diameters (ACI 318 Table 25.3.1)

| Bar size | Minimum bend diameter (standard hook) |
|---|---|
| #3–#8 | 6 × db |
| #9–#11 | 8 × db |
| #14–#18 | 10 × db |
| #3–#5 (stirrup/tie hooks) | 4 × db |

**Standard hook extensions:** 90° hook — 12 db minimum extension beyond the bend; 180° hook — 4 db minimum extension beyond the bend (not less than 2.5 in).

**Rule:** a bend tighter than the minimum diameter for that bar size cracks the bar's core or damages coating at the bend — never field-tighten a bend radius to fit a congested corner.
