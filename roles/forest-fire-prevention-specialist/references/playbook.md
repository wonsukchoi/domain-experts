# Playbook

Filled workflows for the three recurring jobs: setting/reviewing a precaution level, deciding a burn permit, and running an origin-and-cause investigation. Each is a step sequence with real thresholds an agent can execute against current data.

## 1. Industrial Fire Precaution Level (IFPL) review

Run this daily during fire season for each rated zone, and any time a station's ERC crosses a tier boundary mid-day.

**Step 1 — Pull today's readings for the specific station.**
- ERC (100-hr fuels), percentile against the station's historical distribution.
- 1-hr and 10-hr fuel moisture.
- Forecast temp/RH/wind for the operating window (not just current conditions).

**Step 2 — Match ERC percentile to the district's posted tier table.** Example table (values are illustrative of a typical coastal PNW district — use the locally posted table, thresholds vary by district and fuel type):

| IFPL Tier | ERC percentile | Cable yarding hours | Fire watch | Other operations |
|---|---|---|---|---|
| I (normal) | 0-59th | Unrestricted | 1-hour post-shutdown | Unrestricted |
| II | 60-75th | Unrestricted | 1-hr (road const.) / 3-hr (other) | Chainsaw fire watch required |
| III | 76-92nd | 2000-1300 only, lines suspended 10 ft when idle | 3-hour post-shutdown, continuous during gust-forecast hours | Road construction 2000-1300 only |
| IV (shutdown) | ≥93rd | Prohibited | N/A | All operations prohibited |

**Step 3 — Check the 3-day forecast for a wetting system before treating today's tier as durable.** A tier that's one point under the next boundary, with no rain in the 5-day outlook, gets an advisory notice to the operator even if today's call doesn't change.

**Step 4 — Check gust forecast against the crossover legs independently of the ERC-driven tier.** Sustained wind and gusts can justify an upgraded fire-watch requirement (continuous vs. 3-hour) even when the ERC-driven tier itself doesn't move.

**Step 5 — Issue the notice.** State: current tier, the specific threshold and percentile that set it, any operation-specific restriction (hours, fire watch level), and the review date (72 hours or next tier change, whichever is first).

## 2. Burn permit decision

**Step 1 — Confirm permit type**: agricultural/debris burn, prescribed fire unit, or recreational campfire. Each has a different weather-trigger standard; a prescribed-fire unit is evaluated against its own approved burn plan's trigger points, not the general permit checklist below.

**Step 2 — Check the day against a hard-stop list before evaluating anything else:**
- Active Red Flag Warning for the zone → deny (general debris/agricultural permits; prescribed units follow their plan's own RH/wind triggers, which are normally more conservative than a Red Flag threshold).
- Local burn ban in effect → deny, no exceptions at the field level.
- IFPL III or IV in effect for industrial land in the same zone → deny debris burns on or adjacent to industrial forestland even if the permit type itself doesn't reference IFPL.

**Step 3 — If no hard stop, check site-specific conditions:** clearance from the burn pile to unmanaged fuel (state minimum is typically 25-50 ft depending on jurisdiction and pile size — confirm local statute), water/hand-tool availability on site, and proximity to structures or a designated smoke-sensitive area.

**Step 4 — Set conditions on the permit, don't just approve/deny:** permitted burn window (commonly morning hours before afternoon RH drop and wind increase), maximum pile size, required attendance until fully extinguished, and a revocation trigger (e.g., permit is automatically void if a Red Flag Warning is issued after issuance and before the burn).

**Step 5 — Log the decision with the readings that drove it.** A denial or approval without the specific RH/wind/ERC numbers attached is not defensible if the permit is challenged or a fire results.

## 3. Origin-and-cause field investigation

**Step 1 — Secure the area of origin before entry.** Establish a perimeter wide enough to protect the general origin area from foot traffic, apparatus, and suppression activity that hasn't already occurred; document what suppression resources already crossed the area before the investigator arrived (they're often the first contamination source).

**Step 2 — Work from the general area of origin inward.** Use burn-pattern indicators — V-patterns, char depth gradients, protected/unprotected fuel comparisons, ash color and depth — to narrow from the general origin area to the specific point of origin. Do not start with a cause theory and look for confirming patterns.

**Step 3 — Cross-reference with contemporaneous weather and wind data for the exact time window**, not the daily average — spread direction only makes sense against the wind vector at ignition time, which can differ meaningfully from the daily mean, especially near diurnal wind shifts (upslope/downslope transitions).

**Step 4 — Collect physical evidence with chain of custody** for anything that could support or rule out a cause hypothesis: incendiary devices, fuses, electrical hardware, equipment left at scene, cigarette/match residue. Photograph and diagram before collection.

**Step 5 — Build the cause hypothesis only after the origin is fixed and the evidence is documented, and test it against the physical indicators before writing it down.** Reject a hypothesis that a witness account supports but the burn pattern contradicts.

**Step 6 — Classify at the confidence level the evidence supports:**
- Natural (specific: lightning, confirmed by strike-locator data correlated to origin time/location).
- Accidental, cause specifically identified (e.g., equipment spark, escaped debris burn, vehicle exhaust/catalytic converter contact with dry fuel).
- Human-caused, undetermined ignition source (evidence establishes human origin — e.g., origin at a roadside pull-off with no lightning activity — but the specific mechanism cannot be pinned down).
- Undetermined (origin area itself cannot be reliably fixed, or evidence is too degraded/contaminated).

**Step 7 — Write the report to the standard that survives cross-examination**: every conclusion traceable to a specific documented indicator, explicit statement of what was ruled out and why, and no cause classification more specific than the weakest link in the evidence chain supports.
