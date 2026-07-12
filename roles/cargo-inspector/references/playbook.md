# Cargo Inspector — calculation playbook

Filled worked calculations. Substitute the vessel's or shipment's own figures; do not use the example numbers as defaults.

## 1. Draft survey — cargo-loaded calculation

**Step sequence, with the MV Example figures from SKILL.md's worked example:**

| Step | Item | Value |
|---|---|---|
| 1 | Initial mean-of-means draft (fwd, mid, aft × port/stbd, averaged) | 4.10 m |
| 2 | Initial displacement (from hydrostatic tables at that draft, trim, and density) | 18,420.0 MT |
| 3 | Initial deductibles (ship's constant + fuel oil + fresh water + ballast aboard) | 1,850.0 MT |
| 4 | **Net initial displacement** (2 − 3) | **16,570.0 MT** |
| 5 | Final mean-of-means draft | 9.85 m |
| 6 | Final displacement (from tables) | 41,650.0 MT |
| 7 | Bunkers consumed during loading (deducted from initial deductibles) | 160.0 MT |
| 8 | Final deductibles (3 − 7, ballast unchanged) | 1,690.0 MT |
| 9 | **Net final displacement** (6 − 8) | **39,960.0 MT** |
| 10 | **Cargo loaded** (9 − 4) | **23,390.0 MT** |
| 11 | Shore tally (belt scale / weighbridge) | 23,320.0 MT |
| 12 | Variance (10 − 11), as % of 11 | 70.0 MT / 0.30% |
| 13 | Tolerance check | 0.30% ≤ 0.5% trade tolerance → **accept draft-survey figure** |

**Mean-of-means draft reading, worked:** six readings taken (fwd port 4.08 m, fwd stbd 4.09 m, mid port 4.11 m, mid stbd 4.10 m, aft port 4.12 m, aft stbd 4.10 m) → mean = (4.08+4.09+4.11+4.10+4.12+4.10)/6 = 24.60/6 = **4.10 m**. Never substitute a single midship reading for this average — a 2° list alone can shift a single-point reading by several centimeters, which on a full-form bulk carrier translates to tens of tonnes of displacement error.

**When to reject the shore tally instead of the draft survey:** if the shore scale has a documented calibration lapse (belt scale not zero-checked that shift, weighbridge certificate expired), treat the draft survey as governing regardless of variance size, and note the scale's certification status in the report.

## 2. API MPMS tank-gauging outturn (petroleum)

| Step | Item | Value |
|---|---|---|
| 1 | Observed ullage (tape reading from reference point to liquid surface) | 2.145 m |
| 2 | Gross observed volume (from tank calibration table at that ullage) | 8,420.6 barrels |
| 3 | Observed temperature | 78°F |
| 4 | Volume Correction Factor (VCF) at 78°F for this product's API gravity (from API MPMS Ch. 11 tables) | 0.9887 |
| 5 | **Gross standard volume** (2 × 4) | **8,325.4 barrels** at 60°F |
| 6 | Free water found by paste/tape | 12.4 barrels |
| 7 | **Net standard volume** (5 − 6) | **8,313.0 barrels** |

**Rule:** never report the gross observed volume (row 2) as the certified figure — it is only correct at the observed temperature, and a receiving terminal contracts for volume at the 60°F standard. A 1°F swing on a large parcel moves the corrected volume by tens of barrels; always show your VCF and the temperature it was applied at in the report so the calculation can be audited.

## 3. Load height/width clearance check

| Step | Item | Value |
|---|---|---|
| 1 | Measured load height, chassis to top of cargo, on level ground | 13 ft 8 in |
| 2 | Lowest posted clearance on planned route (a rail underpass) | 13 ft 10 in |
| 3 | Applied safety margin (default 6 in) | 6 in |
| 4 | **Required minimum clearance margin** (1 + 3) | 14 ft 2 in |
| 5 | Comparison | 14 ft 2 in > 13 ft 10 in posted clearance → **route rejected; re-route or reduce load height required** |

**Rule:** compare the load height *plus margin* against the posted clearance, not the bare measured height against the posted number — a load that clears by 2 inches on paper is a load that fails against pavement resurfacing, tire pressure variance, or a slightly off-level road the inspector cannot verify at measurement time.

## 4. Cargo securement — aggregate working-load-limit check

| Step | Item | Value |
|---|---|---|
| 1 | Article weight (steel coil) | 18,000 lb |
| 2 | Required aggregate WLL (≥ 0.5 × weight, per 49 CFR 393.106) | 9,000 lb |
| 3 | Tiedown 1 WLL (chain, tagged) | 5,400 lb |
| 4 | Tiedown 2 WLL (chain, tagged) | 5,400 lb |
| 5 | Tiedown 3 WLL (tag illegible — counts as 0) | 0 lb |
| 6 | **Total usable aggregate WLL** (3 + 4 + 5) | **10,800 lb** |
| 7 | Comparison | 10,800 lb ≥ 9,000 lb required → **passes**, but flag Tiedown 3 for re-tagging/replacement before next inspection |

**Rule:** a tiedown with a missing, illegible, or damaged WLL tag contributes zero to the aggregate, even if it is physically sound — do not estimate an untagged tiedown's contribution from its apparent size or material.

## 5. Dangerous-goods segregation check (IMDG Code)

| Step | Item | Value |
|---|---|---|
| 1 | Container A hazard class | Class 3 (flammable liquid), UN 1993 |
| 2 | Container B hazard class, proposed adjacent stow | Class 5.1 (oxidizer), UN 1479 |
| 3 | IMDG segregation table lookup, Class 3 vs. Class 5.1 | "Separated from" (minimum: different hold/compartment, or 3 m if on deck) |
| 4 | Actual planned stow | Same hold, 1.5 m apart |
| 5 | Comparison | 1.5 m < 3 m minimum for on-deck, and same hold violates "separated from" for below-deck stow → **stow plan rejected; re-stow to separate holds or re-space per table minimum** |

**Rule:** check the segregation table for the specific class-pair, not a generic "keep hazmat apart" instinct — some class pairs require only "away from" (general separation), others require full compartment/hold separation, and the required distance changes by stowage location (on deck vs. below deck).

## 6. Letter of protest — filled template

> **LETTER OF PROTEST**
> **Date:** [date] **Vessel/Vehicle:** [name/ID] **Port/Terminal:** [location]
> **To:** [terminal operator / carrier / receiving party]
> **Re:** [specific discrepancy — e.g., "Hold-cleaning certificate presented as clean and dry, fit to load"]
>
> This is to formally protest and place on record that [specific factual finding, with measurement/observation and time]. This finding was documented by [photographs Ref. #### / measurement / instrument reading] at the time of discovery, [time/date].
>
> This protest is issued without prejudice to any rights or claims either party may have, and reserves the surveyor's finding on liability pending further evidence.
>
> [Surveyor name, certification number, signature]
