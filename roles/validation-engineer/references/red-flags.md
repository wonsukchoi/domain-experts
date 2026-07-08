# Validation Engineer — Red Flags

Smell tests for auditing an existing validation package, protocol, or cleaning program before an inspection finds the gap first.

### PPQ batch count fixed at exactly 3 with no variability rationale in the file
- **Usually means:** the protocol writer defaulted to the retired Annex 15 convention instead of justifying the count from process variability, complexity, and prior-knowledge history.
- **First question:** "Where's the risk/variability rationale that supports three, and what would have changed the number?"
- **Data to pull:** the PPQ protocol's batch-count justification section (or its absence) and the process capability/Cpk history cited for it.

### Cleaning acceptance criterion set at 10 ppm or 1/1000-dose with no PDE/HBEL on file
- **Usually means:** the toxicological assessment was never commissioned, or was commissioned and the result quietly dropped because the legacy number was more generous.
- **First question:** "Has toxicology issued a PDE or HBEL for this compound, and if so, why isn't it the governing limit?"
- **Data to pull:** the toxicological assessment report (or ICH M7 TTC default citation) and the MACO calculation worksheet showing all three limits compared.

### Stage 3 continued process verification (CPV) trending absent or >12 months stale
- **Usually means:** the process was qualified once and the ongoing monitoring obligation lapsed — the validated state on file no longer reflects current reality.
- **First question:** "When did someone last look at the CPV trend, and does it still show the process in the qualified state?"
- **Data to pull:** the SPC/CPV trend charts and their last-reviewed date from the quality system.

### GAMP 5 category not documented for a computerized system before CSV/CSA scripting began
- **Usually means:** testing depth was set by habit (usually maximal, sometimes just copied from another system) rather than by the system's actual configurability and criticality.
- **First question:** "What GAMP category was this system assessed as, and where's the assessment?"
- **Data to pull:** the GAMP 5 category assessment memo and the CSV/CSA test plan it should have driven.

### Same CSV test script depth applied across systems of different GAMP categories
- **Usually means:** a Category 3 non-configurable COTS system is being over-tested while the actual risk — a Category 4 configured business-logic system — is under-tested by the same flat template.
- **First question:** "Show me the category assessment for each system these scripts cover — are they actually the same category?"
- **Data to pull:** the system inventory with GAMP categories mapped against the corresponding test script sets.

### Design verification (820.30(f)) evidence on file with no design validation (820.30(g)) against actual use conditions
- **Usually means:** the team confirmed the output matches the spec but never confirmed the spec reflects the real clinical or user need — "verified" is being presented as "validated."
- **First question:** "Where's the human-factors or simulated-use-conditions validation, separate from the spec-conformance testing?"
- **Data to pull:** the design history file's verification and validation sections, checked for whether validation used real or simulated actual-use conditions versus spec re-checks.

### Calculated LOQ with no confirmatory precision/accuracy run at that concentration
- **Usually means:** the analytical method validation stopped at the statistical estimate (from a calibration curve or signal-to-noise extrapolation) instead of empirically confirming it per ICH Q2.
- **First question:** "Is there a precision and accuracy data set actually run at the calculated LOQ concentration?"
- **Data to pull:** the method validation report's LOQ section and the raw data for the confirmatory runs at that level.

### Acceptance criterion in the summary report doesn't match the one in the approved protocol
- **Usually means:** the criterion was loosened after execution to make failing or borderline data pass — a post-hoc rationalization rather than a pre-specified decision.
- **First question:** "Pull the approved protocol version — does this criterion match what was signed before execution started?"
- **Data to pull:** the protocol's approval-dated version and the summary report, compared line by line on acceptance criteria.

### Deviation during protocol execution closed with no documented root cause
- **Usually means:** the deviation was dispositioned by re-test or waiver without actually identifying why the result fell outside the pre-specified criterion, leaving the underlying cause free to recur.
- **First question:** "What was the root cause, and what's the evidence it was actually the cause rather than the most convenient explanation?"
- **Data to pull:** the deviation/CAPA record and its root-cause investigation section.

### Business-critical GxP spreadsheet with unrestricted edit access and no validation record
- **Usually means:** the spreadsheet was never classified as a computerized system requiring validation because "it's just a calculation," despite functioning as the system of record for a regulated result.
- **First question:** "Who can edit this spreadsheet's formulas, and is there a version-controlled, validated copy anywhere?"
- **Data to pull:** the spreadsheet's access-control settings and any GAMP category assessment (or absence of one) covering it.

### Traceability matrix with test cases that don't map back to a numbered user requirement
- **Usually means:** test cases were written from the functional spec directly, skipping the step that confirms every user requirement actually got tested — coverage gaps hide here.
- **First question:** "Walk this test case back to the user requirement it's supposed to satisfy — which number is it?"
- **Data to pull:** the requirements-to-test-case traceability matrix, checked for orphaned test cases and untested requirements.

### Equipment qualified via traditional IQ/OQ/PQ with no risk-based verification tier assigned (ASTM E2500)
- **Usually means:** every commissioning activity was tested identically regardless of GxP criticality, over-testing utility-grade equipment and potentially under-scoping the truly product-critical steps.
- **First question:** "What risk tier was this equipment assigned, and does the verification depth actually track it?"
- **Data to pull:** the commissioning and qualification (C&Q) risk assessment and the verification test list it produced.

### Visually-clean check treated as the sole cleaning acceptance criterion, with no MACO limit behind it
- **Usually means:** the team over-corrected from "10 ppm isn't scientifically derived" all the way to dropping quantitative limits entirely, rather than keeping visually-clean as the supplementary screen alongside a PDE-based MACO.
- **First question:** "What's the quantitative swab or rinse limit this visual check is supplementing — where's that number?"
- **Data to pull:** the cleaning validation protocol's acceptance-criteria section, checked for a numeric MACO/swab limit in addition to the visual check.
