# Red flags

Smell tests a materials engineer catches on a first pass over a material certification, a fracture surface, or a fatigue/failure calculation.

### Fatigue factor of safety calculated against Sy or Sut instead of a corrected Se

- **Usually means:** the analyst ran a static strength check and reported it as if it answered a cyclic-loading question — a common substitution when the part "looks" statically safe.
- **First question:** is the load cyclic, and if so, what is the Marin-corrected endurance limit (or finite-life S-N value) the alternating stress should be checked against?
- **Data to pull:** the load history or duty cycle, the original stress calculation, and the material's S-N or endurance-limit data with surface/size/reliability corrections applied.

### Handbook endurance limit used with no surface, size, or reliability correction applied

- **Usually means:** the Se' figure (0.5*Sut or the 700 MPa steel cap) was taken as the design allowable directly, without the Marin ka/kb/kc/kd/ke reduction — this commonly overstates real capacity by 30-50%.
- **First question:** what surface finish, section size, and reliability level were assumed, and were the corresponding Marin factors actually applied?
- **Data to pull:** the fatigue calculation sheet, part surface finish spec, and section dimension at the checked location.

### Fracture surface described as "fatigue" with no beach marks, striations, or ratchet marks documented

- **Usually means:** the failure mode was assumed from context (cyclic application) rather than confirmed from the fracture surface itself, which can misdirect the entire root-cause chain toward the wrong fix.
- **First question:** has the fracture surface been examined under SEM, and what specific features (beach marks, striations, cleavage facets, dimples) were actually observed at the origin?
- **Data to pull:** fractography photos/SEM images, origin location, and a description of the propagation-zone morphology.

### As-built fillet or hole radius not verified against the drawing tolerance after a fatigue failure

- **Usually means:** the design calculation assumed the drawing's nominal radius, but the fatigue notch factor Kf is highly sensitive to the *actual* radius, and a machining deviation can shift Kf by 20-30% unnoticed.
- **First question:** what is the measured radius at the failure origin, and how does the recalculated Kt/Kf compare to the value the original design calculation used?
- **Data to pull:** dimensional inspection of the failed part at the origin, original drawing tolerance, and the design calculation's assumed Kt/Kf.

### Material chemistry certification passes on every element but sits at the extreme edge of the specified range

- **Usually means:** the heat is technically compliant but the property that actually governs the failure mode (hardenability from carbon/alloy content, or toughness from a tramp element) is pushed toward the unfavorable end of what the spec allows.
- **First question:** which specific element's position in the range correlates with the failure mode observed, and does the Jominy or Charpy data for this specific heat reflect that?
- **Data to pull:** mill certification (full chemistry), heat/lot number, and any heat-specific mechanical test data beyond the minimum cert requirement.

### Surface hardness passes spec but no hardenability (Jominy/H-band) requirement exists for a section over roughly 15-20 mm

- **Usually means:** the spec checked a point property (surface hardness) that doesn't guarantee the part actually through-hardens, and a soft, low-toughness core can exist under a passing surface reading.
- **First question:** has core hardness been verified by sectioning, or only surface hardness by Rockwell/Brinell at an accessible face?
- **Data to pull:** heat-treat cert, Jominy or H-band specification (if any), and a sectioned hardness traverse if one exists.

### Ductile-to-brittle transition temperature not checked against the component's actual minimum service temperature

- **Usually means:** a Charpy impact spec was satisfied at room temperature (or the standard test temperature) without confirming the DBTT sits below the coldest temperature the part will actually see in service or during a cold-weather startup.
- **First question:** what is the material's measured or specified DBTT, and what is the lowest temperature (including transient/startup conditions) the part experiences?
- **Data to pull:** Charpy V-notch test data across a temperature range, service temperature history or design minimum, and the applicable code's required test temperature (e.g., ASME Section VIII impact test exemption curves).

### Computed applied stress intensity K exceeds roughly 0.5-0.6 x KIC for a detected crack-like indication

- **Usually means:** the flaw is close enough to the material's fracture toughness that continued service without a fitness-for-service assessment or immediate repair carries meaningfully reduced margin against unstable fracture.
- **First question:** has a formal fitness-for-service calculation (API 579-1/ASME FFS-1) been run for this specific flaw size, geometry, and applied stress, or is the part still being evaluated by inspection judgment alone?
- **Data to pull:** NDI report (flaw size, location, orientation), material KIC data at service temperature, and applied stress at the flaw location.

### Field failures cluster on a specific heat/lot number rather than being distributed across the population

- **Usually means:** the root cause is material or process (a specific heat's chemistry, a specific furnace run's quench) rather than a systemic design issue affecting every unit equally.
- **First question:** do the failed parts share a heat number, supplier, or production date range that the surviving population doesn't?
- **Data to pull:** failure log with heat/lot numbers, mill certs for the implicated heats, and a population-wide lot distribution for comparison.

### Actual field cycles-to-failure is under roughly 10% of the S-N-predicted life at the calculated applied stress

- **Usually means:** either the applied stress used in the prediction understated the real stress (missed stress concentration, misjudged mean stress, or an unaccounted vibration mode), or an environmental factor (corrosion fatigue, elevated temperature) is degrading fatigue life beyond what the base S-N curve accounts for.
- **First question:** does the applied-stress calculation include every stress riser and the actual measured mean stress, and is the part exposed to a corrosive or elevated-temperature environment the S-N data doesn't cover?
- **Data to pull:** the stress calculation with all concentration factors shown, measured field stress data if available, and service environment records (temperature, exposure to process fluid or humidity).

### Weld or heat-affected-zone hardness exceeds the applicable sour-service or hydrogen-cracking limit (e.g., 22 HRC per NACE MR0175/ISO 15156 for sour service)

- **Usually means:** the welding procedure's heat input or post-weld heat treatment wasn't controlled tightly enough to keep the HAZ hardness under the limit that governs hydrogen-induced cracking susceptibility in that service.
- **First question:** what HAZ hardness was actually measured, at what location relative to the fusion line, and does the welding procedure specification include a post-weld heat treatment or hardness-verification step?
- **Data to pull:** weld procedure specification (WPS), post-weld hardness survey, and the governing service-specific hardness limit (NACE MR0175, or the applicable code).

### Retained austenite reported on a quenched high-carbon or high-alloy part with no dimensional-stability or cracking check

- **Usually means:** the as-quenched microstructure retains untransformed austenite that can transform later (in service, or over time at room temperature), causing dimensional growth or delayed cracking that a hardness reading alone won't reveal.
- **First question:** what retained austenite percentage was measured, and does the heat-treat procedure include a cryogenic or extended temper cycle to address it?
- **Data to pull:** metallurgical report (retained austenite %, typically by XRD), heat-treat procedure (temper cycles), and any dimensional-stability or delayed-cracking history for this part family.
