# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Aseptic vs. sterile

- **Definition:** sterile is an absolute state — free of all viable microorganisms. Aseptic technique is the set of practices used to prevent introducing contamination while working with something that either is sterile or is being kept as clean as the assay requires; it doesn't guarantee sterility on its own.
- **Practitioner usage:** "The media's sterile out of the bottle — the risk is my aseptic technique introducing something while I pipette it into the flask."
- **Common misuse:** treating "I used aseptic technique" as equivalent to "nothing got in." Aseptic technique lowers contamination probability; it doesn't verify a negative. That verification is what an uninoculated media control is for.

## Efficiency vs. R² (qPCR)

- **Definition:** efficiency describes how well the reaction doubles template per cycle (100% = doubling; derived from the standard curve slope). R² describes how well the standard-curve points fit a straight line. They measure different things — a curve can be near-perfectly linear and still systematically inefficient.
- **Practitioner usage:** "R² is 0.999, but efficiency is 78% — the curve is a clean line, it's just the wrong slope. That's not a passing curve."
- **Common misuse:** reading a high R² alone as "the curve is good." R² catches noise; it doesn't catch systematic bias, which is the more common real failure mode (usually pipetting-driven).

## Passage number

- **Definition:** the count of times a cell line has been subcultured (split and regrown) since it was thawed or established. Not a measure of time in culture, and not interchangeable across cell lines from different sources.
- **Practitioner usage:** "This HEK293 line is at passage 34 — past our cutoff of 30 for transfection experiments; pull a lower-passage vial from the bank."
- **Common misuse:** assuming passage number is comparable across lines or labs. A cutoff established for one line at one lab (based on when its behavior started drifting) doesn't transfer to a different line, different medium, or different split ratio.

## Biosafety level (BSL) vs. "biohazard"

- **Definition:** BSL (1–4) is a specific containment classification tied to the agents in use and the required engineering controls, PPE, and procedures — not a general vibe of "this is dangerous." "Biohazard" is the broad category; BSL is the operational answer to "which controls apply here."
- **Practitioner usage:** "We're BSL-2 for this cell line because of the lentiviral vector, even though the parental cells themselves would be BSL-1."
- **Common misuse:** assuming a whole lab or a whole cell line carries one BSL rating regardless of what's introduced into it. The rating follows the highest-risk agent or manipulation present in that specific protocol, not the room.

## Calibration vs. verification

- **Definition:** calibration compares an instrument's output against a known reference and adjusts or documents the deviation across its range. Verification is a lighter, often daily, spot-check (e.g., a single check-weight on a balance) confirming it's still behaving as of last calibration — it doesn't replace calibration.
- **Practitioner usage:** "Daily check-weight passed, so the balance is fine for today's use, but it's still due for its annual calibration next month."
- **Common misuse:** treating a passing daily verification as proof the instrument doesn't need its scheduled full calibration. Verification catches gross failure; it can't catch a slow drift within the range it checks.

## Chain of custody

- **Definition:** an unbroken, documented record of who had physical possession of a sample, when, and under what conditions, from collection through disposition — distinct from the general lab notebook, which records what was done to a sample, not who held it and when.
- **Practitioner usage:** "This is a regulated specimen — it needs its own chain-of-custody form, signed at every handoff, not just an ELN entry."
- **Common misuse:** assuming a thorough ELN record satisfies chain-of-custody requirements. A chain-of-custody form exists specifically because it can't be reconstructed after the fact the way a notebook entry sometimes can be.

## Lot vs. batch

- **Definition:** lot is the manufacturer's traceable production unit for a reagent (what's on the certificate of analysis); batch, in a bench context, more often refers to a technician's own prepared working solution (e.g., a batch of master mix made from that lot). Conflating them loses the ability to trace a problem to its source.
- **Practitioner usage:** "The lot number on the antibody is fine — the issue is the batch of blocking buffer I made from it Tuesday, which sat out too long."
- **Common misuse:** logging only the reagent lot and not the prep batch (or vice versa), which halves the diagnostic value of the record when troubleshooting starts.

## Deviation vs. out-of-specification (OOS)

- **Definition:** a deviation is any departure from the SOP as written, whether or not it affects the result. OOS specifically means a measured value (a control, a QC check, a calibration) falls outside its defined acceptance criterion. Every OOS traces to some deviation, but most deviations never become OOS.
- **Practitioner usage:** "It's a logged deviation — we used lot B instead of lot A — but the controls still passed, so it's not OOS."
- **Common misuse:** using the terms interchangeably, which causes people to either under-report harmless deviations (afraid it implies a failed result) or under-investigate a real OOS by filing it as "just a deviation."

## Contemporaneous documentation

- **Definition:** recording an observation or action at the time it happens, not reconstructed afterward — one of the ALCOA+ principles (attributable, legible, contemporaneous, original, accurate, complete, consistent, enduring, available) underlying GLP-grade recordkeeping.
- **Practitioner usage:** "Log the incubation start time now, not at the end of the day — 'contemporaneous' is the whole point of the requirement."
- **Common misuse:** treating "I'll fill in the notebook later today" as equivalent to real-time logging. Same-day-but-later reconstruction is exactly where small, consequential details (a lot number, an off-schedule check) get lost or smoothed over.

## Validated vs. qualified (method / equipment)

- **Definition:** a validated method has documented evidence it consistently produces accurate, reliable results for its intended use across its full operating range. A qualified instrument has been shown to work correctly (installation, operational, and performance qualification) — necessary for a validated method, but not the same claim.
- **Practitioner usage:** "The plate reader is qualified and on schedule, but this particular assay hasn't been validated on it yet — we can't report quantitative results from that combination until it is."
- **Common misuse:** assuming a qualified instrument automatically means any method run on it is validated. Qualification is about the equipment; validation is about the specific method-instrument-analyst combination producing trustworthy results.
