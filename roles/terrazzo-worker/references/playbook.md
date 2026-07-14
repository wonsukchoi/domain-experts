# Playbook

Filled tables and worked calculations a terrazzo crew actually runs, not descriptions of them.

## 1. System selection by substrate condition

| Substrate condition | Default system | Why |
|---|---|---|
| New structural slab, sound, no cracking expected | Monolithic (poured directly on and bonded to slab) | No isolation layer needed; lowest cost, thinnest build-up. |
| Existing slab with active or likely cracking, renovation over old floor | Sand-cushion (reinforced topping floating on a sand/isolation layer) | Isolates the new terrazzo from substrate movement; the layer that would otherwise telegraph a crack straight through. |
| Sound substrate, thin-set budget/thickness constraint (renovation tying into existing floor height) | Epoxy thin-set (1/4–3/8 in) | No shrinkage cracking risk from the resin matrix; needs the least added floor height. |
| Exterior or heavy-abrasion area, unpolished finish acceptable | Rustic terrazzo | Aggregate exposed but not machine-polished; more abrasion- and slip-resistant as installed. |
| Existing terrazzo substrate, new terrazzo bonding directly to it | Bonded | Bonding agent + mechanical profile on the old surface takes the place of a fresh structural bond. |

## 2. RH/moisture decision table (epoxy and other resin-bound systems)

| ASTM F2170 result (RH at 40% depth, one-sided drying) | Action |
|---|---|
| ≤ 75% RH (or resin manufacturer's stated limit) | Proceed with standard epoxy system. |
| 76–85% RH | Proceed only with a moisture-vapor-reduction (MVR) primer/membrane rated for the tested level; confirm manufacturer's MVR product RH rating covers the reading with margin. |
| > 85% RH | MVR membrane mandatory, or switch to a vapor-permeable cementitious system if design allows; do not proceed on standard epoxy at this level regardless of schedule pressure. |
| Any reading taken before 72-hr HVAC/temperature equilibration in the space | Test is invalid — re-test after equilibration before making a system decision. |

**Worked probe-count example (2,000 sf lobby, 5-in slab, one-sided drying):**
- Probe depth: 5 in × 0.40 = 2.0 in.
- Minimum probes: 3 (first 1,000 sf) + 1 (next 1,000 sf) = 4 probes.
- Readings: 88%, 91%, 93%, 90% → average = (88+91+93+90) ÷ 4 = 90.5% RH.
- Against a 75% RH manufacturer limit: 90.5 − 75 = 15.5 points over → MVR membrane required (see SKILL.md worked example for the full schedule/cost reconciliation).

## 3. Chip size to topping thickness

| Chip grade | Chip size range | Minimum topping thickness |
|---|---|---|
| #00 / #000 (micro-aggregate) | Fine, sub-#0 | 1/4 in |
| #0 | 1/16 in | 1/4 in |
| #1 | 1/8–3/16 in | 1/4–3/8 in |
| #2 | 1/4–3/8 in | 3/8 in |
| #3–#8 (Venetian) | 3/8–1 1/8 in | 1/2–3/4 in |

**Divider strip depth to match:** 1 1/4 in strip depth for a 1/2 in standard topping; 1 1/2 in strip depth for a 3/4 in Venetian topping. Strip gauge: 18, 16, or 14 B&S gauge (or 1/8, 1/4, 3/8 in heavy top for high-traffic/design-forward strips), in white alloy of zinc, brass, or plastic depending on exposure and design.

## 4. Divider-strip layout, worked (cementitious, 40 ft × 50 ft = 2,000 sf room)

**Step 1 — spacing target.** Cementitious rule: panels 4 ft × 4 ft or smaller, or ≤ 25 sf with aspect ratio ≤ 1.5:1.

**Step 2 — panel grid.** 40 ft ÷ 4 ft = 10 panels across. 50 ft ÷ 4 ft = 12.5 — round to 4 ft 2 in panels along that axis (50 ÷ 12 = 4.17 ft) to land on a whole number of panels: 12 panels × 4.17 ft = 50 ft exact.

**Step 3 — panel count and area check.** 10 × 12 = 120 panels, each 4 ft × 4.17 ft = 16.67 sf. 120 × 16.67 = 2,000.4 sf ≈ 2,000 sf (rounding) — matches the room area with no oversized leftover strip.

**Step 4 — tie to substrate joints.** Overlay the substrate's existing control/construction joint map; wherever a substrate joint falls, a divider strip must land on or straddle it — moving the panel grid by up to 6 in to align is preferable to leaving a substrate joint uncovered by a strip.

**Note — epoxy jobs:** the 4×4 rule above does not apply; strip placement on epoxy terrazzo follows the approved design pattern, not a shrinkage calculation. Confirm which system is running before applying this section.

## 5. Cure schedule by system

| System | Minimum cure before grinding | Full cure / design strength |
|---|---|---|
| Epoxy terrazzo | 24–48 hrs (can be as fast as overnight under favorable temp/humidity) | 90 min initial set; full chemical cure within days |
| Cementitious terrazzo | 3–4 days minimum, 7 days if mix/chip/weather unfamiliar | 28 days to design strength and full shrinkage stability |

**Worked example — cementitious floor poured Monday morning, cool site (60–65°F):** minimum grind date is Thursday–Friday (day 3–4) under ideal conditions; because the chip blend is new to this crew and the site is running cool (slows hydration), hold to day 7 (the following Monday) before the first grind pass, and don't schedule sealer/densifier application until day 28 has been reached for the section that will see heavy rolling loads (furniture move-in).

## 6. Grit-progression schedule (grind and polish)

| Pass | Grit | Purpose |
|---|---|---|
| 1 | 40–80 (metal-bond) | Level the surface, expose aggregate, remove excess binder cream. |
| 2 | — | Inspect for voids/pinholes; apply matching grout coat if present; allow grout coat to cure per system (cementitious: 24 hr min; epoxy: per resin data sheet) before continuing. |
| 3 | 100–200 (metal-bond) | Remove grout-coat overpour, refine flatness. |
| 4 | 400–800 (resin-bond) | Begin polish stage; scratch pattern from pass 3 must be fully removed before advancing. |
| 5 | 1500–3000+ (resin-bond) | Final polish/honed finish, per specified gloss level. |

**Rule:** never advance more than one grit tier without a visual check under raking (low-angle) light, not just overhead shop lighting — shop lighting hides scratch patterns that raking light exposes immediately.

## 7. Sealer/densifier sequencing (cementitious)

```
Grind complete (pass 5) → surface dry and dust-free
  → Apply lithium/sodium silicate densifier per manufacturer coverage rate
  → Hold reaction/cure window per data sheet (commonly 24–48 hrs) — do NOT seal over an unreacted densifier
  → Confirm surface pH/reaction complete (manufacturer test strip or visual per data sheet)
  → Apply sealer/finish per specified gloss and traffic classification
  → Hold sealer cure window (per data sheet) before foot traffic; hold longer before rolling loads/furniture
```
