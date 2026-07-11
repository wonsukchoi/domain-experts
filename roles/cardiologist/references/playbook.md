# Playbook

Filled protocols with real thresholds. These reflect ACC/AHA-framework defaults — deviate consciously for local protocol, formulary, or patient-specific factors, and document why.

## 1. Acute chest pain risk stratification (HEART + hs-troponin)

### HEART score components (0-2 points each, max 10)

| Component | 0 points | 1 point | 2 points |
|---|---|---|---|
| History | Slightly suspicious | Moderately suspicious | Highly suspicious |
| ECG | Normal | Nonspecific repolarization disturbance | Significant ST depression |
| Age | <45 | 45-65 | >65 |
| Risk factors | None | 1-2 | ≥3, or known atherosclerotic disease |
| Troponin | ≤ normal limit | 1-3x normal limit | >3x normal limit |

**Disposition by tier:**
- **0-3 (low, ~1.7% 6-week MACE):** discharge with outpatient follow-up in 1-2 weeks; no further testing required if two troponins 3h apart are negative.
- **4-6 (intermediate, ~12-17% 6-week MACE):** admit to observation; same-admission stress echo or coronary CTA before discharge (HEART Pathway protocol) — do not defer to an outpatient slot.
- **≥7 (high, ~50-65% 6-week MACE):** admit, early invasive strategy (angiography within 24h), do not wait on non-invasive testing.

### hs-troponin 0/3h rule-out (assay 99th-percentile URL ~14 ng/L men, ~10 ng/L women — confirm local assay cutoff)

1. Draw at presentation and at 3 hours.
2. Both values ≤ URL and delta <3 ng/L → MI excluded per 4th Universal Definition; proceed to HEART tier disposition above.
3. Either value >URL, or delta ≥3-5 ng/L → treat as troponin-positive; determine type 1 (plaque rupture — ACS pathway) vs. type 2 (supply-demand mismatch — treat the precipitant: sepsis, tachyarrhythmia, GI bleed, hypertensive emergency, PE) before committing to dual antiplatelet therapy.
4. If a faster 0/1h protocol is validated locally, substitute per institutional assay — thresholds differ by manufacturer; never apply another lab's 0/1h cutoffs to a different assay.

## 2. Heart failure with reduced EF — four-pillar GDMT titration

Target: all four classes at target or maximum-tolerated dose within 4-6 weeks of diagnosis in a hemodynamically stable outpatient, not sequential completion of one class before starting the next.

| Class | Example agent | Starting dose | Target dose | Titration interval | Hold if |
|---|---|---|---|---|---|
| ARNI (preferred) or ACEi/ARB | Sacubitril-valsartan | 24/26 mg BID | 97/103 mg BID | 2-4 weeks | SBP <100, eGFR <30 acutely, K+ >5.5 |
| Evidence-based beta-blocker | Carvedilol | 3.125 mg BID | 25-50 mg BID (weight-based) | 2 weeks | HR <50, SBP <90 symptomatic, decompensated HF |
| MRA | Spironolactone | 12.5-25 mg daily | 25-50 mg daily | 4 weeks | K+ >5.0, eGFR <30 |
| SGLT2i | Dapagliflozin | 10 mg daily (start dose = target dose) | 10 mg daily | N/A — no titration | eGFR <20 (varies by agent), recurrent genital infections |

**Sequencing rule:** start all four at low/label dose within the first 1-2 visits if the patient is stable (SBP ≥100, no acute decompensation); uptitrate ARNI and beta-blocker every 2 weeks as tolerated. Do not wait for beta-blocker max dose before starting MRA and SGLT2i — parallel initiation is the 2022 guideline's explicit correction to the older sequential model.

**Discontinuation threshold check before stopping any pillar:** K+ >5.5 (not 5.0-5.4 — adjust MRA dose first), symptomatic hypotension (not an asymptomatic SBP of 95), or a rising creatinine that's stabilized within 30% of baseline (expected with ARNI/ACEi, not a stop signal alone).

## 3. Atrial fibrillation — anticoagulation decision

### CHA₂DS₂-VASc (stroke risk)

| Factor | Points |
|---|---|
| CHF/LV dysfunction | 1 |
| Hypertension | 1 |
| Age ≥75 | 2 |
| Diabetes | 1 |
| Stroke/TIA/thromboembolism history | 2 |
| Vascular disease (MI, PAD, aortic plaque) | 1 |
| Age 65-74 | 1 |
| Sex category (female) | 1 |

**Decision:** score ≥2 (men) or ≥3 (women, i.e., ≥2 excluding the sex point) → anticoagulate, direct oral anticoagulant (DOAC) preferred over warfarin absent mechanical valve or moderate-severe mitral stenosis. Score of 1 (men) / 2 (women, sex-point-only) → anticoagulation reasonable, shared decision. Score 0 (men) / 1 (women, sex-point-only) → no anticoagulation.

### HAS-BLED (bleeding risk — identifies what to fix, not a veto)

| Factor | Points |
|---|---|
| Hypertension (uncontrolled) | 1 |
| Abnormal renal/liver function | 1 each |
| Stroke history | 1 |
| Bleeding history/predisposition | 1 |
| Labile INR | 1 |
| Elderly (>65) | 1 |
| Drugs (antiplatelet/NSAID) or alcohol | 1 each |

Score ≥3: do not withhold anticoagulation — fix the modifiable factor first (control BP, switch NSAID, target INR time-in-range if on warfarin, or move to a DOAC) and recheck the CHA₂DS₂-VASc/HAS-BLED balance after the fix.

## 4. STEMI activation timeline

- **Door-to-ECG:** ≤10 minutes from arrival.
- **Door-to-balloon (primary PCI-capable center):** ≤90 minutes; ≤120 minutes total ischemic time if transfer required from a non-PCI center.
- **Fibrinolysis (if PCI unavailable within 120 min of first medical contact):** door-to-needle ≤30 minutes.
- Activate the cath lab from the ECG, not after a cardiology consult — "activate first, confirm in parallel" is the Mission: Lifeline default; a delay waiting for a formal cardiology read is a process failure, not caution.

## 5. DAPT duration after PCI for ACS

Default: aspirin + P2Y12 inhibitor (ticagrelor or prasugrel preferred over clopidogrel absent a contraindication) for **12 months** post-ACS.

**Shorten to 1-3 months (P2Y12 monotherapy thereafter) when:** high bleeding risk (ARC-HBR criteria — e.g., anemia <11 g/dL, oral anticoagulant co-therapy, prior intracranial hemorrhage, thrombocytopenia) — supported by TWILIGHT and T-PASS trial data on ticagrelor monotherapy after a short DAPT run-in.

**Extend beyond 12 months when:** high ischemic risk and low bleeding risk (prior MI, diffuse multivessel disease, diabetes with prior stent thrombosis) — per PEGASUS-TIMI 54, low-dose ticagrelor extension reduced recurrent ischemic events at the cost of measurably higher (but mostly non-fatal) bleeding; the extension decision is a documented risk-tradeoff conversation with the patient, not a default renewal.

## 6. Stable angina — invasive vs. medical strategy gate

1. **High-risk anatomy present** (left main ≥50%, proximal LAD with reduced EF, three-vessel disease with reduced EF, refractory symptoms despite two anti-anginal classes)? → Heart Team referral for revascularization.
2. **None of the above, EF preserved, symptoms tolerable on medical therapy?** → optimal medical therapy first (per ISCHEMIA): antiplatelet, statin to target, beta-blocker or calcium-channel blocker, ACEi if indicated, risk-factor control.
3. **Symptoms remain limiting after OMT trial (4-6 weeks at maximally tolerated doses)?** → stress imaging or FFR-guided angiography; treat physiologically significant lesions (FFR ≤0.80) for symptom relief — document explicitly that the goal is symptom relief, not mortality reduction, unless high-risk anatomy from step 1 applies.
