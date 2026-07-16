# Red flags

### CE(IIW) or Pcm above 0.40 with no preheat specified on the WPS
- **Usually means:** the WPS was copied from a similar job without recalculating hydrogen-cracking risk for this specific chemistry and thickness.
- **First question:** what CE or Pcm did the mill cert actually calculate to, and what combined thickness governs this joint?
- **Data to pull:** the material certification (full chemistry) and the joint's combined-thickness drawing dimension.

### Crack discovered 24–72 hours after welding, not at weld-day inspection
- **Usually means:** hydrogen-induced delayed cracking, not a fit-up or fusion defect (which shows at weld-day inspection).
- **First question:** was preheat and interpass temperature actually verified and logged for this joint, or assumed from the WPS default?
- **Data to pull:** the preheat/interpass log (if one exists) and the crack's location relative to the fusion line (HAZ vs weld-metal centerline).

### HAZ hardness survey reads above the service's hardness limit (e.g., 248 HV for NACE MR0175 sour service)
- **Usually means:** cooling rate was faster than the WPS's qualification anticipated, or the base metal's actual hardenability exceeds the PQR coupon's.
- **First question:** what heat input and preheat were actually run versus what the qualified WPS specifies?
- **Data to pull:** the hardness survey report with specimen location, and the as-run welding parameter log.

### PWHT hold temperature at or above the base metal's original tempering temperature on a quenched-and-tempered steel
- **Usually means:** PWHT was specified from the code's generic stress-relief range without checking the mill cert's temper temperature, re-tempering (and softening) the base metal.
- **First question:** what temperature was this plate originally tempered at, per its mill certification?
- **Data to pull:** the mill cert's heat-treatment record and the PWHT chart's actual recorded hold temperature.

### An essential variable changed in production (filler lot, preheat, process) with the original PQR still cited as the basis
- **Usually means:** a substitution was made for schedule or availability reasons without routing it through requalification.
- **First question:** who approved this change, and does the code list this specific variable as essential for the properties this joint requires?
- **Data to pull:** the WPS revision history and the production traveler showing the as-run parameters.

### Weld-metal ferrite number outside the qualified range on an austenitic stainless multipass joint
- **Usually means:** filler metal lot or dilution from base metal shifted the actual ferrite content away from what the WRC-1992 diagram predicted for the nominal filler.
- **First question:** what ferrite number did the actual production weld measure, by ferritescope or chemical analysis, versus the WPS's qualified range?
- **Data to pull:** the ferrite reading log and the filler metal certification for the lot in use.

### A through-thickness-restrained joint (T- or K-joint into a thick flange) shows no through-thickness ductility (STRA) test on file
- **Usually means:** lamellar tearing risk was never screened, particularly if the flange's sulfur content is unknown or above roughly 0.01%.
- **First question:** what is the flange material's sulfur content and inclusion shape control, per its mill cert?
- **Data to pull:** the flange mill cert and, if one exists, the STRA test report for that heat.

### NDT reject rate on a production run trending upward across successive joints, not a single one-off
- **Usually means:** a parameter has drifted (heat input, preheat, filler lot) that a single joint's rejection wouldn't reveal but a trend does.
- **First question:** what changed at the point the reject rate started climbing — shift, filler lot, equipment, or ambient condition?
- **Data to pull:** the NDT report log sorted by joint and date, cross-referenced against the production traveler.

### Charpy V-notch average from the PQR is at or barely above the code's required minimum at the service's MDMT
- **Usually means:** the procedure has little margin — a small shift in heat input or preheat in production could drop actual toughness below the qualified value even though the PQR "passed."
- **First question:** how much margin exists between the PQR's Charpy average and the code's required minimum at this MDMT?
- **Data to pull:** the PQR mechanical test report and the vessel or structure's specified MDMT.

### Measured distortion exceeds tolerance despite the crew following the specified weld sequence
- **Usually means:** the sequence itself wasn't adequate for the joint's actual restraint and heat balance, an engineering design gap rather than a workmanship issue.
- **First question:** was the sequence validated against this specific joint's stiffness and restraint, or reused from a similar-looking job?
- **Data to pull:** the approved weld sequence drawing and the as-built distortion measurement.
