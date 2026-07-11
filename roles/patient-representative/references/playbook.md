# Playbook

Filled operational tools a patient representative runs day to day. Adapt the numbers to your organization's actual policy — the structure and the decision logic are the reusable part.

## 1. Intake triage table (complaint vs. grievance vs. safety event)

Run this classification on every intake before anything else — it determines whether the CMS-audited written-response clock starts.

| Signal | Classification | Clock starts? | Who else gets looped in |
|---|---|---|---|
| Rude tone from a nurse, resolved by charge nurse before rep leaves the floor | Complaint | No | Unit manager (FYI only) |
| Long ED wait, patient satisfied after rep explains triage order | Complaint | No | None |
| Billing amount dispute requiring finance investigation | Grievance | Yes | Patient financial services |
| Discharge instructions never given, patient readmitted 4 days later | Grievance | Yes | Quality/risk management |
| Allegation of rough handling or verbal abuse by staff | Grievance (safety event) | Yes, plus safety-event clock | Risk management + nursing leadership same day |
| Wrong medication administered, caught before harm | Safety event | Yes | Risk management immediately, patient safety officer |
| Family disputes a DNR/advance directive was followed | Grievance (safety event) | Yes | Risk management + ethics consult |

**Rule of thumb:** if resolving it requires anyone not present at the original encounter, it's a grievance. If it involves quality of care, abuse, neglect, or patient safety, it's a grievance regardless of how quickly it seems to resolve.

## 2. Service-recovery call script (HEART sequence, filled example)

Scenario: patient's surgery was delayed 6 hours with no update given to the family.

```
HEAR — let the account finish uninterrupted.
  "I want to make sure I have this right — you were told 8am, and nobody
  updated your family until 2pm. Is that the full picture, or is there
  more I'm missing?"

EMPATHIZE — name the impact, not just the fact.
  "Six hours with no word about someone you love in surgery — that's a
  genuinely hard way to spend a day. I'm sorry that happened."

APOLOGIZE — for the organization's part, no blame assigned pre-investigation.
  "Our process is supposed to have someone update your family every two
  hours during a case like this. That didn't happen today, and that's on us,
  not on you for expecting it."

RESPOND — one concrete action with a date, inside your delegated authority.
  "Here's what I'm going to do: I'm flagging this with the OR charge nurse
  today so the two-hour update standard gets reinforced on this unit, and
  I'll call you personally by Thursday to tell you what changed."

THANK — close without minimizing.
  "Thank you for telling me directly instead of just leaving unhappy —
  this is exactly the kind of thing that needs to get fixed."
```

**Delegated-authority note:** this scenario needed no refund or credit, so it stayed inside the rep's own authority. If the family had asked for a parking or meal voucher, that's typically inside a $100–$250 service-recovery fund tier — approve on the spot. A request for a bill adjustment or discount goes to finance; never estimate a number you don't have authority to guarantee.

## 3. Grievance file — mandatory fields (filled example)

```
CASE #: GRV-2026-0417
DATE RECEIVED: [date], via phone
PATIENT: [name/MRN]          REPORTED BY: patient
CLASSIFICATION: Grievance (billing dispute, GFE variance)
DESCRIPTION: Patient received Good Faith Estimate of $850 for outpatient
  colonoscopy; actual bill was $4,200, a $3,350 variance exceeding the
  $400 PPDR eligibility threshold.
INVESTIGATION: Confirmed with patient financial services that pathology
  fees were billed separately and were not included in the original GFE.
ACTION TAKEN: PPDR dispute filed on patient's behalf same day; escalated
  to scheduling to review whether pathology should be itemized in future
  GFEs for this procedure.
RESOLUTION: Dispute filed [date]; billing team to contact patient within
  10 business days with next steps.
WRITTEN RESPONSE SENT: [date], 3 business days after receipt — within the
  hospital's 15-day billing-grievance SLA.
```

Every field above is what a CMS surveyor pulls first during a complaint-file audit — a case with a resolution but no dated written-response entry reads as unresolved regardless of what actually happened.

## 4. Escalation matrix (filled example, SLAs in business days)

| Issue type | Route to | Acknowledge patient | Resolve/respond |
|---|---|---|---|
| Billing/GFE variance | Patient financial services | 2 days | 15 days |
| Clinical quality-of-care concern | Risk management + unit medical director | 1 day | 30 days (may extend with written notice) |
| Allegation of abuse/neglect | Risk management + compliance, same-day | Same day | Per investigation, no standard cap |
| HIPAA disclosure concern | Privacy officer | 2 days | 10 days |
| Interpreter/language access gap | Language services manager | 3 days | 15 days |
| Facilities/environment (noise, food, cleanliness) | Facilities or nutrition services | 3 days | 10 days |

**Rule:** the acknowledgment SLA is the rep's own deadline regardless of who else is investigating — a patient hears from patient relations first, even if the substantive answer is still pending.

## 5. Good Faith Estimate / PPDR referral checklist

1. Confirm patient is self-pay or uninsured (PPDR applies to this population, not insured balance-billing disputes, which route through the insurer's appeal process instead).
2. Pull the original GFE date and amount, and the actual bill date and amount. Subtract.
3. If the variance is $400 or more, confirm days elapsed since the bill date against the 120-day window.
4. If inside the window, file the dispute referral to patient financial services same-day; log the case as a grievance.
5. If outside the window, document why the patient missed it (often: never told the right department existed) and route as service-recovery, since the formal remedy has lapsed but the underlying billing error may still warrant an internal adjustment review.
