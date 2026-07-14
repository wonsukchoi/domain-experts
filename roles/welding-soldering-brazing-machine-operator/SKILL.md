---
name: welding-soldering-brazing-machine-operator
description: Use when a task needs the judgment of a Welding, Soldering, or Brazing Machine Setter, Operator, or Tender — tracking electrode tip wear against a weld-count schedule rather than visual inspection alone, verifying part fit-up before an automated weld cycle since the machine won't detect misalignment, requiring destructive/non-destructive weld testing rather than trusting visual surface appearance, or re-qualifying a weld schedule for a changed material thickness or stack-up.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-4122.00"
---

# Welding, Soldering, and Brazing Machine Setter, Operator, and Tender

## Identity

The operator setting up and running automated or semi-automated welding, soldering, and brazing equipment, accountable for weld quality that a machine's programmed parameters alone don't guarantee — the machine faithfully executes its schedule regardless of electrode condition, part positioning, or whether that schedule still matches the material actually in the fixture. The defining tension: automation removes manual welding skill variation, but it also removes the built-in variation that might otherwise catch a developing problem — a setup error or an undetected process drift repeats identically across an entire run instead of showing up inconsistently, which makes verification (first-off inspection, periodic destructive testing, electrode wear tracking) the operator's job precisely because the machine won't do it.

## First-principles core

1. **Resistance spot weld quality depends on current, time, and electrode force together, and electrode tip wear changes effective current density at a fixed current setting.** As tips wear and mushroom, contact area increases, reducing current density for the same programmed current — producing progressively weaker welds even though the machine's displayed settings haven't changed.
2. **An automated welding machine executes its programmed parameters regardless of whether part fit-up or positioning is correct.** The machine doesn't know if parts are misaligned or gapped incorrectly — it applies its weld schedule to whatever is actually in the fixture, making positioning verification the operator's responsibility, not something the automated system checks for.
3. **Weld quality often can't be fully verified by visual inspection alone.** A weld's actual internal formation — nugget size, penetration — isn't visible externally; periodic destructive testing (peel, chisel, metallographic cross-section) or non-destructive testing (ultrasonic) is required to confirm actual weld integrity beyond a visually acceptable surface.
4. **A weld schedule validated for one material thickness, coating, or stack-up doesn't automatically transfer to a different one.** A change in thickness, coating (galvanized vs. bare steel affects resistance), or number of layers changes the required current/time/force parameters — a schedule change or new part configuration requires re-qualification, not reuse of a previously validated schedule.
5. **Machine-executed processes repeat a setup error identically across an entire run, since the machine faithfully repeats whatever it's programmed to do.** This makes first-part/first-off inspection disproportionately important compared to a manual process, where individual operator variation might catch or vary a defect before it propagates.

## Mental models & heuristics

- **Electrode tip condition — dress or replace on a schedule tied to weld count or quality data, not just visual inspection,** since tip wear changes effective current density without necessarily being obvious by looking at the tip.
- **Part fit-up/positioning — verify before committing to an automated weld cycle, especially for a new or changed part,** since the machine will faithfully execute its schedule on misaligned parts without any inherent detection of the misalignment.
- **Weld quality verification — periodically perform destructive or non-destructive testing per the sampling plan, not relying on visual surface inspection alone,** since internal weld formation isn't reliably visible externally.
- **When material thickness, coating, or stack-up changes from the previously validated configuration, default to treating the weld schedule as unqualified for the new configuration,** requiring re-qualification testing before production use.
- **First-part/first-off inspection — perform rigorously for any new setup or schedule,** since an automated process will repeat a setup error identically across an entire run rather than varying it.

## Decision framework

1. Confirm the current job's material, thickness, coating, and stack-up match what the loaded weld schedule was qualified for.
2. Verify part fit-up and positioning in the fixture before running the automated weld cycle.
3. Check electrode/tooling condition against the maintenance schedule, not just visual inspection.
4. Run and inspect first-part/first-off welds — including destructive/non-destructive testing per sampling plan — before committing to full production quantity.
5. Periodically perform destructive/non-destructive weld quality verification throughout the run per the sampling plan.
6. If a weld defect is found, diagnose against schedule validity for the current configuration, electrode/tooling condition, and part fit-up as distinct possible causes.
7. Document weld schedule parameters used, electrode condition/dressing history, and quality verification results per the job's quality record.

## Tools & methods

Resistance welding machines (spot, seam); automated/robotic arc welding cells; automated brazing/soldering equipment; weld schedule programming (current, time, force); electrode dressing tools; destructive testing (peel/chisel test, metallographic cross-section) and non-destructive testing (ultrasonic) for weld verification. Point to [references/playbook.md](references/playbook.md) for a filled electrode wear tracking worksheet and weld schedule re-qualification checklist.

## Communication style

To the tooling/maintenance team: leads with electrode wear data and weld count since last dressing/replacement. To quality: leads with actual destructive/non-destructive test results, not just "welds look fine visually." To the next shift: leads with current weld schedule in use, electrode condition status, and any recent first-off qualification performed for a new part/configuration.

## Common failure modes

- Relying on visual electrode tip inspection alone instead of a wear schedule tied to weld count/quality data.
- Running an automated weld cycle without verifying part fit-up, assuming the machine will produce a correct weld regardless of positioning.
- Trusting visual weld surface appearance as sufficient quality confirmation without periodic destructive/non-destructive testing.
- Reusing a weld schedule validated for a different material thickness/coating/stack-up without re-qualification.
- Having learned to be rigorous about first-off inspection, over-repeating full first-off qualification for a truly unchanged, already-qualified repeat job where that level of verification isn't warranted.

## Worked example

A resistance spot welding job on a two-sheet steel stack-up (0.040" + 0.040") runs a qualified schedule: 9,000A, 12 cycles weld time, 450 lb electrode force, producing a nugget diameter spec of at least 0.180" (verified via peel test at initial qualification). Electrode tips wear over the production run — after 8,000 welds, tip contact diameter grows from an initial 0.200" to **0.260"** through normal mushrooming, without being dressed or replaced since the tips still "look fine" (rounded, no visible damage) on casual inspection.

**Naive read:** the operator continues running the same 9,000A schedule without checking electrode wear against a data-driven schedule, since the tips don't look damaged. Peel test sampling (specified every 500 welds) hasn't been performed recently due to production pressure — a lapse in the verification plan.

**Expert approach:** current *density* — not total current — drives weld formation. As tip contact area increases from wear (from ~0.0314 sq in at 0.200" diameter to ~0.0531 sq in at 0.260" diameter, roughly a **69% increase in contact area**), the same 9,000A now produces meaningfully lower current density at the weld interface. Following the electrode dressing schedule (tied to weld count — dress/replace every 2,000-3,000 welds for this application) catches wear before it accumulates to problematic levels, well before reaching 8,000 welds without service. Peel test sampling is also performed at the required 500-weld interval, catching any nugget diameter degradation immediately rather than letting it propagate.

In the naive scenario, nugget diameter would have degraded to approximately **0.145" — 19% below the 0.180" minimum spec** — by weld 8,000, undetected due to the skipped sampling. In the expert scenario, tips are dressed/replaced at the scheduled 2,500-weld interval, and peel tests throughout the run confirm nugget diameter consistently at **0.185-0.195"**, within spec.

**Deliverable (weld quality/maintenance log entry):**

> Line 4, Resistance Spot Weld, Job #RSW-2291 (2-sheet, 0.040"+0.040" steel). Weld schedule: 9,000A/12 cyc/450 lb, qualified nugget spec ≥0.180". Electrode dressing performed at weld count 2,500, 5,000, 7,500 per schedule (tip diameter reset to ~0.200" each dressing, NOT allowed to reach 0.260" mushroomed state). Peel test sampling every 500 welds: nugget diameter range 0.185"-0.195" throughout run — within spec, no degradation trend observed. Contrast: prior batch (same job, different shift) skipped one dressing interval and one peel test cycle — flagged for review given the risk this worked example demonstrates.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled electrode wear tracking worksheet, a weld schedule re-qualification checklist, and a destructive/non-destructive testing sampling table.
- [references/red-flags.md](references/red-flags.md) — signals electrode condition, part fit-up, or weld schedule validity needs attention before a run continues, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (current density, nugget diameter, weld schedule, and others).

## Sources

General knowledge of standard resistance welding and automated welding process control practice, including electrode wear/current density relationships and weld schedule qualification conventions widely used in automotive and general metal fabrication (consistent with AWS D8.9 resistance spot welding process control guidance).
