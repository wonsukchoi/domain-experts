# Playbook

Filled reference tables and step sequences for the three recurring decisions: material selection by zone, dry-out/cure scheduling, and expansion-joint sizing.

## 1. Material selection by zone — service-temperature and chemistry table

| Material class | Typical max service temp | Best-fit atmosphere/duty | Typical campaign life in matched duty | Fails fast when |
|---|---|---|---|---|
| Fireclay brick (low/high duty) | ~2600–2800°F | Clean, oxidizing, low mechanical/chemical attack (flues, low-temp kiln zones) | 3–5 years in matched duty | Used above ~2800°F or exposed to alkali/slag |
| High-alumina brick/castable (60–90% Al₂O₃) | ~3000–3200°F | General-purpose high-heat, neutral atmosphere (kiln preheater/calciner, reheat furnaces) | 12–24 months | Exposed to alkali/sulfate dust or molten slag contact |
| Silicon carbide | ~3000°F+ (thermal-shock limited, not just temp-limited) | Abrasion + thermal-cycling duty (cyclones, kiln inlet, incinerator refractory exposed to particulate wash) | 12–36 months depending on abrasion load | Specified for peak temp alone while ignoring cycling/abrasion |
| Magnesia-chrome / magnesia-spinel (basic) | ~3200°F+ | High-alkali, high-sulfate, slag-contact zones (cement kiln burning zone, BOF/EAF vessel) | 8–14 months in kiln burning zone; hundreds of heats in BOF | Used where cost pressure substitutes high-alumina for a basic-duty zone |

**Selection rule, applied in order:**
1. Pull the zone's measured peak temperature (not nameplate) for the last 12 months.
2. Pull atmosphere/chemistry data: alkali or sulfate dust recirculation, slag basicity, reducing vs. oxidizing.
3. If peak temp is within ~200°F of a candidate material's rated max, move up one class.
4. If chemistry shows alkali, sulfate, or slag contact, require basic or SiC regardless of temperature margin — chemistry, not heat alone, is what shortens life in these zones.
5. Cost-compare on **annualized cost** (material + labor + downtime × relines/year), never on installed cost per square foot alone — see the worked example in `SKILL.md` for the arithmetic.

## 2. Dry-out / cure schedule — castable refractory, by thickness

| Section thickness | Free-moisture hold | Ramp to 300°F | Ramp above 300°F to service temp | Total heat-up time (approx.) |
|---|---|---|---|---|
| ≤2 in | 4 hrs at 230–250°F | 75°F/hr | 150°F/hr | 12–18 hrs |
| 2–4 in | 8 hrs at 250–275°F | 50°F/hr | 100°F/hr | 24–36 hrs |
| 4–9 in | 1 hr per inch of thickness at 275–300°F | 50°F/hr | 100°F/hr | 3–6 days |
| >9 in | 1.5 hrs per inch of thickness at 275–300°F | ≤50°F/hr | ≤75°F/hr | 6–10+ days |

**Non-negotiable rule:** the moisture hold is sized to let steam migrate to the surface faster than internal pressure builds — it is not a buffer to cut when the schedule is tight. Every hour cut from the hold on a >4 in section increases steam-spall probability; there is no published safe-compression factor because the failure mode is a threshold effect, not a linear one.

**Field checks during heat-up (any one triggers a hold, not just a slowdown):**
- Visible steam or moisture at the hot face beyond the planned hold window.
- Popping/cracking sounds from the lining.
- Thermocouple readings plateauing or reversing instead of tracking the planned curve (moisture still migrating — hold until it resumes tracking).
- Embedded thermocouple delta between hot-face and mid-wall exceeding the material supplier's stated safe gradient.

## 3. Expansion-joint sizing

**Step sequence:**
1. Get the material's linear thermal expansion coefficient at service temperature (supplier data sheet; typical range 0.5% for fireclay to ~1.2–1.5% for silicon carbide and some basic brick).
2. Calculate absolute growth per linear foot of lining run: `growth (in) = coefficient × run length (in)`.
   - Example: 40 ft (480 in) run of magnesia-chrome brick at 1.0% expansion → 4.8 in of total growth across the run.
3. Distribute that growth across joints spaced no wider than the material/thickness combination allows — as a rule of thumb, one joint every 3–6 courses (roughly 18–36 in of run) for lining thickness up to 9 in; tighten spacing for thicker linings or higher-expansion materials.
   - 480 in run ÷ 24 in joint spacing ≈ 20 joints; 4.8 in total growth ÷ 20 joints = 0.24 in of expansion allowance per joint.
4. Fill joints with a compressible, burn-out paper or ceramic-fiber spacer sized to that per-joint allowance — undersized spacers leave the lining to absorb growth structurally; oversized spacers leave gaps that slag or hot gas can penetrate.
5. Re-verify joint spacing and width whenever thickness or material class changes between campaigns — a joint layout copied from the prior campaign's thinner or different-material lining under-allows for growth.

## 4. Reline decision — patch/gunning vs. full reline

| Factor | Favors patch/gunning | Favors full reline |
|---|---|---|
| Remaining campaign life needed | <8–10 weeks to next scheduled outage | >10–12 weeks, or life unknown |
| Wear pattern | Localized (single hot spot, known cause) | Distributed across zone or multiple failure points |
| Downtime available now | Short window only | Full outage already scheduled |
| Prior failure history at this location | First occurrence | Second or later occurrence at same spot this campaign |

**Rule:** compare the patch's cost (material + labor + downtime for the patch itself) to the probability-weighted cost of an unplanned mid-campaign failure it's meant to avoid — `expected failure cost ≈ P(failure before next outage) × (emergency-downtime cost + emergency-reline cost)`. When that expected cost exceeds the full-reline cost brought forward, do the full reline now instead of patching.
