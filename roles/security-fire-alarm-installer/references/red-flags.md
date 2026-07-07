# Red flags

Smells a senior installer or reviewer catches walking a job site or reviewing a punch list — what it usually means, the first question to ask, and the data to pull before signing off.

## 1. Smoke detectors spaced at a flat 30 ft grid regardless of ceiling height or geometry

**Usually means:** whoever laid out the plan used the nominal spacing figure without checking ceiling height, slope, or beam depth — all of which require a derate under NFPA 72 Chapter 17 and the specific detector's listing.

**First question:** "What's the ceiling height and geometry at each of these locations — flat, sloped, or beamed?"

**Data to pull:** reflected ceiling plan with height call-outs; manufacturer's spacing/derate table for the specified detector model; as-built photos of any beam, joist, or sloped-ceiling area.

## 2. Notification appliances specified at one candela rating building-wide

**Usually means:** the plan used the smallest or most commonly stocked candela rating for every room instead of sizing each room off its governing dimension — passes a casual plan check, fails an AHJ photometric spot-check in the larger rooms.

**First question:** "What's the largest single dimension in each room these appliances cover, and does the candela rating match that room's entry in the spacing table?"

**Data to pull:** room-by-room dimension list; NFPA 72 wall/ceiling-mount spacing table for the specified appliance mounting height; manufacturer's photometric data sheet for the appliance model.

## 3. NAC circuit current draw calculated at nameplate voltage without headroom

**Usually means:** the circuit was loaded right up to the panel's rated output with no margin for battery-voltage sag at end-of-discharge or for a future add-a-device request, which reads as "compliant" on paper and fails in the field as batteries age.

**First question:** "What's this circuit's calculated draw as a percentage of rated output, and does it account for end-of-life battery voltage?"

**Data to pull:** panel spec sheet's rated NAC output; itemized appliance current draw at minimum operating voltage (not nominal); battery calculation worksheet.

## 4. Two different manufacturers' devices on the same initiating or notification circuit

**Usually means:** someone assumed "UL listed" on each individual device label means the combination is a listed system — it doesn't; panel manufacturers publish specific compatibility lists, and mixing outside that list voids the system's listing even if every part is individually UL-marked.

**First question:** "Is this device combination on the panel manufacturer's published compatibility list, or just individually UL listed?"

**Data to pull:** panel manufacturer's compatible-device list (current revision); UL certificate numbers for both devices; any prior AHJ citation for non-compatible mixing on this contractor's other jobs.

## 5. Record of Completion filled out after the AHJ walkthrough is already scheduled, not before

**Usually means:** documentation is being treated as paperwork to catch up on rather than the actual acceptance-test spec — high odds the as-built doesn't match the Record of Completion, which is a common, entirely avoidable acceptance-test failure.

**First question:** "Walk me through the Record of Completion against what's physically installed, right now, before we call the AHJ."

**Data to pull:** current Record of Completion draft; as-built drawings; device count from the panel's programmed database versus the physical device count on site.

## 6. Repeated false alarms on one zone answered by replacing the detector, then replacing it again

**Usually means:** the environmental cause (HVAC airflow, steam, dust, contamination) was never diagnosed, so a fresh detector fails the same way the old one did on the same schedule — the fix addressed the symptom, not the cause.

**First question:** "What's the time-of-day and environmental pattern on these false trips, and has the wiring at that device been checked for a marginal ground fault?"

**Data to pull:** panel event history for the zone (timestamps, device IDs); detector sensitivity/contamination self-test log if the panel supports it; wiring continuity/ground-fault test results at the device and nearest junction.

## 7. A city's verified-response or enhanced-call-verification requirement answered by reducing detection sensitivity

**Usually means:** the installer or monitoring account misread "reduce false dispatch" as "make the system less sensitive" instead of diagnosing false-trip causes — trading a real detection risk for administrative convenience with the verification ordinance.

**First question:** "Is the false-trip rate being addressed at the cause, or is detection sensitivity being turned down to dodge verification callbacks?"

**Data to pull:** false-alarm dispatch history and municipal fine notices for the account; sensitivity/settings change log on the panel; monitoring station's verification-call log.

## 8. Class B wiring specified on a circuit serving a high-rise floor or high-occupancy assembly space with no documented risk review

**Usually means:** the panel's default wiring diagram was used without checking whether the local code amendment or occupancy risk requires Class A — a single wire fault on Class B takes out every downstream device on that run.

**First question:** "What does the locally adopted NFPA 72 edition and any amendment say about pathway class for this occupancy and story count?"

**Data to pull:** local AHJ's code-adoption bulletin and amendments; occupancy classification documentation; circuit-by-circuit pathway class list from the panel programming.

## 9. Battery standby calculation using nameplate device current instead of measured/rated end-of-life current

**Usually means:** the battery sizing worksheet used optimistic current figures, producing a battery that meets the 24-hour standby plus 5-minute alarm requirement on paper but not once the battery has aged past its rated capacity derate.

**First question:** "Does this battery calculation include the manufacturer's aging/derate factor, or just nameplate current at a fresh battery?"

**Data to pull:** battery calculation worksheet; battery manufacturer's capacity-derate curve; date of last battery replacement on the as-built log.

## 10. Duct smoke detectors installed without airflow sampling tube sizing matched to duct velocity

**Usually means:** a duct detector was mounted per a generic template rather than matched to the specific duct's air velocity, which can cause it to under-sample (missed detection) or over-sample (nuisance trips) — this is a distinct failure mode from open-area smoke detector placement and needs its own manufacturer sizing chart.

**First question:** "What's the duct air velocity at this sampling point, and does the sampling tube length/hole spacing match the manufacturer's chart for that velocity?"

**Data to pull:** duct air velocity measurement (from the mechanical contractor's balancing report); duct detector manufacturer's sampling-tube sizing chart; commissioning test result for that specific detector.
