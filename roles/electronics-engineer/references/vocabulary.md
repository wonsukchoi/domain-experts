# Vocabulary

### Link budget
The full accounting of every gain and loss between a transmitter and receiver — TX power, antenna gains, feeder/connector losses, path loss, and receiver sensitivity — reduced to a single margin number.
**In use:** "The link budget closes with 12 dB of margin at 50 kbps, but only 2 dB at 250 kbps — we're shipping at 50 kbps."
**Common misuse:** treating "received power is above sensitivity" as equivalent to "the link is closed" — it ignores the fade-margin target the deployment class actually requires.

### Fade margin
The extra link-budget headroom, beyond bare sensitivity, reserved to absorb signal variation over time and conditions — multipath, weather, foliage growth, connector aging.
**In use:** "This is an outdoor link with seasonal foliage, so we're designing to a 20 dB fade-margin target, not the 10 dB we'd use indoors."
**Common misuse:** using one fixed fade-margin number for every deployment class, instead of scaling it to the environment's actual variability.

### Noise figure
The degradation in signal-to-noise ratio a stage or system introduces relative to an ideal noiseless stage, expressed in dB.
**In use:** "The LNA's 1.2 dB noise figure sets the receive chain's noise floor almost entirely — the mixer's 8 dB noise figure barely matters behind 20 dB of LNA gain."
**Common misuse:** assuming every stage in a chain contributes noise proportionally, instead of recognizing the first gain stage dominates per the Friis cascade equation.

### Gain-bandwidth product (GBW)
The constant relating an amplifier's open-loop gain to its bandwidth at a given frequency; closed-loop bandwidth at a set gain is approximately GBW divided by that gain.
**In use:** "We need 500 Hz of bandwidth at a gain of 100 — that's a 50 kHz minimum GBW, so we're specifying a part with at least 5x that for margin."
**Common misuse:** picking an op-amp by its GBW number alone without dividing by the actual closed-loop gain the circuit uses, then being surprised the bandwidth is far short of expectation.

### Sallen-Key filter
A common active filter topology using a single op-amp in a non-inverting configuration with two resistors and two capacitors to realize a 2nd-order response; simple to design but its component-value sensitivity to Q grows sharply at high Q.
**In use:** "Sallen-Key is fine for our Q = 0.707 anti-alias filter, but the Q = 8 IF filter needs multiple-feedback instead."
**Common misuse:** using Sallen-Key at high Q where a small resistor or capacitor tolerance error produces a large, unpredictable shift in the realized Q and cutoff.

### Multiple-feedback (MFB) filter
An active filter topology using feedback through two paths around a single op-amp, generally less sensitive to component tolerance than Sallen-Key at moderate-to-high Q, at the cost of an inverting output and more complex design equations.
**In use:** "We moved the 4 kHz bandpass stage to MFB once the required Q crossed 5 — Sallen-Key's tolerance sensitivity was making the passband shift unit to unit."
**Common misuse:** defaulting to Sallen-Key for every filter regardless of Q, without checking where MFB's better tolerance behavior becomes the deciding factor.

### EIRP (Effective Isotropic Radiated Power)
The power a theoretical isotropic antenna would need to radiate to produce the same signal strength as the actual transmitter-plus-antenna system in its strongest direction; the quantity most spectrum regulations actually limit.
**In use:** "Raising antenna gain to close the link budget also raises EIRP — check it's still under the band's regulatory ceiling before specifying the antenna."
**Common misuse:** confusing conducted TX power (what the radio chip outputs) with EIRP (what the antenna system radiates) — regulatory limits and link-budget calculations use different ones of these at different points.

### Radiated vs. conducted emissions
Radiated emissions are unwanted energy leaving a product through free space (measured with an antenna at a set distance); conducted emissions are unwanted energy leaving through a cable or power line (measured with a line impedance stabilization network). Different test methods, different limit tables, different root causes.
**In use:** "The 1830 MHz spur showed up on the radiated scan, not conducted — that points to the antenna or PCB trace as the radiator, not the power cable."
**Common misuse:** treating an emissions failure as one undifferentiated "EMC problem" instead of identifying which coupling path (radiated or conducted) is actually responsible, which determines the fix.

### Intentional vs. unintentional radiator (FCC Part 15)
An intentional radiator is a device designed to emit RF energy for communication (a radio transmitter, regulated under FCC Part 15.247 or similar); an unintentional radiator is a device whose RF emissions are an unwanted byproduct of digital circuitry (regulated under Part 15.109/15.209). The same product commonly contains both and each is checked against a different limit table.
**In use:** "The radio's fundamental is checked against Part 15.247's intentional-radiator limits; its harmonics and the MCU's clock harmonics are checked against Part 15.209's unintentional-radiator limits."
**Common misuse:** assuming one FCC Part 15 compliance test covers the whole product, instead of recognizing the radio and the digital board are regulated under different subparts with different limit tables.

### Superheterodyne vs. direct-conversion (zero-IF) receiver
Superheterodyne down-converts the RF signal to a fixed intermediate frequency (IF) before final demodulation, giving strong image rejection via IF filtering; direct-conversion mixes straight to baseband, simplifying the design but exposing it to DC offset from LO self-mixing and 1/f noise near DC.
**In use:** "We're staying superheterodyne on this narrowband link — the direct-conversion DC-offset problem would eat into our already-tight sensitivity budget."
**Common misuse:** choosing direct-conversion purely for its lower part count and smaller size without checking whether the application's required sensitivity and baseband bandwidth can tolerate its DC-offset and flicker-noise floor.

### Image frequency
In a superheterodyne receiver, the frequency that mixes to the same intermediate frequency as the desired signal and, if not filtered out ahead of the mixer, produces a spurious response indistinguishable from the wanted signal.
**In use:** "The image frequency sits 2x the IF away from the desired channel — our RF preselector filter needs at least 40 dB of rejection there."
**Common misuse:** assuming the IF filter alone handles image rejection — image rejection has to happen before the mixer, in the RF stage, because the IF filter can't distinguish the image from the desired signal once both are at the same IF.

### Pre-compliance (EMC)
An in-house or informal scan against a regulatory emissions or immunity limit, performed before the formal, accredited-lab compliance test, to catch and fix problems while they're still cheap to fix.
**In use:** "Pre-compliance found the second-harmonic spur 4 dB under the limit — inside our 6 dB margin heuristic, so we filtered the PA output before scheduling the accredited chamber."
**Common misuse:** treating a pre-compliance pass with near-zero margin as equivalent to an accredited-lab pass, ignoring chamber-to-chamber measurement variance and production spread.

### Friis transmission equation
The formula relating received power to transmitted power, antenna gains, and free-space path loss as a function of distance and frequency — the core equation behind any RF link budget's path-loss term.
**In use:** "Run the Friis equation at the actual deployment frequency, not the nearest round number — a 2.4 GHz vs. 2.45 GHz difference moves path loss by a fraction of a dB but it should still be the real number."
**Common misuse:** confusing the Friis transmission equation (link path loss) with the separate Friis noise-figure cascade equation (receiver chain noise) — same author, two different formulas solving different problems.
