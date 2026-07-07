# Playbook

Filled worksheets for the four procedures that gate most substation/powerhouse jobs: interpreting a DGA trend, testing and coordinating a protective relay, sequencing a substation switching/grounding/stored-energy lockout, and selecting arc-flash PPE from an equipment-specific study. Numbers below are published table values, standard-cited figures, or clearly flagged industry heuristics — a specific utility's protection-and-control procedure, DGA program guide, and relay setting study always control over this worksheet.

## 1. Dissolved gas analysis (DGA) interpretation

**Total dissolved combustible gas (TDCG)** = H2 + CH4 + C2H2 + C2H4 + C2H6 + CO (CO2 tracked separately, used mainly for paper-insulation aging, not TDCG). IEEE C57.104 condition bands (approximate to the current standard revision — verify against your DGA program guide):

| Condition | TDCG (ppm) | Meaning |
|---|---|---|
| 1 | ≤720 | Normal aging |
| 2 | 721–1920 | Exercise caution; increase sampling frequency |
| 3 | 1921–4630 | Elevated concern; investigate probable fault |
| 4 | >4630 | High risk; consider immediate removal from service |

**Key-gas identity** (which gas is rising matters more than the total once a rise is confirmed):

| Gas rising | Suggests |
|---|---|
| Hydrogen (H2), some methane | Partial discharge / corona |
| Acetylene (C2H2), any measurable and rising | Arcing (high-energy discharge) |
| Ethylene (C2H4), ethane (C2H6), limited acetylene | Thermal fault (overheating) |
| Carbon monoxide (CO), carbon dioxide (CO2) | Paper/cellulose insulation involvement |

**Rate-of-rise trigger.** Condition banding is a snapshot; a transformer can sit inside Condition 1 or 2 while gassing fast enough to cross the next band before the next scheduled sample. Many utility DGA programs use a rate-of-rise trigger around 30 ppm/day of TDCG (or a comparable ppm/month figure for individual key gases) to move from the standard annual or semi-annual sampling cycle to immediate resampling, independent of the absolute condition band [heuristic — utility DGA program practice, verify against your program's guide].

**Worked example (matches SKILL.md).** Day 0: H2 50, CH4 40, C2H2 2, C2H4 60, C2H6 30, CO 300 → TDCG 482 (Condition 1). Day 10 (triggered by a sudden-pressure alarm): H2 180, CH4 150, C2H2 25, C2H4 210, C2H6 45, CO 420 → TDCG 1030 (Condition 2). Rate of rise = (1030 − 482) / 10 days = 54.8 ppm/day, above the ~30 ppm/day heuristic trigger. Acetylene rose 2 → 25 ppm (12.5×) while ethylene/ethane rose less sharply — key-gas pattern points to arcing, not pure thermal drift. Action: resample in 24–48 hours rather than the standard interval; do not let the Condition-2 band alone stand in for a service decision.

**IEC 60599 ratio cross-check.** As a second method alongside key-gas reading, IEC 60599 uses three gas ratios — C2H2/C2H4, CH4/H2, C2H4/C2H6 — against published fault-type ranges (discharge, low-energy arcing, high-energy arcing, and thermal faults at increasing temperature bands) to corroborate a key-gas read before committing to a fault-type conclusion. Treat a single method's output as a hypothesis to confirm with the second method and with electrical test data (relay/protection records, load history), not as a standalone diagnosis.

## 2. Protective relay test and coordination check

**Test sequence per relay:**

1. Record the relay's current setting sheet (pickup value, time dial/curve, instantaneous element if present) before testing — a test result is meaningless without the setting it's being checked against.
2. Secondary-injection pickup test: apply current/voltage and confirm the relay operates within tolerance of setpoint. A commonly used utility acceptance criterion is pickup within ±5% of setting [heuristic — common utility test-acceptance practice; exact tolerance is manufacturer- and utility-procedure-specific].
3. Secondary-injection timing test: confirm operating time within tolerance of the published time-current curve at a defined multiple of pickup (e.g., 3× or 5× pickup current). A commonly used acceptance criterion is timing within ±5% of the curve value at that test point [heuristic — as above].
4. If CT ratio, polarity, or wiring is in question (not routine retest), perform primary injection through the actual CT to verify the current the relay sees matches what secondary injection assumed — secondary injection alone tests the relay, not the CT circuit feeding it.
5. Re-check coordination: plot or review the relay's curve against its immediately upstream and downstream neighbors at the maximum expected fault current for that location. Confirm coordination time interval (CTI) is at least roughly 0.2–0.3 seconds [heuristic — commonly cited coordination margin covering breaker interrupting time and relay overtravel; a specific utility's coordination study sets the controlling figure] between adjacent device curves.
6. A relay that passes pickup but fails timing, or passes both in isolation but violates CTI against a neighbor, is a failed test overall — record it as a coordination finding, not a pass.

**Worked example.** Feeder relay pickup set at 400A tests at 392A (2% low, within ±5% tolerance — pass). Timing test at 5× pickup (2000A) is specified to trip in 0.35s per the curve; test result is 0.41s — 17% slow, outside a ±5% tolerance — fail on timing despite passing pickup. Re-plotting this relay's curve at 0.41s against the upstream breaker relay (set to operate at 0.65s at the same fault current) still leaves a CTI of 0.65 − 0.41 = 0.24s, inside the ~0.2–0.3s band — coordination itself is not violated by this specific timing drift, but the relay still fails its own test criterion and requires calibration or replacement before being left in service, since the next timing drift in the same direction would erode that margin further.

## 3. Substation switching, grounding, and stored-energy sequence

Builds on the same de-energize → verify → ground discipline as outdoor line work, extended to substation bus topology and breaker stored energy:

1. Confirm the switching order against the current as-built one-line diagram and today's actual bus configuration (which bus ties are closed, which sources are in service) — a bus can be reconfigured since the one-line was last updated, and a switching order written against a stale diagram is the substation-scale equivalent of misidentifying a conductor's voltage class.
2. Have a second qualified person independently verify the switching order and device numbers before any device operates — substation buses commonly have multiple sources and parallel paths that a single reviewer can misread.
3. Operate switches/breakers per the verified order; test for absence of voltage at every point of work with a rated detector.
4. Apply grounds, bracketing the work position the same way as outdoor line work — on a bus, this often means grounding both the equipment being worked and the bus section it's tied to, not just the equipment itself.
5. Before touching a breaker's operating mechanism: confirm the closing spring is discharged (or blocked from charging), SF6 or compressed-air pressure is isolated/vented per the manufacturer procedure, and any hydraulic accumulator is blocked — treat this as a separate checklist item from the electrical lockout/tagout, since a breaker can be electrically dead and grounded while still holding enough stored mechanical energy to move contacts or eject a component.
6. To return to service: remove grounds in reverse order and confirm count, confirm stored-energy mechanisms are restored to normal (or intentionally left blocked if further work follows), and confirm the protection scheme covering this equipment has a current passed test before re-energizing — not just that the switching itself is correct.

## 4. Arc-flash PPE selection for switchgear/breaker compartments

Voltage-class-only tables (as used for outdoor line clearances) don't capture incident energy inside an enclosure, which depends on gap distance, enclosure size, electrode configuration (e.g., vertical vs. horizontal conductors, barriered vs. open), and available fault current with its clearing time. Selection procedure:

1. Obtain the equipment-specific IEEE 1584 incident-energy calculation (vendor arc-flash study or utility-performed study) for the specific compartment and bus configuration being worked — not a generic voltage-class estimate.
2. Confirm the study's assumed fault current and clearing time still match current protective-device settings; a relay setting change since the study was performed can invalidate its incident-energy result the same way a slower clearing time changes the calculation on outdoor line PPE.
3. Select the PPE category whose minimum arc rating meets or exceeds the calculated incident energy, rounding up if between listed category minimums (same category structure and cal/cm² minimums used for outdoor work — the difference here is exclusively in how the incident-energy number was derived, not in the category table itself).
4. Treat the PPE category as burn-severity mitigation only — arc-blast pressure and projectile hazard from equipment failure require standoff distance and, where available, remote racking/switching devices, not a higher PPE category.

**Worked example.** A 13.8kV metal-clad switchgear compartment's IEEE 1584 study, current as of the transformer's last relay setting review, returns 7.8 cal/cm² incident energy at 18-inch working distance with the differential relay's present clearing time. This selects Category 2 (8 cal/cm² minimum) PPE. If the differential relay's clearing time is later slowed (e.g., a coordination change adds time delay to avoid nuisance tripping), the study must be rerun before the same PPE selection is assumed valid — a slower clearing time on the same fault current increases incident energy, potentially past the 8 cal/cm² boundary into Category 3 (25 cal/cm² minimum).
