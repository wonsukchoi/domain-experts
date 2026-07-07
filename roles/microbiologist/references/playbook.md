# Microbiologist — Playbook

## Identification-tier decision table

| Consequence tier | Example | Method | Turnaround | Confidence |
|---|---|---|---|---|
| Routine/low | Grade C environmental trending, non-critical area | Biochemical panel (API-strip) or MALDI-TOF | 1–2 days | Species-level, presumptive-to-confident |
| Elevated | Grade B environmental excursion, repeat isolate at same location | MALDI-TOF + confirm against reference library match score ≥2.0 | 1–2 days | Species-level, confident |
| High/regulatory | Sterility test failure, suspected outbreak, ambiguous MALDI-TOF score <1.7 | 16S rRNA sequencing (or send-out reference lab) | 3–5 days | Species-level, sequence-confirmed |
| Source-attribution required | Any high-consequence finding where a specific source must be named | Strain typing — PFGE or whole-genome sequencing, on all candidate isolates | 5–10 days | Strain-level |

Rule: never report a source conclusion above "leading hypothesis" without a strain-level match. Species-level match alone downgrades the conclusion language to "consistent with, not confirmed."

## Growth-kinetics back-calculation worksheet

Formula: doublings = log2(N_t / N_0); generation time = t / doublings.

| Measurement | Value |
|---|---|
| N_0 (OD600 or CFU/mL at t=0) | 0.05 |
| N_t (OD600 or CFU/mL at t=4h) | 0.40 |
| Doublings = log2(0.40/0.05) | log2(8) = 3.0 |
| Generation time = 4h / 3.0 | 80 min |

Applying to a field timeline: if a colony count of X CFU is observed at detection, and the generation time is known from a parallel lab culture, back-calculate plausible onset time = detection time − (generation time × doublings needed to reach the observed count from a single-cell or low-level start). Cross-check the resulting window against process/access records for a physically plausible mechanism — a timeline with no corresponding process event is a signal the growth-rate assumption (lab conditions vs. field conditions) needs revisiting, not that the mechanism is confirmed.

## Source-investigation sequence (filled example)

1. **Collect all candidate isolates** — product isolate, environmental isolates from the implicated area and time window, personnel isolates if gowning breach is suspected.
   - *Example:* Product isolate (sterility failure), Grade B gowning-room surface isolate (T-36h), Grade C corridor isolate (unrelated, same week) — 3 isolates collected.
2. **Species ID all isolates** to the tier the case requires (high-consequence = sequence-confirmed).
   - *Example:* All three confirmed *Staphylococcus epidermidis* by 16S rRNA sequencing.
3. **Screen for plausible exposure window** using growth-kinetics back-calculation and process/access records.
   - *Example:* 80-minute generation time consistent with a T-36h introduction matching the Grade B gowning-room detection.
4. **Strain-type all candidate-source isolates against the product isolate.**
   - *Example:* PFGE — product isolate and Grade B isolate: indistinguishable pulsotype. Grade C isolate: distinct pattern, excluded.
5. **State the conclusion at the evidentiary tier actually reached** — "confirmed common source" only with strain-level match; otherwise "consistent with, unconfirmed."
   - *Example:* Confirmed common source, Grade B gowning-room breach — strain-typing-supported.

## Antimicrobial susceptibility applicability check (filled example)

| Isolate | Drug tested | CLSI category match? | Reportable? |
|---|---|---|---|
| *S. epidermidis* | Oxacillin | Yes — Staphylococcus spp. table | Yes — S/I/R reported |
| *S. epidermidis* | Vancomycin | Yes — Staphylococcus spp. table | Yes — S/I/R reported |
| *S. epidermidis* | Ceftazidime | No — table validated for Gram-negatives, not applicable to Staphylococcus | No — "no interpretive criteria available," not force-reported |

The third row is the standard trap: lab software auto-populates a zone diameter for every drug on the panel regardless of organism-category validity; reporting it as a real S/I/R call is a documented CLSI-compliance finding.
