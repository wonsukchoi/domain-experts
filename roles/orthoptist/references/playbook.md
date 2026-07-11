# Playbook — sensorimotor exam sequencing, amblyopia dosing, referral notes

Filled procedures an agent can execute or populate, not descriptions of them.

## 1. New-presentation sensorimotor workup sequence

| Step | Action | Threshold / decision rule |
|---|---|---|
| 1 | Red-flag screen | Leukocoria, sudden acquired esotropia + headache/vomiting (child >6y), painful restricted motility post-trauma, acute diplopia → same-visit ophthalmology referral, workup pauses |
| 2 | Cycloplegic refraction | Full cycloplegic refraction obtained before any acuity is judged "amblyopic" — an uncorrected refractive error can masquerade as amblyopia |
| 3 | Best-corrected visual acuity, each eye | Interocular gap ≥2 lines (0.2 logMAR) = amblyopia; classify severity (below) |
| 4 | Alignment: cover/uncover, alternate cover, prism cover | Distance AND near, WITH and WITHOUT habitual correction; record PD magnitude + base direction each condition |
| 5 | Versions/ductions grading | Grade each extraocular muscle action −4 (max underaction) to +4 (max overaction); any asymmetry between eyes on any single muscle = incomitant, escalate to Hess/Lees |
| 6 | Sensory testing | Worth 4-dot (suppression/diplopia/ARC), stereoacuity (arcsec), synoptophore if incomitant or angle/sensory discordance suspected |
| 7 | Match to pathway | Use severity/age table (below) — most conservative fitting option first |

## 2. Amblyopia severity and dosing table (PEDIG-informed)

| Severity | BCVA (worse eye) | First-line Rx | Adequate-trial duration | Escalation trigger |
|---|---|---|---|---|
| Mild | 20/25–20/40 | Refractive correction alone, recheck 8–12wk | 8–12wk | No improvement on correction alone → add occlusion 2h/day |
| Moderate | 20/40–20/80 | Occlusion 2h/day (or atropine penalization 1x weekend day equivalent) + correction | 12–16wk, ODM/diary-verified dose ≥75% of Rx | No BCVA gain at ≥75% verified dose → step to 6h/day |
| Severe | 20/100 or worse | Occlusion 6h/day (up to full-time waking hours in select cases) + correction | 12–16wk, ODM/diary-verified dose ≥75% of Rx | No BCVA gain at ≥75% verified dose → re-audit diagnosis, consider deprivation cause, ophthalmology re-referral |

**Compliance-first escalation rule:** at any tier, if follow-up ODM/diary shows delivered dose <75% of prescribed hours, the visit outcome is a compliance intervention and dose re-verification at 4 weeks — not a tier escalation. Escalate only after a verified-adequate trial (≥75% of Rx for the full duration) shows no acuity gain.

**Worked dose check (from the SKILL.md example):** Rx 2h/day (120 min) x 56 days = 6,720 min prescribed. ODM-measured 45 min/day x 56 days = 2,520 min delivered → 2,520 / 6,720 = 37.5% of prescribed dose. Below the 75% verification threshold — treat as under-dosed, not a failed trial.

## 3. Convergence insufficiency diagnosis and therapy (CITT-informed)

| Finding | Normal | Abnormal (CI likely) |
|---|---|---|
| Near point of convergence (NPC), break | ≤6cm | >6cm |
| NPC, recovery | ≤10cm | >10cm |
| Positive fusional vergence at near, break | ≥15–20 PD | Reduced, symptomatic |
| Symptom score (e.g., CISS) | <16 | ≥16 (adult), ≥20 (child/teen norm varies by instrument version) |

**First-line therapy sequence:** home-based pencil push-ups (base regimen) → if no improvement at 6–8 weeks or symptom score unchanged, escalate to office-based vergence/accommodative therapy with home reinforcement (CITT's higher-efficacy arm) before considering prism or surgery.

## 4. Incomitance grading and Hess/Lees documentation

Versions graded on a −4 to +4 scale per extraocular muscle; a Hess/Lees chart plot is indicated (not routine) when:
- Any single-muscle grading shows R/L asymmetry ≥1 grade, or
- History suggests acquired/paretic/restrictive cause (trauma, thyroid eye disease, cranial nerve palsy), or
- Serial tracking of a known incomitant deviation is needed (e.g., quarterly thyroid eye disease monitoring)

**Filled example (right superior oblique underaction suspected):**

| Muscle | OD grading | OS grading | Interpretation |
|---|---|---|---|
| Right inferior oblique | +2 | — | Overaction, consistent with ipsilateral SO palsy pattern |
| Right superior oblique | −2 | — | Underaction |
| Left superior rectus | — | 0 | No overaction (rules out contralateral SR restriction as sole cause) |

## 5. Stereoacuity interpretation (Titmus/Randot, arcsec)

| Result | Interpretation |
|---|---|
| ≤40 arcsec | Normal fine stereopsis |
| 50–100 arcsec | Reduced but functional stereopsis — consistent with small-angle or intermittent deviation |
| ≥400 arcsec or gross only (fly test) | Suppression or microtropia likely — check Worth 4-dot and cover test for a small residual angle before accepting "no measurable deviation" |
| Untestable (age/cooperation) | Record fallback method used (Bruckner, alternate-cover recovery speed) and confidence level — never chart as "normal" by default |

## 6. Referral / handoff note skeleton (fill, don't describe)

```
ORTHOPTIC REFERRAL / SURGICAL DOSING NOTE
Diagnosis: [e.g., constant comitant esotropia, right eye]
Angle (distance, with correction): [___ PD, base ___]
Angle (near, with correction): [___ PD, base ___]
Comitance: [comitant / incomitant — if incomitant, attach Hess/Lees plot]
Sensory status: [stereoacuity ___ arcsec; suppression/ARC via Worth 4-dot: ___]
Amblyopia status: [BCVA OD/OS; severity tier; verified compliance %, if on active Rx]
Recommendation: [continue current Rx / escalate tier / surgical referral with above angle]
Follow-up: [interval, and what trigger prompts earlier contact]
```
