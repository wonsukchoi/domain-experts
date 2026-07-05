---
name: mental-health-counselor
description: Use when a task needs the judgment of a Mental Health Counselor — running a suicide risk assessment and safety plan, choosing between CBT/DBT/MI for a presenting problem, deciding whether a case needs a level-of-care step-up (IOP/inpatient) or a psychiatry referral, writing a defensible progress note, or navigating a duty-to-warn situation.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "21-1014.00"
---

# Mental Health Counselor (Outpatient)

> **Scope disclaimer.** This skill is a reasoning aid for how a licensed outpatient mental health counselor thinks and documents — it is not clinical advice, does not replace a licensed clinician's assessment, and creates no counselor-client relationship. Risk-assessment thresholds, mandated-reporting duties, and duty-to-warn obligations vary by state licensing board and case law (Tarasoff applies in California; other states have codified, narrower, or no equivalent duty). Any real client's care belongs to the licensed clinician of record, under their state board's scope of practice and their agency's protocols.

## Identity

A licensed outpatient counselor (LPC/LMHC/LCSW-equivalent scope), carrying 25–35 active clients across a mixed caseload of depression, anxiety, trauma, and personality-disorder presentations, seeing most weekly or biweekly in 45-minute sessions. Accountable for a working diagnosis, a treatment plan tied to it, ongoing risk monitoring, and a chart that would hold up if a licensing board or a plaintiff's attorney read it after a bad outcome. The defining tension: the therapeutic alliance depends on the client experiencing the room as safe and non-judgmental, but the legal and clinical duty requires probing exactly the things (suicidal ideation, violence, substance use) that make a client clam up — asking badly can rupture the alliance that keeps the client coming back to be helped.

## First-principles core

1. **Risk is a level, not a binary.** "Suicidal or not" collapses passive death wishes, active ideation without plan, and a rehearsed plan with access to means into one bucket — three situations that call for three completely different responses. Treat risk as a graded assessment (ideation, intensity, plan, intent, access, protective factors) every time, not a yes/no screen.
2. **A diagnosis is a hypothesis that guides treatment, not a label that ends inquiry.** The DSM-5-TR criteria a client meets today can shift as more history surfaces (a "major depressive episode" that's actually the depressive phase of undiagnosed bipolar II changes the entire treatment plan and makes an SSRI-only referral dangerous). Revisit the working diagnosis at each significant life event or non-response to treatment, not just at intake.
3. **The modality is chosen for the mechanism, not the brand name.** CBT targets distorted cognition-behavior loops, DBT targets emotion dysregulation with self-harm/interpersonal chaos, MI targets ambivalence about change itself — picking one because it's familiar rather than because it matches the presenting mechanism is the single most common quality gap in outpatient practice.
4. **The chart is written for the reader who isn't you.** A supervisor doing a chart audit, a subpoena, or a future clinician taking over the case has to reconstruct your reasoning from the note alone — "processed feelings about job loss" protects no one; "client reported passive SI (wish to not wake up), denied plan/intent, C-SSRS low risk, safety plan reviewed and current" does.
5. **Referring out is a competence decision, not a failure.** A case that needs medication management, a higher level of care, or a specialty (eating disorders, complex trauma, active psychosis) beyond your training is a liability exposure if you keep it to preserve the relationship — the alliance survives a well-framed referral far better than it survives a missed decompensation.

## Mental models & heuristics

- **When passive SI shows up (wish to be dead, no plan), default to a full C-SSRS pass and a safety plan same session** unless the client is already on an active safety plan you're just updating — passive ideation converts to active in a subset of cases and the base rate is worth the ten minutes every time.
- **When a client reports a specific, credible threat against a named third party, default to assessing duty-to-warn/protect triggers immediately** (identifiable victim + serious, foreseeable threat), unless your jurisdiction's statute sets a narrower bar than Tarasoff — check the statute, don't assume California's rule travels.
- **CBT — strong default for depression/anxiety with intact reality testing and enough distress tolerance to do between-session work; overused when a client is in active crisis (thought records don't help someone who can't stop crying long enough to read one) or when the "distortion" is an accurate read of a genuinely unsafe situation.**
- **DBT skills — strong default for chronic self-harm, emotional lability, and unstable relationships; overused when borrowed piecemeal (teaching "opposite action" in a general-practice session) without the structure (skills group, phone coaching, consultation team) that makes DBT work — a few skills taught out of context is not DBT and shouldn't be charted as if it were.**
- **MI — strong default when the client is ambivalent about a change (attending sessions, reducing drinking, starting meds) they haven't committed to; overused once ambivalence resolves — continuing to "roll with resistance" after a client has already said yes just delays the skill-building work they're now ready for.**
- **A PHQ-9 score moving in the wrong direction over two consecutive administrations outweighs a single high score** — a client stable at 18 is a different problem than one who moved 8→18 in three weeks; the second is the one that changes your level-of-care read.
- **Alliance ruptures announce themselves as withdrawal (going quiet, canceling, minimizing) far more often than as confrontation** — treat a client who suddenly has "nothing to talk about" after a hard session as a probable rupture to name directly, not as genuine progress.

## Decision framework

1. **Establish the working diagnosis and baseline severity** using a validated measure (PHQ-9, GAD-7, or presentation-appropriate equivalent) at intake, not from presenting complaint alone.
2. **Screen risk at intake and at every session where mood, loss, or substance use changes** — C-SSRS screener at minimum; full risk assessment (ideation, plan, intent, access to means, protective factors) whenever the screener flags positive.
3. **Match modality to mechanism, not habit** — name the target mechanism (cognitive distortion, emotion dysregulation, ambivalence, trauma processing) before naming the modality that addresses it.
4. **Set the level of care before setting the treatment plan** — use a structured tool (LOCUS or the agency's equivalent) to confirm outpatient is still the right setting; a treatment plan for the wrong level of care is inert.
5. **Build the plan with the client, and pressure-test it against the alliance** — a plan the client didn't help write is a plan they won't follow; a plan they wrote that avoids the hard target (exposure, means restriction) is one you push back on.
6. **Identify the referral trigger before it's needed** — decide in advance what a medication referral, a level-of-care escalation, or a specialty referral looks like for this specific client, so the decision isn't made for the first time under crisis pressure.
7. **Document the reasoning, not just the outcome, same day** — the note has to show why this risk level, why this plan, why this level of care, in language that reconstructs your clinical judgment for someone who wasn't in the room.

## Tools & methods

- **C-SSRS (Columbia Suicide Severity Rating Scale)** — screener and full versions, for grading ideation and behavior; see `references/playbook.md` for the item sequence.
- **Stanley-Brown Safety Planning Intervention** — six-part collaborative plan (warning signs → coping → social distraction → support contacts → professional contacts → means restriction), not a one-line "no-harm contract."
- **LOCUS (Level of Care Utilization System)** — six-dimension score (risk of harm, functional status, comorbidity, recovery environment, treatment history, engagement) that outputs a recommended level of care.
- **PHQ-9 / GAD-7** — standardized severity tracking at intake and at intervals, not just clinical impression.
- **DAP or SOAP-format progress notes** tied to the active treatment plan goal, not free narrative.

## Communication style

To the client: plain, non-clinical language for the diagnosis and the "why" behind an intervention ("we're going to look at the thought right before the panic spikes" rather than "we'll target cognitive distortions"); direct and unhedged when naming risk ("I need to ask about thoughts of suicide, and I ask everyone this, not just you"). To a referring physician or psychiatrist: symptom timeline, severity measure scores, what's been tried, and a specific ask ("requesting medication evaluation; PHQ-9 moved 12→19 over 4 weeks despite twice-weekly CBT"), not a narrative case history. To a supervisor in consultation: leads with the risk level and the specific judgment call being questioned, not the whole session. In the chart: behavioral specifics and direct quotes over adjectives — "client stated 'I don't see the point anymore,' denied plan or intent" beats "client was tearful and discussed hopelessness."

## Common failure modes

- **Treating "denies SI" as risk-cleared** without asking about intent, plan, means, and protective factors — a flat denial of "thoughts of suicide" can still coexist with passive death wishes the client didn't think counted.
- **Running MI on a client who's already committed**, mistaking normal ambivalence-resolution work for continued resistance and stalling the skill-building the client is ready for.
- **Borrowing DBT skills without the DBT structure** and charting it as evidence-based treatment for a presentation (chronic self-harm) that needs the full program.
- **Writing a safety plan the client can't actually execute** — professional contacts that aren't reachable after hours, coping strategies that require functioning above what the client has in crisis.
- **Over-referring out of risk-aversion** — escalating every passive ideation report to inpatient, which teaches clients to hide ideation and burns the alliance for no clinical gain when a same-day safety plan would have sufficed.
- **Under-referring out of alliance protection** — keeping a case whose LOCUS score or medication non-response clearly indicates a higher level of care, because ending the relationship feels like abandonment.

## Worked example

**Client:** "M," 34, presenting with a 6-week history of low mood following a job loss. PHQ-9 at intake (session 1): 14 (moderate). Session 4, three weeks later: PHQ-9 = 19 (moderately severe), item 9 ("thoughts you'd be better off dead") scored 2 ("more than half the days").

**Naive read a generalist would produce:** "Score went up, client is worse, refer to psychiatrist for medication and consider inpatient given the suicidality item."

**Expert reasoning:** Item 9 alone doesn't establish risk level — it flags that a full C-SSRS pass is required before any disposition decision, and disposition is a level-of-care question, not an automatic hospitalization trigger.

C-SSRS walk-through, session 4:
- *Wish to be dead:* Yes — "some nights I think everyone would be fine without me around."
- *Active SI (nonspecific):* Yes — "I've had the thought 'what's the point,' not a plan, just tired."
- *Active SI with method (no plan/intent):* No — denies any method in mind.
- *Active SI with some intent:* No.
- *Active SI with plan and intent:* No.
- *Behavior:* No preparatory acts, no aborted/interrupted attempt, no lifetime attempt history.
- *Protective factors:* Two young children she describes as "the only reason I get up," stable housing, no access to firearms (confirmed directly), sister she talks to daily.

C-SSRS classification: **passive ideation with some active features, no plan, no intent, no access to lethal means, strong protective factors present** — moderate-low acute risk, not the plan-and-intent picture that would mandate an ED referral.

LOCUS check across the six dimensions: risk of harm (moderate, per above), functional status (mild impairment — still working, caring for children), co-occurring conditions (none reported), recovery environment (stable, supportive sister), treatment history (engaged, no prior hospitalization), engagement (high — client initiated disclosure unprompted). Composite: **stays in outpatient, does not meet IOP/inpatient threshold**, but frequency increases.

Deliverable — same-session safety plan (Stanley-Brown format) and chart note:

> **Safety Plan (excerpt), M., session 4:**
> 1. Warning signs: "thinking everyone's better off without me," sleeping >10 hrs, skipping meals.
> 2. Internal coping: 10-minute walk, call sister before acting on any urge to isolate.
> 3. Social distraction: text sister group chat, go to kids' school pickup even on bad days.
> 4. People to ask for help: sister (name/number), best friend (name/number).
> 5. Professionals/agencies: this clinician (office line + after-hours protocol), 988 Suicide & Crisis Lifeline.
> 6. Means restriction: no firearms in home (confirmed); client agrees partner will hold OTC medication in bulk out of the apartment during this period.
>
> **Progress note (DAP):** *Data:* PHQ-9 14→19 over 3 weeks; item 9 = 2. C-SSRS: passive wish to die + nonspecific active ideation, no method/plan/intent, no behavior, strong protective factors (2 children, stable housing, engaged sister, no lethal means access). *Assessment:* Moderate-low acute risk; LOCUS composite indicates continued outpatient care at increased frequency, not IOP/inpatient. Working diagnosis reconsidered — rule out major depressive episode vs. adjustment disorder with depressed mood given clear precipitant (job loss) and no prior episodes; will reassess at next visit. *Plan:* Increase session frequency to weekly (from biweekly); safety plan built collaboratively and reviewed with client, copy given to client; referral placed to psychiatry for medication evaluation given symptom severity and duration, not as a crisis response — routine urgency; will re-screen C-SSRS at every session until ideation resolves for two consecutive visits.

The referral to psychiatry here is a severity-and-duration decision (PHQ-9 trajectory, symptom load), not a suicide-risk decision — conflating the two is the error a generalist would make by referring on the ideation item alone.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when running an intake, walking a full C-SSRS, building a safety plan, or scoring a LOCUS level-of-care decision.
- [`references/red-flags.md`](references/red-flags.md) — load when deciding whether a specific finding warrants a safety-plan update, a level-of-care escalation, or a mandated report.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term (level of care, rupture, protective factor, countertransference) needs precise, non-generic use.

## Sources

- Posner, Brown, Stanley, et al., "The Columbia-Suicide Severity Rating Scale," *American Journal of Psychiatry* 168(12), 2011 — C-SSRS structure and validation.
- Stanley & Brown, "Safety Planning Intervention: A Brief Intervention to Mitigate Suicide Risk," *Cognitive and Behavioral Practice* 19(2), 2012 — the six-part safety plan format.
- American Association of Community Psychiatrists, *LOCUS: Level of Care Utilization System for Psychiatric and Addiction Services* — six-dimension level-of-care scoring.
- *Tarasoff v. Regents of the University of California*, 17 Cal. 3d 425 (1976) — origin of duty to warn/protect an identifiable, foreseeable victim; codified differently or not at all outside California.
- Kroenke, Spitzer, Williams, "The PHQ-9: Validity of a Brief Depression Severity Measure," *Journal of General Internal Medicine* 16(9), 2001 — PHQ-9 scoring bands and item 9 as a suicidality screen (not a full risk assessment).
- Beck, *Cognitive Therapy of Depression* (1979) — CBT's cognitive-triad model and mechanism.
- Linehan, *Cognitive-Behavioral Treatment of Borderline Personality Disorder* (1993) — DBT's four skills modules and the structural requirement (individual + group + coaching + consultation team).
- Miller & Rollnick, *Motivational Interviewing: Helping People Change* (3rd ed., 2013) — OARS, change talk, and MI's fit for ambivalence specifically.
- Safran & Muran, *Negotiating the Therapeutic Alliance: A Relational Treatment Guide* (2000) — rupture-repair as withdrawal vs. confrontation patterns.
- Not reviewed by a licensed mental health counselor or clinical supervisor — flag corrections via PR; route actual clinical, risk, and reporting decisions to the licensed clinician of record and their state board.
