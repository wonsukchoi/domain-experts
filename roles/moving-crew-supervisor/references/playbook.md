# Moving Crew Supervisor — Playbook

Filled templates and worked calculators for the four recurring artifacts: the 110%-cap calculation, the additional-service order, the NIOSH lift-screening worksheet, and the crew-sizing check.

## 1. Non-binding estimate 110% cap calculator

Run this at delivery on every non-binding shipment before collecting payment.

| Field | Value |
|---|---|
| Estimated weight (lbs) | 6,000 |
| Tariff rate ($/cwt) | $120 |
| Estimated linehaul (weight ÷ 100 × rate) | $7,200.00 |
| Estimated accessorials (packing, valuation, etc.) | $750.00 |
| **Estimated total** | **$7,950.00** |
| **110% payment ceiling (estimated total × 1.10)** | **$8,745.00** |
| Actual net weight (certified reweigh) | 6,900 |
| Actual linehaul (actual weight ÷ 100 × rate) | $8,280.00 |
| Actual accessorials billed | $750.00 |
| **Actual total charges** | **$9,030.00** |
| Additional-service charges (signed orders only, billed in full, not capped) | $0.00 |
| **Amount due today = min(actual total, ceiling) + additional-service charges** | **$8,745.00** |
| **Balance deferred ≥30 days (actual total − ceiling, if positive)** | **$285.00** |

Rule to apply, in order: (1) compute the ceiling off the *original estimate*, never off actual weight; (2) additional-service charges from a signed post-BOL order are collected in full, on top of the capped amount, not folded into the cap; (3) if actual total is at or below the ceiling, the full actual total is due today and there is no deferred balance.

## 2. Additional-service order (fill and sign before loading the item)

```
ADDITIONAL SERVICE ORDER — Shipment #____________
Item(s) added after BOL signed: ________________________________
Estimated weight added: __________ lbs
Reason not on original cube sheet: [ ] customer request  [ ] item found during load
                                    [ ] special handling required (specify): ______
Special handling: [ ] team lift  [ ] appliance dolly  [ ] disassembly required
                  [ ] third-party specialist needed (piano, safe >600 lbs, art)
Additional charge quoted: $__________  (flat fee / per-item — NOT rolled into cwt rate
                                         unless a supplemental weight-based estimate is issued)
Customer signature: ______________________  Date/time: ______________
Crew lead signature: ______________________
```

Never load an item under this form without both signatures present — an unsigned verbal "just put it on" is the single most common source of a delivery-day billing dispute.

## 3. NIOSH lift-screening worksheet (single-item, borderline lift)

RWL = LC × HM × VM × DM × AM × FM × CM, where LC (load constant) = 51 lbs. Lifting Index (LI) = actual weight ÷ RWL. **LI > 1.0 → team lift or mechanical aid, no exceptions.**

Worked example — a 210-lb gun safe, hand position 10 in. horizontal from ankles, lift origin 12 in. off the floor, no vertical travel beyond a level carry, no twisting, infrequent (one lift), poor coupling (no handles):

| Multiplier | Factor | Value used | Contribution |
|---|---|---|---|
| HM (horizontal, 10/H) | 25/H | 25/10 → capped at 1.0 max | 1.00 |
| VM (vertical, 1 − 0.003×\|V−30\|) | V=12 | 1 − 0.003×18 = 0.946 | 0.946 |
| DM (distance, 0.82 + 4.5/D) | short carry, D≈10 in | ≈0.99 (short, treat as 1.0) | 1.00 |
| AM (asymmetry, 1 − 0.0032×A) | A=0° (no twist) | 1.00 | 1.00 |
| FM (frequency) | 1 lift/task | 1.00 | 1.00 |
| CM (coupling, poor) | poor grip, no handles | 0.90 | 0.90 |

RWL = 51 × 1.00 × 0.946 × 1.00 × 1.00 × 1.00 × 0.90 ≈ **43.4 lbs**.
LI = 210 ÷ 43.4 ≈ **4.8** — far over 1.0. Call: minimum 3-person team lift or mechanical lift (appliance dolly rated for the weight, or decline and refer to a rigging specialist for safes over ~600 lbs). A crew that "has moved safes before" without a scored LI is estimating this on memory, not on the actual grip and distance conditions in front of them today.

## 4. Crew-sizing / loading-rate check

| Metric | How to compute | Flag threshold |
|---|---|---|
| Sustained loading rate (stairs/long-carry-free stretch) | Weight moved ÷ (crew size × hours) | <250–300 lbs/crew-member-hour sustained → diagnose staging/access before adding labor |
| Stair or long-carry accessorial owed | Confirm distance/flights against original survey | >75 ft from truck to door, or any flight of stairs not disclosed at survey → billable accessorial, document before charging |
| Crew-to-weight ratio for same-day completion | Remaining weight ÷ (target rate × hours remaining) = minimum crew needed | If computed crew exceeds crew on-site, call for backup before falling behind, not after |

## 5. Claims triage (Released Value vs. Full Value Protection)

| Valuation on file | Company's cap | First move at claim intake |
|---|---|---|
| Released Value Protection (no charge, signed waiver on BOL) | $0.60/lb × item weight, regardless of actual value | Weigh the damaged item (or use inventory-listed weight); compute cap; compare against condition tags/photos from origin |
| Full Value Protection | Repair, replacement, or cash settlement at current market value, subject to any deductible on file | Pull origin condition tags/photos first; if none exist for the disputed item, treat causation as unresolved, not assume the crew is liable |

An item with no origin condition tag and no photo is a dispute the crew cannot win on documentation — the tag exists to establish "already damaged before we touched it," not just to describe the item.
