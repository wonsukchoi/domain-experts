# Playbook

Filled calculations and templates a finishing crew actually runs, not descriptions of them.

## 1. Evaporation-rate check (ACI 305 nomograph, worked)

Run before every placement where any of: air temp > 80°F, RH < 40%, wind > 10 mph, or concrete temp > 80°F.

**Inputs and worked example (the noon section of a deck pour):**

| Input | Value |
|---|---|
| Concrete temperature | 85°F |
| Air temperature | 88°F |
| Relative humidity | 30% |
| Wind speed | 10 mph |
| **Evaporation rate (nomograph result)** | **~0.20 lb/ft²/hr** |

**Decision rule:**
- **< 0.10 lb/ft²/hr:** normal precautions, monitor.
- **0.10–0.19 lb/ft²/hr:** stage windbreaks/sunshades, have evaporation retarder on hand.
- **≥ 0.20 lb/ft²/hr:** plastic-shrinkage cracking likely without action — fog spray immediately behind strikeoff, apply evaporation retarder before bleed water appears, and do not leave any placed-but-unfinished concrete exposed even for 10–15 minutes.

**Compare against bleed rate, not just evaporation rate in isolation:** if evaporation rate exceeds the mix's bleed rate, the surface can dry and crust *before* bleed water has finished rising — the surface looks ready to finish while the interior is still bleeding. That combination (high evaporation, normal bleed rate) is the actual plastic-shrinkage-crack mechanism, not high evaporation alone.

## 2. Control-joint layout (worked, 50 ft × 100 ft slab, 5 in thick)

**Step 1 — spacing from thickness.** ACI 302.1R rule of thumb: max spacing (ft) = 2 to 3 × thickness (in). At 5 in: 10–15 ft. Choose 12.5 ft (mid-range, divides both dimensions evenly).

**Step 2 — panel count.** 50 ft ÷ 12.5 ft = 4 panels across. 100 ft ÷ 12.5 ft = 8 panels along. Total 32 panels, each 12.5 ft × 12.5 ft — aspect ratio 1:1, well inside the 1.5:1 maximum.

**Step 3 — reconcile against slab area.** 32 panels × 156.25 sq ft/panel = 5,000 sq ft. Matches the total slab area — layout has no leftover strip that would force an oversized panel at one edge.

**Step 4 — cut depth.** Depth = 1/4 × slab thickness = 1/4 × 5 in = 1.25 in.

**Step 5 — cut timing window.** Early-entry saw: as soon as the surface resists raveling under the saw's weight, typically 1–4 hours after finishing in moderate weather. In hot/windy conditions (evaporation rate ≥ 0.2 lb/ft²/hr, as above), compress the target to the early end of that range — shrinkage cracking can initiate inside 4–6 hours total from finishing, and the joint must be in before that.

**Common layout mistake to check for:** a leftover strip narrower than the panel width at one edge (e.g., a 6 ft sliver against a wall) — that sliver panel will crack on its own regardless of spacing math; either resize all panels down slightly or add a construction joint to absorb the remainder cleanly.

## 3. Hot-weather protection plan (ACI 305 triggers)

| Condition at placement | Required action |
|---|---|
| Concrete temp > 90°F | Reject the load or add ice/chilled water at the plant before placing — hydration and set-time control are already compromised at the truck. |
| Evaporation rate 0.10–0.19 lb/ft²/hr | Windbreaks, sunshades over freshly placed concrete, evaporation retarder ready. |
| Evaporation rate ≥ 0.20 lb/ft²/hr | Fog spray behind strikeoff, evaporation retarder applied before bleed water appears, finish sections immediately as each becomes ready rather than batching. |
| Ambient temp forecast to stay > 85°F through cure period | Wet-cure (soaker hose + burlap) preferred over curing compound alone for the first 24 hours — compound alone under sustained heat can seal in less moisture than a slab this hot needs. |

## 4. Cold-weather protection plan (ACI 306 triggers)

**Trigger:** mean daily air temperature forecast below 40°F for 3 or more consecutive days.

| Section thickness | Minimum concrete temp as placed | Minimum protection duration (conventional cement, no supplementary heat source) |
|---|---|---|
| < 12 in | 55°F | 3 days at ≥ 50°F, or equivalent maturity |
| 12–36 in | 50°F | 2 days at ≥ 50°F |
| > 36 in | 45°F | 2 days at ≥ 45°F |

**Worked example:** a 5-in exterior sidewalk slab poured when overnight lows are forecast at 28°F for the next four nights. Trigger is met (< 40°F, 3+ consecutive days). Section is < 12 in → hold concrete temperature at or above 55°F for 3 days using insulating blankets sized to the forecast low, not just the daytime high; remove blankets gradually over a half-day once the hold period ends so the surface doesn't thermal-shock against the outside air.

**Set-time consequence:** at 40°F, initial set can run roughly double the time it would at 60°F (set time roughly halves per ~20°F rise) — plan a longer float-to-trowel interval and don't call a slow set a "bad batch" before checking ambient and concrete temperature first.

## 5. Pour-day finishing schedule template (filled — hot-weather deck example)

```
PROJECT: Deck Level 2, 5,000 sf, 5 in, 4000 psi, 6% air (F3 exposure)
DATE / CREW: [date] / [foreman name]

SECTION 1 (6:00-8:00a placement, 55-65F):
  Bleed clears: ~8:30-9:00a → Float: 9:00a → Trowel: 9:30a
  Joint cut window: 1:00-3:00p (4-6 hrs post-finish, moderate temp)

SECTION 2 (8:00-10:00a placement, 65-75F):
  Bleed clears: ~9:15-9:45a → Float: 9:45a → Trowel: 10:15a
  Joint cut window: 2:00-3:30p

SECTION 3 (10:00a-12:00p placement, 78-88F):
  Evaporation rate: ~0.20 lb/ft2/hr -> FOG SPRAY at strikeoff, retarder on standby
  Bleed clears: <45 min after placement -> float as sheen clears, do not wait for clock time
  Joint cut window: 2:30-4:00p (compressed, hot/windy)

CURING: compound applied immediately behind trowel, each section independently.
LOG: note any retarder/fog use, actual vs. forecast temps, any deviation from plan.
```
