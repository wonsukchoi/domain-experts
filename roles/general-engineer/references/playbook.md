# General Engineer — Coordination & Interface Playbook

## Interface Control Document (ICD) — filled example

Handoff: pump-skid vendor (mechanical/electrical) to plant SCADA integrator, chilled-water loop retrofit.

| Field | Vendor side (as-delivered) | Integrator side (as-assumed) | Resolved value | Owner |
|---|---|---|---|---|
| Flow signal type | 4–20 mA, 2-wire loop-powered | 0–10 V, 3-wire | **4–20 mA, 2-wire** — integrator adds isolator card | Integrator |
| Flow units | GPM | L/min | **GPM** at the transmitter; PLC scales ×3.785 to L/min internally | Vendor states unit; Integrator owns conversion |
| Pressure setpoint tolerance | ±2 psi at transmitter | ±0.5 psi assumed by control loop tuning | **±2 psi** — control loop retuned to vendor's actual tolerance | Integrator |
| Comms protocol | Modbus RTU, 19200 baud | Modbus TCP expected | **RTU→TCP gateway required**, added to BOM | Vendor confirms RTU is fixed; Integrator supplies gateway |
| Enclosure rating | NEMA 4 | NEMA 4X assumed (washdown area) | **NEMA 4X** — vendor to requote enclosure | Vendor |
| Alarm on comms loss | Not specified by vendor | Assumed fail-safe (valve closes) | **Fail-closed within 5 s of comms loss**, written into vendor spec as a change order | Vendor, verified by Integrator FAT |

**Process:**
1. Pull the "as-assumed" column from each side's own design documents *before* the kickoff call — never from a verbal description of the other side's system.
2. Any row where the two columns disagree is a defect found before integration, not during it; log it, don't just resolve it silently in conversation.
3. Every resolved value gets a named owner — the party whose design changes to close the gap, not the party who happened to notice it.
4. Re-issue the ICD after any vendor change order; a stale ICD is worse than none, since it reads as verified when it isn't.

## Downstream-substitution re-verification checklist

Run this whenever a fabricator, contractor, or vendor proposes a substitution described as "equivalent" or "no design change."

1. **Identify what changed:** part, material, joint/connection type, unit convention, or routing/topology of the load or signal path.
2. **Identify what didn't change:** the claim being made is usually "the unchanged part proves no re-verification is needed" — treat that claim as the thing to check, not evidence.
3. **Re-trace the full path** (load, thermal, signal, or data) through the point of substitution, not just at the substituted component itself.
4. **Recompute demand at every connection/interface the path crosses downstream of the substitution**, using the changed topology, not the original one.
5. **Compare recomputed demand against the connection's original allowable/rated capacity** — a capacity number computed for the *old* topology does not update itself.
6. **State the resulting margin explicitly** (see margin table below) before approving or rejecting.

### Margin re-verification — filled example (two catwalk substitutions, same connection)

| Scenario | Demand on upper box-beam connection | Allowable capacity | FoS | Verdict |
|---|---|---|---|---|
| Original: continuous rod bypasses connection | 6,000 lbf (own level only) | 10,000 lbf | 1.67 | Pass — meets code minimum |
| Proposed: split rod, lower level now anchors to upper connection | 12,000 lbf (6,000 own + 6,000 transferred) | 10,000 lbf (unchanged) | 0.83 | **Fail — hold submittal** |
| Reinforced-connection alternative | 12,000 lbf | 20,000 lbf (reinforced to 1.67× new demand) | 1.67 | Pass — resubmit with reinforcement calc |

**Rule:** never accept a "meets code" verdict computed against the pre-substitution capacity number; recompute capacity at the same time as demand.

## Specialist-routing decision table

Route the moment a problem's governing physics sits outside these five (of the seven OPM 0801 threshold areas): statics/dynamics, strength of materials, fluid mechanics, thermodynamics, electrical fields/circuits.

| Symptom in the problem statement | Governing discipline | Route to |
|---|---|---|
| "Will this crack/yield under repeated load" beyond simple static FoS | Fatigue / fracture mechanics | Mechanical/materials specialist |
| "Will this resonate or amplify vibration" | Structural dynamics, modal analysis | Structural/vibrations specialist |
| "Will this corrode / degrade chemically in service" | Materials/corrosion science | Materials engineer or metallurgist |
| "Will this trip a breaker / meet an arc-flash rating" | Power systems, protective relaying | Electrical/power specialist |
| "Will this meet a thermal-runaway or heat-rejection budget" beyond basic conduction/convection | Thermal systems design | Thermal/HVAC specialist |
| "Will this meet a regulatory emissions/environmental limit" | Environmental engineering | Environmental specialist |
| "Will this hold up under seismic/blast/dynamic extreme load" | Specialized structural dynamics | Structural specialist with that certification |

**Handoff format to the specialist:** state (a) what's already been ruled out and why, (b) the specific governing question, (c) the margin/threshold that triggered the route — never "can you take a look at this," which re-derives the scoping work the generalist already did.

## Systems-integration traceability table (V-model) — filled example

Requirement-to-verification link for a subsystem integration (sensor package → data bus → control logic).

| Requirement ID | Requirement (left leg) | Verification method (right leg) | Verification status | Owner |
|---|---|---|---|---|
| REQ-014 | Sensor reports flow rate accurate to ±1% of reading | Bench calibration against NIST-traceable reference, 5-point curve | Verified 2024-03-11 | Vendor test lab |
| REQ-015 | Data bus delivers sensor reading to control logic within 200 ms | End-to-end latency test, 100-sample average | Verified, avg 142 ms, max 187 ms | Integrator |
| REQ-016 | Control logic issues shutoff command within 500 ms of out-of-range reading | Fault-injection test, 20 trials | **Not yet verified** — test not scheduled | Integrator (flagged) |
| REQ-017 | System fails safe (valve closes) on comms loss | Comms-interrupt test at FAT | Verified 2024-04-02 | Integrator |

**Rule:** a requirement with no row in the right-hand column is not "probably fine" — it's an unverified requirement, and REQ-016 above blocks sign-off until scheduled and closed, regardless of how confident the design looks.

## Escalation memo — filled example (NSPE Canon 1 duty triggered)

Use when safety-relevant professional judgment has been overruled and informal escalation hasn't resolved it.

> **To:** [Employer/client engineering director], cc: project file
> **From:** [Engineer name, EIT/PE status]
> **Re:** Formal notice — unresolved safety objection, catwalk hanger-rod submittal, Building 4
>
> On [date] I identified that the proposed two-rod hanger substitution drops the upper box-beam connection's factor of safety from 1.67 to 0.83 against its code-mandated minimum (see attached calculation). I raised this informally to [name] on [date] and recommended holding the submittal pending reinforcement or reversion to the continuous-rod detail.
>
> On [date] I was informed the submittal will proceed as-is due to schedule pressure, without the reinforcement calculation being completed. This is a documented professional-judgment override on a life-safety item.
>
> Per NSPE Code of Ethics Canon 1, I am notifying you formally that I cannot sign off on this submittal in its current state. If this is not resolved by [date], I am obligated to notify [the appropriate regulatory authority / building official] per the same Canon.
>
> Attached: load-path recalculation, original and proposed submittal drawings, informal-notice email thread.

**Rule:** this memo is dated and attached to a calculation, never a verbal aside — the obligation is to make an unambiguous record, not to have privately raised a concern.
