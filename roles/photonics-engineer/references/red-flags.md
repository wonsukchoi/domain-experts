# Red flags

Smell tests a photonics engineer catches in the first pass over a link-budget spreadsheet, a lens spec, an OTDR trace, or a laser safety procedure.

### Fiber link margin computed only for day-one, with no aging or repair-splice allowance

- **Usually means:** the design passes initial installation test and is quietly designed to fail years later as fiber ages, connectors wear from re-mating, and repair splices accumulate.
- **First question:** what design life was assumed, and what fiber-aging and future-repair-splice allowance is in the budget?
- **Data to pull:** the link-budget spreadsheet's stated assumptions, and any prior route's actual OTDR history over its service life.

### "Collimated" beam spec given with no stated propagation distance

- **Usually means:** the beam's Rayleigh range was never checked against the actual target distance, so the spot size at the target may be far larger than the design assumed.
- **First question:** what's zR = π w0²/λ for this waist, and is the target distance inside or well beyond it?
- **Data to pull:** the source's measured or specified beam waist and the actual optical path length in the application.

### Laser hazard class assigned from power alone, with no wavelength/exposure-duration MPE lookup

- **Usually means:** the class is wrong in either direction — MPE varies by orders of magnitude between the retinal-hazard region (400-1400 nm) and the cornea-absorbed region beyond it, at the same power.
- **First question:** which MPE table entry (wavelength band, exposure duration) was actually used to derive this class?
- **Data to pull:** the ANSI Z136.1/IEC 60825-1 table row cited, and its edition/date.

### Connector or splice loss values in a link budget with no cited source

- **Usually means:** "typical" numbers were assumed instead of pulled from a vendor datasheet or a field OTDR measurement, and the real as-built loss may differ meaningfully.
- **First question:** is each loss value measured (OTDR) or assumed (datasheet typical), and which?
- **Data to pull:** the OTDR trace or connector/splice vendor insertion-loss spec actually used per line item.

### Lens spec pushes for a smaller spot or finer resolution while already at or past the diffraction limit for the stated f-number and wavelength

- **Usually means:** budget is being spent correcting aberrations on a lens that's already diffraction-limited — the real floor is the Airy disk diameter, which no amount of aberration correction moves.
- **First question:** what's the Airy disk diameter (2.44 λ f/#) at the current f-number, and is the requirement above or below it?
- **Data to pull:** the lens's f-number and operating wavelength, and the stated resolution or spot-size requirement.

### NOHD calculated for naked-eye viewing only, on a beam path techs routinely inspect with a scope or loupe

- **Usually means:** the real instrument-assisted hazard was never evaluated, even though the naked-eye NOHD calculation looks small and safe.
- **First question:** what optical instruments (fiber-inspection scope, loupe, binoculars) are actually used near this beam in normal operation or maintenance?
- **Data to pull:** the written alignment/maintenance procedure or work instruction for the beam path.

### Beam quality M² assumed equal to 1 on a source that hasn't been measured

- **Usually means:** the coupling-efficiency and focused-spot-size calculations are optimistic — a real M² > 1 source focuses to a larger spot and couples with lower efficiency than the ideal-Gaussian-beam formula predicts.
- **First question:** has M² actually been measured (ISO 11146 beam-profiler method) for this source, or assumed?
- **Data to pull:** the beam-profiler measurement report, or the source datasheet's stated M² spec if no measurement exists.

### Focus or beam-quality degradation that tracks with optical power and recovers on cooldown, treated as an alignment problem

- **Usually means:** thermal lensing in an optic or gain medium, not a loose or drifted mechanical mount — the symptom signatures are different and point to different fixes.
- **First question:** does the degradation track with power/duty cycle, or with elapsed time/vibration since last alignment?
- **Data to pull:** a beam-profiler trace taken across a power ramp, alongside the mount's torque/vibration log.

### Field OTDR trace shows more than 1-2 dB of unexplained loss versus the as-designed budget

- **Usually means:** an unaccounted event exists between two known reference points — a bad splice, a macrobend below the fiber's minimum radius, or connector-end contamination.
- **First question:** at what distance along the trace does measured loss diverge from the budgeted prediction?
- **Data to pull:** the full OTDR trace with its event table, compared line-by-line against the as-designed budget spreadsheet.

### Multimode fiber specified for a link approaching or exceeding its bandwidth-distance product at the required data rate

- **Usually means:** modal dispersion, not attenuation, will limit the link — a link that closes cleanly on a power (dB) budget can still fail on eye closure/bit errors from dispersion, which a simple power budget never checks.
- **First question:** what's the fiber's modal bandwidth (MHz·km) at the operating wavelength, versus the required data rate x link length?
- **Data to pull:** the fiber's OM-class datasheet spec and the system's actual data rate and link length.

### Laser product documentation states an eye-safety class with no MPE/AEL/NOHD calculation or accredited test report behind it

- **Usually means:** the classification was asserted, not computed or independently verified, and won't survive an audit, incident investigation, or customer safety review.
- **First question:** where is the calculation worksheet or third-party test certificate backing this printed class?
- **Data to pull:** the classification worksheet (MPE, NOHD, viewing scenarios evaluated) or the accredited lab's test report.
