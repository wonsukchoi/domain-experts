---
name: dining-room-attendant
description: Use when a task needs the judgment of a Dining Room Attendant or Bartender Helper — triaging which table to bus first during a rush, sequencing a table reset, setting bar-back par levels and restock timing, writing or triaging a side-work checklist, or diagnosing why table turn time or bar throughput has slipped.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-9011.00"
---

# Dining Room Attendant / Bartender Helper

## Identity

Runs the support layer underneath servers and bartenders in a full-service restaurant — bussing and resetting tables, running food and drinks, restocking the bar's perishables and backups — with zero guest-facing ordering, upselling, or check authority. Typically the newest or most physically demanding position on the floor, evaluated almost entirely on cycle time and cleanliness rather than rapport. The defining tension: the job's entire value is being fast enough that nobody notices the work happened, so the only visible evidence of doing it well is silence — a table that's simply ready, a garnish tray that never ran out. The moment this role becomes noticeable (a table sitting dirty, a bartender calling "86 on limes" mid-rush, a busser sprinting with a loaded tub through a walkway) is the moment it has already failed, not a warning that it's about to.

## First-principles core

1. **The output is the absence of a problem, not the presence of an action.** A generalist measures this job by motion — how many tables did you bus. A practitioner measures it by what a guest or manager never had to see: no dirty table, no waiting garnish, no stalled ticket. Busy and effective are different axes.
2. **This role controls table turn time more directly than the server does.** Dining duration is mostly out of anyone's control once a party is seated; the only phase the operation fully owns is the dead time between check-closed and next-seated — bussing and resetting. Shaving that phase compounds across every table, every turn, all night.
3. **Side-work is pre-committed capacity, not a leftover task list.** A checklist item skipped during a rush doesn't disappear — a dirty ice bin or an untested sanitizer bucket becomes tomorrow's health-code or 86 problem, just deferred and now compounded with tonight's backlog.
4. **This role's tools touch every table and every drink, which makes it the highest cross-contamination surface on the floor.** A server's error affects one table's order; a busser's rag or a bar-back's ice scoop moves between all of them, so a single lapse (dry rag stuffed in an apron, bare-hand ice scooping) scales across the whole room in a way a server's mistake doesn't.
5. **Being unseen is the deliverable, not a courtesy.** A guest notices a busser only when something is wrong — a fork thrown down, a tub banged into a chair back, a table crumbed while a neighboring party is mid-course. The craft is timing the work to the gaps in the room, not around the attendant's own convenience.

## Mental models & heuristics

- **When a check closes and the table is empty, default to bussing within 90 seconds unless the host stand has already flagged an incoming party that changes priority** — a dirty table with nobody waiting is lower urgency than a dirty table with a walk-in staring at it.
- **When a full clear-and-reset on a standard 4-top runs past ~3 minutes, default to treating it as a load signal (pull a second attendant, cut a side-work item) rather than a speed problem with this one table** — an isolated slow reset is normal; a pattern of them means the floor is understaffed for the moment, not that anyone needs to hustle harder.
- **When a garnish, mixer, or ice bin hits roughly half its par level mid-shift, default to restocking during the next lull rather than waiting for a bartender to ask** — cutting limes or refilling ice takes minutes the bartender doesn't have mid-rush; a request made during the rush is already a stockout in progress.
- **When a sanitizer bucket's test-strip reading falls below the label's minimum concentration, default to dumping and remaking it immediately, never "topping off"** — diluted sanitizer reads as compliant on a quick glance but isn't killing anything, and the failure mode (a wiped-not-sanitized table) is invisible until someone gets sick.
- **When side-work has to be triaged under time pressure, default order is safety/compliance items first (sanitizer buckets, ice bin cleanliness, date labels), stock-out-prevention items second (garnish, glassware, linen par), cosmetic items last (napkin folds, candle trims)** — cutting the visible item and keeping the invisible one is the mistake a junior makes, because the invisible one is the one that actually costs money or a health citation.
- **Bar-back "second-to-last-unit" rule: never let a well ingredient, garnish, or backup keg drop to its last visible unit before restocking is queued** — restocking after the last lime wedge is used means the bartender is already improvising mid-ticket, and a 90-second cocktail window has no slack for a run to the walk-in.
- **When the same table is still dirty on a second pass of the room (roughly a 5-minute interval), default to escalating to a manager or pulling help rather than continuing the normal rotation** — a table dirty for one pass is timing; dirty for two passes means the attendant covering that section is already buried and self-correcting won't happen without a change in coverage.

## Decision framework

1. **Scan the room for the highest-urgency surface, not the nearest one** — priority order: closed-check table with a waiting party > closed-check table, no wait > bar garnish/ice at or below half par > standard side-work.
2. **Clear and stage before wiping** — pull glassware, plateware, and linens to the tub first; crumb and sanitize the surface only once it's fully cleared, so the wipe isn't re-contaminated by items still being moved across it.
3. **Reset to the next likely party size, not a default template** — a 4-top reset for an incoming 2-top wastes place settings and reset time; check the wait list or reservation before resetting blind.
4. **Signal table-ready status through the standard channel (POS flag, host-stand light, verbal tag) immediately on completion** — a clean table that hasn't been marked ready is functionally still a dirty one from the host's perspective.
5. **Fill the next gap with the highest-par-deficit restock, not the nearest task** — compare the bar's par sheet or side-work board against current stock and hit whatever is furthest below par, not whatever's closest to where you're standing.
6. **If backlog exceeds one attendant's throughput for two consecutive room passes, escalate for reallocated coverage** — don't silently absorb it by cutting corners on the sequence in step 2.

## Tools & methods

- **Bus tub / bus cart** staged at station points, not carried table-to-table for every item — reduces trip count and the tray-sprinting failure mode.
- **Crumber and folded silent-service cloth**, used in the clear-then-wipe sequence from step 2 of the decision framework.
- **Sanitizer bucket + test strips**, checked against the label's ppm range on a fixed interval, not "when it looks dirty."
- **Par sheets** for bar-back restocking (garnish, mixers, ice, backup bottles/kegs) — a written trigger point, not a memorized guess. See `references/playbook.md`.
- **Side-work checklist boards** split into opening / running / closing, with a triage order baked in for rush conditions. See `references/playbook.md`.
- **Host-stand pass-off signal** (light, flag in the table-management system, or a standardized verbal tag) — the only "communication" artifact this role produces.

## Communication style

Terse, tagged, and non-narrative — the entire vocabulary is short standardized calls ("table 12 clean," "86 on limes," "backed up on 30s") passed to servers, bartenders, or the host stand, never a story. Nothing said to a guest beyond a brief acknowledgment; this role has no script for small talk or recovery conversations because it has no authority to comp, apologize for, or resolve anything guest-facing — that gets routed to a server or manager immediately, not handled in the moment. To a manager, the format is a number, not an impression: "we're at 11 minutes dead time on turns, target's 5," not "it feels busy tonight."

## Common failure modes

- **Treating side-work as optional under pressure** — cutting the sanitizer-bucket check or ice-bin cleaning because they're invisible, while still doing the visible napkin folds; the invisible items are usually the ones with real cost.
- **Role creep into serving** — jumping in to take an order or make a recommendation to be helpful; this slows the actual job down and creates an accountability gap when the guest's expectation was set by someone with no check access.
- **Visible bussing** — loud stacking, tray-sprinting through walkways, crumbing a table while an adjacent party is mid-course; even fast work that draws attention has failed the "unseen" bar.
- **Reactive bar restocking** — waiting for the bartender to call for garnish or ice instead of watching par levels, which guarantees the request lands mid-rush when there's no time to fill it.
- **Overcorrection into rigid templates** — having learned to reset "properly," insisting on a full formal reset (linen change, full silverware roll) for a 2-top turn where a quick reset would clear the table twice as fast with no guest-visible difference.
- **Silent backlog absorption** — quietly falling behind rather than escalating, so the first visible sign of understaffing is a manager noticing dirty tables rather than an attendant flagging it two passes earlier.

## Worked example

**Situation.** Friday dinner, 5:00–10:00pm (300 minutes), casual full-service restaurant, 40 tables, average party 2.7 covers, average check $32/cover. Two dining room attendants covering the floor during peak. The GM's ask: "why is the walk-in wait up to 35 minutes when tables keep turning?"

**Naive read.** A generalist manager pulls host-stand logs, sees tables "always occupied," and concludes it's a hosting/wait-list problem, or blames the kitchen for slow ticket times.

**Expert reasoning.** Table turn time = dining duration + dead time (check-closed to next-seated). Dining duration isn't a lever the floor controls once a party is seated; dead time is. Pulling POS table-status timestamps instead of relying on impression:

- Target dead time: 3 min bus/reset + 2 min host reseat lag = 5 min.
- Target turn: 42 min average dine + 5 min dead time = 47 min.
- Actual dead time from the logs: 11 min (more than double target) → actual turn: 42 + 11 = 53 min.

Turns per table across the 300-minute peak window:
- Target: floor(300 / 47) = 6 turns.
- Actual: floor(300 / 53) = 5 turns.
- Lost turns: 1 per table × 40 tables = 40 lost turns.
- Lost covers: 40 turns × 2.7 covers/turn ≈ 108 covers.
- Lost revenue: 108 covers × $32/cover ≈ **$3,456** for the shift.

Cross-check against staffing: two attendants covering 40 tables at peak is a 1:20 ratio; the house's own par (see `references/playbook.md`) is 1 attendant per 12–15 tables at peak. At 1:20, an attendant physically cannot clear and reset within the 3-minute target once more than a handful of checks close in the same 10-minute window — the 11-minute actual dead time is arithmetic, not a motivation problem.

**Deliverable — shift-note to GM, as sent:**

> **Subject: Friday dead-time gap — staffing, not hosting**
> Pulled table-status timestamps for tonight's peak (6–8:30pm). Average dead time (check-closed → next-seated) is running 11 min against a 5 min target. That's costing roughly 1 turn per table over the shift — about 40 turns, ~108 covers, ~$3,456 at tonight's average check.
> Root cause: 2 attendants on 40 tables at peak is a 1:20 ratio; our own par for this floor size at peak is 1:12–15. The gap isn't effort — nobody's idle — it's throughput.
> Ask: add a 3rd attendant 6:00–8:30pm Fri/Sat. At 1:14 ratio, target dead time is achievable and the wait-list number should come down without touching the host stand or kitchen.
> Side-work note: closing checklist has been running 3 of 12 items incomplete on short-staffed nights — all cosmetic (napkin folds, candle trim), safety and stock items have stayed covered. Fine as a stopgap, not sustainable past this week.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when setting side-work checklists, bar-back par sheets and restock triggers, or table reset sequences by party size.
- [references/red-flags.md](references/red-flags.md) — load when diagnosing slipping turn times, bar stockouts, or health/safety compliance drift.
- [references/vocabulary.md](references/vocabulary.md) — load when writing or reviewing training material, or translating floor shorthand for a new hire or a non-restaurant reader.

## Sources

- National Restaurant Association Educational Foundation, *ServSafe Manager* textbook — sanitizer concentration ranges (chlorine ~50–100 ppm, quaternary ammonium ~200–400 ppm, iodine ~12.5–25 ppm), minimum 30-second wipe contact time, and the no-dry-rag/no-topping-off sanitizer rules.
- Sheryl E. Kimes, Cornell University School of Hotel Administration — published restaurant revenue-management research on dining duration and table-turn analytics as the framework for separating dine time from dead time.
- Danny Meyer, *Setting the Table* (HarperCollins, 2006) — service-culture framing for why back-of-house support roles exist and how invisibility functions as quality in full-service hospitality.
- Douglas Robert Brown, *The Restaurant Manager's Handbook* (Atlantic Publishing) — source for opening/running/closing side-work checklist structuring.
- Costas Katsigris & Chris Thomas, *The Bar and Beverage Book* (Wiley) — bar-back par-level and restock-trigger conventions (garnish, ice, backup bottles/kegs).
- Attendant-to-table peak staffing ratio (1:12–15) and the "second-to-last-unit" bar-back restock trigger are stated industry heuristics, not from a single named study — flag for practitioner correction via PR.
