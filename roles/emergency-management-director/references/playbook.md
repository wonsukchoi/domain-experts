# Emergency management playbook — filled sequences

Executable sequences with real numbers, not descriptions of sequences. Scenario used throughout: Bayshore County (pop. 310,000, coastal), Hurricane Delia, Category 3 landfall.

## 1. EOC activation levels and staffing triggers

| Level | Trigger | EOC staffing | Typical duration |
|---|---|---|---|
| Level 3 (monitoring) | Tropical storm watch issued, landfall 72–96 hrs out | EM duty officer + on-call Section Chiefs (virtual) | Ongoing until upgraded/stood down |
| Level 2 (partial activation) | Hurricane watch issued, landfall 48–72 hrs out | Operations, Planning, Logistics Section Chiefs physically staffed; Finance/Admin on-call | 12-hr shifts, 2 shifts/day |
| Level 1 (full activation) | Hurricane warning issued, landfall <48 hrs, or post-landfall response | All ICS positions staffed, Unified Command seated (county EM, Sheriff, Fire, Public Works, state liaison) | 24/7, 12-hr operational periods until stabilized |

Downgrade rule: do not drop from Level 1 to Level 2 until the first full damage assessment cycle is complete and shelter population has stabilized for 2 consecutive operational periods — downgrading on elapsed time alone loses situational awareness right when PDA fieldwork needs full staffing.

## 2. Shelter sizing worksheet

```
Input: Zone A population subject to mandatory evacuation = 42,000
Step 1 — general shelter demand:
  42,000 × 10% compliance rate = 4,200 people
  4,200 × 40 sq ft/person (post-2020 congregate standard) = 168,000 sq ft
Step 2 — functional/access-needs demand (subset, does NOT reduce Step 1):
  4,200 × 5% = 210 people
  210 × 60 sq ft/person (medical cot + equipment clearance) = 12,600 sq ft
Step 3 — pet-friendly co-located demand (subset, separate wing, same building preferred):
  4,200 × 15% bring a pet = 630 people, no incremental sq ft if co-located
  in same structure with a partitioned area; budget 1 additional staff FTE
  per 100 pet-owning evacuees for animal control liaison
Step 4 — capacity check against available sites:
  3 primary sites × 55,000 usable sq ft = 165,000 sq ft
  Required (Step 1 only) = 168,000 sq ft → shortfall 3,000 sq ft
  Decision: activate 1 overflow site (≥3,000 sq ft, ideally ≥15,000 for margin)
  rather than opening additional full sites and diluting staffing
```

Staffing ratio: 1 shelter manager + 1 assistant per 200 general-population evacuees, 1 medical staff (RN or paramedic minimum) per 20 functional-needs evacuees.

## 3. Resource request escalation sequence

1. **Internal reallocation** — pull from county departments not currently tasked (0–4 hrs to mobilize).
2. **Local/regional mutual aid** — pre-signed agreements with neighboring counties (4–12 hrs to mobilize, no separate approval needed if agreement is pre-executed).
3. **State resources / state EM agency** — requested through the state EOC, typically 12–24 hrs.
4. **EMAC (Emergency Management Assistance Compact)** — out-of-state resources; budget 24–72 hrs from request to boots-on-ground, longer for specialized teams (urban search and rescue, generator strike teams). Requires a signed EMAC request form (REQ-A) and, for anything beyond de minimis cost, a cost-reimbursement agreement executed before deployment, not after.
5. **Direct Federal Assistance** — requested only when steps 1–4 are exhausted or the capability doesn't exist at state/EMAC level (e.g., military airlift); routed through the state to FEMA, days-scale lead time except for pre-staged assets.

Rule: never let a Step 4 or 5 request substitute for Step 1–3 coverage of the first operational period — file the EMAC/federal request in parallel with, not instead of, exhausting closer resources.

## 4. Declaration and Public Assistance sequence

```
T+0h    Local state of emergency declared by county (Board Chair or EM
        Director under delegated authority) — opens local procurement
        emergency authority and is the prerequisite for state/federal asks.
T+12h   Governor issues state disaster declaration, activates state
        resources and EMAC eligibility for the county.
T+24h   FEMA Regional Administrator notified; joint Preliminary Damage
        Assessment (PDA) teams scheduled as soon as safe site access
        allows (county GIS + state + FEMA validator, typically within
        5–10 days post-incident for a hurricane).
T+~10d  PDA total compiled: $38.4M eligible public damage
          Category A (debris)                    $9.6M
          Category B (emergency protective meas.) $6.8M
          Category C (roads & bridges)           $12.2M
          Category E (public buildings)           $5.4M
          Categories F/G (utilities/other)        $4.4M
          -----------------------------------------------
          Total                                  $38.4M
        County per-capita check: 310,000 × $4.72/capita indicator
        ≈ $1.46M threshold — county total clears it ~26×.
T+~14d  Governor requests Presidential major disaster declaration,
        citing the PDA and requesting Individual Assistance (IA) for
        Zone A residential damage in addition to Public Assistance (PA).
T+~21d  Declaration approved. Standard cost share applies: 75% federal /
        25% non-federal ($28.8M / $9.6M on the $38.4M total) unless a
        separate Governor's request for an enhanced share (e.g., 100%
        federal for Categories A/B for a limited window) is separately
        approved — treat as pending, not assumed, until FEMA confirms
        in writing.
T+~21d  Non-federal share obligation ($9.6M, split $4.8M state / $4.8M
        county under this state's standard formula) goes to the Board
        as a budget amendment from reserves — do not wait for federal
        funds to arrive before appropriating the match; PA reimburses
        against expenditure already incurred, not in advance.
```

## 5. Public Assistance documentation checklist (per project worksheet)

- Force account labor: timesheets tied to the specific incident period and task, signed by supervisor, cross-referenced to ICS-214 unit log entries.
- Equipment: FEMA equipment rate schedule hours logged per piece of equipment per operational period, not a lump-sum estimate.
- Contracts: procurement method documented (competitive, non-competitive/emergency, or pre-existing) — emergency (non-competitive) contracts need a written justification memo dated before or at mobilization, not reconstructed afterward.
- Debris removal: pre- and post-removal photos or video per site, with GPS/timestamp metadata, plus a debris monitoring firm's load tickets reconciled to disposal site tonnage.
- Mutual aid/EMAC costs: the executed reimbursement agreement, invoice, and proof of payment, filed together — a cost without its agreement attached is a common disallowance.

## 6. Tabletop exercise design sequence (HSEEP-aligned)

1. Set 2–3 objectives max, each tied to a specific capability being tested (e.g., "test EOC-to-Unified-Command information flow during a Section Chief handoff"), not "test the hurricane plan" as a single vague objective.
2. Write the Situation Manual with a realistic starting scenario plus at least 3 scripted injects, one of which is a cascading failure (e.g., the primary shelter's generator fails at hour 6, or the Planning Section Chief becomes unreachable at shift change).
3. Assign a facilitator (drives the scenario) separate from an evaluator (grades the plan, not the players) — combining the roles produces exercises that grade participant performance instead of testing the plan's gaps.
4. Run the exercise; capture every place a participant says "in real life we'd just call Bob" — that's an undocumented dependency the plan needs to name explicitly.
5. Hot-wash immediately after (15–30 min, what worked / what didn't, no fixes discussed yet), then produce the After-Action Report within 30 days.
6. Convert every AAR finding into an Improvement Plan (IP) line with a named owner, a corrective action, and a deadline — an IP item with no owner is dropped within a year in practice.

## 7. Continuity of Operations (COOP) essentials

- Essential functions list: no more than the ~10–15 functions that must continue within 12 hours of a disruption (payroll, 911 dispatch, water treatment operation, EOC itself) — a list of 50 "essential" functions means nothing was actually prioritized.
- Orders of succession: minimum 3 deep per essential-function lead, named by position not just by person.
- Delegations of authority: pre-signed, specifying exactly which authorities transfer (contracting, emergency declarations, press communication) and the triggering condition.
- Alternate facility: identified, with a MOU if it's another jurisdiction's building, and tested at least once every 2 years with an actual relocation drill, not a tabletop walk-through of the plan.
