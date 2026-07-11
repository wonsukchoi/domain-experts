# Playbook

Filled templates and thresholds for milieu observation, escalation response, restraint monitoring, and shift handoff. Populate directly — these are working structures, not descriptions of structures.

## Observation-tier ladder

| Tier | Interval | Trigger to enter | Trigger to step down |
|---|---|---|---|
| Routine (Q30) | Every 30 min, documented location + activity | Stable, no risk flags in past 72h | N/A — unit default |
| Q15 | Every 15 min, location + affect + behavior vs. baseline | New admission (first 72h), recent risk flag resolved, post-restraint recovery | 3 consecutive shifts with no risk flag and treatment team downgrade |
| 1:1 (constant, line-of-sight) | Continuous, staff within sight/sound at all times | Brøset score ≥2, active suicidal/self-harm ideation with plan, post-restraint/seclusion release (first 4h), acute intoxication/withdrawal | RN/MD order to step down after risk reassessment — never a unilateral tech decision |
| Continuous + restraints monitoring | Continuous + vitals/circulation at facility-mandated interval (commonly q15) | Active restraint or seclusion episode | Release per face-to-face evaluation meeting criteria |

## Brøset Violence Checklist — scoring and response

6 items, each scored 0 (absent) or 1 (present) based on the *current shift's* observation, not history:

| Item | Present this shift? |
|---|---|
| Confusion (disoriented, doesn't understand instructions) | 0/1 |
| Irritability (easily annoyed, snappish) | 0/1 |
| Boisterousness (loud, overactive, restless) | 0/1 |
| Verbal threats | 0/1 |
| Physical threats (gestures, invading space) | 0/1 |
| Attacks on objects | 0/1 |

**Score → action:**

| Total | Action |
|---|---|
| 0 | Routine or Q15 tier per existing plan |
| 1 | Note in chart, re-score at next round, informal engagement |
| ≥2 | Notify RN, upgrade to 1:1, initiate proactive engagement and offer voluntary least-restrictive options before anything escalates further |
| ≥2 and rising across 2+ consecutive scorings | Treatment team review before next shift change — a rising trend without intervention is the pattern that precedes most incidents |

## Escalation-response ladder (CPI-aligned)

| Continuum stage | Patient presentation | Staff response | Escalate to next stage if |
|---|---|---|---|
| 1. Anxious | Fidgeting, pacing, voice change | Supportive: active listening, non-threatening presence, ask what's needed | No de-escalation in ~5–10 min or presentation worsens |
| 2. Defensive | Refusing direction, verbal challenge, loss of rationality | Directive: clear, simple, limited choices ("Would you like to talk in your room or the quiet room?") — offer PRN/voluntary option now | Directive approach declined and behavior intensifies |
| 3. Risk behavior / acting out | Physical aggression, property destruction, imminent danger to self or others | Team response per facility protocol — restraint/seclusion initiation, call for backup, start regulatory clocks (see below) | N/A — this stage is the safety response, not a de-escalation stage |
| 4. Tension reduction | Post-incident: crying, apologizing, exhaustion | Supportive presence, hydration/comfort, begin debrief when patient is ready — not immediately if still dysregulated | N/A |

## Restraint/seclusion clock — worked template

Fill in at initiation; keep visible to the team for the duration.

| Field | Example entry |
|---|---|
| Initiation time | 13:53 |
| Type (restraint / seclusion / both) | Seclusion |
| 1-hour face-to-face deadline (initiation + 1:00) | 14:53 |
| Age-based order window (adult = 4h from initiation) | Expires 17:53 unless renewed |
| Vitals/behavioral check interval during episode | Every 15 min |
| Release criteria (facility-specific, e.g. calm ×15 min, oriented, no imminent danger) | Calm, oriented, meets criteria |
| Actual release time | 15:10 |
| Total duration | 77 min |
| Debrief completed (Y/N, time) | Y, 15:30 |

**Age-based order window reference (adjust to current facility policy implementing 42 CFR 482.13):**

| Age | Max order duration before renewal requires new order |
|---|---|
| 18+ (adult) | 4 hours |
| 9–17 | 2 hours |
| Under 9 | 1 hour |

## PRN medication tracking — worked example

| Med | Max/24h | Given today | Remaining | Notes |
|---|---|---|---|---|
| Lorazepam 1mg PO | 4mg | 1mg @ 0800 | 3mg | Declined @ 1350 offer |
| Haloperidol 5mg IM | 10mg | 0mg | 10mg | Not given — akathisia suspected, hold pending psychiatry review, not "more antipsychotic" |

Fallback order if the first-line PRN is declined or contraindicated: (1) voluntary environmental change (quiet room, walk, phone call to support person) → (2) offered PO PRN → (3) offered IM PRN if PO declined and risk remains elevated → (4) restraint/seclusion only if imminent danger.

## Shift handoff template

```
Patient: [initials], Bed [#], Day [n] of admission
Acuity/observation tier: [Q15 / 1:1 / routine] — reason: [ ]
Last risk flag: [Brøset score / incident type], [time], [resolved how]
Meds of note: [PRN given/declined, any new dose changes in past 72h]
Pending: [face-to-face due, order expiration, scheduled reassessment]
Plan for next shift: [specific — not "continue to monitor"]
```
