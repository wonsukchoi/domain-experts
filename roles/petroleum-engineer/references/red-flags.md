# Red flags

Smell tests a petroleum engineer catches in the first pass over a decline curve fit, reserves report, well test, or casing design.

### Decline curve fit shows b-exponent above 1.0 extrapolated to the economic limit with no terminal decline switch

- **Usually means:** early-time transient (linear/bilinear) flow from a multi-fractured horizontal well is being fit as if it were the well's permanent boundary-dominated behavior.
- **First question:** has a terminal (minimum) decline rate been applied, and at what secant decline does the switch happen?
- **Data to pull:** decline curve fit parameters (qi, Di, b), log-log rate/derivative diagnostic plot, resulting implied well life.

### P/Z vs. cumulative-gas-production plot curves instead of forming a straight line

- **Usually means:** aquifer influx (water drive) is present and is not accounted for in a simple volumetric material balance, or a pressure survey datum/gauge error is distorting one or more points.
- **First question:** does switching to the generalized material balance equation with a We (influx) term straighten the trend?
- **Data to pull:** pressure survey history with datum corrections, Gp vs. time, offset well or regional aquifer evidence.

### Casing collapse design factor falls below the operator's minimum (commonly 1.0-1.125) under the full-evacuation load case

- **Usually means:** the string was sized to a lighter load case (partial evacuation, normal drilling) and never re-checked against the worst credible well-control scenario for this hole section.
- **First question:** what load case actually governs collapse for this string, and was it the one used in the design check?
- **Data to pull:** casing tally and grade, rated collapse pressure (wear- and biaxial-adjusted), load-case worksheet.

### Well's measured producing rate is below the IPR-predicted rate at the same flowing bottomhole pressure

- **Usually means:** near-wellbore skin damage (formation damage, scale, incomplete perforation cleanup) or a mechanical restriction (undersized tubing, partially plugged perforations), not reduced reservoir deliverability.
- **First question:** has a pressure buildup test been run to separate skin from true reservoir permeability?
- **Data to pull:** buildup test derivative (Horner or log-log) plot, most recent IPR test data, completion/perforation diagram.

### Proved (1P) reserves booked on a location with no direct offset production data in the same bench

- **Usually means:** the location was categorized on geologic/team confidence rather than the SPE-PRMS reasonable-certainty (~P90) evidentiary standard.
- **First question:** what specific offset well(s), and how many months of comparable production, support this category?
- **Data to pull:** offset well list with spacing and bench, production history for each offset, the technical support memo behind the category call.

### Voidage replacement ratio (VRR) sustained below 1.0 across three or more consecutive reporting periods

- **Usually means:** water/gas injection volume is not keeping pace with reservoir withdrawal — pressure decline is likely already underway or imminent.
- **First question:** is the shortfall an injectivity limit (per-well rate), an injector-count limit, or a facility capacity limit?
- **Data to pull:** injection and production volumes by phase (reservoir barrels), reservoir pressure survey trend, injector-by-injector rate history.

### Hydraulic fracture treating pressure shows a sudden step-down mid-stage

- **Usually means:** near-wellbore bridging has relieved or a proppant screenout is beginning — a precursor to a full screenout if not addressed.
- **First question:** is treating pressure still tracking the planned net-pressure match, or has it diverged from the pre-job model?
- **Data to pull:** real-time treating pressure/rate/proppant-concentration log, pre-job net-pressure model, any prior step-down test on this well.

### Gas lift injection rate has been increased repeatedly with no corresponding oil rate increase

- **Usually means:** the well has passed the optimum point on its gas lift performance curve and is now loading up on friction losses from excess injection gas rather than gaining lift benefit.
- **First question:** where does the current injection rate sit relative to this well's gas-lift performance curve optimum?
- **Data to pull:** gas lift performance curve, injection/production rate history, surface and downhole pressure survey.

### Decline curve match is built on fewer than roughly 6-12 months of stabilized post-flowback production

- **Usually means:** the fit is capturing early-time transient flow, not boundary-dominated decline, and the resulting b and Di will not hold as the well matures.
- **First question:** does a log-log rate/derivative diagnostic confirm boundary-dominated flow has actually started?
- **Data to pull:** full production history including flowback, log-log diagnostic plot, offset well decline behavior at a comparable maturity.

### Casing burst rating cited is the new-pipe API catalog value with no derate for connection efficiency or documented wear

- **Usually means:** the string's actual working pressure capacity is lower than the number being relied on, especially at a premium connection or on a string with logged wear.
- **First question:** what is this connection's rated efficiency (percent of pipe-body rating), and has a caliper/multi-finger imaging wear log been run?
- **Data to pull:** connection performance rating sheet, casing wear log, API TR 5C3/ISO 10400 derated burst calculation.

### Reserves report's price deck is the current spot or forward-strip price rather than the SEC trailing 12-month first-day-of-month average

- **Usually means:** the report is being prepared for internal planning purposes but is at risk of being mistaken for (or reused as) an SEC-compliant filing number.
- **First question:** which price standard does this specific report need to satisfy — SEC filing or internal planning case?
- **Data to pull:** the 12-month first-day-of-month price series, the report's stated pricing basis and intended use.
