# Medical Assistant — Playbook

## Vitals-intake escalation reference (example practice protocol)

| Vital | Normal range | Escalation threshold | Action on threshold |
|---|---|---|---|
| Systolic BP | 90–139 mmHg | ≥160 mmHg | Stop, notify physician before continuing vitals |
| Diastolic BP | 60–89 mmHg | ≥100 mmHg | Stop, notify physician before continuing vitals |
| Pulse | 60–100 bpm | <50 or >130 bpm | Recheck manually; notify if confirmed |
| Temperature | 97.0–99.5°F | ≥101.5°F or <95.0°F | Notify physician, note associated symptoms |
| O2 saturation | ≥95% RA | <92% | Notify physician immediately, apply O2 per protocol if authorized |

These thresholds are illustrative of a typical ambulatory-care standing order — every practice sets its own, and pediatric/geriatric baselines shift the normal ranges. Confirm the practice's actual protocol before relying on any number here.

## Standing-order verification checklist (before any delegated clinical task)

1. Right patient — confirm against two identifiers (name + DOB, not name alone).
2. Right task — the standing order specifies this exact task for this visit type, not an adjacent one.
3. Right dose/route/site (if applicable) — matches the order, not a judgment call about what seems appropriate for this patient.
4. Right timing — the order's conditions for when the task applies are met (e.g., "at time of annual wellness visit," not any visit).
5. Consent/counseling completed where the practice requires it (e.g., vaccine information statement given before administration).
6. If any checklist item is uncertain — stop and ask before proceeding. Do not resolve ambiguity by inference.

## 12-lead EKG placement quick reference

| Lead | Placement |
|---|---|
| RA (right arm) | Right wrist or right shoulder, per machine convention |
| LA (left arm) | Left wrist or left shoulder, per machine convention |
| RL (right leg) | Right ankle |
| LL (left leg) | Left ankle |
| V1 | 4th intercostal space, right sternal border |
| V2 | 4th intercostal space, left sternal border |
| V3 | Midway between V2 and V4 |
| V4 | 5th intercostal space, midclavicular line |
| V5 | Same horizontal level as V4, anterior axillary line |
| V6 | Same horizontal level as V4, midaxillary line |

Reversed limb leads produce a recognizable artifact (e.g., inverted Lead I with a normal-looking Lead II is a classic RA/LA reversal signature) — if a physician flags an EKG as "doesn't look right," check placement before assuming a cardiac finding.

## Injection technique reference

| Site | Typical use | Needle length (adult) | Note |
|---|---|---|---|
| Deltoid | IM vaccines, small-volume meds | 1–1.5 inch, 22–25G | Max volume ~1mL for most adults |
| Vastus lateralis | Infants, larger-volume IM | 1 inch (infant), 1–1.5 inch (adult) | Preferred site for infants under 12 months |
| Ventrogluteal | Larger-volume IM, viscous meds | 1.5 inch, 21–23G | Avoids sciatic-nerve-injury risk of dorsogluteal |
| Subcutaneous (abdomen/upper arm) | Insulin, heparin, some vaccines | 5/8 inch, 25–27G | 45–90° angle depending on tissue thickness |

Z-track technique (displacing skin laterally before injection, releasing after withdrawal) is standard for medications that stain or irritate tissue (e.g., iron dextran) — prevents the medication from tracking back through the needle channel into subcutaneous tissue.

## Filled example: vitals-escalation intake note

See SKILL.md's Worked Example for the full quoted deliverable (Mr. Alvarez, BP 168/104, immediate-notification protocol). The structural pattern to reuse:

1. State the reason for visit.
2. State the triggering finding and the exact threshold it crossed.
3. State the action taken and the exact timestamp.
4. State remaining findings obtained after notification.
5. State any relevant patient-reported context (in patient's own words where practical).
6. State current status ("awaiting instruction," "proceeding per order," etc.).
