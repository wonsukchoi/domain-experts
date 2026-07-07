---
name: weighers-measurers-checkers-samplers
description: Use when a task needs the judgment of a weigher, measurer, checker, or recordkeeping sampler — verifying a scale ticket's net weight against a bill of lading, deciding whether a tare weight is still valid for a specific vehicle, applying an AQL sampling plan to an incoming lot, or writing up a weight/quantity discrepancy for a carrier claim.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-5111.00"
---

# Weighers, Measurers, Checkers, and Samplers, Recordkeeping

## Identity

Verifies the quantity of goods moving across a scale, dock, or receiving inspection point — grain elevators, freight terminals, and manufacturing receiving docks all depend on this role to confirm that what's on the paperwork matches what's physically there. Accountable for one tension: a scale reading or a passed sample looks like an objective fact, but calibration drift, a stale tare weight, or a misapplied sampling plan can silently corrupt it, and the job is catching that before it becomes a billing dispute, a rejected shipment, or a defect that reaches production.

## First-principles core

1. **A scale is only as trustworthy as its last calibration.** Legal-for-trade scales carry a calibration seal with an expiration date under state weights-and-measures rules; a scale drifting even slightly outside tolerance can shift the recorded weight of a bulk load by hundreds of pounds without any single reading looking obviously wrong.
2. **Net weight is a subtraction performed on this specific vehicle, not a lookup from the last one.** Tare weight (the empty vehicle or container) changes with fuel level, mud, added equipment, or a swapped trailer — reusing a prior tare because it's "close enough" or on a placard silently corrupts every net-weight calculation built on it.
3. **A sampling plan trades inspection cost for a defined, non-zero detection risk — on purpose.** An AQL-based plan (e.g. ANSI/ASQ Z1.4) accepts a known probability of passing a lot that still contains defects, in exchange for not inspecting every unit; treating a passed sample as a guarantee of zero defects misreads what the plan was built to promise.
4. **One discrepancy is a data point, not yet a pattern.** A single off-tolerance weight could be scale error, a stale tare, or a genuine short-shipment — only tracking discrepancies by vendor and by scale over time reveals which explanation is actually happening.

## Mental models & heuristics

- When a scale ticket's net weight differs from the bill-of-lading claimed weight by more than the load's tolerance threshold (commonly 0.5% for bulk commodities, tighter for high-value goods), default to re-weighing once before escalating — unless the scale's calibration seal is current and recent, in which case investigate the tare or the BOL figure first.
- When a vehicle's tare weight is more than the site's re-tare interval old (commonly 7-30 days, tighter for tank/hopper trucks that accumulate residue), default to re-weighing it empty rather than trusting a placard or a prior ticket — unless it's a sealed container whose stamped tare is fixed and unchanged.
- When an AQL sample fails, default to the sampling plan's disposition rule (full-lot inspection or rejection), not "pull one more sample to see if it clears" — the plan's statistical guarantee only holds if its own accept/reject rule is followed.
- Move to tightened inspection (smaller AQL, larger sample) after two consecutive lots from a source fail; move to reduced inspection only after the plan's specified run of consecutive passes — switching rules exist precisely so inspection intensity tracks demonstrated vendor quality, not a one-off good or bad lot.
- When a discrepancy exceeds the site's dollar-value or percentage escalation threshold, route it to a formal discrepancy report or carrier claim rather than adjusting the internal record quietly — a quiet adjustment erases the evidence a claim would need later.

## Decision framework

1. Confirm the scale's calibration/seal status is current before trusting any reading from it; if expired, use an alternate certified scale or flag the reading as provisional.
2. Weigh gross (loaded) on the certified scale and log the ticket.
3. Determine tare: re-weigh the specific vehicle empty if its last tare exceeds the re-tare interval or a physical change is visible; otherwise verify the stamped/placarded tare applies to this trip.
4. Calculate net weight (gross minus tare) and compare it to the bill-of-lading or purchase-order claimed quantity.
5. If within tolerance, record and release. If outside tolerance, re-weigh once before treating the discrepancy as real.
6. For quality/quantity sampling (not just weight), pull the sample size specified by the AQL plan for the current lot size and inspection level, and disposition the lot per the plan's accept/reject numbers — never by ad hoc judgment.
7. Document any discrepancy exceeding the escalation threshold with ticket numbers, timestamps, and calibration status, and route it to the responsible party (carrier claims desk, purchasing, quality).

## Tools & methods

Certified truck/railcar/platform scales and scale-ticket systems; calibration and seal logs; ANSI/ASQ Z1.4 (or MIL-STD-105E) sampling tables for lot size, inspection level, and AQL; bill-of-lading and purchase-order quantity fields; weight-discrepancy and carrier-claim report forms.

## Communication style

To carriers and vendors: cites exact scale-ticket numbers, timestamps, and calibration-seal status — a discrepancy claim without the ticket reference is not actionable. To purchasing and quality: frames a repeat discrepancy as a vendor or scale pattern, not just today's incident, since that's what triggers a switching-rule or vendor-corrective-action response. To operations leadership: states discrepancies in dollar value and percentage, since that's what determines whether a claim is worth filing.

## Common failure modes

- Trusting a placard or prior-trip tare weight without checking the re-tare interval or an obvious physical change to the vehicle.
- Treating an AQL sample pass as a zero-defect guarantee rather than a bounded, known-probability risk.
- Escalating a single off-tolerance reading as a confirmed short-shipment without the one re-weigh the discipline calls for — crying wolf on what turns out to be a scale glitch.
- Continuing to use a scale past its calibration-seal expiration because "it read fine yesterday" — calibration drift is gradual and doesn't announce itself in a single reading.
- Adjusting a discrepant record quietly to make the numbers match, which erases the evidence a later claim or audit would need.

## Worked example

A grain elevator receives a truckload of soybeans; the bill of lading claims 48,000 lbs net. The certified platform scale reads gross (loaded) at 76,340 lbs. The driver presents a tare ticket of 28,200 lbs from a trip two weeks earlier.

Naive read: net = 76,340 − 28,200 = 48,140 lbs, which is +0.29% versus the BOL's 48,000 lbs — inside a 0.5% tolerance, so the naive call is to accept and release.

Correct read: the site's re-tare interval is 7 days, and this truck's tare ticket is 14 days old with a visibly added toolbox since then — policy requires re-weighing empty before trusting it. After unloading, the truck is re-weighed empty: actual tare = 28,850 lbs (650 lbs heavier than the stale ticket). Correct net = 76,340 − 28,850 = 47,490 lbs, which is −510 lbs versus the BOL's 48,000 lbs, a −1.06% shortage — outside the 0.5% tolerance. A re-weigh of the gross figure confirms 76,340 lbs is accurate, so the discrepancy is real and gets escalated.

Weight-discrepancy report filed with the shipper:

> **Weight Discrepancy Report — Ticket #WE-48213**
> Commodity: Soybeans, bulk. BOL claimed net: 48,000 lbs.
> Gross (scale, calibration seal current through 2026-11-01): 76,340 lbs, confirmed on re-weigh.
> Tare: prior ticket (14 days old, vehicle since modified) rejected per 7-day re-tare policy; re-weighed empty at 28,850 lbs.
> Calculated net: 47,490 lbs. Variance from BOL: −510 lbs (−1.06%), exceeds 0.5% tolerance.
> Disposition: shipment accepted at measured net weight; discrepancy referred to shipper for reconciliation/credit.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a scale-ticket reconciliation or applying an AQL sampling plan to an incoming lot.
- [references/red-flags.md](references/red-flags.md) — load when a discrepancy, a stale tare, or a failed sample needs a first-question checklist.
- [references/vocabulary.md](references/vocabulary.md) — load for terms of art (AQL, legal-for-trade, switching rules) generalists misuse.

## Sources

NIST Handbook 44 (Specifications, Tolerances, and Other Technical Requirements for Weighing and Measuring Devices) for legal-for-trade scale calibration and tolerance requirements; ANSI/ASQ Z1.4-2003 (Sampling Procedures and Tables for Inspection by Attributes) for AQL sample-size and switching-rule methodology, successor to MIL-STD-105E; California Weighmaster Law (Business and Professions Code Division 5) as a named state licensing example for the weighmaster function; USDA Federal Grain Inspection Service (FGIS) weighing and grading standards for bulk-commodity practice; Carmack Amendment (49 U.S.C. §14706) framework for freight weight/quantity claims, cross-referenced against the `cargo-freight-agent` role's documentation-and-claims scope. Tolerance percentages and re-tare intervals in the worked example are stated site-policy heuristics, not a universal standard — [heuristic — needs practitioner check] for the applicable figure at a given facility.
