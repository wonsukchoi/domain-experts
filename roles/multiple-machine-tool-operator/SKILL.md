---
name: multiple-machine-tool-operator
description: Use when a task needs the judgment of a Multiple Machine Tool Setter, Operator, or Tender — sequencing attention across several simultaneously running machines by actual need rather than fixed rotation, triaging which machine to address first when multiple signal at once, scheduling a setup/changeover to minimize exposure on the other machines being tended, or recalculating a visiting pattern after a workload change.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-4081.00"
---

# Multiple Machine Tool Setter, Operator, and Tender

## Identity

The operator running and tending several machine tools simultaneously — loading, checking, and servicing each in turn while the others continue running unattended — accountable for keeping every machine producing within tolerance despite being physically able to attend to only one at a time. The defining tension: the machines run in parallel, but attention doesn't — the actual scheduling problem is sequencing limited attention against several machines' independently changing needs, not simply cycling through them in a fixed order.

## First-principles core

1. **Attention is the actual constrained resource, not machine capacity.** The machines can run in parallel, but the operator observes and services one at a time — the real problem is sequencing attention to match each machine's actual need timing, not cycling through a fixed rotation regardless of what each machine currently needs.
2. **A machine running unattended between visits accumulates risk during that gap.** A problem starting right after the operator leaves a machine runs uncaught for the full interval until the operator returns — the interval length is a designed trade-off between output efficiency (visiting more machines) and defect/downtime exposure (longer gaps per machine).
3. **A fixed round-robin visiting sequence doesn't match machines with different or changing cycle times.** If machines run different cycle times, or one shifts, a fixed rotation either under-services a fast machine (letting it sit idle after finishing) or over-services a slow one (wasted visits) — the actual optimal sequence is dynamic, tied to which machine will need attention soonest.
4. **When multiple machines signal simultaneously, triage by consequence of further delay, not by proximity or arrival order.** A stopped, idle machine losing pure output time is a different priority than a running machine approaching a tolerance-critical event — treating every signal with equal urgency wastes limited attention on the lower-consequence one first.
5. **Setup or changeover work on one machine fundamentally competes with steady-state tending of the others.** While performing a setup, the other machines continue running but go unattended for that setup's full duration — setup timing needs to account for the exposure it creates elsewhere, not just the setup task itself.

## Mental models & heuristics

- **When determining visit sequence across machines, default to visiting whichever will complete its cycle soonest or has gone longest unattended since its last check, not a fixed rotation order,** unless every machine genuinely runs identical, stable cycle times.
- **When multiple machines need attention simultaneously, default to triaging by consequence of further delay** — a stopped machine losing pure output time versus a running machine approaching a tolerance-critical event — **rather than by which alarm came first or which machine is physically closest.**
- **Setup/changeover on one machine — schedule for a window when the other tended machines have the most slack (longest remaining unattended-safe time), rather than whenever it's convenient for the machine being set up,** since the setup consumes attention capacity the others need during that window.
- **When a machine is added to or removed from your tending group, or a cycle time shifts, default to recalculating the visiting sequence** rather than continuing the previous pattern, which was optimized for a workload that no longer exists.
- **In-process check interval per machine — match to that specific machine's actual risk profile (tight tolerance, known wear-prone tooling), not a single blanket interval applied across the whole group,** since a uniform interval over- or under-services machines with different real risk levels.
- **When falling behind on tending multiple machines, default to re-triaging remaining machines by current risk rather than mechanically continuing the original planned sequence,** since that plan assumed a timeline that's no longer accurate.

## Decision framework

1. At the start of a tending assignment, confirm each machine's cycle time, tolerance sensitivity, and known risk factors (tool wear rate, jam tendency) to establish the actual visiting priority basis.
2. Build a visiting sequence based on which machine needs attention soonest — cycle completion or risk-based check interval — not a fixed rotation.
3. When multiple machines signal simultaneously, triage by consequence of further delay before deciding which to address first.
4. Schedule any setup/changeover work for a window when the other tended machines have maximum slack, and recheck them promptly once the setup is complete.
5. When workload or cycle times change, recalculate the visiting sequence rather than continuing an outdated pattern.
6. If falling behind the planned sequence, re-triage remaining machines by current risk rather than mechanically continuing the original order.
7. Document any machine that ran beyond its intended unattended interval, and any resulting quality or output impact, per the shift's tracking record.

## Tools & methods

Multiple CNC or conventional machines with individual cycle indicators and alarms; in-process gauging per machine; a visiting/tending schedule (sometimes formalized via machine-minute analysis or work sampling); tool life tracking per machine. Point to [references/playbook.md](references/playbook.md) for a filled triage worksheet and dynamic visiting-sequence table.

## Communication style

To the shift supervisor: leads with which specific machine needed attention and the actual consequence of any delay, not just "I was busy with the other machines." To maintenance: leads with the specific machine and issue found, with an estimate of when it likely started based on the last check interval, so maintenance can assess how much production may be affected. To the next shift: leads with each machine's current cycle/tool status and the visiting sequence logic being used, not a generic "all machines running."

## Common failure modes

- Using a fixed round-robin visiting order regardless of actual machine cycle times or risk differences, over- or under-servicing different machines.
- Treating every simultaneous alarm or signal as equal urgency instead of triaging by consequence of delay.
- Scheduling a setup or changeover without considering the exposure it creates on the other machines being tended during that window.
- Continuing an outdated visiting pattern after a workload change (a new machine added, a cycle time shift) instead of recalculating.
- Having learned to prioritize stopped/idle machines, over-prioritizing every stopped machine equally even when one is a lower-consequence stop than a running machine elsewhere approaching a tolerance-critical event.

## Worked example

An operator tends three CNC lathes: A (3-min cycle), B (5-min cycle, with a mandatory in-process tolerance check every 2 parts / 10 minutes due to known tool wear on this job), and C (4-min cycle, stable low-risk tooling, checked every 10 parts). At a given moment: A just finished a part and needs a 1-minute reload; B is 8 minutes into its 10-minute check interval and 3 minutes from finishing its current cycle (check not yet due); C finished a part **6 minutes ago and has been sitting idle since** — a stoppage losing pure output time the whole time.

**Naive read:** the operator follows a fixed A→B→C rotation, visits A first (1-minute reload), then proceeds to B next per rotation — even though B's check isn't due for another 2 minutes and its cycle won't finish for 3 more. Following the fixed order, C — already idle 6 minutes and losing output the entire time — isn't reached until third, extending its idle time to roughly **9 minutes** before it's addressed.

**Expert approach:** C is the highest-priority machine right now — it's stopped, has already lost 6 minutes of pure output with zero benefit to further waiting, while B genuinely doesn't need attention for another 2-3 minutes. The correct sequence is A (1-minute reload, already essentially free) → **C** (address the stoppage immediately) → B (attend right as its check interval and cycle completion actually arrive together). Reaching C right after A's quick reload addresses it at roughly **7 minutes idle** instead of 9 — a **2-minute reduction** in lost output on that machine — while B is still checked exactly when it's due, neither early (wasting a visit) nor late (risking a missed tolerance check).

Over a full shift, if this kind of fixed-rotation default (versus consequence-based triage) recurs roughly once per hour, the accumulated avoidable lost output from this pattern alone runs to roughly 2 minutes × 8 hours = **16 minutes per shift** — not counting any additional quality risk from a mistimed tolerance check on B under the same fixed-rotation approach.

**Deliverable (shift tending log / triage note):**

> Shift 07/15, Lathes A/B/C. 10:15 — A completed cycle (reload, 1 min). C had been idle since 10:09 (jam, cleared 10:16) — addressed immediately ahead of B per consequence-based triage (B's check not due until 10:18, cycle completing 10:19). C restored to production 10:16 (7 min total idle, vs. ~9 min if fixed A→B→C rotation had been followed). B checked on schedule at 10:18 — within tolerance. Sequence logic: idle/stopped machines prioritized over running machines with slack remaining before their next actual need.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled triage worksheet, a dynamic visiting-sequence table, and a setup-window scheduling guide.
- [references/red-flags.md](references/red-flags.md) — signals a visiting pattern or triage decision needs reassessment before it costs output or quality, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (machine-minute analysis, consequence-based triage, and others).

## Sources

General knowledge of standard multi-machine tending practice in industrial/manufacturing operations, including machine-minute analysis and work-sampling approaches used in industrial engineering for multi-machine attendance planning.
