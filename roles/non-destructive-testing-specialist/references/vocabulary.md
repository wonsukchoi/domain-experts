# Vocabulary

Terms generalists flatten together that an NDT specialist keeps sharply separate — the value is in the misuse, not the definition.

## Discontinuity vs. indication vs. defect

A **discontinuity** is a real physical interruption in the material (a pore, a crack, an inclusion). An **indication** is what the NDT method registers — which can be a false indication (nothing physical there, e.g., a fixture mark) or a geometric indication (a real signal from the part's shape, not a flaw, e.g., weld root geometry on UT). A **defect** is a discontinuity that fails the applicable acceptance criteria for the service.

**In use:** "That's a geometric indication from the root reinforcement, not a discontinuity — confirmed by matching it to the known root profile before writing it up."

**Common misuse:** using "defect" for anything the instrument registers, when most indications on a properly-scanned part are discontinuities that pass the acceptance criteria, or aren't discontinuities at all.

## Planar vs. volumetric discontinuity

**Planar** discontinuities (cracks, lack of fusion, lack of penetration) have a sharp, roughly two-dimensional geometry that concentrates stress regardless of length. **Volumetric** discontinuities (porosity, slag, rounded inclusions) have a three-dimensional, rounded geometry that's a milder stress riser and is evaluated by a size/count table instead of an outright ban.

**In use:** "Length doesn't matter here — the directional response makes this planar, and B31.3 rejects planar indications regardless of size."

**Common misuse:** applying a volumetric-flaw size table (which allows indications up to some length) to a discontinuity that's actually planar, producing a false accept.

## DAC (Distance Amplitude Correction) vs. DGS/AVG (Distance Gain Size)

**DAC** builds an amplitude-vs-sound-path curve from reference reflectors machined into a calibration block of the *actual part's* material and thickness. **DGS/AVG** uses a generic chart tied to the specific transducer's characteristics (frequency, element size) and doesn't require a matching-material calibration block, trading some accuracy for portability when a matching block isn't available.

**In use:** "We don't have a calibration block matching this casting's grain structure, so we're using DGS off the transducer's published curve instead of a DAC block."

**Common misuse:** treating DAC and DGS curves as interchangeable or equally accurate for a given job — DAC is more accurate when a matching block exists; DGS substitutes when one doesn't, with an acknowledged accuracy tradeoff.

## 6 dB drop technique vs. DGS/AVG sizing vs. tip-diffraction

The **6 dB drop** technique sizes a flaw by finding where amplitude falls to half (−6 dB) of its peak as the probe is moved, and is accurate down to about one beam-width; below that, the beam itself — not the flaw edge — dominates the measurement. **DGS/AVG sizing** estimates an equivalent reflector size from amplitude alone via the transducer chart. **Tip-diffraction** (time-of-flight) locates the actual diffracted signal from a crack's tip independent of amplitude, and is the more accurate technique for flaws near or below beam-width.

**In use:** "The indication's smaller than our beam width at that sound path — switch to tip-diffraction, 6 dB drop will just report back the beam dimension."

**Common misuse:** applying 6 dB drop to a flaw at or below the beam's effective width and reporting the result as the flaw's true size, when it's actually reporting a beam-geometry artifact.

## NDT Level I vs. Level II vs. Level III (SNT-TC-1A)

**Level I** performs examinations and equipment calibration under a written procedure but doesn't interpret results against acceptance criteria or sign dispositions. **Level II** sets up and performs exams, interprets and evaluates results against codes/standards, and signs reports. **Level III** develops, qualifies, and interprets codes and procedures; is the technical authority for disputed calls, and typically certifies Level I/II personnel.

**In use:** "Route the disputed lack-of-fusion call to the Level III before we schedule the repair — Level II's call stands unless overturned."

**Common misuse:** treating certification level as a seniority title rather than a defined scope of signing authority — a Level I performing a scan correctly still cannot sign the interpretation line.

## Recording threshold vs. evaluation/rejection threshold

The **recording threshold** is the amplitude or size below which an indication doesn't need to be logged at all — it's set low on purpose to build a dataset for future trending, even for indications that will clearly be acceptable. The **evaluation** (or **rejection**) **threshold** is the higher amplitude or size at which a disposition decision (accept/reject) actually gets made. Confusing the two under-documents minor indications that matter for long-term trending.

**In use:** "Log it — it's above the 20% DAC recording threshold even though it's nowhere near the rejection threshold; we want it in the trend data for the next turnaround."

**Common misuse:** treating "not rejectable" as "don't need to record it," losing the trending data a future fitness-for-service evaluation would need.

## Ug (geometric unsharpness) vs. film contrast vs. definition

**Geometric unsharpness (Ug)** is blur caused by the source's finite size and the exposure geometry (Ug = F×t/D_od) — a setup problem, independent of the film or exposure time. **Film contrast** is how much density difference the film produces for a given change in material thickness — a film/exposure property. **Definition** is the overall sharpness of detail on the radiograph, affected by both Ug and screen/film choice together. A radiograph can have excellent contrast and still fail on definition if Ug is too large.

**In use:** "Density and contrast look fine on this shot, but the SFD was short for this source size — recalculate Ug before accepting the film for fine-crack detection."

**Common misuse:** judging film quality by density/contrast alone without separately checking whether the geometry (SFD, source size) met the Ug requirement for the discontinuity size the exam is meant to detect.

## IQI (Image Quality Indicator) — hole-type vs. wire-type, and "sensitivity"

A **hole-type IQI** (ASME-style) is a shim with drilled holes of specified diameters relative to its thickness; visibility of the smallest required hole (e.g., "2-2T": 2% thickness shim, 2×T hole diameter) demonstrates the film's sensitivity. A **wire-type IQI** (ISO/EN-style) uses a set of wires of decreasing diameter; the smallest visible wire's percentage of material thickness is the demonstrated sensitivity. "Sensitivity" here means the smallest artificial discontinuity size the technique has *demonstrated* it can reveal — not a guarantee about real discontinuities of similar or larger size, which can be harder or easier to detect depending on orientation.

**In use:** "We achieved 2-1T on this shot, better than the 2-2T requirement — the technique's demonstrated sensitivity has margin."

**Common misuse:** treating a passing IQI sensitivity as proof that any real discontinuity of that size would definitely be seen, when orientation and discontinuity type (planar flaws especially) can defeat a technique that passes its IQI check.

## Continuous vs. residual magnetization method (MT)

**Continuous method**: the magnetizing current (or field) is applied while the examination medium (dry powder or wet fluorescent bath) is also being applied and the surface is being observed — used for low-retentivity materials that don't hold a field well. **Residual method**: the part is magnetized first, then the medium is applied afterward, relying on the material's retained magnetism — only valid for high-retentivity, high-coercive-force materials (most hardened steels); using it on a low-retentivity material produces a weak, unreliable field by the time the medium is applied.

**In use:** "This is a low-carbon, annealed part — continuous method only, residual won't hold enough field to be reliable."

**Common misuse:** defaulting to the residual method for convenience (magnetize once, inspect at leisure) without confirming the material's retentivity supports it.

## API 510 vs. API 570 vs. API 653

**API 510** governs in-service inspection of pressure vessels. **API 570** governs in-service inspection of process piping. **API 653** governs in-service inspection of aboveground atmospheric storage tanks. Each has its own corrosion-rate, remaining-life, and inspection-interval methodology and its own inspector certification exam — a finding and interval calculated under one doesn't automatically transfer to equipment covered by another, even on the same unit.

**In use:** "That interval calculation is API 570 piping logic — the tank shell thickness monitoring locations follow API 653's methodology instead, not the same formula."

**Common misuse:** applying one code's inspection-interval or CML-spacing rule to equipment actually governed by a different one, because the underlying corrosion-rate math looks similar.

## Written practice vs. procedure vs. technique sheet

The employer's **written practice** (per SNT-TC-1A) defines how personnel get qualified and certified for each method and level — a personnel-qualification document, not a how-to-inspect document. A **procedure** defines how a specific examination method is to be performed to meet a code (parameters, equipment, calibration steps). A **technique sheet** (or exposure/scan record) documents the actual parameters used and results obtained for one specific job. Confusing these in an audit produces the wrong document for the wrong question.

**In use:** "The auditor wants to see the written practice for how our Level IIs got qualified — that's a different binder from the UT procedure itself."

**Common misuse:** producing the procedure when a written practice (or vice versa) is requested, because both get informally called "the procedure" on the shop floor.
