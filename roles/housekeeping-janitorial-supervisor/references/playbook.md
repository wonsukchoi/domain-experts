# Playbook

Filled worksheets and step sequences for the recurring housekeeping/janitorial supervisor tasks: building a daily assignment board, sizing a janitorial crew against square footage, running the inspection walkthrough, and correcting a chemical/compliance gap.

## 1. Daily room-attendant assignment board (hotel/lodging)

Convert today's arrivals report into a credit worksheet before assigning sections — never assign by "room count" alone.

| Attendant | Section (rooms) | Checkouts (1.0 credit) | Stayovers (0.5 credit) | Eco-refresh (0.15 credit) | Total credits | vs. 16-credit standard |
|---|---|---|---|---|---|---|
| A. Ruiz | 101–117 | 5 | 12 | 0 | 11.0 | −5.0 (light) |
| B. Nguyen | 118–134 | 8 | 9 | 0 | 12.5 | −3.5 |
| C. Osei | 135–151 | 7 | 10 | 3 | 12.45 | −3.55 |
| D. Flores (on-call, 4 hrs) | 152–159 | 6 | 4 | 0 | 8.0 | (0.5-shift target: 8.0) |

**Sequencing rule inside a section:** checkouts before stayovers when both exist in the same section — checkouts have a hard downstream deadline (next arrival); stayovers do not. Exception: a stayover with an active guest-request flag ("need towels now," maintenance callback) jumps the queue regardless of credit type.

**Shortfall protocol (use when present capacity < credit demand):**
1. Convert eligible stayovers to eco-refresh (opt-out/reuse program) — recalculate savings at 0.35 credit per conversion (0.5 − 0.15).
2. Activate on-call/cross-trained labor; credit their allotment at (hours worked ÷ 8) × 16, not a full shift's worth.
3. Recompute remaining shortfall. If still short, defer stayovers only, ranked: (a) no active request flag, (b) longest interval since last full clean was *most* recent (i.e., defer the ones least in need of another clean today), (c) not a VIP/loyalty top-tier guest.
4. Never defer a checkout-credit room to close a shortfall — checkouts are the constraint on sellable inventory.

## 2. Janitorial crew sizing against square footage (commercial/office)

Use ISSA 540 Cleaning Times-style production rates as the planning input, then adjust for the building's actual condition — the standard rate assumes an "ordinary tidiness" starting condition (APPA Level 2), not heavy build-out debris or a post-event mess.

| Task | Production rate (sq ft or units/hour, blended) | Notes |
|---|---|---|
| General office vacuuming/dusting/trash | ~3,000 sq ft/hour | Open-plan floors are faster than cubicle-dense floors; adjust down 15–20% for high partition density. |
| Restroom cleaning | ~2.5–3 minutes per fixture | Fixture count (toilets + urinals + sinks), not square footage, drives restroom time. |
| Hard-floor mopping | ~3,500–4,000 sq ft/hour | Auto-scrubber equipped crews run 2–3x this; factor equipment into the rate before staffing off a manual-labor number. |
| Carpet spot/detail work | ~1,000–1,500 sq ft/hour | Detail work (stain treatment, edge work) is not interchangeable with routine vacuum-and-go. |

**Worked sizing example.** 60,000 sq ft office floor, nightly service, 5 nights/week, mixed open-plan/cubicle (blended rate 2,500 sq ft/hour after 17% cubicle-density adjustment):
- Hours needed = 60,000 ÷ 2,500 = 24 labor-hours/night.
- At an 8-hour shift, that's 3 FTE-equivalent nightly, or a crew of 4 at 6 hours each to allow for a day-porter carve-out.
- Labor cost check (BSCAI-style benchmarking): if the regional loaded labor rate is $22/hour, nightly labor cost = 24 × $22 = $528/night, or ≈ $0.0088/sq ft/night — at 5 nights/week (≈21.7 nights/month), ≈ $0.19/sq ft/month, within the commonly cited $0.10–$0.20/sq ft/month commercial janitorial range. A bid coming in at $0.06/sq ft/month for the same scope and frequency is underpriced — check whether the frequency, headcount, or supply allowance was quietly cut to hit the number before accepting it.

## 3. Inspection walkthrough scorecard

Score on two separate axes — never let one absorb the other.

| Category | Points possible | Score | Critical fail? |
|---|---|---|---|
| Bed/linen presentation | 15 | 14 | No |
| Bathroom sanitation | 20 | 16 | No |
| Dusting/surface cleanliness | 15 | 15 | No |
| Floor/carpet condition | 15 | 13 | No |
| Amenity/supply restock | 10 | 10 | No |
| Odor/air quality | 10 | 9 | No |
| Safety (smoke detector, egress clear) | 15 | 15 | **Checked separately** |
| **Aggregate** | 100 | 92 | — |

A 92/100 aggregate looks like a pass against a typical 90-point threshold. But if the safety row instead showed a non-functioning smoke detector, the room is **out of service regardless of the 92**, per the critical-fail override rule — record the critical fail as a binary flag next to the score, never blended into the average.

## 4. Chemical/compliance gap correction sequence

1. **Identify the gap same-shift** (relabeled secondary container without GHS pictogram/product identifier, wrong dilution ratio, missing PPE at a task with reasonably anticipated exposure).
2. **Pull the SDS** for the product in question and confirm correct dilution ratio, required PPE, and stated contact/dwell time.
3. **Relabel or re-supply on the spot** — do not let the shift end with a non-compliant container in use.
4. **Log the correction** with date, product, location, and corrective action — this is the record an OSHA inspector or CIMS auditor will ask for first.
5. **If the gap involves a bloodborne-pathogen exposure task** (sharps, bodily fluids) with no documented Hepatitis B vaccination offer on file for the attendant involved, escalate to HR/EHS the same day — a missing offer record inside the required 10-day window from task assignment is a standing compliance gap, not a paperwork backlog item.

**Color-coded tool system (cross-contamination control), standard mapping:**

| Color | Zone |
|---|---|
| Red | Restrooms/toilets |
| Yellow | Disinfectant-only surfaces (high-touch points) |
| Blue | General surfaces (furniture, glass) |
| Green | Food-service/kitchen-adjacent areas |

A crew substituting colors "because we ran out" is a stop-work item for that task, not a documented exception — get the correct color to the attendant before the task continues.
