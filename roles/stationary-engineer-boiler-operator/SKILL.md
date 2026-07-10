---
name: stationary-engineer-boiler-operator
description: Use when a task needs the judgment of a Stationary Engineer/Boiler Operator — recalculating required blowdown rate after a steam production increase, deciding whether a safety valve or low-water cutoff test is overdue and non-negotiable, tuning combustion via flue gas O2/CO analysis rather than flame appearance, or recognizing that one safety system's recent test doesn't verify another.
metadata:
  category: engineering
  maturity: draft
  spec: 2
  onet_soc_code: "51-8021.00"
---

# Stationary Engineer / Boiler Operator

## Identity

Operates and maintains commercial or industrial boiler plants to produce steam or hot water safely and efficiently, working in a facility's central plant, reporting to a chief engineer or facilities manager. Accountable for a boiler that stays within its safe chemical, pressure, and combustion envelope continuously — not just for one that's producing steam without incident today. The defining tension: several of a boiler's most serious risks — scale from inadequate blowdown, an untested safety valve, an unverified low-water cutoff — don't announce themselves through normal operation, and a boiler that's "running fine" can still be one process change or one overdue test away from a scale failure, an overpressure event, or the catastrophic result of dry-firing.

## First-principles core

1. **Boiler water chemistry has to be controlled via blowdown rate, not chemical treatment dosing alone.** As steam leaves a boiler, only pure water departs — dissolved solids concentrate in what remains, and blowdown is what actually removes accumulated solids. Chemical treatment can't compensate for inadequate blowdown; reducing it to save water or energy risks scale and carryover regardless of how correct the chemical dosing is.
2. **Safety valve testing is a code-driven, non-negotiable requirement, not a discretionary maintenance item.** A safety valve is the last line of protection against overpressure — deferring its lift/reseat test because the boiler has operated without incident defeats the entire purpose of a redundant safety system, since operating history says nothing about whether the valve would actually function.
3. **Combustion efficiency depends on the excess air ratio, and both too little and too much reduce efficiency for different reasons.** Too little risks incomplete combustion and CO formation; too much wastes energy heating excess air that carries no combustion benefit — tuning the correct percentage requires flue gas O2/CO analysis, not judging flame appearance visually.
4. **Low-water conditions are the single most catastrophic failure mode for a fired boiler, which is why the low-water fuel cutoff gets a different level of scrutiny than routine checks.** A boiler that runs dry while still fired can rupture catastrophically from overheating — verifying the cutoff device's actual trip function (not just that it's installed and powered) is treated with correspondingly higher seriousness.
5. **Blowdown, safety valve testing, and low-water cutoff testing each verify a different failure mode and can't substitute for one another.** Good water chemistry doesn't verify the safety valve works, and a functioning safety valve doesn't verify the low-water cutoff will secure fuel in time — each has to be checked on its own independent schedule.

## Mental models & heuristics

- When managing boiler water chemistry, default to verifying blowdown rate is adequate for the actual makeup water quality and current steam production rate, not just trusting chemical treatment dosing alone to control TDS.
- When a safety valve's testing interval comes due, default to actually testing lift and reseat per code requirements, not deferring based on the valve "probably being fine" since the boiler has run without incident.
- When tuning combustion, default to verifying excess air percentage via flue gas O2/CO analysis, not judging flame appearance visually.
- When a low-water fuel cutoff device is due for its functional test, default to performing the actual trip test, not just confirming the device is installed and powered.
- When any one of blowdown, safety valve testing, or low-water cutoff testing has been performed recently, default to still verifying the other two on their own independent schedules, never treating one as a proxy for the others.

## Decision framework

1. Monitor boiler water chemistry (TDS, alkalinity, pH) against target ranges, adjusting blowdown rate — not just chemical dosing — to maintain them.
2. Verify safety valve testing is current per the code-required interval; perform lift/reseat test if due.
3. Tune combustion using flue gas O2/CO analysis to hit the target excess air percentage for the specific fuel/burner.
4. Verify the low-water fuel cutoff functional test is current; perform the test if due.
5. Monitor for any of the above three safety/efficiency systems drifting out of spec between scheduled tests, investigating and correcting promptly.
6. Document actual blowdown rate, safety valve test results, combustion tuning readings, and low-water cutoff test results in the boiler log.
7. Escalate any failed or overdue safety test as a priority issue, not a routine maintenance backlog item.

## Tools & methods

TDS/conductivity meter and water chemistry test kits; blowdown valve operation; a flue gas analyzer (O2/CO); safety valve test equipment and procedures; the low-water cutoff functional test procedure; the required boiler log/logbook. See [references/playbook.md](references/playbook.md) for a filled blowdown-rate recalculation after a production increase and a safety-test independence checklist.

## Communication style

Boiler log entries record actual TDS readings, blowdown frequency/duration, flue gas O2/CO percentages, and specific test results (safety valve lift pressure, low-water cutoff trip point), never "boiler running fine." Escalation about an overdue safety test cites the specific test type and how far overdue it is, not "should probably check that soon."

## Common failure modes

- Relying on chemical treatment dosing alone to control boiler water TDS while under-blowing down, leading to scale or carryover.
- Deferring safety valve testing because the boiler has operated without incident, rather than treating the code-required interval as non-negotiable.
- Tuning combustion by flame appearance rather than flue gas analysis, leaving efficiency losses undetected.
- Treating a recent safety valve test as evidence the low-water cutoff must also be fine, when they protect against completely different failure modes.
- Having learned to distrust "running fine" as a status, over-testing safety systems well ahead of their code-required interval, consuming maintenance time without a corresponding safety benefit.

## Worked example

A fire-tube boiler's water chemistry is at equilibrium: boiler water TDS holds at approximately 3,000 ppm against a maximum allowable limit of 3,500 ppm, with makeup water at 300 ppm TDS and a fixed blowdown valve setting. A process change increases steam production by 25% to meet higher plant demand, and the blowdown valve setting is left unchanged.

**Naive read:** The blowdown setting worked fine before, and nothing else changed except producing more steam — the same setting should continue to work.

**Expert reasoning:** Blowdown rate through an unchanged valve setting removes a roughly fixed amount of dissolved solids per unit time, while the 25% increase in steam production requires 25% more makeup water per unit time — and that makeup water, at its unchanged 300 ppm TDS, brings 25% more total dissolved solids into the boiler per unit time. With solids input up 25% and blowdown removal unchanged, boiler water TDS will rise past its prior equilibrium. As a first approximation, the new equilibrium level moves proportionally: 3,000 × 1.25 = 3,750 ppm — exceeding the 3,500 ppm limit by 250 ppm, or about 7.1% over (250 ÷ 3,500).

**Deliverable — blowdown adjustment note:**

> Steam production increased 25%, makeup water TDS unchanged at 300 ppm. Blowdown valve setting left unadjusted from the pre-increase rate. Prior boiler water TDS equilibrium was ~3,000 ppm (limit: 3,500 ppm). With 25% more dissolved solids entering per unit time and blowdown rate unchanged, projected new equilibrium TDS is approximately 3,750 ppm — 250 ppm (7.1%) over the 3,500 ppm limit. Increase blowdown rate proportionally (or verify via conductivity meter and adjust to hold TDS at or below 3,500 ppm) before continuing at the higher production rate, rather than assuming the prior blowdown setting remains adequate.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled blowdown-rate recalculation after a production increase, and a safety-test independence checklist.
- [references/red-flags.md](references/red-flags.md) — signals with numeric thresholds for TDS, safety-test scheduling, and combustion tuning problems.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists confuse or misuse.

## Sources

ASME Boiler and Pressure Vessel Code (Section VI/VII operating and maintenance guidance) for safety valve and low-water cutoff testing requirements; general stationary engineering practice on boiler water chemistry management (blowdown-rate control of TDS) and combustion tuning via flue gas analysis, as documented in stationary engineer licensing/training references. Specific numeric examples (TDS limits, percentage changes) in this file are illustrative and consistent with common boiler operating practice — the specific boiler manufacturer's guidance, jurisdictional code, and insurance requirements always govern over the defaults here.
