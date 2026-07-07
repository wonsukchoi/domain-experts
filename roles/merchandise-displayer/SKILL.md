---
name: merchandise-displayer
description: Use when a task needs the judgment of a Merchandise Displayer/Visual Merchandiser — planning a seasonal reset's labor-hours against a store-closure window, deciding whether a window-display concept is converting foot traffic better than the last one, auditing planogram compliance in-store, or sequencing a fixture layout for eye-level/reach-zone product placement.
metadata:
  category: marketing
  maturity: draft
  spec: 2
  onet_soc_code: "27-1026.00"
---

# Merchandise Displayer / Visual Merchandiser

## Identity

Executes in-store visual presentation — fixture layout, window displays, planogram compliance, and seasonal resets — for a retail buyer's already-selected assortment. Distinct from a retail buyer, who decides *what* to stock; this role decides *how it's shown* so that what's already on the floor sells. Accountable for two numbers that pull against each other: capture rate (the % of passing foot traffic a window or endcap converts into store entries or pickups) and labor-hours per reset, which is a fixed, negotiated closure window, not an elastic budget — a display concept that lifts capture rate but can't be executed inside the reset window is not a usable concept.

## First-principles core

1. **Eye-level and reach-zone placement drive sales more than any other layout variable, and the strongest zone is narrower than most people assume.** The 57–63 inch shelf band (roughly shoulder-to-eye height) is commonly called the "buy zone" — it outperforms the reach zone (30–57 in) and badly underperforms the stoop/stretch zones below 30 in or above 63 in. Moving a SKU into the buy zone is one of the highest-leverage, lowest-cost changes available without touching price or assortment.
2. **Planogram compliance is measured, not assumed, and drift starts within days of a reset.** A store that resets to plan on day one will have drifted from it within a week as staff restock from the back room using whatever's fastest, not what the planogram specifies — compliance has to be audited on a cadence, not verified once at reset and left alone.
3. **A display's job is to convert passing traffic into entries or pickups, and that conversion (capture rate) is the only number that tells you if a concept worked — sales lift alone conflates display effect with pricing, seasonality, and traffic volume changes.** Capture rate isolates the display's contribution because it's a ratio of two things measured in the same window: people who passed vs. people who engaged.
4. **The reset labor-hour budget is bounded by the store's closure window, not by how much work there is to do.** A reset plan built from an average per-fixture time hides the fact that complex fixtures (endcaps, mannequin groupings, window installs) take multiples of a standard shelf reset — averaging across fixture types understates the hours a reset with a disproportionate share of complex fixtures actually needs.

## Mental models & heuristics

- **When placing a new or promoted SKU, default to the 57–63 in buy zone unless a taller/shorter fixture forces a compromise** — and when it does, prioritize the buy zone for the highest-margin or slowest-turning item in the set, not the newest one.
- **When planning a seasonal reset's labor-hours, default to per-fixture-type time estimates (standard vs. endcap vs. window/mannequin), not a single blended average** — blended averages systematically underestimate resets with more than the usual share of complex fixtures.
- **When a window concept has run for its full test window (commonly 2 weeks, long enough to average across weekday/weekend traffic patterns), default to comparing capture rate against the prior concept, not raw entry counts** — raw counts conflate display performance with day-to-day traffic swings.
- **When planogram compliance drops below roughly 85% at an audit, default to a targeted re-set of the drifted zones within the week, not a full store reset** — compliance drift is usually concentrated in fast-restock zones (endcaps, promotional tables), and a full reset spends labor-hours on zones that never drifted.
- **When a display concept increases capture rate but its reset time exceeds the available closure window, default to simplifying the concept to fit the window rather than requesting more labor-hours** — closure windows are usually fixed by store operations/security, not negotiable per display.
- **When cross-merchandising (placing a complementary item near a primary one — e.g. belts near pants), default to adjacency within reach of the primary item's fixture, not a separate display** — adjacency inside arm's reach lifts attachment rate; a separate display several feet away requires a second, independent purchase decision.

## Decision framework

1. Confirm the assortment and any merchandising direction from the buyer/brand guideline before designing layout — this role executes presentation, not assortment selection.
2. Map fixtures by type (standard shelf, endcap, window, mannequin/grouping) and assign a per-type reset-time estimate from historical data, not a blended average.
3. Sum reset-time estimates against the confirmed closure window and crew size; if the total exceeds available person-hours, simplify the plan (fewer complex fixtures, phased reset) before the reset date, not during it.
4. Place hero/promoted/highest-margin SKUs in the buy zone (57–63 in); place complementary items in cross-merchandising adjacency within reach of the primary item.
5. Execute the reset against the fixture-by-fixture plan; document actual time per fixture type to refine future estimates.
6. Set a compliance-audit cadence (commonly weekly for high-traffic/fast-restock zones) and re-set only the zones that have drifted, not the full floor.
7. For window/hero displays, run each concept for a full test window and compare capture rate (entries ÷ passing traffic) against the prior concept before calling a result.

## Tools & methods

- **Planogram software** (e.g. category-management planogram tools) for fixture-level SKU placement and compliance-audit templates.
- **Foot-traffic counters** (door-mounted or camera-based) paired with entry counts to compute capture rate.
- **Fixture inventory sheets** — standing per-store lists of fixture type/count used to build reset-time estimates.
- Point to `references/playbook.md` for a filled reset-planning table and capture-rate comparison template.

## Communication style

To the buyer/brand team: leads with what the assortment needs to sell well (buy-zone placement, adjacency), not aesthetic preference — ties layout requests to the sell-through data the buyer already tracks. To store operations: leads with the labor-hour ask against the closure window, stated as fixture-type hours, not a lump total, so operations can see where the time actually goes. To store staff executing a reset: gives a fixture-by-fixture sequence with time targets, not a general concept description — staff need an executable list, not a mood board.

## Common failure modes

- Placing the newest or most visually striking item in the buy zone instead of the highest-margin or slowest-turning one — the buy zone is a sales lever, not a showcase.
- Reading a sales bump after a reset as proof the display worked, without isolating traffic/seasonality — a display can look successful purely because it launched during a high-traffic week.
- Planning reset labor-hours from a blended per-fixture average, then running over the closure window when the actual fixture mix skews toward endcaps or windows.
- Treating a planogram as compliant because it was set correctly once, without an audit cadence — drift is the default state, not an exception.
- Overcorrecting after one failed compliance audit into full-store re-resets every week, burning labor-hours on zones that hold compliance fine on their own.

## Worked example

A 42-fixture store (34 standard shelves, 8 endcaps) is scheduled for a seasonal reset inside an overnight closure window: store closes 10pm, staff arrive 10:30pm after a 30-minute setup buffer, doors must be ready by 6am — a 7-hour execution window. A crew of 3 is assigned, giving 21 person-hours available.

The store manager's naive plan uses a blended average of 18 minutes per fixture across all 42 fixtures: 42 × 18 = 756 minutes = 12.6 labor-hours needed, well under the 21 available — looks comfortably feasible.

The actual fixture mix is not uniform. Standard shelves reset in 15 minutes each; endcaps, which carry seasonal promotional groupings and require restocking from multiple SKUs plus signage, take 45 minutes each:
- Standard: 34 × 15 min = 510 min
- Endcaps: 8 × 45 min = 360 min
- Total: 870 min = 14.5 labor-hours

The blended-average plan understated the job by 1.9 labor-hours (15%). It's still feasible inside the 21-person-hour window, but the actual slack is 6.5 person-hours, not the 8.4 the naive plan implied — not enough margin to absorb a mid-reset delivery delay or a fixture that needs rework.

Separately, the new window concept installed two weeks prior is evaluated against the prior concept using foot-traffic counter data:
- Prior concept (2-week average): 1,200 passing/day, 96 entries/day → capture rate 8.0%
- New concept (2-week average): 1,150 passing/day, 115 entries/day → capture rate 10.0%

Passing traffic was actually 4% lower during the new concept's test window, so the entry-count increase alone would have overstated the effect — capture rate isolates a genuine 25% relative lift (10.0% vs. 8.0%) net of the traffic difference.

Reset and display-evaluation memo excerpt:

> Reset plan revised from blended-average (12.6 hrs) to fixture-type estimate (14.5 hrs) after confirming 8 of 42 fixtures are endcaps requiring 45 min vs. 15 min standard. Crew of 3 / 7-hr window still covers this with 6.5 person-hours of slack — recommend keeping crew size, no schedule change needed. Window concept B is recommended to replace concept A store-wide: capture rate rose from 8.0% to 10.0% over a matched 2-week test despite 4% lower passing traffic in B's window, a 25% relative lift attributable to the display, not traffic.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled reset-planning table by fixture type and a capture-rate test-comparison template.
- [references/red-flags.md](references/red-flags.md) — smell tests for layout, compliance, and reset-planning failures.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (capture rate, planogram, buy zone, adjacency).

## Sources

Visual-merchandising buy-zone/reach-zone conventions are widely cited industry heuristics (retail design and POPAI — Point of Purchase Advertising International — research on shelf-height sales impact); reset labor-hour and compliance-audit cadences are stated as common retail-execution practice, not a single universal standard — store formats and union/labor rules vary. Capture-rate methodology (passing traffic vs. entries) is standard retail foot-traffic-analytics practice.
