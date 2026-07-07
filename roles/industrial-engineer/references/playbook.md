# Industrial Engineer Playbook

## Line-balance worksheet (filled)

| Task | Predecessor | Element time (s) | Assigned station |
|---|---|---|---|
| T1 | — | 35 | St.1 |
| T2 | T1 | 30 | St.1 |
| T3 | T2 | 25 | St.2 |
| T4 | T3 | 40 | St.2 |
| T5 | T4 | 20 | St.3 |
| T6 | T5 | 45 | St.3 |

Takt time = available time ÷ demand. Theoretical minimum stations = ceil(total work content ÷ takt). Assign tasks to the running station in precedence order until the next task would push the station over takt; open a new station; repeat. Never split an indivisible task across two stations without a shared-fixture or dual-handling justification — that's a fixture-cost decision, not a balancing one.

Line efficiency = total work content ÷ (station count × cycle time). Below 85% on a newly balanced line, check whether precedence constraints (not station count) are the binding limit — if so, the fix is resequencing the process, not adding stations.

## Time-study worksheet (filled, 12-cycle observation)

| Cycle | Observed time (s) | Rating | Rated time (s) |
|---|---|---|---|
| 1-12 avg | 38.4 | 1.10 | 42.2 |

Standard time = rated time × (1 + PFD allowance). PFD (personal/fatigue/delay) allowance: 5% personal + 4% fatigue (light assembly, standing) + 6% unavoidable delay = 15% total.

Standard time = 42.2 × 1.15 = **48.5 seconds/unit.**

Rating scale reference (Westinghouse system, illustrative): 1.00 = normal/average pace; 1.10-1.20 = fast/skilled; 0.80-0.90 = slow/unskilled. An observed average with no rating applied silently assumes the observed operator worked exactly at rating 1.00 — rarely true and never verifiable after the fact.

## Systematic Layout Planning (SLP) relationship chart (filled, 6 departments)

| | Receiving | Sub-assembly | Final assembly | Paint | QA | Shipping |
|---|---|---|---|---|---|---|
| Receiving | — | A | U | U | U | X |
| Sub-assembly | A | — | A | U | U | X |
| Final assembly | U | A | — | E | A | I |
| Paint | U | U | E | — | I | O |
| QA | U | U | A | I | — | A |
| Shipping | X | X | I | O | A | — |

Rating scale: A = absolutely necessary adjacency, E = especially important, I = important, O = ordinary closeness okay, U = unimportant, X = undesirable (keep apart). Layout candidates are scored by summing weighted adjacency scores against the actual floor plan; the highest-scoring feasible layout wins, not the one that "feels" right from walking it once.

## OEE breakdown (filled, one line, one shift)

| Metric | Formula | Value |
|---|---|---|
| Availability | run time ÷ planned production time | 405 min ÷ 450 min = 90.0% |
| Performance | (ideal cycle time × total count) ÷ run time | (65s × 350 units) ÷ 24,300s = 93.6% |
| Quality | good units ÷ total units | 340 ÷ 350 = 97.1% |
| **OEE** | Availability × Performance × Quality | **82.0%** |

World-class OEE is commonly cited as ~85%; a line under 60% almost always has an availability problem (unplanned stops), not a performance or quality problem — pull the downtime log before touching the balance.

## SMED changeover reduction (filled, before/after)

| Step | Before (internal, min) | After conversion | After (external/internal, min) |
|---|---|---|---|
| Fetch next-job fixture | 8 | moved external (pre-staged) | 0 |
| Swap fixture | 12 | stays internal | 12 |
| Adjust and verify first-piece | 15 | reduced via locating pins | 6 |
| Total changeover | 35 | | 18 |

Internal = must happen with the line stopped; external = can happen while the line is still running the prior job. The single highest-leverage SMED move is converting internal steps to external — it requires no faster hands, only different sequencing.
