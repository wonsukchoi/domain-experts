# Red flags — histotechnology quality and case-level signals

### Documented fixation time under 6 hours or over 72 hours before a hormone-receptor/HER2 IHC stain
- **Usually means:** the true fixation-start time (collection, not accession) wasn't checked before processing, or a courier/weekend delay pushed the case past the window unnoticed.
- **First question:** what does the referring clinic's collection log say the actual formalin-immersion time was, not the lab's receipt timestamp?
- **Data to pull:** specimen collection/transport log and processing-start timestamp from the LIS; compare against the ASCO/CAP 6-72 hr window.

### Chatter or venetian-blind lines across more than a few sections in one cutting session
- **Usually means:** block-to-water-bath temperature mismatch, more often than blade dullness on its own.
- **First question:** was the block re-chilled/re-warmed to the bath's target range before cutting resumed?
- **Data to pull:** water bath temperature log and time-since-last-blade-change for that station.

### An unexpected or inconsistent tissue fragment on a slide relative to the specimen's expected histology
- **Usually means:** a floater — cross-contamination during flotation or embedding — more often than a true incidental finding.
- **First question:** does the fragment's tissue type match anything else processed in the same run or water bath?
- **Data to pull:** block/slide/cassette reconciliation log for the run; CAP Q-Probes benchmarks extraneous-tissue contamination in the low single-digit percent of cases, which is high enough to rule out systematically.

### Positive or negative control tissue fails to stain as expected on an IHC or special-stain run
- **Usually means:** a run-level reagent, retrieval, or instrument problem, not a case-specific tissue issue.
- **First question:** did every case on that run share the failure, or only the flagged one?
- **Data to pull:** reagent lot number and expiration, retrieval buffer pH/time log, and control-tissue result across the whole run.

### Same block re-cut requests from one pathologist exceeding roughly 5% of that pathologist's cases in a month
- **Usually means:** initial facing/leveling technique isn't reaching diagnostic tissue on the first pass, or orientation at embedding doesn't match what's being asked for (margins, perpendicular sectioning).
- **First question:** are the re-cut requests concentrated on one specimen type (e.g., skin punches needing perpendicular orientation) or spread evenly?
- **Data to pull:** re-cut/recut-reason log tagged by specimen type and original embedding orientation.

### Decalcification endpoint determined by elapsed time alone, with no chemical or physical check
- **Usually means:** the protocol defaults to a fixed clock time regardless of specimen density, risking over- or under-decalcification.
- **First question:** was an ammonium oxalate (or equivalent) endpoint test or a flexibility check run before moving the tissue to processing?
- **Data to pull:** decalcification log showing time in solution against the endpoint-test result, per specimen.

### Turnaround time for a routine biopsy without decalcification or consult exceeding 2 business days from gross to stained slide
- **Usually means:** a processing-queue or staining-backlog bottleneck rather than a case-specific complexity issue.
- **First question:** which phase — processing, embedding, cutting, or staining — is where the case is actually sitting?
- **Data to pull:** LIS phase-by-phase turnaround report for the case and the day's overall queue volume.

### A limited biopsy (core needle, GI pinch) arrives at sign-out with zero banked unstained levels and an added-stain order
- **Usually means:** initial microtomy cut only to the originally ordered stain without banking extra sections, and the block may now be too shallow to re-face.
- **First question:** how much block face depth remains, and is it enough for the newly ordered stain without exhausting the specimen?
- **Data to pull:** original facing/level log for the block and a fresh face-depth estimate before attempting the cut.

### Frozen section turnaround from tissue receipt to pathologist read-out routinely exceeding 20 minutes
- **Usually means:** cryostat temperature not matched to tissue type, or embedding/orientation problems requiring re-cuts under time pressure.
- **First question:** is the delay in embedding/orientation, in cutting, or in staining?
- **Data to pull:** frozen-section time-stamped log broken out by phase, benchmarked against the department's target.
