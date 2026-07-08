# Red flags

Smell tests a marine engineer/naval architect catches in the first pass over a stability booklet, freeboard calculation, powering basis, or structural scantling package.

### GM(fluid) below 0.15 m at any approved loading condition

- **Usually means:** the KG estimate was optimistic relative to the as-built weight, or the free-surface correction was omitted or understated.
- **First question:** has FSC been applied for every slack tank actually in this condition's sounding table, not just a generic tank list?
- **Data to pull:** loading condition weight/KG table, tank sounding table for this condition, latest inclining experiment report.

### GZ curve area under 0.055 m·rad to 30° even though GM clears the minimum

- **Usually means:** the hull has beam-driven initial stability but inadequate reserve buoyancy or freeboard at large heel — common on low-freeboard hulls or vessels with heavy stacked deck cargo.
- **First question:** what is the downflooding angle, and does it occur before the 40° reference angle used in the area criterion?
- **Data to pull:** cross curves of stability (KN table), full GZ curve plot for this condition, downflooding point survey.

### Lightship weight growth exceeding roughly 3-5% between contract weight estimate and inclining experiment

- **Usually means:** unaccounted outfit, piping, cabling, or insulation weight accumulated during detailed design and production.
- **First question:** which weight groups (steel, outfit, machinery) account for most of the growth?
- **Data to pull:** weight control report by group, inclining experiment results and resulting KG.

### Free surface correction computed from tank full capacity instead of the actual sounding for that condition

- **Usually means:** the analyst pulled a generic FSC table value instead of the condition-specific fill level.
- **First question:** what is this tank's actual sounding in this loading condition, and is it in the partial-fill range where free surface peaks?
- **Data to pull:** tank sounding tables, loading computer output for the condition under review.

### Freeboard calculation shows no block-coefficient correction on a hull with Cb above 0.68

- **Usually means:** the calculation template was copied from a finer reference hull and never re-checked against this vessel's actual Cb.
- **First question:** what is this hull's Cb at the freeboard (summer load line) draft, not the design draft used elsewhere in the report?
- **Data to pull:** hydrostatic table at the freeboard draft, ICLL Reg. 30 correction worksheet.

### Admiralty coefficient sourced from a ship type with a materially different Cb or speed-length ratio

- **Usually means:** the powering estimate borrowed a convenient published coefficient instead of a form-matched reference vessel.
- **First question:** does the reference vessel's Cb, L/B ratio, and Froude number actually match this hull, or just its displacement?
- **Data to pull:** reference vessel's trial data and Ac derivation, this hull's Cb/Fn.

### Sea trial speed lands more than roughly 5% below the contract guarantee at the trial power

- **Usually means:** the powering estimate's coefficient was optimistic, or the hull-fouling/sea margin allowance was undersized.
- **First question:** was the trial run at the contracted displacement and sea state, or under more favorable conditions than the guarantee assumes?
- **Data to pull:** sea trial report, original powering prediction basis and margin assumptions, trial displacement/draft.

### Damage stability case shows some positive GZ range but no explicit check against the SOLAS Ch. II-1 required residual GM and range

- **Usually means:** "doesn't capsize immediately" (some positive GZ) was treated as sufficient without checking the actual regulatory residual-stability thresholds for this subdivision index.
- **First question:** what residual GM and range of positive stability does this ship's required subdivision index (A-index) mandate for this damage case?
- **Data to pull:** SOLAS II-1 damage stability calculation set, probabilistic subdivision index report.

### Deck cargo or lashing plan changed without a corresponding loading condition resubmitted to class

- **Usually means:** operations added cargo weight or height beyond what any approved loading manual condition covers.
- **First question:** is this specific cargo/lashing configuration present in the approved loading manual, or an unreviewed extrapolation from a nearby one?
- **Data to pull:** approved loading manual condition list, actual cargo/lashing plan as loaded.

### Installed power sea margin below roughly 15% on a coastal or ocean-going hull

- **Usually means:** the concept-stage power sizing used calm-water Admiralty-coefficient results directly, with no allowance for added resistance in the vessel's actual service route.
- **First question:** what route and sea-state notation is this vessel actually rated for, and does the margin match it?
- **Data to pull:** powering basis report, intended service/route notation, class society margin guidance for that route.

### Midship section modulus check run against class rule minimums with no adjustment for the specified steel grade

- **Usually means:** the scantling check defaulted to mild-steel rule values on a structure specified in higher-tensile steel, or vice versa.
- **First question:** what steel grade does the midship section drawing actually specify, and does the rule calculation reference the matching material factor?
- **Data to pull:** class rule scantling calculation sheet, midship section drawing material callouts.

### Trim by the stern exceeding roughly 1% of LBP at a critical loading condition with no propeller-immersion or forward-visibility check attached

- **Usually means:** the trim result was accepted as a number without checking its operational consequence.
- **First question:** does this trim keep the propeller fully immersed and satisfy the bridge's forward-visibility-over-the-bow requirement?
- **Data to pull:** trim and stability booklet for the condition, propeller immersion diagram, SOLAS forward-visibility calculation.
