# Vocabulary

Terms of art generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Days' supply

- **Definition:** the number of days a dispensed quantity is expected to last at the prescribed dosing rate — quantity divided by daily dose, with PRN orders computed at the stated maximum frequency.
- **Practitioner usage:** "The sig changed to 1.5 tabs/day, so days' supply going forward is 30 ÷ 1.5 = 20 days, not the 30 the old regimen would have given."
- **Common misuse:** recalculating for a new fill's own quantity but forgetting to redo the *prior* fill's leftover-tablet math at the new rate, which is exactly what makes a reject-79 look wrong when it's actually right (or vice versa).

## NCPDP reject code

- **Definition:** a standardized code returned by a payer at claims adjudication (per the NCPDP Telecommunication Standard) identifying a specific reason the claim didn't pay as submitted.
- **Practitioner usage:** "That's a 76, plan limitations exceeded — the quantity's over the cap, not a coverage denial. Split the fill."
- **Common misuse:** treating every reject as one undifferentiated "insurance problem" and routing all of them to the same "call for override" action, which wastes time on the PA-required ones and risks overriding the genuinely-early refill-too-soon ones.

## Beyond-use date (BUD) vs. expiration date

- **Definition:** expiration date is the manufacturer's stability claim for the sealed commercial product; BUD is the date after which a compounded or repackaged preparation should no longer be used, set by USP <795>/<797> defaults or a specific stability study.
- **Practitioner usage:** "The commercial suspension's expiration date is two years out, but once we reconstitute it, USP <795> caps the BUD at 14 days refrigerated unless we have a study that says otherwise."
- **Common misuse:** assigning the manufacturer's expiration date to a compounded or reconstituted product, which describes a different (sealed, undiluted) preparation entirely.

## Tech-check-tech

- **Definition:** a state-authorized workflow where a specially certified technician performs final verification of a filled prescription (typically refills of stable, non-new orders) without a pharmacist re-checking each one, freeing pharmacist time for clinical work.
- **Practitioner usage:** "This state allows tech-check-tech for refills only, and only technicians with the added certification — new prescriptions and controlled substances still need pharmacist final check."
- **Common misuse:** assuming tech-check-tech authority or scope is uniform across states or carries over from a previous employer without re-verifying the current state board's rule.

## LASA (look-alike/sound-alike)

- **Definition:** drug name or packaging pairs prone to confusion due to visual or phonetic similarity, tracked on ISMP's Confused Drug Names list.
- **Practitioner usage:** "Hydroxyzine and hydralazine are a LASA pair — I read the full name and indication back before pulling either one."
- **Common misuse:** relying on bin position or habitual reach instead of reading the full label every time, which is precisely the condition under which LASA errors happen.

## Tall man lettering

- **Definition:** a typographic convention (mixed case, e.g., DOPamine vs. DOBUTamine) applied to known confusable drug-name pairs to make the distinguishing letters visually stand out.
- **Practitioner usage:** "The bin label uses tall man lettering for hydrOMORphone vs. hydrOXYzine — trust that over memory when grabbing quickly."
- **Common misuse:** treating tall man lettering as decorative rather than as a deliberate error-prevention signal, and not noticing when a bin or label is missing it for a known confusable pair.

## High-alert medication

- **Definition:** a drug class where an error, even if infrequent, carries a disproportionately severe risk of patient harm (insulin, opioids, anticoagulants, chemotherapy, concentrated electrolytes), per ISMP's High-Alert Medications list.
- **Practitioner usage:** "It's high-alert, so it gets the independent double-check no matter how backed up the queue is."
- **Common misuse:** treating the double-check as optional or scalable-down under volume pressure, which is the opposite of its intended purpose.

## Drug Utilization Review (DUR)

- **Definition:** an automated or pharmacist-performed check for interactions, duplicate therapy, high dose, or other clinical concerns at the point of dispensing, distinct from insurance eligibility checks.
- **Practitioner usage:** "That's a DUR reject, not a coverage issue — it needs a pharmacist clinical judgment call, not a technician override."
- **Common misuse:** conflating a DUR reject (clinical) with a plan-limitation reject (administrative) and routing both the same way.

## Prescription Drug Monitoring Program (PDMP)

- **Definition:** a state-run database of controlled-substance dispensing history across pharmacies and prescribers, queried to detect duplicate therapy or diversion patterns.
- **Practitioner usage:** "Before assuming this refill-too-soon is a data glitch, I pulled the PDMP — no other fills show up, so it's likely the dose-change explanation."
- **Common misuse:** relying only on the current pharmacy's own fill history, which misses fills from other pharmacies or prescribers entirely.

## Morphine milligram equivalent (MME)

- **Definition:** a standardized conversion of any opioid dose into an equivalent dose of oral morphine, used to compare total opioid burden across different drugs and formulations.
- **Practitioner usage:** "The new prescription's daily MME is roughly double the prior fill's — that's worth flagging to the pharmacist even if the days'-supply math checks out."
- **Common misuse:** comparing raw milligram doses of different opioids directly (e.g., assuming 8mg hydromorphone is "less" than 30mg morphine) without applying the conversion factor.

## DAW (Dispense As Written) code

- **Definition:** a one-digit code submitted with a claim documenting why a specific product (brand vs. generic) was dispensed, required by payers to justify reimbursement and patient cost-sharing.
- **Practitioner usage:** "The prescriber wrote 'brand medically necessary,' so this is DAW 1, not the system's default 0 — otherwise the patient gets billed as if they chose the brand themselves."
- **Common misuse:** leaving the system's default DAW code unchanged without checking it against the actual prescription language, which shows up later as an unexpected copay dispute.

## NDC (National Drug Code)

- **Definition:** the FDA product identifier for a drug, existing in a 10-digit product form and an 11-digit billing form that encodes package size; the two are not always the same string of digits after conversion.
- **Practitioner usage:** "The reject was on the NDC, not the drug — the 10-digit product code was keyed instead of the 11-digit billing NDC for this exact package size."
- **Common misuse:** treating the two formats as interchangeable, which causes billing mismatches even when the correct drug is physically being dispensed.
