# Vocabulary

Terms generalists conflate that a biomed shop keeps sharply separate. Each: definition, a sentence a practitioner would actually say, and the common misuse.

### Preventive maintenance (PM) vs. corrective maintenance (CM) vs. AEM

**PM** is scheduled, risk-interval-driven work performed whether or not anything is wrong (calibration, cleaning, wear-part replacement, safety testing). **CM** is unscheduled work triggered by a reported fault. **AEM** (Alternative Equipment Maintenance) is a facility's own risk-based PM interval, substituted for the OEM's recommended interval under CMS policy, for equipment classes not carved out of the allowance.

*Practitioner usage:* "That's a CM ticket, not a missed PM — the device was on schedule, it just failed between cycles."

*Common misuse:* calling any unscheduled repair a "PM issue," or treating AEM as "skip maintenance" rather than a documented, risk-justified interval that still requires testing on schedule.

### Leakage current vs. ground (protective-earth) continuity

**Leakage current** is the small current that flows where it shouldn't — through a patient or chassis contact point — under normal or single-fault conditions, measured in microamps. **Ground continuity** is the resistance of the protective-earth path from the device's chassis to its power-cord ground pin, measured in ohms; a broken ground path is what turns a leakage-current fault into a shock hazard instead of a harmless one.

*Practitioner usage:* "Ground continuity read 0.4 ohms — over our 0.2-ohm ceiling — so the leakage-current number doesn't matter yet, fix the ground path first."

*Common misuse:* treating "electrical safety test" as one pass/fail number instead of two independent measurements that fail for different reasons.

### Type B vs. Type BF vs. Type CF applied parts

**Type B** applied parts have no direct patient electrical connection (e.g. a device chassis touching skin incidentally). **Type BF** applied parts connect to the patient but not directly to the heart (e.g. an ECG lead, a blood-pressure cuff). **Type CF** applied parts connect directly to the heart or vasculature (e.g. a cardiac catheter, external pacer leads) and carry the tightest leakage-current limits — commonly 10 µA normal / 50 µA single-fault, a tenth of the Type B/BF ceiling.

*Practitioner usage:* "It's a CF applied part, so 40 µA fails even though that number would pass on a BF device."

*Common misuse:* applying one leakage-current limit across all devices in a PM batch instead of checking each device's applied-part classification first.

### IEC 60601 vs. IEC 62353

**IEC 60601** is the type-test standard a manufacturer uses to design and certify a new device before it ships. **IEC 62353** is the recurrent-test standard a facility uses to periodically re-test an in-service device throughout its working life — different test conditions, different pass criteria in places, and the one a biomed actually runs on the bench.

*Practitioner usage:* "We test to 62353 in the field, not 60601 — 60601 was the OEM's job at design time."

*Common misuse:* citing "60601 compliance" as the standard for a routine PM electrical-safety test, when the applicable in-service standard is 62353.

### Recall vs. field correction vs. service bulletin

A **recall** (FDA-classified Class I/II/III by hazard severity) is a manufacturer-initiated action to correct or remove a device already in use because it violates the law or poses a health risk. A **field correction** is the broader FDA term (21 CFR 806) covering any correction made at the use site, whether or not it's formally classified as a recall. A **service bulletin** is manufacturer guidance about a known issue that may not rise to a reportable field action at all.

*Practitioner usage:* "This is a service bulletin, not a recall — no FDA classification, but we still recalibrate the fleet proactively."

*Common misuse:* treating every manufacturer notice as "a recall," which either causes unnecessary alarm or, worse, causes a genuine Class I recall to be under-prioritized because it "looked like the usual bulletin email."

### Recall Class I vs. II vs. III

FDA's severity classification for recalls: **Class I** — reasonable probability of serious adverse health consequences or death; **Class II** — temporary or reversible harm, or remote probability of serious harm; **Class III** — unlikely to cause any adverse health consequence.

*Practitioner usage:* "It's a Class I recall on the infusion pump's software — that jumps every other open ticket in the shop today."

*Common misuse:* assuming recall urgency scales with how many units are affected rather than with the classified severity — a Class I recall on five pumps outranks a Class III recall on five hundred.

### MDR (Medical Device Report) vs. internal incident log

**MDR** under 21 CFR 803 is the formal FDA reporting mechanism for device-related deaths and serious injuries, with a 10-working-day clock from the facility becoming aware. An **internal incident log** captures near-misses and no-harm events per facility risk policy — required for the facility's own pattern-tracking, but not FDA-reportable on its own.

*Practitioner usage:* "No MDR obligation here — nobody was hurt — but it goes in the incident log because it's this asset's second event this month."

*Common misuse:* assuming any device malfunction needs an FDA report, or conversely assuming a "no harm" event needs no documentation at all.

### Composite risk score vs. criticality

The **composite risk score** is the specific sum (equipment function + physical risk + maintenance requirement, each 1–5) used to assign a PM interval. **Criticality** is the broader, less formal judgment of how urgently a given down device needs attention right now, which factors in the risk score but also whether a patient is actively blocked.

*Practitioner usage:* "The pump's composite score is 11, semiannual PM — but its criticality this morning is low, because it's already been swapped out and isn't touching a patient."

*Common misuse:* using "critical" and "high risk score" interchangeably — a high-risk-score device sitting safely in storage is not the same triage priority as a lower-scored device currently in active patient use with no substitute.

### Uptime vs. MTTR vs. MTBF

**Uptime** (or availability) is the percentage of scheduled operating time a device is actually available for use. **MTTR** (mean time to repair) is the average time from a fault report to return-to-service. **MTBF** (mean time between failures) is the average operating time between faults for a device or fleet.

*Practitioner usage:* "MTTR on this ventilator model is 2.1 hours, well inside our 4-hour SLA for OR-critical equipment, but MTBF has dropped from 400 hours to 260 — that's the number that should worry us, not the repair speed."

*Common misuse:* reporting uptime alone as evidence of fleet health, when a fleet can hit a high uptime number while MTBF quietly degrades because repairs are getting faster at fixing a device that's failing more often.

### Calibration vs. preventive maintenance vs. electrical safety test

**Calibration** adjusts a device's measurement or output against a known reference standard (e.g. a pump's flow-rate accuracy, a defibrillator's delivered energy). **Preventive maintenance** is the broader scheduled service event that may include calibration as one of several tasks (cleaning, wear-part inspection, firmware check). **Electrical safety testing** is a separate, mandatory check of leakage current and ground continuity — not a calibration activity at all.

*Practitioner usage:* "The PM includes a calibration check and a separate electrical safety test — passing one doesn't excuse skipping the other."

*Common misuse:* treating "we calibrated it" as equivalent to "we did the full PM," which drops the electrical-safety and mechanical-inspection tasks that calibration alone doesn't cover.

### Grace period vs. PM completion rate

The **grace period** is the facility-defined window (commonly 30 days) after a PM's due date during which the device is still considered in compliance if the work gets done. The **PM completion rate** is the percentage of scheduled PMs actually completed on time (or within grace) over a reporting period — the metric surveyors and internal audits track.

*Practitioner usage:* "It's 11 days past due, still inside grace, but I want it done before it becomes a completion-rate problem at day 30."

*Common misuse:* treating the grace period as a soft target to always use fully, rather than a buffer for genuine capacity constraints — habitually finishing at day 29 on life-support equipment reads to a surveyor the same as being consistently behind.
