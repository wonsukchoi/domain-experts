# Customs and Border Protection Officer — Playbook

## Inspection-tier escalation table

| Tier | Trigger | Action | Time budget |
|---|---|---|---|
| Primary | Every traveler/shipment | Document check, brief interview, manifest review | 30–90 sec (traveler) / 3–8 min (commercial) |
| Secondary — light | 1 low-severity indicator, or ambiguous manifest description | Extended interview, database cross-check, manifest reconciliation | 5–15 min |
| Secondary — full | 2+ indicators clustering, or 1 high-severity indicator (watchlist hit, visible anomaly) | X-ray/imaging, K-9 if available, physical search | 15–45 min |
| Investigative referral | Secondary confirms violation with potential criminal nexus, or value/scale exceeds officer's disposition authority | Hand off to investigative unit (HSI, IPR unit, etc.) with full documentation package | N/A — case-managed |

## Risk-scoring worksheet (filled example)

| Indicator | Present? | Severity weight | Notes |
|---|---|---|---|
| Declared value within 10% of a reporting/duty threshold | Yes | +1 | $8,400 vs $9,000 simplified-entry threshold (6.7% under) |
| Goods description generic relative to declared quantity/value | Yes | +1 | "electronic components," 340 units |
| Repeat-importer pattern clustering near threshold across multiple filings | Yes | +2 (compounding — pattern across shipments outweighs any single shipment) | 4 entries in 60 days, $8,200–$8,800 each, 4 different carriers |
| Travel-document or watchlist mismatch | N/A (cargo, not traveler) | — | — |
| **Total** | | **4** | **Referral threshold for this port: 3.** Refer to secondary — full tier given the compounding pattern indicator. |

Referral threshold is a stated example calibration, not a universal number — individual ports and CBP directives set actual thresholds; this worksheet shows the *structure* of the scoring logic (independent indicators add, patterns across multiple transactions compound rather than simply add) for an agent to reason with, not the real operational threshold.

## Chain-of-custody procedure (seizure)

1. Photograph goods/contraband in place, before moving, with timestamp and location metadata.
2. Complete seizure form at time of seizure — item description, quantity, estimated value, legal basis (statute cited), officer ID, witness officer ID if available.
3. Transfer custody to evidence/property control with a signed receipt at each handoff — no gap in the signature chain.
4. Issue notice of seizure to the owner/importer of record within the statutory notice window (varies by seizure type — verify current requirement, do not assume a fixed number of days without checking current CBP directive).
5. Log the case number and cross-reference to the entry/manifest record and any related prior entries flagged in the pattern review.

A seizure with a gap in steps 1–3 (e.g., photographs taken after goods were moved, or a custody transfer without a signed receipt) is vulnerable to challenge on procedure even when the underlying finding is correct — treat the documentation as equally important as the physical finding, not as paperwork to complete afterward.

## Structuring-pattern review checklist

When a single entry shows one weak indicator, check the importer's/traveler's history before deciding:
- Pull last 90 days of entries/crossings for this importer/traveler ID.
- Plot declared values against the nearest relevant threshold — look for clustering just under the line, not just near it.
- Check for carrier/route diversification on otherwise-similar shipments (a legitimate high-volume importer usually has *some* shipments that vary widely in value; an importer whose every shipment sits just under a threshold is the pattern, not the coincidence).
- If 3+ entries in the review window show the near-threshold-clustering pattern, treat the current entry's weak indicator as a strong one — the pattern moves it from "isolated, low-severity" to "part of a confirmed pattern," which the decision framework treats as a compounding factor, not an additive one.
