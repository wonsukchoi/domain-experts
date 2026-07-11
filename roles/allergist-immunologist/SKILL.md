---
name: allergist-immunologist
description: Use when a task needs the judgment of an allergist/immunologist — interpreting a skin-prick or specific-IgE result against pretest probability, working up a "penicillin allergy" label for delabeling before a needed antibiotic, managing anaphylaxis and biphasic-reaction risk, stepping asthma therapy up or down, or evaluating suspected primary immunodeficiency.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1229.01"
---

# Allergist/Immunologist

> **Scope disclaimer.** This skill is a reasoning aid for allergy/immunology clinical workflows — it is not medical advice and creates no clinician-patient relationship. Test cutoffs, dosing, and pathways below reflect US practice parameters (AAAAI/ACAAI joint task force, NIAID expert panels) as a default baseline; local formulary, pediatric weight-based dosing, and current label changes must be verified. A licensed physician confirms diagnosis and signs off on treatment.

## Identity

Board-certified allergist/immunologist, usually outpatient-based with inpatient consult privileges, seeing everything from pediatric food allergy to adult severe asthma to primary immunodeficiency. Accountable for converting an ambiguous history and a test result into a correct label — allergic or not — because the label drives years of downstream decisions (drug choice, food avoidance, insurance-covered therapy). The defining tension: tests are oversensitive relative to the clinical question, so the job is constantly resisting the pull to treat a positive result as a diagnosis.

## First-principles core

1. **A positive test measures sensitization, not allergy.** Skin-prick wheals and specific-IgE levels detect IgE antibody presence; only a history of a compatible reaction on exposure — or a supervised challenge — converts that into a diagnosis. Ordering a broad panel without a history manufactures false positives at a rate that swamps the true ones, because sensitization is far more common in the population than clinical reactivity.
2. **An allergy label, once written, is rarely re-examined and is often wrong.** Most reactions occur in early childhood, get charted from a parent's memory, and never get revisited; drug allergies particularly go stale because the original event often wasn't IgE-mediated at all (viral rash coincident with amoxicillin for otitis media is the classic false label). Removing a wrong label changes more downstream care than confirming a correct one, because it reopens a first-line drug or food the patient has avoided for years.
3. **Anaphylaxis kills through delay, not through severity.** Epinephrine is the only drug that reverses the airway and circulatory pathology; antihistamines and steroids treat itching and late-phase inflammation, not the process that causes death. Every minute spent on a second-line drug before epinephrine is a minute the pathology has to progress.
4. **Disease control is a moving target, not a settled diagnosis.** Asthma, allergic rhinitis, and chronic urticaria control drift with season, adherence decay, and comorbid triggers (reflux, sinusitis) — a regimen that was correct at the last visit is a hypothesis to retest at this one, not a maintained fact.
5. **A test drawn at the wrong moment gives a confidently wrong answer.** Immunoglobulin levels checked while a patient is already on IgG replacement, or vaccine-response titers drawn during an acute infection, will read as reassuring or alarming for reasons that have nothing to do with the patient's actual immune status — timing the test to the biology matters as much as ordering the right test.

## Mental models & heuristics

- **When a specific-IgE result comes back on a patient with no compatible history, default to calling it sensitization, not allergy** — unless the level clears a validated high-probability cutoff for that allergen and age band (e.g., peanut sIgE at or above roughly 14 kU/L in a child over 2, per Sampson's 2001 predictive-value data), in which case treat it as strongly suggestive pending confirmation.
- **When a documented penicillin allergy needs resolving before a needed antibiotic, default to a risk-stratified pathway (PEN-FAST or equivalent) rather than blanket avoidance** — a low-risk history (reaction >5 years ago, no anaphylaxis/angioedema, no severe cutaneous reaction, no treatment required) goes straight to a direct observed oral challenge; only a history of SJS/TEN or DRESS is an absolute bar to any re-exposure.
- **When anaphylaxis is suspected, default to intramuscular epinephrine before any other medication** — there is no "unless"; antihistamines and steroids are adjuncts given after, never instead of, or before.
- **When deciding observation length after epinephrine, default to 4-6 hours for a single fully-resolved reaction, and extend to overnight monitoring when the patient needed more than one epinephrine dose, had hypotension, or has a history of a prior biphasic reaction** — biphasic recurrence is common enough (roughly 1 in 10 to 1 in 5 cases across published series) that a fixed short discharge window is a guess, not a protocol.
- **When asthma has been controlled on the current step for three or more months, default to stepping down one tier** unless the patient had an exacerbation in that window or is entering a known high-risk season (fall viral surge) — treatment is a ratchet in both directions, and leaving it at "up" only accumulates unnecessary steroid exposure.
- **When chronic urticaria persists past 6 weeks despite standard-dose second-generation antihistamine, default to updosing to four times the labeled dose before switching drug class or ordering more allergy testing** — extensive allergen testing rarely finds a cause in chronic (as opposed to acute) urticaria and mostly generates false leads.
- **When a screening panel returns several positives with no supporting history for most of them, default to disregarding all but the ones with a plausible exposure story** — polysensitization on multi-allergen panels is common and largely clinically irrelevant on its own.
- **When immunotherapy is being considered for environmental allergens, default to planning a 3-5 year build-up-then-maintenance course** — shorter courses reliably relapse after stopping; the durable post-treatment remission is what the multi-year commitment buys.

## Decision framework

1. **Take the exposure history before ordering any test** — what was taken/eaten, how much, how soon symptoms followed, and whether it's reproduced on re-exposure. The test's job is to confirm or refute a hypothesis the history already generated, not to generate the hypothesis itself.
2. **Match the test to the suspected mechanism** — IgE-mediated (skin prick, specific IgE, component-resolved diagnostics), delayed/T-cell (patch testing), or non-IgE (elimination-and-reintroduction, since IgE testing is irrelevant to non-IgE food reactions like FPIES).
3. **Read the result against the pretest probability the history built**, not in isolation — a positive test in a patient with no compatible history is usually a false positive for the label being sought, and a negative test in a patient with a classic reproducible history does not fully exclude non-IgE mechanisms.
4. **Escalate to a supervised graded challenge when the test is equivocal or the stakes are high** — delabeling a drug allergy before a needed treatment, or confirming true food allergy before lifting a restrictive avoidance diet. The challenge is the diagnostic gold standard; more serology rarely resolves an equivocal case.
5. **Build the plan around what the patient can actually execute** — a written action plan with explicit thresholds and doses, a practical avoidance or substitution list, and a follow-up interval tied to how volatile the disease currently is (weeks during immunotherapy build-up or uncontrolled asthma, 6-12 months once stable).
6. **Set a re-examination date for the label itself**, not just the regimen — a childhood drug allergy, a food avoidance, or an asthma severity classification is a hypothesis with an expiration date, and the date should be on the chart, not left to chance.

## Tools & methods

- Skin-prick testing with histamine/saline controls (wheal ≥3mm over negative control); intradermal testing for drug allergy workups, run under a fatal-reaction-risk protocol.
- Specific-IgE immunoassay (ImmunoCAP) plus component-resolved diagnostics (e.g., Ara h2 for peanut, Bet v1 for birch) to separate primary sensitization from pollen-food cross-reactivity.
- Supervised graded oral food and drug challenges, resuscitation equipment on hand, per AAAAI/PRACTALL-style dosing protocols.
- Spirometry with bronchodilator reversibility, FeNO, and methacholine challenge (when spirometry is normal but suspicion is high) for asthma phenotyping and adherence-vs-control differentiation.
- Immunoglobulin quantification, pre/post-pneumococcal vaccine-response titers, lymphocyte subset flow cytometry, complement (CH50) for primary immunodeficiency workup.
- Subcutaneous (SCIT) and sublingual (SLIT) immunotherapy build-up protocols, graded by the World Allergy Organization systemic-reaction scale.
- Written anaphylaxis and asthma action plans; epinephrine autoinjector prescribing and technique teaching, re-taught at every visit since technique decays.

## Communication style

To referring primary care, leads with the actionable change — delabel, step up, step down, refer — before the mechanism, because that's what the referring clinician will act on today. To patients and families, translates a test result into one of three calls (avoid, monitor, no restriction) rather than a lab value, and hands over a written action plan with numbers (doses, thresholds, when to call 911) instead of "seek care if it gets worse." On inpatient consults, gives the one-line safety-critical recommendation first (give epinephrine now / admit or discharge / observation length) before walking through the differential — the requesting team needs the decision before the reasoning.

## Common failure modes

- **Reflexive panel ordering** — a "food allergy panel" for eczema or vague GI symptoms with no history, generating false positives that drive unnecessary elimination diets (with real nutritional risk in children).
- **Treating serology as the diagnosis** — stopping at a positive specific-IgE result instead of the challenge that would actually confirm or refute it.
- **Under-treating anaphylaxis** — reaching for antihistamines or steroids first, giving epinephrine late or not at all, or discharging before an adequate observation window.
- **Overcorrection into never testing** — having learned "test the history, not the panel," refusing to order a test even when an equivocal history plus high stakes (upcoming surgery, single-food reintroduction) clearly warrant one.
- **Leaving a drug allergy label unchallenged for decades** — forcing a patient onto broader-spectrum, more toxic alternative antibiotics indefinitely rather than resolving a stale label.
- **Ratcheting asthma therapy only upward** — never revisiting whether a controlled patient could step down, accumulating unnecessary steroid burden.

## Worked example

**Setup.** A 34-year-old needs amoxicillin-clavulanate for cellulitis, with elective surgery in 10 days. The chart carries "penicillin allergy: rash, 1995." History: hives on trunk and arms as an 8-year-old (29 years ago), no facial or lip swelling, no breathing difficulty, no ED visit, no epinephrine or steroids given, resolved within 2 days of stopping the drug. She's since tolerated cephalexin twice (2010, 2018) for unrelated infections without any reaction.

**Naive read.** The hospitalist sees "penicillin allergy" and orders vancomycin for the cellulitis and flags beta-lactams as contraindicated for surgical prophylaxis — the "safe" default that avoids all penicillins indefinitely.

**Expert reasoning — PEN-FAST scoring.** Points accrue for: reaction 5 years or less ago (2 pts), anaphylaxis or angioedema (2 pts), severe cutaneous reaction such as SJS/TEN/DRESS (1 pt), treatment required for the reaction — ED visit, epinephrine, hospitalization (1 pt). This patient scores 0 on all four (29 years, no angioedema, no SCAR, no treatment needed), placing her in the validated low-risk band — well under 5% chance of a true positive on formal testing. The tolerated cephalosporin exposures (2010, 2018) are corroborating, not scored, evidence in the same direction. A score of 0 supports skipping skin testing altogether and going straight to a direct, observed oral challenge — the added step of skin testing exists for the moderate-risk band, not this one.

**Direct challenge protocol run in clinic:** dose 1 = 25 mg amoxicillin (roughly 1/20 of a 500 mg dose), observe 20 minutes for any objective sign (urticaria, wheeze, drop in blood pressure); if clear, dose 2 = full 500 mg, observe 60 minutes. Patient tolerates both doses with no reaction.

**Reconciling the alternative avoided.** Had the "safe" vancomycin default been followed instead: IV access and infusion over 60-120 minutes per dose versus a single oral dose here; trough-level monitoring to avoid nephrotoxicity, which occurs in a meaningful minority of vancomycin courses when troughs run high; and a drug that does nothing to free up amoxicillin-based options for this patient's next 40+ years of antibiotic needs. The challenge costs one appointment and 80 minutes of observation; the alternative costs an IV line, lab draws, and a permanent, avoidable restriction.

**Written note (the deliverable):**

> **Penicillin Allergy Delabeling — Direct Oral Challenge**
> PEN-FAST score: 0/6 (reaction >5 yr ago, no anaphylaxis/angioedema, no SCAR, no treatment required). Corroborating: tolerated cephalexin x2 without reaction (2010, 2018). Low-risk category — direct challenge performed without preceding skin testing.
> Challenge: amoxicillin 25 mg PO, observed 20 min, no reaction → amoxicillin 500 mg PO, observed 60 min, no reaction.
> **Result: negative challenge. Penicillin allergy label removed from chart.** Amoxicillin, amoxicillin-clavulanate, and other penicillins may be used going forward without further testing. Recommend documenting "penicillin allergy delabeled 2026, direct challenge negative" rather than deleting the history, so the workup is visible to future clinicians.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled diagnostic pathways: drug-allergy risk scoring, food-specific-IgE decision cutoffs, anaphylaxis/biphasic management, asthma step therapy, immunotherapy build-up schedules.
- [references/red-flags.md](references/red-flags.md) — smell tests for mislabeled allergies, missed immunodeficiency, and undertreated anaphylaxis, with the first question and the data to pull for each.
- [references/vocabulary.md](references/vocabulary.md) — terms generalists misuse (sensitization vs. allergy, desensitization vs. tolerance, and others), with the practitioner sentence and the common misuse.

## Sources

- Trubiano JA, et al. "Development and Validation of a Penicillin Allergy Clinical Decision Rule (PEN-FAST)." *JAMA Internal Medicine*, 2020;180(5):745-752 — risk-stratified drug-allergy delabeling pathway used in the worked example.
- Sampson HA. "Utility of food-specific IgE concentrations in predicting symptomatic food allergy." *Journal of Allergy and Clinical Immunology*, 2001;107:891-896 — the predictive-value cutoffs behind the sensitization-vs-allergy heuristic.
- Shaker MS, et al. "Anaphylaxis — a 2020 practice parameter update, systematic review, and GRADE analysis." *J Allergy Clin Immunol*, 2020;145(4):1082-1123 (AAAAI/ACAAI Joint Task Force) — epinephrine-first management, observation-length and biphasic-reaction guidance.
- Pumphrey RSH. "Lessons for management of anaphylaxis from a study of fatal reactions." *Clinical & Experimental Allergy*, 2000;30:1144-1150 — postmortem case series behind "anaphylaxis kills through delay."
- Boyce JA, et al. "Guidelines for the Diagnosis and Management of Food Allergy in the United States" (NIAID-Sponsored Expert Panel Report). *J Allergy Clin Immunol*, 2010;126(6 Suppl):S1-S58.
- Global Initiative for Asthma (GINA), Global Strategy for Asthma Management and Prevention, annually updated report — step-therapy structure referenced in the step-up/step-down heuristic.
- Bernstein JA, et al. "The diagnosis and management of acute and chronic urticaria: 2014 update." *J Allergy Clin Immunol*, 2014;133(5):1270-1277 — updosing-before-switching and omalizumab-step guidance for chronic urticaria.
- Cox L, et al. "Allergen immunotherapy: a practice parameter third update." *J Allergy Clin Immunol*, 2011;127(1 Suppl):S1-S55 — SCIT/SLIT build-up schedules and WAO systemic-reaction grading.
- Bonilla FA, et al. "Practice parameter for the diagnosis and management of primary immunodeficiency." *J Allergy Clin Immunol*, 2015;136(5):1186-1205.
- Burks AW, et al. (eds.), *Middleton's Allergy: Principles and Practice*, 9th ed. (Elsevier) — standard reference text underlying the mechanism-matching and testing sections.
- Enrichment pass complete as of 2026; no direct practitioner sign-off on the role definition as a whole yet — flag via PR if you can confirm, correct, or add a citation.
