# Red Flags

Smell tests for taxonomic claims, dating disputes, phylogenetic results, and collections management. Format per flag: what it usually means, the first question to ask, the check to run.

### New species or genus proposed from a single, often fragmentary specimen

- **Usually means:** taxonomic inflation — an isolated individual's ontogenetic stage, sex, or taphonomic distortion mistaken for a population-level diagnostic character, before it means a genuinely new taxon.
- **First question:** "How many independent specimens show this character state, and do we have juveniles or subadults to rule out ontogenetic variation?"
- **Data to pull:** the full specimen list with size/ontogenetic-stage estimates, and a bivariate or PCA plot of the proposed diagnostic character against the nearest congener's documented range.

### Biostratigraphic age resting on an index-fossil specimen with visible abrasion, rounding, or an out-of-context depositional setting

- **Usually means:** post-mortem transport/reworking from an older (or younger) bed, not a true in-situ first or last occurrence.
- **First question:** "Is the specimen articulated and unabraded like the rest of the assemblage, or does its taphonomic signature suggest transport?"
- **Data to pull:** the sedimentological log of the horizon (channel lag vs. in-place mudstone) and an abrasion/rounding index for the specimen relative to associated fauna.

### Ar-Ar date reported without stating the flux monitor and its calibrated age

- **Usually means:** the date is uncalibrated to the current accepted standard, producing a systematic offset (historically up to roughly 1% before mid-2000s–2010s monitor recalibrations) relative to a directly comparable U-Pb date.
- **First question:** "Which flux monitor and monitor age were used, and has the date been recalculated under the currently accepted calibration?"
- **Data to pull:** the original paper's methods section for the monitor/standard used; recompute or flag if it predates the current accepted monitor age.

### Cladogram presented as a resolved topology with node support of 1 Bremer / under ~50% bootstrap

- **Usually means:** that branching order is a statistical polytomy, not a supported relationship — conclusions resting on it are unsupported.
- **First question:** "What is the bootstrap or Bremer/decay-index support specifically at the node the argument depends on?"
- **Data to pull:** the full support-value tree (not just the strict-consensus topology figure) and a sensitivity run with the most incomplete taxa removed.

### A "mass extinction" or sudden diversity drop at a horizon that coincides with a known unconformity or condensed section

- **Usually means:** a Signor-Lipps sampling artifact or a stratigraphic hiatus, not a synchronous biological extinction event.
- **First question:** "Is this horizon a documented condensed section or unconformity, and how does local sampling density compare across the interval?"
- **Data to pull:** the section's sedimentation-rate log and a range-through presence/absence matrix for the interval, not just the first/last occurrence list.

### Radiometric date and bracketing biostratigraphic zone disagree by more than the zone's stated duration

- **Usually means:** reworking, contamination of the dated mineral (inherited older cores), or misidentification of the index taxon — not that the zonation scheme itself is wrong.
- **First question:** "What does the per-grain U-Pb concordia plot show — any discordant or older inherited zircon cores?"
- **Data to pull:** the full per-grain concordia data, not just the reported weighted-mean age.

### Field jackets sitting unprepared and effectively unlabeled for more than roughly five years

- **Usually means:** prep-lab hour budget hasn't kept pace with acquisition rate, and locality/stratigraphic association is at risk as field labels fade or go missing.
- **First question:** "Does each jacket still have a legible field number cross-referenced to the locality catalog?"
- **Data to pull:** the prep-lab backlog log (jacket ID, field number, locality, elapsed time since collection).

### Redescription of a taxon whose holotype is lost or was never adequately figured

- **Usually means:** the taxon's identity may be unstable enough to need formal ICZN action (neotype designation) before further nomenclatural work proceeds.
- **First question:** "Has a petition been filed with the ICZN Commission, or does the original description contain enough diagnostic detail to stand without the type specimen?"
- **Data to pull:** the original type-series list, repository accession records, and any figured paratypes that could substitute.

### Morphometric "new species" claim built on raw linear measurements with no shape (geometric morphometric) or allometric correction

- **Usually means:** size-driven allometric variation is being read as a taxonomically diagnostic shape difference.
- **First question:** "Does the proposed diagnostic character persist after correcting for centroid size or overall body-size allometry?"
- **Data to pull:** a landmark-based geometric-morphometric dataset with PCA/CVA output, not the raw measurement table alone.

### Exhibit-bound specimen scheduled for prep before any documentation photography or CT scan of the matrix-encased state

- **Usually means:** irreversible loss of burial-orientation and articulation data once the matrix is removed — data that can matter as much as the bone itself.
- **First question:** "Has the specimen been photographed and/or CT-scanned in situ before any preparation began?"
- **Data to pull:** the pre-prep imaging record and original field-jacket photographs.
