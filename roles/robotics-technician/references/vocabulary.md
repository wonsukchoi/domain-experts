# Vocabulary

Terms generalists flatten together that a robotics technician keeps sharply separate — the value is in the misuse, not the definition.

## Mastering vs. homing

**Mastering** ties a joint's absolute-encoder pulse count to a known mechanical zero position — a one-time (or post-disturbance) reference-setting act using a fixture or the OEM's zero-position procedure. **Homing** is the routine act of driving axes to a known start position at the beginning of a program or shift, using the mastering reference that's already established. A robot can home successfully to a wrong position all day if the underlying mastering reference is off.

**In use:** "It homes fine every cycle — homing just proves the servo loop can reach a repeatable position, not that the position it's reaching is the correct one. Check the mastering data."

**Common misuse:** treating successful homing as proof the robot is correctly mastered, when homing only exercises repeatability against whatever reference is currently stored, right or wrong.

## Absolute encoder vs. incremental encoder

An **absolute encoder** reports a unique position value at every angle and retains that value (via battery-backed memory or a multi-turn mechanism) through a power cycle — mastering data survives a restart. An **incremental encoder** only reports relative motion and requires a homing/reference move at every power-up to establish position; it has no mastering data to lose because it never claims an absolute reference between power cycles.

**In use:** "This axis is on an incremental encoder — don't bother checking mastering pulse counts, just verify the homing sequence completed cleanly after the power-up."

**Common misuse:** applying absolute-encoder troubleshooting (pulse-count comparison, mastering-loss alarms) to an incremental-encoder axis, where the relevant check is homing-sequence completion, not a stored reference.

## Zero-energy state

The verified condition where every independent energy source on a machine (electrical, pneumatic, hydraulic, gravitational/mechanical) has been isolated and confirmed at zero by direct measurement (meter, gauge, visual/manual check) — not inferred from a single isolation point or a dark display.

**In use:** "Main's locked, but we're not calling this zero-energy until the accumulator gauge reads 0 and J3's confirmed at its rest pose — three sources, three checks."

**Common misuse:** using "locked out" and "zero-energy" interchangeably, when a lock/tag on one source says nothing about whether other independent sources are actually at zero.

## Category 0 stop vs. Category 1 stop vs. Safety-rated Monitored Stop (SRMS)

Per IEC 60204-1: **Category 0** removes power immediately (uncontrolled coast or dynamic braking to stop, then power off). **Category 1** decelerates under power in a controlled manner, then removes power once stopped. **SRMS** holds the robot stationary under active servo control with power still applied and motion monitored — the arm looks stopped but is fully energized and will resume the instant the monitored condition clears.

**In use:** "It's parked under SRMS for the operator's material load — power's still on the servos, so don't treat it like a Category 0 stop for a hands-in-the-cell task; that still needs LOTO."

**Common misuse:** treating any stopped-looking robot as safe to approach without power isolation, when an SRMS-stopped robot is energized and can move again without warning once the monitored condition is satisfied.

## Tool Center Point (TCP) vs. flange frame

The **flange frame** is the fixed mechanical reference at the robot's mounting face. The **TCP** is a user-defined, offset frame representing the tool's actual working point (a torch tip, a gripper's contact point) — every taught position, speed spec, and payload rating is only meaningful relative to whichever frame is actually configured and active.

**In use:** "Confirm TCP 3 is the active tool frame before trusting these taught points — if it's still pointing at the flange default, every position in this program is off by the torch offset."

**Common misuse:** running or verifying a program against the default flange frame instead of the configured TCP, producing positions that look wrong even though the taught points themselves are correct relative to the intended tool frame.

## Residual (in TCP calibration)

The distance between an individual calibration touch point and the pivot point the controller's routine computes from all touches together — a per-touch error measurement, not the TCP offset value itself.

**In use:** "TCP offset came back fine, but check the individual residuals before accepting — a good mean can hide one touch point that's way off."

**Common misuse:** looking only at whether the calibration routine "completed successfully" without reviewing the per-touch residual numbers and their pattern (scattered vs. systematic).

## Program override (%) vs. taught speed

**Taught speed** is the velocity value programmed into an individual motion instruction. **Program override** is a global percentage multiplier (set at the pendant or in the controller) applied on top of every taught speed simultaneously — a 50% override halves every motion segment's actual speed regardless of what each segment was individually programmed to.

**In use:** "Every segment came back proportionally slower — check the override percentage before you start re-teaching individual moves."

**Common misuse:** diagnosing a uniform, proportional slowdown across all segments as a series of individual motion problems, when a single override-percentage change explains all of them at once.

## Quick master vs. zero-position (full) master

A **quick master** re-establishes the mastering reference using a fixture or pin at a known repeatable pose, fast but only as accurate as the fixture's own repeatability and seating. A **zero-position (full) master** re-establishes the reference using the OEM's factory-defined zero pose and calibration procedure, slower but the higher-confidence method — required when pulse-count drift exceeds the manufacturer's quick-master acceptance band or after a repair touching the drivetrain itself (not just an external hard stop).

**In use:** "Drift's under a thousand counts — quick master and log it. If we'd seen five figures of drift I'd have pulled the drivetrain apart and done a full zero-position master instead."

**Common misuse:** always defaulting to a quick master regardless of drift magnitude or repair type, when large drift or drivetrain-level work calls for the full procedure a fixture-based quick master can't substitute for.

## Stopping distance vs. stopping time

**Stopping time** is the interval from a stop command (protective-stop trigger, E-stop) to zero velocity. **Stopping distance** is the physical distance traveled during that interval, which depends on both stopping time and the speed the robot was moving at when the command was issued — the same stopping time produces a longer stopping distance at a higher commanded speed.

**In use:** "Stopping time barely changed, but we're running the SSM segment faster now than when this was certified — recheck stopping distance at the new speed, not just the time."

**Common misuse:** verifying only stopping time after a speed-related change and assuming stopping distance (the number the separation-distance calculation actually uses) scales the same way without checking.

## Servo trend vs. HMI cycle counter

A **servo trend** (or PLC I/O trace) is a time-stamped record of individual axis/segment/signal states over a cycle, fine-grained enough to isolate which segment changed. The **HMI cycle counter** reports one aggregate number (total cycle time) with no segment detail — useful for spotting that a regression exists, useless for finding where it lives.

**In use:** "The HMI counter told us we're 2.3 seconds over spec; the servo trend told us where — the handshake wait, not the weld."

**Common misuse:** treating the aggregate cycle-time number as diagnostic information on its own, when it can only flag that a regression exists, not which segment caused it.

## Brake-set state (elevated/counterbalanced axis)

Whether an axis's mechanical brake is actively holding position against gravitational or counterbalance load — distinct from whether the axis is powered. A brake can be worn or improperly adjusted such that it "sets" (engages) but doesn't fully arrest the axis under full load, which only shows up as unexpected axis creep during a de-energized/locked-out state, not during normal powered operation.

**In use:** "Brake's setting, but confirm it's holding under this payload before we call the axis safe to work under — don't take 'brake engaged' on the display as proof it's actually arresting the load."

**Common misuse:** confirming a brake is "set" from a controller status indicator alone, without a physical/manual check that the axis actually stays put under load — the indicator reports command state, not verified mechanical holding capacity.
