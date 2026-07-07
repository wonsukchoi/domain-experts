# Playbook

Filled worksheets and sequences for calibration, mixing, and rotation planning. These are templates to populate with the day's numbers, not descriptions of what a template should contain.

## Calibration worksheet (catch-test method)

Formula: **GPA = (GPM × 5,940) ÷ (MPH × W)**, where GPM is catch-cup output per nozzle in gallons/minute, MPH is travel speed, and W is nozzle spacing in inches (or effective swath width in inches for a boomless nozzle).

**Filled example — backpack sprayer, basal-bark stem treatment (not a boom, so calibrated by output-per-minute against target coverage rather than the boom formula):**

- Target: 1.5% v/v triclopyr ester in basal oil carrier, applied to the lower 12–15 in of each stem to wet but not run off.
- Nozzle output measured into a catch cup: 22 oz over 60 seconds of continuous trigger time.
- Estimated stems treated per minute at a walking pace through moderate brush: 4.
- Output per stem: 22 oz ÷ 4 = 5.5 oz/stem — checked against label guidance of 3–6 oz per stem for the stated stem-diameter range; passes.

**Filled example — boom truck, broadcast:**

- Boom width 30 ft (360 in), 18 nozzles at 20-in spacing, travel speed 3 mph.
- Single-nozzle catch, 60 sec: 26 oz = 0.2031 GPM.
- GPA = (0.2031 × 5,940) ÷ (3 × 20) = 20.1 GPA against a 20 GPA target (0.5% variance — pass; recalibrate if any nozzle's individual catch differs from the others by more than 10%, which indicates a partial clog or wear).

## Tank-mix jar-test sequence

Mixing order matters because out-of-order loading causes gelling, separation, or reduced activity that a jar test catches in five minutes instead of in a 200-gallon tank.

1. Fill jar with the water source actually being used on-site (not tap water from the shop) at the mix ratio scaled down — e.g., 1 pint water to represent 100 gallons.
2. Add water-conditioning agent first if the tank water is hard (see red-flags.md) — commonly ammonium sulfate (AMS) for glyphosate.
3. Add dry/wettable-powder formulations, agitate fully before adding anything else.
4. Add liquid flowable formulations, agitate.
5. Add emulsifiable concentrates, agitate.
6. Add surfactants/adjuvants last, agitate.
7. Let the jar stand 15–30 minutes; check for separation, clumping, or a layer that won't re-suspend with shaking. Any of those is a no-go for that combination — retest with a different order or drop a product rather than loading the full tank on a hunch.

## MOA rotation table (right-of-way herbicide program, 3-year plan)

| Year | Primary MOA (WSSA group) | Example active ingredient | Note |
|---|---|---|---|
| 1 | Group 9 (EPSP synthase inhibitor) | Glyphosate | Broad burndown, non-selective |
| 2 | Group 4 (synthetic auxin) | Triclopyr or 2,4-D | Selective to broadleaf/woody, spares grass cover |
| 3 | Group 2 (ALS inhibitor) tank-mixed with Group 4 | Metsulfuron + triclopyr | Two MOAs in one pass; do not repeat Year 1's Group 9 as the sole active two years running |

Rule of thumb from the Take Action program: no single MOA group applied as the sole active ingredient more than two consecutive seasons on the same stand.

## REI and PPE reference by chemical class (label-driven — confirm against the specific product's label; WPS sets a 4-hour floor when a label is silent)

| Chemical class | Example REI | Typical PPE |
|---|---|---|
| Glyphosate (Group 9) | 4 hr (WPS floor; many labels state 4–12 hr) | Long sleeves/pants, chemical-resistant gloves, eye protection |
| Triclopyr ester (Group 4) | 12 hr (this label's stated figure — varies by formulation/task) | Above plus chemical-resistant footwear for basal work |
| Organophosphate insecticide (occasional ROW use) | 24 hr to 5 days depending on task/formulation | Above plus respirator per label; some tasks barred entirely during REI |

## Buffer-zone / aquatic-label decision

| Condition | Default |
|---|---|
| Treated area is more than the label's stated buffer distance from any water body | Standard terrestrial formulation is permitted |
| Treated area is within the buffer distance, or water is present within the ROW itself | Use only the aquatic-labeled formulation of that active ingredient; do not substitute a terrestrial formulation "because the label rate is the same" — aquatic labels differ in surfactant package and approved use sites |
| Ephemeral/intermittent drainage crosses the ROW but is dry at time of application | Still treat as a buffer trigger unless the label explicitly exempts dry channels — most do not |

## Wind/weather go–no-go chart

| Condition at nozzle height | Action |
|---|---|
| Wind < 3 mph | Hold — inversion risk; do not spray unless label explicitly permits low-wind spraying with coarse+ droplets |
| Wind 3–10 mph | Spray window (default; confirm against this label's specific ceiling) |
| Wind > 10 mph (or label's stated ceiling) | Hold, regardless of droplet size selected |
| Clear, calm evening/early-morning conditions near a sensitive downwind crop | Treat as elevated inversion/vapor-drift risk even if wind reads in-window; hold auxin-herbicide applications |

## Second filled spray work order (roadside segment, different scenario)

> **Segment:** County road shoulder/ditch, 3.4 mi × 15 ft average treatment width = 6.2 ac.
> **Target:** Grass and broadleaf regrowth along guardrail sections; no woody brush control needed this cycle.
> **Product:** Glyphosate 1 qt/ac (Group 9 — first season on this segment, no rotation concern yet), 15 GPA broadcast.
> **Mix:** 6.2 ac × 15 GPA = 93 gal total mix. Product: 6.2 × 1 qt = 6.2 qt = 1.55 gal. Water = 93 − 1.55 = 91.45 gal.
> **Calibration:** boom 24 ft (288 in), 16 nozzles at 18-in spacing, travel 4 mph. Catch 60 sec = 15 oz = 0.1172 GPM. GPA = (0.1172 × 5,940) ÷ (4 × 18) = 696.2 ÷ 72 = 9.67 GPA — 35% under the 15 GPA target. **Fail — do not spray.** Cause: nozzle wear or undersized tips for the target rate at this speed; re-tip or slow travel speed to 2.6 mph (696.2 ÷ (2.6×18)=14.9 GPA) and retest before proceeding.
