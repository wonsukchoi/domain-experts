# Vocabulary

### Undercut (etching)
The lateral removal of material beneath the resist edge during etching, occurring alongside the intended downward removal in isotropic etching processes.
**In use:** "At this depth, expect about 0.10mm of undercut per side — the resist opening has to be narrower than the final line width by that much."
**Common misuse:** Designing a resist pattern at the exact final desired feature dimension without accounting for undercut, making the actual etched feature wider (for a removed area) or narrower (for a remaining feature) than the resist opening itself.

### Isotropic etching
An etching process that removes material at approximately the same rate in all directions — downward and laterally — as opposed to anisotropic etching, which is more directional.
**In use:** "This chemical etch is isotropic — depth and lateral spread move together at roughly the same rate."
**Common misuse:** Assuming etch depth and lateral spread are independent, when for isotropic processes they're tied together by roughly the same rate.

### Resist
A masking material applied to protect areas that shouldn't be etched, leaving only the intended pattern exposed to the etchant.
**In use:** "Check the resist under magnification before etching — a pinhole there will show up as an unwanted mark on the finished part."
**Common misuse:** Treating resist presence alone as sufficient, without inspecting for pinholes, incomplete cure, or adhesion failures that let etchant reach unintended areas.

### Etch rate
The speed at which a specific etchant removes a specific material under specific conditions (concentration, temperature), typically expressed as depth per unit time.
**In use:** "Etch rate's 0.025mm per minute for this bath temperature — that's what the time calculation is based on."
**Common misuse:** Assuming etch rate is a fixed universal constant for "the material" regardless of the specific etchant concentration, temperature, or material batch/finish.

### Test coupon
A sample piece processed under trial conditions before a full production run, used to verify etch rate, depth, or engraving parameters.
**In use:** "Run a test coupon on this new batch before committing the full order to these parameters."
**Common misuse:** Skipping test coupon verification on a new material batch or parameter set, assuming prior validated parameters will transfer directly.

### Anisotropic (etching/engraving)
A process that removes or engraves material with a strong directional preference — primarily downward with minimal lateral spread — as opposed to isotropic.
**In use:** "This laser process is far more anisotropic than the chemical bath — expect much less lateral spread at the same depth."
**Common misuse:** Assuming all etching processes behave isotropically, when some processes — particularly certain laser or specialized chemical methods — are deliberately more anisotropic and behave differently.

### Depth gauge / profilometer
Instruments used to measure actual etch or engraving depth on a finished part, verifying it against the target specification.
**In use:** "Profilometer's reading 0.098mm against a 0.10mm target — within tolerance, no rework needed."
**Common misuse:** Relying on visual inspection alone to judge whether an etch or engraving has reached its target depth, rather than a direct depth measurement.

### Line width (functional engraving)
The actual width of an engraved or etched line, which for functional markings — scales, calibration marks — must meet a specific legibility or accuracy requirement, not just look acceptable.
**In use:** "This scale's line width needs to hold to spec for the intended viewing distance, not just be generally readable."
**Common misuse:** Evaluating an engraved scale purely for general legibility rather than checking its actual line width and spacing against the specific functional tolerance it needs to meet.

### Registration (etching/engraving)
The alignment accuracy between a resist pattern (or engraving toolpath) and the part's actual physical features, or between steps of a multi-step process.
**In use:** "Check registration against the part's actual reference marks — the design file being correct doesn't guarantee physical alignment."
**Common misuse:** Assuming registration is automatically correct because the pattern file or design is correct, without verifying actual physical alignment on the part itself.

### Bridging (merged features)
A defect where two adjacent fine features — lines, openings — unintentionally merge together, often from combined undercut or engraving tool width exceeding the space between them.
**In use:** "Those two lines are close enough that combined undercut will bridge them — widen the spacing before running production."
**Common misuse:** Checking each fine feature's individual undercut or tolerance in isolation without checking whether the combined effect with an adjacent feature would cause them to bridge.
