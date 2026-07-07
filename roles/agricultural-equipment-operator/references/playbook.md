# Playbook

Filled templates and worked procedures — run these directly, don't treat them as descriptions of what to do.

## 1. Field-capacity worksheet

Effective field capacity (EFC, ac/hr) = speed (mph) × width (ft) × field efficiency (%) ÷ 8.25.

Field efficiency accounts for turns, unloading on the go vs. stopping, overlap, and idle time — it is never 100%. Typical starting values (adjust from your own machine's actual performance once you have two or three fields of data):

| Operation | Typical field efficiency |
|---|---|
| Planting, no-till or high-residue | 65–75% |
| Planting, conventional tillage | 75–85% |
| Combine, corn (grain cart alongside, no stops) | 78–85% |
| Combine, soybeans (more header-height corrections, more stops) | 70–78% |
| Spraying, self-propelled | 65–80% |

**Worked example — three-job season plan:**

| Job | Speed (mph) | Width (ft) | Efficiency | EFC (ac/hr) | Acres | Hours | Field-days (10 hr) |
|---|---|---|---|---|---|---|---|
| Planting corn | 5.5 | 60 | 0.80 | 5.5×60×0.80/8.25 = 32.0 | 3,200 | 100 | 10.0 |
| Planting soybeans | 5.0 | 60 | 0.75 | 5.0×60×0.75/8.25 = 27.3 | 1,800 | 66 | 6.6 |
| Harvest soybeans | 4.0 | 30 | 0.75 | 10.9 | 1,800 | 165 | 16.5 |
| Harvest corn | 4.5 | 30 | 0.80 | 13.1 | 3,200 | 244 | 24.4 |

Compare each row's field-days requirement against the forecasted good-field-day count for that window before committing to a sequence. A shortfall is closed by adding capacity (second machine, custom hire, wider header) or extending hours — never by silently assuming the efficiency percentage will improve under pressure.

## 2. Planter calibration checklist (run per field, per condition change)

| Crop | Target population (seeds/ac) | Target singulation | Skip tolerance | Double tolerance | Spacing CV target |
|---|---|---|---|---|---|
| Corn | 32,000–36,000 (adjust for hybrid/yield goal) | ≥98% | <2% | <1% | <10%, ideally <8% |
| Soybeans, 30" rows | 120,000–140,000 | ≥97% | <3% | <1% | <15% |
| Soybeans, drilled/narrow row | 140,000–160,000 | ≥95% | <5% | <2% | <20% |

**Procedure:**

1. Fill row units with the seed lot actually going into the field (not a reference lot — seed size and shape affect singulation).
2. Run a 300–500-seed test pass at planned ground speed in a representative part of the field (not the smoothest end-row).
3. Pull the monitor's singulation/skip/double/CV report for that pass. If any value is outside the table above, adjust downforce, disk speed, or vacuum before planting the rest of the field — don't plant first and hope the average recovers.
4. Re-check after any change in soil type, residue level, or moisture within the same field — calibration set at the gate does not hold across a field with mixed soil types.
5. Log the population and CV by field zone against the yield map at harvest; a zone that consistently under-performs at "correct" population may need a population change next season, not a calibration fix this one.

## 3. Combine loss drop-pan test

**Equipment:** a rigid frame or pan of known area (commonly 10 sq ft, e.g., a 2 ft × 5 ft frame), a bucket, and a seed/kernel counter (or a scale and known seeds/lb for the lot).

**Conversion factors (standard heuristics):**

| Crop | Seeds or kernels per sq ft ≈ 1 bu/acre loss |
|---|---|
| Soybeans | ~4 seeds/sq ft |
| Corn | ~2 kernels/sq ft |
| Wheat | ~14–18 kernels/sq ft (varies more by kernel size/moisture) |

**Procedure:**

1. **Pre-harvest baseline.** Toss the pan into standing crop just ahead of where the header will pass. Count seeds/kernels caught — this is natural pre-harvest shatter/drop, not machine loss, and must be subtracted from every later reading.
2. **Total loss.** Immediately after the combine passes over the same strip, drop the pan behind the machine (behind the header for header-only loss; behind the whole machine, ahead of the chaff spreader pattern, for total loss). Count seeds/kernels.
3. **Machine-attributable loss = total loss − pre-harvest baseline.** Divide by the conversion factor to get bu/acre.
4. **Compare against the acceptable-loss threshold** (soybeans and corn: ~1–2 bu/acre is normal; >2 bu/acre calls for an adjustment pass before continuing). Multiply the delta by acres and current price to state the finding in dollars, not just bushels — that's the number that gets a schedule change approved.
5. **Isolate the cause before changing multiple settings at once:** header-only loss points to reel index, header height, or ground speed; separator/tailings loss points to cylinder/rotor speed, concave clearance, or fan speed. Change one variable, retest, then move to the next.

**Worked conversion (soybeans):** total loss 14 seeds/sq ft, baseline 2 seeds/sq ft → 12 seeds/sq ft machine loss ÷ 4 = 3 bu/acre. At $12.50/bu on 1,800 acres, that's 3 × 1,800 × $12.50 = **$67,500** left in the field — the number to lead with when asking for time to stop and adjust.

## 4. Harvest sequencing-by-risk template

Fill this before the first day of harvest, not field-by-field under pressure:

| Field | Crop | Days past maturity | Lodging/shatter risk | Contract/moisture deadline | Priority |
|---|---|---|---|---|---|
| North 40 | Soybeans | 12 | High (pod shatter, thin-walled variety) | None | 1 |
| Home quarter | Corn | 8 | Medium (moderate stalk quality) | None | 3 |
| River bottom | Soybeans | 5 | Low (recently mature, tight pods) | Elevator slot in 10 days | 2 |
| East 80 | Corn | 15 | High (early-planted, stalk rot present) | None | 4 (but escalate if scouting confirms rot spreading) |

Priority order is set by combined risk and deadline, re-scored after any scouting update (a stalk-quality check showing rot progressing moves a field up regardless of its original slot) — not left static once the season starts.

## 5. Grain-bin entry safety checklist (every entry, no exceptions)

1. Shut down and lock out all augers, sweeps, and unload equipment feeding or drawing from the bin — verify at the control panel, not by assumption.
2. Post an entry permit stating purpose, expected duration, and hazards present (engulfment, entanglement, atmospheric).
3. Station a dedicated observer outside the bin with a harness/lifeline attached to the entrant and a plan to call for help — the observer's only job is watching, not helping load or run equipment.
4. Test for flowing-grain hazards (bridged grain, crusted surface over a cavity) before stepping onto the surface; treat any crusted or bridged grain as unstable until probed.
5. If grain must be moving during entry (rare, higher-risk case), the entry does not happen — stop the flow first, every time.
