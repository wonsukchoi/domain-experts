# Vocabulary

Terms generalists blur together that a mechanic keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## L10 life vs. MTBF

**L10 life** is the calculated bearing life at which 10% of a population of identical bearings under identical design load is statistically expected to have failed — a design figure, not an observed one. **MTBF** (mean time between failures) is an *observed* fleet statistic computed from actual run-hours and actual failures on this plant's assets.

*Practitioner usage:* "The catalog says L10 is 11 years at design load, but our demonstrated MTBF on this fan class is under 3 years — that gap is telling us the real-world load doesn't match the design assumption."

*Common misuse:* treating L10 as a guaranteed service life ("it's rated for 11 years, it shouldn't be failing") — L10 is a 10th-percentile failure point calculated from an assumed load; misalignment or contamination routinely moves the real failure point far earlier without any manufacturing defect.

## Vibration severity zone (ISO 10816/20816 Zone A–D)

A machine-class-specific banding of overall vibration velocity (mm/s RMS) into four zones: A (new-machine condition), B (acceptable for unrestricted operation), C (unsatisfactory for long-term operation), D (damage risk). The boundaries differ by machine class (I–IV), based on power and foundation type — the same mm/s reading can be Zone B on one machine and Zone D on another.

*Practitioner usage:* "That's 4.1 mm/s — Zone C on this Class II fan, but it'd only be Zone B on the Class IV turbogenerator down the line. Don't reuse zone thresholds across machine classes."

*Common misuse:* quoting a single "danger threshold" (like "4.5 mm/s is bad") without specifying the machine class the boundary applies to, or ignoring the trend slope and treating every Zone C reading as equally urgent regardless of how fast it got there.

## BPFO / BPFI / BSF / FTF

The four characteristic bearing defect frequencies: **BPFO** (ball pass frequency, outer race), **BPFI** (ball pass frequency, inner race), **BSF** (ball spin frequency), **FTF** (fundamental train frequency, the cage). Each is a function of the bearing's specific geometry (bore, pitch diameter, ball diameter, contact angle) and running speed — they are not generic multiples of running speed.

*Practitioner usage:* "There's a peak at 118 Hz with 1X sidebands — that maps to this bearing's BPFO at 1780 rpm, so it's an outer-race defect, not a gear-mesh harmonic."

*Common misuse:* mistaking a BPFO/BPFI peak for a harmonic of running speed (2X, 3X) because it happens to be numerically close, or reusing another bearing model's defect frequencies because the bore size looks similar — the pitch diameter and ball count change the frequency even for bearings of the same nominal bore.

## Predictive maintenance (PdM) vs. preventive maintenance (PM) vs. RCM

**PM** is maintenance on a fixed calendar or run-hour interval regardless of actual condition. **PdM** is maintenance triggered by measured condition (vibration, oil, thermal) crossing a threshold. **RCM** (reliability-centered maintenance) is the decision process that assigns each failure mode to PM, PdM, or run-to-failure based on its consequence and detectability — RCM is the framework that chooses between the other two, not a fourth maintenance type.

*Practitioner usage:* "We're not switching everything to PdM — RCM says this seal is low-consequence and hard to trend cheaply, so it stays on run-to-failure; the bearing on the same pump earns PdM because it's high-consequence and vibration trends it well."

*Common misuse:* treating "PdM" as universally superior to "PM" and instrumenting every asset, ignoring that PdM has a real per-asset cost that RCM is supposed to weigh against consequence.

## Root cause failure analysis (RCFA) vs. failure mode

The **failure mode** is what physically happened (bearing seized, gear tooth fractured, seal leaked). **RCFA** is the investigation into why it happened — the mechanical, procedural, or design chain of causes behind that failure mode. Two identical failure modes on the same asset can have entirely different root causes.

*Practitioner usage:* "Failure mode is the same as last time — DE bearing seizure — but RCFA this time points to a lubrication interval that got skipped during the changeover, not the misalignment we fixed six months ago."

*Common misuse:* writing the failure mode into the work order's root-cause field ("root cause: bearing failure") — that's circular; the root cause is the reason the bearing failed, one level deeper.

## Laser shaft alignment: offset vs. angularity vs. soft foot

**Offset** is the parallel (radial) displacement between the two shaft centerlines at the coupling. **Angularity** is the angular difference between the two shaft centerlines, expressed per unit of coupling spacing. **Soft foot** is a mounting-frame condition where one or more machine feet aren't coplanar, so tightening a bolt distorts the frame and any alignment reading taken over it won't hold.

*Practitioner usage:* "Offset's within tolerance but angularity is 0.6 mils/inch against a 0.3 spec — and there's 4 mils of soft foot on the outboard corner that has to be shimmed before any of these numbers mean anything."

*Common misuse:* correcting offset and angularity while ignoring an uncorrected soft foot — the alignment will appear good on the laser readout and drift out again within days as the frame relaxes under load.

## Lockout/tagout (LOTO) vs. isolation vs. de-energization

**Isolation** is physically separating equipment from all energy sources (electrical, stored mechanical, hydraulic, pneumatic, thermal). **De-energization** is removing the energy itself. **LOTO** is the documented procedure — locks, tags, verification, and group-lock protocols under 29 CFR 1910.147 — that makes isolation and de-energization auditable and enforces that no one can re-energize while someone is exposed.

*Practitioner usage:* "The breaker's off, but that's de-energization, not LOTO — until my lock and tag are on it and I've verified zero energy at the point of work, it's not isolated for me to work on."

*Common misuse:* treating "the switch is off" as equivalent to LOTO complete, or using a group lockout box as a substitute for each individual crew member's own lock, which removes the protection LOTO exists to provide for whoever is actually hands-on at that moment.

## Oil analysis: ISO 4406 cleanliness code vs. PQ index vs. TAN/TBN

**ISO 4406** codes particle contamination by size and count (e.g., "18/16/13") — higher numbers mean more contamination. **PQ index** (particle quotient) measures ferrous wear debris via magnetic response, a leading indicator of active metal-on-metal wear rather than contamination ingress. **TAN/TBN** (total acid/base number) tracks oil degradation and additive depletion, not particle content at all — three different failure signatures from the same sample.

*Practitioner usage:* "ISO code jumped from 18/16/13 to 21/19/16 — that's contamination ingress, probably the breather. PQ is flat, so it's not active wear yet; catch the seal before it becomes one."

*Common misuse:* reading a single oil report number as "good" or "bad" without separating which of the three signatures moved — a clean ISO code with a rising PQ index still means active wear is underway.

## Criticality ranking vs. FMEA severity/RPN

**Criticality ranking**, in the RCM sense used here, is downtime-cost-per-hour × annual failure probability, used to decide which assets get condition-based monitoring versus run-to-failure. **FMEA severity/RPN** (risk priority number = severity × occurrence × detection, from formal failure-mode-and-effects-analysis) is a broader scoring method that also weighs safety and detectability, not just cost. They overlap but aren't interchangeable — a low-cost failure mode with severe safety consequence can rank low on pure downtime-cost criticality and high on FMEA severity.

*Practitioner usage:* "This spare-pump seal ranks low on downtime-cost criticality — it's redundant — but it stays on the PM list anyway because FMEA flagged the safety severity of an uncontained failure."

*Common misuse:* using cost-based criticality alone to set every PM strategy and dropping a low-cost, high-safety-severity failure mode to run-to-failure because the downtime math looked cheap.
