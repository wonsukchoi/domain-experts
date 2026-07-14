# Playbook

Filled sizing templates a solar thermal installer or design lead runs before ordering material and before finalizing the loop configuration. Every figure below follows common product classes and stated heuristics — always verify the actual collector/tank/fluid manufacturer specs and the local AHJ's adopted plumbing code edition before finalizing a design.

## 1. Storage tank sizing vs. collector aperture area

Method: size storage as a ratio of aperture area (the actual glazed/absorbing area SRCC rates, not the collector's gross panel footprint), then check against the household's daily draw pattern.

**Formula:** Storage (gal) = aperture area (sq ft) × ratio, ratio commonly 1.5–2.0 gal/sq ft.

**Filled example:**

| Collector aperture area | Min. storage (1.5 gal/sqft) | Max. of typical range (2.0 gal/sqft) | Recommended tank |
|---|---|---|---|
| 32 sq ft (1 collector) | 48 gal | 64 gal | 50–65 gal |
| 64 sq ft (2 collectors) | 96 gal | 128 gal | 100–120 gal |
| 96 sq ft (3 collectors) | 144 gal | 192 gal | 150–180 gal |

**Takeaway:** a storage number that "matches the number of collectors" from a past job doesn't transfer across sites — check it against this site's actual aperture area, and against the household's draw pattern if it's well outside a typical 2–4 person household (60–100 gal/day).

## 2. Propylene glycol concentration vs. site design-low temperature

Method: pull the site's ASHRAE 99% heating design-low temperature (or local record low, whichever the jurisdiction/insurer requires), then select a glycol concentration whose freeze point clears that temperature by 10–15°F margin — not the temperature itself.

**Filled example (approximate freeze points, verify against the specific product's data sheet — e.g., Dow Dowfrost HD):**

| Propylene glycol % | Approx. freeze point | Site design-low it clears w/ 10°F+ margin |
|---|---|---|
| 30% | +5°F | Sites with design-low ≥ +15°F only |
| 40% | −12°F | Design-low ≥ −22°F, margin thin below −12°F |
| 50% | −28°F | Design-low ≥ −38°F |
| 60% | −55°F | Design-low ≥ −65°F (rarely needed; viscosity/flow penalty rises) |

**Takeaway:** don't round down to "40% is standard" for a cold-climate site — compute the margin against the actual local design-low temperature, and don't over-concentrate past what the site needs, since viscosity increases and heat-transfer efficiency and pump flow both drop as concentration climbs past ~50-60%.

## 3. Expansion tank sizing for a glycol loop that sees routine stagnation

Method: total system fluid volume (collectors + header piping + heat-exchanger primary side) drives minimum acceptance volume. A pre-charged diaphragm tank's *acceptance volume* (the usable expansion capacity) is not its rated total volume — check the manufacturer's acceptance-volume spec, don't assume it's the full nameplate size.

**Stated heuristic:** minimum acceptance volume ≈ 10% of total system glycol-loop fluid volume for a system that reaches stagnation routinely. Acceptance volume for a typical pre-charged diaphragm tank runs roughly 40–50% of total rated tank volume — verify against the specific product.

**Filled example:**

| System fluid volume | Min. acceptance volume (10%) | Tank total volume needed (at ~45% acceptance ratio) |
|---|---|---|
| 8 gal | 0.8 gal | ~1.8 gal → spec 2-gal tank |
| 12 gal | 1.2 gal | ~2.7 gal → spec 3-gal tank |
| 18 gal | 1.8 gal | ~4.0 gal → spec 4-gal tank |

**When in doubt:** oversize one standard tank size up from the calculated minimum — an expansion tank that's slightly oversized costs little; one that's undersized dumps glycol out the pressure-relief valve on the first hot, low-draw week, and every dump event concentrates and degrades the fluid that's left.

## 4. Drainback slope and restart-lift check

Method: drainback removes the freeze-margin and stagnation-fluid-degradation questions but only if the collector loop can actually drain by gravity, and the pump can overcome the static lift on restart.

**Slope requirement:** collector loop and return piping pitched at a minimum of 1/4 in per foot back toward the drainback reservoir, with no low points, sags, or traps that can hold standing water — a single low spot defeats the freeze protection drainback exists to provide.

**Restart-lift check:** pump must be sized to lift fluid from the drainback reservoir to the top of the collector array (static lift, in feet of head) plus loop friction losses, every time the controller calls for flow — a pump sized only for circulation, not for restart lift, will fail to re-flood the collector loop and the system will appear to be "not heating" with no visible fault.

**Filled example — restart lift by array height above reservoir:**

| Vertical lift (reservoir to collector top) | Static head to overcome on restart |
|---|---|
| 15 ft | 6.5 psi (15 ft × 0.433 psi/ft) |
| 25 ft | 10.8 psi |
| 35 ft | 15.2 psi |

**Takeaway:** confirm the pump's rated head at the system's actual flow rate exceeds the static lift plus friction losses — a pump spec sheet checked only at zero-flow shutoff head overstates what's available at the flow rate the system actually needs to re-flood the array.

## 5. Tempering (anti-scald mixing) valve setpoint

Method: install a thermostatic mixing valve at the solar storage tank's hot outlet, set to the code-required or design delivery temperature — independent of how hot the tank itself gets on a high-solar day.

**Filled example:**

| Storage tank temp on a high-solar day | Tempering valve output setpoint | Delivered fixture temp |
|---|---|---|
| Up to 180°F+ (stagnation-adjacent) | 120°F (commonly code default, verify local amendment) | 120°F, regardless of tank temp |

**Takeaway:** the tempering valve setpoint is fixed at commissioning and doesn't need field adjustment as the tank temperature swings with solar gain — that's the point of the valve; skipping it means the fixture sees whatever temperature the tank happened to reach that day.
