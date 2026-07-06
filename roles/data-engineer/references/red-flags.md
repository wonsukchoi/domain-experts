### A pipeline operation appends or increments values rather than upserting/overwriting by key
- **Usually means:** A retry or backfill will corrupt data by double-counting or duplicating records — this is a matter of when, not if, at any meaningful operational scale.
- **First question:** What happens to the output if this exact pipeline run is executed twice in a row on the same input?
- **Data to pull:** Pipeline's write logic (append vs. upsert/overwrite), retry/backfill history if available.

### A daily/periodic aggregation partitions data by when it was processed rather than when the underlying event occurred
- **Usually means:** Late-arriving records are being misattributed to the wrong time period, which can distort or even reverse an apparent trend.
- **First question:** Does this pipeline partition by event time (with a defined lateness allowance) or by processing/arrival time?
- **Data to pull:** Partitioning logic, sample of records with both event timestamp and processing timestamp to check for misattribution.

### A reported trend shows an unexpected or suspiciously convenient direction right around a period boundary (day/week/month)
- **Usually means:** This is a common symptom of processing-time vs. event-time misattribution, especially for data with a meaningful late-arrival rate (mobile, offline-queued, or multi-hop data sources).
- **First question:** Would the trend look different if late-arriving records were correctly reattributed to their true event-time period?
- **Data to pull:** Late-arrival rate for this data source, event-time-corrected aggregation for comparison.

### An upstream schema change was deployed with no compatibility validation
- **Usually means:** Downstream consumers may break outright or, worse, silently receive nulls or misaligned data without an obvious failure.
- **First question:** Was this schema change checked against a compatibility policy (e.g., additive-only, schema registry validation) before being deployed?
- **Data to pull:** Schema change details, downstream consumers' current behavior since the change.

### A pipeline has no automated data quality checks and relies on someone noticing a downstream anomaly
- **Usually means:** A broken upstream feed could be silently producing empty or wrong data for an extended period before anyone catches it.
- **First question:** What automated checks (row count, null rate, freshness, key uniqueness) run at each pipeline stage, and would they have caught this specific failure mode?
- **Data to pull:** Current data quality check coverage by pipeline stage.

### A use case requiring near-real-time data is served by a batch pipeline, or a use case with no real freshness requirement uses streaming
- **Usually means:** The architecture choice may not match the actual business need — either missing a genuine freshness requirement, or adding unnecessary operational complexity and cost.
- **First question:** What is the downstream use case's actual required freshness, and does the current batch/streaming choice match it?
- **Data to pull:** Documented or inferred freshness requirement, current pipeline's actual latency.

### A backfill or reprocessing scenario has never been explicitly tested
- **Usually means:** Non-idempotent operations or event-time handling bugs are most likely to surface specifically during backfill/reprocessing, and an untested scenario leaves this risk unverified.
- **First question:** Has this pipeline been tested by deliberately re-running it against already-processed data to confirm the output doesn't change?
- **Data to pull:** Test coverage for backfill/reprocessing scenarios (or its absence).

### A data contract or SLA with downstream consumers isn't documented
- **Usually means:** Downstream teams may be relying on implicit assumptions about freshness or completeness that the pipeline doesn't actually guarantee.
- **First question:** Is there a documented data contract specifying freshness, completeness, and schema-change handling for this pipeline's output?
- **Data to pull:** Existing documentation (or its absence) for this pipeline's guarantees to downstream consumers.
