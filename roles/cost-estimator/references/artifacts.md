# Estimator artifacts — templates with real structure

Filled templates for the hard-bid GC context used throughout SKILL.md: 45,000 SF medical office tenant improvement, Class 1 estimate (100% CDs), 14-week schedule, bid due Friday.

## 1. Bid leveling sheet (Division 26 — Electrical)

One tab per CSI division. Rows are scope lines pulled from the drawings/specs; columns are bidders. A blank cell means the bidder's proposal never mentioned the line — treat silence as an exclusion until confirmed otherwise, not as an inclusion.

| Scope line | Apex Electrical | Voltline Inc. | Summit E&C | Bidder D | Bidder E (low, $410K raw) |
|---|---|---|---|---|---|
| Base building power distribution | Included | Included | Included | Included | Included |
| Branch wiring, devices, fixtures per E-101–E-108 | Included | Included | Included | Included | Included |
| Fire alarm devices per FA-201 | Included | Included | Included | Included | **Excluded — "by FA sub"** |
| Emergency generator tie-in per E-601 | Included, $68,000 | Included, $71,000 | Included, $74,000 | Included, $69,000 | **Not mentioned** |
| RTU electrical connections (owner-furnished units) | Included, $64,000 allowance | Included, $60,000 allowance | Included, $65,000 allowance | Included, $63,000 allowance | **Not mentioned** |
| Low-voltage rough-in (data/AV pathways only) | Included | Included | Included | Excluded — priced separately | Included |
| Bonding & insurance per spec | Standard | Standard | Standard | Standard | **No bond letter attached** |
| **Raw bid total** | $545,000 | $558,000 | $612,000 | $670,000 | $410,000 |
| **Leveled total (add back priced exclusions)** | $545,000 | $558,000 | $612,000 | $670,000 + LV rough-in ($22,000 est.) = $692,000 | $410,000 + FA devices ($25,000 est.) + generator tie-in ($70,000) + RTU allowance ($65,000) = **$570,000 est.** |

**Reading it:** once leveled, Bidder E's real number (~$570K est., and unbonded) is not a bargain — it converges with the market band ($545K–$558K) while adding schedule/default risk from missing a bond letter. Carry Apex at $545,000; do not carry the raw $410,000.

## 2. Full estimate recap sheet (markup stack)

The stack is sequential — each layer is a percentage of the running subtotal above it, never of the raw direct cost. This is the sheet that goes to the estimating manager for bid-day sign-off.

| # | Line | Basis / rate | Amount | Running subtotal |
|---|---|---|---|---|
| 1 | Direct trade cost — self-perform + leveled sub bids, all CSI divisions | Takeoff + bid leveling sheets | $4,860,000 | $4,860,000 |
| 2 | General conditions | 14 wks × $16,800/wk (super $9,800 + 0.5 PM $3,600 + temp power/water $1,100 + trailer $650 + safety/cleanup $900 + dumpsters $750) | $235,200 | **$5,095,200** |
| 3 | Design/estimating contingency | 3% of line 2 subtotal (Class 1, 100% CDs — see red-flags.md for what moves this %) | $152,856 | **$5,248,056** |
| 4 | Escalation to midpoint of construction | 2% of line 3 subtotal (NTP ~3 mo out, 9-mo schedule, midpoint ~7.5 mo out) | $104,961 | **$5,353,017** |
| 5 | Payment & performance bond | 0.85% of line 4 subtotal | $45,501 | **$5,398,518** |
| 6 | Overhead & profit (reported as two lines, not blended) | OH 5% + profit 4% = 9% of line 5 subtotal | $242,933 + $242,933 | **$5,884,385** |

**Row 6 detail (never blend these on the internal sheet, even though the client-facing recap can show one combined markup line):**
- Home office overhead recovery: 5% of $5,398,518 = $269,926
- Profit: 4% of $5,398,518 = $215,941
- (Rounding note: 5%+4% applied jointly as 9% above nets $485,867; computing the two components separately and summing gives the same total — $269,926 + $215,941 = $485,867. Use whichever order the estimating software defaults to, but never report only the combined figure internally.)

**Sensitivity note (the arithmetic from SKILL.md's worked example):** swapping line 1's leveled electrical figure ($545,000) for the raw low bid ($410,000) drops direct cost to $4,725,000 and the same stack resolves to a $5,728,474 total — a $155,911 swing from a $135,000 scope gap, because contingency, escalation, bond, and OH&P are all percentages of a base that shrank.

## 3. Contingency burn-down log

Tracked against the $152,856 design/estimating contingency carried at bid. Each draw needs a cause code — the log is the tool that catches contingency being used as an undisclosed scope-creep fund.

| Date | Description | Cause code | Amount | Remaining |
|---|---|---|---|---|
| — | Contingency carried at bid | — | — | $152,856 |
| Wk 3 | Differing subsurface condition — unmapped utility line at column line C-4 | **DSC** (differing site condition) | $18,400 | $134,456 |
| Wk 6 | Owner requested upgraded ceiling grid in lobby | **OC** (owner change — should be a CO, not contingency) | $0 (rejected — routed to CO #4 instead) | $134,456 |
| Wk 9 | Structural steel connection detail omitted from IFC set, RFI #22 | **DO** (design omission) | $9,200 | $125,256 |
| Wk 11 | Estimating error — HVAC ductwork quantity take-off short by 8% | **EE** (estimating error) | $14,800 | $110,456 |

**Cause code key:** DSC (differing site condition), OC (owner change — reject; route to change order), DO (design omission/RFI-driven), EE (estimating error). A contingency log with more OC entries than DSC/DO/EE combined means the reserve is functioning as an unapproved change-order fund, not a risk reserve — flag it to the PM immediately.

## 4. Schedule of values excerpt (AIA G703, CSI-coded)

Submitted to the owner post-award for monthly payment applications; ties directly back to the estimate recap's direct-cost line, broken into CSI divisions.

| Item | CSI Division | Scheduled value | % complete (Pay App 3) | Amount billed to date | Retainage (10%) |
|---|---|---|---|---|---|
| Concrete | 03 | $380,000 | 100% | $380,000 | $38,000 |
| Metals | 05 | $210,000 | 85% | $178,500 | $17,850 |
| Openings (doors/frames/glazing) | 08 | $260,000 | 60% | $156,000 | $15,600 |
| Finishes | 09 | $890,000 | 20% | $178,000 | $17,800 |
| Plumbing | 22 | $410,000 | 70% | $287,000 | $28,700 |
| HVAC | 23 | $980,000 | 55% | $539,000 | $53,900 |
| Electrical | 26 | $545,000 | 65% | $354,250 | $35,425 |
| General conditions (Div 01) | 01 | $235,200 | 60% | $141,120 | — (typically excluded from retainage) |

**Reconciliation rule:** the SOV's division totals must sum to the estimate recap's direct-cost + GC lines exactly (here, $4,860,000 + $235,200 = $5,095,200) before the first pay application goes out. A mismatch caught after award means someone is now negotiating scope against a number nobody agreed to.
