# Playbook

Filled worksheets a blaster-in-charge actually runs in the field, with real structures and example numbers — starting points to adapt to site geology and jurisdiction, not scripts.

## 1. Bench blast design worksheet

Run for every new pattern or whenever bench height, rock type, or hole diameter changes from the last approved design.

**Inputs (example — 6.5 in hole, 30 ft bench, medium-hard limestone):**

| Parameter | Value | Basis |
|---|---|---|
| Hole diameter (D) | 6.5 in (165mm) | Fixed by drill rig on site |
| Burden (B) | 16 ft | ~29× diameter, mid-range for medium rock |
| Spacing (S) | 18 ft | S/B ratio 1.13 (staggered pattern) |
| Bench height (H) | 30 ft | Site bench design |
| Subdrill (J) | 5 ft (0.31×B) | Toe condition: competent, low joint frequency |
| Hole depth (H+J) | 35 ft | |
| Stemming (T) | 11 ft (0.69×B) | Crushed 3/4 in aggregate |
| Charge column | 24 ft | Hole depth − stemming |

**Load calculation (ANFO, 0.85 g/cc = 53.06 lb/ft³):**

```
Hole area = π × (3.25/12)² = 0.2304 ft²
Loading density = 0.2304 × 53.06 = 12.23 lb/ft
Charge per hole = 24 ft × 12.23 lb/ft = 293.5 lb
```

**Volume and powder factor:**

```
Volume/hole = B × S × H = 16 × 18 × 30 = 8,640 ft³ = 320 yd³
Powder factor = 293.5 lb ÷ 320 yd³ = 0.92 lb/yd³
```

Compare against the site's rolling average for this rock type (target band for this limestone: 0.75–0.95 lb/yd³). Inside the band with no geology change → proceed to timing. Below the band → expect oversize; above it → check for over-vibration/flyrock risk before proceeding.

**Reconciliation check:** total pattern charge (14 holes × 293.5 lb = 4,109 lb) must be re-verified against the per-delay compliance cap once the timing plan (Step 3, SKILL.md) is set — the per-hole number above only tells you the load is reasonable for fragmentation, not that it's legal to fire that way.

## 2. Misfire response sequence

Triggered any time a charge fails to detonate as designed, a downline is found intact after firing, or the post-blast count of detonations doesn't match the number of charges loaded.

1. **Stop.** No one re-enters the blast area. Announce the misfire over the site radio/PA immediately — don't wait for confirmation of cause.
2. **Post the exclusion zone** at the same radius used for the original shot; treat every unaccounted charge as live.
3. **Wait the mandated period before approach**, per applicable regulation and initiation system:
   - Cap and fuse: minimum 1 hour (OSHA 1926.911 / 30 CFR).
   - Electric or shock-tube detonators: minimum 30 minutes is common under state/MSHA rules layered on the federal floor — confirm the site's actual permit language, which controls over this default.
   - Do not shorten the wait because the cause "looks obvious" (burned-through leg wire, visible crater) — appearance is not proof of no-detonation.
4. **Investigate from the firing point outward**, never from the suspected charge inward — check the blasting machine/circuit continuity, the connections at the firing point, then trace the line toward the hole.
5. **Choose a resolution method, safest first:**
   - Re-attempt firing if the circuit fault is found and fixed at the firing point (most common outcome — a bad connection, not a bad charge).
   - If the charge must be approached: a certified blaster only, using a method that doesn't require drilling near the misfired charge — flush and reload a new primer if accessible, or use a properly spaced parallel hole for a sympathetic secondary shot.
   - Never attempt to drill out, dig out, or pull the misfired charge by hand.
6. **Document**: cause (if determined), method of resolution, time of clearance, names of everyone involved. A misfire with no root cause identified gets flagged for the next shot's pre-shot circuit check as a pattern-level concern, not filed and forgotten.

## 3. Secondary blasting decision table

For oversize boulders or toes left after the primary shot — choose the least-charge, least-flyrock method that fits the piece.

| Method | When to use | Charge/setup | Flyrock risk |
|---|---|---|---|
| **Blockholing** (drill and load a small charge inside the boulder) | Boulder large enough to drill (typically >3 ft), access for a hand drill or small rig | Small charge, ~10–15% of the powder factor that broke the parent rock | Low — charge is confined inside the rock |
| **Mudcapping / plaster shooting** (charge placed on the surface, covered with stemming/mud) | Boulder too small or awkward to drill, or drill access blocked | Larger relative charge than blockholing for the same rock volume — uncontained detonation | High — this is the method most associated with secondary-blast flyrock incidents; use only with adequate standoff and blast mats |
| **Mechanical breaking** (hoe ram, drop ball) | Any piece where explosive access is restricted by proximity to structures, utilities, or the pit wall | No explosive | None — default choice within any flyrock-sensitive exclusion zone |

**Rule:** if the piece is within the pre-blast survey radius of an occupied structure, mechanical breaking is the default unless a blaster-in-charge documents why blockholing is necessary and what additional standoff/matting compensates for the flyrock risk.

## 4. Pre-blast survey log (filled example)

One entry per structure inside the survey radius (typically set by permit or state rule, often 1,000–2,500 ft depending on jurisdiction and blast size).

```
STRUCTURE: 214 Maple Ridge Ct. — single-story brick residence, built 2011
DISTANCE FROM PLANNED BENCH: 640 ft
SURVEY DATE: 2026-07-10        SURVEYOR: [name], certified blaster
CONDITION NOTED: hairline crack, drywall, NE bedroom ceiling corner (photographed,
  dated); no visible foundation cracking; existing settlement crack, garage slab,
  photographed
OWNER PRESENT: yes — walked property together, both signed condition log
FOLLOW-UP: none required; baseline established for any future claim comparison
```

**Rule:** every structure in the survey radius gets a dated photograph and a signed (or documented-attempt-to-obtain-signature) condition log before the first shot in that phase. This log, not the blaster's memory, is what resolves a damage claim filed six months later.
