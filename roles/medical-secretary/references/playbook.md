# Medical Secretary — Playbook

## Urgency-triage table (example practice policy)

| Reported symptom/request | Slot type | Action |
|---|---|---|
| Chest pain, difficulty breathing | Emergency — do not schedule | Direct to ED / 911, notify on-call clinician immediately |
| Fever >101°F in immunocompromised patient | Same-day buffer slot | Book same-day, flag chart for clinician review before visit |
| New/worsening neuro symptoms (numbness, weakness) | Same-day or next-available buffer slot | Book within 24 hours, note onset date in chart |
| Medication refill, no new symptoms | Routine — next available | Standard scheduling queue |
| Annual wellness visit | Routine — patient preference | Standard scheduling queue, no urgency flag |
| "Just don't feel right," no specific match to list | Routine, but confirm with triage nurse if patient insists | Do not self-escalate without a symptom matching the defined list |

## Prior-authorization deadline calculation

**Formula:** `submission deadline = appointment date − internal confirmation buffer − worst-case authorization cycle`

Worst-case authorization cycle = base insurer SLA + practice's historical response lag to an additional-info request + insurer's second-review time after receiving complete information.

| Insurer | Base SLA (business days) | Additional-info-request rate (this procedure, per practice log) | Worst-case cycle (business days) | Internal confirmation buffer |
|---|---|---|---|---|
| Insurer A (this practice's most common payer) | 5 | 40% (lumbar MRI) | 10 (5 + 2 + 3) | 2 business days before visit |
| Insurer B | 3 | 15% (routine imaging) | 5 (3 + 1 + 1) | 2 business days before visit |
| Insurer C | 7 | 60% (specialty procedures) | 14 (7 + 3 + 4) | 3 business days before visit |

**Rule:** if `(appointment date − order date) < worst-case cycle + buffer`, escalate to the ordering clinician immediately to either expedite documentation or reschedule — do not wait to see if the best case happens.

## HIPAA records-release checklist

1. Confirm requestor identity and authority (patient, patient's legal representative with documentation, or a facially valid subpoena/court order).
2. Read the authorization scope exactly as written — date range, specific record types, intended recipient.
3. Pull only the records matching that scope. Do not include unrelated encounters, other providers' notes, or psychotherapy notes unless specifically and separately authorized (psychotherapy notes require distinct authorization under HIPAA even when general records are authorized).
4. Log the release: date, recipient, scope, method of transmission.
5. If the request is ambiguous about scope, contact the requestor for clarification before releasing — do not default to "send everything to be safe."

## Eligibility re-verification schedule

| Booking lead time | Re-verification action |
|---|---|
| Booked <14 days out | Original verification at booking stands; no re-check needed unless patient reports a coverage change |
| Booked 14–30 days out | Re-verify 48–72 hours before the appointment |
| Booked >30 days out | Re-verify 48–72 hours before the appointment AND flag for a mid-point check if the visit is 60+ days out |

## Filled example: coding-mismatch escalation note

> **To:** Dr. [ordering clinician]
> **Re:** Scheduling flag — [patient], visit reason vs. order mismatch
> Order received states "follow-up, hypertension management" (ICD-10 I10 implied). Visit was requested by patient front-desk call as "annual physical." These map to different visit types under this payer's benefit structure (problem-focused visit vs. preventive visit), and preventive-visit copay/coverage differs from problem-focused. Confirming before scheduling: is this an annual wellness visit with an incidental hypertension check, or a hypertension follow-up visit? Will schedule accordingly once confirmed — holding the slot for 24 hours.
