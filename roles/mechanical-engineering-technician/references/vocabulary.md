# Vocabulary — terms of art, misuse-aware

### True position
The GD&T tolerance zone (a cylinder, for a round feature) within which the feature's actual center must fall, computed as 2√(dx² + dy²) from nominal.
**In use:** "Hole #1 measures 0.0060" position error against a 0.0115" allowable at the as-measured size — well inside."
**Common misuse:** Treated as interchangeable with a ± coordinate tolerance on the same numeric value; a coordinate tolerance defines a square zone, not the round zone true position actually controls, so the two are not equivalent even at matching numbers.

### Datum reference frame (DRF)
The set of datums (primary, secondary, tertiary), in the precedence stated on the drawing, that constrains a part's orientation and location for measurement purposes.
**In use:** "Constrained fit against A|B|C per print precedence, not best-fit — that's what makes the position number reproducible."
**Common misuse:** Assumed to be interchangeable with whatever three features the CMM operator picks for a stable setup; the DRF is defined by the drawing's feature control frame, not by measurement convenience.

### Bonus tolerance
Additional position (or other geometric) tolerance a feature earns as its actual size departs from its Maximum Material Condition, only when the feature control frame carries an MMC modifier.
**In use:** "Measured diameter 0.2585" against MMC 0.2570" earns 0.0015" bonus, raising the allowable from 0.0100" to 0.0115"."
**Common misuse:** Applied by default to every position callout; a callout at RFS (regardless of feature size) or LMC follows different rules, and no bonus applies at all under RFS.

### Wheatstone bridge
A four-arm resistive circuit that converts a small resistance change (from a strained gauge) into a measurable output voltage proportional to strain.
**In use:** "Full bridge, four active arms, output equation Vout/Vex = GF·ε — no division by 2 or 4 needed at this configuration."
**Common misuse:** Assuming the same Vout/Vex-to-strain formula applies regardless of how many arms are active; quarter, half, and full bridge each have a different coefficient, and using the wrong one under- or overstates strain by 2-4x.

### Gauge factor (GF)
The strain gauge's sensitivity constant — the ratio of fractional resistance change to strain, typically ~2.0-2.1 for foil gauges.
**In use:** "GF 2.06 per the gauge lot's certification sheet, not the generic 2.0 textbook value."
**Common misuse:** Using a rounded textbook GF (2.0) instead of the specific lot's certified value, which introduces a systematic few-percent error into every strain calculation from that gauge.

### Self-temperature-compensated (STC) gauge
A strain gauge manufactured with a thermal expansion coefficient matched to a specific substrate material, minimizing apparent strain from temperature change alone on that substrate.
**In use:** "STC-06 gauge selected to match the 6061 aluminum bracket's CTE — apparent thermal output over the test's expected range stays under 5 µε/°F."
**Common misuse:** Treated as eliminating the need for temperature compensation entirely; STC reduces but doesn't zero thermal output, and a full or half bridge is still the more robust cancellation method for a long-duration or wide-temperature-range test.

### Constrained fit (vs. best-fit alignment)
A CMM alignment method that locks the coordinate system to the part's actual datum features in their stated precedence, simulating how the part sits in the assembly or fixture.
**In use:** "Constrained fit against the primary face first, then the secondary edge, then the tertiary hole — matches how the part is actually held in the next assembly."
**Common misuse:** Confused with best-fit, which mathematically minimizes overall deviation across many points with no regard for datum precedence — the two produce different position numbers on identical data and aren't interchangeable substitutes for each other.

### Test uncertainty ratio (TUR)
The ratio of a tolerance being verified to the measurement uncertainty of the instrument verifying it; commonly targeted at 4:1 or better before a pass/fail call is considered defensible without guard banding.
**In use:** "Load cell verified at 45 lbf with 0.14% error against a Class C ±0.25% spec — that's inside spec, but TUR against the tolerance band itself should still be checked before trusting a marginal reading."
**Common misuse:** Ignored entirely on shop-floor instrumentation checks, treating "within spec" as sufficient without asking how much of that spec's margin the measurement's own uncertainty consumes.

### Cold-junction compensation (CJC)
The correction applied to a thermocouple's raw output voltage to account for the reference (cold) junction not being held at 0°C, using the reference junction's measured temperature and its table-equivalent voltage.
**In use:** "Corrected voltage = measured 4.096 mV + CJ equivalent 0.936 mV at 23.4°C reference — reduces to 122.3°C, not the uncorrected ~97°C a naive lookup would give."
**Common misuse:** Skipped when the DAQ is assumed to handle it internally without verifying that the specific channel/module actually has CJC enabled and correctly referenced.

### First article inspection (FAI)
A complete dimensional and characteristic verification of the first production-representative unit of a part, recording actual measured values against every characteristic on the drawing.
**In use:** "First-article record includes all four bolt-pattern holes with individual measured values, not just a pass/fail summary."
**Common misuse:** Treated as equivalent to a routine in-process inspection sampling a subset of dimensions; an FAI is comprehensive by definition — a partial characteristic list isn't a first article inspection, it's a spot check mislabeled.

### Functional (go/no-go) gauge
A fixed-tolerance fixture that directly checks whether a feature falls within its allowable envelope without reporting a magnitude — the part either fits the gauge or it doesn't.
**In use:** "Go/no-go plug gauge clears the bolt-pattern check in under a minute for this repeat-production run — no CMM cycle needed."
**Common misuse:** Used as the sole record on a first-article or engineering-development build, where the lack of a magnitude value (just pass/fail) discards exactly the data the design feedback loop needs.

### Proof load
A test load applied to verify a structure withstands a specified load without detrimental permanent deformation, typically below the structure's design ultimate load.
**In use:** "Proof-loaded to 45 lbf per the test plan; strain returned to baseline post-unload within instrument noise — no permanent set."
**Common misuse:** Conflated with "ultimate load" or "failure load" testing; a proof load test is explicitly designed not to fail or permanently deform the article, and a result showing permanent set is itself the finding, not a sign the test was run wrong.

### Margin of safety (MS)
The fractional or percentage capacity remaining between a structure's allowable (e.g., yield) stress and the applied stress at the test or design condition, computed as (allowable/applied) − 1.
**In use:** "MS vs. yield = 35,000/17,524 − 1 = +1.00 — a safety factor of roughly 2.0 at this test load."
**Common misuse:** Reported as a bare ratio (e.g., "2.0") without stating whether it's against yield, ultimate, or a specific limit/ultimate design case — the same test result yields a different margin depending on which allowable it's measured against.

### As-found / as-left
The measured condition of an instrument or reference standard before any adjustment ("as-found") versus after any adjustment made during that calibration or verification event ("as-left").
**In use:** "As-found and as-left are identical on this load cell — no adjustment was made, it verified within spec as received."
**Common misuse:** Recorded as a single value when an adjustment was actually made, losing the information about how far the instrument had drifted before correction — which matters for interval and trend analysis even when the final as-left value is in spec.
