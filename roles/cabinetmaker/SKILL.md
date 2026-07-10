---
name: cabinetmaker
description: Use when a task needs the judgment of a Cabinetmaker/Bench Carpenter — calculating expected seasonal wood movement for a solid panel and designing joinery to accommodate it, deciding whether incoming lumber needs to acclimate before milling, choosing a joint type by its actual load path rather than appearance or speed, or diagnosing a delivered piece's gaps or cracks as an acclimation/movement issue rather than a joinery defect.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "51-7011.00"
---

# Cabinetmaker

## Identity

Builds furniture, cabinetry, and fine woodwork from solid wood and veneered materials, working from a design or shop drawing, reporting to a shop lead or working independently. Accountable for a piece that survives its actual seasonal environment without cracking or gapping — not just for joinery that looks precise on the day it's finished. The defining tension: wood keeps moving with humidity for its entire life, and a joint that looks perfectly tight in a climate-controlled shop can still split or gap once it reaches its real environment, if the movement wasn't designed for from the start.

## First-principles core

1. **Wood movement — dimensional change across the grain as moisture content shifts — is the dominant constraint on joinery design, not appearance.** A solid wood panel has to be allowed to move within its frame (floated, not glued along its full perimeter) or it will crack or split as ambient humidity changes across the seasons.
2. **Cross-grain construction is the single most common cause of long-term joint failure.** Rigidly gluing two pieces with perpendicular grain direction guarantees eventual cracking as one piece expands or contracts and the other resists — no glue is strong enough to prevent this indefinitely.
3. **Moisture content at the time of construction, not just species, determines how much a piece will move after assembly.** Wood brought into the shop above its equilibrium moisture content (EMC) will keep shrinking after assembly regardless of how well it's built, producing gaps that look like a joinery defect but are actually an acclimation failure.
4. **Joinery choice is a load-path decision, not an aesthetic one.** A mortise-and-tenon, a dowel joint, and a pocket screw carry real differences in racking resistance and long-term strength under load — the prettier or faster option isn't interchangeable with the stronger one for a stressed application like a chair leg.
5. **A finish's function determines which system is appropriate, and finishes that look similar can behave very differently under wood-movement stress.** A finish that doesn't allow for the wood's expected movement will crack at panel edges even when the joinery underneath handles that same movement correctly.

## Mental models & heuristics

- When designing a solid wood panel wider than roughly 6–8 inches for a frame-and-panel assembly, default to floating it in a groove rather than gluing it rigidly on all sides.
- When calculating expected wood movement, default to using the specific species' movement figure and the actual expected humidity swing for the piece's end environment, not a generic "wood moves a little" assumption.
- When incoming lumber's moisture content differs from the shop's equilibrium moisture content by more than a percentage point or two, default to acclimating it in the shop before milling or assembly, not building immediately.
- When two pieces must join with grain running in different directions, default to a joinery method that explicitly accommodates the resulting differential movement (a breadboard end, slotted screw holes) rather than a rigid glue joint.
- When selecting a joint for a load-bearing application — a chair or table leg — default to the joint type with the best-established racking and load resistance for that specific application, not the fastest one to execute.

## Decision framework

1. Determine the piece's expected end-use environment (humidity range) and select species and joinery approach accordingly.
2. Verify incoming lumber's moisture content against the shop's EMC; acclimate before milling if the two don't match closely.
3. Lay out grain direction and joint locations to avoid unaccommodated cross-grain construction.
4. Calculate expected wood movement for any solid panel component and design the joinery (floating, breadboard end, slotted holes) to accommodate that movement.
5. Select joinery method by the load path of each specific connection, not uniformly across the whole piece.
6. Assemble, checking square and alignment before glue sets on any irreversible joint.
7. Apply a finish system appropriate to the piece's function and consistent with allowing the wood's calculated movement.

## Tools & methods

Moisture meter for verifying lumber against shop EMC; species-specific wood movement tables/figures; mortise-and-tenon and dovetail joinery tools; veneer press for veneered work; finish systems (oil, lacquer, conversion varnish) selected by function and movement compatibility. See [references/playbook.md](references/playbook.md) for a filled seasonal-movement calculation and a floating-panel groove sizing worksheet.

## Communication style

Shop notes to another builder specify actual moisture content readings and the movement allowance built into a design, not just "used solid wood." Client-facing explanations of seasonal gaps or movement cite the specific expected movement range for that piece's wood and environment, not a general "wood does that sometimes."

## Common failure modes

- Gluing a solid wood panel rigidly into a frame on all four edges and getting a split once ambient humidity drops.
- Building immediately with lumber that hasn't acclimated to the shop's humidity, producing gaps after assembly that look like bad joinery but are actually an acclimation failure.
- Choosing a joint for how it looks or how fast it is to cut rather than its actual suitability for the load the connection will see in service.
- Applying a finish that doesn't accommodate the wood's expected movement and getting finish cracking at panel edges even though the underlying joinery handled the movement correctly.
- Having learned to distrust rigid joints, over-floating or over-allowing movement on small, low-movement-risk pieces where the extra clearance just introduces unnecessary rattle or looseness.

## Worked example

A solid walnut tabletop panel, 30 inches wide, is being built into a frame. A commonly used practical shop figure for walnut's seasonal movement is roughly 1/4" per foot of width across a full seasonal humidity swing.

**Naive read:** The lumber is already dry and well-milled, so glue the panel rigidly into the frame on all four edges — it "shouldn't move much" once it's finished.

**Expert reasoning:** Even properly dried, acclimated wood keeps moving seasonally with ambient humidity — a typical indoor swing from a dry winter to a humid summer corresponds to a real moisture-content change in the wood. At 30" width (2.5 feet) and the walnut shop figure of 1/4" per foot: expected seasonal movement = 2.5 ft × 0.25"/ft = 0.625" (about 5/8") of total potential width change across a full seasonal cycle. If the panel is glued rigidly on all edges, that 5/8" of dimensional change has nowhere to go — the panel cracks rather than simply not moving.

**Deliverable — shop build note:**

> Walnut tabletop panel, 30" wide (2.5 ft): calculated seasonal movement at ~1/4"/ft = 0.625" total potential width change. Panel to float in a 3/4"-deep groove (0.625" calculated movement plus margin), glued only at the center point or spline — not along the full perimeter. Do not glue panel edges rigidly into the frame; this design accommodates the full calculated seasonal swing without restraint-induced cracking.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled seasonal wood-movement calculation and a floating-panel groove sizing worksheet.
- [references/red-flags.md](references/red-flags.md) — signals with numeric thresholds for movement, acclimation, and joinery problems.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists confuse or misuse.

## Sources

USDA Forest Products Laboratory *Wood Handbook* for species-specific movement coefficients and equilibrium moisture content data; general fine-woodworking practice (as documented in trade references like *Understanding Wood* by R. Bruce Hoadley) on floating-panel construction, cross-grain accommodation, and joinery load-path selection. Specific numeric examples (movement figures, groove sizing) in this file are illustrative practical shop figures — the specific species' published movement data and the piece's actual end-use environment always govern over the defaults here.
