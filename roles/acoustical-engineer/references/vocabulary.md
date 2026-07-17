# Vocabulary — terms of art, misuse-aware

### RT60 (reverberation time)
The time, in seconds, for sound pressure level in a room to decay 60 dB after the source stops, measured per octave or third-octave band, not as a single broadband number.
**In use:** "Mid-frequency RT60 comes in at 1.8s at full occupancy — inside the 1.6-2.2s target band for this hall."
**Common misuse:** Treated as a "lower is always better" metric, the same instinct that gives a good result on a classroom and a ruined result on a concert hall — RT60 has a use-specific optimum, not a universal minimum.

### NC (noise criteria) curve
A family of standardized octave-band curves used to rate steady background noise (typically from HVAC), where a space's NC rating is set by the *highest* band that touches or exceeds a curve, not by an averaged dB(A) reading.
**In use:** "Measured spectrum clears NC 30 in every band except 250 Hz, which pokes through by 2 dB — that's an NC 32 space, not NC 30."
**Common misuse:** Reported as a single dB(A) sound-level number instead of a band-by-band curve fit; a space can pass on overall dB(A) while a narrow low-frequency band still violates the target curve and produces an audible hum or rumble complaint.

### STC (Sound Transmission Class)
A single-number rating of a partition's airborne sound isolation, derived from a lab-measured transmission-loss curve (ASTM E90) fit against a standard reference contour.
**In use:** "Assembly is lab-rated STC 55, but we're specifying to a field target of STC 48-50 to hold margin."
**Common misuse:** Spec'd and accepted at the exact lab-tested number with no allowance for field conditions; field-measured performance (ASTM E1007) typically runs 5-10 points below the lab rating once flanking paths and installation variance are accounted for, so a wall spec'd to exactly the target ships as a code-failing wall.

### IIC (Impact Insulation Class)
A single-number rating of a floor-ceiling assembly's isolation against *impact* noise (footfall, dropped objects), measured with a standardized tapping machine — a separate rating from STC, which covers airborne sound only.
**In use:** "Floor assembly hits STC 58 for airborne but only IIC 42 without the resilient underlayment — the impact path is the one that'll generate complaints."
**Common misuse:** Assumed to track STC — that a wall or floor with a high STC is automatically well-isolated against impact noise. The two ratings test different transmission paths and a high STC value says nothing about footfall performance.

### Flanking (flanking path / flanking transmission)
Sound or vibration energy that reaches the receiving space by a route other than straight through the rated partition — via a continuous structural element, shared ceiling plenum, ductwork, or penetration.
**In use:** "The 8-inch slab-to-slab detail doesn't hit the STC-50 target with that duct penetration left unaddressed — that's a flanking path, not a partition problem."
**Common misuse:** Ignored once the partition itself is spec'd to rating, on the assumption that a correctly rated wall or floor guarantees the field result; an unaddressed flanking path can dominate the total isolation regardless of how well the direct partition performs.

### Sabine equation
A reverberation-time formula (RT60 = 0.161·V/A, metric) relating room volume and total absorption, accurate to roughly 10% error at moderate absorption levels.
**In use:** "Sabine gives RT60 = 1.4s for the untreated shell — but average absorption is pushing 0.25, so we should cross-check against Eyring before committing."
**Common misuse:** Applied unmodified in heavily damped spaces (recording studios, anechoic-adjacent rooms); Sabine's error grows to roughly 28% once average absorption coefficient exceeds ~0.2-0.3, at which point Eyring's formula is the accurate one and Sabine understates achievable RT60.

### NRC (Noise Reduction Coefficient)
A single-number average of a material's absorption coefficients at 250, 500, 1000, and 2000 Hz, rounded to the nearest 0.05 — a coarse mid-frequency summary, not a full performance spec.
**In use:** "NRC 0.85 on the spec sheet, but check the 125 Hz coefficient separately before counting on it for the bass problem in this room."
**Common misuse:** Used as a proxy for low-frequency absorption performance; NRC deliberately excludes the 125 Hz band and below, so a high-NRC panel can still do essentially nothing for the low-frequency energy that's actually causing the complaint.

### Initial Time Delay Gap (ITDG)
The time interval between a direct sound arriving at a listener and the first strong reflection — the acoustic cue perceived as spatial "intimacy" in a performance space.
**In use:** "Vineyard layout shortens ITDG versus the shoebox baseline — that's the intimacy gain, separate from any reverberation-time change."
**Common misuse:** Subordinated to reverberation time in design discussions, or left out of the conversation entirely; in weighted hall-quality models it carries a larger share of perceived quality than RT60, bass ratio, warmth, and diffusion combined, so optimizing RT60 alone while ignoring ITDG can miss the dominant quality driver.

### Exchange rate (noise dosimetry)
The dB increase in noise level that halves the permissible exposure duration under a given occupational noise standard — OSHA uses 5 dB, NIOSH uses 3 dB, and they diverge sharply as level rises.
**In use:** "At 100 dBA, that's 2 hours permitted under OSHA's 5 dB exchange rate but only 15 minutes under NIOSH's 3 dB rate — report both, not just the compliant one."
**Common misuse:** Assumed to be a fixed, standard-agnostic conversion; reporting only the OSHA-derived permissible duration hides the exposure that NIOSH's stricter exchange rate would flag as excessive, even though both are legitimate, differently-calibrated standards.

### Mass law
The principle that airborne sound transmission loss through a single-leaf partition increases roughly 6 dB per doubling of surface mass — a useful first-order estimate that breaks down at the coincidence frequency.
**In use:** "Mass law predicts about a 6 dB TL gain from doubling the gypsum layers — but check where that puts the coincidence dip for this panel thickness."
**Common misuse:** Applied as a universal linear rule across the full frequency range; every panel has a coincidence frequency where transmission loss dips well below the mass-law prediction, and doubling mass without checking that dip can leave the assembly under-isolated at the exact frequency that matters for the complaint.

### Transmission loss (TL)
The frequency-band-by-band reduction in sound energy (in dB) through a partition, measured across the full test spectrum — the raw curve that a single-number rating like STC is derived from.
**In use:** "TL curve shows the coincidence dip sitting right at 2500 Hz — that's inside the STC-rated range but the single number won't show you where the dip is."
**Common misuse:** Treated as interchangeable with the STC number itself; STC is a curve-fit summary against a reference contour, and a partition can carry an acceptable STC while still having a problem frequency the single number conceals.

### Background noise floor
The steady-state ambient sound level present in a space with no intentional source active — the level against which speech intelligibility, music dynamics, or a target NC rating are actually judged.
**In use:** "Background floor measures NC 28 unoccupied — the mechanical system alone is eating most of the NC 30 budget before anyone's even in the room."
**Common misuse:** Measured with the HVAC or other mechanical systems off, then compared against an occupied-condition target; a floor measured under non-representative conditions overstates the margin actually available once the building is running as designed.

### Proof-of-performance verification (post-construction measurement)
The measured RT60/NC/STC data taken in the completed space, checked against the design target — the step that closes the loop between the model and the built condition.
**In use:** "Sign-off is pending field IIC verification; the calculated value cleared the target but nothing's final until the tapping-machine test confirms it built as modeled."
**Common misuse:** Skipped once the design calculation clears the target, on the assumption that a compliant model guarantees a compliant building; the acoustic sign-off is only as good as the last unreviewed architectural or mechanical change, and an unverified model isn't a completed engagement.
