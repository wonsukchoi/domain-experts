# Playbook

Filled matrices, formulas, and workflows a health and safety engineer runs against. Verify site-specific matrix thresholds and the current-year regulatory text before citing — these are commonly applied patterns and named national standards, not a substitute for the governing site program or state-plan text in front of you.

## 1. Risk assessment matrix (4x4 severity x probability, ANSI/ASSP Z590.3-style)

| Severity ↓ / Probability → | 1 – Rare | 2 – Unlikely | 3 – Possible | 4 – Likely |
|---|---|---|---|---|
| **4 – Catastrophic** (fatality, permanent disability, PSM-scale release) | 4 | 8 | 12 | 16 |
| **3 – Critical** (lost-time injury, hospitalization) | 3 | 6 | 9 | 12 |
| **2 – Marginal** (recordable, no lost time) | 2 | 4 | 6 | 8 |
| **1 – Negligible** (first aid only) | 1 | 2 | 3 | 4 |

**Bands:** 1–3 acceptable (monitor) · 4–7 acceptable with periodic verification · 8–11 undesirable, engineering control required within a defined window · 12–16 unacceptable, stop-work until an engineering control drops the score below 12.

**Rule:** score before and after every control. A control that doesn't move the score across a band boundary hasn't done its job on paper, whatever it did in the field.

## 2. Machine guarding — point-of-operation safeguarding distance (OSHA 1910.217, Table O-10)

**Formula:** Ds = 63.5 x Ts

- Ds = minimum safety distance, inches, from the point of operation to the sensing field or barrier edge.
- 63.5 = hand-speed constant, inches/second (based on OSHA's assumed maximum hand-travel speed).
- Ts = press stopping time in seconds, measured at approximately the 90-degree point of the stroke, from a current field brake-monitor test — never a nameplate or rated value.

| Measured Ts (sec) | Ds (in) | Rounded install distance |
|---|---|---|
| 0.150 | 9.525 | 10 in |
| 0.250 | 15.875 | 16 in |
| 0.350 | 22.225 | 23 in |
| 0.500 | 31.750 | 32 in |

**Retest cadence:** 1910.217(e)(1)(ii) requires a brake-monitor check at the start of each operating shift (or continuous monitoring for presses so equipped) — a Ts drift of more than 10% from the baseline reading is a trigger to re-run the Ds calculation and confirm the installed distance is still sufficient, not just re-record the same number.

**Interlock category:** the Ds calculation sizes the *distance*; the *interlock circuit architecture* (single-channel unrated switch vs. dual-channel Category 3/4 safety circuit) is a separate requirement set by the risk assessment's required Performance Level (PLr, ISO 13849-1) or Safety Integrity Level. A catastrophic-severity point-of-operation hazard (matrix severity 4) requires at minimum a Category 3, PLd-rated circuit under ANSI B11.19 — a barrier at the correct distance wired through an unrated switch still fails the standard.

## 3. HAZOP node table (guide-word deviation analysis)

Run one row per guide word at each defined process node (a node = a section of the process with a defined design intent, e.g. "Reactor R-101 feed line, Node 3: cooling water supply").

| Guide word | Deviation | Possible cause | Consequence | Safeguard (existing) | Recommendation |
|---|---|---|---|---|---|
| No/None | No cooling water flow | Pump P-201 trip, valve closed in error | Reactor temperature excursion, potential runaway | Low-flow alarm (operator response) | Add low-flow interlock (SIS) to auto-trip feed on loss of cooling flow |
| More | High cooling water flow | Control valve fails open | Thermal shock to reactor jacket, seal stress | None identified | Add flow high-alarm; evaluate jacket thermal-shock rating |
| Less | Reduced cooling water flow | Partial strainer fouling | Slower but progressive temperature rise | Low-flow alarm | Add strainer differential-pressure alarm as leading indicator |
| Reverse | Reverse flow in cooling line | Check valve failure during pump swap | Contamination of cooling water supply from process side | Check valve (single) | Add second check valve or a spectacle blind for maintenance isolation |
| Other than | Wrong fluid supplied to jacket | Cross-connection during maintenance | Chemical incompatibility, potential reaction | Line labeling only | Add physical incompatible-connector fitting, not signage alone |

**Rule:** a node with no "no/none," "more," and "less" rows filled is an under-scoped node — those three guide words apply to nearly every flow, level, pressure, and temperature parameter and their absence from the table is itself a finding.

## 4. LOPA scenario worksheet (converting a PHA finding into a required control)

| Element | Example entry |
|---|---|
| Scenario | Loss of cooling water flow leads to reactor runaway and vessel overpressure |
| Consequence severity category | Category 4 (major — offsite impact possible) |
| Initiating event frequency | 0.1/yr (pump trip, generic industry data) |
| Independent Protection Layers (IPLs) credited | BPCS alarm + operator response (0.1 PFD) · relief valve (0.01 PFD) |
| Intermediate event likelihood | 0.1/yr x 0.1 x 0.01 = 1x10⁻⁴/yr |
| Target mitigated frequency (site risk tolerance criterion) | 1x10⁻⁵/yr for this consequence category |
| Gap | 1x10⁻⁴ vs. target 1x10⁻⁵ — one order of magnitude short |
| Additional IPL required | Safety Instrumented Function, SIL 1 (PFD ≤ 0.1) — closes the gap to 1x10⁻⁵/yr |

**Rule:** only *independent* layers count — the same sensor or the same human feeding two "layers" (an alarm and a shutdown both triggered off one transmitter) is one layer, not two, and crediting it twice is the most common LOPA scoring error.

## 5. PSM applicability check (29 CFR 1910.119)

1. Does the process hold any chemical on Appendix A above its listed threshold quantity (e.g., anhydrous ammonia 10,000 lb, chlorine 1,500 lb, hydrogen 5,000 lb), or a flammable liquid/gas above 10,000 lb aggregate at one location (excluding certain atmospheric storage and fuel-in-use exclusions)?
2. If yes — the process is PSM-covered: Process Safety Information, PHA (revalidated every 5 years per 1910.119(e)(6)), Operating Procedures, Training, Mechanical Integrity, Management of Change, Pre-Startup Safety Review, Incident Investigation, and Emergency Planning all apply.
3. Any Management of Change event (equipment substitution, setpoint change, procedure revision) that alters a parameter the PHA assumed requires a documented MOC review before startup — not a note for the next scheduled PHA.

## 6. OSHA recordable incident rate (29 CFR 1904.7)

**TRIR = (Number of OSHA-recordable cases x 200,000) / Total hours worked by all employees**

(200,000 = the base for 100 full-time-equivalent workers at 2,000 hours/year each.)

*Example: 2 recordable cases, 300,000 hours worked. TRIR = (2 x 200,000) / 300,000 = 400,000 / 300,000 = 1.33.*

**Rule:** TRIR is a plant- or company-wide aggregate. Use it to benchmark against BLS SOII NAICS-code averages for resource allocation across sites or programs — never as the deciding input for whether a specific open hazard needs an engineering control; that decision runs through the risk matrix (Section 1), keyed to the hazard's worst credible severity, not the aggregate rate.
