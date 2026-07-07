# Playbook

Filled worksheets and step sequences a licensed installer actually runs on site, keyed to 24 CFR Part 3285 (the federal model installation standard) and typical manufacturer's-manual practice. State-approved installation standards (Texas, North Carolina, and others) can set stricter values — always check which standard governs the site before using the defaults below.

## 1. Site assessment and soil-bearing worksheet

Run before any footing is poured or set.

**Soil bearing capacity, by test method (cheapest/crudest first):**

| Method | Cost/time | Use when |
|---|---|---|
| Visual/tactile classification against Part 3285 default table | Free, minutes | Site looks unremarkable, no standing water, no fill dirt, matches surrounding built lots |
| Pocket penetrometer, 4+ points across the footprint | Low cost, ~1 hr | Any doubt at all — damp areas, fill dirt, clay, sloped lot |
| Hand-auger boring to footing depth | Low cost, ~2 hrs | Penetrometer readings vary >30% across the footprint, or water is hit above frost depth |
| Geotechnical soil report (licensed engineer) | $400–$1,500, days | Readings below ~1,000 psf anywhere, visible slab cracking nearby, or state program requires it above a home-weight threshold |

**Default bearing-capacity assumption if untested (Part 3285 §3285.312):** 1,000 psf. Do not use this default where visual/tactile signs (standing water, spongy ground, recent fill, adjacent cracked slabs) contradict it — test instead.

**Footing size formula:** required footing area (sq ft) = pier's tributary load (lb) ÷ soil bearing capacity (psf). Pull tributary load per pier from the manufacturer's manual load table (varies by pier spacing, home weight, and roof/floor live load zone) — never estimate it from home weight ÷ pier count, since end piers and marriage-line piers carry more load than mid-span piers.

**Worked sizing table (28×60 doublewide, 46,000 lb total, 8'-0" o.c. main-beam piers):**

| Pier location | Tributary load | Bearing capacity (tested) | Required footing area | Footing spec |
|---|---|---|---|---|
| Mid-span, typical | ~3,200 lb | 1,400 psf | 2.3 sq ft (330 sq in) | 16"×16" standard pad (256 sq in) — within manual's built-in safety margin |
| End wall | ~4,000 lb | 1,400 psf | 2.9 sq ft (412 sq in) | 20"×20" pad (400 sq in) per manual's end-wall spec |
| Damp corner, mid-span | ~3,200 lb | 650 psf | 4.9 sq ft (706 sq in) | 30"×30" pad (900 sq in) — upsized from standard |
| Marriage-line pier | ~4,800 lb | 1,400 psf | 3.4 sq ft (490 sq in) | 24"×24" pad (576 sq in) per manual's marriage-line spec |

**Frost-line depth by climate zone (footing base must sit below this depth, not just the frost-line number itself — check local jurisdiction, these vary by county even within a state):**

| Climate zone (example) | Typical frost depth | Footing practice |
|---|---|---|
| Gulf Coast / Deep South | 0"–12" | Surface or shallow footing generally acceptable |
| Mid-Atlantic / Upper South | 12"–24" | Standard footing depth, most manuals' default |
| Midwest / Mountain | 24"–42" | Deepened footing or frost-protected shallow foundation detail |
| Northern tier (MN, WI, ND, northern NE) | 42"–60"+ | Full-depth footing or engineered foundation system required |

## 2. Wind-zone anchoring specification

**Wind zone (from the home's HUD data plate) drives anchor rating and spacing — never infer it from "what we usually run around here."**

| Wind zone | Approx. design wind speed | Ground anchor min. working load | Typical spacing |
|---|---|---|---|
| Zone I | up to ~70 mph fastest-mile (most of the continental US) | 3,150 lb per anchor (vertical) | Diagonal ties at every other pier, vertical ties at marriage-line ends |
| Zone II | ~100 mph fastest-mile (coastal strip, parts of Gulf/Atlantic coast) | 4,725 lb per anchor | Diagonal ties at every pier, vertical ties at all end walls and marriage-line ends |
| Zone III | ~110 mph fastest-mile / hurricane-prone coastline (e.g., Florida Keys, immediate Gulf coast) | 4,725 lb per anchor, denser spacing and additional lateral bracing per manual | Diagonal ties at every pier plus supplemental lateral anchors, engineered tie-down system often required |

**Anchor pull/torque verification:** every anchor gets a field torque or pull test after install, not just a visual "it's in the ground" check. An anchor that visually looks set can still be under-torqued in loose, wet, or sandy soil — retest at 50% of rated working load minimum; any anchor that doesn't hold gets re-driven deeper, relocated, or replaced with a helical or auger-style anchor rated for that soil class.

**Anchor count example (28×60, Wind Zone II, 8'-0" o.c. piers, both sections):** 14 total anchor points — 10 diagonal ties (one per pier pair) + 4 vertical/end-wall ties at the two exterior end walls and two marriage-line end walls. Cross-check this count against the specific manual before installing; anchor count is a function of pier spacing and home length, not a memorized number carried job to job.

## 3. Multi-section marriage line and crossover checklist

Run in this order — do not proceed to the next step until the current one is within tolerance.

1. **Set and shim both sections to rough level** using the chassis beams as reference, before touching the marriage wall.
2. **True the marriage line first.** Tolerance: floor surfaces across the mate line level to within 1/4" vertically, and the two sections square to each other within 1/2" measured diagonally corner-to-corner over the mate line length. This is the reference plane for every other measurement on the home.
3. **Re-shim the remainder of the home off the trued marriage line**, not off an independent level reading taken before step 2 — chasing individual room levels before the mate line is true wastes a shimming pass.
4. **Overall home level tolerance:** no more than 1" of level deviation over 40 feet of run, per typical manufacturer spec — verify with a laser level or transit across the full length and width, not a 4-foot bubble level alone.
5. **Close the marriage wall structural connection** per the manual's fastener schedule (lag bolts or manufacturer-specified fasteners at marriage-line studs, typically at 16"–24" o.c.) before any utility crossover work begins — the structural connection carries the load path across the two sections.
6. **Complete crossover connections in this order:** electrical crossover (marriage-line junction boxes) → HVAC ductwork crossover (seal all joints; unsealed ductwork crossovers are a top callback source for comfort complaints) → plumbing crossover (supply and drain, including the marriage-line drain connection, which must maintain its designed slope across the mate line) → gas line crossover if applicable, pressure-tested before service is connected.
7. **Marriage-line exterior close-out:** roof cap/shingle-over per manual (weatherproofing the ridge where the two roof sections meet is a top source of long-term leak claims if rushed), then exterior siding/trim at the mate line, then interior drywall tape/finish last — sequencing it in this order avoids re-opening finished interior work to fix a structural or weatherproofing issue found late.

## 4. Pre-inspection self-walk

Run the day before the scheduled state inspection, using the state program's own checklist where one is published (most states publish the exact form the inspector will use).

- [ ] Data plate and manufacturer's manual on-site and matching the home's actual serial number
- [ ] All footings match the manual spec or the documented soil-based upsizing, with photos of any deviation and the soil test backing it
- [ ] Pier count and spacing match the manual's table for this home's length/weight
- [ ] Anchor count, rating, and placement match the wind zone on the data plate; torque-test records available
- [ ] Marriage line tolerance within spec (1/4" vertical, 1/2" diagonal square) — measured and recorded, not eyeballed
- [ ] Overall level within 1" over 40 feet
- [ ] All utility crossovers (electrical, HVAC, plumbing, gas) sealed, connected, and pressure/continuity tested as applicable
- [ ] Skirting/perimeter enclosure and any required ground vapor barrier installed per manual
- [ ] Steps, landings, and any required egress hardware installed and matching state minimum dimensions
