# Playbook

Filled worked calculations for the artifact types this role produces most often: a NIST traceability chain record, a calibration-interval adjustment (Method A3), and a full uncertainty budget/TUR calculation in a second measurement domain (pressure) to show the method generalizes beyond the electrical example in SKILL.md. Populate with the actual job's numbers; the structure and arithmetic below are real and reconcile.

## Traceability chain — documenting the unbroken path to NIST/SI

**Scenario:** a lab's house reference multi-function calibrator (used as the reference standard in the SKILL.md worked example) needs its traceability documented for an ISO/IEC 17025 assessment.

| Link | Standard | Function/range | Uncertainty (stated on its cert) | Traceable to | Cert / interval |
|---|---|---|---|---|---|
| 1 (working standard, this lab) | House multi-function calibrator, S/N 5730-0442 | DC volts, 10 V | ±50 µV, k=2 | Link 2 | Cert #CA-24-1187, calibrated 2025-11, due 2026-11 (12 mo.) |
| 2 (accredited external lab) | Third-party ISO/IEC 17025-accredited metrology lab's Josephson-array-based DC voltage standard | DC volts, 10 V | ±0.15 µV, k=2 (CMC-limited value for this lab's accredited scope) | Link 3 | Lab accreditation cert + scope, verified current at time of use |
| 3 (national metrology institute) | NIST DC voltage realization, Josephson Voltage Standard array | SI volt, realized via the Josephson constant K_J-90 | Sub-nV level, NMI-realization uncertainty | SI (via CODATA-fixed physical constant) | NIST's own SI realization, published in NIST SP 250-series documentation |

**Chain check performed and recorded:** each cert (Link 1 and Link 2) is current (not expired), each states a numeric uncertainty and a coverage factor, and each names the next link up plus that link's accreditation body (A2LA, NVLAP, or equivalent, listed on the cert). A cert with no stated uncertainty, an expired cert used as if current, or a "reference" standard with no cert at all breaks the chain at that point — the calibration performed downstream of the break cannot claim traceability regardless of how many valid links exist above it.

**Deliverable — traceability statement (as filed in the QMS record for this reference standard):** "House standard S/N 5730-0442 (Cert #CA-24-1187, due 2026-11) is traceable to the SI volt through [accredited lab name], Cert #[xxxxx], A2LA Cert #[xxxxx], scope verified current 2025-11-15, whose DC voltage CMC of ±0.15 µV (k=2) at 10 V is itself traceable to NIST's Josephson Voltage Standard realization per NIST SP 250-series. No traceability gap identified in this chain as of the assessment date."

## Calibration-interval adjustment — Method A3 (simplified change-ratio version)

**Given:** a population of pressure-gauge model "Ashcroft 1009, 0-160 psi" instruments, currently on a 6-month calibration interval. Target reliability (the lab's stated goal for percent of units found in-tolerance at each calibration) = 95%, per the lab's NCSL RP-1-based interval program.

**History pulled from the calibration management system, last 8 cycles for this population:** 7 of 8 calibrations came back in-tolerance at the as-found check; 1 came back out-of-tolerance.

**Step 1 — observed reliability.** Observed % in-tolerance = 7 / 8 = **87.5%**.

**Step 2 — compare to target.** Difference = observed − target = 87.5% − 95% = **−7.5 percentage points** (population is running below the reliability target — the interval is too long for this population as currently observed).

**Step 3 — apply the change ratio, capped at ±25% per review cycle (a common lab-policy cap consistent with RP-1's guidance against large single-step interval swings).** Change factor = 1 + (−7.5% / 100) = **0.925**. Since |−7.5%| < 25%, no cap is triggered.

**Step 4 — new interval.** New interval = old interval × change factor = 6 months × 0.925 = **5.55 months**, rounded down to the nearest whole month per lab policy = **5 months**.

**Note on rigor:** this is a simplified change-ratio illustration of the Method A3 concept (adjust proportionally to the gap between observed and target reliability, bounded by a cap). The full NCSL RP-1 Method A3 procedure additionally accounts for the statistical confidence of the observed ratio given the sample size (8 cycles is a thin sample) and uses published interval-change-factor tables — with only 8 history points, RP-1 itself would flag this population for continued monitoring rather than a large interval change, and a real interval decision on this thin a sample should be reviewed by a technologist, not automated.

**Deliverable — interval review memo excerpt:** "Population: Ashcroft 1009, 0-160 psi (n=8 cycles reviewed). Observed reliability 87.5% vs. 95% target. Interval adjusted 6 mo. → 5 mo. effective [date]. Sample size (8) is below the lab's 20-cycle confidence threshold for a full Method A3 adjustment; population flagged for re-review at the next 4 cycles before further interval changes."

## Uncertainty budget and TUR — pressure domain (dead-weight tester vs. Bourdon gauge)

**Setup:** UUT is a 0-160 psi Bourdon-tube pressure gauge, manufacturer accuracy spec ±0.5% of full scale = ±0.005 × 160 = **±0.80 psi**, tested at the 100 psi point. Reference standard: a piston/dead-weight tester, manufacturer-stated accuracy ±0.02% of reading, calibration certificate reports expanded uncertainty ±0.02 psi at 100 psi, k=2.

**Step 1 — TUR, reference standard only.** TUR = 0.80 / 0.02 = **40:1** — far above the 4:1 target, typical for a dead-weight tester used against a general-purpose mechanical gauge.

**Step 2 — Type A uncertainty.** 5 repeat readings of the UUT at the dead-weight tester's 100 psi test pressure: sample standard deviation s = 0.010 psi. u_A = s / √n = 0.010 / √5 = 0.010 / 2.236 = **0.00447 psi**.

**Step 3 — Type B components.**
- Reference cert (k=2 expanded ±0.02 psi): u_B1 = 0.02 / 2 = **0.0100 psi**.
- Local gravity/air-buoyancy correction uncertainty for the dead-weight tester's mass set, stated as ±0.01% of reading, rectangular: u_B2 = (0.0001 × 100) / √3 = 0.01 / 1.732 = **0.00577 psi**.
- Mass-set calibration uncertainty, stated ±0.005 psi equivalent at this pressure, rectangular: u_B3 = 0.005 / 1.732 = **0.00289 psi**.

**Step 4 — combined and expanded uncertainty.** u_c = √(0.00447² + 0.0100² + 0.00577² + 0.00289²) = √(0.0000200 + 0.0001000 + 0.0000333 + 0.0000084) = √0.0001617 = **0.01272 psi**. Expanded uncertainty at k=2: U = 2 × 0.01272 = **0.02544 psi**.

**Step 5 — TUR, full measurement process.** TUR = 0.80 / 0.02544 = **31.4:1** — well clear of 4:1; no guard banding required at this ratio under the lab's standard policy.

**Deliverable — certificate excerpt:** "UUT: Ashcroft 1009 pressure gauge, 0-160 psi, S/N [xxxxx]. Test point 100 psi. Reference: dead-weight tester, Cert #[xxxxx], 100 psi output = 100.00 psi ± 0.02 psi (k=2). As-found: 100.35 psi (mean of 5, s=0.010 psi). Tolerance ±0.80 psi (0.5% FS). Measurement uncertainty U = 0.0254 psi (k=2); TUR = 31.4:1. Result: PASS, error +0.35 psi well within tolerance and guard band not required at this TUR."
