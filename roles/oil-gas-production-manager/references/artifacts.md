# Artifacts

Filled templates for the three documents an oil and gas production manager produces most: the production shortfall diagnostic, the intervention NPV ranking, and the well integrity investigation report.

## Production shortfall diagnostic (filled example)

```markdown
# Production Shortfall Diagnostic — Field Alpha, Week of [date]

Plan: 12,000 bopd | Actual: 10,200 bopd | Shortfall: -15% (-1,800 bopd)

Step 1 — Measurement/allocation check:
  LACT meter at central tank battery recalibrated 3 weeks ago, timing
  matches shortfall onset exactly. Post-calibration audit against truck
  ticket volumes shows 8.4% undercount versus prior calibration baseline.
  CORRECTED production estimate: ~11,070 bopd (-7.75% vs plan)

Step 2 — Mechanical/artificial lift check:
  Individual well decline curve comparison (actual vs. Arps hyperbolic
  fit) flags 2 wells with performance below curve-predicted output:
    Well #14: -34% vs. decline curve prediction, ESP amp draw pattern
      consistent with pump wear
    Well #27: -29% vs. decline curve prediction, similar ESP signature
  Remaining 38 wells: within +/-5% of decline curve prediction (normal
  variance, no action needed)

Step 3 — Reservoir/interference check:
  Not required — steps 1-2 account for the full corrected shortfall
  (~900 bopd from wells #14 and #27 against the -930 bopd corrected gap).

Conclusion: shortfall is 85% measurement artifact, 15% localized ESP
degradation on 2 identifiable wells. No reservoir-level issue present.
```

## Intervention NPV ranking (filled example)

```markdown
# Intervention Capital Ranking — Q2 candidates

Well  | Intervention type    | Cost      | Incremental bopd | NPV (18mo, $75/bbl) | NPV/$ spent
------|-----------------------|-----------|--------------------|-----------------------|-------------
#14    | ESP replacement        | $170,000  | 210 bopd            | $612,000               | 3.6x
#27    | ESP replacement        | $170,000  | 190 bopd            | $554,000               | 3.3x
#08    | Acid stimulation       | $340,000  | 140 bopd            | $409,000               | 1.2x
#31    | Acid stimulation       | $340,000  | 95 bopd              | $278,000               | 0.8x
#19    | Acid stimulation       | $340,000  | 80 bopd              | $233,000               | 0.7x
#22    | Acid stimulation       | $340,000  | 60 bopd              | $175,000               | 0.5x

Decision: approve #14 and #27 (ESP replacement, $340,000 total, combined
NPV/$ ~3.4x). Defer stimulation candidates #08, #31, #19, #22 pending
next capital cycle — NPV/$ well below the ESP candidates, and #31/#19/#22
don't clear the field's minimum 1.0x hurdle rate this cycle.

Original proposal (6-well stimulation, $2.8M) would have included all
four below-hurdle candidates — this ranking avoids ~$2.46M in capital
that wouldn't clear the field's return threshold.
```

## Well integrity investigation report (filled example)

```markdown
# Well Integrity Investigation — Well #33, Sustained Casing Pressure

Date flagged: [date]
Signal: Annulus B pressure reading increased from 40 psi (baseline) to
215 psi over 6 days, with no corresponding change in production rate
or wellhead temperature.

IMMEDIATE ACTION: Well shut in pending investigation per policy — sustained
casing pressure above 150 psi over baseline is an automatic production
hold, not a monitor-and-continue situation.

Investigation findings:
  Pressure bleed-down test: annulus repressurizes to 210 psi within 4
  hours after bleed-down to 0 — indicates active gas migration, not a
  static trapped-pressure artifact.
  Cement bond log (historical, at completion): showed a moderate-quality
  bond in the interval 8,200-8,450 ft, flagged as monitor-only at the time.
  Working hypothesis: gas migration through the previously-flagged cement
  interval, consistent with the pressure behavior observed.

Determination: NOT cleared to resume normal production. Recommend
remedial cementing (squeeze job) before returning well to production.
Estimated cost: $185,000. Estimated downtime: 12-15 days.

Escalation: this is the third sustained casing pressure event this year
tracing to a cement interval flagged as "moderate quality, monitor-only"
at completion. Recommend reviewing whether monitor-only cement bond
determinations at this field should trigger earlier remedial action
rather than waiting for a pressure event.
```
