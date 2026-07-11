# Working vocabulary — terms a generalist misuses

Format per entry: definition → a sentence a practitioner would actually say → the common misuse.

### Margin (CTV-to-PTV expansion)
The geometric expansion from the clinical target volume (disease + microscopic spread) to the planning target volume, sized to absorb setup error and organ motion — not a surgical "safety margin" for uncertainty about disease extent.
**In use:** "We're using a 7 mm posterior margin here because our IGRT setup data shows more day-to-day rectal-filling variation posteriorly than anteriorly."
**Common misuse:** treating margin as one uniform number chosen for comfort rather than derived from measured setup/motion uncertainty for that specific site and immobilization technique; a margin that's too generous just relocates the OAR-overlap problem instead of solving it.

### Hot spot
A localized region of dose exceeding the prescription, typically flagged above 105–107% of Rx.
**In use:** "The hot spot's sitting right in the middle of the GTV at 106% — that's fine, it's not touching the rectum."
**Common misuse:** assuming any hot spot is automatically a plan defect; location relative to target and OAR is what matters, not the existence of the hot spot itself.

### Conformity index (CI)
A ratio comparing the volume receiving the prescription dose to the target volume (several competing definitions exist in the literature; ideal value is 1.0, meaning the prescription isodose exactly wraps the target).
**In use:** "CI is 1.15 on this plan — I could tighten it further but it'd cost us modulation complexity we don't need."
**Common misuse:** treating a lower CI as always better without checking what it cost in monitor units, beam-on time, or low-dose spread — CI is a tiebreaker among otherwise-acceptable plans, not an independent optimization target.

### Homogeneity index (HI)
A measure of dose uniformity within the target, typically (D2−D98)/D50 or similar; lower values indicate more uniform dose.
**In use:** "HI's a bit high on this SIB plan because we're intentionally running two dose levels close together — that's expected, not a flaw."
**Common misuse:** applying a single-dose-level homogeneity expectation to a simultaneous-integrated-boost plan, where some heterogeneity between dose levels is the design intent, not an error.

### DVH (dose-volume histogram)
A plot of the fraction of a structure's volume receiving at least a given dose; it summarizes dose distribution across a volume but discards spatial location entirely.
**In use:** "The DVH numbers look fine, but let's check where in the rectum that V70 volume actually sits before we sign off."
**Common misuse:** treating the DVH as a complete plan evaluation on its own; two plans can have identical DVH curves for a structure while one puts the high-dose subvolume against the anterior rectal wall (clinically consequential) and the other against a posterior region already resected.

### Gamma analysis / gamma pass rate
A composite metric combining dose-difference and distance-to-agreement criteria (e.g., 3%/2mm) to compare a measured dose distribution against the planned one for patient-specific QA.
**In use:** "We're at 3%/2mm local dose per TG-218, and the plan's coming in at 95.4% — clears the 90% action limit."
**Common misuse:** quoting a pass rate without specifying the criteria (global vs. local normalization, percent and distance values, low-dose threshold) — a 95% pass rate at 3%/3mm global is a materially looser bar than 95% at 2%/2mm local, and the two aren't comparable.

### ITV (internal target volume)
A volume that expands the CTV to account for expected internal motion (typically respiratory), sitting between CTV and PTV in the margin hierarchy; distinct from the PTV, which additionally accounts for setup error.
**In use:** "We built the ITV from the 4D-CT MIP, then added our standard 5 mm setup margin on top to get the PTV."
**Common misuse:** using "ITV" and "PTV" interchangeably, or skipping ITV generation for a mobile target and applying only a generic setup-error margin that doesn't reflect measured motion.

### Simultaneous integrated boost (SIB)
A single treatment plan delivering two or more different dose levels to different target volumes concurrently, in the same fractions, rather than sequentially.
**In use:** "We're SIB-ing the gross disease to 70 Gy and the elective nodal volume to 56 Gy in the same 35 fractions, not sequencing them."
**Common misuse:** assuming an SIB plan's fraction size is uniform across the patient — each dose level has its own Gy-per-fraction, and biological effect (not just total dose) differs by target volume.

### Isocenter
The point in space where the machine's gantry, collimator, and couch rotational axes all intersect — the reference point beams are aimed through, not necessarily the geometric center of the target.
**In use:** "We shifted the isocenter off the geometric center of the PTV to keep beam entry away from the contralateral parotid."
**Common misuse:** assuming isocenter placement is fixed at the anatomic or geometric center of the target; it's frequently offset deliberately for beam-geometry or OAR-avoidance reasons.

### Monitor unit (MU)
The linac's internal measure of delivered output, calibrated (per TG-51) to correspond to a known dose under reference conditions; the number of MU needed to deliver a given dose depends on field size, depth, modulation, and machine-specific output.
**In use:** "This arc's running 650 MU for 200 cGy at isocenter — that's high for this field size, which is why I want the independent check before QA."
**Common misuse:** treating MU as directly proportional to dose in a way that lets you eyeball plans against each other — MU-to-dose ratio depends heavily on modulation and field size, so comparing raw MU across dissimilar plans is meaningless without normalizing for that.

### Bolus
A tissue-equivalent material placed on the skin surface to shift the depth of maximum dose closer to (or onto) the skin, compensating for the natural dose build-up region under megavoltage photon beams.
**In use:** "We're adding 0.5 cm bolus over the mastectomy scar on alternating fractions to make sure the skin gets adequate dose without full-time bolus toxicity."
**Common misuse:** assuming bolus is either always needed or never needed for a given site; it depends on whether the clinical target extends to the skin surface, not on the anatomic region alone.

### Record-and-verify (R&V) system
The software (e.g., Mosaiq, ARIA) that stores the approved plan's delivery parameters and checks them against what the linac is about to deliver before each fraction, functioning as an interlock against manual-entry error.
**In use:** "The R&V caught a couch-angle mismatch before the first fraction — good thing it's not just a paper chart anymore."
**Common misuse:** treating the R&V system as a passive archive rather than an active safety interlock; a parameter that's correct in the TPS but transcribed wrong into the R&V is exactly the failure mode it exists to catch.

### VMAT vs. IMRT (delivery technique)
Both are inverse-optimized, intensity-modulated techniques; VMAT delivers dose during continuous gantry rotation with simultaneously varying dose rate, gantry speed, and MLC aperture, while static-field IMRT delivers from a fixed number of discrete gantry angles.
**In use:** "We went VMAT here for the beam-on-time savings, but static IMRT would've been more forgiving of small MLC positioning errors given how tight this OAR sparing needs to be."
**Common misuse:** treating VMAT as a strict upgrade over static IMRT in all cases; VMAT's added delivery-parameter complexity makes it more sensitive to machine calibration and harder to root-cause on QA failure.
