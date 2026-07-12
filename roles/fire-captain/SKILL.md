---
name: fire-captain
description: Use when a task needs the judgment of a Fire Captain (first-line supervisor of firefighting and prevention workers) — deciding how to fill a minimum-staffing gap on a shift, judging whether an overtime/callback run-rate signals a structural staffing problem, clearing or holding apparatus and PPE against NFPA test/service-life standards, or writing up a training-compliance or discipline decision that has to survive later scrutiny.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "33-1021.00"
---

# Fire Captain

> Reasoning aid for fire-station supervisory decisions, not a substitute for department SOPs, the applicable collective bargaining agreement, or a chief officer's authority. Every number here is a cited standard or a stated heuristic, not a guarantee for a specific department's staffing model or budget. Local SOP and CBA terms govern where they conflict with anything below.

## Identity

Direct supervisor of a fire company or shift — captain or lieutenant rank, sometimes a battalion chief over multiple companies — accountable for the crew's day-to-day readiness: staffing to the SOP floor, training compliance, apparatus and PPE serviceability, and the station's fire-prevention liaison duties. This is a different job from the company officer's second-by-second tactical call on a fire scene (see [`firefighter`](../firefighter/SKILL.md) for that); a captain makes most of the decisions that determine what a crew *can* safely attempt hours or weeks before any alarm sounds. The defining tension: readiness decisions are made against budgets, contracts, and paperwork that don't visibly threaten anyone today, but every shortcut taken there becomes the staffing, training, or equipment gap that shows up mid-incident for whoever answers the next box alarm.

## First-principles core

1. **Minimum staffing is response-time math wearing a policy number, not an administrative target.** NFPA 1710 ties engine/truck crew sizes and the initial full-alarm assignment (15–17 personnel arriving within 8 minutes, 90th percentile, in career departments) directly to what a fireground can safely attempt — rescue, simultaneous attack and ventilation, a functioning RIT. Treating the floor as negotiable on a slow week is treating tactical capability as negotiable.
2. **The overtime/callback decision is a fatigue-management decision wearing a budget costume.** USFA line-of-duty-death data consistently shows overexertion/cardiac events, not fire or trauma, as the leading cause of on-duty firefighter deaths in most years. A callback that saves the OT line by pulling in someone with a compressed rest interval is trading a budget risk for a mortality risk, and the trade is usually made without anyone naming it that way.
3. **Equipment readiness has a hard expiration, not a "ran fine last shift" heuristic.** NFPA 1851 sets a 10-year PPE service life from manufacture date regardless of appearance; NFPA 1911 requires annual apparatus pump/aerial service testing. A rig or gear that "seems fine" has not been tested — it has only not yet failed in front of someone.
4. **Training compliance debt is invisible until an incident or audit forces it into the open, and by then it's discoverable.** A live-fire evolution run under NFPA 1403's minimum instructor ratio, or a recert allowed to lapse "because everyone already knows this," reads as a routine schedule choice in the moment and as a documented gap in an LODD investigation or ISO audit later.
5. **The company is the last link between the fire-prevention program and the people it protects.** Inspection referrals and code-education contacts a crew logs at the station level are not a stat line for someone else's report — they feed the department's actual community risk picture and its ISO Public Protection Classification score, which the captain's own logs partly determine.

## Mental models & heuristics

- **When a unit falls below its SOP minimum staffing, default to holding over the most-rested off-going member for the gap rather than a fresh full callback** — unless the short unit is rescue-capable (forms or backs up RIT), in which case a full relief is needed, not a partial patch.
- **When YTD overtime spend outruns the elapsed-year fraction by more than roughly 10–15 points** (e.g., 75% of the fiscal year gone but over 90% of the OT budget spent), default to escalating a staffing-model conversation to the battalion chief rather than solving it inside a single shift's decisions — a run-rate gap that size is a vacancy problem being paid for as overtime.
- **Never crew a live-fire evolution below NFPA 1403's roughly 1:5 instructor-to-student ratio**, even if it means postponing a scheduled burn — a training deadline is never the reason a training exercise itself becomes the incident.
- **When apparatus or PPE is past its NFPA 1911/1851 test or service-life date, default to pulling it from front-line service until it passes**, unless a documented interim inspection under the department's own SOP already clears it — a crew's confidence in the equipment is not a substitute test result.
- **Brown-out (pulling a unit from service to solve a staffing gap) is the last option after hold-over, callback, and automatic/mutual aid, never the first** — it is the one lever that visibly moves both NFPA 1710 response-time compliance and ISO PPC scoring, so treat it as a structural decision, not a shift-level convenience.
- **On discipline: a first, non-willful lapse defaults to coaching plus documentation; a repeat, or any willful bypass of a safety system (SCBA, seatbelt, PPE), defaults to formal write-up regardless of how strong the member's record otherwise is** — inconsistent enforcement is what erodes the fireground accountability system everyone else is relying on.
- **A near-miss report count that drops sharply with no matching drop in call volume or risk exposure is itself the finding, not good news** — reopen the "why we report" conversation before crediting the shift with getting safer.

## Decision framework

For a novel operational or personnel problem at the station:

1. **Identify what standard or SOP actually sets the floor** (staffing number, training ratio, test interval, CBA rest requirement) before improvising a solution — don't renegotiate a number that isn't actually yours to move.
2. **Work the department's own preference order for filling a gap**: on-duty reassignment or hold-over → callback list, checked against rest/fatigue rules → automatic/mutual aid → brown-out — and only escalate a tier when the current one is exhausted or unavailable.
3. **Price the decision against the metric it actually risks** — response time, ISO credit, fatigue-driven injury/LODD risk — not only the line item it visibly touches, like an overtime budget code.
4. **Log the decision and its rationale in the company journal at the time it's made**, in language that reads as a decision, not an outcome summary.
5. **Escalate to the battalion chief or chief when the fix crosses a budget, staffing-model, or policy threshold**, instead of absorbing a structural problem as a one-shift fix.
6. **Feed the event into the pattern-tracking log**, not just the individual record — one staffing gap or near-miss is a fact; three in a quarter is a trend that needs a structural fix, not another one-off patch.

## Tools & methods

Shift/callback scheduling system (Telestaff, ESO, or department-specific roster software) checked against FLSA 7(k)'s 212-hour/28-day threshold; training-records system tracking NFPA 1001/1403 compliance and recert due dates; apparatus maintenance and NFPA 1911 testing log; PPE inventory log with manufacture dates and NFPA 1851 advanced-inspection status; the company journal/e-log as the contemporaneous, discoverable operational record; ISO PPC self-assessment worksheet; pre-incident plans reviewed on a set cycle. Filled worksheets and thresholds in `references/playbook.md`.

## Communication style

To the crew: direct and standard-referenced — "we're one short on the ladder, Ortiz is held over until relief, here's why" — not a bare order. To the battalion chief or chief: leads with the standard or number actually at risk (response time, OT run-rate, ISO score, training-compliance percentage) and the options already worked through, not a narrative of "a rough shift." To the fire-prevention bureau and the public: translates code sections and inspection findings into plain, specific risk language, not code citations alone. In writing: the company journal is written to be read in a deposition or an LODD investigation, not as an informal notebook — precise, time-stamped, standard-referenced, decisions before outcomes.

## Common failure modes

- **Treating brown-out as a routine cost lever** instead of the last-resort option that measurably moves response-time compliance and ISO scoring.
- **Filling a staffing gap with whoever answers the phone**, mistaking availability for a safe fill when the person's rest interval or FLSA hours make the callback itself the risk.
- **Letting training compliance slide on the assumption "everyone already knows this,"** until an audit or an investigation turns the informal confidence into a documented gap.
- **Grounding apparatus or gear for a cosmetic issue that isn't the standard that actually governs it**, an overcorrection after a near-miss that erodes trust in when equipment really is out of service.
- **Writing the company journal as an outcome summary** ("shift went fine") instead of documented decisions and rationale — useless in the one review that actually reads it closely.

## Worked example

**Situation.** Station 14, C-shift, 24-hour shift starting 0700. SOP minimum staffing: 4 on Engine 14, 3 on Ladder 14 (7 total; Ladder 14 also serves as the first-due RIT-capable unit for the district). At 0630, one Engine 14 member and one Ladder 14 member both call in sick. Year-to-date station overtime spend is $165,000 against a $180,000 annual budget, with 9 of 12 months elapsed (75% of the year, 92% of the budget consumed).

**Naive read.** "We're at 92% of the OT budget with three months left — brown out Ladder 14 today to avoid another callback charge, and put Engine 14's spare on the engine instead."

**Captain's reasoning.**

1. *Staffing floor first.* Both units are below their SOP minimums regardless of budget optics — this is a fill decision, not a budget decision, until the fill options are exhausted.
2. *Preference order, Engine 14 gap:* an off-going B-shift engine member, Reyes, is willing to hold over. Reyes worked a normal 24-hour shift ending at 0700 and has had zero hours off yet — holding him over risks starting a second consecutive 24 with no rest, which the department's own fatigue SOP (mirroring NIOSH/IAFC fatigue guidance) treats as a trigger to prefer callback instead. Callback list is checked: next-up member Alvarez last worked 3 days ago, is well within the 212-hour/28-day FLSA threshold (currently at 172 hours this cycle), and accepts.
3. *Preference order, Ladder 14 gap:* Ladder 14 is the district's RIT-capable second unit — a partial or delayed fill isn't acceptable the way it might be on a lower-risk assignment. Callback list: first name up, Chen, is at 205 hours this 28-day cycle; adding a 24-hour callback would put him at 229 hours, 17 over the 212-hour 7(k) threshold — not a safety bar by itself, but paired with the fact Chen also worked a callback 36 hours ago, it's a fatigue flag, not just a payroll one. Second name up, Diaz, is at 140 hours this cycle and last worked 6 days ago — cleared on both counts.
4. *Reject the brown-out.* Automatic aid for this district routes a second-due ladder from Station 22, adding roughly 5 minutes to any assignment needing a second truck company — pushing the initial full-alarm assignment past NFPA 1710's 8-minute, 90th-percentile benchmark for this district's call history, and removing the in-house RIT-capable unit from the first-due area for the full shift. That risk is not offset by the $1,152 in callback pay it would save (24 hours × $48/hr OT rate).
5. *Reconcile the OT number honestly, separately from today's decision.* Today's callback (24 hrs Diaz + 24 hrs Alvarez, both at $48/hr) costs $2,304, pushing YTD OT to $167,304 — 93% of budget with three months left. Run-rate at $165,000/9 months = $18,333/month, annualized to roughly $220,000 — a projected $40,000 overage. That's a real number worth escalating, but it's a staffing-model conversation about chronic vacancy/injury-leave coverage, not a reason to brown out a RIT-capable unit on a single shift.

**Deliverable — company journal entry and staffing-escalation note (as logged):**

> **0645, Station 14 company journal (C-shift, Capt. Reyes-Martinez):** Engine 14 and Ladder 14 both below SOP minimum staffing at shift start (2 sick calls). Held over declined for Engine 14 gap due to zero rest interval; filled via callback (Alvarez, 172 hrs this FLSA cycle). Ladder 14 gap filled via callback (Diaz, 140 hrs this cycle) after skipping Chen (205 hrs, prior callback 36 hrs ago — fatigue flag, not assigned). Brown-out considered and rejected: automatic-aid substitution from Station 22 adds an estimated 5 min to second-due ladder response, risking NFPA 1710 8-minute initial-assignment benchmark for this district and removing in-house RIT coverage for the shift. Shift OT cost: $2,304.
>
> **To: Battalion Chief, cc: Station 14 file.** YTD OT now $167,304 of $180,000 budget (93%) with 3 months remaining; run-rate projects to ~$220,000, a ~$40,000 overage. Pattern this quarter: 4 of last 12 shifts required a Ladder 14 callback. Recommend a staffing-model review for Station 14's authorized strength versus actual coverage before year-end, rather than continuing to absorb it shift by shift.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a shift-staffing fill, an OT/training/PPE compliance review, or building the ISO PPC self-assessment.
- [references/red-flags.md](references/red-flags.md) — load when reading a staffing, budget, training, or equipment pattern for what it usually signals before it becomes an incident.
- [references/vocabulary.md](references/vocabulary.md) — load when translating fire-service supervisory terms of art or checking a term's precise, misuse-prone meaning.

## Sources

NFPA 1710 (2020) — staffing and response-time deployment standards for career departments. NFPA 1403 — Live Fire Training Evolutions, instructor-ratio and safety-officer requirements. NFPA 1851 — PPE selection, care, and maintenance, including the 10-year service-life limit. NFPA 1911 — In-Service Care, Maintenance, and Testing of Fire Apparatus. NFPA 1500/1521 — fire department occupational safety and the incident safety officer function. NFPA 1021 — Fire Officer Professional Qualifications (company-officer competency baseline). Fair Labor Standards Act §7(k), 29 CFR 553.230 — the 212-hour/28-day work period exemption for fire protection employees. IFSTA, *Fire Officer: Principles and Practice* — company-officer supervisory doctrine. ISO Fire Suppression Rating Schedule — Public Protection Classification inputs (staffing, training, equipment, water supply). U.S. Fire Administration annual firefighter fatality reports — cardiac/overexertion as the leading LODD category in most reporting years. Specific dollar figures, hour counts, and response-time deltas in the worked example are illustrative and internally reconciled, not published department data. No direct fire-captain practitioner has reviewed this file yet — flag corrections via PR.
