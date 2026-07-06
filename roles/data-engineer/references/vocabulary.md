### Idempotency (pipeline)
The property that running a pipeline operation multiple times with the same input produces the same result as running it once, making retries and backfills safe.
**In use:** "This aggregation needs to be idempotent — upsert by date key, not append — so a retry doesn't double-count."
**Common misuse:** Designing a pipeline operation that appends or increments values, which corrupts data the moment the operation is retried or backfilled.

### Event time vs. processing time
Event time is when something actually happened (e.g., when an order was placed); processing time is when the pipeline happened to process that record — the two can differ due to delays, and conflating them misattributes data to the wrong period.
**In use:** "We were partitioning by processing time, which misattributed late-arriving orders to the next day."
**Common misuse:** Partitioning or aggregating time-series data by processing time by default, without checking whether event-time partitioning is what the analysis actually requires.

### Watermark (lateness policy)
An explicit rule defining how long a pipeline will wait for late-arriving events before finalizing and closing out a time period's data.
**In use:** "We set a 6-hour watermark, so orders arriving up to 6 hours late still get correctly attributed to their true event date."
**Common misuse:** Having no defined watermark at all, either closing out a period too early (permanently losing late data) or never closing it out (making a period's totals perpetually unstable).

### Schema evolution / compatibility
The process of managing changes to a data schema over time (adding, removing, or changing fields) in a way that doesn't break downstream consumers, typically governed by explicit compatibility rules.
**In use:** "This schema change is additive-only, so it's backward compatible with existing consumers."
**Common misuse:** Deploying a schema change (renamed field, type change) without validating it against a compatibility policy, silently breaking or corrupting downstream pipelines.

### Schema registry
A centralized service that stores and validates data schemas, enforcing compatibility rules before a new schema version is allowed to be published or consumed.
**In use:** "The schema registry rejected this change because it removes a field that a downstream consumer still depends on."
**Common misuse:** Managing schema changes informally (via documentation or tribal knowledge) instead of enforcing them programmatically through a registry with compatibility validation.

### Data quality checks (completeness, uniqueness, freshness, distribution)
Automated validations run against a dataset to catch common failure modes: missing data (completeness), duplicate records (uniqueness), stale data (freshness), and unexpected value distributions.
**In use:** "The freshness check caught that this table hadn't updated in 18 hours, well past its expected 2-hour SLA."
**Common misuse:** Relying on a human noticing a downstream dashboard anomaly instead of running these checks automatically at each pipeline stage.

### Batch processing
A data processing approach where data is collected and processed in discrete, scheduled intervals (e.g., nightly), rather than continuously as it arrives.
**In use:** "Batch processing runs nightly, which is sufficient since this report doesn't need sub-day freshness."
**Common misuse:** Defaulting to batch processing for a use case that genuinely requires near-real-time data, missing the actual freshness requirement.

### Stream processing
A data processing approach where data is processed continuously as it arrives, typically achieving much lower latency than batch processing at the cost of added operational complexity.
**In use:** "This fraud detection use case needs stream processing — a nightly batch job would be far too slow to catch fraud in time."
**Common misuse:** Adopting streaming architecture for a use case that doesn't actually need sub-minute freshness, adding unnecessary operational complexity and cost.

### Data contract
An explicit agreement between a data producer and its consumers specifying schema, freshness, completeness, and change-management expectations for a dataset.
**In use:** "The data contract guarantees this table is updated by 6 AM daily with less than 0.1% null rate on required fields."
**Common misuse:** Operating without a documented data contract, leaving downstream consumers to rely on implicit and possibly incorrect assumptions about the pipeline's guarantees.

### Backfill
The process of reprocessing historical data through a pipeline, often to correct a bug, apply a schema change retroactively, or populate a new derived dataset.
**In use:** "The backfill needs to be idempotent too — reprocessing March's data shouldn't change April's numbers."
**Common misuse:** Testing a pipeline only against its normal forward-processing flow, never explicitly validating that a backfill or reprocessing run produces correct, non-duplicated results.
