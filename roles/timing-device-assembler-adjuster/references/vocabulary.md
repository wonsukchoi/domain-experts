# Vocabulary

### Position error (rate variation)
The variation in a mechanical timing mechanism's rate caused by gravity affecting the balance wheel/escapement system differently depending on the device's physical orientation.
**In use:** "Position error's showing up as a five-second-per-day swing between dial-up and crown-down — that's within the mechanism, not a testing artifact."
**Common misuse:** Assuming a rate reading taken in one position represents the device's overall accuracy — position error is a real, characteristic behavior of balance-wheel timing mechanisms, and a single-position test can't reveal how the device performs in other orientations it will actually experience.

### Isochronism
The ideal property of a timing mechanism's oscillator (like a balance wheel and hairspring) maintaining a constant period regardless of amplitude, position, or temperature — real mechanisms deviate from perfect isochronism, requiring regulation to minimize that deviation.
**In use:** "We're regulating to minimize isochronism error across positions, not just chasing a single perfect bench reading."
**Common misuse:** Treating a single accurate bench reading as evidence of good isochronism — true isochronism performance is only revealed by testing across the actual range of positions, temperatures, and amplitudes the device will experience.

### Rate regulation
The process of adjusting a timing mechanism's escapement or oscillator system to bring its rate within specification, which must account for position and temperature sensitivity rather than a single test condition.
**In use:** "Regulation's not done until we've confirmed rate across all five positions and both temperature extremes, not just the first good reading we get."
**Common misuse:** Considering regulation complete after achieving a single accurate reading in one convenient test condition — regulation needs to account for the full range of conditions the specification requires, since a mechanism's rate genuinely varies across them.

### Component-specific lubrication
The practice of matching lubricant type, viscosity, quantity, and placement to each individual component's specific requirements, rather than applying a single generalized lubrication approach across an entire mechanism.
**In use:** "Different oil on the escapement pivots than on the mainspring barrel — each has its own specified lubricant for a reason."
**Common misuse:** Using a single, generic lubricant and application method across all components — different components experience different loads, speeds, and friction characteristics, and a mismatched lubricant can measurably affect rate or cause premature wear even if "some oil" was applied.

### Contamination (precision mechanism assembly)
The presence of dust, debris, or incorrect lubricant at a scale that measurably affects a fine mechanism's performance, treated as a functional defect equivalent to a dimensional error rather than a cosmetic concern.
**In use:** "That's not just dust — at this scale, contamination on a pivot changes friction enough to show up as a measurable rate shift."
**Common misuse:** Treating cleanliness during assembly as general good practice or tidiness rather than a functional performance requirement — at the scale of fine timing mechanisms, contamination has a direct, measurable effect on rate and wear, not just appearance.

### Multi-position testing
A verification protocol testing a timing mechanism's rate across several standard orientations (and often temperature extremes) rather than a single bench-test position, revealing position- and temperature-dependent variation.
**In use:** "Multi-position testing caught a five-second swing that single-position testing would have completely missed."
**Common misuse:** Treating a single-position rate reading as sufficient verification — multi-position testing exists specifically because position-dependent variation is a real, common characteristic that a single test condition cannot reveal.

### Escapement
The mechanism in a mechanical timing device that regulates the release of energy from the mainspring in precise increments, directly determining the timekeeping accuracy of the whole mechanism.
**In use:** "Escapement adjustment is where we're addressing the crown-down position error — that's the component actually controlling rate at that orientation."
**Common misuse:** Treating rate problems as generically "somewhere in the mechanism" rather than diagnosing which specific component (escapement, hairspring, balance) is responsible for a given symptom — different rate issues (overall drift vs. position-specific variation vs. temperature sensitivity) point to different components needing adjustment.

### Assembly checkpoint (fine mechanism)
An intermediate verification step during a multi-stage assembly process, confirming a specific component or sub-assembly's function before the next component is added and potentially obscures access to it.
**In use:** "Checking the escapement function now, before the bridge goes on top and we lose easy access to it."
**Common misuse:** Deferring all verification to final assembly test — for fine mechanisms with a specified assembly sequence, catching an issue at an intermediate checkpoint is far cheaper and lower-risk than discovering it after final assembly, when correcting it requires disassembly that risks introducing new problems.

### Hairspring (balance spring)
A fine coiled spring paired with a balance wheel to regulate oscillation period in a mechanical timing mechanism, whose material properties and attachment are especially sensitive to temperature.
**In use:** "That high-temperature rate deviation points at the hairspring — checking its attachment and material spec before assuming it's an escapement issue."
**Common misuse:** Assuming all rate deviations trace to the escapement or general "mechanism wear" — temperature-specific rate issues in particular often point specifically to the hairspring's material properties or attachment, a distinct component requiring its own targeted investigation.
