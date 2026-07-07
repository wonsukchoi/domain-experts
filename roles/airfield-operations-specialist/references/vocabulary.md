# Vocabulary

Terms generalists conflate that airfield operations specialists keep sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

### Runway Condition Code (RwyCC) vs. braking action report

**RwyCC** is the standardized 0–6 numeric code an airport operator assigns per runway third from measured contaminant type and depth against the RCAM table. A **braking action report** is a pilot's subjective in-the-moment assessment (Good/Medium/Poor/Nil) radioed after landing or taxiing. RwyCC is a measurement-derived code issued before the fact; a braking action report is real-time ground truth that can override it.

**In use:** "Published RwyCC was 4, but American just reported Poor on rollout — we're re-inspecting before the next arrival."

**Common misuse:** treating the two as interchangeable or assuming the published code is current once a pilot report contradicts it — the report supersedes the last measurement until confirmed.

### Movement area vs. non-movement area

The **movement area** is runways, taxiways, and other areas used for taxiing, takeoff, and landing, under air traffic control. The **non-movement area** includes ramps, gates, and aprons, typically under the airport operator's or airline's control, not ATC's.

**In use:** "FOD call is on the ramp, that's non-movement — no need to coordinate with the tower, just dispatch the crew."

**Common misuse:** assuming every airfield surface requires ATC coordination before entry; ramps and gate areas generally don't, and treating them as if they did adds unnecessary coordination delay.

### Wildlife Hazard Assessment (WHA) vs. Wildlife Hazard Management Plan (WHMP)

A **WHA** is the triggered, time-bound study (typically by a qualified biologist) identifying species, attractants, and risk after a qualifying strike or sighting event. A **WHMP** is the standing, ongoing plan — habitat modification targets, dispersal procedures, monitoring schedule — that a completed WHA feeds into and updates.

**In use:** "The WHA after the goose strike recommended draining that retention pond faster after storms — that's now in the WHMP as a standing target."

**Common misuse:** treating a WHA as a one-time report to file away rather than an input that should change the WHMP's ongoing targets.

### FOD (Foreign Object Debris) vs. FOD (Foreign Object Damage)

**Foreign Object Debris** is the physical object itself (a bolt, a pavement chunk, a luggage tag) present where it shouldn't be. **Foreign Object Damage** is the harm that debris causes once ingested or struck (engine damage, tire damage). The acronym is shared; the referent isn't.

**In use:** "We caught the debris on the walk before it became damage — that's the whole point of the program."

**Common misuse:** using "FOD" to mean only the damage outcome, which understates the value of debris removal as a preventive control rather than a post-incident cleanup.

### Self-inspection vs. Part 139 certification inspection

**Self-inspection** is the airport operator's own recurring internal check of the movement area per its ACM. A **Part 139 certification inspection** is the FAA's periodic audit of the airport's compliance with its certificate, including whether self-inspections actually happened as documented.

**In use:** "Self-inspection log needs to be airtight — that's exactly what the FAA pulls first during the 139 audit."

**Common misuse:** treating self-inspection as a formality performed for its own sake rather than as the record an external regulator will audit against the certificate.

### TALPA / RCAM

**TALPA** (Takeoff and Landing Performance Assessment) is the FAA rulemaking initiative, implemented across U.S. operations starting fall 2016, that created the standardized runway-condition reporting system. **RCAM** (Runway Condition Assessment Matrix) is the specific lookup table within TALPA that converts a contaminant's type and depth into a RwyCC.

**In use:** "Pull the RCAM row for wet snow over compacted snow at this depth — that's what sets the code, not a guess."

**Common misuse:** using "TALPA" and "RCAM" interchangeably; TALPA is the program, RCAM is the table it produced.

### Airport Certification Manual (ACM)

The FAA-approved, airport-specific document establishing self-inspection frequency, checklist content, wildlife and snow-removal procedures, and other Part 139 compliance details for that specific airport.

**In use:** "Our ACM sets self-inspection at three times daily minimum — the regulation's 'once daily' is the federal floor, not our actual schedule."

**Common misuse:** citing the federal "once daily" minimum as if it were the airport's actual required frequency, when the ACM's own (often stricter) schedule governs day to day.

### Hazing vs. depredation

**Hazing** is active, non-lethal wildlife dispersal (pyrotechnics, distress calls, vehicle harassment) used to move animals off the airfield in the moment. **Depredation** is the lethal removal of wildlife, typically requiring a separate federal or state permit, used when hazing repeatedly fails or the species/situation warrants it.

**In use:** "We've hazed this flock off three times this week — time to talk to the wildlife biologist about a depredation permit."

**Common misuse:** treating repeated hazing as a sustainable long-term control rather than a signal that the underlying attractant needs to be addressed or that depredation authorization should be pursued.

### FDC NOTAM vs. Distant (D) NOTAM

An **FDC NOTAM** originates from the FAA's National Flight Data Center and typically covers regulatory items (e.g., instrument procedure changes). A **Distant (D) NOTAM** is issued by the local facility and covers routine airfield items — runway/taxiway closures, lighting outages, obstacles — distributed nationally through the NOTAM system.

**In use:** "That's a D NOTAM for the taxiway light outage — doesn't need an FDC entry, this isn't a procedure change."

**Common misuse:** assuming all safety-relevant NOTAMs are the same type or come from the same originating authority; misclassifying one as the other can delay or misroute distribution.

### Field Condition (FICON) report / Runway Condition Report (RCR)

The standardized NOTAM subformat specifically for reporting per-third RwyCC and contamination type — the structured template the RwyCC string (e.g., `3/6/1`) is published inside, distinct from a general free-text NOTAM.

**In use:** "Don't free-text the snow condition — build it as a FICON so the RwyCC string parses the way dispatch systems expect."

**Common misuse:** writing a narrative description of runway condition instead of using the structured FICON fields, which risks a dispatch or flight-planning system failing to parse the report correctly.
