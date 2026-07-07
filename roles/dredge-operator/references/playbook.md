# Playbook

Filled planning templates a dredge operator and project engineer actually run before and during a dredging job. Numbers below are illustrative worked examples following standard methods — every project still gets planned against its own permit, testing plan, and current hydrographic survey, never against figures memorized from a document like this one.

## 1. Channel depth, overdepth, and advance maintenance

**Terms:** project (authorized) depth is the contracted minimum; controlling depth is the shallowest surveyed point across a channel cross-section; allowable (paid) overdepth is a contracted tolerance absorbing survey/positioning uncertainty; advance maintenance depth is additional planned depth beyond project depth to extend the interval before the next shoaling-driven maintenance cycle.

**Filled example:**

- Project depth: 45 ft (MLLW).
- Contracted allowable overdepth: 2 ft.
- Advance maintenance allowance: 2 ft.
- Dredge template depth targeted: 45 + 2 (advance maintenance) = 47 ft, with the 2 ft overdepth held as tolerance, not a target to chase.
- Pre-dredge survey: average depth 41.5 ft (shoaled 3.5 ft below project depth) — 5.5 ft of material to remove to reach the 47 ft template.
- Post-dredge as-built survey: minimum controlling depth across the cross-section comes back 45.3 ft.

**Compliance check:** 45.3 ft ≥ 45 ft project depth → channel certified as maintained. Buffer before the next required maintenance cycle: 45.3 − 45 = 0.3 ft above bare project depth plus whatever advance maintenance depth remains uneroded — track this against the reach's known shoaling rate (cy/year) to project the next maintenance window, not just the current pass/fail.

**Failure case:** if the same survey instead returned a minimum controlling depth of 44.2 ft (0.8 ft short of project depth) in one cell, that cell is non-compliant regardless of how the rest of the channel surveyed — it gets redredged before the channel is certified, and the paid-overdepth allowance does not cover a shortfall below project depth; it only covers removal beyond it.

## 2. Dredge-type selection matrix

| Factor | Cutterhead (hydraulic) | Hopper (TSHD) | Mechanical (clamshell/backhoe) |
|---|---|---|---|
| Sediment fit | Loose sand, silt, soft clay | Sand/silt, large-volume open-water runs | Hard clay, rock, debris, contaminated sediment |
| Typical depth/reach | To ~20–25 m without ladder extension; needs pipeline access to placement | Open water, any depth within hull draft; self-propelled transit to disposal site | Shallow to moderate depth, confined access (under piers, marinas) |
| Water added to material | Yes — slurry transport | Yes, but contained in hopper; overflow used to concentrate load | No — material lifted near in-situ volume |
| Environmental fit | Needs turbidity control at cutter and pipeline discharge point | Plume control at hopper overflow/entrainment during loading | Preferred where dilution must be minimized — contaminated material, CDF placement, sensitive habitat edges |
| Production rate | High for soft material with a short pipeline run | High for large open-water volumes | Lower production, higher precision |

**Default rule:** match dredge type to the testing-unit sediment/contamination profile first, then to production-rate goals — a fast plant that adds dilution water to material that must stay concentrated (contaminated, CDF-bound) is the wrong tool even if it's the one already mobilized.

## 3. Sediment-testing decision tree (disposal classification)

**Tier 1 — Bulk sediment chemistry** screened against regional reference sediment. Passes → proceeds toward open-water eligibility (still needs elutriate/water-column testing). Exceeds → Tier 2 triggered.

**Tier 2 — 10-day acute bioassay** (e.g., amphipod species such as *Ampelisca abdita*) against reference sediment. Survival ≥80% of reference control, not statistically different → passes, eligible for open-water disposal. Survival <80% of reference control or statistically significant mortality → fails, Tier 3 or reclassify.

**Tier 3 — 28-day bioaccumulation test**, run if Tier 2 fails and a capping or beneficial-use alternative is under consideration. Fails, or no alternative pursued → material classified unsuitable for open water; routes to a confined disposal facility (CDF) or upland placement.

**Filled example:** Reference sediment PCB concentration 0.02 mg/kg. Testing Unit B bulk PCB comes back 0.19 mg/kg (9.5× reference) → exceeds screening, Tier 2 bioassay ordered → 62% survival vs. the 80%-of-control pass threshold → fails → routed to CDF (see `SKILL.md` worked example for the full cost reconciliation).

## 4. Slurry density and critical (minimum transport) velocity

**Method:** hold pipeline velocity at or above the critical velocity for the sediment's grain size and the pipe diameter in use; within that constraint, target a solids-content band that maximizes production without risking settling.

**Target solids content by volume for medium sand:** roughly 15–20% [stated heuristic — hydraulic transport literature]. Below ~10%: production collapses because most of the pumped volume is water. Above ~30–35%: risk of dropping below critical velocity and settling out in the line, especially at bends and during any flow interruption.

**Filled example** — 24 in (0.61 m) discharge pipeline, medium sand (d50 ≈ 0.3 mm), critical velocity for this grain size/pipe combination ≈4.5 m/s [stated heuristic]:

- Pipe cross-sectional area = π × (0.305 m)² ≈ 0.292 m².
- Flow rate to hold 4.5 m/s critical velocity = 0.292 × 4.5 ≈ 1.315 m³/s = 4,734 m³/hr of slurry.
- **At 18% solids by volume:** solids moved = 4,734 × 0.18 ≈ 852 m³/hr ≈ 1,114 cy/hr. Over a 20-hr production day: ≈22,280 cy/day.
- **At 10% solids (same flow rate, same velocity):** solids moved = 4,734 × 0.10 ≈ 473 m³/hr ≈ 619 cy/hr. Over 20 hr: ≈12,380 cy/day — nearly half the production for the same pump effort, the cost of running too dilute.
- **At an attempted 32% solids:** achieving that mix at the same pump head typically drops achievable velocity to roughly 3.0 m/s — below the 4.5 m/s critical velocity — so particles settle out during any low-flow interval or near bends. The theoretical throughput (4,734 × 0.32 ≈ 1,515 m³/hr ≈ 1,982 cy/hr) is never realized safely; a plug-clearing event costs far more downtime than the production gain would have been worth.

**Operating rule:** watch the density/velocity gauge continuously; if velocity trends toward the critical threshold, cut solids target or shorten the discharge run before the line settles, not after a plug forms.

## 5. Turbidity-monitoring response plan

**Permit condition (typical numeric form, after WAC 173-201A-200):** turbidity at the compliance monitoring point must not exceed background by more than 5 NTU when background is ≤50 NTU, or by more than 10% when background exceeds 50 NTU. Monitoring point typically sited ~150 m downcurrent of the active discharge or cutter/bucket location; background station upcurrent.

**Filled example, low-background case:** background reading 12 NTU → compliance limit = 12 + 5 = 17 NTU. Monitoring point reads 21 NTU → exceeds by 4 NTU → response: deploy secondary silt curtain, reduce cutter swing/bucket cycle rate, re-sample every 30 minutes until back under 17 NTU before resuming full production.

**Filled example, high-background case:** background reading 80 NTU (naturally turbid estuary after a storm) → compliance limit = 80 × 1.10 = 88 NTU. Monitoring point reads 84 NTU → compliant, no containment action required, though the approaching-threshold trend gets logged and re-checked on the next interval.

**Default trigger:** treat any reading within roughly 80% of the numeric limit as a cue to redeploy or reposition containment before the next reading, not to wait for a confirmed exceedance.
