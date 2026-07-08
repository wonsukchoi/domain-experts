# Red flags

Smell tests an NDT Level II/III catches on a first pass over a technique sheet, a scan/exposure record, or a disposition report.

### UT indication amplitude drops more than roughly 10 dB when the probe is rotated ±15° off perpendicular, but the report characterizes it as volumetric

- **Usually means:** the technician sized by amplitude and length alone without doing the directional-response check that actually distinguishes planar from volumetric, and the mischaracterization sends the disposition to the wrong acceptance table entirely.
- **First question:** was an angle/rotation characterization actually performed and recorded, or was the shape call made from amplitude and length alone?
- **Data to pull:** the scan record's amplitude-vs-angle data (or lack of it), and the specific acceptance table cited in the disposition.

### A planar/crack-like indication is dispositioned "accept" with a length comparison to a size-based table

- **Usually means:** the acceptance table applied is the one for rounded/volumetric indications (porosity, slag), which most structural codes (ASME B31.3 341.3.2, Section VIII App. 4) don't permit for crack-like flaws regardless of length.
- **First question:** which specific code paragraph and table was cited, and does that table apply to planar or volumetric indications for this service?
- **Data to pull:** the disposition report's cited paragraph number, and the code's own scope statement for that table.

### RT film density measured outside roughly 1.8-4.0 (or the specific code's stated range) but the film was still interpreted

- **Usually means:** the film is under- or over-exposed enough that discontinuity contrast and detail are compromised, and any interpretation made on it is not reliably traceable to the code's demonstrated-sensitivity requirement.
- **First question:** what was the measured density at the area of interest, and does it fall inside the applicable code's acceptable range for the viewing method used?
- **Data to pull:** densitometer reading log for the film, and the exposure technique sheet's target density.

### IQI (penetrameter) required sensitivity (e.g., 2-2T) not visible on the radiograph, but the film was still accepted for interpretation

- **Usually means:** the technique (kV, exposure time, source-to-film distance, film/screen combination) didn't achieve the code's demonstrated-sensitivity requirement, so any discontinuity below the IQI's demonstrated size threshold could be present and unseen.
- **First question:** what sensitivity did the IQI actually demonstrate on this film, and does the code require re-shooting before this film can support a disposition?
- **Data to pull:** IQI type and placement, hole/wire visibility as read on the film, and the code's minimum sensitivity requirement for this thickness.

### DAC or DGS calibration doesn't reproduce within roughly ±2 dB on a pre/post-scan check

- **Usually means:** something changed between calibration and scan (couplant, probe wear, contact pressure, cable, instrument gain drift) and the entire scan's amplitude-based sizing is now unsupported.
- **First question:** was a pre-scan and post-scan calibration check both performed and recorded, and if the post-check failed, was the scan re-done or the result voided?
- **Data to pull:** the calibration verification log with both timestamps and dB readings.

### A UT thickness reading is compared against nominal or mill wall thickness rather than the code-calculated t_min

- **Usually means:** the disposition logic is using the wrong reference number — nominal wall includes corrosion allowance the code doesn't require to remain intact, and comparing against it either falsely fails serviceable pipe or, worse, falsely passes pipe that's actually below the real structural minimum.
- **First question:** has t_min been calculated per the governing code (B31.3, Section VIII UG-27, etc.) for this specific service and thickness, and is that the number the reading was actually compared against?
- **Data to pull:** the t_min calculation with its inputs (P, D, S, E, Y), and the disposition memo's stated comparison basis.

### Remaining-life calculation uses only the long-term (since-new) corrosion rate when a recent interval shows a materially higher short-term rate

- **Usually means:** an active or recently-worsened corrosion mechanism is being averaged away by the long-term rate, understating near-term risk.
- **First question:** what does the most recent inspection interval's rate show compared to the long-term average, and is there a documented process reason the recent rate isn't representative going forward?
- **Data to pull:** the full UT thickness reading history at this CML (not just the two most recent points), and any process/chemistry change log for the line.

### MT yoke lift-test or prod current isn't logged for the shift the exam was performed

- **Usually means:** the equipment's field-generating capability wasn't verified before use, so a clean (no-indication) result can't be distinguished from an under-powered exam that simply couldn't have found anything.
- **First question:** is there a dated, serial-numbered lift-test or current-verification record covering the shift this specific exam was performed on?
- **Data to pull:** the daily equipment verification log and the exam record's date/time/equipment serial number.

### Wet fluorescent MT black-light intensity or ambient visible-light level not recorded at the exam surface

- **Usually means:** the exam surface may not have met the minimum UV-A intensity (commonly 1,000 µW/cm² at the surface) or maximum ambient visible-light level the code requires for reliable indication visibility, and a clean result under inadequate lighting isn't a reliable clean result.
- **First question:** was intensity measured at the actual exam surface (not just at the light source) during this exam, and is the value recorded on the technique sheet?
- **Data to pull:** the light-meter reading log with location and timestamp matching the exam record.

### Weld cap or surface not ground/dressed before a UT scan on a technique that requires a smooth surface

- **Usually means:** surface roughness or the weld crown itself is scattering or attenuating the beam, producing false or missed indications that have nothing to do with actual subsurface conditions.
- **First question:** does the written procedure require surface preparation before this scan, and was it performed and documented?
- **Data to pull:** the procedure's surface-preparation requirement and the pre-scan surface-condition note in the field record.

### A Level I is signing the interpretation/disposition line on an examination report

- **Usually means:** the certification structure was bypassed — Level I is qualified to perform and calibrate under a written procedure but not to interpret results against acceptance criteria or sign the disposition, per SNT-TC-1A.
- **First question:** who is certified Level II or III on this method and reviewed/signed the interpretation, and does the employer's written practice actually permit the signature on this report?
- **Data to pull:** the technician certification roster (method, level, expiration date) and the report's signature block.
