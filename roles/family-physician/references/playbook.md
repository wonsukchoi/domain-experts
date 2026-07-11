# Playbook

Operational sequences a family physician actually runs, filled with example structure and numbers — adapt, don't script verbatim.

## 1. The 20-minute established-patient visit

**Time budget (typical 20-minute slot):**

| Phase | Minutes | What happens |
|---|---|---|
| Chart review before entering room | 2 | Pending results, overdue care gaps, last visit's deferred items |
| Agenda elicitation | 2 | "What did you want to cover today, and is there anything else?" — asked before addressing item one |
| Primary complaint work-up | 8 | History, exam, assessment for the highest-priority item |
| Secondary items / care gaps | 5 | Whatever fits — explicitly name what doesn't |
| Documentation + orders + after-visit summary | 3 | Problem list update, orders placed, plan explained with teach-back |

**Rule:** if the agenda has 4+ items and none are dangerous, pick the one with the highest cost of delay, address it fully, and say out loud which items are deferred and to when — a vague "we'll get to that" is a dropped item, not a plan.

## 2. Chronic-disease follow-up structure (diabetes example)

Filled template for a T2DM follow-up visit:

```
REVIEW SINCE LAST VISIT
  A1c: 8.9% (was 8.1%, goal <7.5%)          [worsening — investigate why]
  eGFR: 41 (was 52, 12 months ago)           [-11/yr — exceeds KDIGO rapid-
                                               progression threshold of >5/yr]
  BP: 138/84 (goal <130/80 for CKD)          [above goal]
  Med adherence (patient-reported): "mostly" [flag — verify against pharmacy
                                               fill data, don't take at face value]

ROOT-CAUSE CHECK BEFORE INTENSIFYING THERAPY
  - Adherence gap? Cost barrier? New life stressor? Medication interaction?
  - Only intensify dose/add agent after ruling out a fixable non-pharmacologic
    cause — intensifying a dose to compensate for a $40 copay problem fixes
    nothing and adds side-effect risk.

RENAL-ADJUSTED MEDICATION REVIEW (trigger: any eGFR < 45)
  - Metformin: reduce dose at eGFR 30-45, stop below 30
  - SGLT2i: indicated for T2DM+CKD, contraindicated below eGFR 20
  - NSAIDs: flag and discontinue if present — nephrotoxic in CKG

REFERRAL DECISION
  - Rapid progression (>5 mL/min/1.73m²/yr) → nephrology, regardless of
    absolute eGFR value
  - Stable eGFR even if low (<30, no rapid decline) → still refer at CKD
    stage 4, but not urgently

TODAY'S ONE ACTIVE CHANGE
  - State the single medication change made this visit (not three at once)
    so next visit can attribute any effect to it specifically.

DEFERRED TO NEXT VISIT (named explicitly)
  - Retinal exam, foot exam — booked as nurse visit, not silently dropped.
```

## 3. Same-day (advanced-access) triage

When the day's schedule is full and a same-day call comes in, triage by this order, not by call order:

1. **Red-flag symptom present** (see `red-flags.md`) → work in today, no exception.
2. **Acute, self-limited-likely, but patient anxiety high** → same-day slot if available; otherwise nurse triage call with explicit return precautions.
3. **Medication refill / paperwork only** → routed to portal/nurse, not a visit slot.
4. **Non-urgent new concern that fits at next scheduled visit** → offer the next open slot, don't squeeze into an already-full day at the cost of today's booked patients.

**Panel-level math**: a panel of 1,800 patients generating ~3.5 visits/patient/year needs roughly 6,300 visit-slots/year; at 230 clinical days/year that's ~27 visits/day if the physician is the only capacity — which is why team-based triage (phase 1 above routed to nursing/portal) is what makes the math survivable, not personal working faster.

## 4. Referral note template (filled)

```
REFERRAL TO: Nephrology
REASON FOR REFERRAL (specific question, not "please evaluate"):
  Rapid eGFR decline (52→41, -11/yr, exceeds KDIGO rapid-progression
  threshold) in a T2DM patient — requesting evaluation for etiology beyond
  diabetic nephropathy and co-management of renal-protective therapy.
ALREADY DONE:
  - Metformin dose-adjusted for eGFR 41
  - Started empagliflozin (renoprotective indication, eGFR 41 > cutoff of 20)
  - BP goal reset to <130/80 per CKD guidance
  - Urine ACR and renal ultrasound ordered, results attached
WHAT I NEED FROM YOU:
  - Confirm/rule out non-diabetic etiology
  - Recommend target BP and agent adjustments if different from above
  - Preferred follow-up cadence for labs going forward
```

## 5. Deprescribing review (polypharmacy trigger: 10+ active meds)

For each medication, one line, forcing a decision:

```
Drug            Original indication      Still active?   Stopping rule met?   Action
Omeprazole      GERD, started 2019       Unclear          >8wk use w/o re-eval  Trial taper
Lorazepam       Insomnia, started 2017   Not documented   Age >65, fall risk    Taper, refer CBT-I
Metformin       T2DM                     Yes              eGFR 41 → dose-adj   Reduce dose
Atorvastatin    2° prevention post-MI    Yes               —                    Continue
```

**Rule:** any row without a documented "still active + no stopping rule met" gets a taper plan started this visit, not a renewal on autopilot — unless stopping risks destabilizing a controlled condition (e.g., an anticonvulsant with no recent seizure isn't stopped without a specialist input).
