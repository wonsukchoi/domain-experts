# Vocabulary

### Grain
The level of detail a single row in a table represents — order-line grain, order grain, daily-summary grain, etc.
**In use:** "This fact table is at order-line grain, so joining to shipments before aggregating will fan out any line with multiple partial shipments."
**Common misuse:** Assuming a table's grain from its name alone ("orders" table) without checking whether a row is actually one order or one order-line — the two are easy to conflate and produce silent aggregation errors.

### Fan-out (join fan-out)
The multiplication of rows that occurs when a one-to-many join is performed and a value from the "one" side is then summed or counted, effectively duplicating it once per matching row on the "many" side.
**In use:** "The revenue number is inflated because of fan-out — each order line got counted once per shipment instead of once total."
**Common misuse:** Diagnosing an inflated aggregate as a "data quality issue" (assuming duplicate source records) when the actual cause is a join-then-aggregate ordering problem in the query itself — the underlying data may be entirely correct.

### Semantic layer (metrics layer)
A centralized definition layer (e.g. dbt metrics, LookML, Cube) where a metric's calculation logic is defined once and reused across every dashboard, query, or tool that references it.
**In use:** "We moved 'Net Revenue' into the semantic layer so the finance dashboard and the sales dashboard both inherit the exact same definition instead of each having their own SQL."
**Common misuse:** Treating the existence of a semantic layer as automatic governance — without an approval process for adding or changing definitions within it, duplicate near-identical metrics can proliferate inside the "governed" layer just as easily as outside it.

### Star schema
A dimensional modeling pattern with a central fact table (events/transactions at a stated grain) surrounded by denormalized dimension tables (customer, product, date) that the fact table joins to.
**In use:** "We modeled this as a star schema so every report joins to the same conformed date and customer dimensions instead of each analyst writing their own date logic."
**Common misuse:** Applying a full star schema to a one-off ad-hoc analysis that will never be reused — the modeling overhead only pays off when multiple reports need the same consistent joins.

### Conformed dimension
A dimension table (e.g. date, customer) built once with a consistent definition and shared across multiple fact tables, so the same customer or date behaves identically in every report that uses it.
**In use:** "The date dimension is conformed across sales and marketing fact tables, so a 'fiscal quarter' filter means the same thing in both reports."
**Common misuse:** Letting each team build their own version of a common dimension (e.g. two separate "customer" tables with different dedup logic) and calling both "the customer dimension" — this is exactly how metrics diverge silently across departments.

### Mix shift
A change in an aggregate metric that's driven by a change in the relative composition (weights) of its underlying segments, rather than a change in any individual segment's actual performance.
**In use:** "Average order value went up, but it's mix shift — the high-AOV enterprise segment just grew as a share of total orders, not because any segment's typical order got bigger."
**Common misuse:** Reading an aggregate improvement as evidence that "things are working better across the board" without checking whether it's actually a composition change masking flat or declining segment-level performance.

### Data freshness (staleness)
The time lag between when an underlying event occurred and when it's reflected in a dashboard or report, typically expressed as a refresh cadence or maximum acceptable lag.
**In use:** "This pipeline has a 4-hour freshness SLA — if the dashboard shows numbers older than that, the freshness monitor should page someone."
**Common misuse:** Defaulting every dashboard request to the freshest technically achievable cadence rather than the cadence the underlying decision actually requires — freshness has a real infrastructure cost that should be matched to decision cadence, not maximized by default.

### Drill-down
The ability to navigate from an aggregate number to its underlying constituent records or segments within the same reporting tool.
**In use:** "Ops dashboards need drill-down to the individual ticket level so the on-call person can self-diagnose which customers are affected."
**Common misuse:** Adding extensive drill-down to executive-facing dashboards where the audience needs the headline and a one-line driver, not a path to explore raw records — excess drill-down there adds surface area for misreading, not clarity.

### Single source of truth (metric governance)
The principle that a given named metric has exactly one authoritative, documented definition that every tool and team references, rather than each team computing its own version.
**In use:** "Revenue has a single source of truth in the semantic layer now — any dashboard showing a different number for it is querying the wrong table, not using a legitimate alternative definition."
**Common misuse:** Declaring a metric has "a single source of truth" when it's actually defined identically in name only across teams, with differing filter logic underneath that nobody has reconciled.

### Reconciliation
The process of confirming a reported metric matches an independently computed or authoritative reference value (e.g. finance's closed books) within a stated tolerance.
**In use:** "We reconcile the dashboard's revenue figure against finance's monthly close within 0.5% as an automated test on every refresh."
**Common misuse:** Treating a one-time manual reconciliation at launch as sufficient — without an ongoing automated check, drift (schema changes, new join paths, new data sources) can silently break the tie-out again later.
