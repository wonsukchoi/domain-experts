# Chemical Technician Playbook

Filled templates and step sequences. Defaults, not laws — deviate consciously, document why, escalate.

## 1. Daily instrument/reference QC log

Minimum fields, filled example (analytical balance, but the same structure applies to a pH meter buffer check, a GC retention-time check, or a titrant restandardization):

| Date | Instrument ID | Reference used | Certificate/lot | Expected value | Observed | Δ from expected | In SOP tolerance? | In control (2σ/3σ)? | Analyst |
|---|---|---|---|---|---|---|---|---|---|
| 2026-03-09 | QC-BAL-04 | 10.0000 g Class 1 wt | NIST-trace cert #CW-2291, exp 2027-01 | 10.0000 g | 9.9998 g | −0.0002 g | Yes (±0.0005 g) | 2σ warning (limit 9.9998) | J. Alvarez |
| 2026-03-10 | QC-BAL-04 | 10.0000 g Class 1 wt | CW-2291 | 10.0000 g | 9.9998 g | −0.0002 g | Yes | 2σ warning | J. Alvarez |
| 2026-03-11 | QC-BAL-04 | 10.0000 g Class 1 wt | CW-2291 | 10.0000 g | 9.9997 g | −0.0003 g | Yes | 3σ, Rule 6 building | J. Alvarez |
| 2026-03-12 | QC-BAL-04 | 10.0000 g Class 1 wt | CW-2291 | 10.0000 g | 9.9996 g | −0.0004 g | Yes | 3σ exceeded, Rule 6 triggered | J. Alvarez |

**Action on any "3σ exceeded" or run-rule row:** stop using the instrument for reportable results, log a hold notice, notify supervisor same shift, open a service ticket. Do not wait for an SOP-tolerance failure — see the SKILL.md worked example for the projection math.

## 2. Control-chart run rules (apply every day, not just at spec failure)

| Rule | Trigger | Typical meaning |
|---|---|---|
| Rule 1 | 1 point beyond ±3σ | Sudden shift — reagent swap, instrument fault, sample mixup |
| Rule 2 | 2 of 3 consecutive points beyond ±2σ, same side | Early drift — reference degrading, lamp/column aging |
| Rule 5 | 4 of 5 consecutive points beyond ±1σ, same side | Slow bias creeping in |
| Rule 6 | 6+ consecutive points steadily trending one direction | Progressive drift — recalibration due, consumable aging |
| Rule 7 | 8+ consecutive points on one side of centerline | Sustained shift in the mean — recheck the reference standard itself |

Any rule trigger gets logged even if every individual point is inside the SOP acceptance tolerance — spec tolerance and statistical control are different bars, and the chart exists to catch the gap between them.

## 3. Out-of-specification (OOS) investigation flow

1. **Stop.** Do not retest before Step 2 is documented.
2. **Phase 1 — lab investigation.** Check, in order, and record each: (a) calculation/transcription error, (b) instrument calibration status at time of run, (c) reagent/standard lot and expiration, (d) sample prep steps against the SOP. If a clear, documented lab error is found (e.g., wrong dilution factor used), invalidate the result with the specific cause cited and rerun — this is not "retesting into a pass," it's correcting an identified error.
3. **Phase 2 — if no lab error found.** Escalate to the chemist/QA for a full investigation: repeat prep from the original sample (not a new aliquot unless the SOP allows), review other results from the same batch/instrument run, check for a trend on the control chart in the preceding week.
4. **Never average a failing result with a passing retest** to produce a passing mean. Each result stands on its own unless formally invalidated with a documented cause.
5. **Close the investigation record** regardless of outcome — "investigated, cause X, result invalidated" or "investigated, no lab cause found, original result stands, escalated to QA" are both valid closures; "retested, now passes" alone is not.

## 4. Reagent/standard prep and labeling

Minimum label fields, filled example:

```
0.1000 N NaOH (standardized)
Prepared: 2026-03-05 by J. Alvarez
Standardized against: KHP, Lot #KHP-2291 (assay 99.98%)
Standardization result: 0.1000 N (n=3, %RSD 0.4%) — see logbook p.114
Expiration: 2026-04-02 (28-day shelf life per SOP-QMS-021, or upon
  failed restandardization check, whichever comes first)
Restandardization due: weekly, or immediately if control check fails
```

**Restandardization trigger, not just the calendar date:** if a daily titrant check (titrating against a known sample) drifts by more than the method's established %RSD from the last standardization, restandardize immediately rather than waiting for the scheduled interval — titrants degrade (e.g., NaOH absorbing atmospheric CO2) at a rate that varies with how often the container is opened, not on a fixed clock.

## 5. Chain-of-custody (COC) minimum fields

For any sample requiring legal/regulatory defensibility (environmental under NELAC/TNI, forensic, any accredited method):

| Field | Example |
|---|---|
| Sample ID / unique identifier | ENV-24-0817-03 |
| Collected by / date-time | R. Chen, 2026-03-08 09:14 |
| Received by / date-time | J. Alvarez, 2026-03-08 14:02 |
| Condition on receipt | Intact, iced, 4.1°C (acceptance range 0–6°C) |
| Holding time deadline | 2026-03-15 (7-day extraction hold) |
| Every subsequent transfer | Name, date-time, purpose (e.g., "to GC bench for extraction") |
| Final disposition | Disposed 2026-04-01, manifest #WM-33812, or archived location |

A gap of several hours between collection/receipt and login with no explanation is a custody break, not an administrative delay — treat it as a red flag (see references/red-flags.md) even if the analytical result looks fine.

## 6. Chemical storage compatibility groups

| Group | Examples | Never store adjacent to |
|---|---|---|
| Oxidizers | Nitric acid, hydrogen peroxide (>8%), sodium hypochlorite | Flammables, organics, reducing agents |
| Flammables/organics | Acetone, methanol, ethyl acetate | Oxidizers, strong acids |
| Corrosive acids | Sulfuric, hydrochloric, acetic | Bases, cyanide/sulfide salts (toxic gas risk), oxidizers |
| Corrosive bases | Sodium hydroxide, ammonium hydroxide | Acids |
| Water-reactives | Sodium metal, some metal hydrides | Any aqueous solution, sprinklered storage areas |
| Toxics (segregate, ventilate) | Cyanide salts, mercury compounds | Acids (cyanide → HCN gas) |

Group by hazard class using each chemical's SDS Section 7 (Handling and Storage) and Section 10 (Reactivity), never alphabetically. NFPA 45 sets maximum flammable-liquid quantities per storage area and cabinet ventilation requirements — check the site's approved quantity before adding a new flammable to a cabinet.
