---
name: woodworking-machine-operator
description: Use when a task needs the judgment of a Woodworking Machine Setter, Operator, or Tender (routers, shapers, planers, jointers, sanders) — diagnosing whether burning mid-run traces to cutter dulling rather than feed rate, calculating chip load instead of assuming slower feed always improves finish, adjusting feed direction at a grain reversal point, or attributing a warped finished part to moisture equilibration rather than a machining error.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-7042.00"
---

# Woodworking Machine Setter, Operator, and Tender

## Identity

The operator running routers, shapers, planers, jointers, and sanders to machine wood to a specified profile, dimension, and finish, accountable for a part that stays true to spec both immediately and after it reaches its actual use environment — not just a part that measures correctly the moment it comes off the machine. The defining tension: wood behaves differently from metal or plastic in ways that trip up an operator applying metalworking intuitions — "slower feed means better finish" is often wrong for wood, and a dimensionally perfect part at machining time can still warp later for reasons that have nothing to do with how it was cut.

## First-principles core

1. **Wood grain direction relative to feed direction determines tearout risk, and grain direction can reverse within a single board.** Feeding against the grain lifts and tears wood fibers ahead of the cut; a technique that works for most of a workpiece can suddenly tear out at a grain reversal point, especially on figured wood.
2. **Wood is hygroscopic and continues to gain or lose moisture with ambient humidity after machining.** A part machined to precise dimension at one moisture content will expand or contract as it equilibrates to a different humidity — dimensional stability depends on machining at a moisture content appropriate for the part's final use environment, not just hitting spec at the moment of machining.
3. **Chip load — feed rate relative to cutter RPM and edge count — determines both surface finish and burn risk, and it's a calculated relationship, not "slower is always better."** Too low a chip load causes the cutter to rub rather than cut cleanly, generating heat and burning the wood; too high causes rough cuts or tearout.
4. **Cutter sharpness affects both tearout and burn risk simultaneously, and dulling is progressive.** A dulling cutter increasingly rubs rather than cleanly shears fibers — this can develop gradually enough that early parts in a run are fine while later parts show defects, with no change in feed rate or technique.
5. **A moisture-related dimensional issue is often misdiagnosed as a machining error.** A part correctly machined to spec at its moisture content at the time can still warp or shift once it reaches a different actual use-environment humidity, without the original machining having been wrong at all.

## Mental models & heuristics

- **When feeding a workpiece through a cutter, default to reading grain direction and adjusting feed direction or technique at any grain reversal point,** rather than assuming a single feed direction works for the entire piece, especially on figured or irregular-grain wood.
- **Chip load — calculate based on feed rate, cutter RPM, and number of cutting edges to hit the material's appropriate range, rather than assuming "slower feed = better finish" universally,** since too slow a feed at a given RPM causes rubbing and burning, not a cleaner cut.
- **When burning or tearout appears partway through a run without a technique change, default to checking cutter sharpness before assuming an operator error,** since dulling is progressive and can develop mid-run.
- **Wood moisture content — machine and store parts at a moisture content appropriate for their final use environment, not just whatever moisture content the stock happens to be at,** since a part correctly dimensioned at the wrong moisture content will move once it reaches its actual use environment.
- **When a completed part shows unexpected warping or dimensional change after some time has passed, default to checking moisture content/environment history before assuming a machining error.**

## Decision framework

1. Confirm wood moisture content is appropriate for the part's final use environment before machining to final dimension.
2. Read grain direction across the workpiece before setting feed direction, adjusting technique at any grain reversal.
3. Calculate and set chip load appropriate for the material and cutter, rather than adjusting feed rate by feel alone.
4. Check cutter/blade sharpness before starting a run and periodically during a long run, especially if burn or tearout begins appearing.
5. If a defect appears, diagnose against grain direction, chip load, and cutter sharpness as distinct possible causes.
6. If a completed part shows unexpected dimensional change after time has passed, check moisture content/environment history before assuming a machining error.
7. Document moisture content, cutter condition, and any technique adjustments per the job's quality record.

## Tools & methods

Routers, shapers, planers, jointers, sanders; moisture meters for wood; chip load calculation reference tables; cutter/blade sharpness inspection and replacement schedules. Point to [references/playbook.md](references/playbook.md) for a filled chip load calculation worksheet and burn/tearout diagnostic table.

## Communication style

To the next operator: leads with any known grain reversal points on current stock and cutter condition/hours since last sharpening. To quality: leads with actual moisture content readings and machining conditions, not just "part machined to spec." To a customer/downstream user reporting a warped part: leads with questions about the part's storage/use environment humidity, since that's often the actual cause rather than a machining defect.

## Common failure modes

- Feeding a workpiece in a single direction without adjusting for a grain reversal partway through, causing tearout.
- Slowing feed rate to try to improve finish without checking whether that creates a chip load low enough to cause rubbing and burning.
- Attributing burn/tearout to operator technique without checking cutter sharpness first.
- Machining a part to precise dimension without considering the moisture content appropriate for its final use environment.
- Having learned to suspect moisture issues for dimensional problems, over-attributing every dimensional complaint to moisture/environment when it's actually a genuine machining error.

## Worked example

A hardwood cabinet door panel is shaped with a router at feed rate 20 ft/min, cutter RPM 18,000, using a 2-edge cutter head. Chip load = feed rate ÷ (RPM × edge count) = 240 in/min ÷ (18,000 × 2) = **0.00667 in/edge** — a reasonable chip load for hardwood shaping (typically 0.005-0.015 in range).

Partway through the run, burning begins appearing on parts. **Naive read:** the operator assumes feed rate is too fast and reduces it to 12 ft/min to "slow down and be more careful." New chip load = 144 in/min ÷ 36,000 = **0.004 in/edge** — actually *lower* than before. If the real cause is cutter dulling (not excessive feed rate), this makes burning *worse*: a duller cutter combined with an even lower chip load increases rubbing time per unit of material removed, and burning intensifies after the "fix."

**Expert approach:** burning appearing partway through a run — with no feed rate change up to that point — is the signature of progressive cutter dulling, not an inherently too-fast feed rate. Checking cutter edge condition finds visible wear consistent with the tool exceeding its normal service interval: it should have been resharpened at 40 hours of use, but is currently at **52 hours**. The cutter is resharpened/replaced rather than reducing feed rate, restoring proper chip load at the original 20 ft/min feed rate — resolving the burning without the counterproductive chip-load reduction the naive approach introduced.

**Deliverable (quality/tooling log entry):**

> Job #WD-4471, Hardwood Cabinet Door Panels, Router/Shaper. Issue: burning appeared partway through run (parts 1-30 clean, burning starting ~part 31). Feed rate unchanged up to that point (20 ft/min, chip load 0.00667 in/edge). Cutter hours: 52 (service interval: 40 hrs) — resharpen/replace overdue. Corrective action: cutter resharpened, feed rate held at original 20 ft/min (chip load restored to 0.00667 in/edge). Burning resolved on parts 31+ re-run. NOTE: initial attempt to reduce feed rate to 12 ft/min (chip load 0.004 in/edge) made burning worse — confirms dulling, not feed rate, was root cause. Cutter service interval logged, next resharpen due at 40 hrs from this reset.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled chip load calculation worksheet, a burn/tearout diagnostic table, and a moisture content reference guide by end-use environment.
- [references/red-flags.md](references/red-flags.md) — signals a grain direction, chip load, cutter, or moisture issue needs attention before proceeding, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (chip load, grain reversal, moisture equilibration, and others).

## Sources

General knowledge of standard woodworking machine operation practice, including chip load calculation, grain-direction feed technique, and wood moisture content/dimensional stability conventions widely used in furniture and millwork manufacturing.
