# Artifacts — Templates With Example Content

Real work products, filled in with plausible examples. Copy the structure, replace the content. The example runs through Meridian Distribution's ERP replatform from `SKILL.md` — a $380M industrial distributor replacing a 17-year-old customized ERP with a cloud platform while integrating with an existing Salesforce CRM.

---

## 1. Requirements traceability matrix (RTM)

The matrix that catches orphaned requirements — the single most valuable artifact in the role, because "we wrote it down" and "someone owns building it" are different facts.

| ID | Requirement | Source | Classification | Design element | Owner | Status |
|---|---|---|---|---|---|---|
| FIN-014 | 3-way match (PO/receipt/invoice) required above $5,000 | Controller, JAD session 3 | Out-of-box | NetSuite native 3-way match | SI team | Traced |
| FIN-022 | Multi-entity consolidation across 3 legal entities | CFO interview | Configuration | NetSuite OneWorld config | SI team | Traced |
| SALES-007 | Quote approval requires VP sign-off above $50K | Sales ops JAD | Configuration | Approval workflow config | SI team | Traced |
| WHSE-031 | License-plate (nested pallet) tracking at pick | Warehouse walkthrough | Customization | Custom bundle + integration to WMS | Internal dev | Traced |
| WHSE-033 | Cycle-count variance auto-flag at >2% | Warehouse walkthrough | Customization | Custom SuiteScript | Internal dev | Traced |
| CRM-009 | Opportunity-to-order handoff without re-keying pricing | Sales ops JAD | Configuration | CPQ-to-ERP connector | SI team | Traced |
| FIN-041 | Historical GL detail retained 7 years, queryable | Controller, compliance ask | Out-of-box | Data archive + reporting layer | SI team | Traced |
| WHSE-019 | Returns processing reason-code taxonomy (12 codes) | Warehouse walkthrough | *No design element assigned* | — | — | **Orphaned** |
| SALES-015 | Commission clawback on returned orders | Finance/Sales joint session | *No design element assigned* | — | — | **Orphaned** |

**Checkpoint math:** 58 requirements total; 39 out-of-box (67%), 12 configuration (21%), 7 customization (12%); 6 of 58 (10%) orphaned at the gap-analysis checkpoint, including WHSE-019 and SALES-015 above. Every orphaned row gets an owner and a design element before design freeze, or it's descoped in writing — never left silent.

---

## 2. Gap analysis matrix

Same requirements, viewed as current-state vs. target-state capability, with the size of the gap made explicit instead of implied by the classification alone.

| Process area | Current-state capability | Target-state (NetSuite) capability | Gap size | Resolution |
|---|---|---|---|---|
| GL / consolidation | Manual entity elimination in Excel, 3 days/month close | Native OneWorld consolidation, same-day | None — target exceeds current | Adopt native |
| AP 3-way match | Manual match above $5K, 2 FTE-days/week | Native automated match | None | Adopt native |
| Warehouse license-plate tracking | Custom-built module, 12 years of accumulated exceptions | No native equivalent; closest is lot tracking, not nested-pallet | Large | Custom bundle + WMS integration (7 requirements land here) |
| Returns reason coding | 12-code taxonomy, undocumented outside 2 warehouse leads' heads | Generic 4-code return reason field | Large, undiscovered until walkthrough | Orphaned pending design decision — expand target field or retrain to 4 codes (business decision, not IT's to make unilaterally) |
| Commission calculation | Spreadsheet-based, includes clawback rule nobody wrote down | No native clawback logic | Large, undiscovered until walkthrough | Orphaned; likely custom integration to existing comp-calc tool rather than ERP customization |

The two "undiscovered until walkthrough" rows are why walkthroughs happen with the people who do the work, not just their managers — reason-code taxonomies and clawback rules live in institutional memory, not in any system's documentation.

---

## 3. Feasibility study (TELOS structure)

| Dimension | Question | Finding | Verdict |
|---|---|---|---|
| **T**echnical | Can the target platform meet the requirements without unsupportable custom code? | 88% of requirements met out-of-box or by configuration; the 12% requiring customization is concentrated in one process area (warehouse), not scattered | Pass |
| **E**conomic | Does the cost-benefit clear the org's hurdle rate over a stated horizon? | 3-year raw TCO favors Option A by $840K, but the 2028 vendor-sunset risk brings 5-year cost within ~$20K of parity (see SKILL.md worked example) — economic case is genuinely close, not a clear pass | Marginal — flag to sponsor as a risk-tolerance call, not a slam-dunk |
| **O**perational | Can the org actually absorb the change (training capacity, process change tolerance)? | 220 warehouse staff need training; org's historic training throughput is ~15 staff/week fully certified — 220 staff / 15 per week ≈ 15 weeks, incompatible with a single-weekend cutover, compatible with a phased rollout | Pass, phased only — fails for big-bang |
| **S**chedule | Is the requested timeline achievable against comparable projects? | Sponsor requested 14 months; benchmark median is 16 months with 74% of projects over initial budget (Panorama Consulting 2024) | Fail as requested; pass at 19 months |

**Rule:** all four dimensions must clear the bar independently. A project that's economically marginal and schedule-infeasible as requested isn't rescued by strong technical feasibility — it goes back to the sponsor with the specific dimension that needs a different answer (here: schedule and cutover approach), not a blanket "no."

---

## 4. Interface control document (ICD) excerpt

Specifies the data contract, not just which systems talk to each other — this is what the integration developer builds to.

```
ICD-003: Order Creation — CRM (Salesforce) → ERP (NetSuite)

Trigger: Opportunity marked Closed-Won in Salesforce
Pattern: API-led, Process API layer (not direct point-to-point)
Direction: Salesforce → Middleware → NetSuite (synchronous, <5s SLA)

Payload (required fields):
  - opportunity_id (string, Salesforce 18-char ID) — idempotency key
  - customer_tax_id (string, validated against dedup remediation
    output — see Section 5) — reject if not found in cleaned master
  - line_items[] (sku, quantity, unit_price, discount_pct)
  - requested_ship_date (date, must be >= today + 2 business days)

Error handling:
  - Tax ID not found in cleaned customer master → route to manual
    queue, do NOT auto-create a new customer record (this is the
    exact failure mode that produced the 22% duplicate rate
    originally)
  - Price mismatch between CRM quote and ERP price book > 2% →
    hold for pricing-team review, do not auto-approve

Reconciliation: nightly batch compares order count and total value
between Salesforce closed-won and NetSuite created orders; variance
> 0.5% triggers same-day investigation, not next-week review.
```

The error-handling section is the part generalist integration designs skip — "sync the data" without a stated rule for what happens when the data doesn't match is how the next dirty-data problem gets created.

---

## 5. Data migration risk register

| Risk | Likelihood | Impact | Score (L×I, 1-5 each) | Mitigation | Owner |
|---|---|---|---|---|---|
| Duplicate/conflicting customer records (22%, 7,610 of 34,612) carried into new system | High (5) | High (5) | 25 | 5-week manual remediation gate before Phase 1 design freeze; no migration without sign-off | Data steward |
| Warehouse license-plate history (12 years) doesn't map cleanly to target lot-tracking model | Medium (3) | High (4) | 12 | Custom mapping bundle, tested against 3 months of historical picks before cutover | Internal dev lead |
| Commission clawback logic undocumented, discovered late | Medium (3) | Medium (3) | 9 | Orphaned-requirement resolution before design freeze (see RTM) | Finance + Sales joint owner |
| Integration cutover: 14 point-to-point scripts retired same weekend as ERP go-live | High (4) | High (5) | 20 | Reject — phase integration retirement separately from ERP cutover; run parallel for 2 weeks post-cutover with reconciliation checks | Integration lead |
| Vendor support for legacy ERP lapses mid-migration (Q1 2028 sunset vs. 19-month timeline) | Low (2) | High (4) | 8 | Timeline lands migration complete ~8 months before sunset; monitor vendor's actual sunset communications quarterly | Program sponsor |

**Scoring convention:** score ≥ 20 blocks design freeze until mitigated in writing; 10-19 requires a named owner and a check-in cadence; below 10 is tracked but not gating.
