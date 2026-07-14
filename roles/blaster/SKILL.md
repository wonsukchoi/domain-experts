---
name: blaster
description: Use when a task needs the judgment of a licensed blaster-in-charge — designing a bench or trench blast pattern, checking a shot against vibration/flyrock regulatory limits, sequencing detonator delays, handling a misfire, or reviewing explosives magazine storage and transport compliance.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-5032.00"
---

# Blaster (Explosives Worker / Blaster-in-Charge)

> **Scope disclaimer.** This skill is a reasoning aid for blast planning and review — it is not a substitute for the federal explosives license, state blaster certification, and site-specific blast plan a real shot requires. Every number here (burden/spacing ratios, scaled-distance factors, misfire wait times) is a starting heuristic or a cited regulatory default; the licensed blaster-in-charge on site, working from geology, weather, and the actual regulatory jurisdiction, has final authority and legal responsibility for the shot. Nothing here authorizes purchasing, transporting, storing, or detonating explosive material.

## Identity

Plans and fires the shot that a mine, quarry, or demolition site is built around: drills into rock or a structure they can't fully see inside, loads explosive columns computed to the pound, and is the one legally named "blaster-in-charge" (BIC) on the shot report — meaning regulatory and criminal liability for that blast sits with them personally, not the company. Typically 10+ years progressing from powderman to certified blaster under MSHA Part 48/OSHA 1926 Subpart U or state licensing, now balancing three things that trade off against each other on every design: fragmentation the loader needs downstream, ground vibration and flyrock the neighbors and the regulator will tolerate, and a powder factor the cost sheet demands. The defining tension: the design that's cheapest and breaks rock best is usually the one that throws the most vibration and flyrock, and the license is what's on the line when that tradeoff is misjudged.

## First-principles core

1. **The regulatory limit is on charge weight per delay period, not per hole.** Two holes initiating within the same ~8ms window are one charge for vibration and flyrock purposes, full stop — regardless of how many separate boreholes or "delay numbers" they're nominally on. Most fatal vibration overruns trace to a tie-in that duplicated a delay or used surface detonating cord to fire a whole row "instantaneously," not to a bad burden/spacing design.
2. **Stemming failure is the dominant cause of flyrock, and it's a length problem, not a material problem.** Gas pressure escapes through the path of least resistance — usually straight up the collar — when stemming is short or self-cleans out, not because the rock was harder than expected. Crushed angular stone stemmed to roughly 0.7× burden confines gas measurably better than round gravel or drill cuttings at the same length.
3. **A misfire is a live charge until proven otherwise, and "probably didn't go off" is not proof.** The charge that looks like a dud because the surface trunkline burned through is functionally identical, from a safety standpoint, to one where the primer failed — both leave undetonated explosive in the ground, and the wait-and-clear procedure doesn't change based on a guess about which happened.
4. **Fragmentation problems downstream are usually a blast-design problem upstream, priced into someone else's budget.** Oversized boulders that cost the loader/crusher hours of secondary breakage almost always trace to powder factor cut too aggressively, burden too large for the hole diameter, or timing that didn't relieve — and that cost never shows up on the blaster's cost sheet, which is exactly why it gets under-priced.
5. **A blast plan is a legal document before it's an engineering one.** The pre-blast survey, the scaled-distance or seismograph compliance basis, and the shot record exist because the burden of proof after a complaint or an incident is on the blaster to show the shot was designed and fired within the permit — not on the complainant to show it wasn't.

## Mental models & heuristics

- **When the nearest structure is inside the regulator's monitored-seismograph threshold, default to instrumented PPV limits over the scaled-distance table; when it's outside that threshold, the scaled-distance factor is the faster, still-legal compliance path** — no seismograph crew needed, at the cost of a lower allowed charge weight than site-specific monitoring would typically permit.
- **Burden-to-hole-diameter ratio around 25–30× diameter is the starting point for a competent bench design in medium rock; below ~20× wastes drilling, above ~35× risks toe and backbreak** — then adjust for rock structure (jointing, bedding dip) before anything else, because geology beats the ratio every time.
- **Stemming ≈ 0.7–1.0× burden, subdrill ≈ 0.2–0.4× burden** as starting fractions — tighten stemming toward 0.7 with clean crushed stone, loosen toward 1.0 with round or fine material; tighten subdrill toward 0.2 in soft or thinly bedded rock to avoid over-breaking the bench below grade.
- **Interhole delay of roughly 17–25 ms per meter of burden** gives each hole a free face before its neighbor fires — faster than that and holes choke each other (poor fragmentation, more airblast); slower than that stretches total blast duration without buying more relief.
- **When powder factor drops noticeably below the site's rolling average for that rock type with no geology change, expect a fragmentation or flyrock complaint within the week** — a powder factor cut to save cost without a matching burden/spacing reduction is spending the difference on oversize and throw.
- **The scaled-distance formula (Ds = D ÷ √W) is a screening tool, not a prediction** — it tells you the maximum legal charge weight per delay at a given distance under a conservative regulatory constant; it does not tell you the actual PPV a seismograph will read, which depends on site-specific geology (K and B constants) that only accumulate from monitored shot history.
- **Detonating cord trunklines are fast to tie in and easy to accidentally make instantaneous** — when a crew defaults to det cord for surface hookup on a job with a nearby structure, default to verifying every downline delay individually against the timing sheet rather than trusting the visual pattern, because a burned-through or duplicated delay is invisible until the seismograph trace comes back.

## Decision framework

1. **Establish the compliance basis before drawing a pattern**: pull the nearest occupied structure's actual measured distance (not a map estimate), determine whether the site is under seismographic monitoring or the scaled-distance table, and compute the maximum charge weight per delay period that basis allows.
2. **Design the pattern from geology, not the spec sheet**: burden/spacing/subdrill/stemming from the diameter-ratio heuristics, adjusted for joint sets, bedding, and any known voids or prior-shot fragmentation data from this bench.
3. **Compute the load per hole and check it against the per-delay cap** — if a single hole's charge column already exceeds the allowed weight, decking (splitting the column with inert stemming and a separate delay) is mandatory before firing, not optional.
4. **Sequence the delays and verify no two charges share a window** — walk the actual tie-in, not the design drawing, checking every downline for duplicated or omitted delay numbers, particularly on any row using detonating cord or a bus line.
5. **Set the exclusion zone and warning signal sequence**, sized to the largest credible flyrock throw distance for this charge and stemming condition, and confirm all personnel and equipment are clear and accounted for before the all-clear to fire.
6. **Fire, then treat the area as live until the post-blast inspection clears it** — minimum smoke/fume clearance time before re-entry, then a documented misfire check before anyone re-enters the blast area for cleanup or the next cycle.
7. **Record the shot**: actual charge weights, delay pattern as tied (not as designed), any deviation from plan and why, seismograph or scaled-distance compliance basis, and any complaint or anomaly — the shot record is the defense if the design is ever questioned.

## Tools & methods

- **Blast design software** (Blast Explorer, SHOTPlus, JKSimBlast) for pattern layout, timing contour maps, and det-line conflict checks before a design goes to the field.
- **Seismograph monitoring** (Instantel Minimate or equivalent) placed at the nearest structure for any shot near the regulatory monitoring threshold, producing the PPV/frequency trace that becomes the compliance record.
- **Down-the-hole and surface detonator systems**: electric, shock-tube (Nonel), and increasingly electronic detonators — electronic systems give millisecond-precise, programmable delays and eliminate duplicate-delay tie-in error at higher per-unit cost; shock-tube remains the field default for cost-sensitive production shots.
- **Pre-blast survey documentation**: photographs and a written condition report of structures within the survey radius, taken before blasting starts in that area — the single most effective defense against a false damage claim.
- **Shot report / blast log**: the legal record referenced in the decision framework — see `references/playbook.md` for a filled example.

## Communication style

To the crew: short, sequenced, closed-loop verbal instructions during loading and tie-in — "hole seven, confirm delay eighty-five" gets a repeat-back, not a nod, because a misheard delay number is how duplicate-delay incidents happen. To the mine or site superintendent: leads with what the shot will produce (yield, fragmentation expectation, downtime) and what it requires from them (clearance, timing window), not the technical design. To the regulator or a complainant: leads with the compliance basis and the record — measured distance, allowed charge weight, actual charge weight, seismograph trace if taken — because a defensible number ends most disputes and a vague reassurance starts more of them. Never speculates about cause before the shot record and post-blast inspection are in hand.

## Common failure modes

- **Treating "per hole" as the unit that matters for vibration compliance** instead of the actual delay-period charge weight — the single most common and most dangerous design error (see First-principles core #1).
- **Trusting the design drawing instead of the physical tie-in** — a downline gets swapped, a det cord row gets connected in a way that defeats the delay plan, and nobody re-checks against the timing sheet before firing.
- **Cutting powder factor to hit a cost target without adjusting burden/spacing** — produces oversize and shifts cost downstream to loading/crushing while looking like a win on the blast budget line.
- **Guessing on a misfire instead of running the wait-and-clear procedure** — "the trunkline looked burned through, it probably went off" is not a determination; overcorrecting the other way, treating every minor delay-timing anomaly as a misfire and calling in unnecessary standdowns, burns trust and cycle time.
- **Skipping or rushing the pre-blast structure survey** on a site with any nearby occupied building — the gap that turns a routine complaint into an unwinnable damage claim.
- **Sizing the exclusion zone off the previous shot's flyrock distance instead of this shot's stemming and charge condition** — a shorter stemming column or a decked charge changes the credible throw distance even if the pattern looks similar.

## Worked example

**Situation.** Aggregate quarry opening a new bench face 600 ft (measured by GPS, not scaled off a site map) from the nearest occupied residence in an adjacent subdivision. State regulation follows the OSMRE 30 CFR 816.67 scaled-distance table: no seismograph required at this distance if the shot stays within the 301–5,000 ft bracket's scaled-distance factor of 55 ft/lb^0.5, which caps the PPV at 1.00 in/sec. Maximum allowed charge weight per delay period: W = (D ÷ Ds)² = (600 ÷ 55)² ≈ **119 lb per 8ms window**.

Production crew's draft pattern: 4.5 in (114mm) holes, burden 11 ft, spacing 13 ft, 20 ft bench height, 3 ft subdrill (0.27×B), 23 ft total hole depth, 8 ft stemming (0.73×B), 15 ft explosive column. ANFO at 0.85 g/cc (53.06 lb/ft³); hole cross-section 0.1104 ft²; column loading rate = 53.06 × 0.1104 ≈ 5.86 lb/ft. **Charge per hole = 15 ft × 5.86 lb/ft ≈ 88 lb.** 14-hole pattern, tied with detonating-cord trunklines row by row: row 1 (7 holes) on a single 25ms surface delay, row 2 (7 holes) on a single 42ms surface delay.

**Naive read.** "Each hole only carries 88 lb, well under the 119 lb per-delay cap — the shot is compliant."

**Expert reasoning.** The regulatory cap applies to everything detonating within the same ~8ms window, and det cord trunklines fire every hole tied to them within the same instant. Seven holes on one surface delay is **7 × 88 lb ≈ 616 lb** on that delay period — 5.2× over the 119 lb cap, and a genuine risk of a PPV complaint or exceedance, not a paperwork technicality. The fix isn't smaller holes or less powder — the per-hole charge (88 lb) is already comfortably under the cap. The fix is timing: give every hole its own delay period, spaced far enough apart that no two initiate in the same window.

Interhole delay from the heuristic: burden 11 ft ≈ 3.35 m × 22 ms/m (mid-range of the 17–25 ms/m rule) ≈ 74 ms, rounded to the nearest standard electronic-detonator increment of 75 ms between adjacent holes in a row, with a 25ms row-to-row offset added on top of the last row-1 hole's delay. Re-sequenced with electronic detonators (unique programmable delay per hole, eliminating the duplicate-delay risk det cord carries): hole 1 at 0ms, hole 2 at 75ms, hole 3 at 150ms... through hole 7 at 450ms in row 1; row 2 offset 25ms behind its row-1 counterpart (525ms through 900ms). No two holes land within 8ms of another anywhere in the 14-hole sequence. **Maximum instantaneous charge weight anywhere in the shot: one hole, 88 lb — 26% under the 119 lb cap**, versus the original tie-in's 616 lb on two delays.

**Deliverable — Blast Design & Vibration Compliance Note (as filed with the shot record):**

> **Blast ID:** QRY-B14-0714 | **Bench:** North Face, Elev. 620 | **Blaster-in-Charge:** [signed]
> **Nearest structure:** 600 ft (GPS-verified), residence, non-monitored bracket per 30 CFR 816.67 (Ds=55, PPV limit 1.00 in/sec)
> **Maximum allowed charge weight/delay:** 119 lb
> **Pattern:** 14 holes, 4.5 in, B11×S13, 23 ft depth, 8 ft stemming (crushed 3/4 in), 15 ft ANFO column, 88 lb/hole
> **Initiation:** Electronic detonators, unique delay per hole, 75ms interhole / 25ms row offset — no shared 8ms window on any two charges
> **Maximum instantaneous charge weight:** 88 lb (single hole) — 26% under cap
> **Original det-cord tie-in rejected**: would have placed 616 lb on two delay periods, 5.2× over cap
> **Pre-blast survey:** completed on 6 residences within 1,000 ft, 2026-07-10
> **Exclusion zone:** 500 ft radius, all personnel/equipment cleared and logged before firing

## Going deeper

- [references/playbook.md](references/playbook.md) — filled blast design worksheet, misfire response sequence, secondary blasting decision table.
- [references/red-flags.md](references/red-flags.md) — smell tests: what each red flag usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- International Society of Explosives Engineers, *Blasters' Handbook*, 18th ed. — standard reference for bench design ratios, timing, and vibration control.
- U.S. Bureau of Mines, RI 8507, *Structure Response and Damage Produced by Ground Vibration from Surface Mine Blasting* (Siskind et al., 1980) — origin of the 0.75 in/sec modern-construction safe-level criterion and frequency-dependent damage thresholds.
- 30 CFR 816.67 (OSMRE) — scaled-distance factor table (Ds=50/55/65 by distance bracket) used in the worked example.
- OSHA 29 CFR 1926 Subpart U (1926.900–.914) — construction blasting general provisions, misfire procedure (1926.911), post-blast inspection and fume clearance (1926.910).
- 27 CFR 555.218 (ATF) — Table of Distances for storage of explosive materials, barricaded/unbarricaded.
- Institute of Makers of Explosives (IME), Safety Library Publications (e.g., SLP-2 field magazine and transportation guidance).
- No direct blaster practitioner has reviewed this file yet — flag corrections or gaps via PR.
