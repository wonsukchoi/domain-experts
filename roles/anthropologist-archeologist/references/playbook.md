# Playbook

Filled formulas, thresholds, and workflows a CRM archaeologist runs against. Shovel-test intervals, site-definition thresholds, and precision figures vary by state SHPO — these reflect a commonly applied pattern and named national standards, not a substitute for the governing SHPO's current published guidance.

## 1. Section 106 process (36 CFR Part 800)

| Step | Regulation | What happens |
|---|---|---|
| 1. Initiation | § 800.3 | Lead federal agency determines the undertaking has potential to affect historic properties; identifies consulting parties (SHPO/THPO, Tribes, local governments). |
| 2. Identification | § 800.4 | Define the APE; conduct background research and field survey (Phase I) to identify historic properties within it. |
| 3. Assessment of effects | § 800.5 | Apply the adverse-effect criteria (§ 800.5(a)(1)): does the undertaking alter, directly or indirectly, any characteristic that qualifies a property for the National Register? |
| 4. Resolution | § 800.6 | If adverse effect: negotiate a Memorandum of Agreement (MOA) — commonly avoidance-by-redesign, or Phase II/III data recovery as mitigation. SHPO/THPO gets a standard 30-day review period at each formal submission. |

**Rule:** Section 106 requires the agency to *consider* effects and resolve them — an MOA that authorizes destroying an eligible site via data recovery is a valid, common outcome, not a failure of the process.

## 2. Survey phases

| Phase | Purpose | Typical method | Deliverable |
|---|---|---|---|
| I — Identification | Find and record historic properties in the APE | Pedestrian survey (visibility-dependent) + systematic shovel testing | Phase I report; "no historic properties affected" or site(s) recommended potentially eligible |
| II — Evaluation | Determine NRHP eligibility of an identified site | Larger excavation units (1×1m or 1×2m), targeted at site core and margins; may include remote sensing (GPR, magnetometry) | Eligibility recommendation to SHPO (eligible / not eligible / potentially eligible pending more work) |
| III — Data recovery | Mitigate an unavoidable adverse effect on an eligible site | Full or substantial-sample excavation per an approved research design/data recovery plan | Final report; collection curated per 36 CFR Part 79 |

**Rule:** only Phase II or III testing, not Phase I shovel-test data, can support a firm eligibility determination — a Phase I report should read "potentially eligible, Phase II recommended," not a bare "eligible."

## 3. Shovel test pit (STP) protocol

- **Dimensions:** commonly 30–35cm diameter (or 50×50cm square), hand-excavated in 10cm arbitrary levels within the plow zone/Ap horizon, then by natural stratigraphic level into subsoil, terminating at sterile subsoil or a specified minimum depth (commonly 50–80cm) unless bedrock or the water table intervenes sooner.
- **Screening:** all fill passed through 1/4" (6.4mm) hardware cloth; finer mesh (1/8") used where the research question targets small debitage or micro-fauna.
- **Primary grid interval:** commonly 15m (≈50 ft) on systematic transects, per many state SHPO Phase I standards; tightened where background research flags high probability (e.g., 7.5m near a spring, terrace edge, or previously recorded site boundary).
- **Delineation interval:** halve the primary interval (e.g., 15m → 7.5m) around any positive STP, testing outward until bounded by two consecutive negative STPs in each cardinal direction, or a natural boundary (slope break, wetland, water) is reached first.
- **Site-definition threshold (commonly applied pattern):** three or more artifacts recovered within roughly 30m of each other constitutes a site; fewer, with no associated feature, is recorded as an isolated find requiring no further delineation.

*Example — STP count on a rectangular parcel:* 42 acres = 42 × 4,046.86 m²/acre = 169,968 m². At a 15m × 15m grid (225 m² per STP): 169,968 / 225 ≈ 755 STPs.

**Rule:** verify grid interval, STP dimensions, and the site-definition threshold against the governing SHPO's current published Phase I standard before scoping a survey — the figures above are a commonly cited national pattern, not a fixed national rule.

## 4. NRHP eligibility (36 CFR 60.4, National Register Bulletin 15)

**Criteria (a property is eligible if it meets one or more, and retains integrity):**

| Criterion | Basis |
|---|---|
| A | Association with events significant in broad patterns of history |
| B | Association with the lives of significant persons |
| C | Distinctive characteristics of type, period, method of construction, or high artistic value |
| D | Has yielded, or is likely to yield, information important in prehistory or history |

**Seven aspects of integrity** (a property must retain enough of these to convey its significance): location, design, setting, materials, workmanship, feeling, association. For most archaeological sites evaluated under Criterion D, **location and the survival of intact, interpretable subsurface deposits carry the most weight** — a plowed-over surface can still convey integrity if buried features/strata below the plow zone survive.

**Criteria Considerations (A-G, exceptions requiring extra justification):** cemeteries/graves, religious properties, moved properties, birthplaces, reconstructed properties, commemorative properties, and properties less than 50 years old.

*Example — Criterion D eligibility narrative:* "Site 44XX-1234's surface has been disturbed by agricultural plowing to approximately 20cm. However, STP N487E521 exposed an oxidized, charcoal-flecked soil lens at 30–40cm below surface, in apparently undisturbed subsoil context. Because the feature and any associated buried activity surface postdate plowing depth, the site retains sufficient integrity of location and materials to convey information potential under Criterion D, pending confirmation via Phase II excavation."

**Rule:** evaluate the surviving component, not the most disturbed stratum — a disturbed plow zone over an intact buried feature is a common, not disqualifying, condition.

## 5. Harris matrix (relative stratigraphic sequence)

Each excavated context gets a stratigraphic unit (SU) number; the matrix records only direct superposition (what a context sits directly above or below, or what interface cuts what), never inferred age.

*Example — a small excavation unit sequence:*

```
SU 100 (modern topsoil)
   |
SU 101 (plow zone, Ap horizon)
   |
SU 102 (cut — pit feature outline, cuts SU 103)
   |
SU 104 (pit fill, charcoal-rich — dated sample submitted from here)
   |
SU 103 (subsoil, culturally sterile B horizon — pit was dug into this)
```

Reading order: SU 100 is latest (topmost); SU 104 (pit fill) is later than SU 103 (the sterile subsoil the pit was cut into) by the law of superposition, but the matrix alone says nothing about *how much* later — SU 104's charcoal sample is what supplies the absolute date.

**Rule:** a Harris matrix answers "which context is earlier/later," never "how old" — absolute dates attach to specific SUs from independent evidence (radiocarbon, diagnostics), not from position in the diagram.

## 6. Radiocarbon dating and calibration

- **Conventional radiocarbon age (RCYBP)** is reported by the lab with a 1-sigma lab error, already corrected for isotopic fractionation using the sample's measured δ13C value (conventionally normalized to −25‰ for wood charcoal).
- **Calibration** converts the conventional age to calendar years by mapping it against the IntCal20 (Northern Hemisphere terrestrial) curve using software such as OxCal or CALIB; report the **2-sigma (95.4% probability) calendar-year range**, not the uncalibrated lab date, in any eligibility or interpretive narrative.
- Calibration curve plateaus can produce a **multimodal** probability distribution (more than one disconnected calendar-year range) — report the full range and each sub-range's probability, not a single midpoint date.

*Example (illustrative lab result format):* Lab no. Beta-987654, charcoal from SU 104, conventional radiocarbon age 3,120 ± 30 BP (δ13C = −24.8‰). Calibrated (IntCal20, 2-sigma): cal 1495–1320 BC (91.2% probability) and cal 1310–1290 BC (4.2% probability) — reported as the full range with probabilities, not collapsed to a single "1400 BC."

**Rule:** never report a calibrated date as a single point estimate when the calibration output is a range or is multimodal — the range is the finding, not a rounding inconvenience.

## 7. Artifact density and distribution analysis

**Density (artifacts/m³) = artifact count / excavated volume.** STP volume (cylindrical) = π × r² × depth, where r is half the diameter.

*Example:* STP N485E520, 35cm diameter (r = 0.175m), excavated to 40cm: volume = π × 0.175² × 0.40 ≈ 0.0385 m³. 42 artifacts recovered → density ≈ 1,092 artifacts/m³.

**Rule:** always compute a background/off-site density from negative or low-yield testing elsewhere on the same grid before characterizing a high count as a discrete activity locus — a raw artifact count without a density comparison can't distinguish a hot spot from ordinary sheet scatter spread across a larger area.
