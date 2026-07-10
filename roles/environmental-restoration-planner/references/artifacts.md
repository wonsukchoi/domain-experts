# Artifacts

Filled examples for the deliverables an environmental restoration planner actually produces. Populate the numbers, don't just follow the shape.

## CERCLA nine-criteria comparison matrix (Feasibility Study, detailed analysis)

| Criterion | Type | Alt 2 — MNA | Alt 3 — Pump-and-treat | Alt 4 — ISCR |
|---|---|---|---|---|
| Overall protection of human health/environment | Threshold | Fails — completed pathway, no trend data | Meets | Meets |
| Compliance with ARARs | Threshold | N/A (eliminated) | Meets (state groundwater standard) | Meets |
| Long-term effectiveness/permanence | Balancing | — | High (ongoing capture) | High (source destruction) |
| Reduction of toxicity/mobility/volume | Balancing | — | Moderate (hydraulic containment only) | High (in-situ destruction) |
| Short-term effectiveness | Balancing | — | Low disruption | Moderate (injection events) |
| Implementability | Balancing | — | Proven, but 15-yr O&M burden | Proven at similar scale |
| Cost (capital / life-cycle NPV) | Balancing | $180K / — | $1.4M / $4.03M | $950K / $1.43M |
| State acceptance | Modifying | — | Pending comment | Pending comment |
| Community acceptance | Modifying | — | Pending public meeting | Pending public meeting |

Row order matters: the two threshold criteria are evaluated first and gate whether an alternative even reaches the balancing-criteria columns — never average a threshold-criterion score into the ranking.

## Life-cycle cost estimate (AACE/ASTM E2516 class-based)

| Estimate stage | AACE class equivalent | Accuracy range | Basis |
|---|---|---|---|
| Feasibility Study (this document) | Class 4-5 | -30% / +50% | Vendor quotes, analogous-site unit costs, no site-specific pilot data |
| Remedial Design (30% design) | Class 3 | -20% / +30% | Site-specific pilot test results, preliminary layout |
| Remedial Design (90-100% design) | Class 2 | -15% / +25% | Detailed design, subcontractor bids |

State the class and range next to every cost figure in an FS — a Class 4-5 number presented without its range gets treated as a fixed budget by clients and agencies who don't distinguish estimate stages.

## Life-cycle NPV worksheet (O&M discounting)

| Alternative | Capital | Annual O&M | Duration (yrs) | Discount rate | Annuity factor | PV of O&M | Total NPV |
|---|---|---|---|---|---|---|---|
| Alt 3 — Pump-and-treat | $1,400,000 | $220,000 | 15 | 3% | 11.94 | $2,626,800 | $4,026,800 |
| Alt 4 — ISCR (yrs 1-8) | $950,000 | $60,000 | 8 | 3% | 7.02 | $421,200 | — |
| Alt 4 — ISCR (yrs 9-13, confirmation) | — | $15,000 | 5 (deferred 8 yrs) | 3% | 4.58 (then ÷1.03⁸) | $54,220 | — |
| Alt 4 — ISCR, total | $950,000 | — | — | — | — | $475,420 | $1,425,420 |

Formula: annuity factor = [1 - (1+r)⁻ⁿ] / r. For O&M streams that start after year 0 (deferred), discount the annuity-factor result back to present by dividing by (1+r)^(years deferred).

## Stream restoration design comparison against reference reach

| Parameter | Reference reach (unimpacted, same valley type) | Existing impacted reach | Design target |
|---|---|---|---|
| Rosgen stream type | C4 | F4 (entrenched, incised) | C4 |
| Entrenchment ratio | 2.8 | 1.1 | ≥2.2 |
| Width/depth ratio | 14 | 32 | 12-16 |
| Sinuosity | 1.4 | 1.05 | 1.3-1.5 |
| Bankfull discharge return interval | 1.5 yr | N/A (disconnected floodplain) | 1.5 yr |

Design targets are set as a range bracketing the reference reach's measured values, not a single point — natural channels vary within a stable range, and a design pinned to one exact number invites a false "failure" reading during post-construction monitoring when the built channel drifts within a still-stable range.

## Compensatory mitigation credit ledger (wetland restoration bank)

| Mitigation type | Acres | Credit ratio | Credits generated | Basis |
|---|---|---|---|---|
| Restoration (prior-converted cropland to forested wetland) | 40 | 1.5:1 | 26.7 | Rebuilds hydrology + vegetation + soils function |
| Enhancement (degraded wetland, hydrology improved only) | 15 | 4:1 | 3.75 | Partial function gain, some baseline function already present |
| Preservation (existing high-function wetland, permanently protected) | 60 | 10:1 | 6.0 | No new function created, protects existing |
| **Total bank credits** | | | **36.45** | |

Ratios above are illustrative of typical Corps district instrument terms — always confirm against the specific mitigation banking instrument or in-lieu fee program agreement; ratios are negotiated per-instrument and vary by district and wetland type.

## Five-Year Review trigger checklist (CERCLA remedies with residual contamination)

1. Does the selected remedy leave contamination above levels that allow unrestricted use and unlimited exposure? If yes, a Five-Year Review is statutorily required (CERCLA §121(c)).
2. Are all institutional/engineering controls identified in the Record of Decision actually recorded against the property (deed notice, easement) — pull the recorded instrument, not the ROD text describing it.
3. Has land use at or adjacent to the site changed since the last review (new construction, rezoning, well installation) in a way that could create a new exposure pathway?
4. Is monitoring data trending consistent with the remedy's conceptual model, or is there an unexplained divergence (rebound, new contaminant detected)?
5. Protectiveness determination: protective / protective in the short-term with actions needed / not protective — document the basis for whichever is selected, not just the conclusion.
