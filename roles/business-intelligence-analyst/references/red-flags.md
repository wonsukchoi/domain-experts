# Red Flags

### Two dashboards report the same named metric with values differing by more than 5%
- **Usually means:** the metric has divergent underlying definitions (different filters, date boundaries, or included/excluded categories) or a join-grain fan-out on one side; second most likely — a genuine data pipeline bug in one source.
- **First question:** are the SQL definitions behind each dashboard's number actually identical, field for field?
- **Data to pull:** both dashboards' underlying query/model logic, side by side.

### Headline metric sum increased after adding a join to a new table
- **Usually means:** the new join is one-to-many relative to the existing grain, and an aggregation on an existing column is now fan-out-inflated; second most likely — a genuine duplicate-row data quality issue in the new table.
- **First question:** what does one row represent after the new join, compared to before it?
- **Data to pull:** row count before and after the join, compared against the expected row count at the intended grain.

### A metric's definition lives only inside one dashboard's query, with no entry in a shared semantic layer or metrics catalog
- **Usually means:** the dashboard's SQL has become the undocumented de facto standard, and any other team building a similar metric will independently diverge from it; second most likely — the semantic layer exists but this specific metric predates its adoption.
- **First question:** if this dashboard were rebuilt from scratch by someone else today, would they arrive at the same definition?
- **Data to pull:** the metrics catalog/semantic layer's current coverage list, compared against dashboards in active use.

### Aggregate trend moving one direction while the top-3-by-volume segments underneath are flat or moving the opposite direction
- **Usually means:** a mix-shift (Simpson's paradox) artifact — the composition of the aggregate changed, not the underlying segment performance; second most likely — one small, high-growth segment is genuinely driving the whole move and deserves highlighting, not hiding.
- **First question:** has the relative size of each segment changed over the same period the aggregate moved?
- **Data to pull:** segment-level trend lines and segment size (weight) over time, side by side with the aggregate.

### A KPI target set as a single flat number with no reference to historical seasonality
- **Usually means:** the target-setting process didn't account for known weekly/monthly/seasonal patterns, manufacturing false misses or false beats purely from calendar timing; second most likely — the metric genuinely has no meaningful seasonality and a flat target is appropriate.
- **First question:** does this metric show a repeating pattern in the same weeks/months across prior periods?
- **Data to pull:** year-over-year or period-over-period trend for the same metric, checked for a repeating seasonal shape.

### Dashboard "last updated" timestamp isn't visible to the viewer
- **Usually means:** stakeholders can't tell whether they're looking at current or stale data, which is the actual complaint behind most "we need this in real-time" requests; second most likely — the pipeline's freshness is inconsistent and hiding the timestamp avoids surfacing that.
- **First question:** how would a viewer currently tell if this number is from this morning or three days ago?
- **Data to pull:** actual refresh cadence/history for this dashboard's underlying pipeline over the last 30 days.

### A newly requested metric is a near-duplicate of an existing governed metric under a slightly different name
- **Usually means:** the requester didn't know the existing metric existed, or found it doesn't quite match their definition and asked for a new one instead of proposing a change to the shared definition; second most likely — a genuinely distinct metric that happens to sound similar.
- **First question:** what specifically about the existing governed metric doesn't fit this use case?
- **Data to pull:** the existing metric's full definition, compared field-by-field against the new request.
