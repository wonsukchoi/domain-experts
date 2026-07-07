# Playbook

Filled tables and checklists for classifying a trench, choosing a protective system, running a lift as signal person, and staging material on an active site.

## Soil classification decision table (OSHA Appendix A)

Classify on the day of the work, not from an old report — any single exclusionary condition overrides a favorable lab test.

| Type | Baseline description | Unconfined compressive strength | Excludes if any of these are present |
|---|---|---|---|
| A | Cohesive clay, silty clay, sandy clay, clay loam; most stable | ≥ 1.5 tons/sq ft (tsf) | Fissured; subject to vibration from heavy traffic, pile driving, or similar; previously disturbed; part of a sloped, layered system dipping into the excavation at 4H:1V or steeper; seeping water present |
| B | Angular gravel, silt, silt loam, previously disturbed soils meeting Type A strength but not other Type A criteria | 0.5–1.5 tsf | Same exclusionary vibration/fissuring/seepage conditions as Type A push it to Type C |
| C | Granular soils (gravel, sand, loamy sand), submerged soil, soil with freely seeping water, submerged rock that is not stable | ≤ 0.5 tsf, or any submerged/seeping condition regardless of strength test | — (C is the default catch-all once any exclusion applies) |

**Field rule:** if the soil would test Type A or B on a pocket penetrometer or thumb test, but shows seepage, vibration exposure, or fissuring today, classify it Type C today — the lab number doesn't override what's happening at the wall right now.

## Maximum allowable slope table (excavations under 20 ft)

| Soil type | Slope ratio (H:V) | Approx. angle from horizontal | Horizontal offset at 6 ft depth | Horizontal offset at 10 ft depth |
|---|---|---|---|---|
| Stable rock | Vertical | 90° | 0 ft | 0 ft |
| A | 0.75:1 | 53° | 4.5 ft | 7.5 ft |
| A (short-term, ≤24 hr exposure, excavation < 12 ft) | 0.5:1 | 63° | 3 ft | n/a past 12 ft |
| B | 1:1 | 45° | 6 ft | 10 ft |
| C | 1.5:1 | 34° | 9 ft | 15 ft |

Offset = slope ratio × depth, measured from the toe of each wall. Total top width for a fully sloped trench = bottom width + (offset × 2 sides).

## Protective-system selection logic

Run in order; stop at the first system that fits the site.

1. **Is the excavation entirely in stable rock, or under 5 ft with no indication of a hazardous ground movement potential?** → No protective system required, but a competent person still confirms this in writing.
2. **Does the site have room for the full slope offset from the table above, on every open side, without undermining a structure, utility, or property line?** → Sloping/benching is the system; no engineered design needed under 20 ft.
3. **Does the footprint fall short of the required offset on one or more sides (utility, structure, or lot line in the way), and the trench is under 20 ft?** → Shoring (timber or hydraulic) or shielding (trench box), rated for the classified soil type and depth, sized to the available clearance.
4. **Is the excavation 20 ft or deeper, regardless of soil type?** → Protective system (of any type) must be designed by a registered professional engineer; no standard table applies past this depth.
5. **Does more than one condition above conflict (e.g., partial slope fits on one side, not the other)?** → Default to a single consistent system (typically shielding) for the full trench length rather than mixing slope and shore on adjacent sections — simplifies inspection and avoids a transition point becoming the weak point.

## Standard crane/equipment hand signals (ASME B30.5 core set)

| Signal | Gesture | When used |
|---|---|---|
| Hoist | Forearm vertical, forefinger pointing up, hand making small horizontal circle | Raise the load |
| Lower | Arm extended downward, forefinger pointing down, hand making small horizontal circle | Lower the load |
| Use main hoist | Tap fist on head, then use regular signals | Switch load control to main hoist line |
| Use whipline (auxiliary hoist) | Tap elbow with one hand, then use regular signals | Switch load control to auxiliary line |
| Raise boom | Arm extended, fingers closed, thumb pointing up | Raise the boom |
| Lower boom | Arm extended, fingers closed, thumb pointing down | Lower the boom |
| Move slowly | One hand giving any motion signal, other hand motionless in front of the hand giving the motion signal | Reduce speed of any signaled motion |
| Stop | Arm extended, palm down, moved back and forth horizontally | Halt current motion |
| Emergency stop | Both arms extended, palms down, moved back and forth horizontally | Halt all motion immediately — any worker on site may give this signal, not only the designated signal person |
| Travel | Arm extended forward, hand open and slightly raised, making a pushing motion in direction of travel | Move the equipment/carrier |
| Extend boom (telescoping) | Both fists in front of body, thumbs pointing outward | Extend boom sections |
| Retract boom (telescoping) | Both fists in front of body, thumbs pointing toward each other | Retract boom sections |
| Dog everything (hold) | Clasp hands in front of body | Hold all motion, load remains suspended |

**Radio backup protocol (filled example):** operator and signal person confirm channel (e.g., Ch. 3) and callsign ("Box 1 to Operator") before the first lift of the shift; radio traffic restates the hand signal in words ("hoisting slowly") rather than issuing new instructions the hand signal set doesn't cover; if radio and hand signal ever conflict, the hand signal governs and the lift pauses until both channels agree.

## Material-staging zone table (example active site: 40 ft × 60 ft building pad)

| Material | Staging zone | Setback from active hazard | Sequencing note |
|---|---|---|---|
| Rebar/reinforcing bundles | East laydown, 15 ft from pad edge | Outside crane swing radius (28 ft boom + load) | Staged in pour-sequence order, not delivery order |
| Trench spoil | South of open trench only | ≥ 2 ft from trench edge (1926.651(j)(2)) | Never placed on the side needed for shoring access |
| Block/masonry pallets | West laydown | Outside spoil setback and outside crane exclusion zone | Restaged daily to follow the active wall section |
| Conduit/electrical rough-in material | Inside building footprint, by room | Outside any open trench collapse zone; clear of overhead crane path | Coordinated with electrical foreman before final placement, since rough-in zones shift daily |
| Fuel/flammables | Northeast corner, 50 ft from any hot work or excavation with potential gas-line exposure | Per site fire-safety plan, not a laborer judgment call alone | Flagged to site safety officer if hot work location changes |
