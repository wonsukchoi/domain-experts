# Vocabulary

### Decline curve analysis (Arps)
A production forecasting method (Arps, 1945) modeling a well's output over time as exponential, hyperbolic, or harmonic decline, used as the baseline expectation against which actual production is compared.
**In use:** "This well's 34% below its Arps hyperbolic fit — that's outside normal decline variance, worth a mechanical check."
**Common misuse:** Comparing current production against a flat historical average instead of the fitted decline curve, which produces a false read on whether a well is genuinely underperforming or just declining as expected.

### Water cut
The percentage of produced fluid that is water rather than hydrocarbon, which typically rises as a field matures and drives increasing handling and disposal costs over field life.
**In use:** "Water cut's climbed from 40% to 68% over three years — model that into the field's long-term economics, not just current lifting cost."
**Common misuse:** Evaluating field economics on current lifting cost alone, missing that rising water cut can independently drive a field to uneconomic status well before hydrocarbon volumes do.

### Artificial lift (ESP, rod pump, gas lift)
Mechanical or gas-injection systems used to bring produced fluids to the surface once natural reservoir pressure alone is insufficient — electrical submersible pumps (ESP), rod pumps, and gas lift are the three most common methods, each with distinct failure signatures.
**In use:** "The ESP's amp draw pattern is consistent with pump wear — that's a lift problem, not a reservoir problem."
**Common misuse:** Attributing an artificial lift performance issue to reservoir decline without checking equipment-specific diagnostic signals (amp draw, pump curve deviation) that would distinguish the two.

### Well integrity / sustained casing pressure
Well integrity refers to the barriers (casing, cement, wellhead equipment) that contain reservoir pressure and fluids; sustained casing pressure is unexplained pressure buildup in a well's annulus, a leading indicator of a barrier failure.
**In use:** "Annulus B is holding pressure after bleed-down — that's sustained casing pressure, and it means the well doesn't resume normal production until this is investigated."
**Common misuse:** Treating a pressure anomaly as something to monitor while continuing production, rather than as a signal requiring investigation before production resumes, given what it indicates about barrier integrity.

### Stand-down authority
The policy granting any field worker the authority to halt operations over a safety concern, without needing manager pre-approval, and without penalty if the concern turns out to be unfounded.
**In use:** "That call to stand down turned out to be a false alarm, and that's fine — the point is nobody hesitated to make it."
**Common misuse:** Treating a stand-down call as something to be judged after the fact by whether the concern was "real," which quietly discourages future calls and erodes the authority's actual purpose.

### Normalized deviance
The organizational pattern where a known risk signal is repeatedly overridden under operational pressure until the deviation from safe practice becomes treated as routine, eventually compounding into a major failure (Vaughan, *The Challenger Launch Decision*).
**In use:** "This is the third time this specific alarm's been overridden under production pressure — that's normalized deviance, not three unrelated incidents."
**Common misuse:** Treating each overridden safety signal as an isolated incident rather than recognizing the pattern of repeated overrides as itself the leading indicator of a larger failure building.

### LACT (lease automatic custody transfer) / allocation
LACT is the metering system used to measure and transfer custody of produced hydrocarbons at the point of sale; allocation is the process of attributing commingled production volumes back to individual wells for royalty and reporting purposes.
**In use:** "The LACT meter was recalibrated three weeks ago — check whether that's driving the apparent production drop before we blame the wells."
**Common misuse:** Assuming metered or allocated volumes are ground truth without periodically auditing them against independent checks (truck tickets, tank gauging), when calibration drift is a genuinely common source of apparent production anomalies.

### Workover
A well intervention involving significant remedial work — repairing equipment, re-completing a zone, or performing a stimulation treatment — distinct from routine maintenance, typically requiring the well to be taken offline temporarily.
**In use:** "This isn't routine maintenance, it's a workover — we need to schedule the downtime and rank it against other capital candidates."
**Common misuse:** Approving a workover based on which well is generating the most attention rather than ranking it against other candidates by NPV per dollar of intervention cost.

### Formation damage
Reduction in a reservoir's permeability near the wellbore, often caused by fluid incompatibility, fines migration, or pressure cycling during shut-in/restart, which can permanently reduce a well's recoverable output.
**In use:** "Shutting this well in isn't free — cycling it risks formation damage that could permanently reduce its recoverable reserves."
**Common misuse:** Treating shut-in as a reversible, no-cost decision, when the restart process itself can cause damage that a simple "turn it back on" doesn't undo.

### Shut-in
Temporarily stopping production from a well, whether for economic reasons (low commodity price), operational reasons (maintenance), or safety reasons (integrity concern) — each carrying different restart risk profiles.
**In use:** "This is a safety shut-in, not an economic one — different restart criteria apply before we bring it back online."
**Common misuse:** Applying the same restart process regardless of why a well was shut in, when a safety-driven shut-in requires integrity clearance before restart in a way an economic shut-in doesn't.

### HSE (health, safety, environment)
The combined discipline covering worker safety, environmental compliance, and health protocols in field operations, treated as a single integrated risk management function rather than three separate concerns.
**In use:** "That spill response wasn't just an environmental issue — it's an HSE incident, and it gets the full after-action review."
**Common misuse:** Siloing safety, environmental, and health incidents into separate tracking systems, which can miss patterns that only become visible when the three are analyzed together.

### Royalty / severance tax reporting
The regulatory and contractual reporting of produced volumes used to calculate payments owed to mineral rights owners (royalty) and the state (severance tax), both directly tied to allocated production data.
**In use:** "The allocation error doesn't just affect our internal numbers — it affects what we owe in royalty payments, so this needs to be corrected and disclosed, not just fixed going forward."
**Common misuse:** Treating a discovered allocation or measurement error as purely an internal operational fix, without recognizing its downstream effect on royalty and tax obligations that may require retroactive correction.

### SCADA (production surveillance)
Supervisory Control and Data Acquisition — the real-time monitoring and control system used to track well and facility performance data (pressures, rates, equipment status) across a field.
**In use:** "Pull the SCADA history for that well — we need the pressure trend leading up to the anomaly, not just the current reading."
**Common misuse:** Relying on SCADA's most recent reading alone rather than the trend over time, which can miss a gradual anomaly developing well before it crosses an alarm threshold.
