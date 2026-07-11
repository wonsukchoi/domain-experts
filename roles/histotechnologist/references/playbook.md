# Playbook — fixation through slide sign-off

Filled protocol tables and step sequences a histotechnologist executes, with plausible real-world parameters. Verify against the local lab's validated SOPs before use — accredited labs must validate every protocol independently.

## 1. Fixation and processing parameters by specimen type

| Specimen type | Fixative | Min-max fixation time | Processing note |
|---|---|---|---|
| Routine surgical (skin, GI biopsy, breast core) | 10% neutral buffered formalin (NBF), 10:1 volume ratio | 6-72 hr | Standard 8-12 hr overnight processor cycle |
| Breast core/excision for ER/PR/HER2 | 10% NBF | 6-72 hr (ASCO/CAP-mandated window) | Document actual collection-to-formalin start time, not accession time |
| Large resection (colon, lung lobe) | 10% NBF | 24-48 hr typical for adequate penetration at ~1mm/hr | May need extended processor cycle for fatty/large tissue |
| Bone/heavily calcified | 10% NBF, then decalcify | Fixation 6-72 hr, then decal (see table 2) | Decal choice trades speed against future IHC/molecular testing |
| Renal biopsy (light microscopy portion) | 10% NBF or Zenker-type per protocol | Per protocol, often shorter | Cut thinner (1-3 microns) for glomerular detail |
| Intraoperative (frozen) | None — fresh/unfixed, OCT-embedded | N/A | Cryostat cut, target read-out under 20 min from receipt |

## 2. Decalcification method comparison

| Method | Typical time (small bone core) | Effect on morphology | Effect on IHC/molecular | When to default |
|---|---|---|---|---|
| Formic acid (5-10%) | 2-6 hr | Good | Moderate antigen/DNA degradation | Turnaround is the binding constraint and no IHC/molecular workup is anticipated |
| Nitric acid (5-10%) | 1-4 hr (fastest) | Can be harsher on nuclear detail if over-decalcified | Highest degradation risk | Only when speed is critical and morphology-only read is expected |
| EDTA (10-14%, chelating) | 1-5+ days | Excellent | Best preservation of antigenicity and DNA | Any specimen where IHC or molecular testing is foreseeable (e.g., bone marrow core with suspected lymphoma) |

**Endpoint check:** determine end of decalcification by a chemical (ammonium oxalate test) or radiographic/physical flexibility check — never by elapsed time alone; over-decalcification is a common, avoidable source of poor nuclear detail and antigen loss.

## 3. Microtomy section-thickness targets

| Application | Target thickness | Notes |
|---|---|---|
| Routine H&E, most surgical specimens | 4-5 microns | Standard water bath ~8-10°C below paraffin melt point |
| IHC | 3-4 microns | Thinner sections give more even antigen exposure |
| Renal biopsy (light microscopy) | 1-3 microns | Needed for glomerular basement membrane detail |
| Frozen section | 4-8 microns | Cryostat chamber typically -18 to -22°C |

## 4. Artifact troubleshooting matrix

| Artifact | Most likely cause (check first) | Second cause | Fix |
|---|---|---|---|
| Chatter / venetian-blind lines across ribbon | Block-to-water-bath temperature mismatch | Dull or nicked blade edge | Re-chill or re-warm block to match bath temp; rotate/replace blade |
| Wrinkles or folds on mounted section | Water bath temperature too low, section not floating out fully | Section picked up too fast | Raise bath temp slightly (within target range), slow pickup |
| Holes / tissue tears | Hard inclusions (calcium, suture) not detected pre-cut | Dull blade dragging tissue | Re-face and re-examine for calcification; new blade |
| Incomplete deparaffinization before staining | Bake/deparaffinization step shortened for turnaround | Oven temperature below spec | Verify oven temp log; extend deparaffinization, do not skip for TAT |
| Section detaches during IHC run (heat-induced retrieval) | Poor slide adhesive/charge or inadequate baking | Retrieval buffer boiling too vigorously | Use charged slides, verify bake time, moderate retrieval boil |
| Floater — tissue fragment inconsistent with specimen | Cross-contamination during flotation/embedding | Cassette mix-up upstream | Reconcile block/slide/cassette count before sign-out; do not pass as incidental finding |

## 5. IHC antigen retrieval defaults

| Retrieval buffer | Typical pH | Default use | Note |
|---|---|---|---|
| Citrate buffer | pH 6.0 | Broad default for many antibodies | Gentler, lower risk of tissue detachment |
| EDTA/Tris-EDTA | pH 9.0 | Antibodies validated as needing high-pH retrieval (e.g., some nuclear markers) | Higher retrieval strength, can increase background if over-retrieved |

**Default:** use the antibody manufacturer's validated retrieval condition; when validating a new antibody in-house, start with citrate pH 6 unless literature/vendor data specifies high-pH retrieval.

## 6. Turnaround-time benchmarks (CAP Q-Probes-informed)

| Phase | Target |
|---|---|
| Accession to gross | Same day for routine specimens |
| Gross to stained slide (routine biopsy, no decal) | Next business day |
| Frozen section receipt to pathologist read-out | Under 20 minutes |
| Case with decalcification | Add 1-5+ days depending on decal method chosen (table 2) |
| IHC reflex stain (same block) | Add 1 business day beyond the H&E |

## 7. Level-banking rule for limited specimens

When the specimen is a core needle biopsy, GI pinch biopsy, or other tissue with an estimated block-face depth under ~1mm:

1. Face the block only to the point where a full, even tissue face appears (typically 20-50 microns of facing waste).
2. Cut and bank 8-12 unstained sections onto charged slides before running the currently ordered stain — this preserves material for later deeper levels, special stains, or IHC without re-facing into an already-thin block.
3. Log the number of banked unstained slides in the LIS against the block number, so the pathologist or a later tech knows material is already available before ordering a re-cut that would consume more tissue.
4. If the pathologist's order is later expanded (e.g., "add p53 IHC"), pull from the bank first; only re-face the block if the bank is exhausted.
