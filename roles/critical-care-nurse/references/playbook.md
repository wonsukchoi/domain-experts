# Critical Care Playbook

Filled examples for the recurring ICU decisions — escalation ladders, ventilator settings, and the daily liberation sequence. Load this when actually building one of these in the moment, not for background reading.

## Vasoactive escalation ladder (septic shock)

Order set assumed: norepinephrine first-line, protocol permits vasopressin as fixed-dose second agent, epinephrine as third-line, hydrocortisone as adjunct at refractory doses. Always confirm against the actual standing order before acting — this is the common shape, not a universal one.

| Step | Agent | Dose | Trigger to move to next step |
|---|---|---|---|
| 1 | Norepinephrine | Start 2–4 mcg/min, titrate q5–15min within ordered range (commonly 2–20 mcg/min) to MAP ≥65 | Reaches ordered ceiling without MAP at target |
| 2 | Vasopressin | Fixed dose 0.03 units/min (not titrated) added on top of norepinephrine | MAP still <65 after ~30–60 min on vasopressin, or norepinephrine requirement continues climbing |
| 3 | Epinephrine | Start 0.05 mcg/kg/min, titrate to MAP ≥65, added or substituted per protocol | MAP still <65 on three agents |
| 4 | Hydrocortisone | 200 mg/day IV (divided or continuous infusion) | Vasopressor-refractory shock (persistent need for escalating doses despite steps 1–3) |

**Reassessment cadence:** MAP and heart rate every 5–15 minutes during active titration; lactate every 2 hours until clearing ≥10–20% per interval, then per unit protocol; UOP hourly.

**Never do:** titrate norepinephrine past the ordered ceiling to "buy time" before calling — that's the trigger to move down the ladder or call, not a reason to hold at the top rung longer.

## ARDSnet lung-protective ventilation table

Predicted body weight (PBW), not actual weight, sets tidal volume. PBW (male) = 50 + 2.3 × (height in inches − 60); PBW (female) = 45.5 + 2.3 × (height in inches − 60).

| Step | Action | Threshold to advance |
|---|---|---|
| 1 | Set Vt to 8 mL/kg PBW | Immediately reduce toward 6 mL/kg over 1–4 hours |
| 2 | Hold Vt at 6 mL/kg PBW, check plateau pressure (0.5s inspiratory pause) | Plateau ≤30 cmH2O: hold. Plateau >30: reduce Vt in 1 mL/kg steps (to a floor of 4 mL/kg) |
| 3 | If Vt already at 6 mL/kg and plateau >30 | Drop to 5, then 4 mL/kg PBW; accept a rising respiratory rate (permissive hypercapnia) to compensate for minute ventilation, per protocol pH floor (commonly 7.15–7.30) |
| 4 | PEEP/FiO2 combination per ARDSnet low- or high-PEEP table, matched to oxygenation target (commonly SpO2 88–95% or PaO2 55–80 mmHg) | Escalate PEEP/FiO2 pair together, not FiO2 alone, once above ~0.6 FiO2 |

**Peak vs. plateau differential:** peak pressure rises with plateau → compliance problem (worsening lung injury, auto-PEEP, abdominal distension). Peak rises, plateau flat → resistance problem (secretions, bronchospasm, kinked/biting tube) — suction or address the airway before touching ventilator settings.

## Daily liberation sequence (ABCDEF bundle)

Run once per shift, ideally at a consistent time coordinated with respiratory therapy:

1. **A — Assess/manage pain** first; an unmedicated pain source is the most common reason a subsequent SAT looks like it "failed."
2. **B — Both SAT and SBT, paired same day.** SAT safety screen: no active seizure, no escalating sedative need for agitation in the last 4h, no neuromuscular blockade running, no active myocardial ischemia. If SAT passes (patient tolerates being awake without unsafe agitation), immediately run the SBT — a T-piece or low pressure-support trial for 30–120 minutes, screened for RR/tidal volume ratio <105 (rapid shallow breathing index) and hemodynamic stability throughout.
3. **C — Choice of sedation**, targeting the ordered RASS with the lightest agent that achieves it; document the target and the actual score every check, not just the actual score.
4. **D — Delirium: monitor with CAM-ICU** at least once per shift and with any RASS or mental-status change; if positive, work the driver list (hypoxia, new infection, withdrawal, the sedative itself, sleep deprivation) before adjusting sedation dose.
5. **E — Early mobility**, screened against a simple stability gate (MAP at goal without an increasing pressor requirement in the last 2h, FiO2 ≤60%, no new arrhythmia) — re-screen every shift rather than carrying forward yesterday's "not a candidate."
6. **F — Family engagement**: update on the day's plan and the next decision point, invite presence during rounds or mobility sessions where the unit allows it.

## Lactate clearance calculation (worked)

Formula: % clearance = [(initial lactate − repeat lactate) / initial lactate] × 100, over the elapsed interval.

Example: initial 4.2 mmol/L at 0600, repeat 3.1 mmol/L at 0715 (75 minutes later).
(4.2 − 3.1) / 4.2 = 0.262 → **26.2% clearance over 75 minutes**, well ahead of the 10–20% per 2-hour target — a favorable trend even if the blood pressure hasn't caught up yet.
