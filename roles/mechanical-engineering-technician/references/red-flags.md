# Red flags — dimensional inspection, instrumentation, and test data

### CMM position report with no stated datum simulation method
- **Usually means:** the program defaulted to best-fit alignment without anyone deciding that was correct, or the drawing has no DRF and nobody flagged it.
- **First question:** does the drawing call out a datum reference frame, and if so, was the CMM program constrained to it in the stated precedence?
- **Data to pull:** the CMM program's alignment/fit settings and the drawing's feature control frame.

### Position error compared against base tolerance alone on an MMC-modified callout
- **Usually means:** the inspector didn't measure actual feature size, or measured it but forgot to compute bonus tolerance before the accept/reject call.
- **First question:** what is the as-measured feature size, and has bonus tolerance been added to the base callout before comparing against the measured position error?
- **Data to pull:** the feature's measured diameter/width and the position tolerance's modifier (MMC/LMC/RFS).

### Strain-gauge output that doesn't match the bridge configuration's stated equation
- **Usually means:** the wiring doesn't match the documented configuration (e.g., a quarter-bridge wiring labeled as half-bridge), or a gauge in the bridge has failed open/shorted.
- **First question:** does a bridge-resistance check at each arm match the expected nominal gauge resistance, and does the wiring diagram match what's actually connected?
- **Data to pull:** individual arm resistances, the wiring diagram used, and the excitation voltage actually applied vs. assumed.

### Load or force reading taken above the highest verified calibration point
- **Usually means:** the test plan's target load exceeds what was checked during pre-test verification, and nobody extended the reference check.
- **First question:** what is the highest load point this load cell was verified against a traceable reference, and does the test load fall inside that range?
- **Data to pull:** the calibration/verification record's tested points and the test plan's target load profile.

### Strain reading zeroed or rezeroed without a logged repeatability check
- **Usually means:** an operator treated an unexpected reading as gauge drift and rezeroed to make it go away, potentially discarding a real signal.
- **First question:** was the anomalous reading reproduced on a repeat load application before rezeroing, or was it zeroed on the first occurrence?
- **Data to pull:** the raw (pre-zero) data log and the repeat-cycle comparison, if one was run.

### Test-to-analysis delta beyond the documented correlation band (commonly ±5-15% depending on test type) with no engineering disposition on record
- **Usually means:** the result was filed as "passed" without checking it against the predicted value, or the divergence was noticed and not routed to the engineer of record.
- **First question:** what is this test article's documented test-to-analysis correlation band, and is the measured delta inside or outside it?
- **Data to pull:** the predicted (hand-calc or FEA) value, the measured value, and any prior disposition on similar divergences for this test setup.

### First-article deviation log with zero non-toleranced entries
- **Usually means:** the build had no untoleranced observations worth noting (unlikely on a true first article) or the technician only logged pass/fail against printed tolerances and dropped everything else.
- **First question:** were there any fit, finish, or assembly observations during the build that weren't on a toleranced callout, and were they logged regardless?
- **Data to pull:** the build traveler or assembly notes taken during the build, cross-checked against the formal deviation log.

### Functional (go/no-go) gauge used as the sole record on a first-article or engineering-development build
- **Usually means:** the build was treated like routine repeat production, skipping the magnitude data the engineering feedback loop needs.
- **First question:** is this build a first article or development unit (needs a CMM/hand-measured record with actual values), or routine repeat production (a gauge pass/fail is sufficient)?
- **Data to pull:** the work order's build classification and whether a dimensional record beyond gauge pass/fail exists.

### Thermal data reduced without a cold-junction compensation step
- **Usually means:** the raw thermocouple voltage was converted to temperature against a 0°C reference table without adding the terminal block's actual cold-junction equivalent voltage.
- **First question:** was the cold-junction reference temperature measured and its table-equivalent voltage added before the reverse lookup?
- **Data to pull:** the DAQ's cold-junction reference temperature log and the reduction worksheet's correction step.

### Calibration certificate on a reference standard more than half-expired relative to its stated interval
- **Usually means:** the standard is still technically valid but its drift margin is thinner than the certificate's stated uncertainty implies without a documented drift history.
- **First question:** what fraction of the standard's calibration interval remains, and does the lab have drift history on this specific unit or model justifying continued use as-is?
- **Data to pull:** the reference standard's calibration date, stated interval, and due date.

### Hole pattern position error reported without the individual per-hole values (summary "all pass" only)
- **Usually means:** the CMM report was truncated to a verdict, discarding the per-feature magnitude an engineer would need to see a trend across the pattern.
- **First question:** does the underlying point-cloud/measurement export exist with per-hole values, even if the summary only states pass/fail?
- **Data to pull:** the full CMM measurement export, not just the disposition summary.

### Bridge excitation voltage assumed rather than measured at the DAQ terminals
- **Usually means:** the reduction worksheet used the DAQ's nominal/set excitation value instead of the actual measured excitation, which can differ by a fraction of a percent due to cable resistance or supply regulation.
- **First question:** was Vex measured at the bridge (or as close to it as the DAQ allows) rather than assumed from the excitation setting?
- **Data to pull:** the DAQ configuration log and, if available, a directly measured excitation voltage.
