# Playbook

Filled sequences for the four recurring photonics design-and-verification tasks: coupling-lens sizing, fiber link power budget, diffraction-limited lens/resolution check, and laser MPE/NOHD classification. Each is a real worked procedure with formulas and reference tables, not a description of one.

## 1. Coupling-lens sizing (source into single-mode fiber)

**Target:** given a source's near-field beam waist w0_source and divergence, size a two-lens (collimator f1 + focuser f2) system to match the target fiber's mode field radius w0_fiber.

1. Compute the source's far-field divergence half-angle: θ = λ / (π w0_source).
2. Pick a catalog collimating lens f1 (typical range 3-8 mm for laser-diode collimation); compute the collimated beam waist: w1 = f1 x θ.
3. Solve for the ideal focusing-lens focal length: f2 = w0_fiber x π x w1 / λ.
4. Round f2 to the nearest catalog aspheric focal length; recompute the realized output waist: w0_out = f2 x λ / (π w1).
5. Compute mode-mismatch coupling efficiency: η = [2 w0_out w0_fiber / (w0_out² + w0_fiber²)]²; convert to dB loss: -10 log10(η).
6. Add the assembly's alignment-tolerance loss allowance (stated heuristic **0.3-0.8 dB** for a production two-lens fiber-coupling assembly, tighter toward 0.3 dB for actively-aligned/epoxied assemblies, looser toward 0.8 dB for passively-aligned ferrule-based ones) — this, not mode mismatch, is usually the dominant real-world loss term.

**Worked reference table (1550 nm source, SMF-28 target w0_fiber = 5.2 µm, C = f1 = 4.5 mm):**

| Source w0 | θ (rad) | w1 (mm) | Ideal f2 | Nearest catalog f2 | Realized w0_out | Mismatch loss |
|---|---|---|---|---|---|---|
| 1.0 µm | 0.4935 | 2.221 | 23.4 mm | 22.85 mm | 5.08 µm | -0.002 dB |
| 1.5 µm | 0.3290 | 1.4805 | 15.6 mm | 15.29 mm | 5.09 µm | -0.002 dB |
| 2.0 µm | 0.2468 | 1.1105 | 11.7 mm | 11.00 mm | 4.79 µm | -0.03 dB |

**Single-lens (ball/GRIN) alternative:** faster and cheaper to align, but couples a fixed magnification set by the ball/GRIN's own geometry — mismatch loss and alignment sensitivity are both materially higher (stated heuristic: 1-2 dB total coupling loss typical, vs. 0.3-0.8 dB for a two-lens assembly). Use when board space or per-unit cost rules out the two-lens approach and the extra 1-2 dB is affordable in the link budget.

## 2. Fiber link power budget (day-one and end-of-life)

1. **Sum day-one loss** from real datasheet/spec values, not rounded assumptions:

   | Loss term | Typical value | Source |
   |---|---|---|
   | SMF attenuation @ 1310 nm | 0.35 dB/km | ITU-T G.652 |
   | SMF attenuation @ 1550 nm | 0.20-0.22 dB/km | ITU-T G.652 |
   | Connector (physical contact, PC/APC) | 0.2-0.5 dB each | connector datasheet |
   | Fusion splice | 0.05-0.15 dB each | field OTDR-measured average |
   | Mechanical splice | 0.1-0.3 dB each | field OTDR-measured average |
   | Macrobend (per bend, radius below spec) | 0.5-2+ dB per bend | fiber datasheet bend-loss curve |

2. **Compute received power** = launch power (dBm, after coupling loss) - total day-one loss (dB). Compare against receiver sensitivity (dBm) for margin.
3. **Add end-of-life additions**, each a stated design allowance — verify against the specific fiber vendor's aging spec and the carrier's own maintenance history before using in a filed design:

   | End-of-life term | Stated allowance |
   |---|---|
   | Fiber aging (buried/aerial plant, 20-yr life) | 0.02-0.05 dB/km cumulative |
   | Connector re-mating wear (per connector, over life) | 0.1-0.3 dB |
   | Future repair splices (budget N splices per 10-20 km of route) | 0.05-0.15 dB each |
   | Temperature extremes (macrobend sensitivity at cold temperature) | 0.5-1 dB, cold-weather installs only |

4. **Recompute margin at end of life.** Design-margin thresholds by link class (stated telecom design practice, not a universal standard):

   | Link class | Minimum end-of-life margin |
   |---|---|
   | Short-haul / data center (<2 km) | 1-2 dB |
   | Metro / access (2-40 km) | 2-3 dB |
   | Long-haul unrepeatered (40-120 km) | 3-6 dB |

5. **If end-of-life margin is under the threshold**, adjust in priority order: (a) reduce splice count via longer fiber-reel runs, (b) specify a lower-loss connector grade (APC vs. UPC), (c) raise launch power (check laser eye-safety classification doesn't change), (d) add an optical amplifier or repeater — highest cost, last resort.

## 3. Diffraction-limited lens / resolution check (Rayleigh criterion)

**Airy disk diameter at focus:** d_Airy = 2.44 x λ x (f/#).

**Worked reference table (Airy disk diameter, µm):**

| f/# | 550 nm (visible) | 1064 nm (Nd:YAG) | 1550 nm (telecom IR) |
|---|---|---|---|
| f/1.4 | 1.88 | 3.63 | 5.29 |
| f/2.8 | 3.75 | 7.27 | 10.58 |
| f/5.6 | 7.51 | 14.54 | 21.17 |
| f/11 | 14.76 | 28.58 | 41.62 |

**Worked example — machine-vision lens selection.** A vision system must resolve features on a sensor with 3.45 µm pixel pitch, illuminated at 550 nm. Practical rule: the Airy disk diameter should stay at or below roughly 2x the pixel pitch, or the lens (not the sensor) becomes the resolution bottleneck. Target: d_Airy <= 2 x 3.45 = 6.9 µm. Solve for f/#: f/# <= 6.9 / (2.44 x 0.55) = 6.9 / 1.342 = **5.14**. A candidate f/8 lens gives d_Airy = 2.44 x 0.55 x 8 = **10.74 µm**, above the 6.9 µm threshold — the lens diffraction-limits the system before the sensor's pixel pitch does; specify an f/4 or faster lens instead of a higher-megapixel sensor to actually gain resolution.

## 4. Laser MPE and NOHD classification

1. **Identify wavelength band and exposure duration** — MPE tables differ by band (400-1400 nm retinal-hazard region vs. beyond ~1400 nm cornea/lens-hazard region) and by exposure duration class (typically <=0.25 s, up to 10 s, >=10 s/extended for CW sources). Pull the MPE from the current ANSI Z136.1 or IEC 60825-1 table for the actual band/duration — do not reuse an MPE from a different band.
2. **Compute NOHD** (far-field, point-source approximation): NOHD = (2/Θ) x sqrt(Φ / (π x MPE)), where Θ is the full-angle beam divergence (rad), Φ is source power (W), and MPE is in W/cm² (keep units consistent — Φ in W and MPE in W/cm² gives NOHD in cm).
3. **Compare against the AEL (Accessible Emission Limit) class boundaries** — the widely-cited, wavelength-independent CW boundary is **500 mW at the aperture** for the Class 3B/Class 4 line (ANSI Z136.1/IEC 60825-1); Class 1/1M/2/2M/3R/3B boundaries below that are wavelength- and exposure-duration-dependent and must be read from the standard's table, not assumed.
4. **Evaluate every credible viewing scenario, not just naked eye** — if a naked-eye NOHD comes out small, still check whether the operating or maintenance procedure involves a loupe, fiber-inspection scope, binoculars, or any other magnifying/collecting optic anywhere near the beam path. If so, classify as at least Class 1M/2M/3R (instrument-hazard) rather than the naked-eye-only class.
5. **Document the classification** with the MPE value, its source table/edition, the NOHD calculation, and every viewing scenario evaluated — this is the artifact a laser safety officer or auditor checks against, not a printed "Class 1" label alone.
