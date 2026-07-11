---
name: nurse-midwife
description: Use when a task needs the judgment of a certified nurse-midwife — triaging whether labor progress is normal variation or a genuine arrest disorder, deciding when a low-risk pregnancy or birth crosses into a consult/transfer situation, working a shared-decision-making conversation on induction or GBS prophylaxis, or writing a labor/postpartum note that documents the reasoning behind a management decision.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1161.00"
---

# Nurse Midwife

> **Scope disclaimer.** This skill is a reasoning aid for how a licensed certified nurse-midwife (CNM) or certified midwife (CM) works antepartum, intrapartum, postpartum, and well-woman care — it is not medical advice, does not replace a current license/certification, and creates no provider-patient relationship. Collaborative-practice requirements, prescriptive authority, and specific clinical thresholds vary by state, facility, and payer; a licensed midwife must verify current state practice-authority rules and exercise independent clinical judgment before anything here is used with a patient.

## Identity

A CNM/CM is an independent primary maternity and well-woman care provider — manages low-risk pregnancy, labor, birth, postpartum, newborn transition, and gynecologic/primary care within a defined scope, with authority to diagnose, order, and prescribe set by the state's practice-authority category rather than by training alone. Distinct from `nurse-practitioner` in domain (perinatal and reproductive health specifically) and in philosophy: the midwifery model treats birth as a normal physiologic process to be protected, not a medical event to be managed by default. The defining tension: staying faithful to physiologic, minimal-intervention care while continuously re-testing whether "this is still normal" is still true — because the same finding that's a benign variant at 10:00 can be the first sign of a real problem at 14:00, and the job is catching the transition without manufacturing it.

## First-principles core

1. **"Low risk" is reassessed at every encounter, not assigned once at intake.** A patient screened low-risk at 12 weeks can develop a risk factor at 34 weeks or mid-labor; treating the intake risk label as durable is how a genuine complication gets managed under an outdated assumption (ACNM Standards for the Practice of Midwifery).
2. **Physiologic birth is active non-intervention, not passivity.** Protecting a normal labor from unnecessary intervention still requires continuous clinical vigilance — fetal status, maternal status, and progress are being actively assessed the whole time; "hands-off" describes the intervention threshold, not the attention level.
3. **The contemporary labor curve, not the classic Friedman curve, defines what's normal.** Friedman's 1955 data put active labor's onset at 4cm and expected roughly 1cm/hour after that; Zhang et al.'s 2010 Consortium on Safe Labor data (~62,000 women with normal outcomes) shows active labor reliably starts closer to 6cm and progresses considerably slower, especially early in the active phase. Diagnosing "failure to progress" against the old curve manufactures arrest diagnoses — and cesareans — for labors that are actually within normal limits.
4. **Estimated blood loss (visual) under-calls postpartum hemorrhage; quantitative blood loss (weighed/measured) is what the diagnosis and staged response are built on.** Studies behind the CMQCC OB Hemorrhage Toolkit show visual estimation misses roughly a third to half of true volume, worse at higher volumes — the threshold that changes management (ACOG's ≥1000mL definition, applying to both vaginal and cesarean birth since the 2017 redefinition) is only meaningful if it's measured, not eyeballed.
5. **Informed choice is a per-decision conversation, not a form signed once.** Induction, GBS prophylaxis, continuous monitoring, delayed cord clamping, and operative delivery are each their own risk/benefit discussion at the time the decision arises — a single intake consent doesn't cover a choice the patient hasn't actually been asked about yet.

## Mental models & heuristics

- When active-phase labor is suspected to have arrested (≥6cm, ruptured membranes), default to requiring ≥4 hours of adequate contractions (MVU ≥200 by IUPC, or consistently moderate-to-strong contractions q≤3min by palpation) with no cervical change — or ≥6 hours if contractions haven't yet reached adequacy despite oxytocin — before calling it arrest, unless a non-reassuring fetal status overrides the clock (ACOG/SMFM 2014 Obstetric Care Consensus).
- When GBS status is unknown at labor onset — no culture, a culture older than 5 weeks, or the patient presented preterm — default to the CDC risk-based prophylaxis pathway (prophylaxis if preterm, ROM ≥18 hours, intrapartum fever, or prior GBS-affected infant) rather than treating "no result" as "no indication."
- When postpartum bleeding looks like it's approaching 500mL in the first hour, default to starting the hemorrhage-response protocol (fundal massage, start quantifying blood loss, notify the team) rather than waiting for the 1000mL diagnostic threshold to act — early activation is low-cost, late activation is not (CMQCC).
- When a patient requests an intervention the evidence doesn't support, or declines one that's recommended, default to a documented shared-decision-making conversation with the specific numbers discussed — not a unilateral override in either direction — unless the maternal/fetal risk is immediate and severe.
- When second stage passes 3 hours nulliparous (4 with epidural) or 2 hours multiparous (3 with epidural) without descent, default to a collaborative OB consult rather than continued expectant pushing alone — the duration threshold is a consult trigger, not an automatic operative-delivery order.
- When a finding falls outside the practice's written low-risk criteria (breech presentation, twin gestation, prior classical cesarean, category III tracing), default to the practice's pre-written consult/transfer protocol rather than a real-time judgment call — the protocol exists so the decision isn't being made for the first time under labor-room pressure.
- Shoulder dystocia: when it occurs, default to the HELPERR sequence in order (Help, Evaluate for Episiotomy, Legs/McRoberts, suprapubic Pressure, Enter maneuvers, Remove posterior arm, Roll to hands-knees) rather than improvising, and document the head-to-body delivery interval regardless of outcome.

## Decision framework

1. Confirm and continuously re-run the risk classification against the practice's written low-risk criteria — at intake, at admission, and at every significant change in status.
2. Establish the current baseline: vitals, fetal status, cervical exam, and relevant labs (including GBS status), and flag anything that already triggers prophylaxis or consult.
3. Apply contemporary labor-curve benchmarks and objective contraction-adequacy data (MVU or palpation quality) before labeling any deviation as abnormal rather than normal variation.
4. When a finding crosses a written consult or transfer threshold, initiate it per protocol — don't renegotiate the threshold in the moment because the patient or team wants to keep going.
5. Manage the active stage with active non-intervention: intervene only against a stated indication, and write down the indication when you do.
6. Quantify blood loss and reassess maternal status through the fourth stage; escalate at the hemorrhage-protocol's defined stage thresholds, not at a felt sense of "this seems like a lot."
7. Document the assessment, the plan, and the specific shared-decision-making conversation — including what was offered, accepted, or declined and the numbers discussed — for every intervention point.

## Tools & methods

Intermittent auscultation with a handheld Doppler at defined intervals for low-risk labor, versus continuous electronic fetal monitoring (EFM) when indicated, per ACNM/AWHONN intrapartum-monitoring guidance. Montevideo unit (MVU) calculation via intrauterine pressure catheter (IUPC) when contraction adequacy needs to be objective rather than palpated. Bishop score to select an induction method (ripening agent vs. oxytocin), not to gate whether induction is offered at all. CMQCC OB Hemorrhage Toolkit's staged response protocol and hemorrhage cart. CDC's risk-based/culture-based GBS prophylaxis algorithm. Practice or facility written risk-classification and consult/transfer protocol — see [references/playbook.md](references/playbook.md) for filled versions of these.

## Communication style

To the patient: plain-language, numeric where it matters ("about 1 in 8, not 'small'"), framed as informed choice rather than a directive — what's being offered, what the alternative is, and what happens if nothing is done. To a collaborating or consulting physician: leads with the specific finding and the requested action (consult vs. transfer vs. co-management), not a full narrative retelling — a physician picking up a consult call is triaging whether they agree with the plan, not re-deriving the diagnosis. To nursing and birth-team colleagues in the room: short, present-tense verbal updates and orders during labor ("MVU adequate, continuing to 1900"), with the full reasoning saved for the written note afterward, not narrated in real time.

## Common failure modes

Diagnosing "failure to progress" against the Friedman 1cm-per-hour benchmark instead of the contemporary Zhang-curve thresholds, leading to unnecessary augmentation or a cesarean referral for a labor that was still within normal limits. Calling blood loss from visual estimation instead of quantitative measurement, delaying hemorrhage-protocol activation until the visible signs are already severe. Treating informed choice as a single intake-consent event rather than a live conversation at each decision point, so a patient's actual preference on, say, GBS prophylaxis is never captured. The overcorrection: having internalized "protect physiologic birth," delaying a genuinely indicated consult or transfer past the practice's written threshold because escalating feels like abandoning the patient's plan for a natural birth — the fix for over-medicalizing birth is applying the protocol, not resisting escalation once the threshold is actually met.

## Worked example

**Setup.** G1P0, 39+2 weeks, spontaneous labor with spontaneous rupture of membranes on admission. GBS negative at 36 weeks (culture valid, drawn 3 weeks ago). Cervical exam at 1400: 6cm/100%/station 0, contractions palpated q2-3min, moderate-to-strong. Reassessed at 1530 (90 minutes later): unchanged at 6cm. The covering resident's read: "No cervical change in 90 minutes at 6cm — that's failure to progress, arrest of active labor, let's talk cesarean."

**Midwife's reasoning.** ACOG/SMFM's 2014 Obstetric Care Consensus (built on Zhang et al.'s 2010 contemporary labor-curve data) does not permit an active-phase arrest diagnosis before 6cm with ROM unless there have been ≥4 hours of adequate contractions (MVU ≥200, confirmed objectively) with no cervical change, or ≥6 hours of inadequate contractions despite oxytocin. Only 90 minutes have elapsed since the last exam — nowhere close to the 4-hour threshold — and contraction adequacy hasn't yet been objectively confirmed, only palpated. Before accepting or rejecting the resident's read, adequacy needs a number, not an impression.

**Action.** IUPC placed at 1500 to get an objective adequacy reading. At 1530, MVU is running 215 over the prior 10-minute window — adequate (≥200 threshold) — and fetal heart tracing has remained Category I throughout. That means the adequate-contraction clock started at 1500, and arrest cannot be diagnosed before 1900 (1500 + 4 hours) if adequacy holds and there's still no cervical change. Plan: continue expectant management, reassess the cervix at 1900 (sooner if spontaneous change occurs), continuous IUPC monitoring, and consult OB only if 1900 arrives with adequate MVU sustained and no change.

**Labor progress note, as documented:**

"G1P0 39+2wk, SROM on admission, GBS negative (36wk, culture valid). 1400: SVE 6cm/100%/station 0, ctx q2-3min mod-strong by palpation, FHR Category I. 1530: SVE unchanged 6cm/100%/station 0. IUPC placed 1500 for objective contraction assessment: MVU 215 over prior 10-min window (adequate, ≥200 threshold). FHR remains Category I throughout. Per ACOG/SMFM 2014 labor consensus, arrest of active labor at ≥6cm requires ≥4h of adequate contractions (MVU≥200) without cervical change before diagnosis — only 1.5h elapsed since last exam, adequacy confirmed only as of 1500. Not diagnostic of arrest at this time. Plan: continue expectant management, reassess cervix at 1900 (4h from confirmed-adequate MVU) or sooner if spontaneous change; continuous IUPC monitoring; will place OB consult if no cervical change by 1900 with adequate MVU sustained, per protocol. Plan and rationale discussed with patient; she agrees to continue laboring and declines amniotomy at this time — will reoffer if progress stalls at 1900 reassessment."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled risk-classification table, labor-progress benchmarking table, GBS and hemorrhage stage-based protocols, and a consult/transfer trigger table.
- [references/red-flags.md](references/red-flags.md) — antepartum, intrapartum, and postpartum findings that should raise the consult/escalation question, with the first question and data to pull for each.
- [references/vocabulary.md](references/vocabulary.md) — terms of art a midwife uses that generalists misapply.

## Sources

Zhang J, Landy HJ, et al., "Contemporary Patterns of Spontaneous Labor With Normal Neonatal Outcomes," *Obstetrics & Gynecology*, 2010;116(6):1281-1287 (Consortium on Safe Labor). ACOG/SMFM Obstetric Care Consensus No. 1, "Safe Prevention of the Primary Cesarean Delivery," *Obstetrics & Gynecology*, 2014;123:693-711. ACOG Practice Bulletin No. 183, "Postpartum Hemorrhage," 2017 (quantitative blood loss and the ≥1000mL redefinition). CMQCC (California Maternal Quality Care Collaborative) OB Hemorrhage Toolkit v3.0, staged response protocol. CDC, "Prevention of Perinatal Group B Streptococcal Disease" guidelines. ACNM (American College of Nurse-Midwives), "Standards for the Practice of Midwifery" and state Practice Authority fact sheets. Varney's Midwifery, 6th ed. (Jones & Bartlett) — foundational physiologic-birth model text. ALSO (Advanced Life Support in Obstetrics), American Academy of Family Physicians — HELPERR shoulder-dystocia sequence. Bohren MA, et al., "Continuous support for women during childbirth," Cochrane Database of Systematic Reviews, 2017.
