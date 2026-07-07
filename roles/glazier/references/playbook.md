# Playbook

Filled worksheets for the three recurring calculations: hazardous-location classification, wind-load glass selection, and setting-block/edge-clearance sizing. Use these as the actual work, not a description of the work.

## 1. Hazardous-location classification (IBC 2406.4 checklist)

Walk every opening through this before quoting a glass type. Any "yes" mandates safety glazing (tempered or laminated) unless the code official has approved a documented exception.

| Check | Threshold | This opening |
|---|---|---|
| Within a door's swing arc | ≤24" horizontally from either edge of the door, in the plane of the door or an intersecting wall within 24" | |
| In or adjacent to a sliding/swinging door itself | Glass is part of the door leaf or a sidelite within 24" of the door edge | |
| In a guard or railing | Any glass panel used as (or infilling) a guard | |
| Near a stair, ramp, or landing | ≤36" horizontally AND ≤60" above the walking surface | |
| In a wet enclosure (shower/tub) | ≤60" horizontally from the water's edge or drain, regardless of height | |
| In a bathroom, ≤60" above the drain inlet | Applies even outside the enclosure itself | |

**Example:** a sidelite 18" from a door edge, 30" tall, bottom rail 6" off the floor → fails the door-arc check (18" < 24") → tempered or laminated required, full stop, independent of any other factor.

## 2. Wind-load glass selection (ASTM E1300 workflow)

1. Get the design pressure (DP) from the structural glazing schedule or the framing system's tested rating. Never substitute the safety-glazing code minimum for this — they answer different questions.
2. Note the lite's dimensions, support condition (4-side simply supported is standard for framed storefront/curtain wall), and candidate makeup.
3. Look up (or run through E1300 software) the load resistance (LR) for that makeup at those dimensions and support condition. Compare LR against the higher-magnitude DP (usually the negative/suction value governs on corner and edge zones).
4. If monolithic doesn't clear it, check laminated — E1300's laminated-glass load-share method typically credits ~90% combined stiffness for standard PVB interlayers at room temperature, meaning two 1/4" lites laminated perform close to (not equal to) a monolithic lite of the combined nominal thickness.
5. Record which requirement governed (safety-glazing type, wind load, or both) on the job spec sheet.

**Worked lookup — repeat of the SKILL.md worked example, as a standalone reference:**

| Makeup | Nominal thickness | DP required | E1300 result at 72"×96", 4-side | Pass? |
|---|---|---|---|---|
| 1/4" monolithic tempered | 0.25" | ±45/−55 psf | LR ≈ low-20s psf | No — fails wind load |
| 3/8" monolithic tempered | 0.375" | ±45/−55 psf | LR clears −55 psf | Yes — 4-day special order |
| 1/4" temp + 0.090" PVB + 1/4" temp | 0.5625" nominal | ±45/−55 psf | LR clears −55 psf (laminated load-share) | Yes — in stock |

Decision: laminated tempered — clears both constraints, in stock, fails safer.

## 3. Setting-block and edge-clearance sizing

**Setting-block placement:** quarter points of the sill (in from each corner by roughly 1/4 of the sill length) for standard lites. Move to eighth-point or an engineered layout above ~400 lb per lite or for oversized laminated/IGU makeups where the fabricator specifies otherwise.

**Setting-block sizing formula:**

```
block length (in) = total lite weight (lb) ÷ [number of blocks × allowable bearing stress (psi) × block width (in)]
```

Standard neoprene setting blocks: Shore A durometer 70–90, allowable bearing stress 50 psi (a conservative, widely used ceiling — check the specific block manufacturer's spec sheet, as harder-durometer blocks rate higher). Block width should equal or slightly exceed the glazing pocket bite for the makeup (commonly 5/8" for laminated or IGU makeups, 1/2" for standard monolithic).

**Worked example, reused:**

- Lite: 72" × 96", laminated tempered, ~7.2 lb/sq ft, 48 sq ft → 345.6 lb total.
- 2 blocks, quarter points (18" in from each corner along the 72" dimension).
- Load per block: 345.6 ÷ 2 = 172.8 lb.
- Block width: 5/8" (0.625").
- Length required: 172.8 ÷ (50 × 0.625) = 5.53" → specify standard 6" block.
- Check: 172.8 ÷ (6 × 0.625) = 46.1 psi < 50 psi allowable. Passes.

**Glass weight reference (approximate, by nominal thickness, lb/sq ft):**

| Nominal thickness | Weight (lb/sq ft) |
|---|---|
| 1/8" (3mm) | 1.64 |
| 3/16" (5mm) | 2.45 |
| 1/4" (6mm) | 3.27 |
| 3/8" (10mm) | 4.90 |
| 1/2" (12mm) | 6.54 |

Laminated makeups: sum the plies' weight and add roughly 0.7 lb/sq ft per 0.090" PVB interlayer. IGUs: sum each lite's weight plus the spacer/seal weight (typically 0.3–0.5 lb/sq ft, usually immaterial to the setting-block calculation).

**Edge clearance minimums (NGA guidance, standard framing):**

| Lite condition | Minimum edge clearance |
|---|---|
| Monolithic, ≤10 sq ft | 3/16" (5mm) |
| Monolithic, >10 sq ft, or laminated | 1/4" (6mm) |
| Laminated or IGU, oversized, dark frame, or high thermal-stress exposure | 5/16"–3/8" (8–10mm) |

Bump one tier when the frame is a dark color, the lite is oversized for its makeup, or the opening has partial shading — all three increase the temperature differential the edge has to accommodate.

## 4. Seal-failure and thermal-stress service-call triage

**On a fogging/haze call:**
1. Confirm the haze is between the panes, not on either exterior surface (wipe test on both faces — if it persists, it's interpane).
2. Interpane haze or visible desiccant residue = confirmed seal failure. Quote IGU replacement; do not quote a cleaning service.
3. Check IGMA certification/warranty documentation on the original unit before quoting — a failure inside the warranty term is a manufacturer claim, not a paid repair.

**On an unexplained crack with no impact point:**
1. Check the crack origin — thermal-stress cracks start at the edge and run roughly perpendicular to it; impact cracks radiate from a point of contact, often with a visible chip or cone fracture at the origin.
2. If edge-originated, check exposure: partial shading (a sign, an awning edge, adjacent trees), frame color, and any interior treatment (blinds, film) set within a few inches of the glass.
3. Recommend heat-strengthened or tempered replacement if the original was annealed and the exposure explains the differential; annealed replacement into the same conditions repeats the failure.
