# Red flags — what a plant manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### Any single fuel supplier accounting for more than ~50-60% of total fuel volume
- **Usually means:** a seasonal shortfall, price spike, or logistics disruption from that one source can directly threaten plant reliability with no fast fallback.
- **First question:** "If this supplier's next delivery is 40% short, what's the actual qualified alternative and how fast can it be activated?"
- **Data to pull:** fuel volume by supplier over the trailing 12 months, qualification status and lead time for alternate sources.

### Ash content of an incoming or candidate fuel batch that would push daily ash production above the ash-handling system's rated capacity
- **Usually means:** running this fuel at scale risks an ash-handling system overload, not just a cost or efficiency tradeoff — a hard operational constraint, not a soft one.
- **First question:** "At the volume we'd need to burn, what's the resulting daily ash tonnage, and how does that compare to system capacity?"
- **Data to pull:** fuel ash content by batch/source, ash-handling system rated capacity, planned burn volume.

### Fuel moisture content 5+ percentage points above the level combustion parameters were last tuned for
- **Usually means:** the combustion process is likely running against a spec it's no longer matched to, risking incomplete combustion, efficiency loss, or slagging.
- **First question:** "When were combustion parameters last adjusted, and against what moisture spec — does that still match what's coming in now?"
- **Data to pull:** incoming fuel moisture test results by batch, combustion parameter change log and the fuel spec each setting was tuned against.

### Biomass fuel sitting in storage for longer than the source-specific safe storage window (commonly a few weeks to a couple of months depending on moisture and pile size) without turnover or temperature monitoring
- **Usually means:** elevated risk of moisture absorption, quality decay, or spontaneous combustion — a real fire and quality risk, not just an inventory-aging concern.
- **First question:** "What's the internal pile temperature reading, and when was it last checked?"
- **Data to pull:** storage duration by pile/lot, temperature monitoring logs, moisture re-test since intake.

### A new or expanded fuel source priced attractively at origin but sourced from meaningfully beyond the plant's established economical transport radius
- **Usually means:** the quoted origin price may not reflect the real delivered cost once biomass's low energy-density-per-transport-cost is factored in — it can look cheaper than it actually is.
- **First question:** "What's the fully delivered cost per unit of fuel energy (not per ton) from this source, at the actual distance?"
- **Data to pull:** origin price, transport distance and cost per ton-mile, as-received calorific value to normalize to a cost-per-MMBtu basis.

### Combustion efficiency or emissions readings drifting from baseline with no corresponding fuel-characteristic testing done to explain it
- **Usually means:** a fuel-quality shift is likely the cause and hasn't been diagnosed yet, as opposed to an equipment issue being investigated in isolation.
- **First question:** "Has incoming fuel been re-tested for moisture/calorific value/ash since this drift started?"
- **Data to pull:** efficiency/emissions trend, fuel test results over the same period, maintenance log for the same equipment.

### Procurement planning that doesn't reference the known seasonal availability pattern of the plant's primary fuel type(s)
- **Usually means:** the plant is exposed to a predictable seasonal shortfall it isn't planning around, rather than an unforeseeable disruption.
- **First question:** "What does this fuel source's historical seasonal availability curve look like, and does current inventory/contracting account for the next low-availability period?"
- **Data to pull:** historical seasonal supply-volume data by source, current contracted volume and inventory by month.

### An operating decision to accept an off-spec fuel batch justified solely by "it keeps the plant running"
- **Usually means:** a short-term output goal is being prioritized over checking whether the fuel's characteristics (moisture, ash, calorific value) actually fit what the combustion and ash-handling systems can safely process.
- **First question:** "What does this fuel's moisture/ash/calorific profile say about the combustion and ash-handling impact if we run it at the volume needed?"
- **Data to pull:** fuel test results for the candidate batch, system capacity limits it would be tested against.
