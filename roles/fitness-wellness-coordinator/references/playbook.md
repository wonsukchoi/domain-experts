# Playbook: Screening Intake, Program Audit, and Incentive Design

Filled process for the four recurring executions of the role: participant screening and clearance, the HERO/CDC audit choice and walk-through, an incentive-design calculation against the HIPAA/ACA and ADA ceilings, and the emergency-response drill cycle. Adapt names and numbers to the facility in front of you; keep the sequence, the branch logic, and the thresholds.

## 1. New-Participant Screening Intake

Run this before assigning any intensity level, every time — no exceptions for "looks fit" or "has trained before elsewhere."

**Step 1 — PAR-Q+ (7 core questions, administered verbatim, no paraphrase):**

| # | Question | Any "yes" triggers |
|---|---|---|
| 1 | Has a doctor ever said you have a heart condition or high blood pressure? | Follow-up page 2 |
| 2 | Do you feel pain in your chest at rest, during daily activities, or during exercise? | Follow-up page 2 |
| 3 | Do you lose balance because of dizziness, or have you lost consciousness in the last 12 months? | Follow-up page 2 |
| 4 | Have you had a diagnosed bone or joint problem that could worsen with exercise? | Follow-up page 2 |
| 5 | Are you currently prescribed medication for blood pressure or a heart condition? | Follow-up page 2 |
| 6 | Do you have a diagnosed medical condition other than the above? | Follow-up page 2 |
| 7 | Has a doctor recommended you only do medically supervised exercise? | Automatic referral, skip to Step 3 |

**Step 2 — branch on Step 1 result:**

- **All 7 "no":** cleared for self-directed exercise at any intensity. Log clearance date; re-screen at next annual physical-activity-readiness cycle or after any 6-month gap in participation.
- **Any "yes" on Q1–Q6:** administer the relevant PAR-Q+ follow-up module for that question (each module is itself a 2–4 item branch). Any "yes" on a follow-up item → physician referral before starting; a full "no" clear on all follow-ups for that module → cleared with a documented note naming which module was triggered and cleared.
- **"Yes" on Q7:** skip follow-ups, route straight to physician referral.

**Step 3 — physician referral tracking:**

| Field | Entry |
|---|---|
| Participant ID | |
| Trigger question(s) | e.g., "Q1 core + follow-up 1b (chest pain during exertion)" |
| Referral sent date | |
| Medical clearance received (Y/N/pending) | |
| Cleared-for level (unrestricted / supervised only / restricted — name restriction) | |
| Re-screen due date | 12 months from clearance, or sooner if condition changes |

**Expected volume (staffing planning number):** on a general adult population, expect roughly 54% of new intakes to route to a physician before any exercise and roughly 3% before vigorous exercise specifically — size the referral-tracking workload and the "cleared for moderate only, pending physician sign-off for vigorous" holding category accordingly, not as a rare exception queue.

**Step 4 — biometric screen (where offered), route on first flag, don't average across metrics:**

| Metric | Referral cut point |
|---|---|
| Blood pressure | ≥130/85 mmHg |
| Waist circumference | ≥40 in (men) / ≥35 in (women) |
| Fasting triglycerides | ≥150 mg/dL |
| HDL cholesterol | <40 mg/dL |
| Fasting glucose | ≥100 mg/dL |

Any single flag → route to physician referral queue (Step 3 table) with "biometric" as the trigger field and the specific metric/value recorded, in parallel with — not instead of — the PAR-Q+ result.

## 2. Program Audit — Instrument Selection and Walk-Through

**Selection gate (answer this before opening either instrument):**

| Question being asked | Instrument | Structure |
|---|---|---|
| "Is our program's leadership, strategy, and measurement mature?" | HERO Scorecard | 62 questions, 6 domains (strategic planning, organizational support, program integration, participation strategies, evaluation, measurement) |
| "What policies and environmental supports actually exist on-site?" | CDC Worksite Health ScoreCard | 154 questions, 18 modules |

**HERO walk-through — scoring template:**

| Domain | Max points (illustrative weighting) | This cycle's score | Prior cycle | Delta |
|---|---|---|---|
| Strategic planning | 100 | 62 | 55 | +7 |
| Organizational support | 100 | 71 | 68 | +3 |
| Program integration | 100 | 48 | 44 | +4 |
| Participation strategies | 100 | 55 | 50 | +5 |
| Evaluation | 100 | 39 | 41 | −2 |
| Measurement | 100 | 44 | 38 | +6 |
| **Composite** | 600 | **319 (53%)** | 296 (49%) | +23 |

Flag any domain that drops two cycles running (Evaluation above, −2 this cycle) for a root-cause pass before the next audit, regardless of composite trend.

**CDC ScoreCard walk-through — module sampling template (18 modules, showing 3):**

| Module | Item example | Present? | Gap action |
|---|---|---|---|
| Nutrition | "Healthy items placed at eye level in vending/cafeteria" | No | Add to Q3 facilities work order |
| Physical activity | "On-site or subsidized fitness facility access" | Yes | — |
| Tobacco | "Tobacco-free campus policy, posted and enforced" | Partial (policy exists, not posted) | Signage order, 2-week turnaround |

Report the audit as domain/module scores plus a dated gap-action list, not a single number — leadership acts on the gaps, not the composite.

## 3. Incentive-Design Calculation Template

Run this any time an incentive amount, structure, or trigger changes — treat the ceiling as re-verified each time, not carried over from the last cycle.

**Inputs:**

| Field | Example value |
|---|---|
| Average annual total cost of coverage (self-only) | $9,400 |
| Program type | Health-contingent (activity- or outcome-based) |
| Tobacco-cessation component included? | Yes |
| Proposed general incentive (as designed) | $3,500/employee |
| Proposed tobacco incentive (as designed) | $3,500/employee (same, undifferentiated) |

**Calculation:**

1. General ceiling = 30% × total cost of coverage = 0.30 × $9,400 = **$2,820**.
2. Tobacco-specific ceiling = 50% × total cost of coverage = 0.50 × $9,400 = **$4,700** (only applies to the tobacco-cessation track; do not apply the 50% rate to the general incentive).
3. Compare: proposed general ($3,500) vs. ceiling ($2,820) → **over by $680/employee (24%)**.
4. Compare: proposed tobacco ($3,500) vs. ceiling ($4,700) → **under ceiling by $1,200** — room exists to increase this track specifically if it improves cessation participation.
5. ADA cross-check (only if incentive is large enough that disclosure stops being "voluntary" in practice, and a disability-related inquiry or medical exam is involved): confirm the ADA-linked cap, tied to self-only coverage cost specifically, against current EEOC guidance — this cell is contested and must be re-checked each cycle, not assumed stable from the prior year.
6. Output two tracks, not one blended number: general track at or under $2,820; tobacco track at or under $4,700, gated to confirmed tobacco users only.

**Revised proposal line (what goes in the memo):**

> General incentive: $2,800/employee (under the $2,820 ceiling). Tobacco-cessation incentive: $4,700/employee (at the 50% ceiling), limited to enrolled tobacco users, tracked as a separate program component.

## 4. Emergency-Response Readiness Cycle

Run this quarterly, and immediately after any staffing change on the floor.

| Step | Requirement | Evidence to file |
|---|---|---|
| 1 | Written emergency-response policy on file, reviewed this quarter | Dated sign-off sheet |
| 2 | AED(s) functional, battery/pad expiration checked | Inspection log, next expiration date |
| 3 | 100% of floor staff drilled on the response sequence in the last 90 days | Drill roster with names, date, role played (caller / AED / compressions / crowd control) |
| 4 | Drill timed: call for AED to pad-on-chest | Target ≤3 minutes; log actual time each drill |
| 5 | Any drill or real event >3 minutes to pad-on-chest | Root-cause note (equipment location, staffing gap, signage) and corrective action with owner and due date |

**Why the 3-minute target:** survival after cardiac arrest falls roughly 7–10 percentage points per minute of delay to defibrillation — about 90% at 1 minute, 50% at 5 minutes, 30% at 7, 10% at 9–11, 2–5% past 12 — so a drill time north of 3 minutes is treated as a finding requiring corrective action, not a pass.

## 5. Documentation Standard (what survives an audit)

Every screening, referral, audit cycle, and incentive change is logged with the specific trigger and the specific number, not a narrative summary:

- ❌ "Participant seemed fine, cleared them to start."
- ✅ "PAR-Q+ core Q1–Q6 all 'no', Q7 'no'. Cleared for unrestricted self-directed exercise, effective 2026-07-06. Re-screen due 2027-07-06 or sooner on 6-month participation gap."
- ❌ "Incentive looks compliant."
- ✅ "General incentive set at $2,800 vs. $2,820 ceiling (30% × $9,400 total cost of coverage); tobacco track at $4,700 vs. $4,700 ceiling (50% × $9,400), gated to confirmed tobacco users; ADA cross-check pending EEOC guidance re-verification dated this cycle."
