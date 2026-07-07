# Playbook

Filled procedures a cargo supervisor actually runs, with real numbers plugged in. Swap in the carrier's own SOP thresholds and the aircraft type's own charts where they differ from the illustrative figures below.

## 1. ULD max gross weight quick reference

| Type code | Common name | Max gross weight | Tare (approx.) | Typical use |
|---|---|---|---|---|
| AKE | LD3 | 1,588 kg (3,500 lb) | 80–105 kg | Standard belly container, narrow/wide-body lower deck |
| ALF | LD6 (two-LD3 footprint) | 3,175 kg (7,000 lb) | ~170 kg | Wide door-sill widebody lower deck |
| AAP/AYY | LD8/LD11 | 2,449 kg (5,400 lb) | ~130 kg | Larger-footprint widebody lower deck |
| PMC | 88×125 in pallet + net | 6,033 kg (13,300 lb) structural cert | ~105 kg pallet + net | Main-deck freighter or large-belly combi |
| PAG | 88×125 in pallet, lighter cert | 4,626 kg (10,200 lb) structural cert | ~100 kg | Lower structural-cert pallet variant |

**Field procedure:**

1. Read the ULD's own placard for its type code and certified max gross weight — never assume from the manifest line what container it actually is.
2. Weigh the built ULD on the platform scale; do not accept the manifest-summed weight as the actual weight.
3. If actual weight ≥ certified max gross weight, reject and rebuild — subtract actual from max gross weight to know exactly how much must come off, and pull enough to leave margin, not to land exactly on the limit.
4. Remember the aircraft-specific position limit can be lower than the ULD's own structural certification (e.g., a floor-loading or CG-index constraint at a specific position) — check both, and the lower number governs.

**Worked check — the 42R case:** LD3 max gross weight 1,588 kg; actual build 1,750 kg; overage = 1,750 − 1,588 = 162 kg (162 ÷ 1,588 = 10.2% over). Reject.

## 2. Hazmat segregation lookup (illustrative subset of IATA DGR 9.3.A logic)

| Class A | Class B | Requirement |
|---|---|---|
| 1 (Explosives, other than 1.4S) | Any other class | Do not load, transport, or store together |
| 3 (Flammable liquid) | 5.1 (Oxidizer) | Separated From — different compartment, or non-adjacent position with full separation |
| 4.1 (Flammable solid) | 5.1 (Oxidizer) | Separated From |
| 3 (Flammable liquid) | 8 (Corrosive) | Away From — minimum ~1.2 m (4 ft) horizontal separation; same compartment permitted |
| 6.1 (Toxic) | 3 (Flammable liquid) | Away From |
| 2.2 (Non-flammable gas, no subsidiary hazard) | Most classes | No restriction |

**Field procedure:**

1. Identify the exact UN number and class for every dangerous-goods item from its shipper's declaration and package marking — not from the manifest description alone.
2. Look up the pairing against every position physically adjacent to the assigned position in that specific compartment, not just the position it's replacing.
3. "Away From" clears with standard horizontal spacing in the same compartment; "Separated From" requires a different compartment or a fully non-adjacent position with a barrier; anything marked prohibited rules out the same aircraft cargo compartment entirely, not just the same ULD.
4. Any relocation driven by a segregation conflict updates the NOTOC before departure — a NOTOC that doesn't match the actual built position is itself a hold condition.

## 3. Load-plan reconciliation / Last-Minute-Change (LMC) decision

| Change type | Within LMC scope? | Action |
|---|---|---|
| Weight change ≤ carrier LMC threshold (e.g., ≤100 kg per compartment), no position added/removed | Yes | Ramp updates the build tag/local log; no dispatch reissue required |
| Weight change > threshold, no position added/removed | No | Call load control; hold for amended loadsheet before continuing |
| Any ULD/position added or removed vs. the original LIR | No — always | Call load control regardless of the weight delta |
| Hazmat class or position change (segregation-driven relocation) | No — always | Call load control and update the NOTOC |

**Worked reconciliation — the 42R/Bulk-5 case:** Planned total cargo weight 5,410 kg (1,320 + 1,180 + 990 + 1,540 + 380). 42R reverts to its planned 1,540 kg (net change zero on that position). Bulk hold moves from 380 kg to 590 kg (+210 kg) as a new, previously unplanned addition. Actual total: 5,410 + 210 = 5,620 kg. Because a position was added — not merely a weight shift — this is outside LMC scope regardless of the 100 kg threshold; load control reissues the loadsheet before pushback is cleared.

## 4. Restraint (lock/net) verification checklist

1. Walk every restraint point on the ULD — floor locks, side guides, and any net or strap — and confirm each shows fully engaged (commonly a "green" or flush-seated indicator), not partially seated.
2. Treat any point that's ambiguous — discolored indicator, visible gap, obstructed view — as unrestrained; re-latch and recheck rather than accepting a visual "looks caught."
3. Run the ULD past the compartment's contour gauge before spotting for loading; a container that clears its own weight limit can still exceed the door or guide-rail contour if built unevenly.
4. Log the position as loaded only after both restraint and contour checks pass — a scale-cleared, contour-failed, or restraint-ambiguous ULD is not a loaded position yet.

## 5. FOD walk and ground-equipment clearance

| Item | Standard | Fallback if uncertain |
|---|---|---|
| FOD walk cadence | Per the ramp safety program's fixed interval (commonly before each aircraft turn or arrival/departure) | If the last walk predates recent GSE traffic on the stand, treat the stand as unwalked and re-walk before pushback |
| GSE clearance at idle power | Published intake/exhaust danger-zone radius for that engine at idle (commonly on the order of a few meters) | If the published radius isn't posted for this aircraft type, default to the widest published radius among types on the ramp |
| GSE clearance at engine-start/high power | Published danger-zone radius expands sharply with thrust — treat as a much larger exclusion zone than idle | Hold all GSE movement until engine spool-up is confirmed complete and crew signals clear |
| GSE parked adjacent to fuselage/wingtip | Minimum published parking clearance per ramp safety chart, wing-walker required for any GSE movement inside that clearance | If clearance distance is unclear for the specific stand, assign a wing-walker regardless |

Never rely on a generic "stay back" instinct for engine hazard zones — the radius is power-setting-dependent and published per aircraft type, and idle-power clearance is not a safe distance once start or high-power sequencing begins.
