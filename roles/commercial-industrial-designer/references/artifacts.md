# Commercial/Industrial Designer — Artifacts

## DFM checklist (injection-molded part, filled example)

| Check | Rule of thumb | This part | Pass/Flag |
|---|---|---|---|
| Draft angle (vertical faces) | ≥1° textured, ≥0.5° polished | 1.5° all faces | Pass |
| Wall thickness | 1.0-3.0mm typical for ABS; uniform ±10% | 0.8mm at snap-fit wall | **Flag — below minimum** |
| Wall-thickness transitions | Gradual, ≤3:1 ratio, no abrupt step | 2.5mm to 0.8mm abrupt step | **Flag — linked to above** |
| Internal corner radius | ≥0.5x wall thickness | 0.6mm radius on 2.5mm wall | Pass |
| Undercuts | Avoid, or design for side-action/lifter | One undercut (battery clip) — requires slide | Flag — cost adder, client approved |
| Boss-to-wall spacing | ≥2x wall thickness from nearest wall | 3.2mm boss, 2.5mm wall | Pass |
| Parting line placement | Non-cosmetic face if possible | Rear face, non-cosmetic | Pass |
| Ejector-pin witness marks | Locate on non-cosmetic/hidden face | All 6 pins on interior ribs | Pass |

**Disposition:** 2 flags. Wall-thickness flag requires geometry revision before tool release (see Rev D). Undercut flag is a known cost adder (side-action slide, +$4,200 to tool cost) — approved by client for the battery-door function; no redesign needed.

## Material selection matrix (Ashby-style index, filled example)

Part: structural housing clip, must survive repeated snap-fit cycling without fatigue cracking. Dominant load case: cyclic bending stress at the snap-fit living hinge.

| Material | Flexural modulus (GPa) | Fatigue life index (cycles to failure, 2% strain) | Cost ($/kg) | Index score (fatigue life ÷ cost, normalized) |
|---|---|---|---|---|
| ABS | 2.3 | ~5,000 | $2.10 | 1.0 (baseline) |
| Polypropylene (PP copolymer) | 1.4 | ~500,000+ | $1.60 | 133.9 |
| Polycarbonate (PC) | 2.4 | ~15,000 | $3.80 | 1.7 |
| Nylon 6/6 (glass-filled 30%) | 9.0 | ~8,000 | $4.20 | 0.8 |

**Selection: Polypropylene copolymer.** ABS and glass-filled nylon score poorly on the fatigue axis despite being stronger in raw flexural modulus — modulus is the wrong index for a living-hinge feature designed to flex repeatedly, not resist deflection. PP's lower stiffness is a design *requirement* here, not a weakness, since the hinge needs to flex without cracking. Cost is a secondary filter after the fatigue index eliminated the higher-modulus options.

## Tooling cost-breakeven worksheet (template)

| Input | Value |
|---|---|
| Process A (e.g., injection molding) tooling cost | $______ |
| Process A unit cost | $______ |
| Process B (e.g., CNC machining) tooling cost | $______ (often $0) |
| Process B unit cost | $______ |
| **Breakeven volume** | (Tooling A − Tooling B) ÷ (Unit cost B − Unit cost A) |
| Projected volume | $______ |
| **Recommendation** | Process A if projected volume > breakeven; Process B if below |

**Sensitivity check:** always recompute at 50% of the optimistic volume forecast — a design recommendation that flips below a realistic downside case needs to be flagged to the client as a volume-dependent decision, not presented as settled.
