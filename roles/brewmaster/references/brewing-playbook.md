# Brewing Playbook

Filled worked procedures for the four processes this role executes most often: a batch-release QC checklist, a diacetyl (VDK) rest decision, a yeast pitch-rate calculation from cropped slurry, and a contamination trace with recall scoping. Populate with the actual batch's numbers; the structure, thresholds, and arithmetic below are real and reconcile.

## Batch-release QC checklist

Run every parameter against the batch's own style/label thresholds — never a generic chart — before authorizing packaging.

| Parameter | Method | Threshold (style/label-specific) | Reading | Pass/Hold |
|---|---|---|---|---|
| Mash pH | Room-temp probe | 5.2–5.6 | 5.34 | Pass |
| Final gravity | Hydrometer/refractometer | 1.010–1.014 (recipe range) | 1.012 | Pass |
| ABV vs. label | Calc: (OG−FG)×131.25 | Within ±0.3% of label claim | (1.062−1.012)×131.25 = 6.56%; label 6.5%, Δ0.06% | Pass |
| VDK (diacetyl) | Gas chromatography | Ale: 0.10–0.40 ppm (house target ≤0.20 for hop-forward styles, so diacetyl isn't masked by hop aroma); Lager: <0.05 ppm | 0.18 ppm | Pass |
| Dissolved oxygen, packaging | DO meter, in-line | ≤50 ppb target; >100 ppb hard reject | 38 ppb | Pass |
| Spoilage organisms | Membrane filtration, ASBC method | 0 CFU/50 mL (zero tolerance) | 0 CFU/50 mL | Pass |
| Bitterness (IBU) | Spectrophotometric | Recipe target ±5 IBU | 63 (target 65±5) | Pass |

**Deliverable — release memo, as filed (Batch I-1102, American IPA):**

> All six release parameters clear house/label/regulatory thresholds. ABV 6.56% calculated vs. 6.5% label claim, within ±0.3% TTB tolerance. VDK 0.18 ppm, under the 0.20 ppm house target for hop-forward ales. Zero spoilage-organism CFU. **Released to packaging.**

**Hold trigger:** any single row failing its own threshold holds the whole batch — a passing ABV and a passing VDK do not offset a spoilage-organism positive. Route to the relevant corrective procedure below (VDK rest, or contamination trace) rather than re-averaging or re-testing hoping for a different number.

## Diacetyl (VDK) rest decision

**Style thresholds (release gate, GC method):** Lager <0.05 ppm · Ale 0.10–0.40 ppm depending on sub-style (British ales tolerate the top of that band; clean American ales should target ≤0.20 ppm).

1. **Pull VDK sample near terminal gravity, day 8–10**, not earlier — diacetyl is a fermentation-tail byproduct and an early reading understates it.
2. **Compare to the threshold for this batch's actual style** — confirm on the batch sheet, not from memory or a general chart.
3. **If the reading clears the threshold, proceed to cold crash on schedule.**
4. **If the reading exceeds the threshold, hold and execute a diacetyl rest:** ramp from fermentation temperature to 15–18°C over 4 hours, hold 48–72 hours. Yeast reabsorb diacetyl only while warm and active — do not cold-crash first and rest after.
5. **Retest via GC at the same method after the rest.** If clear, release to cold crash.
6. **If still above threshold after the first rest, extend in 24-hour increments up to 96 hours total.** Beyond 96 hours without clearing, escalate to the QC lead — the cause is likely upstream (low pitch rate, premature racking off yeast, underattenuated gravity) and a longer rest at the same temperature won't fix a root cause outside the tank.

**Worked example.** Pilsner batch P-0622, day-9 VDK reads 0.11 ppm against the lager threshold of <0.05 ppm — roughly 2.2x over. Execute rest: ramp 9°C → 16°C over 4 hours, hold 60 hours. Retest: 0.04 ppm, clears. Packaging slips 2.5 days against the printed schedule.

**Deliverable — QC hold note, as filed:**

> Batch P-0622 (Pilsner): Day-9 VDK 0.11 ppm exceeded lager threshold (<0.05 ppm). Diacetyl rest executed 9°C→16°C, held 60h. Retest: VDK 0.04 ppm, GC method, cleared for cold crash. Packaging rescheduled +2.5 days. No further hold required.

## Yeast pitch-rate calculation (cropped slurry)

**Formula:** cells needed = target pitch rate (million cells/mL/°Plato) × batch volume (mL) × wort gravity (°Plato).

**Worked example — 30 hL lager, wort at 12.5°P, target 1.5 million cells/mL/°Plato (fresh-culture pitches can use half this rate):**

- Volume: 30 hL = 3,000 L = 3,000,000 mL.
- Cells needed = 1,500,000 × 3,000,000 × 12.5 = **5.625 × 10¹³ cells (56.25 trillion / 56,250 billion).**

**Step — convert to slurry volume from the house yeast bank.** Measure viable density via hemacytometer + methylene blue: bank reads 1.0 × 10⁹ cells/mL, 88% viability.
- Viable cells/mL = 1.0 × 10⁹ × 0.88 = **8.8 × 10⁸ cells/mL viable.**
- Slurry volume required = cells needed ÷ viable cells/mL = 5.625 × 10¹³ ÷ 8.8 × 10⁸ = **63,920 mL ≈ 63.9 L.**

**Step — check against slurry on hand.** 40 L available → shortfall of 23.9 L. Do not stretch the pitch by using the 40 L alone (underpitching stresses the fermentation and is a known upstream driver of the VDK failures caught in the rest above); either crop additional slurry from a healthy active fermentation or step up a fresh propagation batch to cover the shortfall.

**Repitch/viability decision rule:**
- Viability ≥90%: repitch at calculated volume, log generation count.
- Viability 70–89%: repitch, but increase pitch volume proportionally to compensate for the dead fraction, and flag for closer monitoring next generation.
- Viability <70%: do not repitch — order or step up a fresh lab-propagated culture instead (target pitch rate can be halved for a fresh culture per the house heuristic).
- **House generation cap: 10.** Regardless of viability, retire a strain at generation 10 and pitch fresh — genetic drift and accumulated contamination risk in repeatedly-cropped slurry outweigh the cost of a new culture.

**Deliverable — pitch worksheet, as filed:**

> Batch L-1130 (30 hL lager, 12.5°P): target 1.5M cells/mL/°P → 5.625×10¹³ cells required. Bank slurry: 1.0×10⁹ cells/mL, 88% viable → 63.9 L slurry needed; 40 L on hand, 23.9 L shortfall. Action: step up 24 L propagation batch (generation 6 of 10) to cover shortfall before pitch date.

## Contamination trace & recall scoping

1. **Identify the symptom precisely** — sensory descriptor, panel score, or a positive lab test — not "tastes off."
2. **Pull the batch/lot record**: tank ID, transfer line, packaging date, associated raw-material lots.
3. **Test retained samples from every batch sharing the same equipment/path in the surrounding window** (same transfer line, same tank, same changeover), not only the flagged batch.
4. **Build a timeline of shared touchpoints and find the point of introduction** — the earliest batch in the shared-equipment window that tests positive.
5. **Scope the recall to dated lots downstream of that point of introduction only** — batches that used the same equipment before the point of introduction, confirmed clean by retest, are excluded.
6. **Correct the root cause at the identified equipment**, then update the HACCP plan or cleaning SOP so the same failure path doesn't recur.
7. **Document and file**: symptom, retest results by batch, identified root cause, recall scope, corrective action.

**Worked example.** Distributor complaint on Batch K-0745 (American Pale Ale, packaged July 5–7): "band-aid, medicinal" off-flavor. Retained-sample membrane filtration: **40 CFU/50 mL *Lactobacillus brevis*** — positive against the 0 CFU/50 mL zero-tolerance threshold.

Trace: K-0745 transferred via Line B, Tank 4, July 3. Other batches on Line B in the surrounding window: K-0743 (July 1, Tank 2), K-0744 (July 2, Tank 3), K-0746 (July 4, Tank 5).

Retest all four retained samples:

| Batch | Transfer date | Line B result |
|---|---|---|
| K-0743 | Jul 1 | 0 CFU/50 mL — clean |
| K-0744 | Jul 2 | 0 CFU/50 mL — clean |
| K-0745 | Jul 3 | 40 CFU/50 mL — positive |
| K-0746 | Jul 4 | 15 CFU/50 mL — positive |

**Point of introduction:** between the July 2 (clean) and July 3 (positive) transfers — Line B became contaminated in that window. Inspection finds a cracked tri-clamp gasket on Line B harboring biofilm.

**Deliverable — recall scoping memo, as filed:**

> Root cause: cracked gasket, Line B tri-clamp fitting, biofilm-positive for *L. brevis*. Point of introduction: between Jul-2 and Jul-3 transfers. **Recall scope: K-0745 and K-0746 only** (packaged Jul 5–7, 3 states, retained-sample positive) — K-0743 and K-0744 confirmed clean by retest and excluded. Corrective action: gasket replaced; Line B added to weekly biofilm swab schedule; pre-packaging CIP-verification swab added as a new HACCP checkpoint effective next changeover.
