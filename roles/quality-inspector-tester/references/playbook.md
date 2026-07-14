# Playbook

## AQL sampling plan reference table (illustrative — always use the applicable current Z1.4 table)

| Lot size range | Sample size code | Sample size (n) | AQL 1.0% Ac/Re (Major) | AQL 2.5% Ac/Re (Minor) | Critical Ac/Re |
|---|---|---|---|---|---|
| 501-1,200 | H | 80 | 2/3 | 5/6 | 0/1 |
| 1,201-3,200 | J | 125 | 3/4 | 7/8 | 0/1 |
| 3,201-10,000 | K | 200 | 5/6 | 10/11 | 0/1 |

**Rule:** Critical defect plans are always Ac=0/Re=1 (or a facility-specific equivalent zero-acceptance plan), applied independently of the major/minor result — a single critical defect rejects the lot on that characteristic regardless of the major/minor sample outcome.

## Critical-defect override decision table

| Scenario | Action |
|---|---|
| 0 critical, major/minor within Ac | Lot passes — normal release per authority level |
| 0 critical, major/minor exceeds Ac | Lot rejected on major/minor — standard rejection process |
| 1+ critical found, major/minor within Ac | Lot REJECTED/HELD on critical characteristic regardless of major/minor pass — escalate to engineering |
| 1+ critical found, major/minor also exceeds Ac | Lot REJECTED — critical finding takes priority for escalation urgency/handling |

**Follow-up for any critical finding:** flag remaining lot units for 100% inspection of that specific characteristic pending root-cause determination (isolated occurrence vs. systemic/tooling issue).

## Gauge R&R interpretation guide

| % of tolerance consumed by gauge R&R | Interpretation | Action |
|---|---|---|
| <10% | Measurement system generally acceptable | Trust readings for pass/fail decisions |
| 10-30% | Marginal — acceptable depending on application/risk | Use judgment; consider improvement for critical characteristics |
| >30% | Measurement system generally unacceptable for this tolerance | Don't trust individual borderline readings; improve measurement system or add margin/re-test protocol |

**Rule:** for any reading within the measurement system's known R&R uncertainty band around a specification limit, treat the pass/fail call as inconclusive rather than definitive — re-measure with a more capable method or apply the facility's defined borderline-result protocol rather than accepting the single reading at face value.

## Disposition authority matrix (illustrative — use facility's actual matrix)

| Disposition type | Required authority |
|---|---|
| Accept lot (sample within Ac, no critical findings) | Inspector |
| Reject lot (sample exceeds Re, no critical findings) | Inspector |
| Hold lot pending review (critical finding, or ambiguous result) | Inspector (hold authority) — but NOT final release |
| Release from hold / accept with deviation | Engineering / Quality Manager sign-off required |
| Customer waiver / use-as-is on a nonconforming characteristic | Quality Manager + customer approval (if contractually required) |
