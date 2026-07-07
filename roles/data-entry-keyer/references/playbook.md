# Data Entry Keyer — Playbook

## Batch quality-control audit (AQL-style, post-keying)

Applied after a batch is keyed, before release, using an acceptance-sampling table matched to batch size and required inspection level (ANSI/ASQ Z1.4-style; adjust Ac/Re to the organization's actual disclosure-risk policy — figures below are illustrative).

| Batch size (records) | Sample size | Accept (Ac) | Reject (Re) |
|---|---|---|---|
| 91–150 | 20 | 1 | 2 |
| 151–280 | 32 | 2 | 3 |
| 281–500 | 50 | 3 | 4 |
| 501–1,200 | 80 | 5 | 6 |
| 1,201–3,200 | 125 | 7 | 8 |

Procedure: pull the sample size at random from the completed batch, re-key each sampled record independently against source, count defects (any field disagreement). Defects ≤ Ac → batch accepted. Defects ≥ Re → batch fully re-verified, not just the sample. Between Ac and Re → escalate to supervisor for a judgment call, do not auto-accept or auto-reject.

**Filled example** — batch of 800 records, sample size 80, defects found: 4.
- Ac(5) for this sample size — 4 ≤ 5 → **accept**, release batch.
- If defects had been 7 (≥ Re(6)) → full re-verification required before release.

## Exception log (filled format)

| Record # | Field | Issue | Source reference | Resolution | Resolved by |
|---|---|---|---|---|---|
| 0347 | Date of loss | Ambiguous DD/MM order, handwritten "03/07/2026" | Form image p.2, box 14 | Cross-checked against policy effective-date range (01/01/2026–12/31/2026); both readings fall in range — genuinely ambiguous | Flagged for adjuster review |
| 0512 | Claim amount | Decimal point unclear, "1250.00" vs "12500.0" | Form image p.3, box 22 | Cross-checked against itemized-loss subtotal on p.4 = $1,250.00 | Resolved: $1,250.00 |
| 0688 | Policy number | 9th digit smudged, could be "3" or "8" | Form image p.1, box 3 | Looked up first 8 digits in policy system — only one active policy matches, 9th digit is "3" | Resolved: policy #402-119-3 |

Every row needs all six columns filled — a resolution without a source reference is a guess, not a resolution.

## Key-verification discrepancy reconciliation (filled example)

Batch: 800 records × 15 fields = 12,000 field-entries, two-key verified.

| Step | Value |
|---|---|
| Total discrepancies | 96 |
| Aggregate rate | 96/12,000 = 0.80% |
| Highest single-field discrepancy count | Date of loss: 58 |
| Field-level rate (highest field) | 58/800 = 7.25% |
| Ratio to aggregate rate | 7.25% / 0.80% = 9.1× |
| Trigger for root-cause investigation | Any field ≥ 3× the aggregate rate |

Rule of thumb used above: investigate any field whose individual rate is 3x or more the batch's aggregate rate — a field at or near the aggregate rate is not usually worth a separate investigation.

## Production-quota vs. accuracy check

Track exception-flag rate alongside keying speed per shift. A sudden drop in flag rate at the same time speed increases is the signature of suppressed flagging, not genuine improvement — investigate before crediting the speed gain.

| Shift | Keys/hour | Exception flags/100 records | Interpretation |
|---|---|---|---|
| Week 1 baseline | 8,200 | 3.1 | Normal |
| Week 2 | 8,400 | 3.0 | Normal — small, consistent change |
| Week 3 | 9,100 | 0.4 | **Investigate** — 11% speed gain with an 87% flag-rate drop is not plausible from skill improvement alone |
