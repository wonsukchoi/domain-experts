# Playbook

Filled sizing templates a PV installer or design lead runs before ordering material and before finalizing an electrical one-line diagram. Every figure below follows common code sections and typical product classes — always verify the actual module/inverter/racking specs and the local AHJ's adopted code edition before finalizing a design.

## 1. String voltage vs. cold-weather Voc

Method: pull the site's NEC 690.7(A)(1) lowest-expected-ambient temperature (ASHRAE 2% extreme minimum design temp) first, then calculate the module's Voc at that temperature using its published temperature coefficient — not the module's STC (25°C) rating. The correction-factor table in 690.7(A)(2) is a fallback only when a manufacturer coefficient isn't available.

**Formula:** Voc(corrected) = Voc(STC) × [1 + (temp. coefficient %/°C) × (25°C − lowest expected ambient °C)]. String Voc = Voc(corrected) × modules per string. Max modules per string = inverter max input voltage ÷ Voc(corrected).

**Filled example — 400 W module, Voc(STC) 40.0 V, coefficient −0.29%/°C, inverter max 600 V:**

| Site low temp | ΔT from STC | Voc increase | Voc(corrected)/module | Max modules/string (600 V ÷ Voc) |
|---|---|---|---|---|
| 0°C | 25°C | 7.25% | 42.9 V | 13.98 → 13 |
| −10°C | 35°C | 10.15% | 44.1 V | 13.61 → 13 |
| −18°C | 43°C | 12.47% | 45.0 V | 13.33 → 13 |
| −30°C | 55°C | 15.95% | 46.4 V | 12.93 → 12 |

**Takeaway:** the max-string-length number tightens as the site's design low gets colder — a string count validated for a mild climate can be over-length for a cold-climate site using the identical hardware. Always run the calculation against the specific site's design low, not a rule-of-thumb module count carried from a warmer job.

## 2. Rapid shutdown (NEC 690.12) compliance check

Method: verify two zones separately — outside the array boundary (conductors more than 1 ft from the array or entering the building) must reach ≤30 V/240 VA within 30 seconds of initiation; inside the array boundary, current code requires the same 30 V/30-second limit at the module or sub-array level, not just at the array's single combined output.

**Compliance paths, in order of simplicity:**

1. **Module-level power electronics (MLPE)** — power optimizers or microinverters, each independently listed for rapid shutdown, satisfy both zones inherently because each module's output is already limited at the module.
2. **Listed array-boundary RSD system** (transmitter at the disconnect, receiver/relay at or near each module or sub-combiner) — satisfies both zones without MLPE, at the cost of an added control circuit to install and maintain.
3. **String inverter with a single central combiner-level RSD device only** — satisfies the outside-array-boundary requirement but **not** the inside-array-boundary requirement; not code-compliant as a standalone solution under current NEC on its own.

**Verification at commissioning:** initiate rapid shutdown at the installed switch, then measure voltage at a point within 1 ft of the array and at a point between two modules inside the array — both must read ≤30 V within 30 seconds. Log the elapsed time and voltage reading for the commissioning record; a device that "usually" trips fast isn't verified until it's timed on this specific installation.

## 3. NEC 705.12(B)(3)(c) — 120% interconnection rule

Method: two separate numbers matter — the breaker size the inverter's actual output requires (NEC 690.8(A), 125% of continuous output current), and the busbar ceiling the panel allows (705.12(B)(3)(c)). Size to the smaller constraint that still clears both, and check headroom left for future additions.

**Formulas:**
- Minimum inverter-output OCPD = inverter continuous AC output current × 1.25.
- Maximum allowable backfed breaker (opposite-end busbar tap) = (1.2 × busbar rating) − main breaker rating.

**Filled example — 200 A busbar, 200 A main breaker, three inverter sizes:**

| Inverter continuous output | Min. OCPD (×1.25) | Busbar ceiling (120% rule) | Fits? | Headroom left on busbar |
|---|---|---|---|---|
| 24 A | 30 A | 40 A | Yes | 10 A (40 − 30) |
| 32 A | 40 A | 40 A | Yes, at the ceiling | 0 A |
| 42 A | 52.5 A → 60 A std. breaker | 40 A | **No** | N/A — exceeds ceiling |

**When the inverter output exceeds the busbar ceiling:** options in preference order — (1) relocate the main breaker to the opposite end of the busbar from the PV breaker if the panel and code edition support it (changes the formula basis), (2) upsize the panel/busbar, (3) use a supply-side (ahead-of-the-main) connection instead of a load-side breaker tap, which isn't subject to the 120% busbar rule at all but requires its own disconnect and metering coordination with the utility.

## 4. Roof attachment and flashing sequence (asphalt shingle)

Method: attachment integrates into the shingle's water-shedding order — never caulked on top of finished shingles as a standalone seal.

**Sequence:**
1. Locate rafter/truss with the framing member, not just the roof deck — attachment must land in structural framing, not decking alone.
2. Drill pilot hole sized to the lag/flashing manufacturer's spec; set minimum embedment (commonly 3 in into the rafter, verify against the specific product's engineering letter for the actual rafter species).
3. Remove the shingle course covering the penetration point; install the racking manufacturer's flashing under the course above and over the course still-in-place below — the same shingle-lap order the roofing trade uses for any other roof penetration (vent stack, skylight curb).
4. Torque the lag to the racking manufacturer's spec (commonly in the 20–25 ft-lb range for common lag sizes — verify against the actual product).
5. Reinstall the disturbed shingle course over the flashing; sealant goes at the flashing's edge as a secondary defense, not as the primary seal.
6. Photograph the penetration before and after the shingle course is reinstalled — the single most useful record when a leak-liability question surfaces later.

**Attachment spacing:** driven by the racking manufacturer's per-attachment pull-out rating (commonly several hundred lbf, verify against the specific fastener/rafter-species combination) checked against the site's wind and snow load, not a flat "every 4 ft" habit — a longer rail on a high-wind-zone roof needs more attachment points per linear foot than the same rail on a sheltered low-wind site.

## 5. Fire-code pathway and setback layout

Method: pull the jurisdiction's adopted fire code edition first — pathway width and small-roof exceptions differ across IFC editions and local amendments.

**Common baseline (2018+ IFC-derived, verify local adoption):**

- 3 ft clear pathway from eave to ridge along each side of a roof hip or valley.
- 3 ft setback below the ridge, both sides.
- Smoke-ventilation pathway at the ridge, sized per the adopted code (commonly 3 ft, verify locally).
- Small residential roofs below the jurisdiction's plan-view area threshold may qualify for a reduced-pathway or no-pathway exception — confirm the specific threshold and don't assume it applies.

**Layout order:** mark hips, valleys, and the ridge on the roof plan before placing any module — pathway and setback lines constrain usable array area, and laying modules out first invites a costly re-layout once the pathway requirement is applied.
