# Working vocabulary

Terms a project management specialist uses precisely and generalists blur. Format: definition → practitioner sentence → common misuse.

**PV / EV / AC (planned value, earned value, actual cost)** — PV = the budgeted cost of work scheduled to be done by now. EV = the budgeted cost of work actually done by now. AC = what was actually spent to do it.
In use: "PV says we should have earned $520K by now; we've only earned $430K, and it cost us $505K to get there."
Misuse: treating AC vs. PV as the meaningful comparison (that's just spend-vs-budget, ignoring how much work actually got done) instead of comparing EV against both.

**CV / SV (cost variance, schedule variance)** — CV = EV − AC (negative means over budget for work done). SV = EV − PV (negative means behind schedule).
In use: "CV is −$75K, SV is −$90K — we're both over budget and behind, and by similar magnitude."
Misuse: reading SV as a measure of calendar days late. It's a dollar-denominated proxy for schedule health, not days — a big SV on a small work package can be schedule-trivial.

**CPI / SPI (cost/schedule performance index)** — CPI = EV/AC; SPI = EV/PV. 1.0 is on-plan; below 1.0 is unfavorable.
In use: "CPI's at 0.85 — for every dollar spent we're only earning 85 cents of planned value."
Misuse: averaging CPI across work packages and reporting only the blended number — one package at 0.33 can hide inside a total that looks like a survivable 0.85.

**EAC (estimate at completion)** — The forecast total cost given performance to date. Multiple formulas exist and picking the wrong one for the driver produces a wrong forecast: `AC + (BAC − EV)` assumes the variance was one-time; `BAC / CPI` assumes it persists; a CPI×SPI-weighted version assumes both cost and schedule pressure compound.
In use: "The rate increase is structural, so EAC = BAC/CPI ≈ $987K, not the optimistic AC + (BAC−EV) number."
Misuse: defaulting to one EAC formula regardless of whether the underlying cause is one-time or systemic — this is the single most common EVM error in practice.

**ETC (estimate to complete)** — EAC minus AC: how much more the project is forecast to cost from today forward.
In use: "ETC is $482K — that's what's left to spend, not the $335K the original budget implies."
Misuse: confusing ETC with the *remaining budget* (BAC − AC), which is what's left in the original plan, not what's actually forecast to be needed.

**TCPI (to-complete performance index)** — The cost efficiency the remaining work must achieve to hit a target (BAC or EAC). `(BAC−EV)/(BAC−AC)` for the original budget; `(BAC−EV)/(EAC−AC)` for the current forecast.
In use: "TCPI to hit the original $840K is 1.22 — we've never run above 0.85, so reporting $840K as live is fiction."
Misuse: quoting TCPI-to-BAC as if it were achievable without asking whether the team has ever historically performed at that efficiency level.

**Contingency reserve vs. management reserve** — Contingency = budget set aside for identified, quantified risks within the project baseline; the specialist/PM can draw it against a named risk. Management reserve = budget held above the baseline for unknown-unknowns; only the sponsor/PMO can authorize release, and doing so is itself a baseline change.
In use: "That draw comes out of contingency — R-014 was already scored and budgeted for. The $63K gap beyond that needs management reserve, which means it goes to the sponsor."
Misuse: treating the two as one pool, or letting a PM release management reserve without a formal change entry — this is how reserves quietly disappear before anyone realizes the project has no cushion left.

**Baseline vs. rebaseline** — The baseline is the originally approved scope/schedule/cost plan, frozen for variance comparison. Rebaselining replaces it with a new approved plan — a discrete, dated, approved event, not a gradual drift.
In use: "We rebaselined in month 6 after CR-09 was approved — everything before that compares to the old baseline, everything after to the new one."
Misuse: letting "the current plan" silently become the new baseline without a logged approval — every EVM variance calculated afterward is then comparing against a plan nobody signed off on.

**Float (total float vs. free float)** — Total float = how long a task can slip without delaying the project end date. Free float = how long it can slip without delaying the *next* task. Critical path = the chain of tasks with zero total float.
In use: "That task shows 15 days of total float but 0 free float — slip it and the successor's start moves even though the project end date doesn't."
Misuse: assuming a task with float is "safe" to deprioritize — high float concentrated late in a schedule is often a sign of missing successor logic, not real slack.

**Near-critical path** — A path whose total float is small enough (commonly under ~10–20% of remaining project duration, no universal standard) that normal variance could make it the new critical path.
In use: "That integration path has 4 days of float against a 6-week remaining duration — call it near-critical and watch it every cycle."
Misuse: monitoring only the critical path (0 float) and ignoring near-critical paths, which routinely flip to critical after one bad reporting period.

**RAID log (Risks, Assumptions, Issues, Dependencies)** — A single register tracking all four categories, typically scored probability × impact for risks, with an explicit cross-reference when a risk materializes into an issue.
In use: "R-014 realized into I-022 this cycle — same row lineage, new status, so the history survives for the postmortem."
Misuse: overwriting a risk row when it materializes instead of cross-referencing it as an issue, which erases the fact that it was known and scored in advance.

**Baseline tolerance** — The pre-agreed cost/schedule variance band (e.g., ±5% of BAC or ±2 weeks) within which the specialist or PM can approve a change without escalating to the sponsor or change control board (CCB).
In use: "CR-08 is $18K against a $42K tolerance — approved at my level. CR-09 is $147K — that's a CCB item."
Misuse: treating tolerance as a judgment call made case by case rather than a number fixed at the charter stage — "obviously fine" changes are exactly what tolerance is supposed to keep out of ad hoc judgment.

**Scope creep vs. gold plating** — Scope creep = unapproved scope additions that expand the baseline without a change request. Gold plating = delivering more than the specification required, unrequested, usually well-intentioned.
In use: "That's gold plating, not scope creep — nobody asked for it, but it also didn't come through a change request, so it's still untracked cost."
Misuse: assuming gold plating is harmless because it wasn't demanded by the customer — it still consumes budget and schedule outside the tracked plan, exactly like scope creep does.

**Rolling wave planning** — Planning the near-term work in detail and leaving later phases at a coarser level of definition until they're closer, refining progressively rather than fully detailing the whole plan up front.
In use: "We've got the next 6 weeks task-level, but UAT is still a rolling-wave placeholder until integration testing closes out."
Misuse: using "rolling wave" as an excuse for never detailing later phases at all — the wave is supposed to roll forward and get refined, not stay permanently vague.
