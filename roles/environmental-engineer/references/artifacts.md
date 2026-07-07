# Artifacts

Filled examples for the deliverables an environmental engineer actually produces. Populate the numbers, don't just follow the shape.

## Mass balance worksheet (wastewater treatment)

| Parameter | Influent | Design basis | Current loading | % of design |
|---|---|---|---|---|
| Flow (gpd) | 260,000 | 300,000 (hydraulic) | 260,000 | 87% |
| BOD5 (mg/L) | 850 | — | 850 | — |
| BOD5 mass (lb/day) | 1,842 | 1,600 (biological) | 1,842 | 115% |
| TSS (mg/L) | 620 | — | 620 | — |
| TSS mass (lb/day) | 1,344 | 1,400 | 1,344 | 96% |
| Effluent BOD5 (mg/L) | — | 30 (limit) | 38 | 127% of limit* |

\*Flag immediately — this line means the current *effluent*, not just the loading, is already trending toward the limit before the proposed increase; don't let a capacity memo bury an existing near-exceedance.

Formula: mass (lb/day) = concentration (mg/L) × flow (MGD) × 8.34.

## NPDES permit application checklist (Form 2C-equivalent industrial discharge)

1. Facility description and SIC/NAICS code.
2. Outfall location(s) with lat/long, receiving water name and use classification.
3. Effluent characteristics — 3 rounds of sampling minimum (grab and/or 24-hr composite per outfall, per permit-specified method), for each parameter the permit will limit.
4. Flow measurement method and calibration record (weir, flume, or meter — specify).
5. Treatment system description — unit processes in order, design capacity of each.
6. Best Management Practices (BMP) plan if stormwater co-mingled.
7. Certification statement signed by a responsible corporate officer (not the engineer) — 40 CFR 122.22 requires this specific signatory, an engineer's signature alone does not satisfy it.

## Air permit applicability screen (New Source Review / Title V)

| Pollutant | Current PTE (tpy) | Proposed increase (tpy) | New PTE (tpy) | Major source threshold (tpy)* | Status |
|---|---|---|---|---|---|
| NOx | 38 | 6 | 44 | 40 (nonattainment) / 100 (attainment) | Check attainment status of county before concluding |
| VOC | 22 | 3 | 25 | 40 / 100 | Below either threshold |
| PM10 | 12 | 1 | 13 | 100 | Below threshold |

\*Thresholds vary by pollutant, attainment classification, and source category (40 CFR 51/52) — never apply a single number across all pollutants without checking the county's attainment designation for each one.

## Site remediation technology comparison (feasibility study excerpt)

| Option | Est. cost | Time to closure | Handles active pathway? | Recommended when |
|---|---|---|---|---|
| Monitored Natural Attenuation (MNA) | $150K (10 yrs monitoring) | 8-15 years | No | No completed exposure pathway, declining contaminant trend confirmed over 2+ years of data |
| Pump-and-treat | $1.2M (design+O&M, 10 yrs) | 5-10 years | Partial (hydraulic containment) | Groundwater plume needs containment but source is diffuse |
| In-situ chemical oxidation (ISCO) | $650K | 1-3 years | Yes, source-area | Discrete source area, no nearby structures at vapor-intrusion risk |
| Excavation and disposal | $2.1M | <1 year | Yes, immediately | Active vapor intrusion pathway to occupied building, or sale/redevelopment deadline forces fast closure |

Default to the cheapest option meeting the cleanup level on the regulator's timeline unless a documented urgency (active pathway, transaction deadline) justifies paying for speed — see SKILL.md heuristic.

## Discharge monitoring report (DMR) exceedance log template

| Month | Parameter | Result | Limit | Exceedance? | Sample type | Cause investigated |
|---|---|---|---|---|---|---|
| Jan | BOD5 | 34 mg/L | 30 mg/L | Yes | Grab (permit requires composite) | Invalid — wrong sample type, resample required |
| Feb | BOD5 | 28 mg/L | 30 mg/L | No | Composite | — |
| Mar | BOD5 | 41 mg/L | 30 mg/L | Yes | Composite | Aeration blower failure, 6-hr downtime — corrective action filed |

Rolling 12-month count of *valid* exceedances (excluding invalidated samples like January's) is what most enforcement escalation triggers actually count — track it separately from the raw exceedance count.
