# Playbook

Filled reference tables for the four assembly decisions that carry real risk: fire-rated wall/ceiling assemblies, STC/acoustic assemblies, control-joint placement, and fastener spacing. Numbers below are representative of common UL-listed and manufacturer-published assemblies (Gypsum Association GA-600, UL Fire Resistance Directory, USG/National Gypsum literature) — always verify the exact listed design number and current manufacturer evaluation report on a live job before pricing or hanging board; a listing can be revised or withdrawn.

## Fire-rated assembly quick reference

| UL Design | Rating | Framing | Board (per face) | Cavity | Fastener spacing |
|---|---|---|---|---|---|
| U305 | 1-hr | Wood studs, 16" o.c. | 1 layer 5/8" Type X | None required | Nails 7" o.c. edges, 12" o.c. field (screws: 12"/16") |
| U411 | 1-hr | 3-5/8" 25-ga steel studs, 24" o.c. | 1 layer 5/8" Type X | R-11 unfaced batt | Screws 8" o.c. edges, 12" o.c. field |
| U419 | 1-hr | 3-5/8" 25-ga steel studs, 24" o.c. | 2 layers 1/2" Type X, staggered joints | R-13 unfaced batt | Base layer 16" o.c.; face layer 12" o.c. |
| P526 (assembly family) | 2-hr | Steel studs, 24" o.c. | 2 layers 5/8" Type X per face | Mineral wool, full cavity | Base layer 24" o.c.; face layer 12" o.c. |

**Rule for all rows:** stud gauge, spacing, insulation type, board layer count, and fastener spacing travel together as one listed unit. Changing framing spacing from 24" o.c. to 16" o.c. "to be stiffer," or dropping the cavity insulation to save cost, produces an unlisted assembly even though every product used is individually fire-rated. Confirm substitution language in the specific UL design before swapping manufacturer or board brand — some designs name a generic "gypsum panels, Type X" and allow substitution; others name a proprietary board by model number and do not.

## STC / acoustic assembly options (single wood or steel stud wall, one row of framing)

| Assembly | Typical tested STC | Notes |
|---|---|---|
| Single layer 1/2" board each face, no insulation | 33–35 | Baseline; fails most demising-wall STC-50 requirements |
| Single layer 5/8" board each face, cavity insulation | 39–42 | Mass + absorption only; common "looks compliant" trap |
| Add resilient channel (RC-1) one face, single layer opposite | 46–50 | Decoupling does the work mass alone can't |
| Resilient channel one face + double layer staggered opposite + insulation | 50–54 | Standard demising-wall target assembly, per worked example in SKILL.md |
| Staggered/double stud (separate top/bottom plates) + double layer both faces + insulation | 55–60 | Highest isolation; used where music/AV rooms adjoin |

**Fallback order when a target STC isn't being met on a mock-up or field test:** (1) verify every electrical box, duct, and pipe penetration is sealed with non-hardening acoustic sealant — a single unsealed box can cost 5–8 STC points; (2) verify no continuous framing member (top track, stud) bridges both faces; (3) add or upgrade resilient channel/isolation clips before adding another board layer — decoupling fixes typically outperform another layer of mass at lower cost.

## Control joint placement

- Place a control joint on any single, unbroken wall or ceiling run exceeding **30 linear feet**, measured along the actual run — not the nominal room dimension. An L-shaped corridor that reads as two 20-ft rooms on the plan can still be one continuous 40-ft run of board and framing.
- Place a control joint at every point the framing itself has a structural expansion joint, at a change of substrate (e.g., gypsum board abutting a different wall assembly), and at large ceiling expanses exceeding roughly **2,500 sq ft** in one unbroken field.
- Control joints interrupt continuous board and continuous framing — a control joint that stops at the board but doesn't correspond to a break in the framing behind it, or an insulated/soundproofed wall assembly, does not perform the accommodation function and does not exempt the wall from acoustic or fire detailing at that same location.
- On fire-rated assemblies, verify the control-joint detail itself is part of the listed design (some UL designs specify a fire-rated control-joint trim); an ordinary control joint on a rated wall can be the one component that voids the listing if the detail isn't the tested one.

## Fastener spacing by application (unrated, default assembly)

| Application | Fastener type | Perimeter/edge | Field |
|---|---|---|---|
| Wall, wood studs 16" o.c. | Nails | 7" o.c. | 8" o.c. |
| Wall, wood studs 16" o.c. | Screws | 12" o.c. | 16" o.c. |
| Ceiling, framing 16" o.c. | Nails | 7" o.c. | 7" o.c. |
| Ceiling, framing 16" o.c. | Screws | 12" o.c. | 12" o.c. |
| Wall, steel studs 24" o.c. (rated assemblies) | Screws | 8" o.c. | 12" o.c. |

Any cited fire-rated or acoustic assembly overrides this table with its own spacing — this table is the starting point for ordinary, non-rated partitions only.

## Suspended acoustic ceiling grid (CISCA / ASTM E580)

- Main runners at 4 ft o.c., cross tees at 2 ft o.c. for standard 2×4 tile layout; 2×2 layout adds a secondary cross tee at 2 ft o.c. in the other direction.
- Hanger wire spacing: maximum 4 ft o.c. along each main runner, with a hanger within 8" of each wall.
- Perimeter trim (wall angle) bearing: minimum 7/8" on each wall for standard installations.
- Seismic design categories D, E, and F (per ASCE 7): add compression struts (posts) at each hanger wire location within 6 ft of a wall, and 2"-wide wall-angle clips (or equivalent perimeter closure detail) instead of the standard resting perimeter — grid without this detail can walk off the wall angle during lateral movement even though it hangs correctly under gravity load alone.
