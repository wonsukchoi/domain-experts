# Playbook

Filled worked calculations for the artifact types this role produces most often: a UT DAC curve and 6 dB-drop sizing, an RT exposure calculation, an MT field-strength verification, and an API 570 corrosion-rate/remaining-life/interval calculation. Populate with the actual job's numbers; the structure and arithmetic below are real and reconcile.

## UT — DAC curve construction and 6 dB-drop sizing

**Setup:** butt weld, carbon steel, t = 19 mm (0.75 in), shear wave 70° probe, 2.25 MHz, per ASME Section V Article 4.

**Step 1 — build the DAC curve.** Machine (or select) a calibration block of the same material and thickness, with three side-drilled holes (SDH), 2.4 mm (3/32 in) diameter, at 1/4T, 1/2T, and 3/4T metal-path depth: 4.75 mm, 9.5 mm, 14.25 mm.

| Reflector | Depth (mm) | Sound path at 70° (mm) | Peak amplitude, gain set to 80% FSH on shallowest | Gain to bring each to reference (dB) |
|---|---|---|---|---|
| SDH 1 (1/4T) | 4.75 | 4.75/cos70° = 13.9 | 80% FSH (reference point) | 0 |
| SDH 2 (1/2T) | 9.5 | 9.5/cos70° = 27.8 | 46% FSH as found | +4.8 dB to reach 80% |
| SDH 3 (3/4T) | 14.25 | 14.25/cos70° = 41.7 | 30% FSH as found | +8.5 dB to reach 80% |

Plotting the three peak-amplitude points (sound path vs. % FSH, all normalized to the 80% FSH reference gain) and connecting them gives the **100% DAC line**. Draw a second curve at half the amplitude of the first at every sound path — the **DAC − 6 dB (50%) line** — used for 6 dB-drop sizing.

**Step 2 — scan and evaluate.** Any reflector reaching or exceeding the 100% DAC line at its sound path is recorded regardless of eventual disposition (recording threshold per ASME V Article 4 is commonly 20% DAC for welds under this scope — verify the specific referencing code's recording threshold, it is not always the same as the evaluation threshold).

**Step 3 — 6 dB-drop length sizing.** For an indication whose peak reaches 100% DAC, move the probe along the weld axis in each direction from the peak until amplitude falls to the DAC − 6 dB line; mark the probe index position at each drop point. The distance between the two marks is the reported length. Worked number: peak at probe position 142 mm (weld-axis scale reading); −6 dB drop points at 135 mm and 149 mm → length = 149 − 135 = **14 mm**.

**Step 4 — 6 dB-drop height sizing.** With the probe fixed at the peak weld-axis position, walk the probe perpendicular to the weld (toward/away from the weld centerline) to find the sound-path values where amplitude drops 6 dB on the near-surface side and far-surface side of the indication; convert each sound path to depth via depth = SP × cos(angle). Worked number (70° probe): SP_near = 15.0 mm → depth = 15.0 × cos70° = 5.13 mm; SP_far = 19.5 mm → depth = 19.5 × cos70° = 6.67 mm; height = 6.67 − 5.13 = **1.54 mm**.

**Deliverable — sizing worksheet line item:** "Weld CW-207, indication #3: SP 27.8 mm (2nd leg check: 1st-leg limit at 70°/t=19mm = 19/cos70° = 55.6mm, so SP 27.8mm is 1st-leg), depth 9.5 mm (50% T), length 14 mm (6dB), height 1.54 mm (6dB), directional response −11 dB over ±15° rotation → planar."

## RT — exposure calculation (source-to-film distance and geometric unsharpness)

**Setup:** carbon steel butt weld, t = 12.7 mm (0.5 in), single-wall single-image technique, Ir-192 source, source size F = 3 mm, Class 1 film.

**Step 1 — required minimum source-to-object distance from the geometric-unsharpness limit.** ASME Section V Article 2 Table T-274.1-type requirements commonly set Ug_max = 0.51 mm (0.020 in) for material thickness in this range (typical published value — verify against the current edition and the specific technique class before use). Formula: Ug = F × t / D_od, where D_od = source-to-object (front surface) distance. Rearranged: D_od(min) = F × t / Ug_max = 3 × 12.7 / 0.51 = 38.1 / 0.51 = **74.7 mm**, round up to **75 mm minimum**.

**Step 2 — resulting minimum source-to-film distance (SFD).** SFD = D_od + t = 75 + 12.7 = **87.7 mm**, round to **90 mm** to leave margin.

**Step 3 — decay-corrected source activity.** Source nominal activity was 100 Ci at last calibration, 45 days ago. Ir-192 half-life T½ = 73.8 days. Decay factor = (1/2)^(45/73.8) = (0.5)^0.6098 = 0.6554. Current activity A = 100 × 0.6554 = **65.5 Ci**.

**Step 4 — exposure time.** Using an Ir-192 characteristic-curve exposure factor K = 12 Ci·min/in² for 0.5 in steel with Class 1 film (a stated heuristic value from published Ir-192 exposure charts — verify against the source manufacturer's or lab's current chart before use), SFD in inches D = 90 mm / 25.4 = 3.54 in: t = K × D² / A = 12 × (3.54)² / 65.5 = 12 × 12.53 / 65.5 = 150.4 / 65.5 = **2.30 min** ≈ **2 min 18 sec**.

**Deliverable — RT technique sheet line item:** "Weld RT-33, Ir-192 @ 65.5 Ci (decay-corrected, cal. date + 45 days), SFD 90 mm, Ug calculated 0.43 mm (< 0.51 mm limit, meets Class 1), exposure time 2 min 18 sec, IQI: hole-type, 2-2T sensitivity required and achieved, film density measured 2.8 (within 1.8-4.0 range)."

## MT — field-strength verification (prod method and yoke lift test)

**Prod method current, per ASME Section V Article 7 / ASTM E709 guidance of 90-125 A per inch of prod spacing for material this thickness (commonly cited range — verify against the applicable code table for the specific material and thickness before use):**

Prod spacing = 150 mm (5.9 in). Required current range = 90-125 A/in × 5.9 in = **531-738 A**. Set and verify current at mid-range target = **635 A**, confirmed on the prod unit's ammeter before each exam segment.

**Field-strength check with a pie gauge / quantitative Hall-effect gaussmeter:** tangential field strength measured at the exam surface between prods = 38 Gauss, within the commonly-cited 30-60 Gauss acceptable range for wet-fluorescent continuous-method MT (stated heuristic — verify against ASTM E709/E1444 for the specific technique and material).

**Yoke lift-test verification (daily/per-shift equipment check):** AC electromagnetic yoke, pole spacing set to maximum rated spacing (100 mm / 4 in). Per ASME Section V Article 7 / ASTM E709, an AC yoke must lift a minimum of 10 lb (4.5 kg) at maximum pole spacing to be considered serviceable; a DC or permanent-magnet yoke must lift a minimum of 40 lb (18 kg) at maximum pole spacing. Worked check: 10 lb test weight lifted cleanly and held for 5 sec at 100 mm spacing → **yoke passes**, logged with date, yoke serial number, and technician initials before use on today's exams.

**Deliverable — MT technique sheet line item:** "Weld MT-19, prod method, 150 mm spacing, 635 A (within 531-738 A calculated range), wet fluorescent, black light intensity 1,250 µW/cm² at exam surface (>1,000 µW/cm² minimum), ambient visible light 18 lux (<20 lux maximum), yoke lift-test passed same shift."

## API 570 — corrosion rate, remaining life, and next inspection interval

**Given:** NPS 8 Schedule 40 carbon steel (A106 Gr. B) process pipe. Design pressure P = 285 psig, allowable stress S = 20,000 psi, E = 1.0 (seamless), W = 1.0, Y = 0.4 (ferritic steel, service temperature < 900°F), D_o = 8.625 in.

**Step 1 — pressure-design minimum thickness (ASME B31.3 eq. 304.1.2):** t = P × D_o / (2 × (S×E×W + P×Y)) = 285 × 8.625 / (2 × (20,000×1×1 + 285×0.4)) = 2,458.1 / (2 × 20,114) = 2,458.1 / 40,228 = **0.0611 in**. This is t_min — the retirement thickness API 570 compares field readings against, not the original nominal wall.

**Step 2 — UT thickness readings at this CML.** Pipe installed 15 years ago at nominal Schedule 40 wall = 0.322 in. Reading 5 years ago: t1 = 0.285 in. Reading today: t2 = 0.254 in.

**Step 3 — corrosion rates, both bases.** Short-term rate = (t1 − t2) / years = (0.285 − 0.254) / 5 = 0.031 / 5 = **0.0062 in/yr (6.2 mpy)**. Long-term rate (since new) = (t_nominal − t2) / total years = (0.322 − 0.254) / 15 = 0.068 / 15 = **0.00453 in/yr (4.5 mpy)**. Per the mental-model default, use the higher (short-term) rate absent a documented reason otherwise: governing rate = **6.2 mpy**.

**Step 4 — remaining life.** RL = (t_actual − t_min) / CR = (0.254 − 0.0611) / 0.0062 = 0.1929 / 0.0062 = **31.1 years**.

**Step 5 — next inspection interval.** API 570 sets the interval at the lesser of half the remaining life or the code's Class-based maximum (10 years for this piping class under a UT/on-stream inspection program). Half of RL = 31.1 / 2 = 15.6 years. Compare to the 10-year code cap: min(15.6, 10) = **10 years**.

**Deliverable — corrosion/interval memo excerpt:** "CML-114, NPS 8 Sch 40 A106 Gr. B. t_min (calc., B31.3 304.1.2) = 0.061 in. t_actual (today) = 0.254 in. Governing corrosion rate = 6.2 mpy (short-term, higher of two bases). Remaining life = 31.1 yr. Next UT inspection interval = 10 yr (code cap governs; half-RL of 15.6 yr exceeds it)."
