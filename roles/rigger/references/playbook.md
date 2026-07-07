# Playbook

Filled calculations a rigger actually runs, with real numbers and thresholds. Verify against the manufacturer's chart or the crane's load chart in front of you — these are worked starting points, not universal constants.

## 1. Center of gravity and multi-point load share

**Step 1 — CG from vendor data.** Never estimate on an asymmetric load.

```
CG (in/ft from reference) = Σ(component weight × distance from reference) ÷ total weight
```

**Step 2 — load share between two pick points**, treating the points as simple-beam supports:

```
R_near = W × (dist from far point to CG) ÷ span between points
R_far  = W × (dist from CG to near point) ÷ span between points
```

*Example: 120,000 lb load, CG at 26 ft from reference, pick points at 10 ft and 50 ft (40 ft span):*
`R_A (at 10 ft) = 120,000 × (50 − 26) ÷ 40 = 72,000 lb`
`R_B (at 50 ft) = 120,000 × (26 − 10) ÷ 40 = 48,000 lb`
Check: 72,000 + 48,000 = 120,000 lb.

**Rule:** an even split by pick-point count is only correct when the CG sits exactly at the geometric midpoint between points — verify, never assume.

## 2. Sling angle and hitch-type derating

**Per-leg tension**, vertical hitch, multi-leg bridle:

```
Tension per leg = (Load ÷ number of legs) ÷ sin(included angle from horizontal)
```

| Included angle | Load factor (1/sin θ) | 8,400 lb load, 2-leg bridle — tension/leg |
|---|---|---|
| 90° | 1.000 | 4,200 lb |
| 60° | 1.155 | 4,850 lb |
| 45° | 1.414 | 5,940 lb |
| 30° | 2.000 | 8,400 lb |

**Rule:** never rig below 30° without recalculating against the sling's rated WLL at that angle; default target 45°+ for anything using more than half a sling's rated capacity.

**Choker-hitch angle derate** (choke angle measured at the choke point, percent of the sling's tagged choker rating):

| Choke angle | % of choker-rated capacity |
|---|---|
| ≥120° | 100% |
| 90°–119° | 87% |
| 60°–89° | 74% |
| 30°–59° | 62% |
| <30° | not recommended — reconfigure the hitch |

**Basket-hitch angle derate** (basket at 90° = 2× the sling's vertical WLL; derates below 90° the same way a vertical bridle leg does):

| Basket angle from horizontal | % of basket (2×) rating |
|---|---|
| 90° | 100% |
| 60° | 87% |
| 45° | 71% |
| 30° | 50% |

## 3. D/d ratio derating (sling bearing point to pin/shackle/spreader-bar diameter)

```
D/d = diameter of pin, shackle bow, or spreader-bar trunnion ÷ nominal sling body diameter
```

| D/d ratio | Approx. wire rope sling efficiency (% of tagged WLL) |
|---|---|
| 1:1 | 75% |
| 2:1 | 85% |
| 4:1 | 93% |
| 5:1 | 95% |
| 6:1 | 96% |

*Example: 1-1/4 in wire rope sling (58,000 lb tagged vertical WLL) reeved over a 3.25 in shackle pin: D/d = 3.25 ÷ 1.25 = 2.6:1 → ~87% efficiency → effective capacity 58,000 × 0.87 = 50,460 lb. Upsizing to a 5 in pin gives D/d = 4:1 → 93% → 53,940 lb effective.*

**Rule:** treat a tagged WLL as unusable at the bearing point until derated for D/d; default to sizing hardware for D/d ≥ 5:1 when margin matters, and never accept D/d under 4:1 on a critical lift without recalculating the derated capacity against the required tension.

## 4. Critical-lift trigger checklist

A lift is critical (requires an engineered lift plan, PE review where the site procedure calls for it, and a documented pre-lift meeting) if **any** of the following is true:

- Calculated load at the crane's actual working radius exceeds **75% of charted capacity**.
- The lift requires **more than one crane** (tandem/multi-crane).
- The load path crosses **occupied space, a public way, or live process equipment**.
- The load, rigging configuration, or pick-point geometry is **non-standard** (asymmetric CG, custom spreader, personnel platform).
- The load or asset value exceeds the site's stated critical-lift dollar or safety threshold.

Engineered lift plan contents at minimum: load weight and CG source, crane chart(s) with radius and percent utilization, rigging diagram with hitch type/angle/D-d for every sling and hardware piece, load-share calculation for multi-point/multi-crane picks, exclusion-zone radius and basis, tag-line assignments, and the sign-off chain required by the trigger.

## 5. Tandem (multi-crane) lift contingency

1. Calculate each crane's load share from CG and rigging-point geometry (§1).
2. Add **10–15% contingency** to each crane's calculated share for rigging-point tolerance, crane positioning error, and load-shift risk during the pick — never plan to the bare calculated number on a multi-crane lift.
3. Verify each crane's contingency-loaded share against **its own** load chart at **its own** working radius — cranes at different radii do not share a single capacity check.
4. If either crane's contingency-loaded share exceeds 75% of its own chart capacity, the lift is critical on that basis alone, independent of the multi-crane trigger.

## 6. Exclusion zone and tag-line planning

```
Exclusion radius = greater of:
  (a) 125% of the maximum working boom radius used during the lift
  (b) the load's longest dimension + 20 ft
```

*Example: 75 ft boom radius (a → 93.75 ft) vs. 60 ft load + 20 ft (b → 80 ft) — (a) governs at 93.75 ft in this case; use whichever value is larger for the actual lift.*

Assign one dedicated rigger per tag line (minimum two on any load over ~20 ft or with rotation risk), radio-linked to both crane operators before the load leaves the ground. Barricade the full exclusion radius, not just the area directly under the boom — swing and drop paths extend past the visual "under the load" zone.

## 7. Pre-use inspection — numeric rejection criteria

**Wire rope sling — remove from service if:**
- 10 randomly distributed broken wires in one rope lay, or 5 broken wires in one strand in one lay.
- Wear/scraping exceeding 1/3 the original diameter of outside individual wires.
- Kinking, crushing, bird-caging, or core protrusion.
- Heat or arc damage of any degree.
- End attachment (hook, eye, splice) cracked, deformed, or worn more than 10%.

**Synthetic (web/round) sling — remove from service if:**
- Acid, caustic, or UV damage (discoloration, brittleness).
- Melting, charring, or snags/punctures/tears/cuts in the load-bearing fabric.
- Broken or worn stitching in a load-bearing splice.
- Any knot in the sling body.
- Missing or illegible capacity tag.

**Chain sling — remove from service if:**
- Wear exceeding 10% of the original diameter of any link.
- Stretch beyond the manufacturer's specified elongation limit (commonly ~3%).
- Nicked, gouged, or twisted/bent links.

**Hardware (shackles, master links) — remove from service if:**
- Visible deformation, crack, or nick in a load-bearing surface.
- Pin doesn't seat fully or shows thread damage.
- Missing or illegible working-load-limit stamp.
