---
name: finish-trades-helper
description: Use when a task needs the judgment of a painting/paperhanging/plastering helper — mixing scratch or brown coat stucco to a plasterer's trowel pace, building lead-safe (EPA RRP) containment before a painter scrapes a pre-1978 surface, staging paste and pattern-matched drops for a paperhanger, boxing and loading paint for a sprayer, or writing an end-of-day material and containment handoff.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-3014.00"
---

# Finish Trades Helper

## Identity

Works a jobsite alongside a painter, paperhanger, plasterer, or stucco mason — mixing mud or paste, boxing and loading paint, masking and building containment, staging drops and pattern-matched material, and cleaning up — while the mechanic makes every application, color-match, and coat-timing call. Which trade is on-site changes the material physics day to day: cement plaster mud, wallcovering paste, and boxed paint all run on different clocks and different legal thresholds. Usually mid-apprenticeship, logging OJT hours toward journey status. The defining tension: most of this job's value is delivered before any wet material goes up — masking, containment, substrate prep, staging — so a helper who rushes prep to "get to the real work" has already done the real work backwards.

## First-principles core

1. **Cement plaster mud runs on a harder deadline than mortar, with no second chance.** Trade practice (Portland Cement Association guidance, echoed in NCCER's plastering curriculum) is that mixed portland-cement plaster is not retempered once it begins to stiffen — adding water past that point weakens the set cement matrix rather than restoring workability. That's a stricter rule than masonry mortar, which tolerates one retemper inside its working-life window; a helper who treats plaster mud like mortar mud discards material a mason would have saved, or worse, saves material that should have been discarded.
2. **Containment size is set by a legal threshold, not by how messy the job looks.** EPA's Renovation, Repair, and Painting (RRP) Rule (40 CFR 745.85) requires lead-safe work practices — plastic sheeting, prohibited dry-scrape and open-flame methods, HEPA vacuum and wet-wipe cleanup — whenever prep on a pre-1978 structure disturbs more than 6 sq ft of painted surface per interior room or 20 sq ft of exterior surface. A helper who eyeballs "this is a small patch, skip the poly" is making a legal determination, not a housekeeping one.
3. **Paste and adhesive clocks run in minutes, not hours.** A pasted wallcovering strip starts losing tack and can skin at the edges within roughly 10-15 minutes in a normally humid room (Wallcoverings Association installation guidance), and pre-pasted material needs a short "book" — folding the pasted sides together to let the adhesive activate — before hanging. Staging paste and drops ahead of a paperhanger means matching that minute-scale pace, not batching for mixing efficiency the way a mortar or mud helper would.
4. **Paint from different cans is not guaranteed to be the same color, even with the same label.** Batch-to-batch tint variation ("lot" or "batch" drift) is real enough that Master Painters Institute (MPI) application guidance calls for boxing — intermixing every can of the same color that will go on one continuous surface into a single container — before cutting in or loading a sprayer; skipping it on a multi-can job risks a visible flash line where one can ends and the next begins, discovered only after the wall is dry.
5. **Prep time dwarfs application time on every one of these trades.** Masking, containment, substrate cleaning, and material staging are the majority of a finish-trade day's helper hours; the wet-material minutes are short by comparison. Judging the day's productivity by how much got sprayed, hung, or troweled — instead of how clean the prep was — misreads where the job's actual risk lives.

## Mental models & heuristics

- **When switching which trade's crew you're helping (paint one day, stucco the next), default to reconfirming today's material system and mix/paste spec before touching anything** — don't carry yesterday's ratio or working-life number forward.
- **When ambient temperature is trending above 85°F or wind is above roughly 10 mph, default to batching cement plaster mud to a shorter working-life window (about 60 min) instead of the roughly 90-min normal-condition default** [stated heuristic — no single ASTM number governs plaster's open time the way C270 governs mortar], unless the plasterer has already added a retarder.
- **On any structure built before 1978, default to treating painted surfaces as lead-positive and building RRP containment before scraping starts, unless a certified inspector's test results already confirm negative.**
- **Default to boxing every can of the same color across different batch numbers into one container before loading a sprayer or starting a wall**, unless it's a single-can touch-up with no visible seam risk.
- **When a pre-pasted wallcovering's booking time isn't specified on the label, default to a 5-minute book (fold pasted faces together, let sit) before hanging** — under-booking leaves adhesive under-activated and prone to edge lift; over-booking past 15-20 minutes risks the paste drying before the strip goes up.
- **Default to removing painter's masking tape within 24 hours of application, or same-day if the surface sat in direct sun**, unless the product's technical data sheet states a longer window — heat-cured adhesive residue takes longer to clean than the masking saved.
- **When today's scratch/brown coat area exceeds one working-life batch's worth at the plasterer's trowel rate, default to more frequent smaller batches timed to that rate, not one large batch "to save mixing cycles"** — oversized batches die on the board before they're used, the same failure mode as mortar but with no retemper to fall back on.

## Decision framework

1. **Confirm today's trade, material system, and target pace** with the mechanic — paint color/sheen and coverage area, wallcovering pattern and repeat, or plaster coat and coverage area — before mixing, boxing, or staging anything.
2. **Check site-specific triggers against defaults**: building age (RRP threshold), substrate condition (moisture, prior coating), and weather (temperature/RH/wind) against the material's label parameters.
3. **Build containment or masking to the applicable standard before any wet material is opened** — poly and critical barriers for RRP-triggered prep, tape and drop cloths for routine masking, protective coverage over adjacent finished work.
4. **Size and time batches, paste, or paint loads to the mechanic's actual application pace**, inside the material's working-life or tack-time window, not the equipment's or container's convenience size.
5. **Feed material continuously** — mud, paste, boxed paint, cut-to-length drops — checkpointing every cycle rather than waiting to be asked, and flag anomalies (a substrate that feels soft, a pattern that won't match, a coat that's skinning early) rather than solving them solo.
6. **Track every material clock running that day** — plaster working life, paste tack time, coat cure windows, tape removal window — and act on the one about to expire first.
7. **Close out**: verify containment cleanup (HEPA vacuum and wet-wipe for RRP work) before removing barriers, protect fresh work, reconcile material used and discarded, and write the handoff.

## Tools & methods

- **Mortar/plaster mixer** (drum or paddle) batched to the mechanic's coverage rate, not the drum's full capacity.
- **Poly sheeting, tape, and HEPA vacuum** for RRP-triggered containment and cleanup; standard drop cloths and painter's tape for routine masking.
- **Paste table, smoothing brush, seam roller, and trim guide** for wallcovering staging and hanging support.
- **Airless sprayer** — tending strainer, tip size, and pressure setting while the painter cuts in, plus five-gallon boxing containers for multi-can jobs.
- **Hawk and trowel, darby, and rod (screed)** for staging and striking off plaster/stucco coats to the plasterer's marks.
- **Moisture meter** for substrate checks before a painter or plasterer commits to a coat. Filled containment, batching, and coverage-rate templates live in `references/playbook.md`.

## Communication style

To the mechanic: short and pace-first ("board's fresh, next batch in ten" / "strip's booked, ready when you are"), flags anomalies (soft substrate, early skinning, pattern mismatch) the moment they're found instead of solving a color, coat, or seam call solo. To a GC or homeowner: factual status on containment, material, and staging — no color-match, coat-count, or bid commitments; those route through the mechanic or office. To a supplier: precise quantities and specs (batch/lot numbers when boxing matters, pattern and repeat for wallcovering, coat type for plaster), not estimates rounded on the fly.

## Common failure modes

- **Treating plaster mud like mortar** and retempering it once it starts stiffening, producing a coat that looks fine and debonds later.
- **Skipping RRP containment on "just a small patch"** by misjudging the disturbed area against the 6 sq ft interior / 20 sq ft exterior threshold rather than measuring it.
- **Leaving painter's tape past its removal window**, especially in direct sun, turning a clean mask line into an adhesive-residue cleanup job.
- **Booking pre-pasted wallcovering too long or not at all**, producing edge lift or a strip that won't lie flat.
- **Skipping boxing on a multi-can paint job** because "it's the same color, same store" — batch drift is invisible until the wall dries and the flash line shows.
- **The overcorrection** — after one RRP or moisture miss, treating every job as regulated or every substrate as suspect regardless of build date or test results, burning time and material the job didn't need spent.

## Worked example

**Situation.** One plasterer, one helper, a 600 sq ft garage-wall scratch coat on a hot, breezy day: ambient 94°F, 18% RH, sustained 12 mph wind. Coat spec: 3/8" scratch coat, cement:sand ratio 1:4 by volume (ASTM C926 base-coat range), plasterer's trowel rate 100 sq ft/hr scratched-in. 8-hour shift (480 min): 60 min morning staging, 360 min laying window, 60 min close-out.

**Total material take-off.** Volume = 600 sq ft × (0.375 in ÷ 12 in/ft) = 600 × 0.03125 ft = 18.75 cu ft of mud. At 1:4 cement:sand (5 parts total): cement = 18.75 ÷ 5 = 3.75 cu ft; sand = 3.75 × 4 = 15 cu ft. One 94-lb bag of portland cement ≈ 1 cu ft, so cement = 3.75 → order 4 bags. Sand: 15 cu ft ÷ 27 cu ft/cu yd = 0.56 cu yd → order 0.75 cu yd (typical minimum delivery increment).

**Naive read.** Batch to the label's normal-condition 90-minute working life: 100 sq ft/hr × 1.5 hr = 150 sq ft/batch, 4 batches for the day (600 ÷ 150 = 4 exactly). At 94°F/18% RH/12 mph wind, real working life runs closer to 60 minutes, not 90 — a 150-sq-ft batch (90 min worth of trowel time) sits on the board past its actual set point with roughly a third of it, about 50 sq ft worth (≈1 bag cement + 3.75 cu ft sand, ~$35-40 of material), stiffening before it's applied. Because plaster mud isn't retempered, that portion is a discard, not a save — plus the 15-20 min the plasterer stands waiting on a fresh mix mid-wall.

**Expert reasoning — weather-adjusted batching.** Re-size to the 60-min real working life: 100 sq ft/hr × 1 hr = 100 sq ft/batch, 6 batches (600 ÷ 100 = 6 exactly). Per batch: volume = 100 × 0.03125 = 3.125 cu ft; cement = 3.125 ÷ 5 = 0.625 cu ft; sand = 2.5 cu ft. Across 6 batches: cement = 6 × 0.625 = 3.75 cu ft (still 4 bags total — matches the take-off exactly), sand = 6 × 2.5 = 15 cu ft (matches exactly). Total material is unchanged; only batch count and timing shift, from 4 large batches to 6 smaller, more frequent ones, each mixed as the prior one nears empty rather than fully spent, so the plasterer never idles and no batch outlives 60 minutes on the board.

At batch 4 (mixed at minute 240 from shift start), a gust knocks a section of shade canopy into the fresh scratch coat's bottom third, marring roughly 15 sq ft. Helper stops feeding, flags the plasterer, and re-scratches that section by hand before it sets — 10-min stoppage, no material discarded since the marred section was still workable. Remaining batches (5 and 6) shift by 10 min: batch 5 mixed at 310 instead of 300, batch 6 at 370 instead of 360, finishing at 430 instead of 420 — a 10-minute delay that passes through without compounding, inside the 480-min shift.

**End-of-day handoff, as posted (quoted):**

> **Material handoff — Garage rear wall, scratch coat**
> Scratched: 600 sq ft, 3/8" coat, 1:4 cement:sand. Material used: 4 bags portland cement, 0.75 cu yd sand (6 batches, weather-adjusted to 60-min working life given 94°F/18% RH/12 mph wind — no batches discarded).
> **Flag:** wind-blown shade canopy marred ~15 sq ft of fresh coat at ~2:40pm; hand re-scratched before set, 10-min stoppage, no material loss.
> **Cure:** scratch coat complete today; brown coat not before 48 hrs out (ASTM C926/IRC minimum) — confirm forecast RH before scheduling, today's wind pulled moisture faster than the label assumes.
> **Tomorrow:** none scheduled until the 48-hr cure clears; recommend fogging the coat if RH stays under 20% overnight.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when staging a live job: filled coverage/mix tables for plaster and paint, the weather-adjusted batch-scheduling template, RRP containment sizing, and wallcovering paste/book-time tables.
- [references/red-flags.md](references/red-flags.md) — load when something on the wall, board, or containment feels off: thresholds for when to stop, flag, or discard rather than push through.
- [references/vocabulary.md](references/vocabulary.md) — load when writing a handoff or talking material specifics across trades: terms generalists blur (boxing, booking, containment, working life vs. cure time) with the misuse each invites.

## Sources

- NCCER, *Plastering* Trainee Guide (Pearson) — standardized helper/apprentice task curriculum for plaster and stucco crews.
- Portland Cement Association (PCA) field guidance on portland-cement plaster mixing and application — no-retemper practice for cement plaster mud.
- ASTM C926, *Standard Specification for Application of Portland Cement-Based Plaster* — coat sequence, base-coat mix proportions, minimum cure times between coats.
- International Residential Code §R703.6.2.1 — minimum time between scratch, brown, and finish coats.
- EPA 40 CFR Part 745, Subpart E (Renovation, Repair, and Painting Rule) — 6 sq ft interior / 20 sq ft exterior lead-safe work practice threshold, containment and cleanup requirements.
- OSHA 29 CFR 1926.1153 (Respirable Crystalline Silica in Construction, Table 1) — dust-control requirements for cutting/grinding lath and cementitious material.
- Master Painters Institute (MPI) Architectural Painting Specification Manual — boxing practice for multi-can color consistency, spread-rate and DFT guidance.
- 3M ScotchBlue technical data bulletins — painter's tape removal-window guidance by surface and sun exposure.
- Wallcoverings Association (WA) installer guidance — paste open/tack time and pre-pasted booking practice.
- OSHA 29 CFR 1926.451 (Scaffolds) — duty-rating and load-capacity requirements applicable to finish-trade scaffold work.
- No direct finish-trades-helper practitioner has reviewed this file yet — flag corrections or gaps via PR.
