# Playbook

Filled worksheets a loader actually runs at the rack or dock, not descriptions of them — adapt the numbers to the compartment, product, and terminal in front of you.

## 1. Bonding/grounding verification worksheet

1. Attach the bonding cable to a bare-metal contact point on the vehicle/vessel — never through paint, coating, or a gasketed fitting, which breaks continuity even when the clamp is physically attached.
2. Test resistance to ground with a dedicated continuity/resistance tester (not a visual check). Terminal threshold: commonly ≤10 ohms per API RP 2003 practice.
3. Do not open any liquid or vapor valve until the reading passes.
4. Log the reading, not just a pass/fail checkbox — a trend of readings creeping toward the threshold across shifts flags a corroding contact point before it fails outright.

Example: clamp attached to the cargo tank's designated bonding lug; tester reads 3.2 Ω against a 10 Ω threshold — pass, logged, valve sequence proceeds.

Failure example: clamp attached to a painted frame rail reads 480 Ω — fails. First question: is this reading through paint/coating, or is the cable itself damaged? Move the clamp to the designated bare-metal lug and retest before concluding the cable has failed.

## 2. Overfill-prevention / outage worksheet

1. Confirm compartment rated capacity and the terminal's outage percentage for the product being loaded (commonly 1–2% for gasoline/light distillates; higher for products with a larger thermal-expansion coefficient, e.g., some crude and NGL grades run 3–5%).
2. Compute the outage volume and the trip target: trip target = capacity × (1 − outage%).
3. Confirm the overfill sensor (optic or float type) is set to the trip target, independent of the visual gauge.
4. During the fill, monitor sensor status directly — confirm the automatic shutoff engages at the trip target, not that the gauge merely looks close to full.

Example: 2,500-gal compartment, gasoline, 2% outage → outage volume = 2,500 × 0.02 = 50 gal → trip target = 2,500 − 50 = 2,450 gal (98% of capacity). Sensor confirmed tripped automatically at 2,450 gal on the metered totalizer.

Higher-expansion-product example: 6,000-gal compartment, a product with a 4% terminal-specified outage → outage volume = 6,000 × 0.04 = 240 gal → trip target = 5,760 gal (96% of capacity).

## 3. Restricted initial-rate / switch-load worksheet

1. Check the compartment's prior cargo against the product being loaded. If different (switch load) — or if the product is a static accumulator regardless of prior cargo — apply the restricted-rate procedure even on a submerged bottom-loading line.
2. Compute the restricted-rate flow limit for the fill line: target linear velocity ≈1 m/s (≈3.3 ft/s). Flow (gpm) = pipe cross-sectional area (ft²) × velocity (ft/s) × 60 × 7.48.
3. Hold the restricted rate until the terminal's specified initial volume is loaded (commonly enough to cover the drop-tube outlet — check the rack's own SOP for the number, since it depends on compartment geometry).
4. Step up to full rack rate for the remainder of the fill up to the overfill trip target.

Example: 4-inch line (ID 4.026 in, area ≈0.0884 ft²), velocity 3.3 ft/s → flow = 0.0884 × 3.3 × 60 × 7.48 ≈ 130 gpm. Restricted phase covers first 200 gal (terminal SOP value) → time = 200 ÷ 130 ≈ 1.54 min ≈ 92 sec. Full-rate phase at 400 gpm for the remaining 2,250 gal (to reach a 2,450-gal trip target) → 2,250 ÷ 400 ≈ 5.625 min ≈ 338 sec. Total load time ≈ 430 sec.

## 4. Vapor-recovery / vapor-tightness worksheet

1. Connect the vapor-recovery coupler to the compartment's vapor dome/return fitting before enabling liquid flow — the liquid-valve interlock should refuse to open without a confirmed vapor-tight connection.
2. Confirm the vapor path reading (vacuum-assist systems: negative pressure, commonly around −1 to −3 in. w.c. at the connection during flow; balance systems: confirm the return line is open and unobstructed).
3. Terminal vapor-collection efficiency requirement: ≥98% capture (per NESHAP Subpart R practice for gasoline distribution) — a coupler that isn't seated, or a return line valved shut, defeats this regardless of what the liquid side is doing.
4. Where the cargo tank's own vapor-tightness certification is due (EPA Method 27 pressure/vacuum decay test), confirm the certification date is current before accepting the vehicle for vapor-recovery loading — an uncertified tank can't be verified vapor-tight at this rack even if the coupler physically connects.

Example: coupler connected, vacuum-assist reading −2 in. w.c. confirmed before liquid valve enabled; cargo tank's Method 27 certification dated 8 months prior, within the terminal's required interval — proceed.

## 5. Shipping paper / placard cross-check worksheet

1. Pull the shipping paper (bill of lading) proper shipping name, UN number, hazard class, packing group, and stated quantity.
2. Confirm these match the rack's selected product code exactly — not "close enough" (e.g., confirm PG II vs PG III if the product has both grades in service, since they carry different packaging requirements).
3. Confirm the metered/loaded quantity reconciles with the shipping paper's stated quantity, converting units as needed (volume ↔ weight via the product's stated density).
4. Confirm the vehicle's/vessel's placards match the hazard class and UN number on the shipping paper — for a dedicated single-commodity cargo tank, placards are usually permanent and only the shipping paper/BOL number changes per load; for a multi-commodity cargo tank or tank car, re-verify placards against the specific load just completed.
5. Do not release the vehicle/vessel until every field reconciles — a "probably a typo" quantity or class mismatch is a hold, not a judgment call.

Example: shipping paper states "Gasoline, UN1203, Class 3, PG II, 2,450 gal." Loaded quantity from the rack totalizer: 2,450 gal. Converted at 6.8 lb/gal (terminal-stated density): 2,450 × 6.8 = 16,660 lb — matches the paper's stated weight exactly. Placard: FLAMMABLE (UN1203), present and correct for this dedicated cargo tank — release proceeds.

## 6. Marine transfer — Declaration of Inspection (DOI) worksheet

1. Complete the joint vessel/facility Declaration of Inspection (USCG 33 CFR 154/155 practice, commonly logged on a form equivalent to CG-3760) before any hose is connected.
2. Confirm both parties have signed off on: communication method between vessel and dock, emergency shutdown procedure and signal, transfer rate agreed and maximum rate the receiving side can accept, and vapor-return line status if applicable.
3. Re-confirm the DOI at any watch change or extended hold during the transfer — a DOI signed at the start of a multi-hour transfer doesn't cover a crew change partway through without a re-confirmation per the facility's procedure.
4. File the completed DOI with the transfer log; an unsigned or incomplete DOI is a hold, not a paperwork formality to complete after the fact.

Example: Tanker transferring 4,000 bbl of gasoline blendstock to a shore tank. DOI signed by both vessel mate and dock supervisor at 0600, transfer rate capped at 1,200 bbl/hr per the shore tank's receiving limit, emergency shutdown signal confirmed as three short whistle blasts plus radio call. Watch change at 1000 — DOI re-confirmed by incoming dock supervisor before transfer resumes.
