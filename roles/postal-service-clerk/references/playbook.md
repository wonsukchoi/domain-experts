# Postal Service Clerk — Playbook

## Dimensional-weight determination

| Step | Calculation | Example |
|---|---|---|
| 1. Measure | L × W × H in inches | 18 × 14 × 8 |
| 2. Cubic size | L × W × H | 2,016 cubic inches |
| 3. DIM threshold check | Is cubic size ≥ 1,728 (1 cubic ft)? | Yes → DIM pricing applies |
| 4. Dimensional weight | Cubic size ÷ 166, round up to next whole pound | 2,016 ÷ 166 = 12.14 → 13 lb |
| 5. Billable weight | Greater of actual weight and dimensional weight | max(4, 13) = 13 lb |

If cubic size is under 1,728 cubic inches, skip to actual weight — do not calculate DIM weight on a package that doesn't cross the threshold; it wastes time at the window and the number is irrelevant to the rate.

## Service-level selection table

| Customer need | Recommend | Why not the alternative |
|---|---|---|
| Prove something was sent (legal notice, contract termination, tax filing) | Certified Mail | Registered's chain-of-custody overhead isn't needed — the sender only needs proof of mailing/delivery, not item-value protection |
| Prove a specific person received it | Certified Mail + Restricted Delivery / Signature Confirmation | Adds the recipient-identity requirement Certified alone doesn't guarantee |
| Protect a high-value or irreplaceable item (jewelry, cash-equivalent, rare document) | Registered Mail | Manual chain-of-custody at every handoff point is the control that justifies the cost and time; Certified Mail has no equivalent custody tracking |
| Track a shipment, no legal-proof need | Priority Mail (tracking included) or Signature Confirmation add-on | Certified Mail's legal-proof documentation is unnecessary overhead for a simple tracking need |

## Mailability screening — common flagged categories

| Category | Ground-eligible? | Air-eligible? | Notes |
|---|---|---|---|
| Nail polish / polish remover, most flammable liquids | Yes, in limited quantity with proper packaging | No | Air prohibition is the trap — item is legal, transportation mode isn't |
| Lithium batteries, loose (not installed in device) | Yes, with hazmat labeling | Restricted/no | Installed-in-device batteries have different (usually more permissive) rules than loose cells |
| Aerosols (hairspray, spray paint) | Limited quantity, proper packaging | No | Same air/ground split as flammable liquids |
| Dry ice (as a coolant, small quantity) | Yes, must be labeled and vented, quantity-limited | Yes, with the same labeling/venting/quantity rules | Package must not be airtight — the dry ice needs to vent |
| Perishable food (no dry ice) | Yes, with appropriate class (e.g., expedited) | Yes | Class selection matters more than a hard restriction — a slow class risks spoilage before a mailability violation |
| Ammunition | Ground only, licensed shipper in most cases | No | Often requires the sender to hold specific licensing — verify before accepting, don't assume retail eligibility |

When an item doesn't clearly fit a known category, the fallback position — in order of preference — is: (1) check the current Publication 52 restricted/prohibited list by item name, (2) ask a supervisor rather than guess, (3) accept for ground-only transportation if genuinely uncertain about air eligibility but the item is clearly not fully prohibited, (4) refuse and document the reason if the item matches a prohibited category outright.

## Filled example: rate-and-insurance transaction summary

**Package:** 18×14×8 in box, 4 lb actual weight, Zone 5 destination, declared value $250, contents ceramic lamp (not restricted).

**Calculation:**
- Cubic size 2,016 in³ ≥ 1,728 in³ → DIM pricing applies
- DIM weight: 2,016 ÷ 166 = 12.14 → 13 lb
- Billable weight: max(4, 13) = 13 lb
- Base rate (Priority Mail, Zone 5, 13 lb, illustrative): $24.10
- Included insurance: $100; declared value $250 → coverage gap $150
- Additional insurance fee (illustrative, tiered by coverage amount): $3.65
- **Total: $27.75**

**Receipt handed to customer:**

> Priority Mail, Zone 5, billable weight 13 lb (dimensional — box size, not scale weight, determined this) — $24.10
> Insurance: $100 included + $150 additional — $3.65
> Total: $27.75
> Tracking: [XXXXXXXXXXXXXXXXXXXX]
