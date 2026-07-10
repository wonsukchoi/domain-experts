# Vocabulary

Terms of art a generalist reliably misuses. Format per term: definition, how a practitioner actually says it, the common misuse.

### RQD (Rock Quality Designation)

The percentage of a core run made up of "sound" pieces ≥10 cm long, divided by the *total drilled run length*.
**In use:** "Run 9 is 60% RQD after rejoining two mechanical-break clusters — that's fair, not poor."
**Common misuse:** dividing by recovered length instead of drilled run length, which silently inflates the number by exactly the recovery loss. RQD and core recovery are two different fractions with two different denominators.

### Core recovery

The percentage of a run's drilled length that was physically recovered, regardless of piece size or quality: recovered length ÷ drilled run length.
**In use:** "97% recovery but only 60% RQD — we got the rock back, most of it just isn't intact."
**Common misuse:** treating high recovery as a proxy for good rock quality. A run can recover 95%+ of highly fractured rubble; recovery measures quantity, RQD measures intactness, and they diverge exactly where it matters.

### Mechanical break vs natural fracture

A mechanical break is core separation caused by the drilling/handling process (fresh, angular, uncoated surface); a natural fracture is a pre-existing discontinuity in the rock mass (weathered, coated, or slickensided surface).
**In use:** "That break's fresh and perpendicular to the axis with a clean fit — mechanical, rejoin it before you tally RQD."
**Common misuse:** treating piece count alone as the signal, or overcorrecting and rejoining every break regardless of surface evidence, which hides real ground hazard.

### CRM (Certified Reference Material)

A sample of known, laboratory-certified composition (with a stated mean and standard deviation) inserted into a sample batch to test the analytical lab's accuracy.
**In use:** "This batch has a CRM out at −2.4 SD — hold reporting until the lab reruns it."
**Common misuse:** calling any "standard rock sample" a CRM. A true CRM has a certificate with a statistically defined acceptable range; an uncertified reference material can only be used qualitatively.

### Blank

A sample of material known to contain none (or negligible amounts) of the analyte of interest, inserted to detect contamination in sample prep or analysis.
**In use:** "Blank came back at 12× detection limit — something upstream in the prep line is carrying over."
**Common misuse:** confusing a blank (tests for contamination) with a CRM (tests for accuracy) — they diagnose different failure modes and a batch needs both.

### Field duplicate vs pulp duplicate

A field duplicate is a second, independent split taken from the original sample material at the point of collection, testing field sampling variability. A pulp duplicate is a second split taken from the pulverized lab pulp, testing only lab-stage repeatability.
**In use:** "The pulp duplicates are tight but field duplicates show 35% RPD — the variability's coming from how the material's split in the field, not the lab."
**Common misuse:** treating any repeated analysis as equivalent QAQC evidence. A tight pulp duplicate says nothing about whether the original field split was representative.

### Chain of custody

The unbroken, documented, signed record of who possessed a sample from collection through final disposal, used to establish the sample's evidentiary integrity.
**In use:** "Custody's broken between the site and the courier pickup — nobody signed the handoff, so this batch's results are defensible only as indicative."
**Common misuse:** treating chain-of-custody as paperwork rather than as the thing that makes a result usable in a technical report or legal proceeding — a perfect analytical result with a broken custody chain is not admissible evidence of anything.

### Downhole survey (deviation survey)

A measurement of a borehole's actual azimuth and dip at intervals down its length, used to correct the planned (collar-based) trajectory to the hole's true path.
**In use:** "We're two surveys behind past 90 m — don't trust the true-depth cross-section below that until we shoot it."
**Common misuse:** assuming a drilled hole follows its planned trajectory. Torque and formation contacts deflect the bit continuously; without surveys, true depth and planned depth diverge more the deeper the hole goes.

### USCS (Unified Soil Classification System)

A standardized soil classification (ASTM D2487/D2488) assigning a two-letter group symbol (e.g., SM, CL) based on gradation and plasticity.
**In use:** "Field call is SM pending lab confirmation — sand with fines, non-plastic on the field ribbon test."
**Common misuse:** assigning a group symbol from visual gradation alone without running the plasticity field tests (dry strength, dilatancy, toughness) D2488 actually requires — a symbol without the supporting tests behind it is a guess wearing a standard's notation.

### Detection limit vs practical quantitation limit

The detection limit is the lowest concentration an instrument can reliably distinguish from zero; the practical quantitation limit (PQL) is the lowest concentration that can be reliably *quantified* with acceptable precision — always higher than the detection limit.
**In use:** "It's above detection but below the PQL — report it as a trace, not a number we'd put in a resource model."
**Common misuse:** treating "detected" and "quantifiable" as the same thing, then averaging a column of numbers that includes values below the PQL as if they carried the same precision as the rest.

### True thickness vs drilled (apparent) thickness

Drilled thickness is the length of an interval measured along the borehole; true thickness is that length corrected for the angle between the hole and the geological contact.
**In use:** "12 m drilled thickness at this dip and hole angle works out closer to 7 m true thickness — don't quote the drilled number without the correction."
**Common misuse:** reporting drilled thickness as if it were the geologically meaningful number. Without the hole's angle relative to the contact (from a downhole survey plus structural measurement), drilled thickness systematically overstates true thickness for any non-perpendicular intersection.

### Composite sample vs grab sample

A composite sample combines material from multiple points across an interval or a batch to represent it as a whole; a grab sample is taken from a single point.
**In use:** "That's a grab from the top of the pile, not a composite — it tells us about one spot, not the stockpile average."
**Common misuse:** presenting a grab sample's result as representative of a larger interval or volume when only a composite protocol supports that claim.

### Assay pulp vs coarse reject

The pulp is the finely pulverized material actually analyzed; the coarse reject is the crushed-but-not-pulverized leftover material retained (often for years) in case a result needs re-checking.
**In use:** "Send the coarse reject for a check assay before we accept this result — don't just rerun the pulp, since that only re-tests the lab's own prep, not the original sample."
**Common misuse:** treating a pulp re-assay as an independent check on a suspect result. Re-running the same pulp can only confirm or contradict the lab's analytical step, not the original sample's representativeness.
