# Statistical Assistant — Playbook

## Double-entry reconciliation log (filled example)

| Record ID | Field | Entry 1 | Entry 2 | Source doc value | Resolution |
|---|---|---|---|---|---|
| INT-0187 | Intake date | 06/07/2026 | 07/06/2026 | Source form reads "6/7/26" (clinic uses DD/MM) | Corrected to 2026-07-06; flagged as date-format discrepancy |
| INT-0203 | Referral source | "Self" | "Self-referral" | Source form checkbox: "Self" | Corrected to standardized code `SELF`; not a true discrepancy, a coding-convention gap |
| INT-0241 | Assessment score 2 | 14 | 41 | Source form: "14" | Corrected to 14; transposition error, Entry 2 clerk notified |
| INT-0309 | Enrollment date | 07/12/2026 | (blank) | Source form: "7/12/26" | Entry 2 missed the field; corrected, not a disagreement |

**Resolution rule:** every discrepancy is checked against the source document, never resolved by picking between the two entries without it. A blank in one entry and a value in the other is still logged as a discrepancy (a miss), not silently accepted.

## Range/consistency-check specification (filled example)

| Field | Check type | Rule | Action on flag |
|---|---|---|---|
| Date of birth | Range | Between 1900-01-01 and today | Hold record, verify against source |
| Assessment score 1-3 | Range | 0-40 (instrument's documented scale) | Hold record, verify against source |
| Enrollment date | Cross-field | Must be ≥ intake date | Hold record, verify both dates against source |
| Eligibility category | Valid-value list | Must match current codebook's 6 defined categories | Hold record; if a 7th value is legitimate, escalate to researcher for codebook update, don't just add it |
| Contact phone | Format | 10 digits, US format | Flag but don't hold — allow international/incomplete with a missing-data code |

**Threshold-review rule:** if a range check hasn't fired in the last 200 records of a high-volume batch, check whether the threshold is still appropriately tight for this data before assuming the field is simply clean.

## Codebook entry (filled example)

```
Variable:        intake_date
Label:           Date of intake assessment
Type:            Date (ISO 8601, YYYY-MM-DD in dataset; source forms use DD/MM/YYYY)
Valid range:      2024-01-01 through current date
Missing codes:    -99 = not recorded on source form
                  -98 = source form illegible
Collection dates: Batch 1-3, 2026-01-15 through 2026-07-06
Notes:            Source paper form uses DD/MM/YYYY (clinic convention). Entry
                  template lacked input mask through Batch 3 — see Batch 3 data
                  quality summary. Input mask added Batch 4 onward.
```

**Codebook-update trigger:** any new missing-data code, any accepted out-of-range value, or any field-definition clarification discovered during entry gets added to the codebook the same day, not batched for "later."

## Tabulation request (filled example)

Researcher's spec: "Cross-tab of eligibility category by referral source, unweighted counts, suppress any cell under 5."

| Referral source \ Eligibility | Category A | Category B | Category C |
|---|---|---|---|
| Self | 42 | 18 | 6 |
| Clinic referral | 61 | 34 | *[suppressed, n=3]* |
| Court-mandated | 12 | *[suppressed, n=4]* | 0 |

Deliverable note: "Two cells suppressed per your n<5 threshold (Clinic/Category C, n=3; Court-mandated/Category B, n=4). Court-mandated/Category C is a true zero, not suppressed." — the true-zero vs. suppressed-small-cell distinction is called out explicitly so the researcher doesn't misread a suppression as a zero.
