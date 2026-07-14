# Playbook

Operational workflows a geography instructor actually runs, with filled example numbers. Starting points to adapt, not scripts.

## 1. Projection-selection worksheet (run before any measurement-based GIS assignment)

Fill this before students touch the software, so the projection is a documented decision, not a software default.

| Task type | Required projection property | Default choice | Wrong-default failure mode |
|---|---|---|---|
| Area comparison (canopy cover, land use, country size) | Equal-area | Albers Equal-Area (regional) / Mollweide (global) | Mercator (EPSG:3857) inflates high-latitude area — Greenland reads ~14x larger than its true relative size vs. Africa |
| Distance/routing (navigation, bearing) | Conformal (local angle-true) | Lambert Conformal Conic / Mercator | Equal-area projections distort local shape/angle, giving wrong bearings |
| Local site-scale measurement (parcel, tract area) | Projected, locally accurate | State Plane / UTM zone for the site | Unprojected geographic coordinates (EPSG:4326) produce area/distance figures off by 10-20%+ depending on latitude |
| General reference/web display | Balance of all properties | Robinson / Winkel Tripel | Using a measurement-grade projection for display wastes visual space without adding accuracy value |

**Filled example — the GEOG 415 canopy-cover project (city at 42°N):** area calculation must use a projected equal-area CRS. Correct choice: NAD83 / Conus Albers (EPSG:5070). Wrong choice used by the student: raw EPSG:4326 pixel-count conversion, which overstated the 42-tract average canopy area by 18%.

## 2. Confound-check worksheet (run before accepting any causal claim from a spatial correlation)

**Step 1 — state the claimed relationship and its correlation coefficient.**
Example: "Tree canopy cover causes lower summer land-surface temperature," r = −0.71 across 42 tracts.

**Step 2 — list at least two candidate confounds that plausibly correlate with both variables.**

| Candidate confound | Correlation with outcome (LST) | Correlation with predictor (canopy %) | Plausible? |
|---|---|---|---|
| Impervious surface % | r = 0.68 | r = −0.55 | Yes — canopy loss and impervious surface both track urban density |
| Tract median elevation | r = 0.04 | r = 0.02 | No — city has minimal elevation range, ruled out |
| Distance to nearest water body | r = −0.22 | r = 0.11 | Weak — worth a footnote, not a full control |

**Step 3 — recompute as a partial correlation controlling for the strongest confound.**
Example: partial r (canopy, LST | impervious surface) = −0.34, down from raw r = −0.71 — the relationship survives but at roughly half the apparent strength.

**Step 4 — restate the claim at the size the controlled statistic supports.**
"Tree canopy cover is associated with a real but moderate cooling effect (partial r = −0.34) once impervious-surface density is controlled for" replaces the uncontrolled causal claim.

## 3. GIS-lab rubric template (methodology-weighted, for labs worth 20%+ of course grade)

| Category | Points | What it scores |
|---|---|---|
| Methodology & scale justification | 30 | Was the unit of analysis and spatial scale justified for the phenomenon studied? Was a confound considered before any causal language? |
| Data source & projection accuracy | 20 | Is the dataset current, correctly attributed, and was the projection/CRS appropriate for the specific calculation performed? |
| Statistical/spatial reasoning | 30 | Is the statistical method appropriate (correlation vs. regression vs. spatial autocorrelation test), and are confounds addressed? |
| Map/output communication | 20 | Is the final map or output legible, correctly labeled, and does its design choice (color, classification breaks) match the data's actual distribution? |

**Grading rule:** a data-source or projection error that changes a reported number (as in the worked example's 18% area overstatement) deducts from Data source & projection accuracy in proportion to the error's size, not a flat penalty — a 5% area error and an 18% area error should not cost the same points.

## 4. Balanced-sources lesson design (for contested geopolitical / human-geography topics)

**Trigger:** any lesson involving a border dispute, resource-rights conflict, migration policy debate, or other topic where reasonable, informed parties disagree on normative grounds (not resolvable by a single data point).

**Steps:**
1. Separate the descriptive claims (population figures, resource locations, historical timeline) from the normative claims (whose claim is legitimate, what policy should follow) — descriptive claims get a single best-sourced answer; normative claims do not.
2. For the normative portion, assign at least one credible source representing each major position, named and attributed, not summarized secondhand through a single source's framing.
3. Frame classroom discussion prompts around the sourced positions ("what does source A argue, and what does source B argue, and what evidence does each cite") rather than "which side is right."
4. Document the source list in the syllabus or lesson plan so the balance is auditable after the fact, not just asserted.

**Filled example — a river water-rights dispute between two named regions:**

| Claim type | Example claim | Source treatment |
|---|---|---|
| Descriptive | "Region A's agricultural sector draws an estimated 2.3 billion cubic meters annually from the river" | Single best available hydrological/government dataset, cited |
| Descriptive | "The treaty allocating flow rights dates to 1960" | Single verifiable historical record, cited |
| Normative | "Region A's historical usage should set its allocation baseline" | Source representing Region A's position, named |
| Normative | "Population growth in Region B since 1960 justifies renegotiating the allocation" | Source representing Region B's position, named |

Discussion prompt built from this table: "Compare how source A and source B each use the same 1960 treaty and the same usage data to argue opposite conclusions — what assumption does each source make that the other rejects?"
