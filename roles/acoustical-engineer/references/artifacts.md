# Artifacts

## RT60 calculation worksheet — Sabine vs. Eyring (filled example)

Room: 300-seat multipurpose room, unoccupied shell condition being checked against occupied design target.

Volume: 24 ft × 45 ft × 14 ft = **15,120 ft³**.

**Step 1 — surface inventory and absorption coefficients (500 Hz, Sabins):**

| Surface | Area (ft²) | Material | α (500 Hz) | Sabins (A × α) |
|---|---|---|---|---|
| Floor | 1,080 | Carpet on pad | 0.14 | 151.2 |
| Ceiling | 1,080 | Acoustic tile, 15/16" suspension | 0.76 | 820.8 |
| Walls (4) | 1,932 | Painted gypsum board | 0.06 | 115.9 |
| Seating (unoccupied, 300 fixed) | — | Upholstered, unoccupied | 1.5 sabins/seat | 450.0 |
| Glazing | 180 | Laminated glass | 0.04 | 7.2 |
| **Total Σ(A·α)** | | | | **1,545.1** |

**Step 2 — average absorption coefficient:**
α̅ = ΣA·α / ΣA = 1,545.1 / 4,272 = **0.362**

**Step 3 — formula selection.** α̅ = 0.362 exceeds the ~0.2–0.3 threshold where Sabine's error range (up to ~28%) becomes unacceptable → **switch to Eyring.**

**Step 4a — Sabine (for comparison only, not the spec basis):**
RT60 = 0.049 · V / Σ(A·α) [imperial] = 0.049 × 15,120 / 1,545.1 = **0.48 s**

**Step 4b — Eyring (governing calculation):**
RT60 = 0.049 · V / [−S · ln(1−α̅)]
−ln(1 − 0.362) = 0.4494
S = 4,272 ft²
RT60 = 0.049 × 15,120 / (4,272 × 0.4494) = 740.9 / 1,920.2 = **0.386 s**

**Step 5 — compare to target.** Design brief specifies RT60 0.6–0.8 s at 500 Hz for a multipurpose room used for both speech and light amplified music. Calculated 0.386 s (unoccupied, worse case is occupied — occupancy adds absorption and lowers RT60 further) is **under target, not over** — the room will read acoustically dead, not live. Flag: remove or reduce ceiling tile coverage (α 0.76 is doing 53% of total absorption) rather than adding treatment.

## STC/IIC assembly comparison table (filled example)

Wall type: corridor-to-classroom partition, ANSI/ASA S12.60 target **STC 50 minimum** (core learning space adjacency).

| Assembly | Lab STC (ASTM E90) | Field-margin deduction | Projected field STC | Meets STC 50 as-built? |
|---|---|---|---|---|
| Single 5/8" gyp each side, 2×4 wood stud @ 16" o.c., unfilled cavity | 34 | −7 (typical wood-stud, no isolation) | 27 | No |
| Same, cavity filled R-11 batt | 39 | −7 | 32 | No |
| Double 5/8" gyp each side, metal stud @ 24" o.c., R-13 batt | 52 | −6 (metal stud, less rigid coupling) | 46 | No |
| Double 5/8" gyp each side, staggered stud, R-13 batt, resilient channel one side | 58 | −6 | 52 | **Yes — 2 pt margin** |
| Double 5/8" gyp each side, staggered stud, R-13 batt, RC one side, sealed penetrations | 58 | −5 (sealed penetrations reduce flanking) | 53 | **Yes — 3 pt margin, spec basis** |

Rule applied: reject any assembly whose lab-minus-margin result lands at or below the target — a 0-point margin (e.g., lab 55, margin −5, projected 50 against a 50 target) still fails, since the margin figure is itself a typical-case average, not a guarantee.

## NC-curve band-by-band worksheet (filled example)

Space: operating room, mechanical background noise from AHU-managed supply/return. Target: **NC 30** (ASHRAE OR guidance, upper bound of the 25–30 range for this room type).

| Octave band (Hz) | 63 | 125 | 250 | 500 | 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|---|---|---|---|
| NC-30 curve limit (dB) | 57 | 48 | 41 | 35 | 31 | 29 | 28 | 27 |
| Measured/calculated SPL (dB) | 52 | 44 | 40 | 34 | 26 | 22 | 18 | 14 |
| Margin to curve (dB) | +5 | +4 | +1 | +1 | +5 | +7 | +10 | +13 |

**Reading the table:** the room passes NC 30 (every band is at or under the curve), but the 250 Hz and 500 Hz bands carry only 1 dB of margin each — those are the AHU's dominant tonal bands, and a single band exceeding the curve by any amount fails the space regardless of how far under curve every other band sits. **Governing rule:** NC rating = the highest curve that no single band exceeds, never an average across bands.

**Decision:** resize the 250/500 Hz silencer elements to buy back 3 dB in each band (target: calculated NC 27–28 with ≥4 dB margin per band), so field-installed performance has room to underperform calculated values and still clear NC 30 as-built.

## OSHA/NIOSH exposure comparison (filled example)

Measured equipment noise at operator station: **97 dBA**, 8-hour shift, continuous.

| Standard | Exchange rate | Allowed duration at 97 dBA | Dose at 8 hr exposure |
|---|---|---|---|
| OSHA PEL (29 CFR 1910.95) | 5 dB | 3 hr 2 min | 264% of 8-hr allowable → engineering/admin controls or HPD required |
| NIOSH REL | 3 dB | 30 min | 1,600% of 8-hr allowable → same trigger, far larger excess |

**Step — TWA dose calc (OSHA method):** allowed time T = 8 / 2^[(L−90)/5] = 8 / 2^[(97−90)/5] = 8 / 2^1.4 = 8 / 2.639 = **3.03 hr**. An 8-hour shift at 97 dBA is 264% of the OSHA-allowable dose — mandatory hearing conservation program enrollment, not merely "recommended."

**Step — TWA dose calc (NIOSH method):** allowed time T = 8 / 2^[(L−85)/3] = 8 / 2^[(97−85)/3] = 8 / 2^4 = 8 / 16 = **0.5 hr (30 min)**. Dose = 8 hr / 0.5 hr = **1,600%** of the NIOSH-allowable dose — over 6x further past its own criterion than the OSHA number.

**Recommendation order (fallback positions, in preference):**
1. Engineering control at source (enclosure, silencer, isolation mounts) — targets the 97 dBA reading itself.
2. Administrative control (job rotation to cap individual exposure time below 3 hr at this station).
3. Hearing protection device (HPD) as the last resort, sized to bring effective exposure under both OSHA and NIOSH — a single-number NRR spec isn't sufficient; verify against the measured octave-band spectrum, since HPD attenuation is frequency-dependent and a broadband-rated device can under-protect at the equipment's dominant band.
