# Red flags

Smell tests an RF/analog electronics engineer catches in the first pass over a design, a bench measurement, or a compliance-lab report.

### Link margin computed under 3 dB above the deployment class's fade-margin target

- **Usually means:** the design closes on paper today but will fail after cable aging, connector corrosion, or a season of foliage growth — the margin exists to absorb exactly that drift.
- **First question:** which single variable (data rate, antenna gain, TX power) is cheapest to change to buy back margin, and does changing it stay under the regulatory EIRP ceiling?
- **Data to pull:** the full link-budget spreadsheet with every stage's source (datasheet page, not a rounded assumption), and the site's actual terrain/obstruction profile.

### Filter or amplifier spec set without a rechecked gain-bandwidth or Q consequence

- **Usually means:** gain, bandwidth, or data rate was raised in isolation, without recomputing the linked constraint (GBW product, receiver sensitivity, filter component sensitivity) it trades against.
- **First question:** what was the gain-bandwidth product, or the sensitivity-vs.-rate tradeoff, before and after this change?
- **Data to pull:** the op-amp or transceiver datasheet's actual GBW or sensitivity table at the new operating point, not the old one.

### Bench prototype passes at nominal but the design hasn't been run through a tolerance/temperature corner check

- **Usually means:** the design works with the specific components on the bench, at room temperature, but hasn't been shown to survive the worst-case combination of component tolerance, temperature, and supply voltage a production run will see.
- **First question:** what's the worst-case (not nominal) cutoff frequency, gain, or margin using each component's actual tolerance and the datasheet's temperature coefficient?
- **Data to pull:** component tolerance specs (E96 = 1%, E24 = 5%, or the actual bin), temperature coefficient (ppm/°C), and the product's rated operating temperature range.

### EMC pre-compliance scan shows a harmonic within 6 dB of the limit line

- **Usually means:** chamber-to-chamber measurement variance, cable routing differences, or normal production-unit spread will push at least some units over the limit at the accredited lab.
- **First question:** which harmonic and which fix (output filter, layout, shielding, power derate) buys the most margin for the least cost and schedule risk?
- **Data to pull:** the full pre-compliance scan (frequency, level, limit, class, margin per emission), not just the emissions that were closest to failing.

### Receiver desense or blocking appears only with the antenna connected, not on a cabled bench test

- **Usually means:** a nearby strong out-of-band emitter is overloading the front end (radiated susceptibility), not a baseband or digital bug — a cabled test bypasses the antenna and the RF environment entirely.
- **First question:** what known strong emitters (cellular, Wi-Fi, another product on the same site) are in-band or near-band to the receiver's front-end filter passband?
- **Data to pull:** a spectrum survey at the deployment site, and the receiver front-end filter's actual rejection curve at the suspect frequency.

### A link budget or filter memo has a formula result quoted with no corresponding real component value

- **Usually means:** the design stopped at the ideal-math stage and was never carried through to a buildable bill of materials — the ideal R or C value from a formula isn't a standard part.
- **First question:** what's the nearest E96/E24 standard value, and what's the resulting realized (not ideal) performance number?
- **Data to pull:** the BOM with actual specified part values and tolerances.

### An intentional radiator's data rate or modulation was changed late in the program without re-verifying Part 15.247 (or the equivalent non-US) compliance basis

- **Usually means:** the original compliance filing or pre-compliance scan was run against a different modulation/bandwidth configuration than what's now shipping.
- **First question:** does the current configuration still meet the digital-modulation or frequency-hopping conditions the original limit calculation (or FCC grant) assumed?
- **Data to pull:** the FCC grant or test report's stated operating parameters, compared line-by-line against the current firmware/radio configuration.

### A noise-figure or sensitivity problem is being chased by upgrading a component deep in the signal chain

- **Usually means:** per the Friis noise-figure cascade, a downstream stage's noise contribution is already suppressed by the gain ahead of it — the real leverage is almost always the first active stage (LNA, first mixer, first amplifier).
- **First question:** what's the first active stage's noise figure and gain, and has the cascade calculation actually been run to confirm where the noise floor is being set?
- **Data to pull:** stage-by-stage gain and noise-figure numbers for the full receive chain, from antenna to baseband.

### A design reuses a reference design's antenna or filter values without re-deriving them against this project's actual frequency, impedance, or enclosure

- **Usually means:** the reference design's values were tuned for a different board layout, enclosure material, or frequency plan, and copying them skips the re-derivation that made them correct in the first place.
- **First question:** what's different about this project's enclosure, ground-plane geometry, or operating frequency versus the reference design's?
- **Data to pull:** the reference design's original application note or schematic notes stating what it was tuned for, and this project's actual mechanical/enclosure drawing.
