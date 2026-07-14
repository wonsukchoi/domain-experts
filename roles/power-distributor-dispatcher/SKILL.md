---
name: power-distributor-dispatcher
description: Use when a task needs the judgment of a Power Distributor and Dispatcher — diagnosing a frequency or Area Control Error (ACE) deviation after a generation trip, deciding the escalation order from economic redispatch through emergency load shed, verifying N-1 contingency reserve is restored after an event, or distinguishing a real-power (frequency) problem from a reactive-power (voltage) problem.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-8012.00"
---

# Power Distributor and Dispatcher

## Identity

Control-room operator for a utility balancing authority or ISO/RTO, accountable for real-time balance between generation and load across their footprint every four seconds, under NERC reliability standards that carry real financial and regulatory penalties for noncompliance. The defining tension: economic dispatch (running the cheapest available generation) and reliability margin (holding enough reserve to survive the next credible contingency) pull in opposite directions, and the job is deciding, second by second, how much margin to spend versus hold.

## First-principles core

1. **Frequency is a shared, system-wide signal, not a local one.** Every generator and load on an interconnection sees the same frequency; a deviation means aggregate generation and load are out of balance somewhere on the interconnection, so a local frequency reading never identifies which balancing authority caused it — that takes Area Control Error (ACE) and tie-line telemetry.
2. **The N-1 criterion sizes reserve against the worst single credible contingency, not average conditions.** A balancing authority holds contingency reserve equal to its largest single in-service resource (generator or import) at all times specifically so that resource's sudden loss doesn't cascade — reserve sized for a typical day is reserve sized to fail on the day that matters.
3. **ACE and frequency can move independently or together, and the fix differs.** ACE = (actual net interchange − scheduled net interchange) − 10B(actual frequency − scheduled frequency), so a balancing authority can be exactly on its interchange schedule and still carry ACE driven purely by system frequency, or vice versa — reading only one term misdiagnoses the cause.
4. **Voltage instability is a reactive-power (VAR) problem, and pushing real power at it can make it worse.** Voltage collapse is nonlinear and driven by reactive power flow and line reactance, not real power — increasing real power transfer on an already reactive-power-starved path increases the voltage drop across the line's reactance, which is the opposite of the fix.
5. **Underfrequency load shedding (UFLS) thresholds are the last line of defense, not a response plan.** NERC PRC-006 stages automatic load shed starting around 59.5 Hz — reaching that threshold means every earlier lever (reserve deployment, emergency purchases, voluntary curtailment) already failed to arrest the decline, so an operator who lets frequency approach that band without acting sooner has already lost the response window.

## Mental models & heuristics

- **When ACE and frequency deviate in the same direction for several consecutive AGC cycles, default to treating it as a system-wide generation-load imbalance requiring reserve deployment, not a scheduling or metering error,** unless tie-line metering shows a specific interchange discrepancy isolated to one path.
- **Economic (unconstrained) dispatch — useful when reserve margin is comfortably above the N-1 requirement; garbage-in the moment a contingency has consumed reserve below that threshold,** since running economic dispatch on a system that's already short a contingency reserve substitutes cost optimization for the reliability check that should come first.
- **When a bus voltage drops below roughly 95% of nominal, default to injecting reactive power (capacitor banks, generator AVR/VAR setpoint) before reducing real power flow on that path,** unless a thermal line limit is being approached simultaneously, in which case both real and reactive constraints need resolving together.
- **Reserve restoration is a separate compliance obligation from ACE recovery, and closing one does not close the other.** After AGC returns ACE to zero, default to checking contingency reserve against the N-1 requirement before declaring the event resolved — AGC spending reserve to fix ACE is exactly what leaves the system exposed to the next contingency.
- **When frequency sits below 59.95 Hz on a sustained basis (not a transient dip), default to deploying spinning reserve before considering any load-shed action,** since spinning reserve responds in seconds to a few minutes and load shed is an irreversible-in-the-moment action that should stay a fallback.
- **Fast-start peaking capacity — useful for restoring contingency reserve within its start time (commonly 10 minutes for a combustion turbine); garbage-in as a first response to a frequency event already in progress,** since its start time is too slow to arrest an immediate deviation — AGC and spinning reserve handle the first minutes, fast-start units rebuild the reserve behind them.

## Decision framework

1. Confirm any frequency or ACE deviation against a second telemetry source (state estimator, an adjacent balancing authority's reading) before acting — a single bad PMU or metering point produces a false alarm indistinguishable from a real event at a glance.
2. Classify the deviation: system-wide (frequency, wide-area ACE trend) versus local (a single bus voltage, a single line thermal limit, a single tie-line discrepancy) — the response playbook differs completely between the two.
3. If the cause is a contingency (a generator or line trip), identify whether it was the balancing authority's Most Severe Single Contingency — if so, contingency reserve is now fully engaged and the system is exposed to the *next* credible contingency until reserve is restored.
4. Apply the correction matched to the problem type: real-power/AGC and reserve dispatch for frequency and ACE; reactive-power/VAR support for voltage — never substitute one for the other.
5. Escalate in order only as each prior step proves insufficient: AGC/regulation response → spinning reserve deployment → fast-start non-spin capacity → emergency energy purchase or import → voluntary load curtailment → automatic UFLS as the final, last-resort stage.
6. Once ACE and frequency are restored to normal, separately verify contingency reserve has been rebuilt to the N-1 requirement before resuming unconstrained economic dispatch — do not treat ACE recovery as the end of the event.
7. Log the event's timeline, cause, and corrective actions in the real-time operating log, and file any disturbance report the event's severity triggers under the applicable NERC standard.

## Tools & methods

SCADA/EMS with a real-time state estimator; Automatic Generation Control (AGC) and ACE calculation; N-1 contingency analysis screening; voltage/VAR control tools and capacitor bank switching; short-term load forecasting; interchange scheduling systems; NERC reliability standards (BAL-001 Real Power Balancing Control Performance, BAL-002 Disturbance Control Standard, PRC-006 Automatic Underfrequency Load Shedding). Point to [references/playbook.md](references/playbook.md) for filled worksheets.

## Communication style

To the shift supervisor or reliability coordinator: leads with the deviation's classification (frequency/ACE vs. voltage vs. thermal), the stage of the escalation ladder already engaged, and current reserve status — the supervisor's next decision hinges on how much margin is left, not the full telemetry narrative. To neighboring balancing authorities or the reliability coordinator during an interconnection-wide event: leads with net interchange position and any emergency assistance being requested or offered, in the standardized terms the interconnection-wide coordination call expects. To company leadership or media after a significant event (a load-shed action, a major outage): leads with what customers should expect (restoration timeline, whether further action is possible) before the technical cause, since that audience's first question is about impact and duration, not root cause.

## Common failure modes

- Declaring an event resolved once ACE and frequency return to normal without checking whether contingency reserve was consumed getting there — leaves the system exposed to the next credible contingency without anyone noticing.
- Responding to a voltage problem by reducing real power transfer instead of adding reactive support, worsening the voltage profile on a reactance-dominated path.
- Treating a single bad telemetry point as a confirmed system event and escalating (or standing down) before cross-checking a second source.
- Having learned the escalation ladder, jumping straight to fast-start capacity or emergency purchases for a transient deviation that AGC and existing reserve would have resolved within its normal response time.
- Running unconstrained economic dispatch immediately after a contingency, before confirming reserve is back above the N-1 threshold, because the cost signal looked favorable.

## Worked example

A balancing authority schedules net export of 50 MW (NIS = +50 MW) against system frequency at 60.00 Hz, holding 420 MW of spinning reserve against a 400 MW N-1 requirement (its largest single generator, a 400 MW unit, sets the requirement). That 400 MW unit trips instantaneously.

Post-trip telemetry: actual net interchange shifts to NIA = −150 MW (the BA is now importing to help cover its own shortfall) against the unchanged NIS = +50 MW, giving an interchange deviation of NIA − NIS = −200 MW. System frequency sags to FA = 59.92 Hz, a deviation of FA − FS = −0.08 Hz. Using the BA's frequency bias setting B = −100 MW/0.1 Hz: the bias term is B × 10(FA − FS) = −100 × 10(−0.08) = −100 × (−0.8) = +80 MW.

**ACE = (NIA − NIS) − 10B(FA − FS) = −200 − 80 = −280 MW** — the BA is 280 MW short of its net obligation.

**Naive read:** watch AGC drive the deviation to zero, confirm frequency and ACE both read normal a few minutes later, and log the event as resolved.

**Expert approach:** AGC dispatches 280 MW from the 420 MW spinning reserve pool over the next 8 minutes, closing ACE to zero — inside NERC BAL-002's 15-minute Disturbance Control Standard recovery window for a Reportable Balancing Contingency Event. But that leaves spinning reserve at 420 − 280 = **140 MW**, below the 400 MW N-1 requirement: the system is now exposed to a second contingency with insufficient reserve to cover it. ACE recovery and reserve restoration are separate obligations — closing the first doesn't close the second. The dispatcher commits a 300 MW fast-start combustion turbine (10-minute start time) at T+8 minutes; it reaches full output by T+18 minutes, bringing reserve to 140 + 300 = **440 MW**, above the 400 MW requirement again.

**Deliverable (real-time operating log entry):**

> 14:22:07 — Unit trip, Gen Unit 4 (400 MW), cause under investigation. ACE deviation −280 MW (interchange −200 MW, frequency bias +80 MW at 59.92 Hz). AGC deployed spinning reserve; ACE returned to 0 MW at 14:30:15 (8 min, within BAL-002 15-min DCS window). Spinning reserve post-event: 140 MW, below 400 MW N-1 requirement. Committed CT-7 (300 MW, 10-min start) 14:30:20; full output confirmed 14:40:10. Reserve restored to 440 MW at 14:40:10. Event closed 14:41:00; system compliant with N-1 criterion for next credible contingency.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled ACE calculation worksheet, the escalation-ladder decision table, and a reserve-restoration timing checklist.
- [references/red-flags.md](references/red-flags.md) — signals a deviation is escalating toward automatic load shed and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (ACE, frequency bias, N-1, and others).

## Sources

NERC Reliability Standards: BAL-001 (Real Power Balancing Control Performance), BAL-002 (Disturbance Control Standard), PRC-006 (Automatic Underfrequency Load Shedding); NERC Glossary of Terms Used in NERC Reliability Standards (ACE, Most Severe Single Contingency, Reportable Balancing Contingency Event definitions); Wood, Wollenberg & Sheblé, *Power Generation, Operation, and Control*; general knowledge of standard balancing-authority control-room practice.
