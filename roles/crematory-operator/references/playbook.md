# Crematory Operations Playbook

Operational defaults with concrete steps and thresholds. Cycle-parameter figures are typical operating ranges cited by equipment vendors — verify against your specific retort's manual before treating them as fixed.

## 1. Intake and identification protocol

1. **Match the decedent to the case folder on arrival.** Confirm name, case number, and funeral home against the transfer paperwork before the body leaves the transport vehicle. Discrepancy of any kind — weight, name spelling, missing signature — halts intake until resolved with the funeral home, not "close enough."
2. **Assign and affix the stainless-steel ID disc.** Stamp the case number, place it with the decedent before the body enters the cooler, and log the disc number in the chain-of-custody sheet. This disc travels through cooler storage, charging, combustion, and cremulator processing — it is the one physical object present at every step.
3. **Open the chain-of-custody log** with: case number, date/time received, weight, funeral home, staff signature. Every subsequent handoff (cooler to charging table, charging table to retort, retort to cremulator, cremulator to packaging) gets its own timestamp and initials on this same log.
4. **Confirm the legal hold status before scheduling a charge time.** Pull the waiting-period clock (commonly 24–48 hours from death or from authorization, state-dependent), the medical examiner/coroner release if the case involved one, and the signed cremation authorization from the next of kin or authorizing agent. No open item, no slot on the day's charge schedule.

## 2. Pre-charge inspection checklist

Run this on every case, regardless of what the authorization form says:

- **Implanted electronic devices.** Physically palpate chest and abdomen for pacemakers, ICDs, insulin pumps, neurostimulators — do not rely on the form's checkbox. A confirmed or suspected device holds the case until surgically removed and documented; do not charge "carefully" around a suspected device, hold it.
- **Radioactive medical treatment.** Check the case file for recent brachytherapy or radioisotope treatment. If flagged (or unclear and the decedent's recent oncology history suggests it), hold and consult the facility's radiation safety protocol rather than processing routinely — this affects operator exposure, not just the cycle.
- **Container compliance.** Confirm the container is combustible, rigid enough to be handled without leakage, and free of prohibited materials (glass, sealed metal, aerosol canisters, batteries not already accounted for as an implant).
- **Prosthetics and orthopedic hardware.** Note known joint replacements, plates, or rods in the case file — not a hold condition, but flagged so the post-cycle magnet pass isn't a surprise and the recovered hardware can be logged and disposed of per facility policy (not returned with the remains).
- **Multi-occupancy check.** If more than one case is proposed for the same chamber load (commonly infant twins or, rarely, family members), confirm a signed multi-occupancy authorization is on file. Absent that signature, each case is charged separately regardless of family preference — this is usually a statutory requirement, not a facility policy choice.

## 3. Charge cycle parameters by body-weight band

| Weight band | Primary burner modulation (first ~25 min) | Est. primary cycle time | Cooldown before door open |
|---|---|---|---|
| Under 150 lb | 90–100% | 60–75 min | 30–45 min |
| 150–249 lb | 80–100% | 75–100 min | 45–60 min |
| 250–349 lb | 55–70% (throttled — adipose is self-sustaining fuel) | 100–150 min | 60–90 min |
| 350 lb+ | 40–55%, staged and viewport-monitored rather than timer-driven | 150–210+ min | 90–120 min |

Both primary and secondary chamber temperature must be confirmed against the facility's air permit before the cycle is logged complete — a cycle that finishes on time but never showed secondary chamber at its required hold temperature (typically in the 1,600–1,800°F range) is not a finished case, it's an emissions event waiting to be found on the next inspection.

## 4. Cool-down and remains recovery

1. Do not open the charge door until chamber temperature drops to the manufacturer-specified threshold — opening early risks operator burns and thermal-shocks the refractory brick lining, shortening its service life.
2. Recover all bone fragments and the ID disc from the chamber floor; sweep and vacuum the chamber fully before it's used for the next case. This full-clear step is the actual control against trace commingling between back-to-back cases, not a courtesy.
3. Pass a magnet over the recovered material to pull ferrous and prosthetic hardware (joint replacements, surgical screws, casket hardware) before processing. Log recovered hardware separately; it does not go back with the remains.

## 5. Processing and packaging

1. Weigh the recovered bone before processing and log it against the case number.
2. Process in the cremulator to a uniform granular consistency. Expect a 10–20% weight loss between recovered bone and finished processed remains from residual dust and transfer loss — a loss outside that range on a routine case is worth investigating (see red-flags.md) before packaging, not writing off.
3. Re-verify the ID disc against the case log at this step — the last point before the remains are sealed into a container that no longer shows the case's full processing history.
4. Package, label with the case number, and log the release: who picked up, when, signature. This closes the chain-of-custody record opened at intake.

## 6. Chain-of-custody log template

```
CASE #: ________          DATE RECEIVED: ________     TIME: ________
DECEDENT: ________________________     FUNERAL HOME: ________________
INTAKE WEIGHT: ______ lb    ID DISC #: ________         STAFF: ________

HOLDS CLEARED:  [ ] Waiting period   [ ] ME/Coroner release   [ ] Authorization signed
PRE-CHARGE INSPECTION:
  [ ] Implanted device check — result: ________________________
  [ ] Radioactive treatment check — result: _____________________
  [ ] Container compliance — result: ____________________________
  [ ] Multi-occupancy authorization (if applicable): ____________

CHARGE TIME: ________   PRIMARY TEMP LOG: ________   SECONDARY TEMP LOG: ________
CYCLE COMPLETE: ________   COOLDOWN COMPLETE: ________
RECOVERED BONE WEIGHT: ______ lb   ID DISC CONFIRMED: [ ] Y  [ ] N
PROCESSED REMAINS WEIGHT: ______ lb   PROCESSING LOSS: ______ %
PACKAGED / LABELED: ________   RELEASED TO: ________   SIGNATURE: ________
```
