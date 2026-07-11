# Histology bench playbook

Filled reference tables and step sequences for the most common technical decisions. Populate a lab's own validated SOP values where they differ — these are working defaults, not a substitute for the local procedure manual.

## 1. Fixation and sectioning-thickness quick reference

| Specimen type | Max intact thickness before bread-loafing | Fixation window (10% NBF) | Routine section thickness |
|---|---|---|---|
| Core/needle biopsy | already ≤3mm — no bread-loaf needed | 6–24h | 4–5 microns |
| Punch/shave skin biopsy | already ≤3mm | 6–24h | 4–5 microns |
| Excisional biopsy / lumpectomy | bread-loaf at 0.5cm intervals if >3cm in any dimension | 6–72h (validated window for ER/PR/HER2) | 4–5 microns |
| Mastectomy / large resection | bread-loaf at 0.5cm intervals | 6–72h for IHC-ordered cases; up to 48h routine | 4–5 microns |
| Renal biopsy (native/transplant) | already thin — handle as core | 6–24h for the light-microscopy portion; the immunofluorescence portion goes in Michel's transport medium, not NBF — confirm specimen triage before fixing anything | 2–3 microns |
| Peripheral nerve biopsy | already thin | 6–24h | 2–3 microns |
| Lymph node (excisional) | bread-loaf at 0.3–0.5cm intervals | 6–48h | 3–4 microns |
| Bone / bone marrow core | decalcify after adequate fixation (see §3) | fix 6–24h before decal | 3–5 microns |

Ratio rule for all types: **specimen:fixative volume ≥ 15:1**. Formalin volume needed (mL) ≈ tissue volume (cm³, approximated as L×W×H for a rough block) × 15. A specimen that doesn't fit this ratio in the container on hand needs a bigger container, not a shorter fixation clock.

## 2. Fixation-time deviation decision table

| Time in formalin before processing | IHC-dependent case (ER/PR/HER2, etc.) | Routine H&E-only case |
|---|---|---|
| < 6h | Out of validated window — hold, do not process; document and notify pathologist | Acceptable only for thin biopsies; hold larger specimens |
| 6–72h | Within validated window — proceed | Proceed |
| 72h–120h (weekend backlog) | Flag as extended fixation on requisition; most IHC still valid but document | Proceed, note extended fixation if unusually long |
| > 120h | Notify pathologist before proceeding — antigenicity loss risk for some markers | Generally still acceptable for H&E morphology |

## 3. Decalcification protocol (bone/marrow core)

1. Confirm adequate prior fixation (6–24h in 10% NBF) before starting decal — decalcifying underfixed tissue compounds artifact.
2. Select reagent: rapid acid decal (e.g., formic acid-based) for routine H&E-only cases; EDTA (slower, gentler) when downstream IHC or molecular testing is anticipated.
3. Check end-point starting at the reagent's minimum expected time (varies by specimen density — do not guess from a fixed day count).
4. Run the chemical end-point test (e.g., ammonium oxalate test: combine spent decal solution with ammonium oxalate reagent; a persistent cloudy precipitate means calcium is still present and decal is incomplete; a clear result means the test point has been reached).
5. Record reagent, start time, end time, and end-point test result on the case log — not just "decalcified."
6. Rinse thoroughly before processing to prevent residual acid from degrading downstream staining.

## 4. Microtomy artifact troubleshooting sequence

| Artifact | Check 1 | Check 2 | Check 3 |
|---|---|---|---|
| Chatter (fine compression lines) | Blade nick/dullness — change blade | Block face temperature (too warm) — re-chill on cold plate | Clearance angle setting for tissue type |
| Venetian-blind (wide alternating bands) | Blade dull across a wider zone — rotate/replace blade | Block too soft (needs more chilling or a different paraffin blend) | Cutting speed too fast for tissue density |
| Wrinkling on water bath | Bath temperature too low relative to paraffin melting point (~10°C below) | Section picked up too slowly, cooled before flattening | Paraffin type mismatch for ambient lab temperature |
| Tissue/section loss from slide | Bath too hot — tissue over-expanded and torn | Poor adhesive/charge on slide | Slide not fully dried before staining |
| Holes/tears in section | Calcified or under-decalcified focus | Necrotic/friable tissue needing a different processing schedule | Blade damage at that specific point on the edge |

## 5. IHC control and retrieval troubleshooting sequence

When a stain looks weak, absent, or unexpectedly strong, work in this order — not by changing antibody concentration first:

1. **Check the positive control on the same slide/run.** If it failed, the run is invalid regardless of what the patient tissue shows — do not interpret the patient result.
2. **Check the retrieval method against that antibody's validation sheet** (buffer, pH, time, temperature) — a mismatch here is the most common cause of a weak-but-present stain.
3. **Check reagent lot and expiration** — an expired or near-end-of-life antibody lot degrades gradually, not as a hard failure.
4. **Check fixation time/type on the block** — under- or over-fixed tissue can blunt antigenicity in ways no amount of retrieval or concentration adjustment fixes.
5. **Only after 1–4 are cleared**, consider antibody concentration or incubation time adjustment, and re-validate with controls before applying to the next patient case.

## 6. QC log entry — filled example

```
Date: 2026-03-11        Run/batch ID: HE-0311-B
Stain: H&E (routine)     Reagent lot: Hematoxylin #H2241, Eosin #E1187
Slides through current hematoxylin since last change: 412
Control slide included: Yes — tonsil control, nuclear/cytoplasmic detail clear
Water bath temp at run start: 47°C (paraffin mp 56°C — within 10°C target)
Deviations noted: None
Technologist: [initials]     Reviewed by: [initials/date]
```

```
Date: 2026-03-11        Case ID: S26-04471
Stain: HER2 IHC          Antibody lot: HER2-4B5 #Q3312, exp 2026-09
Retrieval: HIER, citrate pH 6, 20 min, 110°C pressure cooker
Positive control: Cell line control, 3+ membranous staining as expected
Negative control: Same slide, no primary — clean
Fixation time on block: 18h in 10% NBF (within 6–72h validated window)
Deviations noted: None — result eligible for pathologist interpretation
Technologist: [initials]     Reviewed by: [initials/date]
```

## 7. Floater investigation checklist (fallback position order)

1. Compare floater morphology/tissue type against the case's own diagnosis and known history — does it plausibly belong?
2. Pull the block list for every case processed in the same run/session and compare grossly.
3. Check the water bath log — was it cleaned between cases, and which cases shared it that shift?
4. Check the microtome blade-change log — was the same blade used across multiple cases without a change?
5. If no match found and the floater is diagnostically significant (e.g., malignant cells on a benign case), escalate to the pathologist and lab director immediately — do not wait for the investigation to fully resolve before flagging the case.
6. Document the investigation outcome on the case regardless of whether a source was found, including "source undetermined" as a valid documented conclusion.
