# Vocabulary

### Essential variable
A welding parameter that, if changed beyond a code-defined limit, requires the WPS to be requalified with a new PQR — process, base-metal P-number group, filler F-number, a preheat decrease, and adding or removing PWHT are the common ones.
**In use:** "Dropping preheat 30°F is an essential variable change under Section IX — that WPS doesn't cover this joint anymore until it's requalified."
**Common misuse:** Treating any parameter drift as a minor field adjustment; some variables (position, for instance) are non-essential for most properties, but preheat and process changes almost always are.

### Combined thickness
The sum of the thicknesses of the two members meeting at a joint, used (not the thinner or thicker member alone) to look up hydrogen-cracking preheat requirements.
**In use:** "Combined thickness here is 51 mm — that's the number that sets the preheat bracket, not the 19 mm nozzle wall by itself."
**Common misuse:** Using only the thinner or the governing-code-minimum member's thickness for the preheat lookup, understating the actual restraint and heat-sink effect of the joint.

### CE(IIW) vs Pcm
Two carbon-equivalent formulas predicting hydrogen-cracking susceptibility from chemistry: CE(IIW) = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15 fits higher-carbon structural steels; Pcm = C + Si/30 + (Mn+Cu+Cr)/20 + Ni/60 + Mo/15 + V/10 + 5B fits lower-carbon, higher-strength steels where CE(IIW) understates risk.
**In use:** "This is a 0.06%-carbon HSLA plate — run Pcm, not CE(IIW), or the preheat calc will come out too low."
**Common misuse:** Defaulting to CE(IIW) for every steel grade; on low-carbon, higher-alloy steels it systematically underpredicts cracking risk relative to Pcm.

### Diffusible hydrogen (H4/H8/H16)
The AWS A5.1/A5.5 classification of a filler metal's hydrogen content in deposited weld metal, in mL per 100 g of deposited metal, at increasing risk tiers.
**In use:** "Spec calls for H4 consumables on this joint — that means redried low-hydrogen rod, not whatever's already open on the rack."
**Common misuse:** Assuming any electrode marketed "low-hydrogen" delivers H4 regardless of storage and exposure; field-exposed, un-redried low-hydrogen rod commonly runs closer to H8.

### PWHT (Post-Weld Heat Treatment)
A controlled heating cycle after welding, held at a specified temperature and time, primarily to relieve residual stress and temper the HAZ — governed by thickness and P-number exemption curves (e.g., ASME Section VIII UCS-56).
**In use:** "This shell is over the UCS-56 exemption thickness — PWHT isn't optional here, and it has to stay under the plate's original temper temperature."
**Common misuse:** Treating PWHT as purely a stress-relief step with no effect on strength; on quenched-and-tempered steel it can re-temper and soften the base metal if run at or above the original temper temperature.

### MDMT (Minimum Design Metal Temperature)
The lowest metal temperature a pressure-retaining component is designed to experience in service, which sets whether and how demanding a Charpy impact test requirement applies.
**In use:** "MDMT on this vessel is -20°F — that's what drives the Charpy requirement on the PQR, not the ambient temperature the shop happens to sit at."
**Common misuse:** Confusing MDMT with ambient or operating temperature; it's a design-basis low-temperature exposure, often well below normal operating conditions, chosen to cover startup, upset, or auto-refrigeration cases.

### Charpy V-notch (CVN) impact test
A test striking a notched specimen to measure absorbed energy at a specified temperature, used as a toughness proxy that predicts resistance to brittle fracture.
**In use:** "PQR Charpy average is 22 ft-lb at -20°F against a 20 ft-lb minimum — passes, but with almost no margin."
**Common misuse:** Treating a passing Charpy average alone as sufficient; most codes also require no single specimen below a lower minimum, and a passing average can still mask one low outlier.

### Ferrite Number (FN)
A standardized measure of the ferrite content in austenitic stainless weld metal, predicted from composition via the WRC-1992 diagram and verified by ferritescope or point-count.
**In use:** "We're targeting 3 to 8 FN on this multipass 316L weld — enough ferrite to resist solidification cracking without hurting corrosion resistance."
**Common misuse:** Assuming the filler metal's certified nominal ferrite number carries through to the actual weld; base-metal dilution and actual cooling rate shift the as-deposited ferrite content from the filler's certified value.

### Lamellar tearing
A stepped, terrace-like crack running parallel to the plate surface in the base metal beneath a weld, driven by through-thickness tensile stress acting on planar non-metallic inclusions.
**In use:** "That's classic lamellar tearing under the flange, not a weld-metal defect — check the plate's through-thickness ductility, not the WPS."
**Common misuse:** Diagnosing a subsurface crack near a weld as a welding-process defect by default; a stepped fracture morphology in the base metal points at the plate's inclusion content and joint restraint, not the weld parameters.

### Dilution
The percentage of a weld's deposited metal that comes from melted base metal rather than filler metal, which shifts the weld's actual chemistry and properties away from the filler's certified values.
**In use:** "At 30% dilution off this high-carbon base metal, the weld-metal chemistry isn't what the filler cert alone would predict — that's why the PQR coupon gets tested, not just the filler."
**Common misuse:** Assuming deposited weld-metal properties equal the filler metal's certified properties; dilution from the base metal (often 15–40% depending on process and joint design) changes the actual as-welded chemistry.

### Procedure qualification thickness range (t/2t rule)
The code rule (e.g., ASME IX QW-451) setting how far a PQR's qualified thickness range extends above and below the actual coupon thickness welded and tested.
**In use:** "The coupon was 1 inch — under the t/2t rule that only qualifies this WPS from roughly 3/16 up to 2 inches, so it doesn't cover the 2.5-inch shell on the new job."
**Common misuse:** Assuming a PQR qualifies "any thickness" once tested; the qualified range is a defined multiple of the actual coupon thickness, and thicker or thinner joints outside that range need a separate qualification.

### Backing / root pass
A backing strip or the first weld pass in a joint, which establishes root-side soundness before subsequent passes are deposited over it.
**In use:** "Root pass on this pipe joint is GTAW for fusion control, then we switch to SMAW for the fill and cap — mixed-process WPS, qualified as one procedure."
**Common misuse:** Treating the root pass as just "the first pass of the same process"; it's frequently a deliberately different process chosen for fusion quality at the root, and that process combination is itself an essential variable of the qualified WPS.
