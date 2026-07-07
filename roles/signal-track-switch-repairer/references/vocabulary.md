# Vocabulary

Terms generalists conflate that a signal maintainer keeps sharply separate, because the difference changes what was actually verified or what's actually protecting a train movement.

## Fail-safe vs. redundant

**Fail-safe** means a specific failure mode (broken wire, dead coil, lost power) drives the system to the most restrictive state by the physical properties of the design, not by a second system catching the first one's mistake. **Redundant** means two independent systems perform the same check so that one covers for the other's failure. A track circuit is fail-safe on its own; PTC adds redundancy on top of it, but the track circuit doesn't need PTC to be fail-safe.

**In use:** "PTC being down doesn't make this track circuit unsafe — the track circuit is fail-safe by itself. PTC is the redundant layer on top, not the thing making the base circuit safe."

**Common misuse:** treating a redundant overlay (PTC, a second detection system) as what makes the underlying system fail-safe, when the underlying system has to be fail-safe independent of whether the overlay exists.

## Shunting sensitivity vs. track circuit "working"

**Shunting sensitivity** is the specific, numeric property of whether the track circuit reliably detects a 0.06-ohm shunt (a train's wheel-axle resistance) anywhere in the circuit, per 49 CFR 236.56. A track circuit "working" in the sense of showing correct signals during normal traffic can still have degraded shunting sensitivity that hasn't been exposed yet by the right combination of ballast condition and train position.

**In use:** "The signals have looked normal all week, but that doesn't tell you anything about shunting sensitivity — we test that specifically, with the calibrated shunt, at more than one point in the circuit."

**Common misuse:** treating normal-looking signal operation as evidence that shunting sensitivity is fine, when the two are only loosely correlated until a marginal condition is actually tested for.

## Ballast resistance vs. ballast condition

**Ballast resistance** is a measured electrical value (ohms per 1,000 feet) describing how much current leaks from rail to rail through the ballast bed. **Ballast condition** is the general physical state of the ballast (clean, fouled, vegetation-choked) that a track inspector assesses visually. Ballast can look reasonably clean and still test electrically low if it's fouled with a conductive contaminant like coal dust or de-icing salt, which isn't always obvious by eye.

**In use:** "The ballast looks fine to the eye at that location, but it tested at 0.4 ohms per 1,000 feet against a 2-ohm design minimum — pull a resistance test before assuming visual condition tells you the electrical story."

**Common misuse:** substituting a visual ballast inspection for an actual resistance measurement when diagnosing a marginal track circuit.

## Switch point fit vs. switch throw-and-lock function

**Switch point fit** is the geometric condition of the point closing tight against the stock rail with no gap a wheel flange can enter. **Throw-and-lock function** is whether the switch machine correctly moves the points and locks them in position, verified through the circuit controller. A switch can pass a throw-and-lock test every time and still have a point fit failure, because the two are checked by different tests against different failure modes.

**In use:** "Circuit controller test passed, the switch throws and locks fine — but that's not the same test as the point-to-rail fit measurement, which is what actually tells you if a wheel can split this switch."

**Common misuse:** treating a passing throw-and-lock/circuit controller test as evidence the switch point geometry is also fine.

## Most restrictive aspect vs. "the signal is red"

**Most restrictive aspect** is the specific, ranked signal indication a system defaults to on a given failure, per the signal's aspect chart for that location — which is not always a literal red light; it can be a restricting aspect, an approach aspect, or a cab-signal restrictive code depending on the system. **"The signal is red"** is the layperson's shorthand that assumes a single universal fail-safe output.

**In use:** "This location's most restrictive aspect on a track circuit failure is Approach, not Stop, because of how the signal is designed into the block system here — check the aspect chart before assuming what 'fail-safe' looks like on this signal."

**Common misuse:** assuming every signal system's fail-safe default is a literal stop indication, rather than checking the specific aspect chart for that location and system type.

## Wayside interface unit (WIU) status vs. vital test result

**WIU status** is what a PTC wayside interface unit reports to the back office about a track circuit or switch's current state, based on what the WIU itself can sense. **Vital test result** is the outcome of an independent, code-mandated test (236.56 shunting sensitivity, switch-point geometry, relay test) run by a signal maintainer against a specific numeric threshold. A WIU reporting "healthy" is not evidence that the underlying vital test has been run or passed.

**In use:** "PTC dashboard shows this switch as normal, but that's WIU status, not a vital test result — when did we last actually run the point-geometry check here?"

**Common misuse:** treating PTC/WIU health monitoring as a substitute for the underlying signal system's own periodic vital tests, rather than as an additional, separately-verified layer.

## Vital circuit vs. non-vital circuit

**Vital circuit** is any circuit whose failure could permit an unsafe train movement (track circuits, switch position detection, interlocking logic) — governed by 49 CFR 236's fail-safe requirements and subject to the periodic test intervals in that part. **Non-vital circuit** performs a function (indication lights, office alarms, data logging) whose failure degrades convenience or information but can't itself authorize an unsafe movement. The distinction determines which test intervals, documentation, and defeat-protection rules apply.

**In use:** "The alarm panel feed is non-vital — fix it on the next visit. The switch point detector feeding that same panel is vital — that one needs protection in place before you touch it, today."

**Common misuse:** assuming a circuit's priority for repair tracks its vital/non-vital status, when a low-priority-feeling indication light can share wiring with a vital detection circuit and needs the same defeat-protection discipline.

## Blunt face vs. flat spot (switch point wear)

**Blunt face** describes wear along the point's leading edge where it should taper to a thin, sharp profile against the stock rail — measured as a width along the closed rail. **Flat spot** describes a worn or chipped area lower on the point's running surface, measured as a width at a specified depth (3/4 inch) below the top of rail. Both are wear conditions on the same component, but they're measured differently and have different thresholds (3/16 inch for blunt face, 5/16 inch for flat spot), and a point can fail one without failing the other.

**In use:** "The blunt face measured out at 0.22 inch, over the 3/16-inch line, even though the flat-spot measurement at 3/4-inch depth came in under 5/16 — that's still a failing point, on the blunt-face criterion alone."

**Common misuse:** checking only one of the two measurements and assuming it stands in for the other.
