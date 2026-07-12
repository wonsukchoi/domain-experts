# Playbook

## Task-boundary quick check, by trade

Helper-cleared vs. escalate-to-journeyworker, for the tasks that actually come up daily. Not exhaustive — when a task isn't on this list, default to asking before starting.

| Trade | Helper-cleared | Escalate (licensed-only) |
|---|---|---|
| Electrical | Rough-in conduit/box mounting, wire pulls to length, like-for-like device swap under state exemption, cable stripping/labeling, temporary lighting setup | Panel landings, breaker sizing/selection, service work, anything inside an energized panel, circuit tracing for troubleshooting |
| Plumbing | Pipe cutting/measuring/staging, fixture unboxing/prep, trench/access prep, insulation wrap, drain snaking (non-main) | Gas line joints, water-service connections, backflow-preventer work, main-line repair, any permit-triggering DWV alteration |
| HVAC | Ductwork staging/hanging, filter/coil access prep, condensate line rough-in, equipment uncrating and rigging | Refrigerant circuit work (EPA Section 608), gas furnace ignition/valve work, electrical control wiring inside the unit |
| Elevator | Material staging, rail/track cleaning, pit housekeeping, non-energized component transport | Controller wiring, hydraulic/traction system adjustment, any work inside the machine room on energized equipment |

## Staggered-pipeline scheduling template

Use when the helper's rough-in output feeds directly into the journeyworker's licensed step, to avoid the batching trap (finish everything, then hand off, with zero slack).

| Run | Helper start | Helper done | Journeyworker start | Journeyworker done |
|---|---|---|---|---|
| Prep/take-off | 0 | 30 | 0 (own prep) | 40 |
| Run 1 | 30 | 70 | max(70, 40) = 70 | 100 |
| Run 2 | 70 | 110 | max(100, 110) = 110 | 140 |
| Run 3 | 110 | 150 | max(140, 150) = 150 | 180 |
| Run 4 | 150 | 190 | max(180, 190) = 190 | 220 |
| Run 5 | 190 | 230 | max(220, 230) = 230 | 260 |
| Run 6 | 230 | 270 | max(260, 270) = 270 | 300 |
| Final test/label | — | — | 300 | 330 |

Rule: journeyworker start time on run *n* = max(previous journeyworker finish, helper finish on run *n*). If the max is consistently the helper's finish time, the helper is the bottleneck — shift more prep to the journeyworker's idle window or add a second helper. If the max is consistently the journeyworker's previous finish, the helper is running ahead — safe to have them start next-day staging or non-blocking cleanup instead of idling.

## Material take-off worksheet (filled example)

| Item | Measured/counted | Waste factor | Order quantity |
|---|---|---|---|
| EMT ½" conduit | 240 ft (6 runs: 35+38+40+42+45+40) | +10% | 270 ft (27× 10-ft sticks) |
| EMT connectors | 12 (2 per run × 6) | none | 12 |
| EMT couplings | 12 (2 per run × 6, worst case) | none | 12 |
| THHN 12 AWG | 720 ft (240 ft × 3 conductors) + 72 ft tails (6 ft × 2 ends × 6 circuits) = 792 ft | round up to reel size | 1,000-ft reel |
| 4×4 boxes w/ mud ring | 6 (1 per run) | none | 6 |
| 20A single-pole breakers | 6 (1 per circuit) | none | 6, plus 1 spare on truck stock |

Verify every row against the drawing and the panel schedule before cutting — a take-off error surfaces as a blocked journeyworker hours later, not as an obvious mistake at the moment it's made.

## OJT hour-log categories (example set, electrical)

| Code | Category | Typical daily tasks |
|---|---|---|
| 1.4 | Material take-off & ordering | Measuring runs, verifying pull lists, placing orders |
| 3.2 | Rough-in wiring methods | Conduit runs, box mounting, wire pulls |
| 3.5 | Device installation (non-panel) | Like-for-like swaps under state exemption |
| 5.1 | Panel work (observed/assisted) | Time spent directly assisting a landing, not performing it |
| 6.1 | Jobsite safety & housekeeping | LOTO setup/removal (when authorized), egress clearance, PPE checks |
| 7.3 | Blueprint reading | As-built comparison, drawing markup |

Log same-day, against the task actually performed that block of time — not the trade in general. A day split across three categories logs as three line items, not one rounded total.

## Jobsite handoff / escalation note template (filled)

> **Jobsite handoff — [site name], [date]**
> Rough-in complete: [circuits/runs list], [material and quantity installed].
> Landings/testing: [journeyworker name] complete, [what was tested], [what was updated — panel directory, labeling].
> **Flag:** [what was found] at [location], not on [drawing reference]. Not touched, area isolated. [Journeyworker] inspected [time]; [change order/no action needed]; [customer notified by whom].
> **OJT hours logged today:** [X.X hrs Category name (Code)], [X.X hrs Category name (Code)]. Total [X.X] hrs — week [N] of [program total] toward journeyworker hours.

Keep every field factual and specific — a vague flag line ("found some old wiring, told the boss") is the version that turns into a dispute with the GC three weeks later when nobody can reconstruct exactly what was found, where, or when.
