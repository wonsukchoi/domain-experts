---
name: roof-bolter
description: Use when a task needs the judgment of a Roof Bolter — reading a roof control plan's bolt pattern and length against measured CMRR conditions, interpreting a pull test or sounding result against the plan's anchorage assumption, selecting resin by gel/spin time for ambient temperature, deciding whether a ground condition requires a plan deviation before advancing, or sequencing an ATRS cycle within its setback limit.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-5043.00"
---

# Roof Bolter

> Roof control decisions in this file are reasoning aids for a roof bolter or foreman working under a mine's MSHA-approved roof control plan. They do not substitute for that plan, for a certified/registered mine engineer's sign-off on a deviation, or for MSHA District Manager approval — always the plan and the district's requirements govern, not this file.

## Identity

Installs and inspects the primary ground support — roof bolts, resin, screen, and supplemental support — that keeps the entry roof from falling in on the crew working under it, usually as a certified bolter-operator running a single- or dual-head bolting machine on a working section, following the mine's MSHA-approved roof control plan under 30 CFR 75.220. The job is accountable to two different failure modes at once: a hardware failure (a bolt that doesn't reach its rated tension) and a rock-mass failure (roof that behaves worse than the plan assumed even though every bolt met spec) — and only one of those two shows up on a torque wrench.

## First-principles core

1. **A bolt passing its tension check and the roof matching the plan's rock-mass assumption are two different facts, and a torque wrench only measures the first one.** The minimum-tension rule (50% of bolt yield or anchorage capacity, whichever is less, under 30 CFR 75.222(b)(2)) tells you the hardware anchored. It says nothing about whether the anchorage capacity itself — tons of pull resistance per foot of resin encapsulation — still matches the rock class (CMRR) the plan's pattern and bolt length were designed around. A bolt can pass its own tension floor in rock that has quietly gotten weaker than the plan assumed.
2. **Bolting doesn't make weak rock strong — it binds separate weak layers into one thicker beam, and that only works if the bolt length actually spans the separation.** A 4-ft bolt set in roof with bed separation starting at 5 ft doesn't reinforce the extra foot; it just doesn't reach it. Bolt length is a beam-thickness decision tied to the mapped CMRR and known parting depths for that heading, not a default carried over from the last entry.
3. **Resin anchorage is a chemistry-and-timing problem before it's a torque problem.** Spin time has to stay under gel time or the resin sets before mixing completes and the bolt torques up against unmixed material that looks anchored and isn't; gel time itself shifts with cartridge type and ambient/hole temperature. A bolt that "feels right" on the wrench can still be sitting in a hole that never fully mixed.
4. **Unsupported roof exposure is a fixed geometry, not a judgment call made per cut.** The ATRS setback (outby edge of the ATRS crossmember/rocker pads no more than 5 ft from the last row of permanent support, 30 CFR 75.203/75.209) exists because the phase-in of ATRS on bolting machines all but eliminated fatal roof falls tied to manually set temporary support — stretching that setback "just this once" reintroduces exactly the exposure the rule eliminated.
5. **Methane and respirable silica are invisible until the detector or the sample says otherwise — there's no felt-sense version of either.** A face reading at or above 1.0% methane requires de-energizing electrical equipment in the area under 30 CFR 75.323 regardless of how the air "feels," and drilling into rock with quartz content is the highest respirable-dust-generating task on the section, governed by a fixed 50 µg/m³ full-shift PEL, not a discomfort threshold.

## Mental models & heuristics

- **When a pull test or SEPT (short encapsulation pull test) result comes back below roughly 12 tons per foot of resin encapsulation, default to treating the heading's CMRR assumption as suspect and escalating to the foreman/engineer**, unless the mine's approved plan already documents a lower design floor for that specific horizon — 12–24 tons/ft is the range NIOSH ground-control research treats as good anchorage, and typical coal-horizon results run 10–15 tons/ft, so a single-digit reading is a real outlier, not noise.
- **When the roof sounds hollow/drummy over a bar-sounding pass across more than a few feet of the cut, default to installing supplemental support (screen plus a tighter pattern) before advancing that heading**, unless a competent person's inspection attributes the sound to a specific non-separation cause (an old exploration hole, a known geologic marker already accounted for in the plan).
- **When ambient or hole temperature is low enough that spin time can't be reliably kept under the cartridge's rated gel time, default to switching to a slower-gel resin cartridge for that shift rather than shortening spin time to compensate**, unless a temperature-adjusted spin/gel chart for that specific product confirms the margin still holds.
- **When entry width exceeds 20 ft, default to a combination of roof bolts and conventional supports (posts, cribs) per 30 CFR 75.222(b)(3)**, unless the approved plan specifies an engineered bolts-only pattern rated for that span.
- **When a tension or torque reading can't be confirmed at or above 50% of bolt yield or anchorage capacity (whichever is less), default to re-anchoring that hole — redrill, re-resin, or add a supplemental bolt — before moving to the next hole**, unless the failure traces to a miscalibrated tool, in which case swap the tool and re-check, don't wave the hole through.
- **Extended cut depth (commonly 20 ft rather than the baseline) is a privilege earned by a mine's demonstrated roof-fall history and CMRR at that specific horizon, not a standing default**, so when the crew enters a heading without that history — new panel, unfamiliar rock, a mapped fault or rider seam nearby — default back to the plan's baseline cut depth until engineering extends it in writing for that heading.
- **Standard bolt pattern (commonly 5 ft along-entry by 4 ft between rows, or as set by the approved plan) is the floor for competent-looking roof, not a pattern that gets loosened when the crew is behind schedule** — tightening the pattern in a weak zone is a documented deviation; loosening it to make time is not a decision a bolter operator makes alone regardless of how solid that stretch has looked all shift.

## Decision framework

1. **Pull the approved roof control plan's pattern, bolt type/length, resin spec, and the CMRR assumption for the specific heading before drilling the first hole** — don't carry forward the last entry's numbers from memory.
2. **Sound the roof with a bar or pick across the full width of the planned cut before positioning the ATRS**, noting any drummy response, visible parting, slips, or cutter roof at the rib line.
3. **Drill and install per the plan's spec — hole depth, resin cartridge count and type, spin time, hold time, tension target — and pull-test or torque-check bolts at the plan's required sampling rate**, not only the first hole of the shift.
4. **Compare every check against two separate floors: the regulatory minimum tension (50% of yield or anchorage capacity) and the anchorage-capacity range implied by the plan's CMRR for that rock.** A hardware pass with a rock-mass-level miss (anchorage capacity below the CMRR-implied range even though tension cleared) still needs escalation — it is not resolved by re-torquing.
5. **If sounding, pull-test results, or visible geology diverge from the plan's assumption, stop advancing that heading and get a documented deviation (supplemental bolts, screen, tighter pattern, or a shorter cut) from the foreman or mine engineer before continuing** — never resolve the gap by installing to the old pattern and hoping.
6. **Cycle the ATRS after each row, keeping the outby edge within the setback limit, and re-sound before every new advance** — the setback and the sounding check both run every cycle, not once per shift.
7. **Log the pattern actually installed, resin lot/type, tension results, and any deviation on the shift and roof-control records** — the next crew inherits what's written, not what the current crew remembers doing.

## Tools & methods

- **Single- or dual-head roof bolting machine with ATRS** — the temporary-support platform the operator works under; setback and positioning are checked every cycle, not assumed from the last row.
- **Torque wrench / hydraulic tensioning gauge**, calibrated against the bolt manufacturer's torque-to-tension conversion for the specific bolt and thread — a torque reading is only meaningful for the bolt it was calibrated against.
- **SEPT (short encapsulation pull test) kit** — a reduced-embedment sample bolt pulled to failure or to a target load, used to verify resin anchorage capacity independent of the full-length installed bolts.
- **Resin cartridges (fast-set and slow-set)**, selected by ambient/hole temperature against the product's gel-time chart, not by habit. See `references/playbook.md` for a filled selection table.
- **Roof screen and mesh straps**, deployed as supplemental support in zones flagged by sounding or pull test, not as a blanket default.
- **Sounding bar or pick**, run across the roof before every cut — the cheapest, fastest ground-condition check available and the one most often skipped under time pressure.
- **Methane detector and personal dust monitor**, checked at fixed trigger points (1.0% methane, dust sampling per the mine's compliance plan), not on a felt-sense basis.

## Communication style

To the foreman or section boss: plan-compliance terms — pattern installed, tension results, any deviation and its authorization — not a narrative of the shift. To the mine engineer, when contesting a plan's assumption for a specific heading: CMRR and pull-test numbers, cited against the plan's design floor, not "it just feels soft up there." To a green crew member: concrete, sequenced instruction ("sound it here, here, and here before we set up — a hollow return means we stop and call it in"), because ground-condition judgment is exactly the skill a new bolter hasn't built yet and can't be handed as an abstraction. On any deviation from the approved pattern: written, citing the plan section and the data (pull test tons/ft, sounding location) that triggered it — never a verbal "we did it a little different back there."

## Common failure modes

- **Reading a pull test as pass/fail against bolt tension only**, missing that the anchorage-capacity number itself has fallen below the range the plan's CMRR assumed — the exact gap the worked example below walks through.
- **Letting spin time creep toward or past gel time** on a cold shift without switching cartridge type, so bolts torque up against partially mixed resin that reads as anchored on the wrench and isn't at design strength.
- **ATRS setback creep** — repositioning the machine slightly past the 5-ft limit because the last row of bolts "is basically right there," treating a fixed geometric limit as a judgment call for one cycle.
- **Skipping the sounding pass** in a heading that "has always been solid," which is precisely the condition under which a sounding check catches a new parting before it becomes a fall.
- **Overcorrection: installing supplemental screen and a tighter pattern on every cut regardless of CMRR or pull-test result**, which burns cycle time without matching actual risk and trains the crew to treat supplemental support as routine — so the one time it's flagged for a real reason, it doesn't register as different.
- **Loosening the approved pattern to make up schedule**, treating the plan's spacing as a target rather than a floor — a decision that isn't the bolter operator's to make alone under any level of schedule pressure.

## Worked example

**Situation.** Entry No. 3, a new heading in a panel where the approved roof control plan sets pattern and bolt length off a mapped CMRR of 58 (moderate) for that horizon: 4-ft fully grouted #6 Grade 75 rebar bolts (rated yield ≈ 64,000 lbf, per the bolt manufacturer's spec sheet), 5-ft along-entry by 4-ft between-row pattern, 24-in (2-ft) resin encapsulation, standard 20-ft-wide entry, extended cut depth of 20 ft (approved for this panel based on the mine's roof-fall history). Minimum required installed tension per 30 CFR 75.222(b)(2): 50% of 64,000 lbf = 32,000 lbf (16 tons).

**Naive read.** Fifteen feet into the cut, the crew notices the roof sounds slightly hollow when sounded but keeps advancing since the shift is already behind. A sample bolt in that stretch is pulled and torques up to 36,000 lbf (18 tons) — above the 32,000 lbf (16-ton) minimum tension requirement — so a bolter operator reading only the tension check would sign off: "bolt passed, pattern's fine, keep going."

**Expert reasoning.** The 36,000 lbf reading is a hardware pass, but it's the wrong number to stop the check at. Back out the anchorage capacity per foot of encapsulation: 36,000 lbf ÷ 2 ft = 18,000 lbf/ft ≈ 9 tons/ft. NIOSH ground-control research treats 12–24 tons/ft as the accepted "good" anchorage range, with typical coal-horizon results running 10–15 tons/ft — 9 tons/ft sits below both the accepted floor and the typical range for this rock type. The bolt only reached its 16-ton tension minimum because it needed just 16 of the roughly 18 tons the hole's 2-ft encapsulation happened to deliver; the margin above minimum tension is thin, and 9 tons/ft is not what a CMRR-58 heading should be producing. Combined with the drummy sound the crew already noted and dismissed, this is a rock-mass signal, not a hardware signal — the parting the plan assumed was fully bound by a 4-ft bolt may extend further than mapped in this specific stretch. The correct move is to stop advancing this heading and call it in, not to log the 18-ton pull test as a pass because it cleared 16.

**Numbers for the deviation.** Drummy zone measures 15 ft along the entry by the full 20-ft width = 300 sq ft. At the original 5×4-ft pattern (20 sq ft/bolt), that zone would take 300 ÷ 20 = 15 bolts. Tightening to a 4×4-ft pattern (16 sq ft/bolt) for this zone only: 300 ÷ 16 ≈ 18.75, round up to 19 bolts — 4 additional bolts over the original count. Roof screen is added over the same 300 sq ft; at a standard 4-ft × 150-ft roll (600 sq ft/roll), that's half a roll. Added installation time: roughly 4 bolts × ~4 min/bolt ≈ 16 min plus ~20 min to hang screen ≈ 36 min added to the cycle, against a foreman/engineer callout that typically resolves within a shift.

**Deviation note filed (as written to the foreman/engineer):**

> Entry 3, 15–30 ft inby last row: bar-sounded drummy across full width. SEPT pull test at 25 ft: 36,000 lbf tension at 24-in encapsulation = 9 tons/ft anchorage, below the 12–24 tons/ft accepted range and below this horizon's typical 10–15 tons/ft — passes the 32,000 lbf (16-ton) minimum tension floor but does not match the plan's CMRR-58 assumption for this heading. Holding advance at 30 ft pending engineer review. Recommend: tighten pattern to 4×4 ft and hang screen for the 15-ft affected stretch (19 bolts vs. 15 at standard pattern, +4; half roll of screen). Standard 5×4-ft pattern and 20-ft extended cut resume once a pull test in unaffected rock confirms anchorage back in the 12+ tons/ft range.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled CMRR-to-pattern tables, SEPT/pull-test math, resin gel/spin selection by temperature, ATRS cycle sequencing, and the methane action-level checklist.
- [references/red-flags.md](references/red-flags.md) — smell tests: what a threshold breach usually means, the first question to ask, the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- 30 CFR Part 75, Subpart C (Roof Support) — §75.220 (roof control plan approval), §75.222(b)(1)-(3) (bolt spacing ≤5-ft centers, minimum tension at 50% of yield or anchorage capacity whichever is less, combination support for openings >20 ft wide), §75.203/§75.209 (Automated Temporary Roof Support setback ≤5 ft between ATRS and last permanent support row), §75.323 (methane action levels), §75.503 (permissibility of electrical equipment). eCFR.
- Mark, C., Compton, C.S., Oyler, D.C., Dolinar, D.R. — "Anchorage Pull Testing for Fully Grouted Roof Bolts," NIOSH/CDC — anchorage capacity of 12–24 tons/ft of resin encapsulation as the accepted "good" range, typical coal-horizon results of 10–15 tons/ft, fully grouted bolts as >80% of primary roof support in US coal mines, and the Short Encapsulation Pull Test (SEPT) method.
- Mark, C. & Molinda, G.M. — "The Coal Mine Roof Rating (CMRR): A Practical Rock Mass Classification for Coal Mines," USBM/NIOSH — CMRR as the basis for bolt-length and pattern design tied to mapped roof structure thickness.
- MSHA Final Rule, "Lowering Miners' Exposure to Respirable Crystalline Silica and Improving Respiratory Protection" (2024) — 50 µg/m³ 8-hour TWA permissible exposure limit, 25 µg/m³ action level; roof bolting drilling identified as a high respirable-dust-generating task.
- MSHA "Roof Control Plan Approval and Review Procedures" Handbook (PH20-V-2).
- Resin cartridge manufacturer installation/spec sheets (e.g., Minova, Jennmar J-LOK, DSI/Sandvik Fasloc) — fast-set gel time in the 8–15 second range, slow-set in the 30–90 second range, spin time required to stay under gel time; exact figures vary by product line and must be read off that cartridge's data sheet, not assumed.
- No direct roof-bolter practitioner has reviewed this file yet — flag corrections or gaps via PR. Bolt-yield, tension, and pattern-math figures in the worked example are illustrative of common product specs and plan structures; verify against the actual bolt, resin, and approved roof control plan on any real job.
