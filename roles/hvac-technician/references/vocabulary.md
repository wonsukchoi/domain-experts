# Vocabulary

Terms generalists and junior techs flatten together that a practitioner keeps sharply separate — each with the misuse that leads to a mischarge or a wrong diagnosis.

## Superheat vs. subcooling

**Superheat** is how many degrees a refrigerant vapor has been heated above its saturation (boiling) temperature at the measured pressure — read at the evaporator outlet or compressor, it verifies charge on fixed-orifice systems. **Subcooling** is how many degrees liquid refrigerant has been cooled below its saturation temperature — read at the condenser outlet or liquid line, it verifies charge on TXV/EEV systems.

**In use:** "Don't check superheat on that one, it's a TXV — give me subcooling against the nameplate target."

**Common misuse:** using superheat to judge charge on a TXV/EEV system. The valve actively modulates to hold superheat near its setpoint across a wide charge range, so a "normal" superheat reading there says almost nothing about actual charge.

## Fixed orifice (piston) vs. TXV vs. EEV

**Fixed orifice** is a non-adjustable metering restriction — refrigerant flow through it varies with pressure differential only, so charge is verified by superheat. **TXV** (thermostatic expansion valve) modulates flow to hold a target superheat mechanically. **EEV** (electronic expansion valve) does the same electronically, usually with tighter control and diagnostic feedback.

**In use:** "It's a piston system, so the chart superheat target is what we charge to — not the 10-degree rule some TXV systems use."

**Common misuse:** applying one universal superheat or subcooling "rule of thumb" number across all three device types instead of pulling the specific chart or nameplate target for the equipment in front of you.

## Manual J vs. Manual S vs. Manual D

**Manual J** calculates the building's actual heating/cooling load in Btu/h. **Manual S** selects equipment capacity against that load within an acceptable sizing window. **Manual D** sizes ductwork to deliver the required airflow for the selected equipment at an acceptable friction rate.

**In use:** "Manual J says 33,000 Btu/h — Manual S puts us in a 3-ton, and Manual D has to move 1,200 CFM to it without the static climbing past 0.5."

**Common misuse:** treating "Manual J" as shorthand for "the load calc software" and skipping Manual S and D — a correct load number paired with an oversized unit or undersized ducts still produces a bad install.

## Total external static pressure (TESP) vs. CFM

**TESP** is the resistance the blower works against, measured across the whole air handler in inches of water column. **CFM** (cubic feet per minute) is the volume of air actually being delivered. High static doesn't directly tell you CFM — it tells you the blower is working harder, and delivered CFM has to be checked against the blower's rated performance table at that static.

**In use:** "TESP is 0.9 against a 0.5 rating — pull the blower table before assuming we're still moving 1,200 CFM, because we're probably not."

**Common misuse:** treating static pressure and airflow as the same measurement, or assuming a variable-speed blower "fixes" high static by ramping up — it compensates only within a range, past which capacity and motor life both suffer.

## Charge by weight vs. charge by superheat/subcooling

**Charge by weight** means evacuating fully and adding the manufacturer's nameplate charge (plus line-length adjustment) by scale — the method for a full recharge after a leak repair or new install. **Charge by superheat/subcooling** means fine-tuning an already-charged system by reading and adjusting against a target — the method for verifying or correcting an existing charge without a full evacuation.

**In use:** "We're not evacuating today, just verifying — charge by subcooling, not by weight."

**Common misuse:** charging by weight alone on a system with an unknown or altered line-set length and skipping the superheat/subcooling confirmation, or trying to charge by superheat from a fully open, empty system instead of evacuating and weighing in first.

## Short cycling

Repeated on/off cycles shorter than the equipment's design run time (often under 5–7 minutes on a moderate cooling call), most commonly caused by oversized equipment satisfying the thermostat before completing a full dehumidification cycle, or by a control/refrigerant fault causing safety trips.

**In use:** "It's cycling every four minutes on a 78-degree day — that's oversizing, not a bad thermostat."

**Common misuse:** attributing short cycling to a "sensitive thermostat" or "bad capacitor" before checking installed capacity against the Manual J load.

## Flood-back vs. slugging

**Flood-back** is liquid refrigerant returning to the compressor through the suction line, usually from a chronic undercharge/low-superheat or airflow fault, causing gradual oil dilution and bearing wear. **Slugging** is a sudden, larger liquid return event — often from severe overcharge or a failed metering device — that can mechanically damage the compressor immediately.

**In use:** "That compressor didn't fail overnight — years of flood-back from running low superheat wore the bearings down."

**Common misuse:** using the terms interchangeably; flood-back is a slow-wear mechanism, slugging is an acute-failure mechanism, and the corrective action (recheck charge/airflow trend vs. immediate charge correction) differs.

## Temperature split (delta-T)

The difference between return air and supply air dry-bulb temperature across the evaporator coil — a fast field check, typically 16–22°F on a properly dehumidifying cooling system, but not a standalone diagnosis.

**In use:** "Split's only 12 degrees — that tells us something's off, gauges and a manometer tell us what."

**Common misuse:** treating split as sufficient on its own to diagnose charge, and skipping the static pressure and superheat/subcooling checks that actually separate an airflow cause from a charge cause.

## Leak rate vs. one-time charge loss

**Leak rate** is an annualized percentage of full charge lost per year, the regulatory basis for EPA Subpart F repair-timeline triggers on equipment at or above the 50 lb threshold. **One-time charge loss** is refrigerant lost to a specific, now-repaired event (a failed Schrader valve, a fitting never tightened at install) and doesn't recur once fixed.

**In use:** "That's not a 20%-a-year leak rate situation — it lost charge once, at the fitting we just repaired, full stop."

**Common misuse:** citing "leak rate" for equipment under the 50 lb threshold where the rate-based regulatory trigger doesn't apply, or assuming any refrigerant loss automatically means an ongoing rate-based problem rather than a single fixable event.

## Microns vs. inches of mercury (vacuum)

**Inches of mercury (in. Hg)** is a coarse vacuum measurement adequate for confirming a system is roughly evacuated. **Microns** measure vacuum precisely enough to detect residual moisture and non-condensables — the unit that matters for confirming a system is dry enough to charge, commonly targeting 500 microns or below with a stable hold.

**In use:** "Gauge manifold says it's pulled down, but that's inches of mercury — put the micron gauge on before we call it dry."

**Common misuse:** using a manifold gauge's coarse vacuum reading (in. Hg) to confirm dryness instead of a micron gauge, missing moisture that later causes acid formation and compressor damage.
