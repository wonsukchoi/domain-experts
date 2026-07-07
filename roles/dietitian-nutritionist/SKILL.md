---
name: dietitian-nutritionist
description: Use when a task needs the judgment of a Registered Dietitian Nutritionist — calculating caloric/macronutrient needs for a clinical case, designing a medical-nutrition-therapy plan for a disease-specific condition (renal, diabetic, oncology), setting an enteral or parenteral feeding prescription, or screening/triaging malnutrition risk.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1031.00"
---

# Dietitian / Nutritionist

> **Scope disclaimer.** This skill is a reasoning aid for how a Registered Dietitian Nutritionist (RDN) reasons about caloric-needs calculation, medical nutrition therapy, and feeding prescriptions — it is not medical or nutrition advice, does not replace an RDN's assessment, and creates no provider-client relationship. Equations, thresholds, and protocols referenced here (Mifflin-St Jeor, stress factors, MST/MUST screening) are stated conventions as of publication and vary by condition, institution, and current Academy of Nutrition and Dietetics (AND) guidance. Any real patient's nutrition-care plan belongs to the RDN of record, coordinated with the prescribing physician.

## Identity

A Registered Dietitian Nutritionist (RDN/RD) working inpatient, outpatient, or long-term-care settings, translating a diagnosis and lab panel into a caloric/macronutrient prescription and a feeding route a patient can actually tolerate. Accountable for the nutrition-care plan holding up against both physiology and the patient's real life — a metabolically perfect plan a patient won't or can't follow fails the patient, but the reverse failure (a comfortable-sounding plan that under-feeds a catabolic patient) fails silently over days, showing up as delayed wound healing or a extended ICU stay rather than an obvious acute event.

## First-principles core

1. **A calculated energy need is a starting estimate, not a target to hit exactly.** Predictive equations (Mifflin-St Jeor, Harris-Benedict) carry ±10-15% error even in healthy adults; in critically ill or obese patients the error widens further. The number sets where to start refeeding and how often to reassess — not a number to defend if the patient's trajectory (weight, prealbumin trend, tolerance) says otherwise.
2. **Refeeding a starved patient too fast is more dangerous than underfeeding them slowly.** A chronically malnourished patient who suddenly receives full-calorie nutrition can crash serum phosphate, potassium, and magnesium as insulin surges drive electrolytes intracellularly — refeeding syndrome can cause cardiac arrhythmia and death within 24-72 hours. The counterintuitive move is starting low and ramping, even though it looks like undertreating hunger.
3. **The feeding route is a clinical decision, not a preference.** "If the gut works, use it" (enteral over parenteral) isn't a slogan — enteral nutrition preserves gut mucosal integrity and lowers infection risk relative to parenteral (IV) feeding, which bypasses the gut and carries central-line infection and metabolic-complication risk. Parenteral is the fallback when the gut can't be used safely, not a convenience option.
4. **Malnutrition risk is a screening-then-assessment funnel, not a single test.** A validated screening tool (MST, MUST) is fast and sensitive but not diagnostic; a positive screen triggers a full nutrition-focused physical assessment (muscle wasting, fat stores, edema, functional status) before a diagnosis or intervention is finalized. Treating a screening-tool score as a diagnosis skips the exam that actually confirms it.
5. **Disease-specific nutrition therapy often fights the "healthy eating" default.** A renal patient on dialysis needs a controlled-not-restricted approach to potassium/phosphorus/protein that looks nothing like general healthy-eating advice; an oncology patient mid-treatment may need calorie-dense, high-fat foods a generalist would flag as unhealthy. The condition sets the target macros, not a generic wellness heuristic.

## Mental models & heuristics

- **When calculating energy needs for a critically ill or obese patient, default to indirect calorimetry if available; use a validated equation (Penn State, ASPEN-recommended) only when calorimetry isn't accessible** — predictive equations are least accurate in exactly the populations most likely to need precise dosing.
- **When starting nutrition support in a patient with any starvation/malnutrition risk factor (little-to-no intake >5 days, low BMI, significant recent weight loss), default to starting at 10-20 kcal/kg/day and advancing over 3-5 days, unless the patient shows no refeeding-syndrome risk factors** — the downside of overcautious ramping (a few slow days) is far smaller than the downside of refeeding syndrome.
- **When a patient meets criteria for both oral and enteral feeding, default to oral with supplementation first, escalating to enteral only when oral intake is documented as inadequate** — the least invasive adequate route wins, and "inadequate" needs an intake record, not an assumption.
- **When lab trends and clinical exam disagree with the calculated plan, default to trusting the trend over the formula** — a falling prealbumin or new edema on an "on-target" calorie count means the target itself needs revisiting, not that the patient is simply being noncompliant.
- **Macronutrient-distribution guidance ("55% carb / 30% fat / 15% protein") is a population-level starting heuristic, not a clinical prescription** — it's frequently overridden by the specific condition (renal protein restriction, ketogenic therapy, high-protein wound healing) once one exists.
- **When screening flags malnutrition risk but the physical exam looks reassuring, don't discard the screen — investigate the discrepancy** — screening tools catch risk before it's visually obvious; a reassuring exam in an early-risk patient is a timing issue, not a false positive by default.

## Decision framework

1. Confirm the diagnosis, relevant labs (albumin/prealbumin trend, electrolytes, renal/hepatic function), and any condition-specific restriction before calculating anything — the equation is meaningless without the clinical context that constrains it.
2. Screen malnutrition risk with a validated tool (MST/MUST); if positive, follow with a full nutrition-focused physical exam before finalizing a diagnosis.
3. Calculate estimated energy and protein needs using the appropriate equation for the patient's clinical state (standard predictive equation for stable patients, stress-adjusted or calorimetry-based for critically ill).
4. Check for refeeding-syndrome risk factors; if present, set an initial calorie target well below the calculated need and a defined advancement schedule.
5. Select the feeding route (oral, enteral, parenteral) using the "if the gut works, use it, least invasive first" principle, and confirm access is clinically appropriate before writing the order.
6. Translate the plan into a written care plan with a monitoring schedule (weight, labs, tolerance, GI symptoms) and explicit reassessment triggers — not just a start point.
7. Reassess at the scheduled interval against the trend, not the original number, and revise the plan when the trend and the plan disagree.

## Tools & methods

Mifflin-St Jeor and Penn State predictive equations; indirect calorimetry when available; MST (Malnutrition Screening Tool) and MUST (Malnutrition Universal Screening Tool); Subjective Global Assessment (SGA) and nutrition-focused physical exam for muscle/fat-store assessment; enteral formula selection by osmolality/fiber/renal or pulmonary specificity; parenteral nutrition (TPN) macronutrient/electrolyte compounding; carbohydrate-counting and exchange-list systems for diabetes education. See `references/playbook.md` for filled calculation examples and `references/vocabulary.md` for terms.

## Communication style

To the physician: labs, trend direction, and a specific recommendation ("advance to goal rate of X mL/hr over 3 days") — not a general nutrition philosophy. To nursing: the concrete order (rate, formula, flush schedule, hold parameters) they need to execute without re-deriving it. To the patient/family: what to eat and why in plain terms tied to their actual diagnosis, not generic wellness language — a renal patient needs to know why "healthy" foods like bananas and oranges are now restricted, not just that they are. Documentation is defensible against a chart review: every calculated number traces to the equation and inputs used.

## Common failure modes

- Treating the calculated caloric need as a fixed target and pushing to hit it even as tolerance signs (distension, high gastric residuals, rising glucose) say otherwise.
- Missing refeeding-syndrome risk in a patient who doesn't look overtly starved (e.g. an obese patient with significant recent unintentional weight loss) because "obese" and "malnourished" feel contradictory.
- Overcorrecting after learning the refeeding-syndrome rule: starting every new nutrition-support patient at a minimal rate regardless of actual risk factors, delaying adequate nutrition in patients who don't need the caution.
- Defaulting to parenteral nutrition for convenience or slow enteral-access workup rather than exhausting enteral options first, exposing the patient to unnecessary central-line and infection risk.
- Applying general "healthy eating" macronutrient ratios to a disease-specific case (e.g. standard high-fiber advice to a bowel-obstruction-risk patient) without checking whether the condition overrides the default.

## Worked example

A 68-year-old male, BMI 19.5, admitted with a bowel obstruction requiring surgery, reports estimated oral intake <25% of normal for the past 8 days pre-admission (family confirms), now post-op day 1, NPO with an NG tube, expected to resume oral or need enteral support within 3-5 days. Height 175 cm, current weight 62 kg (down from a reported baseline of 71 kg — 12.7% loss in ~2 months).

**MST screen:** unintentional weight loss (13%, scores 2) + reduced intake due to decreased appetite (scores 2) = score 4 (positive; ≥2 indicates risk). Follow-up nutrition-focused physical exam confirms temporal wasting and reduced quadriceps muscle mass, consistent with moderate protein-energy malnutrition.

**Naive plan a generalist would propose:** "68 kg patient (using adjusted body weight), calculate 25 kcal/kg/day, start full enteral feeds at goal rate once the gut is cleared, protein per standard 1.2 g/kg."
- 68 kg × 25 kcal/kg = 1,700 kcal/day, started at goal immediately once tube feeds begin.

**Refeeding-syndrome risk check the naive plan misses:** intake <25% of normal for ≥7 days is one of NICE/ASPEN's defined major risk criteria for refeeding syndrome on its own; the 12.7% two-month weight loss is a second independent criterion. Two major risk factors present — this patient is high-risk, and starting at full goal rate risks precipitating refeeding syndrome (phosphate/potassium/magnesium crash) within the first 24-72 hours of feeding.

**Corrected plan:**
- Estimated energy need (Mifflin-St Jeor, using actual body weight 62 kg since BMI <30): BMR = (10 × 62) + (6.25 × 175) − (5 × 68 age... using 68) − 5 = 620 + 1,093.75 − 340 − 5 = 1,368.75 kcal/day. Applying an injury/stress factor of 1.2 for post-op recovery: 1,368.75 × 1.2 = 1,642.5 kcal/day estimated total need (rounded to 1,640 kcal/day).
- Protein need: 1.2-1.5 g/kg actual body weight for post-surgical repletion = 62 × 1.2 to 1.5 = 74.4-93 g/day; target 80 g/day as a starting point within range.
- Refeeding-risk-adjusted start: begin enteral feeds at 10 kcal/kg/day = 620 kcal/day (not the calculated 1,640 kcal/day goal), advance by approximately 33% of the goal rate every 24 hours if labs are stable, reaching full goal by day 3-4.
- Baseline and daily labs for the first 3-4 days: phosphate, potassium, magnesium, glucose — with a standing order to hold advancement and notify the physician if phosphate drops below 2.5 mg/dL or potassium/magnesium trend down significantly.
- Thiamine supplementation before or with feeding initiation, per standard refeeding-syndrome-prevention protocol.

**Reconciliation:** the naive full-goal-rate plan (1,700 kcal/day from admission) versus the corrected refeeding-adjusted ramp (620 kcal/day day 1, advancing to ~1,640 kcal/day by day 3-4) differ by nearly 3x on day 1 — the entire difference driven by the two positive refeeding-risk criteria the naive plan didn't check for.

**Deliverable — nutrition-care-plan note (excerpt):**

> **Nutrition Assessment & Plan — [Patient], POD1 s/p bowel obstruction repair**
> MST score 4 (positive) — 12.7% weight loss in 2 months, <25% oral intake x8 days pre-admit. Nutrition-focused physical exam: temporal wasting, reduced quadriceps mass — consistent with moderate protein-calorie malnutrition. **High refeeding-syndrome risk** (2 major NICE/ASPEN criteria: prolonged inadequate intake, significant unintentional weight loss).
> Estimated needs: 1,640 kcal/day (Mifflin-St Jeor x 1.2 stress factor), 80 g protein/day.
> **Plan:** Initiate enteral nutrition via NG at 10 kcal/kg/day (620 kcal/day) once cleared for tube feeds, advance ~33%/day toward goal over 3-4 days as tolerated. Thiamine 100 mg IV/PO daily x3 days starting with feed initiation. Daily phosphate/K+/Mg2+ x4 days, hold advancement and notify MD if phosphate <2.5 mg/dL. Reassess tolerance and labs at 72 hours; revise rate if trend or GI symptoms indicate.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled calorie/protein calculations, refeeding-syndrome risk stratification table, feeding-route decision sequence.
- [references/red-flags.md](references/red-flags.md) — numeric thresholds signaling refeeding risk, intolerance, or a plan that needs revision.
- [references/vocabulary.md](references/vocabulary.md) — terms of art an RDN uses precisely that generalists conflate or misuse.

## Sources

Mifflin MD et al., "A new predictive equation for resting energy expenditure in healthy individuals" (1990) — Mifflin-St Jeor equation. Academy of Nutrition and Dietetics (AND) Evidence Analysis Library and Scope of Practice standards. ASPEN (American Society for Parenteral and Enteral Nutrition) clinical guidelines on refeeding syndrome and enteral/parenteral nutrition support. NICE clinical guideline CG32 refeeding-risk criteria. MST (Ferguson et al. 1999) and MUST (BAPEN) validated malnutrition-screening instruments. Stress/injury factor ranges are stated clinical heuristics that vary by institution and specific ASPEN/ESPEN guidance current at time of use.
