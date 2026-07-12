# Freight Forwarder — Playbook

## Revenue-ton calculation (filled example)

| Field | Value |
|---|---|
| Shipment weight | 11,000 kg |
| Shipment volume | 22 CBM |
| Weight-based tons | 11,000 ÷ 1,000 = 11 tons |
| Volume-based tons | 22 CBM ≈ 22 tons-equivalent (1 CBM ≈ 1 revenue ton, industry convention) |
| **Revenue tons (billing basis)** | max(11, 22) = **22** |
| LCL rate | $70.00 / revenue ton |
| LCL freight | 22 × $70.00 = $1,540.00 |
| CFS handling/devanning fee | $225.00 flat |
| **Total LCL cost** | $1,540.00 + $225.00 = **$1,765.00** |

Rule: always compute both bases and bill the greater. A "light and bulky" shipment (foam, apparel, furniture) is volume-driven; a "dense and heavy" shipment (machinery, metal stock) is weight-driven. Quoting off whichever number the shipper mentions first is the single most common LCL pricing error.

## FCL-vs-LCL breakeven worksheet (filled example)

| Option | Basis | Rate | Total cost | Transit add-on |
|---|---|---|---|---|
| LCL (22 revenue tons) | Revenue ton | $70.00/ton + $225 CFS fee | $1,765.00 | +3-5 days for CFS consolidation/deconsolidation |
| FCL (20' container, ~26-28 CBM / ~17,500 kg capacity) | Flat container rate | $1,650.00 all-in (ocean freight + BAF + THC O/D + doc fee) | $1,650.00 | none — direct door-to-port-to-door |
| **Delta** | — | — | **$115.00 (6.5% of LCL total) in FCL's favor** | FCL also avoids co-mingled cargo damage risk |

Decision rule: quote FCL alongside LCL whenever the shipment falls within roughly 12-15+ CBM of the lane's typical 20' breakeven band; below that band, LCL is reliably cheaper and the transit-time cost of consolidation rarely matters enough to justify a full container.

## Incoterm responsibility-split matrix (filled example, common terms)

| Incoterm | Export clearance | Origin haulage to port | Main carriage booking | Import clearance | Destination haulage |
|---|---|---|---|---|---|
| EXW (Ex Works) | Buyer | Buyer | Buyer | Buyer | Buyer |
| FOB (Free On Board) | Seller | Seller | Buyer | Buyer | Buyer |
| CIF (Cost, Insurance, Freight) | Seller | Seller | Seller (books, buyer's forwarder tracks) | Buyer | Buyer |
| DAP (Delivered At Place) | Seller | Seller | Seller | Buyer | Seller (to named place) |
| DDP (Delivered Duty Paid) | Seller | Seller | Seller | Seller | Seller |

Read this matrix against the actual shipping instructions before booking — a forwarder engaged by the buyer on an FOB deal only owns main carriage onward; if origin haulage or export clearance hasn't visibly been arranged by the seller, that's a gap to raise before the cargo-ready date, not after a missed cutoff.

## Agent-vs-NVOCC posture checklist (filled example)

Scenario: forwarder is booking a 22 CBM shipment and deciding whether to issue its own House Bill of Lading.

| Question | Answer this shipment | Consequence |
|---|---|---|
| Is the forwarder contracting in its own name with the shipper? | Yes — issuing HBL | Forwarder takes on carrier-like liability to the shipper |
| Does the forwarder hold an active NVOCC tariff/bond for this trade lane? | Yes — FMC-registered OTI, current bond on file | HBL is enforceable; liability cap applies per published tariff |
| Is declared cargo value stated on the HBL? | Declared at $18,500 (matches commercial invoice) | Caps recoverable claim amount at declared value, not full replacement cost if higher |
| Is the underlying Master B/L consistent with the HBL particulars (weight, pieces, marks)? | Confirmed matching | Mismatch here is a customs-hold risk at destination, independent of liability question |

Outcome: proceed with HBL issuance as NVOCC; declared value and MBL/HBL consistency both confirmed before the booking is finalized, not discovered at claim time.

## Demurrage/detention tracking worksheet (filled example)

Scenario: 22 CBM FCL shipment arrives Long Beach, carrier free time is 4 calendar days for demurrage (container at terminal) and 4 calendar days for detention (container off-terminal, in shipper's possession).

| Milestone | Date | Days elapsed | Status |
|---|---|---|---|
| Vessel arrival / discharge | Day 0 | 0 | Free time clock starts |
| Customs entry filed | Day 1 | 1 | On track |
| Customs release | Day 3 | 3 | Within 4-day demurrage free time |
| Container picked up from terminal | Day 3 | 3 | Demurrage avoided; detention clock starts |
| Container returned empty | Day 6 | 3 days of detention use | Within 4-day detention free time — no per diem charge |

Rule: push the return deadline to the shipper the day the vessel arrives (Day 0), not the day free time expires — a shipper notified on Day 3 of a Day 4 deadline has no room to react if customs clearance slips.
