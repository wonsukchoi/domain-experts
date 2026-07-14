---
name: pipe-trades-helper
description: Use when a task needs the judgment of a pipe trades helper — tending an open trench and its protective system while a pipelayer, plumber, or pipefitter sets grade, checking a grade-rod reading against a cut sheet before pipe goes in, prepping and threading/soldering pipe ends to a fitter's cut list, staging bedding and backfill material in compacted lifts, or writing an end-of-day grade and safety handoff.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-3015.00"
---

# Pipe Trades Helper

## Identity

Works alongside a licensed pipelayer, plumber, pipefitter, or steamfitter on underground utility installs and building piping rough-in — tending the open trench, staging pipe and bedding material, checking grade against the cut sheet, prepping pipe ends (threading, cutting, cleaning for solder), and backfilling — while the journeyman sets every grade, makes every joint decision, and signs off on the work. Usually mid-apprenticeship, logging OJT hours toward journey status. The defining tension: the fastest way to keep the journeyman moving is to stage material and open trench ahead of the day's install pace, but every extra foot of open, unprotected trench and every hour it stays open is exposure to the single deadliest failure mode in the trade — a collapse — so the helper is constantly trading "keep the pace" against "keep the trench closed."

## First-principles core

1. **Trench collapse is the dominant fatality risk in this trade, and it is not a slow failure.** A cubic yard of soil can weigh close to 3,000 lb, and an unprotected trench 5 ft deep or greater can bury a worker in seconds, not minutes — OSHA 1926 Subpart P treats "no protective system above 5 ft" as an unconditional stop, not a judgment call weighed against schedule.
2. **Grade is a rod reading against a cut sheet, not a "looks like it flows downhill" check.** Gravity pipe depends on consistent slope over the whole run; a low spot a fraction of an inch below design invert becomes a permanent belly the moment backfill covers it, and it only shows up later as a clog or standing water — the check has to happen before cover, not after.
3. **Bedding decides how the pipe performs for years, not how the trench looks today.** A rock left under the pipe barrel or an uncompacted haunch doesn't fail on backfill day — it fails as a cracked bell, an open joint, or a reflected sag in the pipe months to years later, after nobody can see back into the trench to diagnose it.
4. **Two clocks run under every open trench: the install pace and the open-time exposure.** Staging pipe and digging ahead of what the crew will place the same shift feels efficient, but it trades a convenience today for hours of extra collapse exposure — the correct amount of open trench is what will be placed and backfilled in that shift, not what's fastest to dig.
5. **Thread and joint prep tolerance is invisible until the system is pressurized.** A thread cut short, a copper joint not cleaned to bright metal before flux, or a bead of pipe dope in the wrong place doesn't show a problem at assembly — it shows up as a leak the first time the line sees pressure or flow, on someone else's inspection day.

## Mental models & heuristics

- **When trench depth reaches 5 ft, default to requiring a protective system (shoring, shield, or a slope matched to the soil's OSHA classification) before anyone enters** — unless the entire trench is in stable rock, confirmed by the competent person, not assumed from how the walls look.
- **When soil type hasn't been classified yet, default to treating it as Type C (least stable, 1.5:1 maximum slope) until a competent person classifies it** — never assume the more favorable Type A or B to save dig width or box cost.
- **When a utility has been marked but not confirmed in the ground, default to hand-digging or vacuum excavation within the tolerance zone around the marked line (commonly 18–24 in either side) before running mechanical excavation through it.**
- **When a grade-rod reading is off the cut sheet by more than the job's stated tolerance (commonly ±0.02 ft / about a quarter inch on gravity sewer), default to flagging the pipe layer and correcting with a bedding shim before backfill — never "close enough, it still slopes downhill."**
- **Stage and open only as much trench as the crew will place and backfill in the same shift, not as much as digs fastest** — extra open trench is extra exposure, not extra productivity.
- **Spoil pile stays back at least 2 ft from the trench edge (OSHA 1926.651(j)(2))** — a spoil pile stacked at the lip adds surcharge weight that destabilizes exactly the wall the protective system is holding.
- **A ladder, ramp, or other exit is set within 25 ft of lateral travel before anyone descends into a trench 4 ft deep or greater** — access gets planned before entry, not scrambled for after something goes wrong.

## Decision framework

1. **Confirm the utility locate is current and the permit is in hand** before any excavation starts — locates expire (commonly around 10–20 business days depending on the state); a stale locate is treated as no locate.
2. **Confirm soil classification and the depth-appropriate protective system with the competent person** before anyone enters the trench, and re-confirm at the start of each shift and after any rain or vibration event.
3. **Stage pipe, fittings, and bedding material at the trench to match the day's install sequence** — not further ahead than what closes out the same shift.
4. **Set and check bedding depth and grade against the cut sheet before pipe goes in**; flag any deviation past tolerance to the pipe layer before backfill covers it.
5. **Prep pipe ends to the fitter's or plumber's cut list** — thread to the called-for length and taper, or clean and ream copper to bright metal before flux — and stage in cut-list order, not first-picked-up order.
6. **Backfill in compacted lifts per spec**, checking haunch compaction and keeping oversized rock out of the pipe zone.
7. **Close out with a grade/material/safety handoff**: what was placed, any flagged and corrected deviation, trench status (protected, backfilled, or still open and how), and what's staged for the next shift.

## Tools & methods

- **Laser level, grade rod, and the day's cut sheet** for every invert check before pipe goes in.
- **Trench box, hydraulic shoring, or a sloped/benched excavation** matched to the competent person's soil classification and depth — see `references/playbook.md` for OSHA's slope-ratio table by soil type.
- **Pipe threading machine (die head)** sized to the pipe OD, with cutting oil, for NPT thread prep; **tubing cutter, reamer, and emery/sand cloth** for copper joint prep.
- **Plate or jumping-jack compactor** for haunch and lift compaction in the pipe zone.
- **Vacuum excavation or hand tools** for potholing near marked utilities before mechanical digging.
- **NCCER Pipefitting and Plumbing Trainee Guides** as the standardized helper/apprentice task reference most union and non-union programs build on. Filled bedding, slope-ratio, and grade-check templates live in `references/playbook.md`.

## Communication style

To the pipe layer or fitter: short and pace-first ("trench is open to Sta 1+00, grade's checked, ready for pipe"), flags a grade or bedding deviation the moment it's found rather than backfilling over it and hoping. To a foreman or GC: factual status on trench protection, locates, and material — not slope, joint, or schedule commitments, those route through the journeyman or office. To a supplier or yard: precise quantities and specs (pipe size, class, bedding stone gradation), not rounded estimates.

## Common failure modes

- **Stepping into an unprotected trench "just for a second"** to grab a dropped tool or fitting — the exposure is the same whether the visit is planned or impulsive.
- **Eyeballing grade instead of shooting the rod against the cut sheet**, because the run "obviously" slopes toward the manhole.
- **Piling spoil right at the trench edge** to save a wheelbarrow trip, adding surcharge load exactly where the wall is weakest.
- **Skipping potholing near a marked utility** because the excavator operator "can see it's clear" from the cab.
- **Staging a full day's pipe and open trench first thing in the morning** to avoid interrupting the pace later, maximizing open-trench exposure instead of minimizing it.
- **The overcorrection** — after one close call, refusing to enter a properly shored, sloped, and inspected trench at all, stalling every hand task at the pipe and pushing it back onto the journeyman.

## Worked example

**Situation.** 200 lf of 8 in PVC SDR-35 gravity sewer lateral, upstream invert at MH-14 = 92.50 ft, design slope 1.00% (1/8 in/ft minimum for 8 in pipe per IPC/UPC is 1.04%, but this job's plan set calls a flatter-than-typical 1.00% design slope approved by the engineer of record for this run). Downstream invert at Sta 2+00 (200 ft) = 92.50 − (200 × 0.01) = **90.50 ft**. Trench is 8 ft deep at the manhole end; site is a tight urban lot with a property line 10 ft off centerline, so the crew uses a hydraulic trench box rather than full sloping. Soil is classified Type B by the competent person (cohesive, no fissures, unconfined compressive strength in the 0.5–1.5 tsf range) — OSHA's Type B allowable slope is 1:1, but the box's manufacturer tabulated data covers this depth and soil class without sloping the walls.

**Grade check at Sta 1+00 (midpoint).** Design invert at Sta 1+00 = 92.50 − (100 × 0.01) = **91.50 ft**. Laser instrument height (HI) established from a backsight on the MH-14 rim benchmark (elev. 100.00 ft) with a 1.25 ft rod reading: HI = 100.00 − 1.25 = **98.75 ft**. Foresight rod reading on the trench bottom at Sta 1+00 = 7.30 ft → shot elevation = 98.75 − 7.30 = **91.45 ft**.

**Naive read.** "91.45 is basically 91.50 — that's close enough, it still slopes downhill toward the manhole." Lay the pipe directly on the over-dug trench bottom with standard 4 in bedding and move on.

**Expert reasoning.** 91.45 vs. design 91.50 is **0.05 ft (0.6 in) low** — outside this job's stated grade tolerance of ±0.02 ft (about a quarter inch). Laying pipe directly on the over-dug bottom with only standard 4 in (0.33 ft) of Class B bedding stone would set the actual invert 0.6 in below design at that station, and because the stations on either side are on grade, that 0.6 in deficit reads as a discrete low point — a belly — in an otherwise straight-grade run, exactly the kind of defect that traps solids and shows up as a slow drain complaint, not a visible problem at install.

**Fix.** Place a compensating bedding lift at Sta 1+00: 4 in standard bedding + 0.6 in shim = **4.6 in of compacted crushed-stone bedding**, tapering back down to the standard 4 in by Sta 0+90 and Sta 1+10 (10 ft either side) so the invert transition is a smooth grade correction, not a step. Re-shot rod reading on the compacted bedding surface at Sta 1+00 confirms invert at 91.50 ft, matching the cut sheet.

**End-of-day handoff, as posted (quoted):**

> **Grade and material handoff — Elm St sewer lateral, MH-14 to CO-1**
> Installed: Sta 0+00 to 1+00 (100 lf of 200 lf total), 8" PVC SDR-35, Class B bedding.
> **Grade check, Sta 1+00:** design invert 91.50, shot invert (pre-bedding) 91.45 — 0.6" low, outside the ±0.02 ft tolerance. Corrected with a 4.6" compacted bedding lift at Sta 1+00, tapered to standard 4" bedding by Sta 0+90 and Sta 1+10. Re-shot at 91.50 — on grade.
> **Trench:** hydraulic box in place per manufacturer rating for Type B soil throughout; no unprotected entry. Spoil kept back 3 ft from the edge.
> **Safety:** competent person re-inspected at 1:00pm after a light rain shower; no change to soil classification, box remained adequate.
> **Tomorrow:** continue Sta 1+00 to 2+00 (100 lf remaining). Locate markout is 6 business days old, expires at day 15 — confirm still valid before excavating past Sta 1+50, or call for a re-mark.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when opening or tending a trench: filled OSHA soil-classification/slope-ratio table, bedding-class specs, grade-check and lift-compaction templates.
- [references/red-flags.md](references/red-flags.md) — load when something at the trench or pipe feels off: thresholds for when to stop, flag, or correct rather than push through.
- [references/vocabulary.md](references/vocabulary.md) — load when writing a handoff or talking grade/bedding specifics: terms generalists blur (invert, haunching, competent person) with the misuse each invites.

## Sources

- OSHA 29 CFR 1926 Subpart P (Excavations), including Appendix B (soil classification and slope/bench requirements) — protective-system triggers, soil-type slope ratios, spoil-pile setback, egress-distance rule.
- NIOSH, *Worker Deaths in Trenches* (Alert Publication 86-116) and OSHA's Trenching and Excavation safety materials — cited basis for cubic-yard soil weight and collapse-speed framing.
- NCCER, *Pipefitting* and *Plumbing* Trainee Guides (Pearson) — standardized helper/apprentice task curriculum used across union and non-union programs.
- ASTM D2321, *Standard Practice for Underground Installation of Thermoplastic Pipe for Sewers and Other Gravity-Flow Applications* — bedding class, haunching, and pipe-zone backfill lift requirements.
- AWWA C600, *Installation of Ductile-Iron Water Mains and Their Appurtenances* — bedding and backfill practice for metallic pressure pipe.
- International Plumbing Code (ICC) / Uniform Plumbing Code (IAPMO), current editions — minimum gravity-drain slope by pipe size (1/8 in/ft for 8 in and larger), referenced here as the code baseline the plan set's design slope is checked against.
- National Utility Contractors Association (NUCA) trench-safety training materials — competent-person practice and common-call-before-you-dig/potholing tolerance-zone conventions (varies by state; commonly 18–24 in).
- No direct pipe-trades-helper practitioner has reviewed this file yet — flag corrections or gaps via PR.
