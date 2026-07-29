# Acoustical Engineer — Red Flags

### Assembly spec'd with 3 points or fewer of field-margin cushion above the target STC/IIC
- **Usually means:** the design team is quoting the lab rating (ASTM E90/E492) as if it were the delivered field rating, with no allowance for the 5-10 point field-vs-lab gap documented under ASTM E1007.
- **First question:** "What field STC/IIC number are we designing to, not the lab number on the manufacturer's data sheet?"
- **Data to pull:** the assembly's lab test report and the project's target STC/IIC line item in the design brief.

### RT60 calculation lands within 0.1s of the applicable code or brief boundary
- **Usually means:** the room was designed to just clear the standard (e.g. ANSI/ASA S12.60's ≤0.6s classroom ceiling) rather than to a comfortable margin, leaving no room for as-built variance in furnishing or occupancy.
- **First question:** "What happens to speech intelligibility or musical warmth if this room measures 0.1s over the calculated value once built and furnished?"
- **Data to pull:** the RT60 calculation worksheet, including which absorption coefficients are assumed-vs-measured.

### Average room absorption coefficient exceeds ~0.2–0.3 but the RT60 calc still uses Sabine's formula
- **Usually means:** the calculation was run once with a stock formula and never re-checked against the room's actual treatment level; Sabine's error climbs toward ~28% in heavily damped rooms.
- **First question:** "Has this been re-run in Eyring, and does the answer still clear the target?"
- **Data to pull:** the surface-by-surface absorption schedule used in the calculation.

### Occupational noise exposure reported against OSHA's 90 dBA PEL with no NIOSH 85 dBA REL comparison
- **Usually means:** the report is citing the legal floor as if it were the health target — OSHA's 5 dB exchange rate and NIOSH's stricter 3 dB exchange rate can disagree by hours of permitted exposure at the same measured level.
- **First question:** "What does this same exposure look like run through NIOSH's exchange rate, not just OSHA's?"
- **Data to pull:** the dosimetry log (measured dBA and duration per task) and both exchange-rate calculations side by side.

### Thin (<2 in) foam panel treatment specified as the fix for a low-frequency (<250 Hz) complaint
- **Usually means:** a broadband-marketed product is being applied to a problem it doesn't address — thin foam does essentially nothing below a few hundred Hz, and bass energy is a corner/boundary geometry problem, not a surface-material one.
- **First question:** "Has corner/boundary bass-trapping or source relocation been evaluated before adding more panel area?"
- **Data to pull:** the frequency-resolved measurement (not just a broadband dB reading) that identified the complaint band.

### NC or dBA target cleared by less than 2 dB of margin, concentrated in one or two tonal bands
- **Usually means:** the mechanical design is passing on paper by exploiting exactly the bands the calculation checks, with no buffer for the field-installation variance and flanking that silencer/lined-duct attenuation routinely loses.
- **First question:** "If the as-built result comes in 3 dB worse than calculated in just those bands, does this still pass?"
- **Data to pull:** the band-by-band NC worksheet, not the single summary dB(A) figure.

### Seating, wall-geometry, or ceiling-height change made after construction documents are issued, with no re-run of the acoustic model
- **Usually means:** the change was treated as an architectural or scheduling decision only, on the assumption that an earlier acoustic sign-off still holds — the same failure mode that took Philharmonic Hall (now David Geffen Hall) from its 1962 opening to a 1976 gut renovation.
- **First question:** "Has this change been routed back through the acoustic model, and if not, why was it assumed not to matter?"
- **Data to pull:** the current drawing set's revision log against the date of the last acoustic model run.

### STC number quoted on a wall/floor spec with fewer than all 3 flanking paths (penetrations, continuous ceiling plenum, shared ductwork) addressed
- **Usually means:** the spec lists a rating for the assembly in isolation but doesn't name the penetrations, continuous ceiling plenum, or shared ductwork that will undermine that rating once built.
- **First question:** "What flanking paths were checked, and what's the mounting/penetration detail that keeps them from short-circuiting this rating?"
- **Data to pull:** the construction-checkable spec sheet (material, thickness, placement, mounting) and the reflected ceiling plan for continuous plenum runs.

### Non-shoebox (vineyard-style) hall geometry modeled with specular-reflection tools built for shoebox rooms
- **Usually means:** the modeling approach was carried over from standard practice without accounting for vineyard layouts defeating the specular-reflection assumptions those tools rely on.
- **First question:** "What modeling method was used for this geometry, and does it handle irregular, non-parallel surfaces?"
- **Data to pull:** the acoustic model's documented method (ray-tracing/wave model vs. classical formula) and the room's plan geometry.

### Performance-space design reviewed on RT60 alone, with no Initial Time Delay Gap figure reported despite ITDG carrying roughly 40% of Beranek's weighted hall-quality score
- **Usually means:** the review is anchored to the single most familiar number (reverberation time) while skipping the early-reflection "intimacy" metric that, per Beranek's weighted hall-quality data, outweighs RT60, bass ratio, warmth, and diffusion combined.
- **First question:** "What's the calculated or modeled ITDG for the main seating areas, not just the RT60?"
- **Data to pull:** the room model's early-reflection timing output for representative listener positions.

### Operating-room or other highest-consequence space calculated result lands exactly on the NC target
- **Usually means:** the mechanical submittal is being approved because it clears the number on paper, without weighing that a coin-flip design in the highest-consequence room type risks a failed post-occupancy test after the ceiling is closed.
- **First question:** "Why is this design sized to land exactly on NC 30 instead of a few points under it?"
- **Data to pull:** the silencer/duct-attenuation submittal's calculated margin above target, band by band.
