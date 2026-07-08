# Red flags

Smell tests a calibration technologist catches on a first pass over a certificate, an uncertainty budget, or an interval record.

### Certificate reports pass/fail with no measurement uncertainty stated anywhere

- **Usually means:** the uncertainty budget was never built, or was built but stripped from the customer-facing certificate, either of which means the accept/reject call can't be independently checked against a TUR or guard band.
- **First question:** does the lab's internal record (not just the customer certificate) contain a budget with sourced Type A/Type B terms, and if so, why isn't the expanded uncertainty on the certificate?
- **Data to pull:** the internal uncertainty budget worksheet for this calibration and the lab's certificate-content procedure (ISO/IEC 17025 §7.8 requires it be available on request at minimum).

### TUR reported as a single number with no denominator shown

- **Usually means:** it's unclear whether the ratio used the reference standard's uncertainty alone or the full measurement-process uncertainty (Type A + all Type B terms) — the two numbers are legitimately different (SKILL.md worked example: 4.8:1 vs. 4.18:1) and conflating them can hide a marginal calibration behind a comfortable-looking reference-only ratio.
- **First question:** is the reported TUR computed against the reference standard's expanded uncertainty only, or against the full combined-and-expanded measurement uncertainty including Type A repeatability and all Type B terms?
- **Data to pull:** the uncertainty budget's individual components and which subtotal fed the reported TUR.

### A reference standard's manufacturer accuracy spec is used directly as its standard uncertainty, with no divisor applied

- **Usually means:** the spec was treated as already being a standard uncertainty (1-sigma) when it's almost always either an expanded uncertainty (needs division by k, typically 2) or a bound on a rectangular/uniform distribution (needs division by √3) — using it raw overstates confidence and can silently pass a budget that shouldn't pass.
- **First question:** does the manufacturer or cert documentation state whether this figure is a standard uncertainty, an expanded uncertainty with a stated k, or a distribution bound, and was the correct divisor applied?
- **Data to pull:** the source spec sheet or certificate language for that term, and the budget worksheet's divisor column.

### Reference standard's calibration certificate is more than its stated interval past due, but was used anyway

- **Usually means:** the traceability chain is broken at this link — an expired cert's stated uncertainty no longer has a documented basis for still applying, since drift since the last calibration is now unbounded, not just unmeasured.
- **First question:** what is the reference standard's calibration due date, and is there a documented interim-check or extension basis if it's being used past that date?
- **Data to pull:** the reference standard's calibration due-date record and any documented extension/interim-verification basis.

### TUR is below roughly 4:1 but the certificate shows a straight pass/fail against nominal tolerance with no guard band applied

- **Usually means:** the lab's guard-banding policy for low-TUR calibrations wasn't applied, so a result near the tolerance edge may be reported PASS (or FAIL) at a false-accept (or false-reject) risk higher than the lab's stated policy allows.
- **First question:** what is this lab's documented TUR threshold for requiring guard banding, and does this calibration's TUR fall below it?
- **Data to pull:** the lab's Z540.3-based guard-banding procedure and this calibration's computed TUR.

### An instrument has been on the same calibration interval for years with no reference to its own in-tolerance/OOT history

- **Usually means:** the interval was never reviewed against Method A3 (or an equivalent) data, either leaving a stable instrument on an unnecessarily short (costly) interval or, more importantly, leaving a drifting instrument on too long an interval until it fails OOT in the field.
- **First question:** when was this instrument's (or its population's) interval last reviewed against its actual calibration history, and how many history points support the current interval?
- **Data to pull:** the calibration history log (as-found/as-left values across cycles) and the date of the last interval review.

### An out-of-tolerance finding has no documented impact assessment on measurements taken since the last good calibration

- **Usually means:** the OOT was corrected (re-cal, adjustment) without asking whether any product, test, or process data measured with the instrument while it was drifting out of tolerance is now suspect — this is a quality-system gap, not just a re-cal formality.
- **First question:** has anyone traced what was measured with this instrument between its last in-tolerance calibration and this OOT finding, and is an impact/recall assessment underway if warranted?
- **Data to pull:** the instrument's usage log or asset-tracking record for the period in question, and any customer notification or nonconformance record opened.

### A Type A uncertainty component is computed from fewer than about 3-5 repeat readings, or from a single reading

- **Usually means:** the sample size is too small for the standard deviation to be a stable estimate — a single reading gives no Type A information at all (u_A is undefined, not zero), and 2-3 readings produce a standard deviation with very high variance itself.
- **First question:** how many repeat readings were actually taken for the Type A component, and does the lab's procedure specify a minimum n for this parameter?
- **Data to pull:** the raw repeatability data set (not just the reported mean and standard deviation) for this test point.

### A budget's combined uncertainty is calculated by simple addition of Type A and Type B terms instead of root-sum-square

- **Usually means:** whoever built the budget didn't apply GUM combination rules, and simple addition overstates the combined uncertainty (each term is treated as if it moves in lockstep with the others, which is only correct for fully correlated terms).
- **First question:** were the individual components independent (uncorrelated), and if so, was root-sum-square used rather than linear addition?
- **Data to pull:** the budget worksheet's combination formula and a check of whether any flagged terms are genuinely correlated (which would legitimately change the combination method).

### Accreditation scope (CMC) claimed for a parameter/range that the lab's actual reference standards can't support at the stated uncertainty

- **Usually means:** either the scope document is stale relative to what reference standards are currently on hand and traceable, or a technician calibrated outside the lab's demonstrated measurement capability without flagging it.
- **First question:** does the current, traceable reference standard on the bench actually support the CMC uncertainty claimed in the lab's accreditation scope for this exact parameter and range?
- **Data to pull:** the accreditation body's published scope document and the specific reference standard's current certificate.
