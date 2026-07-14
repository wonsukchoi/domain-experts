# Red flags

### Cumulative reduction approaching the material's specified anneal trigger point
- **Usually means:** continuing further passes without an anneal risks exceeding the material's actual work-hardened capacity, even if the mill can still force the nominal reduction.
- **First question:** what is the cumulative reduction since the last anneal (or since starting stock), and how close is it to the specified trigger?
- **Data to pull:** pass-by-pass reduction log, material's specified cumulative reduction/anneal trigger threshold.

### Edge cracking appearing on a later pass in a multi-pass schedule, not on earlier passes at the same nominal reduction percentage
- **Usually means:** accumulated work hardening has reduced the material's actual ductility, even though the per-pass reduction percentage looks the same as earlier, successful passes.
- **First question:** does cumulative reduction since the last anneal exceed the material's specified threshold?
- **Data to pull:** cumulative reduction count, hardness data if available, anneal history for this coil/batch.

### Output thickness checked at only one point rather than across the material's width
- **Usually means:** a crown-mismatch-driven thickness variation across width could be present and undetected.
- **First question:** has thickness been measured at multiple points across width, or just a single location?
- **Data to pull:** multi-point thickness data if available, roll crown specification vs. actual load/width.

### A crown/gap setting carried over from a different width or reduction job without re-verification
- **Usually means:** the crown compensation validated for the prior job's load/width may not be correct for the current one.
- **First question:** does the current job's width and reduction match what the crown/gap setting was validated for?
- **Data to pull:** current job specifications, the setting's original validation parameters.

### A thickness profile showing "high center" or "high edge" across the material's width
- **Usually means:** roll crown mismatch relative to the actual rolling load — direction of the profile (thick center vs. thick edge) indicates whether crown is too much or too little for current conditions.
- **First question:** does the profile direction match an under- or over-crowned condition for this specific load?
- **Data to pull:** thickness profile data across width, current crown specification and rolling force.

### An inter-stand speed adjusted on one stand in a multi-stand mill without checking effect on adjacent stands
- **Usually means:** tension between stands may now be mismatched, risking necking, breaks, or buckling.
- **First question:** was the speed change on this stand evaluated for its effect on tension to the stands immediately before and after it?
- **Data to pull:** speed settings for all stands, any tension/buckling symptoms observed since the change.

### Material buckling or misalignment between rolling stands
- **Usually means:** insufficient inter-stand tension, likely from a stand speed mismatch.
- **First question:** do current stand speeds match the coordinated schedule, or has one been adjusted independently?
- **Data to pull:** stand speed settings across the mill, tension monitoring data if available.

### A necking or break occurring between rolling stands
- **Usually means:** excessive inter-stand tension, likely from a stand speed mismatch in the opposite direction from buckling.
- **First question:** does the break location correspond to a specific inter-stand gap with a known speed mismatch?
- **Data to pull:** stand speed settings, break location relative to stand positions.

### A material lot or heat processed on a standard pass schedule without checking its specific hardness/ductility characteristics
- **Usually means:** material variation between lots/heats could shift actual reduction capacity from what the standard schedule assumes.
- **First question:** does this lot's material certification match what the standard pass schedule was validated for?
- **Data to pull:** material lot/heat certification, standard schedule's validated material specification.

### An anneal performed but not verified to have actually restored the material's ductility before resuming rolling
- **Usually means:** an assumption that the anneal process ran correctly without confirming the material's actual post-anneal state.
- **First question:** has hardness or a similar verification confirmed the anneal achieved its intended effect, or is it assumed based on the furnace cycle completing?
- **Data to pull:** post-anneal hardness/verification data if performed, anneal furnace cycle log.
