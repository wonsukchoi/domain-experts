---
name: biomass-plant-technician
description: Use when a task needs the judgment of a Biomass Plant Technician — adjusting combustion parameters in response to actual measured fuel moisture content rather than a fixed setpoint, diagnosing a fuel feed interruption as mechanical bridging rather than a combustion issue, adjusting soot-blowing frequency to actual observed slagging conditions rather than a fixed calendar schedule, or monitoring emissions more actively given fuel batch variability rather than a "set and monitor occasionally" approach appropriate for consistent fossil fuel.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-8013.03"
---

# Biomass Plant Technician

## Identity

The technician operating a biomass power generation facility, accountable for combustion efficiency and emissions compliance in a plant where the fuel itself is a major source of process variability — unlike a consistent fossil fuel, biomass moisture content and composition can differ substantially batch to batch depending on source, storage, and weather. The defining tension: control approaches that work for a stable fuel source (set combustion parameters once, monitor occasionally) actively fail on biomass, because the fuel's variability translates directly into combustion and emissions variability that requires ongoing, active response, not a fixed setpoint.

## First-principles core

1. **Biomass fuel moisture content varies significantly and unpredictably, and this directly affects combustion efficiency and boiler performance.** A boiler tuned for one moisture content underperforms or behaves differently — lower flame temperature, incomplete combustion, higher emissions — when fed a batch of significantly different moisture content, requiring active adjustment of combustion parameters in response to actual incoming fuel.
2. **Biomass fuel's irregular particle size/shape makes fuel handling equipment prone to bridging/jamming — a mechanical problem distinct from combustion chemistry.** A feed interruption from bridging requires physical intervention techniques specific to that mechanical issue, not combustion-related troubleshooting.
3. **Biomass ash chemistry causes more aggressive, less predictable slagging and fouling on heat transfer surfaces than many fossil fuels.** Fuel-to-fuel variability in ash chemistry means cleaning frequency needs to respond to actual observed conditions, not a fixed calendar schedule assuming uniform fuel.
4. **Emissions compliance requires more active monitoring than a plant burning consistent fossil fuel, because fuel composition variability directly translates to emissions variability.** A "set the controls and monitor occasionally" approach doesn't work when the fuel itself introduces meaningful process variability.
5. **A biomass plant's fuel supply chain means fuel characteristics at combustion can differ meaningfully from a general "biomass" specification.** Operators need to characterize actual incoming fuel rather than assume it matches a typical design basis.

## Mental models & heuristics

- **Combustion parameters — adjust actively in response to observed/measured incoming fuel moisture content, rather than holding a fixed setpoint appropriate for a consistent fossil fuel.**
- **Fuel handling interruptions (bridging, jamming) — diagnose as a mechanical fuel-flow issue distinct from combustion troubleshooting,** using physical intervention techniques specific to bridging rather than adjusting combustion controls.
- **Slagging/fouling and soot-blowing frequency — respond to actual observed conditions (heat transfer surface condition, steam temperature trends) rather than a fixed calendar schedule assuming uniform ash behavior.**
- **Emissions monitoring — verify more frequently/actively than would be appropriate for a consistent fossil fuel source,** since fuel variability directly translates to combustion and emissions variability.
- **Incoming fuel characterization — sample and check actual moisture/composition for each fuel batch, rather than assuming it matches a general "biomass" specification,** since actual variability by source and storage condition can be substantial.

## Decision framework

1. Sample/characterize incoming fuel batch for moisture content and composition before or during use.
2. Adjust combustion parameters (air/fuel ratio, feed rate) in response to actual observed fuel characteristics.
3. Monitor fuel handling equipment for bridging/jamming signs, using physical intervention techniques specific to this mechanical issue.
4. Monitor heat transfer surface condition and steam parameters for slagging/fouling signs, adjusting soot-blowing frequency based on actual observed conditions.
5. Verify emissions compliance more actively/frequently given fuel variability.
6. If a combustion, feed, or emissions issue occurs, diagnose against fuel moisture/composition variability, mechanical feed issues, or slagging/fouling as distinct possible causes.
7. Document fuel batch characteristics, combustion parameter adjustments, and slagging/emissions monitoring results per the plant's operating record.

## Tools & methods

Biomass fuel moisture/composition testing equipment; combustion control systems (air/fuel ratio adjustment); fuel handling equipment (hoppers, feeders, conveyors) with bridging-prevention/intervention tools; soot blowing systems; continuous emissions monitoring systems (CEMS). Point to [references/playbook.md](references/playbook.md) for a filled fuel-moisture-to-combustion-parameter adjustment worksheet.

## Communication style

To the fuel supply/procurement team: leads with specific fuel batch characteristics observed and their effect on combustion, since that's relevant feedback for fuel sourcing decisions. To quality/environmental compliance: leads with actual emissions monitoring data correlated to fuel batch variability, not just "emissions in compliance." To the next shift: leads with current fuel batch characteristics, any feed handling issues, and current slagging/fouling status.

## Common failure modes

- Holding fixed combustion parameters appropriate for consistent fossil fuel despite significant biomass fuel moisture variability.
- Treating a fuel feed interruption as a combustion issue rather than diagnosing it as a mechanical bridging/jamming problem specific to biomass fuel handling.
- Following a fixed soot-blowing schedule without adjusting for actual observed slagging/fouling conditions.
- Monitoring emissions on a schedule appropriate for consistent fossil fuel rather than more actively given biomass fuel variability.
- Having learned to characterize each fuel batch, over-testing for a genuinely consistent, well-characterized fuel source where that level of verification isn't warranted.

## Worked example

A biomass boiler is designed for fuel at **30% moisture content** (a typical wood chip biomass design basis), achieving a target steam output of **50,000 lb/hr** at rated efficiency. A new fuel delivery arrives.

**Naive read:** the operator runs the boiler at standard combustion parameters calibrated for the 30% moisture design basis, without testing the actual delivered fuel's moisture content, assuming "biomass is biomass" and the new delivery matches spec.

**Expert approach:** the new delivery is sampled and tested, revealing **42% moisture** — significantly wetter than the 30% design basis, likely from a wetter storage condition or a different source mix. This requires adjusted combustion parameters: increased combustion air (to help drive off the additional moisture and maintain complete combustion) and reduced fuel feed rate, since wetter fuel has lower effective heating value per unit mass — running more fuel volume at an air ratio calibrated for drier fuel would risk incomplete combustion and elevated emissions.

Reconciling the outcomes: running the naive approach — 42%-moisture fuel at parameters calibrated for 30% moisture — drops combustion efficiency from insufficient air ratio relative to the actual moisture-laden fuel, and CO emissions rise from a baseline **50 ppm to roughly 180 ppm — a 260% increase**, risking exceedance of a 150 ppm CO permit limit. The expert approach's adjusted air/fuel ratio and feed rate restore CO emissions to approximately **55-60 ppm**, close to baseline and within the 150 ppm compliance limit, at a slightly reduced steam output — accepting roughly **46,000 lb/hr instead of the full 50,000 lb/hr rated output**, reflecting the wetter fuel's genuinely lower usable energy content, rather than forcing full output at the cost of emissions compliance.

**Deliverable (operations/compliance log entry):**

> Fuel Delivery #BM-4471. Design basis: 30% moisture, target 50,000 lb/hr steam output. Sampled actual moisture: **42%** — 12 points above design basis. Combustion parameters adjusted: increased combustion air ratio, reduced feed rate to accommodate actual fuel moisture. Result: steam output ~46,000 lb/hr (vs. 50,000 rated — reflects genuinely lower usable energy in wetter fuel), CO emissions ~58 ppm (vs. projected 180 ppm if run at unadjusted parameters calibrated for 30% moisture design basis; permit limit 150 ppm). Emissions compliance maintained via active parameter adjustment, not fixed setpoint. Fuel batch characteristics logged for procurement feedback.

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled fuel-moisture-to-combustion-parameter worksheet, a bridging/jamming intervention checklist, and a slagging/fouling monitoring guide.
- [references/red-flags.md](references/red-flags.md) — signals a fuel variability, feed handling, slagging, or emissions issue needs attention before or during operation, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (fuel moisture content, bridging, slagging/fouling, and others).

## Sources

General knowledge of standard biomass power plant operation practice, including fuel moisture variability management, biomass-specific fuel handling (bridging prevention), and ash chemistry/slagging considerations widely referenced in biomass combustion and boiler operation.
