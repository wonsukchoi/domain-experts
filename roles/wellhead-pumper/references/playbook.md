# Playbook

Filled procedures and reference tables for the four recurring judgment calls: reading a dynamometer card, responding to an H2S reading, gauging a tank battery/separator, and tracking a well against its decline curve.

## 1. Dynamometer card diagnosis table

Read top-of-stroke (upstroke start) and bottom-of-stroke (downstroke start) corner shape first, then the mid-stroke line.

| Card shape | Diagnosis | Mechanism | Corrective action |
|---|---|---|---|
| Sharp corners top and bottom, parallelogram-ish, load swings cleanly between max (~upstroke) and min (~downstroke) | Normal pump operation | Traveling valve seats and standing valve seats close crisply at each stroke end | None — log as baseline for future comparison |
| Near-vertical load drop mid-downstroke (e.g., 18,000 → 11,000 lb at ~55–65% of stroke) | Fluid pound | Pump displacement exceeds well inflow; plunger free-falls through a partially gas/vapor-filled barrel before impacting fluid | Reduce strokes per minute (SPM) to match fillage, or install/adjust a pump-off controller; re-card in 48 hrs before considering a workover |
| Rounded, sloped bottom corner instead of a sharp one; reduced card area | Gas interference | Free gas entering the barrel compresses before the standing valve opens, delaying pressure buildup | Slow SPM, check for an undersized or missing downhole gas separator; not a pump-wear issue — don't pull the pump for this alone |
| Nearly flat card, minimal load swing (e.g., <2,000 lb range where normal is 6,000–8,000 lb) | Gas lock | Gas trapped in the barrel prevents either valve from opening under load | Cycle the pump off/on to break the lock; if it recurs, gas anchor or perforation interval needs review |
| Gradual, rounded pickup at top of upstroke instead of a sharp corner | Traveling valve leak | Valve not sealing; fluid bleeds back through the plunger during the load transfer | Schedule a valve/plunger pull; continuing to run erodes seating surfaces further |
| Downstroke doesn't fully unload before the next upstroke begins | Standing valve leak | Valve not holding fluid in the barrel between strokes | Schedule a standing valve replacement; distinguish from fluid pound by checking whether the drop is gradual (valve) vs. near-vertical (pound) |
| Card area shrinks steadily over weeks with corners staying sharp | Pump/plunger wear | Barrel or plunger clearance has opened up, reducing volumetric efficiency | Track rate of area loss; schedule a pump change at a rate-of-decline threshold rather than at first sign, since some wear is expected between service intervals |

**Reading order:** classify the bottom corner first (fluid pound vs. gas interference are both bottom-of-stroke phenomena and are the two most commonly confused), then the top corner (valve leaks), then overall area trend (wear) last.

## 2. H2S response protocol

| Reading (personal monitor, ppm) | Physiological reference point | Required action |
|---|---|---|
| 0–10 | Below OSHA general-industry ceiling and NIOSH REL (10 ppm ceiling); odor perceptible from roughly 0.001–1.5 ppm in most people | Continue normal work; log if sustained above 5 ppm |
| 10–20 | Approaches OSHA general-industry acceptable ceiling of 20 ppm (29 CFR 1910.1000 Table Z-2) | Low alarm — don gas monitor if not already worn, ventilate/move upwind if possible, notify partner or dispatch |
| 20–50 | Above OSHA ceiling; eye and respiratory irritation possible with continued exposure | High alarm — withdraw from area; do not re-enter without SCBA or forced-air respiratory protection and a second reading |
| 50–100 | Olfactory fatigue begins in this range for many people — the nose starts under-reporting true concentration | Treat any perceived "smell going away" as concentration likely still rising, not clearing; full retreat, no unprotected re-entry |
| 100 | NIOSH IDLH (Immediately Dangerous to Life or Health) value | Full-face SCBA required for any approach; unprotected personnel evacuate immediately |
| 100–500 | Olfactory paralysis essentially complete for most people; eye/respiratory damage accelerates | Confined to trained emergency responders in appropriate SCBA only |
| 500–700+ | Loss of consciousness and respiratory failure can occur within minutes; above ~700 ppm, collapse can be near-immediate | Rescue-only scenario; no unprotected entry under any circumstance |

**Rule that governs all of the above:** once a reading has been at or above ~50 ppm during a visit, the absence of smell afterward is not evidence the area cleared — re-confirm with the instrument before treating the smell's disappearance as good news.

## 3. Tank battery and separator gauging

**Tank gauging round (per tank, per visit):**

| Field | Example reading | Note |
|---|---|---|
| Gauged oil level | 9 ft 4 in | Convert via strapping chart to barrels |
| Strapped capacity | 1,680 bbl (per API 12F 400-bbl tank battery of 4) | Compare gauged volume to capacity, not to yesterday's level alone |
| Calculated volume | 1,140 bbl | 1,140 / 1,680 = 68% of capacity |
| BS&W cut (thief sample) | 1.2% | Flag if trending up from a baseline (e.g., prior month 0.6%) with no known workover — can indicate water breakthrough or emulsion issue upstream |
| Tank pressure/vacuum | 1.5 oz/in² | Compare to relief-hatch setting (commonly ~2.5 oz/in² pressure / ~6 oz/in² vacuum on an API 12F atmospheric tank) — within a small margin of setting means treat as already at the operating limit |

**Separator round:**

| Field | Example reading | Note |
|---|---|---|
| Operating pressure | 145 psi | Compare to relief-valve set point (commonly set ~10% above MAWP) |
| MAWP (per vessel nameplate) | 230 psi | Relief set point ≈ 253 psi in this example |
| Margin to relief set point | 253 − 145 = 108 psi (43% margin) | A separator sitting within roughly 10% of its relief set point is treated as already at its operating limit, not a "watch it" item |

## 4. Produced-water disposal-pressure check

| Field | Example value | Note |
|---|---|---|
| Max authorized surface pressure (MASP), per permit | 1,200 psi | Set by the state regulator (e.g., Railroad Commission of Texas Statewide Rule 9/46, or the applicable UIC Class II authority under 40 CFR 146) below the estimated fracture gradient for the injection zone |
| Current injection pressure | 1,050 psi | 1,050 / 1,200 = 87.5% of MASP |
| Action threshold | ≥90% of MASP | At or above this, treat as a hard stop — throttle injection rate down rather than let pressure approach the permit limit; exceeding MASP risks fracturing above the confining zone and is a reportable exceedance, not a target to run up to |

## 5. Decline-curve tracking worksheet

Arps hyperbolic decline: q(t) = qi / (1 + b·Di·t)^(1/b)

**Filled example (Smith 3H):** qi = 120 BOPD, Di = 0.35/yr, b = 0.6, t = 1.2 yr since curve start.

1. + b·Di·t = 1 + (0.6 × 0.35 × 1.2) = 1 + 0.252 = 1.252
1.252^(1/0.6) = 1.252^1.667 ≈ 1.454
q(1.2) = 120 / 1.454 ≈ **82.5 BOPD projected**

| Month | Measured BOPD | Projected BOPD | % of projection | Flag? |
|---|---|---|---|---|
| Month 12 | 79 | 84.1 | 94% | No |
| Month 13 | 66 | 83.3 | 79% | Yes — 1st |
| Month 14 (t=1.2) | 61 | 82.5 | 74% | Yes — 2nd consecutive → investigate mechanically before requesting a workover |

**Flag rule:** two consecutive readings below ~85% of projection (i.e., more than ~15% under curve) triggers a mechanical investigation (dynamometer card, fillage check, leak check) before a workover request goes to the engineer.
