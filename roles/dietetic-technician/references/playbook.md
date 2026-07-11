# Dietetic Technician Playbook

Filled sequences and thresholds, not descriptions of them — defaults to execute or adapt, with the reasoning for when to deviate.

## 1. Nutrition screening → escalation sequencing

**On admission (acute care: within 24 hours per Joint Commission PC.01.02.01; long-term care: within 14 days of admission, then per the MDS schedule):**

1. Administer the facility's validated tool. Example, MST (Malnutrition Screening Tool):
   - Unintentional weight loss: none = 0, uncertain = 2, 1–5 kg = 1, 6–10 kg = 2, 11–15 kg = 3, >15 kg = 4.
   - Poor appetite/eating less: no = 0, yes = 1.
   - **Score ≥ 2 = at risk → route to RDN inside the screening window.** Score 0–1 = routine, recheck at next scheduled interval.
2. For residents already flagged at risk, layer a validated severity tool at the RDN's direction (MNA-SF for geriatric populations, subjective global assessment for complex cases) — the NDTR administers and records; interpreting a borderline severity score into a nutrition diagnosis is the RDN's step.
3. Log the raw score and the trigger reason, not just "at risk" — the RDN needs the actual weight-loss bucket or appetite answer, not a summary label.

## 2. Diet-order translation table (example facility diet manual mapping)

| Physician order as written | What it actually means (per Nutrition Care Manual-style diet manual) | First check before cutting the ticket |
|---|---|---|
| "Cardiac diet" | No-added-salt (~2–3g sodium/day), limited saturated fat; NOT automatically low-cholesterol unless co-ordered | Confirm current facility sodium target — "cardiac" alone is not a fixed gram count |
| "ADA diet" / "diabetic diet" | Legacy term; current standard is "consistent carbohydrate diet" — same carb grams at each meal daily, not a sugar-free diet | Confirm carb-gram target per meal with the RDN's plan, not a generic 45–60g default |
| "Renal diet" | Restricted potassium/phosphorus/sodium, protein level depends on dialysis status — pre-dialysis vs. hemodialysis protein targets are opposite in direction | Confirm dialysis status before applying a protein restriction — the wrong direction here is a clinical error, not a preference issue |
| "NPO advance to clears" | Sequential order: NPO → clear liquids → full liquids → mechanical soft/regular, each step gated on tolerance | Confirm which step the resident is actually on today, not the order's original date |
| "Mechanical soft" | Maps to IDDSI food level 6 (soft & bite-sized) in most current diet manuals | Check the facility's IDDSI crosswalk — some legacy manuals still use "mechanical soft" inconsistently across texture and liquid levels |
| "Thicken to nectar" | Legacy NDD term → IDDSI liquid level 2 (mildly thick) | Confirm the facility completed its IDDSI conversion; mixed legacy/IDDSI terminology on one tray ticket is a common source of thickener errors |

## 3. Intake/weight monitoring thresholds (Academy/ASPEN significant-loss criteria)

| Time frame | Significant loss | Severe loss |
|---|---|---|
| 1 week | 1–2% | > 2% |
| 1 month | 5% | > 5% |
| 3 months | 7.5% | > 7.5% |
| 6 months | 10% | > 10% |

Calculation: `% loss = (usual weight − current weight) / usual weight × 100`.

**Meal-intake escalation rule (typical facility policy):** average intake < 50% of the ordered diet for 3 consecutive days (or 3 consecutive meals in acute care with faster turnover) → same-shift RDN notification, independent of weight status. Weight-loss threshold and intake threshold are two separate triggers — either alone is sufficient to escalate; do not wait for both.

## 4. Food-safety threshold checklist (FDA Food Code)

1. **Cold holding:** ≤ 41°F. Out of range → check unit temp log for a 4-hour cumulative window; discard if cumulative time above 41°F exceeds 4 hours, or if unknown.
2. **Hot holding:** ≥ 135°F. Below 135°F → one-time reheat to 165°F within 2 hours is the only save; a second failure on the same batch is a discard, not a second reheat.
3. **Cooling:** 135°F → 70°F within 2 hours, then 70°F → 41°F within an additional 4 hours (6 hours total). Missing either checkpoint → discard, do not average the two windows.
4. **Reheating for hot holding:** to 165°F for at least 15 seconds before placing in hot holding.
5. **Allergy/intolerance cross-check:** every tray ticket compared against the chart's active allergy/intolerance flags before tray assembly — this check is not covered by temperature logs and is the most common miss when food-safety compliance is otherwise perfect.

## 5. When intake decline and a texture/tolerance signal appear together

Do not default to "encourage intake" as the first intervention. Sequence:

1. Pull nursing/CNA notes for the same window for coughing, pocketing, prolonged chewing, or refusal specifically at the current texture/liquid level.
2. If tolerance signals are present, hold the current IDDSI level (do not downgrade or upgrade unilaterally) and route to RDN + SLP for swallow re-evaluation.
3. If no tolerance signals are present, route to RDN as an appetite/intake issue — the differential matters because the fix (texture re-evaluation vs. preference/appetite intervention) is different, and guessing wrong wastes the RDN's next visit on the wrong hypothesis.
