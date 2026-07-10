# QC Investigation & Statistics Playbook

Operational playbooks with concrete steps and thresholds. Defaults, not laws — deviate consciously and document why.

## 1. OOS/OOT investigation — Phase I / Phase II

### Phase I — laboratory investigation (open same day the result is confirmed)

1. **Confirm the result is real before investigating causes.** Re-check calculation, unit conversion, and dilution math from raw data — a transcription error is not a lab investigation, it's a correction with its own record.
2. **Pull the run-specific objective evidence**, not the analyst's memory of the run:
   - Instrument calibration/PM status current for the date of the run
   - System-suitability data for that specific sequence (resolution, tailing factor, %RSD of replicate injections — typical SOP limit ≤2.0% RSD for HPLC assay)
   - Reference standard/CRM lot, expiry, and current CoA
   - Reagent/mobile-phase prep date and any deviation from SOP
   - Raw data (chromatograms, weighments, photos) for the specific unit/vessel/replicate that failed
3. **Interview the analyst same-day** while memory is fresh — technique deviations (pipetting, dilution order, sample prep timing) are the most common assignable cause and the easiest to lose after 48 hours.
4. **Decide: assignable cause found, or not.** "Assignable" means objective evidence ties the failure to a specific, identifiable event (missing sinker, expired standard, instrument fault, documented technique error) — not "the analyst is inexperienced" or "this happens sometimes."
5. **Time box.** Typical SOP window for Phase I: initial assessment within 1 business day of result confirmation, full Phase I closure within 5 business days. Exceeding the window without escalating to Phase II is itself a finding in an audit.

### Phase II — full investigation (when Phase I finds no assignable lab cause)

1. Widen scope to the manufacturing record: batch record deviations, in-process control trends, raw-material CoAs, equipment logs, environmental monitoring for that batch.
2. Pull the last 10–20 lots' results for the same test/spec and control-chart them — is this an isolated point or the tail of a drift?
3. Cross-check other tests on the same batch — a real product failure usually correlates with something else (a blend uniformity flag, an environmental excursion), a lab-isolated anomaly usually doesn't.
4. Conclusion is one of: confirmed product failure (batch rejected/reworked per QA), or inconclusive with documented rationale for retest under a predefined retest protocol (never an open-ended "test again").
5. Retesting protocol, if invoked, must be written into the SOP *before* any OOS occurs — number of retests, who can authorize, and how results are combined are decided in advance, never improvised after seeing a bad number.

## 2. Multi-stage acceptance protocols — evaluate stage-by-stage, never blended

### USP <711> dissolution, example spec Q = 80%

| Stage | Units tested (cumulative) | Acceptance criterion |
|---|---|---|
| S1 | 6 | Each unit ≥ Q + 5% (85.0%) |
| S2 | 12 | Mean of 12 ≥ Q (80.0%); no unit < Q − 15% (65.0%) |
| S3 | 24 | Mean of 24 ≥ Q; no more than 2 units < Q − 15%; no unit < Q − 25% (55.0%) |

Rule: a stage failure sends you to the *next* stage's criterion applied to the *cumulative* unit count — it never resets to "average everything and see."

### ANSI/ASQ Z1.4 attribute sampling — example, Lot size 501–1200, General Inspection Level II

| AQL | Sample size code | n | Accept (Ac) | Reject (Re) |
|---|---|---|---|---|
| 1.0 | J | 80 | 2 | 3 |
| 1.5 | J | 80 | 3 | 4 |
| 2.5 | J | 80 | 5 | 6 |

Read as: pull `n` units; ≤`Ac` defects accepts the lot, ≥`Re` defects rejects it. The sample size is fixed by lot size and inspection level *before* sampling — pulling extra units after seeing early defects to "get more data" invalidates the plan's statistical guarantee.

## 3. Control chart rules (Western Electric / Nelson) — apply to any trended parameter

Zones relative to centerline (CL), in units of process sigma (σ):

- **Rule 1 — 1 point beyond 3σ** (Zone A exceeded): stop, investigate immediately — near-certain special cause.
- **Rule 2 — 2 of 3 consecutive points beyond 2σ, same side:** investigate — probable shift.
- **Rule 3 — 4 of 5 consecutive points beyond 1σ, same side:** investigate — possible shift.
- **Rule 4 — 7 (or 8, per Nelson) consecutive points on one side of centerline:** the process mean has likely shifted even though every point may be inside spec.
- **Rule 5 — 6 consecutive points steadily increasing or decreasing:** trend, not a step-shift — check for drift causes (reagent aging, calibration drift, seasonal raw-material variation).

None of these rules require a spec violation to trigger an investigation — that's the point of trending versus spec-checking.

## 4. Process capability — worked example

Ten most recent lots' potency assay results (%, spec 95.0–105.0%): 98.2, 99.1, 97.8, 100.3, 99.6, 98.9, 101.2, 99.4, 98.7, 99.9.

- Mean x̄ = (98.2+99.1+97.8+100.3+99.6+98.9+101.2+99.4+98.7+99.9)/10 = 993.1/10 = 99.31
- Sample std dev s = √(Σ(xᵢ−x̄)²/(n−1)) = √(9.089/9) ≈ 1.00
- Cpk = min[(USL − x̄)/3s, (x̄ − LSL)/3s] = min[(105.0−99.31)/3.00, (99.31−95.0)/3.00] = min[1.90, 1.44] = **1.44**

Cpk = 1.44 with n=10 reads "capable" on the formula, but at n=10 the confidence interval on Cpk is wide — do not report this as settled capability to a customer or in a validation report. State it as a preliminary estimate and flag the minimum subgroup count (commonly cited as ≥30, ideally ≥100 individual results across multiple lots) needed before treating Cpk as decision-grade.

## 5. Lot-disposition decision tree

1. Result within spec, no control-chart rule triggered → release, no further action.
2. Result within spec, control-chart rule triggered → release this lot (spec was met), but open a trend investigation before the next lot — don't wait for a spec failure to act on a signal you already have.
3. Result OOS/OOT → Phase I investigation (Section 1) before any retest.
4. Phase I finds assignable cause → invalidate per SOP, apply the pre-defined next-stage or retest protocol, document.
5. Phase I inconclusive → Phase II; outcome is confirmed failure (reject/rework via QA) or documented inconclusive-with-retest under a pre-existing protocol — never an ad hoc retest invented after the fact.
