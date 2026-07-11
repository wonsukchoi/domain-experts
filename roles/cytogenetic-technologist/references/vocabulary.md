# Vocabulary — Cytogenetics

### ISCN
The International System for Human Cytogenomic Nomenclature — the standardized syntax for writing chromosome findings (e.g., `47,XY,+8[2]/46,XY[18]`).
**In use:** "The ISCN string needs the cell counts in brackets, or the director's going to send it back."
**Common misuse:** Treated as a formatting style choice rather than a precise, parseable specification — omitting cell counts or using non-standard breakpoint notation changes what the string actually asserts.

### Clonal abnormality
A chromosome abnormality present in enough cells to meet ISCN's statistical threshold (2 cells for a shared gain/structural change, 3 for a shared loss), distinguishing a real finding from culture artifact.
**In use:** "One cell with -21 isn't clonal — I need three before I can report a monosomy."
**Common misuse:** Calling any deviant cell "clonal" or "mosaic" the moment it's observed, before checking whether a second/third matching cell exists.

### Mosaicism
The presence of two or more cytogenetically distinct cell lines in an individual derived from a single zygote.
**In use:** "The 15% abnormal clone on repeat FISH is consistent with true mosaicism, not a lab artifact — we counted enough cells to rule out artifact at that level."
**Common misuse:** Conflated with confined placental mosaicism (an entirely placental finding) or with a simple 1-cell karyotype outlier that hasn't met clonality criteria.

### Confined placental mosaicism (CPM)
A discordance between the chromosome constitution of the placenta (via CVS) and the fetus, where the abnormal clone is restricted to placental tissue.
**In use:** "The direct prep showed trisomy 16 but the cultured mesenchyme was normal — this reads as CPM, follow up with amniocentesis to confirm the fetus is unaffected."
**Common misuse:** Assuming a CVS abnormal result always reflects true fetal status without checking direct-prep vs. long-term-culture concordance.

### Band resolution
The level of detail visible in G-banded chromosomes, expressed as the approximate number of bands resolvable per haploid set (e.g., 400, 550, 850 bands); higher resolution requires longer, more synchronized culture.
**In use:** "This needs 850-band resolution to see that breakpoint — the routine 400-band prep from the stat workup won't show it."
**Common misuse:** Treating band resolution as a fixed lab standard rather than a per-case dial traded against turnaround time.

### Metaphase spread
A single cell arrested in mitotic metaphase and prepared on a slide, showing its full complement of condensed chromosomes for analysis.
**In use:** "We only got twelve analyzable metaphase spreads off that harvest — not enough for a full count, needs a re-culture."
**Common misuse:** Conflated with "cell" generally; a poor-quality or overlapping spread doesn't count toward the analyzable total even though a cell is present on the slide.

### Karyotype
The organized, analyzed representation of an individual's full chromosome complement from a metaphase spread, written in ISCN shorthand.
**In use:** "The karyotype came back 46,XX,t(11;22)(q23;q11.2) — balanced reciprocal translocation, needs genetic counseling referral."
**Common misuse:** Used interchangeably with "chromosome test" broadly, blurring the distinction from FISH or microarray, which answer different questions at different resolutions.

### FISH (Fluorescence In Situ Hybridization)
A targeted probe-based technique that detects a specific DNA sequence's presence, location, or copy number in interphase or metaphase cells.
**In use:** "FISH for BCR-ABL1 came back positive on 40% of nuclei — faster answer than waiting on the karyotype, but it only tells us about that one fusion."
**Common misuse:** Treated as a genome-wide screen; FISH only detects what its specific probe targets and says nothing about the rest of the genome.

### Chromosomal microarray (CMA)
A genome-wide test for copy-number gains and losses at much higher resolution than karyotype, performed directly on extracted DNA without cell culture.
**In use:** "CMA picked up a 400 kb deletion the karyotype would never have resolved — but it's blind to the balanced translocation we're also worried about, so karyotype still needs to run."
**Common misuse:** Assumed to be a strict upgrade over karyotype in all cases; it cannot detect balanced structural rearrangements at all.

### Maternal cell contamination (MCC)
Presence of maternal cells within a fetal specimen (amniotic fluid, CVS, products of conception) that can produce a false result if not identified.
**In use:** "The mosaic result on that amnio needs an MCC workup with maternal STR markers before we finalize it as fetal."
**Common misuse:** Assumed to only matter for "abnormal" results; MCC can also mask a true fetal abnormality by diluting it with normal maternal cells.

### Synchronization (cell-cycle)
A culture technique (e.g., methotrexate or thymidine block) that arrests cells at a uniform point, increasing the yield of high-resolution prometaphase spreads.
**In use:** "We synchronized this culture for the high-resolution request — expect a longer turnaround than the routine 550-band prep."
**Common misuse:** Applied by default to every case rather than reserved for cases specifically needing elevated band resolution, wasting turnaround time.

### Colcemid arrest
Mitotic-spindle-inhibitor exposure that halts cells in metaphase for harvesting; exposure duration trades metaphase yield against chromosome condensation (length/bandability).
**In use:** "That harvest had too long a colcemid exposure — plenty of metaphases, but the chromosomes are too short to band well."
**Common misuse:** Treated as a fixed step rather than a tunable parameter the technologist adjusts per specimen and resolution target.

### Reflex testing
A pre-specified or case-driven decision to run an additional test (FISH, microarray, maternal comparator) based on an initial result, rather than as the original order.
**In use:** "The karyotype found a possible trisomy 8 clone in 2 of 20 cells — reflexing to FISH to quantify it before this goes out."
**Common misuse:** Skipped under turnaround pressure, resulting in a bare, unconfirmed percentage going out on a clinically significant finding.

### Proficiency testing (PT)
Externally provided, blinded specimens a laboratory analyzes to verify its performance against an expected result, a CLIA/CAP compliance requirement.
**In use:** "PT sample came back matching the expected 47,XY,+21 — documented and filed for the CAP inspection."
**Common misuse:** Treated as a bureaucratic formality rather than the mechanism that catches systematic count/resolution/reporting drift before it reaches patient specimens.
