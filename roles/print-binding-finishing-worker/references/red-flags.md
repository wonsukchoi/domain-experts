# Red flags

### Fold direction running against the paper's grain on coated or heavy stock
- **Usually means:** imposition or press-sheet orientation wasn't checked against grain direction before folding.
- **First question:** has the grain direction actually been confirmed on this specific stock lot, not assumed from the previous job?
- **Data to pull:** grain-direction test result (tear or fold test) on the current stock, imposition layout fold direction.

### Saddle-stitch booklet page count approaching or exceeding roughly 60-80 total pages
- **Usually means:** the job is near or past saddle-stitch's practical structural limit, where creep and spine bulk both become significant.
- **First question:** has creep compensation been calculated for this specific page count and stock caliper, or copied from a shorter job?
- **Data to pull:** page count, stock caliper, creep compensation values applied at imposition.

### A sample perfect-bound booklet showing pages that separate under a normal pull test
- **Usually means:** glue formulation isn't matched to the stock (commonly coated stock with a standard, non-coated-rated glue), or glue temperature was out of range during binding.
- **First question:** is the glue formulation rated for this specific stock's coating?
- **Data to pull:** glue formulation spec sheet, binder temperature log during the run, stock coating type.

### Collating/gathering sensor triggering a jam or fault mid-run without a corresponding spot-check
- **Usually means:** a signature hopper depleted or misfed at that point in the run, risking a missing or duplicate signature in output around that timestamp.
- **First question:** what output quantity was produced between the last verified-good spot-check and the fault?
- **Data to pull:** collating sensor fault log with timestamp, spot-check log timestamps and results before and after the fault.

### Design content placed within roughly 1/16"-1/8" of a trim or fold line
- **Usually means:** prepress didn't flag the design against this specific job's mechanical finishing tolerance.
- **First question:** does this press/trimmer's actual documented tolerance make this margin genuinely risky, or is it comfortably within spec?
- **Data to pull:** the finishing equipment's documented tolerance spec, the exact distance from content to the cut/fold line.

### Die-cutting registration marks not matching the current press sheet's actual printed registration
- **Usually means:** press sheet registration has drifted since the file was proofed, or the die-cutting setup wasn't re-registered to the current run.
- **First question:** when was registration on this press sheet last verified against the die setup?
- **Data to pull:** press sheet registration measurement, die-cutting setup registration reference, time elapsed since last verification.

### A trimmed sample showing inconsistent margins across different sheets in the same stack
- **Usually means:** the trimmer's clamp pressure or blade alignment has drifted, or sheets in the stack aren't jogged/aligned consistently before cutting.
- **First question:** does the inconsistency track a specific position in the stack (suggesting a jogging issue) or appear randomly (suggesting a trimmer mechanical issue)?
- **Data to pull:** margin measurements across multiple sample sheets, trimmer blade/clamp maintenance log.

### A new stock or binding-method combination running for the first time without a sample/proof binding
- **Usually means:** time pressure skipped the verification step for an untested combination.
- **First question:** has this exact stock-and-binding-method combination been run and verified before, or is it genuinely new?
- **Data to pull:** job history for this stock/binding combination, sample binding test results if one was performed.

### Lamination showing bubbling, delamination, or edge lifting on a sample
- **Usually means:** lamination temperature, pressure, or adhesive wasn't matched to the substrate, or the substrate wasn't fully dry/cured before laminating.
- **First question:** what substrate and ink/coating combination is being laminated, and is the laminate rated for it?
- **Data to pull:** lamination equipment temperature/pressure settings, substrate cure time before lamination, laminate film spec.

### A finished sample not checked against the approved proof before the full run releases
- **Usually means:** time pressure skipped the final verification step between finishing and shipping.
- **First question:** has anyone actually compared a finished, trimmed/bound sample side-by-side with the approved proof?
- **Data to pull:** the approved proof, a pulled finished sample from the current run.
