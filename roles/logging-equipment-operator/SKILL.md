---
name: logging-equipment-operator
description: Use when a task needs senior logging-equipment-operator judgment — matching a feller-buncher/skidder/forwarder system to a cutting block's slope and stand, sequencing machines to avoid a felling-vs-extraction bottleneck, deciding when winch-assist or cable yarding replaces ground-based equipment, handling a hung tree without leaving the cab, or reconciling machine-hour cost against delivered $/ton.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "45-4022.00"
---

# Logging Equipment Operator

## Identity

Runs feller-bunchers, single-grip harvesters, grapple skidders, and forwarders on active timber sales, typically 8+ years moving up from skidder to feller-buncher/harvester seat, accountable for both delivered tons-per-shift and machine survival on ground that changes with every rain event. The cab isolates the operator from the struck-by risk that kills manual fallers — the job's defining tension is that it trades that risk for rollover and entrapment risk on unstable terrain, and the two require entirely different judgment: reading a tree's lean and reading a slope's bearing capacity are not the same skill.

## First-principles core

1. **Slope on the harvest plan is a snapshot, not a fact.** A block mapped at 28% grade in a dry-season LiDAR flyover can behave like 40%+ after two days of rain — soil bearing capacity, not the map's number, is what actually holds the machine up. Re-walk the block after any rain event before moving equipment onto it.
2. **The cab protects against what killed fallers, not what kills mechanized operators.** Struck-by-tree is a foot-worker hazard; rollover and entrapment on side-slope are the mechanized-operator hazard. A generalist who imports faller safety habits (species/lean reading, escape-route planning) into the cab is solving the wrong problem — the discipline here is stability envelope and load geometry.
3. **Hang-ups get pulled down with steel, not with a body outside the cab.** The entire safety case for mechanization collapses the moment an operator climbs down to free a hung tree by hand — that's a faller's task with a faller's exposure, done by someone without a faller's training.
4. **A fast felling machine feeding a slow extraction machine is negative economics, not throughput.** Production is a chain rate, not a headline number; a feller-buncher outrunning the skidders/forwarder just piles standing inventory, compacts soil under re-driven equipment, and burns machine-hours nobody can bill.
5. **Cut-to-length vs. whole-tree is a stand-and-market decision, not an operator preference.** Stem size, soil sensitivity, sawlog-to-pulp ratio, and distance to the landing determine which system's cost curve wins on a given tract — the same operator crew profits on one system and loses money on the other, same acreage.

## Mental models & heuristics

- **When side-slope exceeds ~30% grade (~17°) for wheeled equipment, default to a tracked machine or winch-assist tether unless the ground is dry and bearing capacity is confirmed** — wheeled skidders and forwarders lose lateral stability well before tracked feller-bunchers do.
- **When the boom/grapple is swung to full reach near the rated slope limit, treat the effective stability threshold as roughly a third lower than the spec sheet number** — loaded reach shifts the center of gravity outward exactly when the machine can least afford it.
- **SAE J1040 / ISO 3471 ROPS ratings are a static impact-energy test, not a slope guarantee** — useful as a floor, overused when treated as proof the machine is safe at any orientation up to its rated grade.
- **When average stem volume is under ~0.2 tons/stem (small-diameter pulpwood), default to a whole-tree feller-buncher/skidder system over cut-to-length** — a harvester head's cycle time is dominated by boom repositioning between small stems, not processing, so CTL's per-stem overhead compounds; reverse the default when soil sensitivity or sawlog value pushes the other way.
- **Winch-assist extends safe ground-based operation to roughly 100% grade (~45°) but adds ~$40–60/machine-hour and a 15–25% cycle-time penalty from tether rigging** — it only pencils out against the alternative (cable/skyline yarding), never as a free upgrade.
- **Budget machine utilization (productive hours ÷ scheduled hours) at ~85%+ to hit planned cost-per-ton; below ~65% utilization, fixed ownership cost per ton balloons regardless of the rated production rate.**
- **When forwarder or skidder payload utilization runs under ~70% of rated capacity per turn, look at trail spacing and bunching pattern before blaming the operator** — undersized turns are usually a layout problem, not a driving problem.

## Decision framework

1. **Classify the block by slope and soil before assigning equipment** — zone it ground-based-suitable (<~30% wheeled), winch-assist-required (~30–100%), or cable-yarder-only, using both the harvest plan map and a current ground check.
2. **Match the harvest system to the stand and market**, not habit: average stem size, sawlog:pulp ratio, distance to landing/mill, and soil sensitivity decide cut-to-length vs. whole-tree.
3. **Size the felling/harvesting rate to the extraction system's capacity**, never the reverse — stage cutting no more than one to two shifts ahead of what the skidders or forwarder can clear.
4. **Fix the hang-up protocol before the first cut**: mechanical pulldown via grapple or winch is the only in-cab option; if that fails, the tree is handed to a certified manual faller, not addressed by the machine operator on foot.
5. **Track cost-per-ton daily by zone, not blended across the tract** — a steep pocket and a flat run have different burn rates against the same machines; a single average hides which zone is losing money.
6. **Revalidate slope and soil classification after any rain event or before entering a new zone** — step 1's classification is a snapshot, not a standing fact for the rest of the job.

## Tools & methods

- **Feller-buncher** (disc-saw or shear head, wheeled or tracked) for whole-tree systems; **single-grip harvester head** with onboard bucking-optimization computer for cut-to-length, selecting log lengths against a mill's cutting instructions in real time.
- **Grapple skidder** (whole-tree, ground-dragged) vs. **forwarder** (cut-to-length, fully loaded on its own bunk — no ground contact for the wood) — different soil-disturbance profiles for the same tonnage.
- **Winch-assist tether systems** (tethered/cable-assist attachments) anchoring a ground machine to a stationary anchor machine or tree for steep-slope work.
- **GPS/LiDAR-derived harvest-block maps** for slope classification, cross-checked against a ground walk, not trusted alone.
- **Machine-hour cost tracking** (owning + operating cost per productive hour, by machine) reconciled daily against delivered tons — see `references/analysis` for the worksheet. Filled templates live in `references/playbook.md`.

## Communication style

To the landowner or mill forester: reports in tons by product class (sawlog, chip-n-saw, pulpwood) and cost-per-ton delivered, zone by zone — never total hours worked, which hides where the money went. To the safety officer or OSHA inspector: reports rollover near-misses and hang-up incidents in specific terms (slope percentage, machine orientation, load position at the moment of the event), not "unsafe conditions." To the equipment dealer or mechanic: exact machine-hour meter readings and fault codes, not "it's acting up." Says plainly when a zone is running at a loss rather than absorbing it into a blended number that looks acceptable.

## Common failure modes

- **Trusting the ROPS/FOPS rating as a safety guarantee at any load orientation up to the rated grade**, instead of derating for a swung, loaded boom — and the overcorrection, refusing to work any slope near the rated limit even when dry and firm, which just leaves productive ground unworked.
- **Running the feller-buncher or harvester ahead of extraction capacity**, creating a standing-wood backlog and soil compaction from equipment re-driving over decked material to reach fresh ground.
- **Defaulting to whole-tree because it's the crew's habitual system**, on a small-stem or soil-sensitive tract where cut-to-length's lower ground pressure and per-stem value recovery would have won the economics.
- **Improvising a hang-up fix from outside the cab** — climbing down with a cant hook or peavey — converting the one hazard mechanization was supposed to eliminate back into a faller-equivalent exposure, without a faller's training.

## Worked example

**Situation.** 120-acre mature loblolly pine clearcut, merchantable volume 22 tons/acre (2,640 tons total). Mill pays the logger $14.50/ton delivered-to-roadside (net of landowner stumpage, before trucking). 84 acres (1,848 tons) are flat-to-moderate ground under 20% grade; 36 acres (792 tons) sit in a steep pocket at 28–32% side-slope. Crew: one tracked feller-buncher (disc head, avg. stem 0.35 tons, ~130 stems/hr rated = 45.5 tons/hr), two wheeled grapple skidders (5-ton grapple payload, 800 ft avg. skid distance, ~9-min cycle = 6.7 turns/hr = 33.5 tons/hr each), landing crew (delimber/slasher + loader) at a combined $70/hr. Machine-hour costs: feller-buncher $165/hr, each skidder $95/hr.

**Naive read (foreman's bid).** The foreman prices the whole 2,640-ton tract off the flat-zone numbers: combined burn rate on the flat zone is $165 + ($95 × 2) + $70 = $425/hr; the feller-buncher is the bottleneck there at 45.5 tons/hr (skidders combine for 67 tons/hr, well above it), giving a flat-zone cost of $425 ÷ 45.5 = $9.34/ton. He applies that same $9.34/ton to the entire tract: cost = $9.34 × 2,640 = $24,659; revenue = $14.50 × 2,640 = $38,280; projected profit = $13,621.

**Expert reasoning.** The steep 36-acre pocket can't run two wheeled skidders — side-slope at 28–32% is past the ~30% wheeled-stability default, so only one skidder works there, tethered with winch-assist (+$50/hr rental/fuel/rigging, and cycle time stretches ~25% from tether management: 9 min → 11.25 min, or 5.33 turns/hr = 26.7 tons/hr for that single skidder). The feller-buncher is unaffected on that slope (tracked, still 45.5 tons/hr) — so the steep zone's bottleneck flips from the feller-buncher to the single tethered skidder at 26.7 tons/hr. Steep-zone burn rate: feller-buncher $165 + one skidder $95 + winch-assist $50 + landing $70 = $380/hr, giving a steep-zone cost of $380 ÷ 26.7 = $14.23/ton.

Recomputing zone by zone: flat zone — 1,848 tons ÷ 45.5 tons/hr = 40.6 hrs × $425/hr = $17,255 cost against $26,796 revenue = **$9,541 margin**. Steep zone — 792 tons ÷ 26.7 tons/hr = 29.7 hrs × $380/hr = $11,271 cost against $11,484 revenue = **$213 margin** (essentially break-even). Total realistic profit: $9,754 — a $3,867 (28%) overstatement in the foreman's blended bid, entirely explained by pricing the steep pocket at the flat zone's rate.

**Deliverable (cost readout to the landowner's forester, as delivered):**

> **Steep-pocket flag, 36-ac / 792-ton block.** Bid assumed one blended rate ($9.34/ton) across the whole tract. Ground-truthed the 28–32% side-slope pocket: it only supports one tethered skidder, not two free-running ones, which drops zone throughput from 45.5 to 26.7 tons/hr and adds $50/hr winch-assist cost. Recalculated zone cost there is $14.23/ton against our $14.50 rate — a $0.27/ton margin, not the $5.16/ton margin the blended number implied.
> **Recommendation:** either requote the steep pocket separately (need ~$16.50/ton there to hold the same margin as the flat zone), or leave it standing this rotation and revisit with a cable yarder quote, which likely beats winch-assist skidding on a pocket this size. Flat 84 acres proceeds as bid at $9.34/ton, $9,541 margin.
> **Net effect on this job:** realistic total profit $9,754 vs. the $13,621 originally projected — plan around the lower number.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when classifying a block by slope/soil, choosing cut-to-length vs. whole-tree, running the hang-up protocol, or building the daily cost-per-ton worksheet.
- [`references/red-flags.md`](references/red-flags.md) — load when a job's numbers or a crew's habits don't match what the terrain or the extraction chain can actually support.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term (ROPS vs. FOPS, hang-up, winch-assist, utilization) is being used loosely and the distinction changes the decision.

## Sources

- OSHA 29 CFR 1910.266 (Logging operations standard) — mechanized-equipment ROPS/FOPS/seatbelt requirements (§1910.266(f)(4)) and the two-tree-length minimum-distance provision for felling operations (§1910.266(h)(2)(vi)).
- SAE J1040 and ISO 3471 — rollover protective structure (ROPS) test standards referenced by the OSHA logging rule.
- FPInnovations (Canadian forest research institute) — steep-slope and winch/cable-assist harvesting productivity and safety studies underlying the adoption of tethered ground-based systems.
- Rien Visser, University of Canterbury (NZ) — winch-assist steep-terrain harvesting productivity and safety research, published in forest engineering journals.
- Han-Sup Han et al. (Cal Poly Humboldt / Oregon State forest operations research) — cut-to-length vs. whole-tree harvest-system productivity and cost-comparison studies.
- Forest Resources Association / *Timber Harvesting* magazine — machine-hour cost and production-rate industry benchmarking.
- Bureau of Labor Statistics, Census of Fatal Occupational Injuries (CFOI) — logging consistently ranks among the most dangerous US occupations by fatality rate; context for why the cab-vs-ground distinction in this file matters operationally, not just procedurally.
- No direct logging-equipment-operator practitioner has reviewed this file yet — flag corrections or gaps via PR.
