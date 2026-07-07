# Red flags

Smell tests a senior loader catches on the first pass through a rack log, a bonding test record, or a shipping paper. Format for each: what it usually means, the first question to ask, and the data to pull before committing to a response.

## 1. Bonding resistance reads above the terminal threshold (commonly >10 ohms)

**Usually means:** the clamp is attached through paint/coating rather than bare metal, a corroded contact point, or a damaged cable — not necessarily a fully failed cable.

**First question:** "Is this reading through paint or coating at the contact point, or is it the cable itself?"

**Data to pull:** bonding test log and trend across recent shifts, contact-point inspection, cable continuity history.

## 2. A switch-loaded compartment is run at full rack rate from the start

**Usually means:** the restricted initial-rate procedure was skipped because the fill line is a submerged bottom-loading design — a design that doesn't by itself remove the switch-load static-accumulation risk.

**First question:** "What product was in this compartment last, and was the restricted-rate step applied regardless of the fill-pipe design?"

**Data to pull:** compartment's prior-cargo record, rack SOP for switch loading, loading-rate log for the transfer in question.

## 3. Overfill sensor and visual level gauge disagree by more than a small margin

**Usually means:** a miscalibrated sensor, a stuck float, or a gauge reading affected by foam/splash rather than true liquid level — either way, the disagreement itself is the finding, not something to average away.

**First question:** "Has the sensor been function-tested recently, and is the disagreement consistent across recent fills or new to this one?"

**Data to pull:** sensor calibration/function-test record, gauge reading history for this compartment, maintenance log.

## 4. Vapor-recovery coupler shows no vacuum/pressure response after connection

**Usually means:** the coupler isn't fully seated, the return line is valved shut somewhere downstream, or the cargo tank's vapor dome fitting is damaged — liquid transfer should not proceed on the assumption it'll self-correct.

**First question:** "Is the return-line path confirmed open all the way to the vapor-recovery unit, or only at the coupler itself?"

**Data to pull:** vapor-return line valve-position log, coupler seating check, cargo tank vapor-tightness certification date.

## 5. Loaded/metered quantity doesn't reconcile with the shipping paper's stated quantity

**Usually means:** a unit-conversion error (volume vs. weight, wrong density figure used), a wrong product code selected at the rack, or a paperwork error made before the load started — this is a hold regardless of which it is.

**First question:** "What density figure was used to convert between the metered volume and the paper's stated weight, and does it match the product actually in the line?"

**Data to pull:** rack totalizer reading, shipping paper quantity field, density/conversion factor used, product-code selection log.

## 6. Placard hazard class doesn't match the shipping paper's hazard class for the product loaded

**Usually means:** a multi-commodity cargo tank or tank car wasn't re-placarded after a product change, or the wrong placard set was applied at dispatch — this is a transport-document violation, not a cosmetic mismatch.

**First question:** "Is this a dedicated single-commodity cargo tank with permanent placards, or a multi-commodity tank that needed re-placarding for this specific load?"

**Data to pull:** placard application/change log, shipping paper for the current load, cargo tank's commodity-dedication status.

## 7. A cargo tank or tank car's periodic test (external visual, leakage, pressure, or thickness test under 49 CFR Part 180) is past due

**Usually means:** the vehicle is not currently qualified to carry the hazmat product being loaded, regardless of how routine the loading operation otherwise looks.

**First question:** "What test is overdue, and by how much — is this vehicle actually qualified to load today?"

**Data to pull:** cargo tank/tank car periodic-test certification record, last completed test date and type, current date against the required interval.

## 8. A marine transfer's Declaration of Inspection is missing a signature or wasn't re-confirmed after a watch change

**Usually means:** the joint vessel/facility safety agreement covering communication, shutdown signal, and transfer rate isn't actually in force for the crew currently on watch, even though the transfer is physically running.

**First question:** "Who signed the current DOI, and were they on watch when it was signed?"

**Data to pull:** DOI form and signatures, watch-change log, transfer start/re-confirmation timestamps.

## 9. Vapor-recovery capture is running below the terminal's efficiency requirement (commonly <98%)

**Usually means:** a leak in the vapor-return path, a partially open bypass, or a vapor-processing unit (carbon bed/refrigeration/oxidizer) operating degraded — not a liquid-side problem.

**First question:** "Is this a vapor-return path leak, or is the vapor-processing unit itself underperforming?"

**Data to pull:** vapor-recovery unit performance log, last capture-efficiency test result, return-line inspection record.

## 10. Repeated overfill near-misses are cleared by manual override rather than investigated

**Usually means:** the crew is treating the sensor trip as a nuisance alarm rather than checking sensor calibration, fill-rate control, or a rack-side flow-control issue — the near-miss will recur, likely at a worse moment, until the actual cause is found.

**First question:** "Has the sensor been function-tested for each of these events, or has each one just been overridden and reset?"

**Data to pull:** overfill event log with timestamps, sensor function-test record for the same windows, fill-rate log for each event.
