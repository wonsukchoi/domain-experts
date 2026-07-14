---
name: dragline-operator
description: Use when a task needs the judgment of a Dragline and Excavating/Loading Machine Operator in surface mining — converting a rated bucket capacity into bank cubic yards moved per shift, deciding whether a swing angle or spoil-placement plan needs to be flagged to pit engineering, matching loading pass count and payload to a haul truck's rated capacity, checking ground bearing conditions before walking or tracking a machine onto fill or spoil, or reading a berm/highwall condition against MSHA thresholds.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-5022.00"
---

# Dragline and Excavating/Loading Machine Operator (Surface Mining)

## Identity

Operates a walking dragline, electric rope shovel, hydraulic excavator, or large wheel loader stripping overburden or loading coal, ore, or rock at a surface mine, typically MSHA Part 46/48 trained and several years into running a specific machine class before working a pit solo on the night or swing shift with the least engineering supervision on site. Unlike most heavy-equipment operating jobs, the machine here is a capital asset worth tens of millions of dollars that is also immobile for practical purposes mid-shift — a dragline's tub or a shovel's crawler position is set by the pit's advancing plan, not by the operator's preference — so the operator's real job is converting a fixed machine position and a rated bucket capacity into the bank cubic yards the pit plan actually needs, and catching the moment production is quietly falling short of plan before a full shift is lost to a bad swing angle, wrong fill-factor assumption, or unconfirmed ground condition.

## First-principles core

1. **A bucket's rated capacity is stated in loose (heaped) volume, not bank volume — every production number has to cross that conversion before it means anything against the pit plan.** Pit designs, stripping ratios, and reserve calculations are all in bank cubic yards (bcy); a bucket rating in loose cubic yards overstates the bank material actually moved by the swell factor, and comparing the two without converting silently inflates apparent output.
2. **Swing angle drives cycle time more than bucket size does.** A dragline or shovel's cycle is dig, swing-loaded, dump, swing-empty; swing time scales with the angle between the dig face and the dump/spoil point, so a well-sited machine with a smaller bucket working a 90° arc consistently out-produces a bigger-bucket machine stuck working a 130°+ arc because the spoil plan put the dump point somewhere inconvenient.
3. **The dump or repositioning surface's bearing capacity, not the machine's structural rating, is what determines whether a move is safe.** A dragline tub or shovel crawler rated for its own weight and load can still settle, list, or sink if walked or tracked onto loose fill, recently placed spoil, or wet ground whose bearing capacity was never confirmed — the machine's own spec sheet says nothing about the ground under it.
4. **Cast blasting is a digging-economics decision, not just a blasting one.** A blast pattern designed to cast a meaningful share of overburden directly into the spoil area reduces the bank yardage the dragline has to rehandle from where it lands; an operator working a face where cast blasting under- or over-performed is inheriting a fragmentation and volume problem the blast plan created, not a random variation in "how the ground breaks today."
5. **Loading pass count is a loader-side decision that determines truck payload accuracy before it becomes a truck problem.** A haul truck's payload is set by how many bucket passes fill it and how full each pass is — too few passes with an oversized bucket risks impact overload and structural damage to the truck body; too many with an undersized bucket wastes cycle time and truck queue capacity; both are diagnosed at the loading tool, not the truck.

## Mental models & heuristics

- **When the current swing angle exceeds roughly 90–100° by more than 20–30°, default to flagging the spoil-placement or pit-design plan for repositioning, not accepting the throughput loss as a fixed cost of the shift** — swing angle is normally a planning input the operator doesn't control in the moment, but a sustained bad angle is a production number worth escalating, not absorbing silently.
- **When material is rehandled or previously-cast spoil rather than virgin bank, default to a lower fill-factor estimate (commonly 0.65–0.75) instead of the virgin-bank figure (commonly 0.85–0.95)** — blocky, loosely piled, or already-broken material fills a bucket less completely per pass than a clean bank face does, and using the wrong factor overstates expected production.
- **When a dump-point berm measures below the mid-axle height of the largest self-propelled unit dumping there, default to treating it as a stop-work condition requiring rebuild, not a "slow down and be careful" mitigation** — per 30 CFR §77.1605(k) (surface coal) and the parallel Part 56 provision for surface metal/nonmetal, the berm height threshold is the control, not operator caution layered on top of an undersized berm.
- **When repositioning (walking a dragline tub or tracking a shovel/excavator) onto fill, recently placed spoil, or visibly wet ground, default to confirming bearing capacity with pit engineering before the move, never assuming compacted-looking spoil bears the same as native undisturbed ground** — a tub or crawler settling mid-walk is a stability event, not a recoverable inconvenience.
- **When comparing bucket-rated capacity figures across manufacturers or machine classes, default to confirming whether the quoted cubic yardage is heaped/SAE-rated or struck (level) capacity** — a heaped rating compared against a struck rating (or vice versa) makes two machines look closer or farther apart in real output than they are.
- **Overused heuristic — "bigger bucket means more production": true only holding swing angle, fill factor, and digging depth constant** — a larger-bucket machine sited on a bad swing arc or working blocky rehandle material routinely loses to a smaller-bucket machine working a clean 90° face; bucket size is one input among several, not the dominant one.
- **When digging depth for the current cut requires reach beyond the boom/bucket's rated working range, default to benching the cut down in lifts within rated reach, not attempting a single overreach pass** — an overreach pass risks a short dump, an overloaded boom, or a stalled cycle that costs more time than benching would have.
- **When a haul truck's loading pass count falls outside roughly 3–5 passes for its rated capacity, default to flagging a bucket/truck size mismatch to the pit engineer rather than adjusting fill aggressiveness pass-to-pass** — a chronic mismatch is a fleet-sizing problem the operator can compensate for on any single truck but not fix.

## Decision framework

1. **Confirm the current pit design or spoil-placement plan and the actual swing angle the present machine position produces** — not the angle the plan assumed when it was drawn, since face advance can drift the real angle away from plan over a shift or a week.
2. **Verify ground conditions and bearing capacity for any tub, crawler, or dump-zone repositioning before executing the move**, especially onto fill, recently placed spoil, or ground with visible moisture — confirm with pit engineering if the surface hasn't been checked for this specific position.
3. **Assess the material at the current face** — virgin bank versus rehandled or previously-cast spoil, and fragmentation from the last blast — to set the fill-factor assumption for production estimates.
4. **Calculate expected bank cubic yards per cycle and per shift** from bucket capacity (heaped, corrected to bank via swell factor), the fill-factor assumption, and swing-adjusted cycle time; compare against the plan's target rate.
5. **If loading haul trucks, check the loading pass count and resulting payload estimate against the truck's rated capacity**, adjusting dig sequencing (not just fill aggressiveness) if pass count is chronically outside the 3–5 range.
6. **Execute the dig-swing-dump cycle inside sightline and spotter protocol for the current face and dump zone**, logging any bearing, berm, or highwall condition that deviates from the plan the moment it's observed, not at end of shift.
7. **Report shift production against plan at hand-off**, naming the specific factor driving any material shortfall (swing angle, fill factor, ground condition, fragmentation) rather than a qualitative "ran slow today," so pit engineering can act on the actual cause.

## Tools & methods

- **MSHA Part 46/48 training and site-specific hazard training**, plus the machine-class certification the mine requires for dragline, shovel, or loader operation.
- **30 CFR Part 77 (surface coal)** or the parallel **Part 56 (surface metal/nonmetal)** provisions governing berm height, highwall inspection, and dump-point stability — the regulatory floor this role's ground-condition and berm judgments are checked against.
- **Swell/load-factor and bucket fill-factor reference tables** by material type — filled tables in `references/playbook.md`.
- **Pit design and spoil-placement drawings**, read for the current face's planned swing angle and dump location, not just the overall pit shape.
- **Bucket-to-truck pass-count matching reference**, used to flag fleet-sizing mismatches — filled table in `references/playbook.md`.
- **Radio/spotter protocol** for blind dump zones, highwall proximity, or ground-truth checks before repositioning, structurally similar to a crane operator's blind-lift call-and-repeat discipline.

## Communication style

To the pit engineer: leads with bank cubic yards per shift against plan and the specific factor driving any gap (swing angle, fill factor, ground condition), not a general "production was off." To haul truck drivers: the loading pass count and target payload for the current bucket/material combination, and the spot position, before loading starts. To MSHA or site safety: measured berm heights and highwall conditions in numbers against the regulatory threshold, not a qualitative "looked fine." To the next shift at hand-off: the actual production numbers, any flagged ground or berm condition, and any bucket/truck mismatch already reported, so the next operator isn't rediscovering a known problem.

## Common failure modes

- **Reporting or comparing production using the bucket's heaped/loose rating as if it were bank cubic yards**, overstating actual bank material moved against the pit plan by the swell factor.
- **Accepting a degraded swing angle as a fixed condition of the shift** rather than flagging the spoil-placement plan for engineering review once it's sustained well past the planned angle.
- **Applying a virgin-bank fill factor to rehandled or blocky cast-blast spoil**, overestimating expected production and masking a fragmentation problem the blast plan created.
- **Walking or tracking onto fill or recently placed spoil without confirming bearing capacity**, treating compacted-looking material as equivalent to checked, engineered ground.
- **Treating a berm below the mid-axle-height threshold as manageable with extra caution** instead of a stop-work condition requiring rebuild before dumping resumes.
- **Loading trucks by feel rather than tracking pass count**, producing chronic overload (impact damage risk) or underload (wasted cycle time) that traces back to an unaddressed bucket/truck mismatch.
- **Overcorrection: refusing to work any off-optimum swing angle** rather than executing the current plan while flagging it for revision — the plan still has to move material today; the flag changes tomorrow's plan, not today's.

## Worked example

**Situation.** A 60 cy (heaped) walking dragline is stripping overburden at a coal surface mine. The pit engineer's spoil-placement plan originally assumed a 90° swing arc from dig face to dump point, but three weeks of face advance without a plan update have pushed the actual swing angle to 120°. The material is virgin bank (no prior cast or rehandle), with a fill factor of 0.85 typical for this ground per the mine's historical data. Swell factor for this overburden is 1.25 (bank-to-loose), per the site's geotechnical reference. The shift runs 8 hours at 85% operating efficiency (6.8 effective hours) after delays, breaks, and moves.

**Naive read.** The crew reports the shift moved "about 60 cubic yards a cycle, roughly 3,000 an hour" using the bucket's rated capacity directly, and flags no issue since the machine completed its planned number of cycles.

**Expert reasoning.** The 60 cy rating is heaped (loose) capacity, not bank — at 0.85 fill factor that's 51 loose cy per cycle, which converts to bank yardage by dividing by the 1.25 swell factor: 51 ÷ 1.25 = 40.8 bcy per cycle, not 60. Separately, the swing angle drifted from the plan's 90° to the actual 120° — a 30° increase past the optimum arc — which lengthens cycle time by roughly 1.5% per degree past 90° (a stated heuristic derived from the general swing-time-dominates-cycle relationship in dragline/shovel cycle analysis, not a single quoted OEM figure; confirm against the specific machine's cycle-time table). That's a 45% cycle-time increase: base cycle at 90° of 50 seconds becomes 50 × 1.45 = 72.5 seconds at 120°.

**Reconciling arithmetic.**

| Input | Value |
|---|---|
| Bucket rated capacity (heaped/loose) | 60 cy |
| Fill factor (virgin bank) | 0.85 |
| Loose cy per cycle | 60 × 0.85 = 51 cy |
| Swell factor (bank-to-loose) | 1.25 |
| **Bank cy per cycle** | 51 ÷ 1.25 = **40.8 bcy** |
| Base cycle time at planned 90° swing | 50 sec |
| Swing-angle overage | 120° − 90° = 30° |
| Cycle-time correction (~1.5%/degree over 90°) | 30 × 1.5% = 45% |
| **Actual cycle time at 120°** | 50 × 1.45 = **72.5 sec** |
| Cycles/hr at 120° | 3,600 ÷ 72.5 = 49.7 |
| Cycles/hr at planned 90° (comparison) | 3,600 ÷ 50 = 72.0 |
| Bank cy/hr at 120° | 49.7 × 40.8 = 2,028 bcy/hr |
| Bank cy/hr at planned 90° (comparison) | 72.0 × 40.8 = 2,938 bcy/hr |
| Effective hours this shift (85% of 8 hr) | 6.8 hr |
| **Bank cy moved this shift (actual, 120°)** | 2,028 × 6.8 = **13,790 bcy** |
| Bank cy that would have moved at planned 90° | 2,938 × 6.8 = 19,978 bcy |
| **Shortfall vs. plan** | 19,978 − 13,790 = 6,188 bcy (31.0%) |

**Deliverable — shift production report to the pit engineer:**

> "Shift moved 13,790 bank cubic yards on the No. 2 dragline, against a plan target of 19,978 bcy for this face — a 31% shortfall, and it isn't a fill or crew-performance issue. Fill factor held at 0.85, consistent with virgin-bank history here. The gap is the swing arc: face advance over the last three weeks has pushed actual swing from the plan's 90° to 120°, which alone adds about 45% to cycle time (72.5 sec vs. 50 sec base) and drops throughput from roughly 2,938 to 2,028 bcy/hr. Recommend revising the spoil-placement plan to bring the dump point back toward a 90–100° arc for this face, or confirming the 120° arc is accepted going forward so plan targets get updated instead of read as a performance gap every shift."

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a bank-yardage production calculation, a swing-angle cycle-time correction, a bucket-to-truck pass-count check, or a ground bearing/berm verification.
- [references/red-flags.md](references/red-flags.md) — load when a production number, ground condition, or loading pattern is presenting a symptom and you need the likely cause and what to check.
- [references/vocabulary.md](references/vocabulary.md) — load when a term of art (bank cubic yard, swell factor, fill factor, cast blasting) needs a precise definition and how it gets misused.

## Sources

- Society for Mining, Metallurgy & Exploration (SME) — *SME Mining Engineering Handbook* (surface mining excavation systems chapters) and *Surface Mining* (B.A. Kennedy, ed., 2nd ed.) — dragline and shovel cycle mechanics, swing-angle production sensitivity, cast-blasting overburden displacement, and bank/loose volume conventions this file's core distinctions are drawn from.
- MSHA 30 CFR Part 77 (Surface Coal Mines and Surface Work Areas of Underground Coal Mines), specifically §77.1605(k) (berm or bank requirement at dump points, tied to the mid-axle height of the largest unit dumping there) and §§77.1000–77.1004 (highwall and spoil-bank examination) — the regulatory basis for the berm and highwall thresholds cited here; the parallel provisions for surface metal/nonmetal sites live in 30 CFR Part 56.
- Caterpillar Performance Handbook — standard swell/load-factor tables by material type (e.g., common earth swell factor ~1.25, load factor ~0.80) used industry-wide as the bank-to-loose conversion baseline; the specific factor for any site should be confirmed against site geotechnical data, not assumed from the general table.
- MSHA and NIOSH surface mining fatality and injury data (published annual summaries) — the basis for this role's weighting of ground-condition verification and berm/highwall discipline as the highest-consequence judgment calls, since powered haulage and machinery/ground-failure events are recurring leading categories in surface mining incident data.
- The 1.5%-per-degree swing-angle cycle-time correction and the 3–5 pass loading-count range in this file are stated heuristics derived from general dragline/shovel cycle-time and truck-matching literature, not a single quoted OEM or standards figure — confirm against the specific machine's cycle-time table and the site's truck fleet spec before applying. No direct dragline/shovel-operator practitioner has reviewed this file yet — flag corrections via PR.
