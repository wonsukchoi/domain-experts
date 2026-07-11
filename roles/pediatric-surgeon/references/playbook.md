# Pediatric surgery playbook

Filled decision tables for the recurring time-sensitive calls. Use alongside SKILL.md's decision framework, not instead of it.

## Bilious vomiting by age band

| Age | Default working diagnosis | First test | Time budget |
|---|---|---|---|
| 0–7 days | Malrotation/volvulus, duodenal/jejunal atresia, meconium ileus | Emergent upper GI contrast series | Hours, not a shift — call radiology directly |
| 1–4 weeks | Malrotation/volvulus (still the must-rule-out), Hirschsprung's enterocolitis | Emergent upper GI series; abdominal film first if distended | Hours |
| 1 month–2 years | Intussusception, malrotation (less common but still active), incarcerated hernia | Ultrasound (target sign for intussusception) then upper GI if negative | Same-visit |
| >2 years | Adhesive obstruction (if prior surgery), malrotation presenting late (rare) | Abdominal film, CT if prior surgical history | Same-visit, less emergent absent distension/peritonism |

## NEC / Bell staging management table

| Stage | Findings | Management | Reassess |
|---|---|---|---|
| IA/IB (suspected) | Nonspecific signs (temp instability, apnea, mild distension); normal or nonspecific film | NPO, decompression, antibiotics considered, serial exam | q6–8h film + exam |
| IIA (definite, mild) | Pneumatosis intestinalis on film | NPO 7–10 days, IV antibiotics, serial films q6–8h, trend platelets/lactate | Any exam change → escalate stage |
| IIB (definite, moderate) | Pneumatosis + portal venous gas +/- mild acidosis/thrombocytopenia | Same as IIA plus closer hemodynamic monitoring; surgical consult standing | Platelet drop >50% in 12h or lactate >4 mmol/L → treat as impending IIIA |
| IIIA (advanced, intact bowel) | Severe illness, acidosis, DIC, bowel intact | ICU-level support, surgical consult at bedside, laparotomy if deteriorating despite max support | Continuous |
| IIIB (advanced, perforated) | Pneumoperitoneum on film | Laparotomy (or primary peritoneal drainage if <~1000g/unstable), source control | N/A — operative |

**Weight-based fork:** below roughly 1000g and hemodynamically unstable, default to bedside primary peritoneal drainage as a first move — in the NEST trial cohort, drainage and laparotomy produced statistically similar 90-day mortality and neurodevelopmental outcomes in extremely low birth weight infants, so drainage is a legitimate definitive option, not only a bridge.

## Pediatric Appendicitis Score (PAS) breakdown

| Component | Points |
|---|---|
| Migration of pain to RLQ | 1 |
| Anorexia | 1 |
| Nausea/vomiting | 1 |
| RLQ tenderness | 2 |
| Cough/percussion/hopping tenderness | 2 |
| Fever ≥38.0°C | 1 |
| Leukocytosis (WBC >10,000) | 1 |
| Neutrophilia (ANC/left shift) | 1 |
| **Total** | **10** |

- **≥7:** high probability — proceed to OR without further imaging in a classic presentation.
- **3–6:** equivocal — ultrasound first (CT reserved for non-diagnostic ultrasound with ongoing concern).
- **≤2:** low probability — reassess, consider discharge with return precautions if exam is reassuring.

## Testicular torsion: salvage vs. time-from-onset

| Hours from symptom onset | Approximate salvage rate | Action |
|---|---|---|
| 0–6h | ~90–100% | Go straight to OR on clinical grounds if Doppler would delay more than ~60–90 minutes |
| 6–12h | ~50–70% | Still emergent; do not wait on a full radiology read if exam is convincing |
| 12–24h | ~20–50% | Emergent exploration regardless — even a low-probability salvage is worth the attempt |
| >24h | <10% | Exploration still indicated (contralateral fixation at minimum), consent conversation includes likely orchiectomy |

## CDH / ECMO decision table

| Signal | Threshold | Action |
|---|---|---|
| Oxygenation index (OI), sustained trend | ~25–40 despite optimized ventilation | Initiate ECMO evaluation before considering repair |
| Repair timing relative to ECMO | — | Default to deferring anatomic repair until after decannulation/stabilization, not before or during early ECMO run, unless the center's protocol specifies on-ECMO repair |
| Pre-/post-ductal saturation gap | Persistent gap despite vent optimization | Escalate PPHN-directed therapy (iNO, sildenafil) before assuming the anatomic repair itself will resolve gas exchange |

## Gastroschisis closure decision

1. **At delivery:** bowel inspected for color, edema, and matting/peel.
2. **If bowel is pink, minimally edematous, no peel:** attempt bedside or OR primary reduction and closure within the first hours of life.
3. **If bowel is edematous, matted, or abdominal domain is clearly insufficient:** place a preformed silo, begin gravity-assisted reduction, targeting full reduction over roughly 5–7 days.
4. **Fallback ladder if reduction stalls:** continue silo reduction with serial tightening → surgical closure once domain allows → flap/prosthetic closure only if primary fascial closure remains unsafe after staged reduction.
5. **Never force primary closure against rising peak inspiratory pressure or bladder pressure** — abdominal compartment syndrome from an over-tight closure is a worse outcome than a longer staged course.
