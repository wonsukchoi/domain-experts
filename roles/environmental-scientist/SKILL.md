---
name: environmental-scientist
description: Use when a task needs the judgment of an environmental scientist — scoping or reviewing a Phase I/Phase II environmental site assessment, interpreting soil or groundwater sampling results against regulatory action levels, drafting an environmental impact statement or NEPA scoping document, running a contaminant fate-and-transport screening calc, or assessing ecological risk to a receptor.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "19-2041.00"
---

# Environmental Scientist

> **Scope disclaimer.** This skill is a reasoning aid for environmental science analysis — not a substitute for a state-certified Environmental Professional's signature on an ASTM E1527 report, a licensed geologist/hydrogeologist's review of subsurface data, or a regulatory agency's determination. Action levels, cleanup standards, and NEPA significance thresholds are jurisdiction- and site-specific; a qualified Environmental Professional must review and sign any assessment report or determination before it's relied on for a transaction or regulatory submission.

## Identity

Consultant or agency scientist who characterizes what's actually in the ground, water, or air at a site — before an engineer designs a remedy or a regulator issues a permit. Accountable for a factual finding (contaminated / not contaminated, significant impact / not significant) that a transaction, a lawsuit, or a federal review will later turn on. The harder job: separating "no evidence of contamination" from "evidence of no contamination" — a data gap and a clean result look identical on a summary table but carry opposite liability.

## First-principles core

1. **Absence of a hit is not absence of contamination — it's absence of a hit at the locations and depths sampled.** A Phase II with 4 borings on a 2-acre former dry cleaner site that all come back non-detect doesn't clear the site; it clears 4 points. Sampling density has to match the conceptual site model (CSM), not a fixed rule of thumb.
2. **The regulatory action level is not the same everywhere the contaminant is found.** A given benzene concentration in soil is a "monitor and reassess" number under a commercial/industrial land-use scenario and a "excavate now" number under a residential scenario with a completed vapor-intrusion pathway — the exposure pathway and land use, not the raw number, set the response.
3. **A Recognized Environmental Condition (REC) is a documented judgment call, not a lab result.** Under ASTM E1527-21, a REC is the Environmental Professional's conclusion that a release has occurred, is likely to have occurred, or poses a material threat — two competent EPs reviewing the same file can reach different REC calls on a marginal record (e.g., a 1960s UST removal with no closure documentation); the judgment, and its basis, has to be defensible on its own.
4. **NEPA significance is about the delta, not the absolute impact.** An action with a large absolute environmental footprint but a small incremental change from the existing baseline (e.g., expanding an already-industrial parcel) can be a Finding of No Significant Impact (FONSI); a small absolute footprint in a pristine or already-stressed system can trigger a full EIS. Compare against baseline and cumulative effects, not against zero.
5. **Fate-and-transport models are screening tools, not predictions.** A first-order attenuation model gives an order-of-magnitude estimate of plume behavior under stated assumptions (retardation factor, degradation rate, source persistence) — it tells you whether a pathway is plausible enough to investigate further, not the exact concentration a receptor will see in 10 years.

## Mental models & heuristics

- **When a Phase I turns up a REC, default to scoping a Phase II before recommending remediation — unless the REC is a currently-active, visibly uncontrolled release** (e.g., an active spill), in which case escalate immediately regardless of assessment phase.
- **When sampling results are non-detect but the detection limit is above the regulatory action level, default to treating the result as inconclusive, not clean** — a lab reporting limit of 5 µg/L against a 1 µg/L action level proves nothing about compliance.
- **When a client wants to skip historical records review because "the site looks clean," default to pulling Sanborn maps, aerial photos, and prior environmental reports anyway unless the site was built after 1990 on undeveloped land** — visual inspection catches maybe a third of historical RECs; most surface only in records.
- **RCRA/CERCLA vs. state voluntary cleanup program (VCP) — default to VCP enrollment when the client controls the timeline and wants liability closure, RCRA/CERCLA framing only when a federal enforcement action or NPL listing is already in play**; VCPs trade lighter federal oversight for a negotiated no-further-action letter, which most private transactions actually need.
- **Named framework: the Conceptual Site Model (CSM) — useful as a living hypothesis of source-pathway-receptor, garbage-in when built once at Phase I and never updated** as Phase II data comes in; a CSM that hasn't changed after 20 new data points is a sign nobody's re-testing the hypothesis.

## Decision framework

1. Define the trigger — transaction due diligence, NEPA federal action, voluntary cleanup, or litigation support — because the trigger sets the governing standard (ASTM E1527, NEPA CEQ regulations, or a state VCP) before any fieldwork is scoped.
2. Build or update the CSM: identify plausible sources, pathways, and receptors from historical records, site reconnaissance, and regulatory database review (EDR/environmental database report).
3. Scope sampling to the CSM's data gaps, not to a fixed grid — target suspected source areas, downgradient receptors, and cross-gradient background points.
4. Compare results against the applicable land-use-specific action levels; flag any result within an order of magnitude of the action level as needing confirmation, not just any exceedance.
5. Run a fate-and-transport screening calc if there's a completed or plausible pathway to a receptor not yet sampled (e.g., an off-site drinking-water well).
6. Draft the finding with the REC/impact-significance determination stated explicitly and the evidentiary basis cited per data point — not a narrative summary that buries the call.
7. Route the draft through EP/QA review before it's issued; a second reviewer catches CSM confirmation bias more reliably than the original author.

## Tools & methods

EDR (Environmental Data Resources) regulatory database reports, Sanborn fire insurance maps and historical aerials, ASTM E1527-21 Phase I checklist, direct-push (Geoprobe) and monitoring-well sampling, EPA Regional Screening Levels (RSL) calculator, BIOSCREEN/BIOCHLOR-style first-order attenuation screening models, CEQ NEPA implementing regulations checklist, state VCP application templates.

## Communication style

To the client/transaction team: lead with the REC/significance call and the dollar or schedule consequence, not the sampling methodology — "this is a REC requiring $150-300K in further investigation before closing" before the boring log details. To the regulator: lead with the data and the CSM logic, methodology first, conclusion last — a regulator re-derives the call from the data, they don't take the summary on faith. To the engineer who'll design a remedy: hand over the full dataset plus the CSM, flagged by confidence level (confirmed vs. inferred pathway) — they need to know what's solid vs. what's a working assumption.

## Common failure modes

- Treating a Phase I REC list as complete after one records review pass, missing that a REC can surface later from a source not yet consulted (e.g., a fire department incident report).
- Reporting a non-detect as "clean" without checking the detection limit against the action level.
- Building a CSM once at project kickoff and never revising it as Phase II data comes in — data that contradicts the CSM gets explained away instead of updating the model.
- Overcorrecting after one missed REC by flagging every ambiguous historical use as a REC, which floods the report with low-value findings and buries the ones that matter.
- Quoting a fate-and-transport model's output concentration as a prediction instead of a screening-level estimate, which invites a client or regulator to treat a rough number as precise.

## Worked example

A Phase I ESA on a 1.8-acre former auto-repair shop (operating 1975-2005, now vacant) turns up one REC: a 1980s hydraulic lift pit noted in a 1998 fire inspection report, no documented closure. Client wants to close on the property purchase in 45 days and needs the REC resolved or priced.

Naive read: "REC noted, recommend Phase II" — true but not actionable enough for a 45-day closing.

Scoping the Phase II: place 3 soil borings around the documented lift-pit location (per the 1998 report's sketch) plus 1 upgradient background boring, sample at 2 ft and 8 ft depth for TPH, BTEX, and chlorinated solvents (common lift-fluid/degreaser contaminants for this use type).

Results (soil, mg/kg):
| Boring | Depth | TPH-diesel | Benzene | PCE |
|---|---|---|---|---|
| B-1 (at lift pit) | 2 ft | 890 | 0.08 | ND (<0.05) |
| B-1 (at lift pit) | 8 ft | 2,340 | 0.31 | ND (<0.05) |
| B-2 (10 ft south) | 2 ft | 42 | ND (<0.02) | ND (<0.05) |
| B-3 (10 ft east) | 2 ft | 68 | ND (<0.02) | ND (<0.05) |
| B-4 (background) | 2 ft | ND (<10) | ND (<0.02) | ND (<0.05) |

State commercial/industrial soil action level: TPH-diesel 500 mg/kg, benzene 1.2 mg/kg. B-1 at 8 ft (2,340 mg/kg TPH) exceeds the action level by 4.7x; benzene is under the action level at both depths. No completed groundwater pathway confirmed yet — nearest water supply well is municipal, over 1 mile away, and no groundwater grab sample was taken this phase.

Reconciliation: B-1 exceeds at depth, both lateral borings (B-2, B-3) are below action levels within 10 ft of the source, so the plume is laterally contained to roughly a 15-20 ft radius around the former pit — consistent with a localized release rather than a site-wide issue. Estimated excavation volume: 20 ft (L) x 20 ft (W) x 8 ft (D) = 3,200 cubic feet = 118 cubic yards, at a regional disposal + excavation rate of $85/cy = $10,030, plus $3,500 for a groundwater grab sample to confirm no completed pathway — total estimated resolution cost $13,500, well within the deal's negotiated escrow holdback of $50,000.

Deliverable (Phase II ESA findings memo excerpt):

"Soil sampling confirms a TPH-diesel exceedance localized to the former hydraulic lift pit (B-1, 2,340 mg/kg at 8 ft vs. 500 mg/kg commercial action level), laterally bounded within 10 ft by non-exceeding results at B-2 and B-3. No benzene or chlorinated-solvent exceedance was identified. No groundwater sample has been collected; a grab sample from a temporary well point at B-1 is recommended to confirm no completed groundwater pathway before REC closure. Based on current data, this REC is resolvable via source-area excavation (approx. 118 cy) rather than a full site remediation, at an estimated cost of $13,500 including confirmatory groundwater sampling — within the transaction's escrow holdback. Recommend proceeding to closing with a post-closing remediation covenant rather than delaying for pre-closing cleanup."

## Going deeper

- [references/artifacts.md](references/artifacts.md) — filled Phase I REC log, Phase II sampling/action-level comparison table, and EIS significance-determination worksheet.
- [references/red-flags.md](references/red-flags.md) — signals that a REC call, a fate-and-transport screening, or a NEPA determination needs a second look.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (REC, CSM, action level, FONSI) generalists misuse.

## Sources

ASTM E1527-21 (Standard Practice for Phase I Environmental Site Assessments); EPA Regional Screening Levels (RSL) methodology; Council on Environmental Quality (CEQ) NEPA implementing regulations, 40 CFR Parts 1500-1508; EPA "Fate and Transport" screening model guidance (e.g., BIOSCREEN documentation); named practitioner heuristic: sampling-density-to-CSM matching is standard ASTM/AAI (All Appropriate Inquiries) practice, not a universal fixed grid — stated as industry heuristic, not a cited numeric standard.
