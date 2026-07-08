# Red flags — what a microsystems engineer notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together in the same layout, test report, or failure-analysis packet is a pattern worth stopping the review for.

### Mechanical overload stop set past g/3 of the sense/actuation gap
- **Usually means:** the stop was sized to the maximum expected shock displacement or to a rounded fraction of the physical gap, without computing the electrostatic pull-in limit — the plate goes electrostatically unstable and snaps to contact before it ever reaches the intended mechanical stop.
- **First question:** "What's the pull-in limit (g/3) for this gap, and is the stop distance below it with margin?"
- **Data to pull:** the sense-gap dimension from the process stack, the stop-geometry drawing, and the computed pull-in displacement.

### Pilot-lot self-test or stiction failure rate above ~2-3% with no travel/stop-geometry check performed first
- **Usually means:** the failure was routed straight to surface chemistry (add a hydrophobic coating, re-run) before checking whether the stop sits past the pull-in point — geometry defects are cheaper and faster to diagnose than a chemistry root cause and are the more common culprit.
- **First question:** "Has the stop-versus-pull-in check been run on this design before a coating change is proposed?"
- **Data to pull:** the pilot-lot self-test failure log, the stop-geometry drawing, and the pull-in calculation.

### Hermeticity result reported as a flat pass against MIL-STD-883 Method 1014 with no cavity-volume context
- **Usually means:** the test's ~5×10⁻¹¹ atm·cm³/s resolution floor is being treated as universally adequate, when for a cavity under ~10⁻³ cm³ a real leak can sit an order of magnitude below what the method can resolve — "passed Method 1014" and "actually sealed" are different claims at this scale.
- **First question:** "What's the package cavity volume, and does the measured leak rate sit within an order of magnitude of the test's resolution floor?"
- **Data to pull:** the Method 1014 leak-rate result, the cavity volume from the package drawing, and the method's stated resolution floor.

### DRIE feature aspect ratio validated only against a ~80:1 lab/R&D-tier capability number, not the ~40:1 mass-production tier, before layout freeze
- **Usually means:** the design was checked against the foundry's best demonstrated aspect ratio (~80:1) rather than the production-tier number (~40:1) the part will actually ship on — a feature that survives at lab scale doesn't survive at mass-production yield.
- **First question:** "Is this aspect ratio checked against the foundry's stated production-tier capability, or against a best-case R&D figure?"
- **Data to pull:** the foundry's process-capability documentation broken out by tier, and the specific feature's aspect ratio in the layout.

### Reliability sign-off based on peak-voltage overload survival alone, with no duty-cycle or sustained-drive test
- **Usually means:** the qualification plan tested instantaneous overload but never modeled sustained one-sided actuation at operating temperature — hinge memory/creep is a slow, cumulative failure mode that a peak-voltage-only test doesn't exercise, and a part that survives the overload test can still fail in the field from a drive pattern the test never ran.
- **First question:** "What's the duty cycle and thermal exposure this element sees in the field, and has it been tested at that profile, not just at peak voltage?"
- **Data to pull:** the field drive-pattern/duty-cycle spec, the qualification test plan, and the life-test rig's actual run conditions.

### Shock or temperature-cycling qualification plan states peak g-level and temperature extremes but omits axis count, ramp rate, or dwell time
- **Usually means:** the plan was written from a rounded approximation of JESD22-B104/A104 rather than the standard's actual parameters — matching peak values while dropping ramp rate or dwell isn't equivalent qualification.
- **First question:** "Does this test plan specify axis count, shocks per axis, ramp rate, and dwell exactly as JESD22-B104/A104 require, or only the peak numbers?"
- **Data to pull:** the qualification test plan and the relevant JEDEC standard's full parameter table.

### Dedicated fab lot committed before a process-capability or pull-in/stop-margin check has been run
- **Usually means:** schedule pressure pushed the team past a cheap simulation or MPW shuttle check straight to a $50k-plus NRE plus ~$10k-per-wafer dedicated lot — a defect an MPW run or a pull-in calculation would have caught for a fraction of the cost is instead discovered after committing to the lot.
- **First question:** "Has this design passed a process-capability check and a pull-in/stop-margin check, or an MPW shuttle run, before the dedicated-lot PO was cut?"
- **Data to pull:** the design-review sign-off record, the MPW shuttle schedule (if any), and the dedicated-lot cost/NRE commitment.

### SPC control chart on wafer critical dimensions shows drift trending toward the design's tolerance band with no design-margin re-check
- **Usually means:** the process is trending out of the window the design was validated against, but the drift is being tracked as a fab-yield metric only, not fed back into whether the design's stop margins and pull-in calculations still hold at the drifted dimension.
- **First question:** "At the current drift trend, does the pull-in/stop-margin calculation still hold, or does it need to be re-run against the drifted critical dimension?"
- **Data to pull:** the SPC control chart for the relevant critical dimension and the original design-margin worksheet it was validated against.

### Anti-stiction contact geometry (dimple, standoff) absent at a mechanical stop that arrests overtravel
- **Usually means:** the stop was placed to prevent electrostatic pull-in contact but the contact surface itself was left flat, leaving capillary or van der Waals stiction risk at the stop even though the pull-in failure mode was correctly addressed.
- **First question:** "Is there anti-stiction contact geometry at this stop, or is it a flat mechanical contact?"
- **Data to pull:** the stop-geometry drawing detail at the contact point.

### Failure-analysis memo attributes a field return to "reliability" or "wear" without naming a specific mechanism
- **Usually means:** the finding wasn't traced to a distinguishable mechanism (pull-in overtravel, hinge-memory creep, moisture-assisted capillary stiction, fatigue crack) before being written up, which means the recommended fix is a guess rather than a targeted design change.
- **First question:** "Which specific mechanism — pull-in, creep, moisture-assisted stiction, fatigue — does the failure data point to, and what data separates it from the alternatives?"
- **Data to pull:** the field-return failure log, SEM/optical inspection images if available, and the device's actual drive/thermal history.

### Duty-cycle margining applied uniformly across all actuators after a hinge-memory finding, including intermittent-duty elements
- **Usually means:** an overcorrection from a genuine creep finding on one actuator got generalized to the whole design without checking which elements actually see sustained asymmetric drive — intermittent-duty elements were never at risk from creep and don't need the same margin.
- **First question:** "Which actuators in this design actually see sustained one-sided drive, versus intermittent or symmetric drive that was never the creep risk?"
- **Data to pull:** the per-actuator drive-pattern spec across the design, not just the one that triggered the finding.
