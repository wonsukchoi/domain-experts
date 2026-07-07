# Playbook

Filled worksheets a stonemason (or the foreman coordinating a crew) actually runs before accepting a stone submittal, before setting anchors, before building a dry-stack wall, and before selecting a repair mortar on restoration work. Numbers below follow published standards (ASTM, Natural Stone Institute, NPS) and rule-of-thumb guidance from named sources — a specific project's structural drawings, engineer of record, and local code amendment always govern over a worked example in this document.

## 1. Stone density/absorption classification by type

| Stone type | Standard | Class/grade | Approx. density (pcf) | Max absorption | Notes |
|---|---|---|---|---|---|
| Limestone | ASTM C568 | Class I (low) | ~134 | 12.0% | Least freeze-thaw resistant; avoid as primary exterior facing in severe freeze-thaw climates |
| Limestone | ASTM C568 | Class II (medium) | ~144 | 7.5% | Common exterior default for northern climates |
| Limestone | ASTM C568 | Class III (high) | ~159 | 3.0% | Highest durability, cost premium |
| Marble | ASTM C503 | Groups I–IV | ~165–175 | 0.20% typical max | Absorption low across groups; group instead governs flexural/abrasion behavior |
| Granite | ASTM C615 | single spec | ~165–185 | 0.40% typical max | Lowest absorption of common building stones; still verify per quarry, not by name alone |
| Sandstone | ASTM C616 | Grade I–III (by absorption) | ~130–150 | varies widely, some >20% | Widest performance range of any common building stone — never assume "sandstone" implies durability without the data sheet |

**Selection rule:** pull the actual data sheet's absorption/density class for the specific quarry lot before accepting a submittal on color and finish. A commercial stone name ("limestone," "bluestone," "brownstone") is a marketing category, not a durability spec — two quarries selling under the same name can differ by a factor of four or more in absorption.

## 2. Stone-veneer anchor spacing and load worksheet

**Rule:** maximum tributary area per anchor = anchor's allowable rated load (lb) ÷ stone weight per sq ft (density × nominal thickness). Unlike a fixed brick-tie area cap, this number is recomputed for every stone type/thickness/anchor combination — there is no single reusable constant.

**Formula:** weight/sq ft = density (pcf) × thickness (ft); tributary cap = allowable anchor load ÷ weight/sq ft; columns = wall length ÷ horizontal spacing (round up); rows = wall height ÷ vertical spacing (round up); total anchors = columns × rows; check actual area/anchor = wall area ÷ total anchors ≤ tributary cap; check actual load/anchor = actual area/anchor × weight/sq ft ≤ allowable rated load.

**Filled example — 40 ft × 10 ft granite veneer, 2 in nominal thickness, density 175 pcf, anchor allowable load 120 lb:**

| Metric | Calculation | Result |
|---|---|---|
| Weight/sq ft | 175 pcf × 0.1667 ft (2 in) | 29.2 psf |
| Tributary cap | 120 lb ÷ 29.2 psf | 4.11 sq ft/anchor |
| Wall area | 40 ft × 10 ft | 400 sq ft |
| Horizontal spacing (set) | coordinated to stone module | 2 ft (24 in) |
| Max vertical spacing | 4.11 sq ft ÷ 2 ft | 2.05 ft, rounded down to 2 ft (24 in) |
| Columns | 40 ft ÷ 2 ft | 20 |
| Rows | 10 ft ÷ 2 ft | 5 |
| Total anchors | 20 × 5 | 100 |
| Actual area/anchor | 400 sq ft ÷ 100 | 4.0 sq ft (under the 4.11 cap) |
| Actual load/anchor | 4.0 sq ft × 29.2 psf | 116.8 lb (under the 120 lb allowable) |

Re-run this worksheet for every distinct stone type, thickness, and anchor product on a job — a granite base course and a limestone upper field on the same facade are two separate calculations, not one grid extended.

## 3. Dry-stack batter and thrust-line worksheet

**Rule:** a freestanding dry-laid wall needs the resultant thrust line to stay within the middle third of its cross-section at every course (Heyman, *The Stone Skeleton*, no-tension gravity-structure principle). Battering each face inward as the wall rises — commonly ~1:6 (about 10° off vertical) per the Dry Stone Conservancy/DSWA rule of thumb — keeps the thrust line centered without mortar.

**Rule of thumb (freestanding wall, no surcharge):** base width ≈ 0.75 × wall height; top width ≈ 0.4–0.5 × base width, tapering linearly between them.

**Filled example — 3 ft (36 in) tall freestanding dry-stack wall:**

| Metric | Calculation | Result |
|---|---|---|
| Base width | 0.75 × 36 in | 27 in |
| Top width | 0.45 × 27 in | ~12 in |
| Batter per face | (27 − 12) ÷ 2 ÷ 36 in rise | ~0.208 in/in ≈ 1:4.8, round to standard 1:6 template for a shallower, more conservative batter |
| Check | at 1:6 batter over 36 in rise, each face steps in 6 in, total width reduction 12 in | Top width = 27 − 12 = 15 in (still within the tapering range and comfortably keeps thrust line centered) |

**Retaining (surcharged) walls need an engineer, not this worksheet** — soil pressure moves the thrust line toward the face and the middle-third check above assumes a freestanding, unsurcharged wall only.

## 4. Historic mortar compatibility

| Property | Historic lime mortar (lime putty / NHL) | Modern Portland-cement mortar (Type S/M) |
|---|---|---|
| Typical compressive strength | ~50–150 psi | ~1,800–2,500 psi |
| Vapor permeability | High — mortar breathes, moisture migrates out through the joint | Low — moisture migration is pushed toward the stone face |
| Failure mode when mismatched | N/A (designed to be the sacrificial element) | Traps moisture; freeze-thaw and salt-crystallization pressure spalls the stone face instead of eroding the joint |

**Selection rule (per NPS Preservation Brief 2):** the repair mortar must be softer and more permeable than the stone it joins, not stronger. Match new mortar to the original's lime-to-cement ratio and strength range wherever the original composition can be determined (core sample, historical spec, or comparable-era reference); default to a lime-based or lime-heavy hybrid mix on pre-1930s stone construction absent other documentation, and never substitute a full Portland-cement mix "for durability" on a soft historic stone.

## 5. Bedding orientation quick check

| Orientation | Use | Failure risk if misapplied |
|---|---|---|
| Natural bed (bedding planes horizontal, matching quarry orientation) | Standard for vertical exposed faces — ashlar, veneer, wall stone | N/A — correct default |
| Face-bedded (bedding planes vertical, parallel to exposed face) | Never appropriate for load-bearing or weather-exposed vertical work | Delamination/exfoliation, often 5–15 years after installation |
| Edge-bedded | Acceptable only for thin units specifically cut and rated for it (some sills, copings) | Fine for its rated use; wrong choice for a full-height veneer unit |

Check bedding orientation on-site by sighting the stone's grain lines before setting — a unit cut from the same block can be face-bedded by mistake in the yard and look correct until it's set.
