# Vocabulary

### Exposure Index (EI)
A vendor-standardized numeric value representing the radiation dose that reached the digital detector for a given exposure, independent of how the image displays on screen.
**In use:** "EI came back at 210 against a target of 300-450 for this chamber setup — check chamber selection before we assume the technique was underexposed."
**Common misuse:** Treated as interchangeable with the older film-based "density" concept, or ignored entirely because the digital image "looks fine" — post-processing can make a significantly overexposed or underexposed image display normally.

### Deviation Index (DI)
A logarithmic comparison of the actual EI to the vendor's target EI for that exam type; DI of 0 means exact match, each whole number represents roughly a doubling/halving of exposure.
**In use:** "DI is +1.2 on that abdomen — that's over double the target exposure, not a rounding difference."
**Common misuse:** Read as a pass/fail threshold rather than a magnitude — a DI of +0.5 and +2.0 are both "over target" but represent very different actual dose differences.

### ALARA
"As Low As Reasonably Achievable" — the radiation-safety principle that exposure should be minimized without sacrificing diagnostic image quality, not minimized absolutely.
**In use:** "ALARA doesn't mean drop the mAs until it's borderline nondiagnostic — it means the lowest technique that still answers the clinical question on the first try."
**Common misuse:** Invoked to justify reducing technique to the point of forcing a repeat, which increases integrated patient dose rather than reducing it.

### Grid ratio
The ratio of the height of the lead strips in a scatter-reduction grid to the distance between them (e.g., 12:1); higher ratios remove more scatter but require more exposure and tighter SID/centering tolerance.
**In use:** "We're on a 12:1 grid for this lateral spine — SID has to be within the grid's focal range or we'll get cutoff."
**Common misuse:** Assumed that a higher grid ratio is always "better image quality" without accounting for the dose increase and the positioning precision it demands.

### Source-to-Image Distance (SID)
The distance from the X-ray tube's focal spot to the image receptor; standardized per exam type (commonly 40 in general radiography, 72 in for chest) to control magnification and geometric distortion.
**In use:** "Chest has to be at 72 in SID — anything shorter and the heart size reads falsely enlarged."
**Common misuse:** Treated as a fixed constant regardless of exam type, when it's actually exam-specific and directly affects both magnification and the grid's usable focal range.

### AEC (Automatic Exposure Control)
A system of ionization chambers or solid-state detectors beneath the image receptor that terminates exposure once a preset radiation quantity has reached the receptor.
**In use:** "AEC isn't valid here — the mass is off to one side and outside the chamber, so it'll expose to whatever tissue happens to be over the chamber, not the pathology."
**Common misuse:** Trusted as a universal safeguard against wrong exposure, when it only measures flux at fixed chamber locations and fails silently when anatomy doesn't match its calibrated geometry.

### 15% rule
The relationship that a 15% increase in kVp produces approximately the same receptor exposure as doubling mAs, used to trade contrast for exposure time or vice versa.
**In use:** "Patient can't hold still — bump kVp 15% and halve the mAs to shorten exposure time without losing density."
**Common misuse:** Applied as if it only affects density, ignoring that raising kVp also lowers subject contrast — appropriate for penetration/motion problems, not a free substitute in every situation.

### Repeat/reject rate
The percentage of exposures that had to be repeated or rejected as non-diagnostic, tracked per room and per reason code as a core QA metric.
**In use:** "Room 3 is at 11% this month, mostly positioning-coded — that's a training conversation, not an equipment ticket."
**Common misuse:** Used as an individual performance score in isolation, without checking whether the underlying reason codes point to equipment drift rather than technologist error.

### MR-conditional
An implant or device classification meaning it is safe under specific, documented MRI conditions (field strength, gradient limits, positioning) — not an unconditional "MRI safe" or "MRI unsafe" label.
**In use:** "The card says MR-conditional at 1.5T with the coil not directly over the device — that doesn't clear it for our 3T magnet."
**Common misuse:** Collapsed into a binary "safe/unsafe" when the actual clearance is scan-condition-specific and can be voided by using different parameters than the documentation covers.

### Nephrogenic systemic fibrosis (NSF) risk
A rare but serious fibrosing condition linked to gadolinium-based contrast administration in patients with eGFR below roughly 30 mL/min/1.73m².
**In use:** "eGFR's under 30 — we need the radiologist to weigh in on agent choice and dose before this gadolinium study proceeds."
**Common misuse:** Treated as a concern only for dialysis patients, when the risk threshold is tied to eGFR level generally, not dialysis status alone.

### Gonadal/fetal shielding
Lead or lead-equivalent shielding historically placed over reproductive organs during applicable exams; per current guidance, no longer placed by default due to minimal dose benefit at modern technique levels and risk of obscuring relevant anatomy.
**In use:** "Skip the gonadal shield on this pelvis obstruction series — it'll sit right over the anatomy we need to see."
**Common misuse:** Still applied reflexively on every abdomen/pelvis order as a liability habit, without checking whether it will overlap the clinical region of interest.

### Zone III / Zone IV (MRI safety zones)
The ACR four-zone MRI facility model in which Zone III is the restricted-access area for screened personnel/patients and Zone IV is the magnet room itself, requiring re-screening at entry every time.
**In use:** "Re-confirm screening at the Zone IV door even though she was in an hour ago for the same-day follow-up — that's not optional."
**Common misuse:** Assumed that clearing Zone II screening once per visit covers all subsequent entries into Zone IV, when re-verification at the magnet room door is required each time.

### Portable/bedside exam
A radiographic exam performed at the patient's location (ICU, OR, bedside) using a mobile unit, rather than in a fixed radiography room.
**In use:** "Portable chest on bed 4 — document the SID and angulation deviation since we can't match the 72-inch upright standard here."
