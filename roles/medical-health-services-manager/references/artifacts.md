# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual staffing analysis, denial tracker, or quality-investment case — not for general reasoning (that's `SKILL.md`).

## Acuity-adjusted staffing worksheet

```
Unit: Med-Surg 4B                    Period: trailing 3 months

Census (avg daily patients): 32 (flat vs. prior period)
Acuity workload score (from patient classification system, e.g., points per patient by category):
  3 months ago: avg 2.4 points/patient
  Current: avg 2.83 points/patient (+18%)

Current staffing: 1 RN : 5 patients (night shift)
Effective workload per RN (census/ratio × acuity score):
  3 months ago: (32/5) × 2.4 = 15.4 points per RN-shift equivalent
  Current: (32/5) × 2.83 = 18.1 points per RN-shift equivalent (+18%, matching acuity rise)

Safety indicator cross-check:
  Fall rate: 2.1 -> 2.6 per 1,000 patient days
  Med-error near-misses: [trend]

Interpretation: flat census + rising acuity = staffing that was adequate 3 months ago is now
effectively understaffed for the current patient population, even without any ratio change.
Reducing the ratio further moves in the wrong direction relative to actual need.
```

## Denial root-cause tracker

```
Month: [date]              Total claims: 1,240          Denied: 87 (7.0% denial rate, up from 5.2%)

Denial category breakdown:
  Documentation insufficient: 31 (35.6%)
  Coding error: 18 (20.7%)
  Prior authorization missing/expired: 22 (25.3%)
  Eligibility/coverage issue: 11 (12.6%)
  Payer policy change: 5 (5.7%)

Root cause of the rate increase (vs. prior month at 5.2%):
  Documentation category rose from 12 to 31 denials -> investigate: new EHR template rolled out
  mid-month, missing a required field for [specific service line]

Action: fix EHR template field requirement, retrain affected department, re-measure in 30 days
before considering this a payer-behavior issue.
```

## Quality investment cost-avoidance case

```
Proposed initiative: [e.g., enhanced fall-prevention protocol], cost: $85,000/year

Avoided cost calculation:
  Current fall rate: 2.6/1,000 patient days
  Annual patient days: 11,680
  Expected falls/year at current rate: 30.4
  Average cost per fall with injury (published benchmark, verify current figures): $14,000
  Expected annual fall-related cost at current rate: 30.4 × $14,000 = $425,600

  Protocol's expected fall-rate reduction (from pilot data or published evidence): -35%
  Expected falls/year post-intervention: 19.8
  Expected annual cost post-intervention: 19.8 × $14,000 = $277,200

  Gross avoided cost: $425,600 - $277,200 = $148,400/year
  Net benefit after $85,000 program cost: $63,400/year

Frame to finance as: net positive ROI, not purely a quality/compliance expense.
```
