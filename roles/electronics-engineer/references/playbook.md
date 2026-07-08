# Playbook

Filled sequences for the three recurring design-and-verification tasks: RF link budget, active-filter design, and EMC pre-compliance. Each is a real worked procedure with formulas and standard tables, not a description of one.

## 1. RF link budget

**Step sequence:**

1. **Compute free-space path loss.** FSPL(dB) = 20*log10(d_km) + 20*log10(f_MHz) + 32.44 (distance in km, frequency in MHz). Example: 5 km at 2.4 GHz (2400 MHz) → 20log10(5) + 20log10(2400) + 32.44 = 13.98 + 67.60 + 32.44 = **114.02 dB**.
2. **Add environment-specific excess loss** on top of free space — these are stated design heuristics, verify against a site survey or propagation model (e.g., Longley-Rice, ITU-R P.452) for anything commercial:

   | Environment | Typical excess loss over FSPL |
   |---|---|
   | Open line-of-sight, no obstruction | 0 dB |
   | Light foliage / suburban | 3-6 dB |
   | Moderate forest / rolling terrain | 6-12 dB |
   | Dense urban / heavy obstruction | 15-25 dB |

3. **Sum the link budget:**
   Received power (dBm) = TX power (dBm) + TX antenna gain (dBi) + RX antenna gain (dBi) − TX feeder/connector loss (dB) − total path loss (dB) − RX feeder/connector loss (dB).
4. **Compare received power to receiver sensitivity at the intended data rate/modulation** (from the transceiver datasheet, not a rounded assumption). Margin = received power − sensitivity.
5. **Apply the fade-margin target for the deployment class:**

   | Deployment class | Typical fade-margin target |
   |---|---|
   | Indoor, controlled environment | 10 dB |
   | Fixed outdoor, line-of-sight | 15 dB |
   | Outdoor with seasonal foliage/weather variation | 20-25 dB |
   | Mobile / NLOS-prone | 25-30 dB |

6. **If margin < target, adjust one variable and recompute** — in priority order of cost-to-implement: (a) reduce data rate (recovers ~10 dB sensitivity per 10x rate reduction at fixed modulation), (b) raise antenna gain (cheap, but check local regulatory EIRP limit isn't exceeded), (c) raise TX power (check regulatory conducted-power limit), (d) change antenna height/siting to cut excess loss.
7. **Check the regulatory EIRP ceiling isn't exceeded** by any change in step 6: EIRP(dBm) = TX power (dBm) + TX antenna gain (dBi) − feeder loss (dB). Under FCC §15.247 for digitally modulated systems in the 902-928 MHz band with the frequency-hopping or digital-modulation provisions met, the conducted-power limit is +30 dBm (1 W) and EIRP is generally unrestricted for digitally-modulated systems meeting bandwidth requirements — verify against the current rule text and the specific sub-band, since limits differ by band and modulation type.

## 2. Active filter design (Sallen-Key, equal-component Butterworth)

**Target:** given a required cutoff frequency fc and a maximally-flat (Butterworth, Q = 0.707) response:

1. Pick a standard capacitor value C (start with 1 nF-100 nF range for audio/instrumentation-band filters).
2. Solve R = 1 / (2*pi*fc*C).
3. Round R to the nearest E96 (1%) standard value; recompute the realized fc = 1/(2*pi*R*C) and confirm it's within the design's tolerance budget (typically ≤2-5% of target, tighter if cascaded with other stages).
4. Set the non-inverting gain required for the target Q: K = 3 − 2Q. For Butterworth (Q=0.707), K = 1.586.
5. Realize K via K = 1 + Rf/Rg: pick Rg (commonly 10 kΩ), solve Rf = (K−1)*Rg, round to nearest E96 value, recompute realized K and confirm error is within tolerance.

**Worked reference table (C = 10 nF, Butterworth):**

| Target fc | Ideal R | Nearest E96 R | Realized fc | Error |
|---|---|---|---|---|
| 1000 Hz | 15.92 kΩ | 15.8 kΩ | 1007 Hz | 0.7% |
| 2500 Hz | 6.37 kΩ | 6.34 kΩ | 2510 Hz | 0.4% |
| 5000 Hz | 3.18 kΩ | 3.16 kΩ | 5038 Hz | 0.8% |

**Higher-Q or multi-pole needs:** past Q ~3-5, switch to a multiple-feedback (MFB) topology — Sallen-Key's component sensitivity to tolerance grows with Q, making an MFB stage (or a cascaded pair of lower-Q Sallen-Key stages) the more manufacturable choice. For >2nd-order response, cascade 2nd-order (and, for odd order, one 1st-order RC) stages using standard Butterworth/Chebyshev pole-location tables rather than deriving pole positions from scratch.

## 3. EMC pre-compliance scan sequence

1. **Identify the applicable limit table before scanning** — for a US unintentional radiator, FCC Part 15.109 (radiated) Class B limits (residential/consumer):

   | Frequency range | Field strength limit at 3 m |
   |---|---|
   | 30-88 MHz | 100 µV/m |
   | 88-216 MHz | 150 µV/m |
   | 216-960 MHz | 200 µV/m |
   | above 960 MHz | 500 µV/m |

   Class A (commercial/industrial) limits are looser by roughly 15-20 dB — confirm which class applies to the product's intended use before comparing a scan to a limit line.

2. **Convert every limit and measurement to dBµV/m for comparable math**: dBµV/m = 20*log10(µV/m). (500 µV/m = 53.98 dBµV/m; 200 µV/m = 46.02 dBµV/m.)

3. **Scan harmonics of every clock and RF carrier in the design**, not just the fundamental — a spread-spectrum radio's fundamental is regulated under Part 15.247, but its 2nd and 3rd harmonics fall under the Part 15.209 unintentional-radiator limits at their respective frequencies.

4. **Compute margin = limit (dBµV/m) − measured (dBµV/m)** for every identified emission. Apply the 6 dB pre-compliance margin heuristic: below 6 dB, treat as a likely fail at the accredited lab (chamber-to-chamber variance, cable routing differences, and production-unit spread routinely consume several dB) and fix before scheduling formal test time.

5. **If a harmonic fails margin, prioritize fixes in this order**: (a) add or tighten an output low-pass/harmonic filter at the PA, (b) improve ground-plane/return-path layout under the offending trace, (c) add shielding local to the emitting component, (d) as a last resort, re-derate TX power (only if the link budget still closes with the reduced power — recheck step 1's margin before committing).

6. **Document every measurement with frequency, measured level, limit, class, and margin** in a pre-compliance report — this is the artifact the accredited lab and the regulatory filing both reference.
