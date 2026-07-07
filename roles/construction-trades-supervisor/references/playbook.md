# Playbook

Filled templates and worked calculations a foreman actually runs on-site. Adapt the numbers to the job; keep the structure.

## 1. Daily labor-unit tracking sheet

Reconciled every morning before assigning today's work — this is the leading indicator that beats the master schedule by days.

| Date | Crew | Task | Budgeted rate (unit/crew-hr) | Crew-hrs worked | Budgeted output | Actual output | % of budget | Action |
|---|---|---|---|---|---|---|---|---|
| Mon | Drywall (3) | Hang 5/8" FR board | 225 SF | 8 | 1,800 SF | 1,100 SF | 61% | Flag — investigate |
| Tue | Drywall (3) | Hang 5/8" FR board | 225 SF | 8 | 1,800 SF | 1,100 SF | 61% | Root-cause: stairwell staging |
| Wed | Drywall (3+1 laborer) | Hang 5/8" FR board | 225 SF | 8 | 1,800 SF | 1,780 SF | 99% | Fixed — laborer pre-staging material |
| Thu | Concrete finish (4) | Slab flatwork | 12 CY/crew-hr | 6 | 72 CY | 68 CY | 94% | Within normal variance |

**Trigger rule:** two consecutive days below ~80% of budget escalates from "watch" to "root-cause today" — do not let a third day pass on the same unexplained variance.

**Root-cause categories to check, in this order** (cheapest to verify first): material staging/travel distance, crew mix (wrong skill ratio for the task), access/interference from another trade, rework from a prior defect, genuine underestimate in the original budget. Only the last one justifies revising the budget rather than fixing the site condition.

## 2. Competent-person designation checklist

Filled per OSHA-triggered condition, signed daily — this is the individual's personal liability record, kept independent of the general site safety log.

| Date | Task/location | Trigger condition | Designated competent person | Inspection completed | Notes |
|---|---|---|---|---|---|
| Mon | Trench, north utility run | Excavation >5 ft (1926.651) | J. Alvarez (foreman) | Yes, 6:45am, before entry | Sloped per Type B soil, no water intrusion |
| Mon | 3rd-floor edge, no guardrail yet | Fall protection zone >6 ft (1926.501) | J. Alvarez (foreman) | Yes, 7:00am | Guardrail installed by 9am; zone re-inspected before removing PFAS |
| Tue | Trench, north utility run (day 2) | Excavation >5 ft (1926.651) | J. Alvarez (foreman) | Yes, 6:40am | Same excavation as Monday — re-inspected anyway, overnight rain noted, added additional shoring |
| Wed | Scaffold, west elevation | Erection/dismantling | R. Kim (scaffold-competent, certified) | Yes, 7:10am | Different person than excavation — designation is per-task, not per-site |

**Rule:** a condition unchanged since yesterday still gets today's dated signature. "Same as yesterday" is a description of the site, not a substitute for the inspection.

## 3. Trade-sequencing conflict log

Logged the moment a space conflict surfaces, resolved same-day, referenced at the next huddle so it isn't relitigated.

| Date | Space | Trade A ask | Trade B ask | Which deadline is harder | Call | Outcome |
|---|---|---|---|---|---|---|
| Thu | 3rd-floor corridor wall, 250 SF section | Electrician: hold open 8–11am for conduit | Drywall: close today for tomorrow 8am fire inspection | Electrician's 1pm re-inspection slips 1 week if missed; fire inspection reschedules same-week | Hold for electrician 8–11am, drywall closes after 11am | Both deadlines met; drywall covered gap with 1 hr approved OT |
| Fri | Mechanical room, ceiling grid | Plumber: needs grid open for overhead rough-in | Ceiling sub: on schedule to install grid today | Plumber's rough-in blocks the fire-sprinkler rough-in scheduled Monday; ceiling install has 4 days of float before it's on critical path | Plumber goes first; ceiling grid moves to Monday | No critical-path impact; logged in look-ahead |

**Rule for the "which deadline is harder" column:** prefer the deadline that is externally fixed and non-repeating (an inspector's calendar, a one-time delivery window, an occupancy date) over one that is internally set and reschedulable. When both are genuinely fixed and in conflict, that's an escalation to the superintendent, not a foreman-level call.

## 4. Crew-sizing-by-delivery-rate calculator

Used whenever a crew's work is fed by an external delivery or placement rate rather than self-paced task work.

**Formula:** required crew size = delivery/placement rate ÷ per-worker output rate.

**Worked example — concrete flatwork:**
- Pump delivers concrete at 60 CY/hour (rated pump output for the mix and line size in use).
- One finisher can keep pace with roughly 12 CY/hour of finishing work (stated heuristic, order-of-magnitude for float/bull-float finishing on a slab, not a quoted rate).
- Required finishers = 60 ÷ 12 = **5**.
- Crewing 3 finishers against a 60 CY/hour pour means the leading edge starts setting before it's finished — cold-joint and surface-defect risk, not a productivity problem solvable by working faster. Crewing 7 finishers against the same 60 CY/hour pour doesn't finish the slab any faster; the pump rate is still the ceiling.

**Same logic applied to material handling:** a hanging crew's throughput is capped by how fast board reaches the point of installation, not by how fast the hangers can hang — which is why the Section 1 drywall fix was one laborer added to staging, not a fourth hanger added to the crew.

## 5. Near-miss tally against the accident-ratio benchmark

Tracked monthly as its own metric, separate from the recordable-incident count, specifically to catch a reporting-culture collapse rather than to celebrate a low number.

| Month | Recordable incidents | Near-misses reported | Expected near-misses at ~1:30 ratio (Bird, conservative end) | Flag |
|---|---|---|---|---|
| Jan | 0 | 14 | — | Reporting active, no flag |
| Feb | 0 | 11 | — | Within normal range |
| Mar | 1 (minor, first aid) | 9 | ~30 (per minor incident, Bird ratio) | Under-reporting suspected — near-miss count should rise around a recorded minor injury, not stay flat |
| Apr | 0 | 2 | — | Reporting culture flag — investigate whether near-miss cards are being filed or discouraged before assuming the site got safer |

**Rule:** a sharp drop in near-miss reports with no corresponding drop in actual hazard exposure (same tasks, same crew, same conditions) is itself the finding — reopen the toolbox talk on "why we report" before treating the low number as good news.
