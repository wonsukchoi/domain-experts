# Bioinformatics QC Playbook

## Assay QC threshold table (filled example — validate against your own lab's assay validation before use)

| Assay | Mean coverage | % bases >=20x | FREEMIX (contamination) | Ti/Tv | Duplication rate |
|---|---|---|---|---|---|
| Whole exome (clinical) | >=100x | >=90% | <0.03 | 2.0-2.1 | <15% |
| Whole genome (clinical) | >=30x | >=95% at 10x | <0.03 | 2.0-2.1 | <10% |
| Targeted panel (e.g. 50-gene oncology) | >=500x | >=98% at 250x | <0.05 | n/a (too few variants) | <10% |
| RNA-seq (research) | >=20M mapped reads | n/a | n/a | n/a | <30% (protocol-dependent) |

## Run-triage decision sequence

1. **Run-level gate first.** Cluster PF% >=80, Q30 >=80%, index-hopping <2%. Fail here blocks all downstream per-sample QC — fix or re-run the whole lane before evaluating individual samples.
2. **Per-sample gate.** Pull the full metric set (coverage, uniformity, FREEMIX, Ti/Tv, duplication, insert size) for every sample in the run in one table — never eyeball one sample at a time; shared patterns only show up in the full table.
3. **Classify any failure by signature**, using the table below, before deciding a fix.
4. **Cross-check isolated vs. shared.** Group failing samples by index pool, capture-kit lot, library-prep batch, and flow-cell lane. Two or more failing samples sharing any one of these is a shared-cause signal — investigate that shared factor before re-running samples individually.
5. **Disposition.** Pick one, in this fallback order of preference (cheapest-to-confirm first):
   - Pass as-is (metrics within spec).
   - Pass with documented caveat, research-use-only samples only — never for clinical release.
   - Re-run bioinformatics only (re-align/re-call with corrected parameters) if the raw reads are sound.
   - Re-run sequencing only (re-pool, re-sequence existing library) if reads are insufficient but the library is intact.
   - Re-run from library prep if the library itself is implicated (e.g. shared capture-kit-lot signature).
   - Reject and escalate to lab director / file a deviation report if root cause is unresolved or spec-defining (e.g. reagent lot, instrument fault).
6. **Log disposition and root cause in the LIMS record before variant interpretation begins.**

## Failure-signature table (filled example)

| Signature | Coverage mean | Uniformity (%>=20x) | FREEMIX | Ti/Tv | Likely cause |
|---|---|---|---|---|---|
| Loading-concentration too low | Low | Low (moves with mean) | Normal | Normal | Library under-loaded on flow cell — re-quantify and re-load |
| Capture/probe inefficiency | Normal or borderline | Low despite normal mean | Normal | Normal | Capture-kit lot or hybridization issue — check shared lot across failing samples |
| Cross-sample contamination | Normal | Normal | High (>0.03-0.05) | Often skewed toward 1:1 het ratio | Index hopping, sample mixup, or reagent carryover |
| Calling/filter artifact | Normal | Normal | Normal | Outside 2.0-2.1 | Wrong reference build, caller misconfiguration, or version mismatch — check pipeline version log first |
| PCR over-amplification | Normal | Normal | Normal | Normal | High duplication rate — check library-prep cycle count vs. protocol |

## Sample QC report — filled excerpt

```
Sample ID: EXOME24-013
Assay: Clinical whole exome, DRAGEN 4.2, GRCh38
Mean target coverage: 111x (threshold >=100x) — PASS
% bases >=20x: 79% (threshold >=90%) — FAIL
FREEMIX: 0.009 (threshold <0.03) — PASS
Ti/Tv: 2.05 (threshold 2.0-2.1) — PASS
Duplication rate: 8.2% (threshold <15%) — PASS
Disposition: HOLD — uniformity failure, shared with samples 07 and 21 (capture lot #4471).
Recommended action: re-prep with lot #4488, re-sequence.
QC reviewed by: [technician], [date]. Escalated to: [lab director], deviation report DR-2026-041 filed.
```
