# Airline Pilot Playbook

Filled worksheets for the calculations and checks the SKILL.md decision framework calls for. Numbers below are illustrative, self-consistent examples in the shape of a typical widebody ETOPS operation and a Part 121 crew-scheduling system — always substitute the operator's actual approved fuel policy, current MEL, and current Part 117 tables.

## 1. ETOPS diversion-ring quick reference

Ring radius = one-engine-inoperative (OEI) driftdown cruise speed (KTAS) × rating (hours). Example uses a fuel-policy OEI speed of 420 KTAS.

| ETOPS rating | Ring radius (420 KTAS) | Typical use |
|---|---|---|
| 120 min | 420 × 2 = 840 nm | Standard twin-engine oceanic/remote rating; most North Atlantic tracks |
| 180 min | 420 × 3 = 1,260 nm | Common long-haul twin rating; most North Pacific and polar tracks |
| 240 min | 420 × 4 = 1,680 nm | Extended rating for ultra-long-haul city pairs with sparse adequate airports |

**Downgrade rule:** an ETOPS-specific MEL "M" procedure attached to a deferred item reduces the *tail's* current rating below the fleet's certified maximum for the remainder of the deferral interval. Recompute the ring at the downgraded rating before accepting a release built on the higher one.

**Worked recompute (matches SKILL.md worked example):**

| | Rating | Ring radius | Critical-point distance | Margin |
|---|---|---|---|---|
| Original release | 180 min | 1,260 nm | 1,050 nm to Shemya | 210 nm / 16.7% — compliant |
| After ETOPS-MEL downgrade | 120 min | 840 nm | 1,050 nm to Shemya | −210 nm / −25% — **non-compliant** |
| Amended track | 120 min | 840 nm | 815 nm to Shemya | 25 nm / 3.0% — compliant, minimum margin |

## 2. Dispatch-release audit checklist (filled example)

| Line item | What to check | This release |
|---|---|---|
| Routing | Matches current ETOPS rating for this tail, not fleet max | Amended after MEL downgrade — see §1 |
| Fuel | Trip + reserve + critical-fuel scenario rerun for current track | +5,420 lb over original (2,123 trip + 3,300 critical-fuel reserve) |
| Alternates | Adequate (not just suitable) at ETA, current NOTAMs checked | Shemya, Sapporo confirmed adequate; NOTAMs current as of release time |
| Weather | Destination + alternate forecasts bracket ETA, no unresolved TEMPO/PROB at minimums | RJAA forecast VMC at ETA; alternate forecast checked independently |
| MEL/CDL status | Every open item's placard/procedure reviewed, ETOPS-specific notes flagged | System C hydraulic demand pump — ETOPS-M procedure applied |
| Crew legality | Part 117 FDP checked against actual (not scheduled) report time and leg count | Report time unchanged this leg; FDP margin 1:10 under table limit |

**Rule:** any "no" or "not checked" answer on this table is a query to dispatch before pushback, not a note to revisit airborne.

## 3. Part 117 flight-duty-period table (illustrative excerpt)

Simplified shape of 14 CFR §117.11's Table B for unaugmented (2-pilot) operations — always consult the operator's actual FDP table for exact values; the real table has finer report-time bands and additional leg-count columns.

| Report time window | 1–2 flight segments | 3 segments | 6–7 segments |
|---|---|---|---|
| 0700–1159 (best circadian window) | 14 hr | 13:30 | 12:30 |
| 0600–0659 | 13 hr | 12:30 | 11:30 |
| 0000–0359 (worst circadian window) | 9 hr | 9 hr | 9 hr |

**Reading it:** the same crew, same aircraft, same raw hours worked can be legal at a 0700 report and illegal at a 0100 report — and legal at 2 segments but illegal once a diversion or reroute adds a 3rd or 7th segment to the same duty period. Recompute against the *actual* report time and segment count after any delay; don't reuse the number checked at original dispatch.

**Part 121 vs. Part 135 contrast:** Part 135 duty/rest (14 CFR §135.267) uses a flatter, segment-and-circadian-insensitive duty-day ceiling (e.g., a single ~14-hour duty-day limit regardless of report time) — a Part 121 pilot who reasons from Part 135-style flat-duty-day intuition will under-restrict an early-morning-report, multi-leg day that Part 117 actually caps well below 14 hours.

## 4. Critical-fuel-scenario worksheet (filled example)

Scenario: decompression plus engine failure at the route's most adverse (critical) point, diversion to nearest adequate airport at driftdown altitude and OEI speed — the ETOPS-specific fuel-planning floor, distinct from normal enroute contingency fuel.

| Component | Original release (critical pt. 1,050 nm) | Amended release (critical pt. 815 nm) |
|---|---|---|
| Trip fuel to critical point | Baseline | +2,123 lb (added track distance, 60 nm @ 480 kt GS, 17,000 lb/hr burn) |
| Descent + driftdown to adequate airport | Computed for 1,050 nm diversion | Rerun for 815 nm diversion — shorter diversion, but recomputed, not assumed lower |
| Reserve at alternate | Standard reserve | Standard reserve, unchanged |
| Net critical-fuel reserve added | — | +3,300 lb (rerun scenario at new critical point, not carried forward) |
| **Total fuel added, this amendment** | — | **2,123 + 3,300 = 5,423 lb ≈ 5,420 lb** |

**Rule:** every track or ETOPS-rating change requires rerunning this scenario from the new critical point — a shorter diversion distance does not automatically mean lower critical fuel once decompression descent profiles and driftdown altitude are recomputed.

## 5. PF/PM briefing card (filled example, oceanic leg)

| Phase | PF (Pilot Flying) | PM (Pilot Monitoring) |
|---|---|---|
| Preflight/dispatch review | States ETOPS rating, MEL status, fuel figures aloud | Independently checks each figure against the release before agreeing |
| Below 10,000 ft (departure/arrival) | Flies, communicates only essential items | Sterile cockpit enforced; defers non-essential items to level-off |
| Cruise, automation/route changes | Enters FMS/MCP change, states it aloud before executing | Cross-checks entry against clearance/plan before it's executed, not after |
| Approaching critical (equal-time) point | Confirms fuel state and diversion option aloud | Independently verifies remaining fuel against critical-fuel figure for that point |
| Any PF/PM role swap (fatigue, workload, leg change) | States "you have controls, you have PF" explicitly | States "I have controls, I have PF" explicitly — no silent handoff |
