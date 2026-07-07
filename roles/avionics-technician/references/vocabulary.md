# Vocabulary

Terms generalists conflate that an avionics technician keeps sharply separate.

## Repairman certificate (14 CFR 65.101) vs. A&P certificate

A **repairman certificate** is issued to a named individual for one specific repair station's specific duties — it doesn't transfer if the person changes employers or the station's scope changes. An **A&P certificate** is a general, transferable credential authorizing airframe/powerplant work anywhere.

**In use:** "I can sign this off under my repairman certificate at this station, but if I move shops next month that authority doesn't come with me the way an A&P ticket would."

**Common misuse:** assuming any experienced avionics tech has blanket sign-off authority the way an A&P does, when a repairman certificate's scope is specific to one employer and one set of duties.

## STC vs. field approval vs. DER-approved data

An **STC** (Supplemental Type Certificate) is a durable, reusable approval for installing a specific modification on a specific airframe model, ideal when the alteration will repeat. A **field approval** (FAA Form 337 with FSDO data approval) is meant for a genuine one-off alteration with no covering STC. **DER-approved data** is an engineering disposition for a configuration question outside both.

**In use:** "We're doing this on six aircraft, not one — that's an STC situation, not a field approval, even though we already have the field-approval paperwork from last year's single job."

**Common misuse:** reusing a prior field approval as if it were a durable, repeatable approval path, when it was only ever valid for that one specific installation.

## TSO authorization vs. STC

A **TSO** (Technical Standard Order) authorization qualifies the equipment itself as an airworthy article, built and tested to a minimum performance standard. An **STC** authorizes installing that specific article in a specific airframe location. Both are required — one without the other doesn't make an installation legal.

**In use:** "The box has a valid TSO — that only means it's an approved article. We still need the STC or field approval that says it's approved to go in *this* airplane, in *this* location."

**Common misuse:** treating a TSO'd part as automatically legal to install anywhere, when the TSO says nothing about installation approval for a given airframe.

## AML STC vs. single-aircraft STC

An **AML (Approved Model List) STC** covers an equipment installation across a list of airframe models named in the STC — ideal for fleet or repeat installs. A **single-aircraft STC** (or one obtained for a specific model without an AML) covers only the model(s) explicitly listed, which may be one.

**In use:** "Check whether this transponder's STC is on an AML before assuming it covers our whole King Air fleet — some STCs for this same box only list the 200-series, not the 300."

**Common misuse:** assuming any STC for "this equipment" automatically covers every airframe model the shop happens to be working on.

## Bonding vs. grounding

**Bonding** is the low-resistance electrical connection between two conductive structures or components (equipment rack to airframe, for example), intended to keep them at the same potential and provide a return path for static/fault current. **Grounding** more specifically refers to a connection to the aircraft's designated ground/return system for a circuit's normal operating current.

**In use:** "This strap is a bonding jumper for static and lightning current — it's not the circuit's ground return, so don't size it like a power-return wire."

**Common misuse:** treating any strap or wire connected to structure as interchangeable "grounding," when bonding straps and circuit ground returns serve different functions and have different resistance requirements.

## DO-160 environmental category vs. TSO minimum performance standard

A **DO-160 environmental category** (per section — temperature/altitude, vibration, EMI, lightning, etc.) describes the environmental conditions the equipment is qualified to survive. The **TSO's minimum performance standard** describes the equipment's functional performance requirements (accuracy, response time). Passing one says nothing about the other.

**In use:** "It meets the TSO's accuracy spec fine — the question is whether its DO-160 Section 4 category covers the temperature this bay actually sees at altitude."

**Common misuse:** citing a TSO authorization as if it certifies the equipment for any environment, when environmental qualification is a separate, section-by-section DO-160 basis.

## Wiggle test vs. functional/operational check

A **functional or operational check** verifies the system performs its function under static, ground-power conditions. A **wiggle test** deliberately flexes connectors and wire bundles while monitoring the system, specifically to reproduce an intermittent fault the static check won't trigger.

**In use:** "It passed the operational check again — that doesn't rule anything out, we need an actual wiggle test correlated to when the flag drops."

**Common misuse:** treating a passed operational check as equivalent to a completed troubleshooting step for an intermittent fault, when it only rules out a fault that would show up under static conditions.

## LRU vs. shop-repairable unit

An **LRU** (Line Replaceable Unit) is designed to be swapped at the aircraft with basic tools and returned to service quickly; the removed unit is then either repaired at a shop capable of component-level work or exchanged. Not every LRU is a **shop-repairable unit** at the technician's own station — some are sealed, vendor-repair-only exchange items.

**In use:** "It's an LRU, so we can swap it on the ramp, but this particular receiver isn't shop-repairable here — it goes back to the vendor as a core exchange."

**Common misuse:** assuming "LRU" implies the technician's own shop can open it up and repair it, when LRU only describes ease of removal/replacement at the aircraft, not repair-level access.

## ADS-B Out vs. ADS-B In

**ADS-B Out** broadcasts the aircraft's own position/velocity data and is the mandated equipment under 14 CFR §91.225/91.227. **ADS-B In** receives traffic and weather data broadcast by other sources — it's optional and not what satisfies the mandate.

**In use:** "The mandate is about Out — In is a nice-to-have for traffic display, don't let the customer think adding In satisfies the compliance requirement."

**Common misuse:** treating an ADS-B In-only installation as contributing toward mandate compliance, when only Out equipment satisfies §91.225/91.227.

## WAAS vs. RAIM

**WAAS** (Wide Area Augmentation System) improves GPS position accuracy and integrity using ground reference stations and geostationary satellites, enabling precision approach minimums. **RAIM** (Receiver Autonomous Integrity Monitoring) is the receiver's own internal check that enough satellites are in view to detect a position error, used when WAAS coverage isn't available.

**In use:** "We lost WAAS coverage briefly there, so the receiver fell back to RAIM — that's a normal degraded-mode behavior, not a fault."

**Common misuse:** treating a "RAIM unavailable" annunciation as a hardware defect, when it's the receiver correctly reporting a satellite-geometry condition outside its control.

## AFM Supplement vs. POH

An **AFM Supplement** (Airplane Flight Manual Supplement) is the FAA-approved document issued with an STC that adds or modifies operating limitations/procedures for the installed equipment — it's part of the aircraft's approved data. The **POH** (Pilot's Operating Handbook) is the manufacturer's general operating manual and may not reflect equipment added after original delivery.

**In use:** "The autopilot's new mode isn't in the factory POH — it's in the AFM Supplement that came with the STC, and that supplement is what's actually binding."

**Common misuse:** referencing the original POH for procedures on equipment that was added later via STC, when the AFM Supplement is the controlling document for that equipment.

## Certificate of Conformance vs. FAA Form 8130-3

A **Certificate of Conformance** is a manufacturer's or vendor's statement that a part was built to its specification — it is not an airworthiness release. **FAA Form 8130-3** is the airworthiness approval/release tag confirming the part meets its approved data and is eligible for installation on a type-certificated aircraft.

**In use:** "A conformance certificate just says the vendor built it to spec — for it to go on this aircraft we need an actual 8130-3 tag."

**Common misuse:** accepting a certificate of conformance as sufficient documentation for installing a part on a certificated aircraft, when only an airworthiness release (8130-3 or equivalent) establishes that eligibility.
