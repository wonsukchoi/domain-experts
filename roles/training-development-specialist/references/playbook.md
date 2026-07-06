# Playbook

Filled templates for the recurring instructional-design and LMS-administration mechanics. Adapt the numbers to the actual case; keep the sequence and the thresholds.

## 1. Rossett three-level needs assessment worksheet

Run before writing a single objective — a stakeholder's stated topic is an input, not the assessment.

```
REQUEST: "Customer service training" (VP of Operations, complaint volume up 22% QoQ)
SCOPE APPROVED BY: Training & Development Manager (skill gap confirmed, budget: $12,000)

LEVEL 1 — ORGANIZATIONAL (why now, what business metric is at risk)
  Driver: complaint volume +22% QoQ; escalation rate to store managers on
  receipt-less returns: 41% (POS override-code report, trailing 90 days).
  Business metric this must move: receipt-less-return escalation rate.

LEVEL 2 — TASK (what correct performance actually looks like)
  Method: structured interviews with 3 highest-CSAT store managers +
  review of 40 complaint transcripts (not a generic "walk me through
  your day" — ask "show me the last receipt-less return you handled").
  Finding: correct performance is a 3-tier decision rule (store-credit-only /
  manager-approval / decline) applied without escalation in under 2 min.
  Associates either escalate everything (safe but slow) or improvise
  (fast but inconsistent/non-compliant).

LEVEL 3 — PERSON (who has the gap, how large)
  Method: shadow 10 associates across 3 stores handling live returns;
  score against the Level 2 decision rule.
  Finding: 6/10 could not state the 3-tier rule unprompted; 8/10
  escalated at least one return that didn't require it.

GAP STATEMENT (write this, not the original request):
  Associates lack a decision procedure for applying the 3-tier
  receipt-less refund rule without escalating or improvising — this is
  a genuine skill gap (not a motivation or process-access issue; the
  policy exists and associates want to use it correctly), so a training
  intervention is warranted at the scope already approved.
```

**If Level 3 shows most people already perform correctly:** stop — the gap may be isolated to a few individuals or one store, which coaching resolves faster and cheaper than a training program built for the whole population.

## 2. Objective-writing worksheet (Mager format)

One terminal objective per course; one enabling objective per module/chunk.

```
TOPIC AS STATED: "Customer service training"

TERMINAL OBJECTIVE:
  Condition:  Given a customer return without a receipt
  Behavior:   the associate correctly applies the store's three-tier
              refund rule (store-credit-only / manager-approval / decline)
  Criterion:  within 2 minutes, per the process checklist, in 9 of 10
              observed transactions

ENABLING OBJECTIVES (each maps to one storyboard chunk):
  EO1 — Condition: given a return scenario description
        Behavior:  correctly classify it into one of the 3 tiers
        Criterion: 8/10 practice scenarios correct
  EO2 — Condition: given a tier-2 (manager-approval) scenario
        Behavior:  correctly identify what documentation to request
        Criterion: 4/4 documentation types correctly identified
  EO3 — Condition: in a live or role-played customer interaction
        Behavior:  deliver the tier decision to the customer without
                   escalating a tier-1/2 case to a manager
        Criterion: no unnecessary escalation in 5 role-play reps

BLOOM LEVEL CHECK: EO1/EO2 = Apply (not Remember — a multiple-choice
  "name the three tiers" question tests the wrong level for a decision-
  rule objective; use a classification/scenario item instead).
```

**Objective smell test:** if the behavior verb is "understand," "know," "be familiar with," or "appreciate," it isn't gradable — rewrite until the behavior is something you could watch someone do or a system could score.

## 3. Delivery-format decision matrix

Run per objective, not once per course — a single course can mix formats across modules.

```
                          ILT              eLearning         Blended
Fidelity to real task     High             Low-Med           High
                          (live practice,  (branching sim    (sim + live
                          feedback)        caps at decision  practice)
                                           logic, not
                                           physical/social
                                           skill)
Dev cost/finished hr      $3,000-6,000     80-300 production Both, additive
                                           hrs/finished hr
                                           (~$50/hr designer
                                           rate = $4,000-15,000)
Delivery cost/learner     5-20x eLearning  1x baseline       ILT portion only
                          for same content
Scales to distributed,    Poor (travel,    Excellent         Good (sim scales,
large audience            scheduling)                        live doesn't)
Best fit                  Psychomotor,     Declarative       Decision-rule +
                          high-stakes                        knowledge (sim),
                          interpersonal                       interpersonal
                                                              delivery (ILT)

DECISION for this objective set:
  EO1/EO2 (decision-rule knowledge) → eLearning branching scenario
    (20 min, ~$4,000 at lower interactivity tier, scales to 340 associates,
    12 stores, no travel).
  EO3 (live delivery to customer) → ILT role-play drill, store-manager-led,
    15 min per associate, ~$400/store all-in — the eLearning module can't
    simulate the live social-delivery component this objective requires.
  RULE APPLIED: match format to the objective's required practice fidelity,
  not to whichever format the last project used.
```

## 4. Storyboard fragment (branching scenario, one screen)

```
SCREEN 4.2 — Decision point
NARRATION: "The customer has no receipt and the item is a $180 jacket,
  purchased per the tag 41 days ago (store policy: 30-day full-refund
  window). What do you do?"

ON-SCREEN: 3-button choice (store-credit-only / request manager approval
  / decline) + return-context panel (item, price, days-since-purchase
  pulled from scenario variables, not hardcoded per screen)

BRANCH LOGIC:
  Choice A (store-credit-only) → CORRECT for 31-60 days past window.
    Feedback: "Correct — 31-60 days past the refund window is
    store-credit-only per the tier rule. No escalation needed."
    xAPI statement: {verb: "answered", result: {success: true},
    object: "return-decision-4.2"}
  Choice B (manager approval)  → INCORRECT, over-escalation.
    Feedback: "Not required here — 31-60 days past window is
    store-credit-only, no manager approval needed. Reserve manager
    approval for 61+ days or damaged-item claims."
    xAPI statement: {result: {success: false}, response: "manager-approval"}
  Choice C (decline)           → INCORRECT, under-serves customer.
    Feedback: "Too restrictive — this return still qualifies for
    store credit at 31-60 days; only decline past 61 days without
    a manager exception."

ROUTING: any incorrect choice → 60-second remediation card (the tier
  table) → retry with a new scenario variable set, not the same screen.
```

## 5. Kirkpatrick Level 1-4 evaluation plan template

Fill this at design time — every field needs a data source before the course ships, not after.

```
COURSE: Receipt-less Return Policy Module          LAUNCH: 2026-08-01

L1 REACTION
  Instrument: 5-item post-module survey (relevance, clarity, pace,
  confidence, would-recommend), 5-point scale.
  Data source: LMS survey block, auto-triggered at module completion.

L2 LEARNING
  Instrument: xAPI-tracked branch-choice accuracy across the scenario
  (see #4). Pass threshold: 8/10 correct branch selections.
  Data source: LRS (learning record store) xAPI statements, not the
  LMS's binary completion field.

L3 BEHAVIOR
  Instrument: manager observation checklist, 5 live transactions per
  associate, scored against the terminal objective's criterion.
  Schedule: day 30 and day 60 post-training (not "eventually").
  Data source: store manager submits checklist via [form/system]; specialist
  aggregates by store and cohort.

L4 RESULTS
  Metric: receipt-less-return escalation rate.
  Baseline: 41% (trailing 90 days pre-launch).
  Target: <=15% at day 60.
  Data source: POS override-code report, pulled monthly.
```

## 6. SCORM/xAPI LMS configuration checklist

Run when publishing any module, not just once at platform setup.

```
[ ] Package standard chosen: SCORM 1.2 (widest legacy LMS compatibility,
    coarse completion/score data) vs SCORM 2004 (sequencing/navigation
    control) vs xAPI (tracks individual interactions/branch choices,
    needs an LRS, required for #4/#5's branch-level data)
[ ] Completion trigger set to assessment pass, not "viewed all frames"
[ ] Pass/fail threshold matches the enabling objective's criterion
    (e.g., 8/10, not an arbitrary default like 70%)
[ ] Enrollment/assignment rule matches the actual population from the
    needs assessment (job role, store, or cohort — not "all employees"
    by default, which pollutes completion-rate reporting with people
    outside the identified gap)
[ ] Reporting fields exposed match what the L2/L3 evaluation plan
    committed to (branch-choice data, not just pass/fail, if the
    evaluation plan calls for it)
[ ] Retake/remediation path configured (how many attempts, what
    remediation content shows on failure) before launch, not patched
    in after the first failing cohort
```
