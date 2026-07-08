# Playbook

Filled worksheets for the four calculations that recur on every PV design: cold-temperature string sizing, source-circuit ampacity, DC/AC ratio comparison, and the performance-ratio yield build-up. Numbers below are the worked-example array (108 x 400 W modules, Denver, CO) unless a row states otherwise — treat structures and formulas as reusable, plug in project-specific inputs.

## 1. NEC 690.7 cold-temperature string-sizing worksheet

Formula: `Voc_corrected = Voc_STC x [1 + (T_low - 25) x (TempCo_Voc / 100)]`, where `T_low` is the site's ASHRAE 99% extreme minimum design dry-bulb temperature (°C) and `TempCo_Voc` is the module's Voc temperature coefficient (%/°C, negative).

| Input | Value |
|---|---|
| Module Voc (STC) | 49.5 V |
| Voc temp. coefficient | -0.27 %/°C |
| Site design low temp (ASHRAE 99% extreme min, verify per project) | -18°C |
| Delta-T from STC (25°C) | -43°C |
| Voc_corrected per module | 49.5 x [1 + (-43 x -0.0027)] = **55.25 V** |
| Inverter max DC input voltage | 1,000 V |
| Max modules/string = floor(1,000 / 55.25) | **18 modules** |
| Check: 18 x 55.25 | 994.5 V (5.5 V margin) |

Hot-side MPPT check (confirms the string still sits inside the inverter's MPPT window at maximum expected cell temperature — a string sized correctly for cold can still fail on this check for a long string on a low-MPPT-minimum inverter):

| Input | Value |
|---|---|
| Module Vmp (STC) | 41.3 V |
| Vmp temp. coefficient | -0.29 %/°C |
| Expected max cell temp (NOCT-based: Tamb_max + (NOCT-20)) | 60°C |
| Delta-T from STC | 35°C |
| Vmp_hot per module | 41.3 x [1 + (35 x -0.0029)] = **37.11 V** |
| String Vmp_hot (18 modules) | 668.0 V |
| Inverter MPPT window | 250-950 V |
| Result | Pass — 668.0 V inside window |

**Fallback if manufacturer temperature coefficients are unavailable:** use NEC 690.7(A)(2)'s Table 690.7(A) ambient-temperature-adjustment-factor method (crystalline/multicrystalline silicon default correction factors by low-temperature bin) instead of the manufacturer's-coefficient method — never assume STC Voc is safe without applying one of the two.

## 2. NEC 690.8/690.9 conductor and OCPD worksheet

Formula: required conductor ampacity = `Isc_STC x 1.25 (690.8(A) irradiance factor) x 1.25 (690.8(B) continuous-duty factor)` = `Isc_STC x 1.5625`.

| Input | Value |
|---|---|
| Module Isc (STC) | 10.30 A |
| Max PV circuit current (690.8(A)): 10.30 x 1.25 | 12.875 A |
| Required conductor ampacity (690.8(B)): 12.875 x 1.25 | **16.09 A** |
| Combined check: 10.30 x 1.5625 | 16.09 A (matches) |
| Conductor selected | 10 AWG PV wire, 40 A rated (90°C, before derating) |
| Conduit-fill / ambient derating applied? | Confirm per NEC 310.15 before final selection — not shown |
| OCPD (fuse/breaker) sizing (690.9) | Rated no less than 690.8(B) ampacity, not to exceed conductor and connector rating; series fuse required when more than 2 parallel strings combine into a single OCPD-protected conductor |

**Fallback preference order when the calculated ampacity lands between standard conductor sizes:** (1) round up to the next standard AWG size, never down; (2) if conduit fill forces a smaller conductor, split into additional parallel circuits rather than undersizing; (3) re-run the OCPD rating any time the conductor size changes — they're sized off each other, not independently.

## 3. DC/AC ratio comparison worksheet

| Candidate | DC (kWdc) | AC (kWac) | DC/AC ratio | Est. annual clipping loss (8760 sim) | Est. annual AC yield |
|---|---|---|---|---|---|
| A — 1:1 sizing | 34.5 | 34.5 | 1.00 | ~0.1% | 62,900 kWh/yr |
| B — chosen design | 43.2 | 34.5 | 1.25 | 1.6% | 78,412 kWh/yr |
| C — aggressive oversizing | 48.3 | 34.5 | 1.40 | 4.8% | 82,100 kWh/yr |

Reading the table: B adds 25% more DC capacity than A for roughly 25% more annual yield (clipping loss still small at this ratio) — a strong marginal trade. C adds another 12% DC capacity over B for only about 5% more yield, because clipping loss nearly triples — the marginal capacity in C is a weak trade unless module pricing has dropped enough to justify it independently. **Fallback position in preference order:** (1) run the 8760 simulation per candidate rather than an annual-average clipping heuristic; (2) if simulation tooling isn't available for a screening pass, use 1.2-1.3 as the default band and flag the estimate as unverified; (3) never exceed any contractual export/curtailment cap regardless of what the ratio comparison favors.

## 4. Performance-ratio loss-stack worksheet

Formula: `Annual AC yield = Reference yield (h) x Pdc,STC (kWdc) x PR`, where `PR = product of all loss factors below` and `Reference yield = POA irradiance (kWh/m²/yr) / 1 kW/m²`.

| Loss factor | Typical range | This project | Basis |
|---|---|---|---|
| Temperature | 3-9% loss (0.97-0.91) | 0.9595 | Pmax temp. coeff. x (Tcell_avg-operating - 25°C) |
| Soiling | 1-5% loss | 0.98 | Climate-dependent; arid sites at the low end without frequent rain |
| Shading | 0-10%+ loss | 0.99 | Site survey / shading analysis (SunEye, Helioscope 3D model) |
| Mismatch + first-year LID | 2-3% loss | 0.98 | Manufacturer LID spec + module mismatch |
| DC wiring | 1-3% loss | 0.985 | Source/output circuit voltage drop, target under 2% at STC current |
| Inverter conversion + clipping | 2-6% loss | 0.9653 | CEC weighted efficiency x (1 - clipping loss from worksheet 3) |
| AC wiring/transformer | 1-2% loss | 0.99 | Interconnection run length and conductor size |
| Availability | 1-3% loss | 0.99 | O&M-stated heuristic; verify against the specific O&M contract's SLA |
| **Cumulative PR** | **0.75-0.85 typical** | **0.8502** | Product of all rows above |

**Reconciliation step (required, not optional):** compare the resulting annual AC yield against the inverter's theoretical ceiling (`AC nameplate kW x 8,760 h`) — if the modeled yield exceeds, say, 40-50% of that ceiling for a fixed-tilt array outside a very high-irradiance desert site, re-check the loss stack before shipping the number; a PR-based estimate that's internally inconsistent with the inverter's own capacity is a red flag on the model, not a reason to trust the higher number.
