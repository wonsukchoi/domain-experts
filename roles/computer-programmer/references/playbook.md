# Computer Programmer — playbook

## Spec-clarification memo (filled template)

Send as a single batched message, section-numbered, before writing code against the ambiguous section.

> **Re: Spec v1.3, section 4.2 — loyalty discount threshold**
> Three items need confirmation before implementation:
>
> 1. **4.2 (discount threshold basis):** For a multi-item order with a same-day partial return, is the $50 threshold checked against pre-return or post-return subtotal? Given examples are all single-item, no-return.
> 2. **4.5 (rounding):** Discount is stated as "10% off, rounded to the nearest cent" — for a $47.005 edge case, round-half-up or banker's rounding? Not stated.
> 3. **4.7 (currency):** Spec examples are all USD. Does the discount apply pre- or post-currency-conversion for non-USD orders, or is 4.2 USD-only until a future spec revision?
>
> Blocking implementation on #1 only; will implement #2 as round-half-up and #3 as USD-only pending confirmation, flagged in code comments, unless corrected by EOD Thursday.

## Clause-to-test traceability table (filled example)

| Spec clause | Stated example? | Test case | Result | Notes |
|---|---|---|---|---|
| 4.2 threshold, single item | Yes ($65 → $58.50) | `test_single_item_over_threshold` | Pass | Matches spec example exactly |
| 4.2 threshold, post-return | No — clarified | `test_single_item_return_drops_below_threshold` | Pass | Clarification response, 2026-03-04 |
| 4.2 threshold, multi-item | No — inferred additive | `test_multi_item_over_threshold` | Pass | Additive subtotal confirmed in clarification #1 reply |
| 4.5 rounding | Partial (rule stated, no edge case) | `test_rounding_half_cent` | Pass | Assumed round-half-up per memo; flagged pending |
| 4.7 currency | No | *(not implemented — scoped out)* | N/A | USD-only per memo assumption |

Clause coverage reported as **4/5 implemented, 1 explicitly scoped out** — never silently omitted.

## Characterization-test sequence (legacy modernization, no spec available)

1. Run the existing routine against 20-50 real historical inputs pulled from production logs; record actual outputs verbatim — these become the initial test suite, regardless of whether the behavior looks correct.
2. Flag outputs that look wrong to a domain reviewer (not fixed yet) — get written confirmation on which are intentional quirks vs. bugs before changing anything.
3. Only after the characterization suite is green and reviewed: make the confirmed-bug fix, updating only the tests tied to that specific confirmed case.
4. Re-run the full characterization suite — every other locked-in behavior must still match, or the "unrelated" change touched more than intended.

## Assumption log (carried in every deliverable, not just the memo)

```
ASSUMPTIONS (as of commit a3f9c21):
- 4.5 rounding: round-half-up (industry default absent a stated method) — PENDING confirmation
- 4.7 currency: USD-only, non-USD orders raise NotImplementedError — SCOPED OUT per memo 2026-03-02
RESOLVED THIS COMMIT:
- 4.2 threshold basis: post-return subtotal, confirmed 2026-03-04 (see clarification reply)
```
