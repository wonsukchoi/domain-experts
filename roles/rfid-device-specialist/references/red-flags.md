# Red flags — rfid-device-specialist

### A zone's read rate drops but no hardware, firmware, or layout change is logged for that period
- **Usually means:** Stale WMS/ERP records, an ID mismatch between the tag encoding and the system of record, or a damaged/missing tag — the cheap causes that outnumber actual RF failures — rather than antenna detuning.
- **First question:** "Has anything physically changed in that zone, or is this the same hardware reporting a new number?"
- **Data to pull:** Zone-level read-rate trend line for the last 30 days against the facility change log (racking moves, new fixtures, door installs).

### A reference/witness tag's RSSI drifts more than roughly 10 dB from its install-day baseline
- **Usually means:** An environmental change near that antenna — new metal fixture, added moisture, layout shift — not tag wear or chip degradation (a passive tag doesn't "wear out" electrically over normal read counts).
- **First question:** "What changed in this zone's physical environment since the baseline reading was taken?"
- **Data to pull:** Reference-tag RSSI log since install, cross-referenced with the facility change log for that bay.

### In-situ return loss (S11) measures above −10 dB at an antenna after installation
- **Usually means:** The antenna's factory bench match no longer holds against the real environment — metal racking, a curved mounting surface, or proximity to a new structure has detuned it — and it needs re-matching on site, not a firmware or power adjustment.
- **First question:** "Was this antenna ever measured in situ after the racking and inventory were in place, or only on the bench?"
- **Data to pull:** VNA S11 sweep at the antenna's current mounting position, plus the original bench-test spec sheet for comparison.

### A reader keeps re-querying the same tag population without the count ever settling
- **Usually means:** Gen2's Q-algorithm working correctly against too many tags per query frame for the current Q value, not a malfunctioning reader or a collision bug.
- **First question:** "What's the current Q setting relative to the estimated tag count in this read zone?"
- **Data to pull:** Reader's Q-algorithm parameter log and an independent tag-count estimate for the zone (manual count or a slower single-antenna pass).

### A tag reads as present but its payload is garbled or incomplete
- **Usually means:** Partial power delivery through an obstruction — an obstructed tag can receive on the order of 10% of emitted energy, enough to wake the chip but not enough to backscatter a clean reply — rather than physical tag damage.
- **First question:** "Is there a metal or liquid obstruction between this tag and the antenna, and does the garbling clear if the item is repositioned?"
- **Data to pull:** Read log showing partial-vs-complete payload rate by tag position, plus a site photo/diagram of the obstruction.

### Specified reader power plus antenna gain pencils out above the regional EIRP/ERP ceiling (4 W EIRP FCC, 2 W ERP ETSI)
- **Usually means:** A spec sheet was assembled for maximum range without checking the math against the region the site actually operates in — the margin against the ceiling can look fine in one region and be blown by several dB the moment the same hardware pairing is quoted for the other.
- **First question:** "Was this EIRP/ERP math run against the site's actual regulatory region, or copied from a spec sheet written for the other one?"
- **Data to pull:** Reader transmit power and antenna gain spec sheets, plus the site's regulatory region.

### Blended read/accuracy rate reported to the client doesn't match the number in the original proposal
- **Usually means:** The proposal was priced off a vendor best-case or a named industry benchmark (e.g. the Auburn/GS1 US 95% figure) rather than a site-specific floor negotiated before go-live — the gap is an expectations problem, not necessarily a technical one.
- **First question:** "What accuracy floor was actually written into the SOW, and was it site-specific or the vendor's ceiling number?"
- **Data to pull:** Signed SOW/proposal accuracy commitment and the pilot's measured blended accuracy by lane/zone.

### One lane or antenna in a multi-lane portal underperforms the others by more than roughly 15 percentage points while the rest hit spec
- **Usually means:** A localized multipath null or detuned match at that specific antenna (often traceable to a nearby structure like a steel door), not a systemic reader, tag, or software fault — ruling out systemic causes first is what the per-lane breakdown is for.
- **First question:** "Is the underperformance isolated to one lane, or does it show up across all lanes equally?"
- **Data to pull:** Per-lane/per-antenna read-accuracy breakdown for the pilot window, plus reference-tag RSSI at the underperforming antenna.

### A pilot monitoring window runs less than roughly 2 weeks before go-live sign-off
- **Usually means:** Schedule pressure is compressing the phase that catches dead zones and environmental drift before the client does — deployments with 3+ months of planning and pilot testing succeed at roughly 94% versus about 47% for rushed rollouts.
- **First question:** "What's driving the shortened pilot window, and has that tradeoff been surfaced to the client explicitly?"
- **Data to pull:** Project timeline showing planned vs. actual pilot duration, and the pilot's read-rate trend over whatever window it did run.

### A legacy WMS/ERP integration ticket sits open with RFID reads arriving but nothing showing up downstream
- **Usually means:** The receiving system can't natively ingest RFID event data (it expects barcode-shaped scans), not a bad antenna layout or a reader configuration error — the fix is usually a middleware translation layer, not RF rework.
- **First question:** "Is the receiving system parsing the read events at all, or are they arriving and being silently dropped?"
- **Data to pull:** Middleware/integration log showing read events in versus records successfully written to the WMS/ERP.

### Client or floor staff describe the system in RTLS terms (real-time location, sub-meter positioning) for a passive UHF deployment
- **Usually means:** A capability mismatch has crept into the sales conversation or staff expectations — passive UHF delivers identity/presence, not the sub-meter positioning that belongs to UWB-based RTLS — and needs correcting before it becomes a contractual expectation.
- **First question:** "Where did the location-tracking expectation come from — was it ever actually scoped as RTLS?"
- **Data to pull:** Original proposal/SOW capability description and any client-facing materials that reference location or positioning.
