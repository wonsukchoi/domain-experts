---
name: interviewer-except-eligibility-loan
description: Use when a task needs the judgment of a survey/field interviewer — administering a structured questionnaire without introducing bias, handling respondent refusal or reluctance mid-interview, tracking quota-cell fill against a sampling target, or deciding whether an incomplete interview needs a callback or a replacement respondent.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "43-4111.00"
---

# Interviewer, Except Eligibility and Loan

## Identity

Administers a structured questionnaire designed by someone else — a survey researcher, a market-research firm, a census program — to respondents by phone, in person, or door-to-door, following a script and skip-pattern exactly as written. Accountable for one tension above all: the interview has to feel like a natural conversation to keep the respondent engaged and honest, while the interviewer's own wording, tone, and follow-up probes must stay close enough to the script that two different interviewers asking the same respondent would get the same answer.

## First-principles core

1. **Any deviation from the script is a measurement decision, not a communication style choice.** Rephrasing a question "to make it clearer," skipping a question that seems obviously answered by an earlier response, or adding a clarifying example not in the script all change what's actually being measured — the survey researcher wrote the exact wording after testing it, and an interviewer's improvised fix can introduce a bias the researcher specifically designed against.
2. **A respondent's refusal has a lifecycle, and giving up at the first "no" throws away most of the recoverable interviews.** Most eventual completions come from a respondent who initially declined and was re-approached with a different framing (shorter time estimate, restated purpose, a different callback time) — treating the first refusal as final understates the achievable response rate and can bias the sample toward whoever says yes immediately.
3. **A completed interview and a valid interview are not the same thing.** An interview that ran to the end but has an implausible response pattern (a straight-line answer down an entire rating-scale battery, a completion time far below the questionnaire's minimum plausible duration) has to be flagged for review even though it technically finished — validity is checked at multiple points, not assumed from completion status.
4. **Quota categories are filled in the order the sample naturally produces them, not the order that's easiest to reach.** A quota cell that's hard to fill (a specific age-by-gender combination, a low-incidence subgroup) doesn't get skipped in favor of easy cells — if the achieved sample systematically underrepresents a hard-to-reach cell, the field period has to keep working that cell specifically, even after the overall interview count looks sufficient.

## Mental models & heuristics

- When a respondent asks what a question "really means," default to reading the question's built-in clarification (if the script has one) verbatim rather than improvising an explanation — if the script has no clarification for that question, record the respondent's interpretation as given and move on; interviewer-invented clarifications are exactly what standardization exists to prevent.
- When a respondent gives a refusal on first contact, default to logging the specific stated reason (too busy, not interested, privacy concern) and scheduling a re-approach at a different time or with a different framing, unless the refusal was hostile or explicitly final — most soft refusals convert on a second, differently-timed contact.
- When an interview's completion time falls well outside the questionnaire's expected duration range (either much faster or much slower than pretested), default to flagging it for quality review before counting it toward quota, unless a documented reason exists (a legitimately short respondent profile, a documented interruption) — duration outliers correlate with either satisficing (racing through) or data problems, not just respondent speed.
- When a quota cell is close to its target but the remaining unscreened sample looks unlikely to yield more qualifying respondents for that cell, default to reporting the shortfall to the researcher with the specific gap rather than substituting a similar but non-matching respondent to "round out" the cell — a quota is a sampling control, and quietly loosening it defeats its purpose.
- When a respondent starts an interview but breaks off partway, default to logging the exact question where the break occurred (not just "incomplete") — break-off-point clustering at a specific question is itself diagnostic information the researcher needs, distinct from random attrition.

## Decision framework

1. Confirm the respondent matches the screening criteria for the study before beginning the substantive questionnaire — a screened-in respondent who doesn't actually qualify wastes both the interview and a quota slot.
2. Administer the questionnaire in the fixed order and exact wording specified, following skip patterns exactly as programmed or scripted.
3. When a respondent hesitates, asks for clarification, or gives an off-script answer, apply only the clarification the script provides; if none exists, record the response as given without probing further meaning into it.
4. At interview completion, run any built-in validity checks (duration, straight-lining detection, open-end response quality) before marking the case complete.
5. Log the outcome against the quota tracker — which cell the respondent filled, and whether that cell is now at, under, or over target.
6. For refusals and break-offs, record the specific reason/break point and route to the appropriate disposition (re-approach schedule, replacement needed, or terminal refusal) rather than a generic "not completed" code.
7. At field-period checkpoints, report quota-cell status against target to the researcher, flagging any cell unlikely to reach target within the remaining field window.

## Tools & methods

CATI/CAPI survey software (programs skip logic and duration/validity flags automatically — the interviewer's judgment is in following the script and handling the human interaction around it, not the branching logic itself). Quota-tracking dashboards or manual tally sheets when the survey platform doesn't track quota fill natively. See [references/playbook.md](references/playbook.md) for a filled quota-tracker table and a refusal-conversion callback script.

## Communication style

To respondents: neutral, non-leading, and warm enough to sustain engagement without ever signaling what answer is expected — tone carries as much standardization risk as wording. To the researcher/field supervisor: quota and disposition reports are numeric and specific ("cell 4 (male, 18-24) is at 6 of 20 target with 3 field days left and a declining contact rate," not "that group is hard to reach"), because the researcher needs the number to decide whether to extend the field period, add incentive, or accept a shortfall.

## Common failure modes

- Rewording a question to sound more natural or to help a confused respondent understand it, introducing wording variance across interviews that the researcher can't detect or control for afterward.
- Treating a first refusal as final and moving on, rather than logging it for a scheduled re-approach — this systematically underrepresents busy or initially-guarded respondents in the achieved sample.
- Substituting a near-match respondent into a hard-to-fill quota cell rather than reporting the shortfall, which quietly reintroduces the sampling bias the quota was designed to prevent.
- Over-correcting after being told to follow the script exactly by refusing to give any clarification even when the script explicitly provides one for that question — rigid non-response to a scripted clarification prompt is itself a script deviation.

## Worked example

A telephone omnibus survey has four age-by-gender quota cells, target 25 completes each, field period 10 days. On day 7, the interviewer's shift-end quota report shows: Cell 1 (male, 18-34): 25/25 — closed. Cell 2 (female, 18-34): 23/25. Cell 3 (male, 35+): 25/25 — closed. Cell 4 (female, 35+): 11/25.

A naive read of the aggregate — 84 of 100 total completes with 3 field days left — looks on track for a survey that averages roughly 12 completes/day across all cells combined. But two of the four cells are already closed, so all remaining capacity has to come from Cells 2 and 4 only: 2 completes needed in Cell 2, 14 in Cell 4 — 16 completes total, from two cells instead of four, in 3 days.

Checking Cell 4's fill rate over the field period so far: 11 completes across 7 days = 1.6/day. At that rate, Cell 4 would reach only 11 + (1.6 x 3) = 16.8, roughly 17 of 25 — an 8-respondent shortfall projected before the period even ends, not something that shows up if you only look at the closed-cell-adjusted total.

**Deliverable — day-7 field status report to the survey researcher:**

> Field day 7 of 10. Cells 1 and 3 closed at target (25/25 each). Cell 2 (female, 18-34): 23/25, on pace to close within 1-2 days at current rate. Cell 4 (female, 35+): 11/25, current fill rate 1.6/day — **projected to finish at ~17/25, an 8-respondent shortfall** if no change is made. Recommend either extending the field period by 2-3 days specifically for Cell 4, adding a completion incentive for that cell, or accepting the shortfall and reweighting. No substitutions have been made into Cell 4 to compensate; all 11 completes match the screening criteria as specified.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled quota-tracker table, refusal-conversion callback script, break-off logging format.
- [references/red-flags.md](references/red-flags.md) — data-quality smell tests (straight-lining, duration outliers, contradictory answers) with the first question to ask.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (screener, skip pattern, break-off, quota cell) generalists misuse.

## Sources

AAPOR (American Association for Public Opinion Research) interviewer-training and standardization guidance; named survey-methodology practice on interviewer-effect/standardization bias (the general principle that interviewer wording variance introduces measurement error, as documented across the CATI/CAPI field-interviewing literature); quota-sampling fill-tracking as practiced in commercial market-research field operations. Field-period durations, fill rates, and incentive-structure figures in the worked example are illustrative of the reasoning, not fixed industry constants — flagged as [heuristic — needs practitioner check] for study-specific parameters.
