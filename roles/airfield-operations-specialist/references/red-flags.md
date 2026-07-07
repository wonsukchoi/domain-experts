# Red flags

Smell tests an operations supervisor or FAA certification inspector catches during a shift or an audit. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. Self-inspection interval exceeded during active precipitation

**Usually means:** staffing gaps or a competing priority (a construction escort, a wildlife call) pushed the inspection past the condition-driven interval, and the runway's actual condition is now older data than the escalation trigger requires.

**First question:** "What time was the last inspection, and what's the accumulation rate since then?"

**Data to pull:** inspection log timestamps against the ACM's condition-triggered frequency table; current precipitation rate/type; time since last RwyCC measurement.

## 2. RwyCC reported without a measured contaminant depth on file

**Usually means:** the code was assigned from visual impression rather than measured against the RCAM table — a common shortcut under time pressure that silently corrupts every downstream landing-distance calculation using that code.

**First question:** "What depth was actually measured for this contaminant, and on which runway third?"

**Data to pull:** the inspection log's depth measurement field (or its absence); the RCAM table entry that measurement maps to; comparison against the code actually reported.

## 3. NOTAM issuance more than a few minutes behind discovery

**Usually means:** the finding was batched for the next scheduled update or shift change instead of issued on confirmation — the gap between the two timestamps is the actual safety exposure window.

**First question:** "What time was this confirmed, and what time did the NOTAM actually post?"

**Data to pull:** inspection log confirmation timestamp versus NOTAM system origination timestamp; any operations happening on that surface during the gap.

## 4. A wildlife strike or sighting report doesn't generate a WHA evaluation

**Usually means:** the event meets an AC 150/5200-33C trigger criterion (damage, ingestion, hazardous species/quantity) but was treated as a one-off logged incident instead of routed into the WHA process.

**First question:** "Does this event meet a WHA trigger, and if so, where's the evaluation record?"

**Data to pull:** the strike/sighting report; the trigger checklist; the WHA/WHMP file for a corresponding entry and date.

## 5. FOD-walk frequency unchanged during active construction

**Usually means:** the routine schedule wasn't adjusted upward for the highest FOD-generation condition on the field — construction equipment and material handling produce debris at a materially higher rate than routine operations.

**First question:** "Has the walk frequency actually increased since this work period started, or is it still on the routine schedule?"

**Data to pull:** walk-frequency log before and after construction start date; any debris finds logged since; construction contractor's own housekeeping/FOD-control compliance record.

## 6. Pilot braking-action reports consistently worse than the published RwyCC

**Usually means:** the measurement or the mapping to the RCAM table is off, or conditions have deteriorated since the last inspection faster than the published code reflects.

**First question:** "How many braking-action reports have come in below the published code, and when was the code last updated?"

**Data to pull:** pilot report log against RwyCC amendment timestamps; re-inspection results following each discrepant report.

## 7. Habitat conditions drifting outside the Wildlife Hazard Management Plan's stated targets

**Usually means:** grass height, standing water, or food-source controls specified in the WHMP have lapsed (mowing schedule slipped, drainage issue unaddressed) and the airport is accumulating attractant risk ahead of the next seasonal peak.

**First question:** "What does the WHMP specify for this control, and what's the field condition right now?"

**Data to pull:** WHMP target specifications (mowing height, drainage standards); most recent habitat inspection against those targets; upcoming seasonal migration/breeding pattern for the species of concern.

## 8. NOTAM text uses free-form narrative instead of standardized field-condition phraseology

**Usually means:** the report wasn't built from the standard FICON/RCR format, which means downstream systems or pilots parsing it may miss an element that isn't in its expected field position.

**First question:** "Does this NOTAM follow the standard runway-condition-report format, field for field?"

**Data to pull:** the issued NOTAM text side by side with the standard FICON template; any recent format deviations flagged by the tower or a dispatch office.

## 9. Repeated strikes of the same species in the same season, year over year, with no WHMP update

**Usually means:** the underlying attractant was never identified or addressed after the first cluster, and dispersal (hazing) has been treated as the standing control instead of a stopgap pending a habitat fix.

**First question:** "What changed in the WHMP after last year's cluster, and did it address the attractant or just the symptom?"

**Data to pull:** multi-year strike data by species and month from the airport's wildlife log; WHMP revision history; habitat modification work orders since the last cluster.

## 10. A FOD-detection system alarm cleared without a physical inspection

**Usually means:** the alarm was dismissed as a probable false positive (debris blown across the field of view, equipment shadow) without sending someone to physically confirm — the one alarm that's real gets the same treatment as the nine that aren't.

**First question:** "Was this alarm physically verified, or just reviewed on the sensor feed?"

**Data to pull:** alarm log with dismissal method (physical check vs. remote review); false-positive rate for this sensor/location; time between alarm and any eventual physical FOD find at that location.

## 11. NOTAM canceled or amended immediately after a mitigation action, without a re-inspection

**Usually means:** the specialist assumed the plow pass, dispersal action, or debris removal fully resolved the hazard rather than confirming it — plowing can miss a section, dispersal can be temporary, removal can leave residual material.

**First question:** "Was this re-inspected after the mitigation, or was the NOTAM cleared on the assumption the action worked?"

**Data to pull:** timestamp of mitigation action versus timestamp of NOTAM cancellation/amendment; re-inspection record, if one exists, between the two.
