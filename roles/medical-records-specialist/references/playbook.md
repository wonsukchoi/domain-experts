# HIM Playbook

Filled workflows with real thresholds. Defaults, not laws — deviate consciously and document why.

## 1. Release of information (ROI) — minimum necessary workflow

**Step 1 — verify the requester and the authorization.** A valid HIPAA authorization (45 CFR §164.508) needs all six elements or the request is deficient and gets returned, not processed:

| Element | Missing → |
|---|---|
| Specific description of information | Return — cannot scope minimum necessary without it |
| Who may disclose | Return |
| Who may receive | Return |
| Purpose of disclosure | Return unless requester is the patient |
| Expiration date or event | Return |
| Patient/representative signature + date | Return |

**Step 2 — apply minimum necessary by requester type:**

| Requester | Default scope |
|---|---|
| Patient (their own designated record set) | Full requested record — minimum necessary does not apply to patient's own access |
| Treating provider, referral | Records relevant to the referral episode, not the full longitudinal chart |
| Payer, medical-necessity review | The specific encounter(s)/date range named in the request |
| Attorney/subpoena, no court order | Return unless accompanied by patient authorization or a qualified protective order |
| Court order or valid subpoena duces tecum | Scope exactly to the order's terms; log as a mandatory disclosure |
| Substance use disorder (SUD) records, any requester | Requires separate 42 CFR Part 2 consent — a general HIPAA authorization does not cover it |

**Step 3 — turnaround and fees.** HIPAA ceiling is 30 days (one 30-day extension with written notice); many states set a shorter floor — verify the state's statute before defaulting to 30. Patient-directed fees are capped at a reasonable, cost-based amount; do not apply a third-party per-page rate to a patient's own request.

**Step 4 — log the disclosure.** Non-routine disclosures (not treatment/payment/operations) go into the accounting-of-disclosures log: date, recipient, description, purpose. Routine TPO disclosures do not require logging.

**Escalation trigger:** any request touching mental health process notes, HIV status, or SUD treatment — route to HIM supervisor/privacy officer before release regardless of how complete the authorization looks; these categories carry additional state-law layers on top of HIPAA and Part 2.

## 2. Pre-bill coding and query workflow

**Chart completeness gate — do not start coding until:**
- [ ] H&P signed
- [ ] Discharge summary signed (or discharge note if summary pending >30 days per facility policy — escalate, don't code around a missing summary)
- [ ] All diagnostic/pathology reports filed

**Coding pass:**
1. Abstract principal diagnosis (UHDDS: condition established after study as chiefly responsible for admission).
2. Assign secondary diagnoses/CCs/MCCs only where documented; flag ambiguous or clinically-indicated-but-undocumented conditions for query instead of guessing.
3. Assign POA indicator per code: **Y** (present at admission), **N** (not present), **U** (documentation insufficient to determine — triggers its own query), **W** (clinically undetermined, physician unable to say).
4. Sequence per grouper logic; run pre-bill edits (NCCI/MUE bundling, LCD/NCD medical necessity).

**Query decision table:**

| Situation | Action |
|---|---|
| Diagnosis stated once early, never revisited by discharge | Query — cannot code as uncertain-at-discharge |
| Diagnosis stated by one provider, contradicted by another | Query the attending of record, not the consultant |
| Clinical indicators present, no diagnostic statement anywhere | Query — indicators are not a diagnosis |
| Diagnosis stated and consistent through discharge summary | Code as documented, no query needed |
| Query sent, no response by day 2 | Escalate to physician advisor/CDI liaison |
| Query sent, no response by bill-drop deadline | Code to the lower-specificity documented level; do not hold the bill indefinitely |

**Post-bill audit response:** pull the record as it stood at bill-drop, re-derive the code independently, and write the defense to the specific guideline section or NCCI edit that supports (or contradicts) the billed code. A defense that says "coder judgment" without a citation does not survive appeal.

## 3. Medicare claim denial — five-level appeal timeline

| Level | Filed with | Filing deadline | Decision deadline | Amount in controversy (2024, indexed annually) |
|---|---|---|---|---|
| 1. Redetermination | Medicare Administrative Contractor (MAC) | 120 days from denial | 60 days | None |
| 2. Reconsideration | Qualified Independent Contractor (QIC) | 180 days from redetermination | 60 days | None |
| 3. ALJ hearing | Office of Medicare Hearings and Appeals | 60 days from reconsideration | 90 days (frequently exceeded) | ≈$180 (indexed yearly — verify current threshold before filing) |
| 4. Departmental Appeals Board (Council) | HHS Departmental Appeals Board | 60 days from ALJ decision | 90 days | None |
| 5. Federal district court | U.S. District Court | 60 days from Council decision | N/A | ≈$1,840 (indexed yearly — verify current threshold) |

**RAC/payer additional documentation request (ADR):** 45-day response window from the date of the request letter, not the date it's opened. Missing the window converts to an automatic technical denial regardless of clinical merit — track every open ADR against this clock and escalate anything unaddressed by day 40. RAC look-back period is 3 years from the paid-claim date; extrapolation to a broader claim universe applies only above a documented error-rate threshold set by the specific RAC contract, not automatically.

**Building the appeal packet:** the denial reason code (e.g., medical necessity, DRG validation, coding error), the specific guideline/LCD/NCD/NCCI citation that supports the original code, and the portion of the record that documents it — never a general narrative restating the diagnosis without pointing at where it lives in the chart.
