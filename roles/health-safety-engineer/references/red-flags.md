# Red flags

Smell tests a health and safety engineer catches on a first pass over a machine guarding installation, a PHA record, or an incident-rate report.

### Point-of-operation guard distance matches the machine's nameplate stop-time spec, not a recent field-measured value

- **Usually means:** the guard was sized once at commissioning and never re-verified against brake wear, which commonly extends real stopping time well past the rated figure.
- **First question:** when was the last field brake-monitor test, and does the installed distance still satisfy Ds = 63.5 x Ts using that reading?
- **Data to pull:** brake-monitor test log (date, measured Ts), original guard installation calculation sheet.

### Safety interlock present, but the control circuit is a single unrated switch on a catastrophic-severity hazard

- **Usually means:** "there's an interlock" was treated as satisfying the standard without checking the required Performance Level or Safety Integrity Level the risk assessment calls for.
- **First question:** what Category (ANSI B11.19) or Performance Level (ISO 13849-1) does the hazard's severity actually require, and does the installed circuit architecture meet it?
- **Data to pull:** risk assessment PLr determination, interlock circuit diagram, component safety-rating datasheets.

### Risk matrix score recorded at initial assessment, no residual score after the control was installed

- **Usually means:** the control was installed and the item closed on completion, not on verified risk reduction — a common gap between "we fixed it" and "we confirmed the fix worked."
- **First question:** what is the residual severity x probability score with the control in place, and does it clear the matrix's acceptable-band threshold?
- **Data to pull:** initial and residual risk assessment records for the same hazard ID.

### PHA revalidation is more than 5 years old for a PSM-covered process (1910.119(e)(6))

- **Usually means:** the revalidation cycle was missed, or a management-of-change event was never tied back to a documented re-review.
- **First question:** what changed in this process — equipment, chemistry, procedure — since the last PHA, and was each change routed through MOC?
- **Data to pull:** PHA revalidation date log, MOC records for the process since the last PHA.

### LOPA worksheet credits two independent protection layers driven by the same sensor or the same human response

- **Usually means:** a scenario's mitigated frequency was calculated using layers that aren't actually independent, understating true risk.
- **First question:** does each credited IPL have its own sensor, logic solver, and final element, fully independent of the initiating event and of every other credited layer?
- **Data to pull:** instrument loop diagrams for each credited IPL, cause-and-effect matrix.

### TRIR below the industry NAICS benchmark cited as the reason a specific open hazard is deprioritized

- **Usually means:** an aggregate lagging indicator is being used to make a decision about a single hazard's severity, which the rate doesn't measure.
- **First question:** what is this specific hazard's worst credible outcome, independent of the plant-wide rate?
- **Data to pull:** hazard-specific risk matrix score, incident history at that specific station or task, not the plant aggregate.

### Confined-space or lockout/tagout control depends on an operator remembering a manual sequencing step

- **Usually means:** the control was written as a procedure because a physical interlock (trapped-key system, group lockout box) was seen as too costly, without an independent failure-rate check on the procedural alternative.
- **First question:** what happens if the operator skips or reorders the manual step — is the unsafe state physically reachable?
- **Data to pull:** lockout/tagout procedure document, energy-isolation point list, any near-miss reports involving this task.

### HAZOP node table is missing "no/none," "more," or "less" rows for a flow, level, pressure, or temperature parameter

- **Usually means:** the session ran as an open brainstorm rather than a guide-word-driven analysis, and systematically skipped a deviation category.
- **First question:** was every relevant guide word applied to every parameter at this node, or only the ones the team happened to think of?
- **Data to pull:** the completed node worksheet, node boundary definition (P&ID markup showing node scope).

### Machine guarding standard cited by name (ANSI B11.19) with no documented Performance Level determination behind it

- **Usually means:** the standard was invoked as a label rather than applied — a real B11.19 compliance claim requires a risk assessment that produced a specific PLr, not just "we followed B11.19."
- **First question:** what PLr did the risk assessment calculate, and does the installed safety function's achieved PL meet or exceed it?
- **Data to pull:** risk assessment worksheet with PLr calculation, safety function validation report (achieved PL).

### Two or more OSHA-recordable injuries at the same station or task within 12 months, all logged as separate, unrelated incidents

- **Usually means:** a systemic unguarded or under-controlled hazard is producing repeat outcomes, and each incident investigation stopped at the immediate cause instead of flagging the pattern.
- **First question:** do the incident reports share a common task, machine, or energy source, and has that common factor been risk-matrix scored on its own?
- **Data to pull:** OSHA 300 log entries for the station, incident investigation root-cause fields, prior risk assessment for that station if one exists.
