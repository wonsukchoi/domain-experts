# Playbook

## Triage worksheet

Fill at the moment multiple machines need a visiting decision.

| Machine | Status | Time since last visit | Time to next need (cycle/check) | Consequence of further delay | Priority order |
|---|---|---|---|---|---|
| A | Just finished cycle | — | Ready now (1-min reload) | Low (quick, brief) | 1 |
| B | Running, mid-cycle | 8 min into 10-min check interval | 2 min until check due, 3 min until cycle done | Moderate — check due soon, tool wear risk | 3 |
| C | Idle/stopped | 6 min since last output | N/A — needs immediate attention | HIGH — pure output loss accumulating | 2 |

**Rule:** priority order follows consequence of further delay, not arrival order or physical proximity. A stopped machine losing pure output typically outranks a running machine that still has slack before its next actual need — unless the running machine's need is a hard, imminent tolerance/safety event.

## Dynamic visiting-sequence table (recalculate whenever conditions change)

| Trigger for recalculation | Action |
|---|---|
| New machine added to tending group | Recalculate full sequence based on new group's cycle times and risk profiles |
| Machine's cycle time observed to shift | Update that machine's position in the sequence logic |
| A machine develops a new risk factor (tool wear noticed, material change) | Tighten that machine's check interval; recalculate sequence priority |
| Operator falls significantly behind planned sequence | Re-triage ALL remaining machines by current status, don't resume the original plan blindly |
| Setup/changeover required on one machine | Check remaining slack on all other machines before starting; schedule for maximum-slack window if possible |

## Setup-window scheduling guide

1. Before starting a setup/changeover on any machine, check the current cycle status of every other machine in the tending group.
2. Identify the window where other machines have the most slack (longest remaining time before their next check/completion).
3. If no good window exists (all machines need attention soon), consider whether the setup can be delayed briefly, or flag to supervisor that simultaneous coverage may be needed.
4. Once setup begins, treat it as consuming full attention — don't assume partial attention can still cover other machines during the setup.
5. Immediately after setup completion, check every other machine's status to catch anything that developed during the exposure window before resuming normal sequence.
