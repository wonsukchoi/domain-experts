# Playbook

Filled worksheets and sequences a biomed shop actually runs — starting points to adapt to a facility's own equipment management plan, not scripts to follow blind.

## 1. Risk-scoring worksheet (AAMI EQ56-style) and PM-interval bands

Score every device 1–5 on three factors, sum to a composite (range 3–15), assign PM interval by band. Re-score whenever a recall, service bulletin, or new failure pattern touches an equipment class.

| Factor | 1 | 3 | 5 |
|---|---|---|---|
| Equipment function | Non-patient-contact (e.g. exam light) | Diagnostic/therapeutic, non-life-support (vitals monitor) | Life-support or surgical-critical (ventilator, anesthesia machine, defibrillator) |
| Physical risk (if it fails) | Inconvenience, no harm pathway | Delayed diagnosis or therapy, recoverable | Death or serious irreversible harm |
| Maintenance requirement | Simple, rarely fails, easy to verify | Moderate electromechanical complexity | Complex, calibration-sensitive, failure hard to detect without testing |

**Filled example (one shop's inventory):**

| Equipment class | Function | Physical risk | Maint. req | Composite | PM interval |
|---|---|---|---|---|---|
| Ventilator | 5 | 5 | 3 | 13 | Quarterly + post-repair verification |
| Anesthesia machine | 5 | 5 | 4 | 14 | Quarterly |
| Defibrillator/AED | 5 | 5 | 2 | 12 | Quarterly (battery + energy-delivery check) |
| Infusion pump (titrated drug) | 4 | 4 | 3 | 11 | Semiannual |
| Infusion pump (general) | 3 | 3 | 3 | 9 | Annual |
| Vital-signs monitor | 3 | 2 | 2 | 7 | Annual |
| Exam light | 1 | 1 | 1 | 3 | AEM-eligible, on-fail-only (no scheduled PM) |

**Bands (adapt to program history, don't treat as universal law):** composite ≥12 → quarterly or tighter; 8–11 → semiannual; 5–7 → annual; ≤4 → AEM-eligible run-to-failure or facility-inspection-only, subject to the exclusions in section 3.

## 2. Return-to-service checklist

Run in this order on every corrective-maintenance or PM job before a device goes back into patient use. Skipping to step 2 because step 1 "obviously" passed is the single most common shortcut that produces a later incident.

1. **Functional verification** against the device's acceptance criteria (OEM spec or facility-adopted tolerance) — e.g. infusion-rate accuracy within OEM's stated tolerance (commonly ±5%) across a spread of clinically used rates, not just one.
2. **Electrical safety test per IEC 62353** (the in-service/recurrent-test standard — not 60601, which is the pre-market type-test standard the OEM used to design the device):

   | Applied-part class | Patient leakage, normal condition | Patient leakage, single-fault condition |
   |---|---|---|
   | Type B (no direct patient connection, e.g. chassis-only contact) | ≤100 µA | ≤500 µA |
   | Type BF (patient-connected, not direct cardiac) | ≤100 µA | ≤500 µA |
   | Type CF (direct cardiac contact, e.g. cardiac catheter, external pacer leads) | ≤10 µA | ≤50 µA |

   Ground/protective-earth continuity: resistance at or below the facility's adopted ceiling (commonly ≤0.2 Ω measured at rated test current) — treat any reading within ~20% of a limit as a fail requiring root-cause, not a pass with a note.
3. **Label and log:** asset tag with next-due date, work order closed with actual measured values (not just pass/fail), technician ID and timestamp.

## 3. Alternative Equipment Maintenance (AEM) eligibility matrix

CMS's AEM policy (S&C 14-07-Hospital) lets a facility set its own risk-based PM interval instead of the OEM's recommended interval — but not for everything.

| Equipment category | AEM-eligible? | Why |
|---|---|---|
| Imaging/radiologic equipment (CT, MRI, mammography, fluoroscopy) | No | CMS carve-out — federal/state radiation-safety rules require OEM-recommended intervals regardless of in-house risk data. |
| New equipment, first maintenance cycle | No | No in-house failure history yet to justify deviating from OEM; use OEM interval until at least one full cycle of data exists. |
| Equipment under an open FDA recall or safety notice specifying a maintenance action | No | The recall/notice interval supersedes both AEM and any standing PM schedule until closed. |
| Life-support equipment (ventilators, anesthesia machines) with ≥2 years of documented in-house failure/PM history | Yes, with documented justification | Permitted, but CMS guidance expects a stronger evidence trail before lengthening intervals on anything life-support-critical. |
| General diagnostic/therapeutic equipment with stable failure history | Yes | The typical AEM use case — risk-scored interval replacing OEM default. |

## 4. Recall / repeat-fault triage sequence

Run this whenever a device model throws the same fault at more than one location, or whenever a device is involved in a reported patient event.

1. **Freeze first.** Preserve the device's current settings and event/error log before any troubleshooting. If a patient event is involved, pull the device fully out of service and tag it "hold — do not repair" until risk management clears it.
2. **Pull the fault history** for the specific asset (not just this ticket) and, if a second event within roughly 30 days on the same asset or the same model at another location, escalate from single-unit repair to fleet-level check.
3. **Check three sources before touching hardware:** the manufacturer's service-bulletin feed, the FDA MAUDE database for the model, and the facility's own incident log across all serial numbers of that model.
4. **Classify the reporting obligation** before repairing:
   - Death: report to FDA and the manufacturer within 10 working days of the facility becoming aware (21 CFR 803.30).
   - Serious injury: report to the manufacturer within 10 working days; report to FDA only if the manufacturer is unknown.
   - Near miss / no harm: log internally per facility risk policy; not an FDA-reportable event, but still feeds the fleet-pattern check above.
   - Manufacturer-initiated recall of the model: classify by FDA severity — Class I (reasonable probability of serious harm or death), Class II (temporary or reversible harm), Class III (unlikely to cause harm) — and follow the manufacturer's specified correction, not an internal workaround.
5. **Repair and re-verify** per the return-to-service checklist (section 2) only after the reporting determination is made and, for a fleet pattern, flag every other unit of that model/firmware version crossing the same risk threshold (age, cycle count, time since last calibration) for proactive action rather than waiting for the next failure.

## 5. PM backlog escalation table

| Days past due | Status | Action |
|---|---|---|
| 1–10 | Within normal scheduling slack | No escalation; complete in the current cycle. |
| 11–29 | Approaching grace-period limit | Flag to equipment manager; schedule catch-up capacity before day 30. |
| 30+ (grace-period breach) | Compliance gap | Escalate immediately; document reason for delay and revised completion date — this is what a surveyor will ask about first if it's a life-support/high-risk asset class. |
| Any life-support asset, any day past due | Treat as day-30 regardless of the count | Life-support/high-risk equipment gets zero grace in practice even where the written policy allows some — Joint Commission and CMS weight this subclass far more heavily than the facility-wide average. |
