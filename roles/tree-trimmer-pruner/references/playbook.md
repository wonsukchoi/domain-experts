# Playbook

Filled worksheets for the three calculations that show up on almost every job: is this union a defect, can this crew legally work this close to the wire, and will the rigging hold the load. Numbers below are worked examples, not universal constants — remeasure on site.

## 1. Structural risk rating (TRAQ-style matrix)

Rate each axis independently, then combine. Don't shortcut straight to a rating from gut feel — write down what put you in each cell.

**Likelihood of failure** (based on defect severity — decay extent, crack, lean, union quality):

| Rating | Criteria |
|---|---|
| Improbable | No visible defect; sound union or trunk |
| Possible | Minor defect (small deadwood, shallow seam) unlikely to fail before next inspection cycle |
| Probable | Clear defect (included bark, decay column >30% of cross-section, active crack) likely to fail within the tree's expected inspection interval |
| Imminent | Failure has begun or is underway (active split, hinge already cracking, root plate lifted) |

**Likelihood of impacting a target** (based on target occupancy and fall/drop path):

| Rating | Criteria |
|---|---|
| Very low | No target within range of the piece if it fails |
| Low | Target occasionally within range (rarely-used path) |
| Medium | Target regularly within range (driveway, walkway) |
| High | Target constantly within range (occupied structure, main road) |

**Consequences** (based on target value/occupancy if struck):

| Rating | Criteria |
|---|---|
| Negligible | No meaningful damage or injury potential |
| Minor | Small property damage, no injury potential |
| Significant | Serious property damage, injury potential |
| Severe | Structural damage to occupied building, high injury/fatality potential |

**Combined risk rating** (read off likelihood-of-failure × likelihood-of-impact, then bump by consequence):

| Likelihood of failure | Low impact likelihood | Medium impact likelihood | High impact likelihood |
|---|---|---|---|
| Possible | Low | Low–Moderate | Moderate |
| Probable | Low–Moderate | Moderate–High | High |
| Imminent | Moderate–High | High | Extreme |

Worked example (from SKILL.md): failure = Probable, impact = Medium–High (driveway is regularly occupied by vehicles), consequence = Significant → combined rating **High**. A High rating means the defect gets addressed on this visit or in writing with a firm follow-up date — it does not go on a "someday" list.

## 2. Minimum approach distance (MAD) by voltage class

ANSI Z133 Table 1 minimum approach distances for a **qualified line-clearance arborist**, phase-to-ground exposure:

| Voltage class | Qualified line-clearance MAD | Non-qualified worker default clearance |
|---|---|---|
| 0–300V | Avoid contact; insulate or treat as energized | 10 ft |
| 301V–750V | 1 ft 0 in | 10 ft |
| 751V–15kV | 2 ft 2 in | 10 ft |
| 15.1kV–36kV | 2 ft 7 in | 10 ft, +4 in per additional 1kV above 50kV if scaling beyond this table |
| 36.1kV–46kV | 2 ft 10 in | 10 ft |
| 46.1kV–72.5kV | 3 ft 6 in | 10 ft |

Reading this table: the qualified-arborist column is what a certified line-clearance crew may approach to; the 10-ft default is the hard floor for anyone on the crew without that qualification, regardless of how experienced they are with a saw. If your crew's certification roster doesn't have a name on the line-clearance list for this voltage class, the job gets referred out or the line gets scheduled for de-energization — there is no third option.

Worked example: 7.2kV/12.47kV primary conductor, canopy at 6 ft horizontal clearance. 6 ft < 10 ft non-qualified floor → general crew must decline. 6 ft > 2 ft 2 in qualified MAD → a line-clearance-qualified crew may legally proceed.

## 3. Rigging load worksheet

Estimate static weight, then apply a shock-load multiplier based on drop distance before comparing to the rigging hardware's working load limit (WLL).

**Static weight estimate** (green hardwood, taper-corrected field rule of thumb — not a precise cylinder calculation, cross-check against experience on unfamiliar species):

`Weight (lb) ≈ length (ft) × average diameter² (in²) × 0.027 × specific gravity (≈0.80 for green hardwood, 50 lb/cu ft ÷ 62.4 lb/cu ft water)`

Worked example — 25-ft leader section, average diameter 18 in:
`25 × 18² × 0.027 × 0.80 = 25 × 324 × 0.027 × 0.80 ≈ 175 lb` — cross-check against a saw-time visual estimate before trusting the formula on an unfamiliar species/moisture condition.

**Shock-load multiplier by controlled drop distance** (rigging line, not free-fall):

| Drop before line takes load | Approximate multiplier on static weight |
|---|---|
| 0 ft (lowered under tension throughout) | 1.0–1.5x |
| 1–2 ft | 2–3x |
| 3–5 ft | 4–6x |
| Free-fall / uncontrolled | Treat as unrated — do not rig this way |

Worked example continued: 175 lb piece, planned 2-ft drop before the line takes tension → estimated dynamic load ≈ 175 × 2.5 = **~440 lb**. If the rigging block/sling is rated for a 500-lb WLL, that load sits at 88% of rated capacity — inside the "within ~20%" trigger from SKILL.md's heuristic — so the plan defaults to adding a wrap of friction on the lowering device or breaking the piece into two smaller sections rather than running it as planned.

## 4. Drop-zone sizing

| Piece/tree scenario | Minimum clear radius |
|---|---|
| Single piece removal, length L | 1.5 × L |
| Whole-tree takedown | 1.0 × total tree height, minimum |
| Any scenario with an occupied target (road, structure) inside the base radius | Base radius + full width/berth of the target, or reroute traffic/occupants entirely |

Worked example: 25-ft leader → 1.5 × 25 = 37.5 ft, rounded up to a 40-ft cleared radius, expanded toward the driveway rather than shrunk to fit it.
