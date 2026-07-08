# Vocabulary

Terms generalists flatten together that an automotive engineer keeps sharply separate — the value is in the misuse, not the definition.

## Weight transfer vs. weight shift

**Weight transfer** is the instantaneous, dynamic change in each tire's normal load caused by longitudinal or lateral acceleration acting through the CG height — it reverses the moment the acceleration stops and the total vehicle weight is unchanged, only its distribution across the four tires. **Weight shift** (loosely used interchangeably by generalists) more properly describes a static or quasi-permanent change in load distribution, such as adding cargo or fuel burn-off.

**In use:** "That's weight transfer, not weight shift — it disappears the instant we're off the brake, so don't spec a suspension component against it as if it were a static load case."

**Common misuse:** treating a dynamic weight-transfer figure as if it were a permanent static load the chassis carries at rest, which leads to over- or under-designing a component for a load case that only exists transiently.

## Friction circle (traction circle)

The combined-force limit √(Fx² + Fy²) ≤ μ·Fz a tire can produce at a given normal load — lateral (cornering) and longitudinal (braking/accelerating) force share one budget, not two independent ones.

**In use:** "The inside front tire is inside the friction circle for lateral alone, but adding the naive braking split pushes the combined vector outside it — that's the actual failure mode, not either force checked separately."

**Common misuse:** checking lateral grip and longitudinal grip against μ·Fz independently and concluding a maneuver is safe because neither exceeds the limit alone, missing that their vector sum does.

## Understeer vs. oversteer (gradient, not single-instant behavior)

**Understeer** is a vehicle's tendency, as cornering force increases, to require more steering angle than a neutral-steer baseline to hold the same radius (front tires reach their slip-angle limit first). **Oversteer** is the opposite (rear tires reach their limit first). The understeer gradient (deg/g) is a continuous property across the g-range, not a single yes/no label — a car can understeer at low g and transition toward neutral or oversteer at the limit.

**In use:** "It's mildly understeering at 0.4g but the gradient flattens toward neutral by 0.8g — don't characterize the whole envelope from the low-g number."

**Common misuse:** describing a car's handling with a single "it understeers" or "it oversteers" label from one test point, when the behavior is a gradient that can change sign across the g-range.

## Traction-limited vs. power-limited (or torque-limited)

**Traction-limited** acceleration is capped by the tire-road friction budget at the drive axle's dynamic load (μ·Fz), independent of how much more torque the engine could deliver. **Power-limited** (or torque-limited in a given gear) acceleration is capped by the powertrain's force output at that speed, with traction to spare. Which regime governs changes with speed — low-speed launch is frequently traction-limited even on a car that is power-limited by highway speed.

**In use:** "Don't spec a bigger turbo to fix the 0-60 number if the car is traction-limited until 45 mph — more torque there just spins the tires harder, not the car faster."

**Common misuse:** assuming a car's acceleration is always torque/power-limited (the powertrain's numbers) and sizing improvements there, when the actual limiting factor at the speed in question is tire traction.

## Crush distance vs. crush force (and crash-pulse average vs. peak)

**Crush distance** is how far the structure physically deforms during an impact; **crush force** is the resisting force during that deformation, and their product (integrated over distance) is the energy absorbed. The **average** crash-pulse deceleration (v²/2d) is a single summary number; the **peak** deceleration within the pulse — which governs many injury and component criteria — commonly runs 1.5-2x the average depending on pulse shape.

**In use:** "14g average sounds fine, but the haversine peak is over 22g — check that against the restraint system's rating, not the average."

**Common misuse:** citing only the average crash-pulse deceleration as if it were the number safety criteria are evaluated against, when peak or short-duration-clip values are frequently the governing metric.

## HIC (Head Injury Criterion) vs. raw peak head acceleration

**HIC** is a time-integrated function of head acceleration over a specified interval (commonly HIC15, a 15 ms window), not simply the peak g the head experiences — a short, very high spike can produce a lower HIC than a longer, moderate acceleration, because HIC weights magnitude and duration together.

**In use:** "Peak head accel dropped but HIC15 went up — the pulse got longer even as it got shorter in magnitude, and HIC captures that tradeoff where a raw peak-g comparison wouldn't."

**Common misuse:** comparing two crash pulses by peak head acceleration alone and assuming the lower-peak pulse is automatically the lower-HIC (and therefore safer) one.

## Natural frequency vs. resonant frequency

The **natural frequency** (f_n) is a property of the mass-spring(-damper) system alone — √(k/m) terms — independent of any excitation. The **resonant frequency** is where peak response actually occurs under a specific forcing input, which shifts from f_n as damping increases (resonance peak moves to a slightly lower frequency than the undamped natural frequency as damping ratio rises).

**In use:** "The mount's natural frequency is 10.6 Hz, but with the actual damping in the elastomer, the resonant peak sits a bit below that — use the damped figure for the transmissibility curve, not the raw undamped f_n."

**Common misuse:** using the undamped natural-frequency formula's result as if it were exactly where the worst real-world resonance occurs, ignoring that damping shifts and flattens the actual resonant peak.

## Transmissibility vs. isolation

**Transmissibility (TR)** is the ratio of force (or motion) transmitted through a mount system to the force (or motion) input — a single number at a given frequency ratio r = f_forcing/f_n. **Isolation** only occurs (TR < 1) once r exceeds √2 ≈ 1.414; below that ratio, the mount system actually amplifies the input rather than isolating it.

**In use:** "At idle we're at r = 1.2 on that proposal — that's below √2, so the 'soft' mount is amplifying idle shake into the body, not isolating it."

**Common misuse:** assuming any elastomeric or "soft" mount is automatically isolating vibration, without checking whether the resulting frequency ratio actually clears the √2 threshold where isolation begins.

## Firing frequency vs. engine order

**Firing frequency** is the actual rate (Hz) at which cylinders fire, computed from rpm and cylinder count/stroke type. An **engine order** is that same excitation expressed as a multiple of shaft rotational frequency (e.g., a 4-cylinder 4-stroke's dominant firing order is the 2nd order — two firing events per crank revolution) — orders are used to track excitation across the whole rpm range on one normalized axis (a Campbell diagram), rather than one frequency at one rpm.

**In use:** "Plot the 2nd-order line across the full rpm sweep on the Campbell diagram — a single firing-frequency-at-idle number only tells you about one operating point, not where it crosses the mount's natural frequency across the rev range."

**Common misuse:** checking NVH isolation only at one named rpm (usually idle) instead of sweeping the relevant order across the full operating rpm range to find where it crosses a structural or mount natural frequency.

## Static weight distribution vs. dynamic (corner) weight

**Static weight distribution** is the front/rear (and left/right) split measured with the vehicle at rest. **Dynamic (corner) weight** or **instantaneous normal load** is each tire's actual load during a maneuver, after longitudinal and lateral weight transfer — the number that actually governs available grip at that instant.

**In use:** "55/45 static is the starting point for brake-bias calibration, but the EBD table has to be built on dynamic corner weight across the g-g envelope, not the static split alone."

**Common misuse:** using the static weight distribution as the sole input to a proportioning, suspension, or grip calculation that is actually governed by the dynamic, maneuver-specific load.

## Rolling resistance coefficient (Crr) vs. tire drag

**Rolling resistance coefficient** is a dimensionless factor (Crr) relating rolling resistance force to normal load (F_rr = Crr·W) from tire hysteresis and deformation, independent of speed to a first approximation. It's frequently conflated with aerodynamic drag from the tire/wheel, which is a separate, speed-squared-dependent force captured in the vehicle's overall drag coefficient and frontal area, not in Crr.

**In use:** "Crr covers the tire's own rolling loss — the wheel's contribution to aero drag is a separate term already folded into the vehicle Cd·A, don't double-count it as part of rolling resistance."

**Common misuse:** treating rolling resistance as speed-dependent in the same way aerodynamic drag is, or folding aerodynamic effects into the rolling-resistance term.

## Barrier speed vs. closing speed

**Barrier speed** (e.g., FMVSS 208's 30 mph / 48.3 km/h) is the vehicle's own speed into a fixed, rigid barrier — the full kinetic energy the vehicle's own structure must absorb. **Closing speed** in a vehicle-to-vehicle crash is the relative speed between two moving vehicles, and translates to a different, generally lower, effective barrier-equivalent speed per vehicle depending on the mass ratio and whether the collision is head-on or offset.

**In use:** "Don't cite the 30 mph FMVSS 208 barrier number as if it directly represented a 30 mph closing-speed car-to-car crash — the energy each structure has to absorb is a function of both vehicles' mass and speed, not the barrier test's single-vehicle number."

**Common misuse:** treating a regulatory barrier-test speed as directly equivalent to a real-world two-vehicle closing speed, when the energy absorbed by each vehicle's structure differs by mass ratio and impact configuration.

## Wheel torque vs. engine torque

**Engine torque** is measured at the crankshaft/flywheel. **Wheel torque** is engine torque multiplied through the full gear reduction (transmission gear ratio × final-drive ratio) and driveline efficiency — the number that actually determines tractive force at the tire contact patch, and can be an order of magnitude larger than engine torque in a low gear.

**In use:** "350 N·m at the crank becomes nearly 4300 N·m at the wheel in first gear after the 3.5:1 and 3.9:1 reductions — that's the number to check against traction limits, not the crank figure."

**Common misuse:** comparing engine (crank) torque figures directly against traction or acceleration requirements without applying the gear reduction and driveline efficiency that actually convert it to usable wheel force.
