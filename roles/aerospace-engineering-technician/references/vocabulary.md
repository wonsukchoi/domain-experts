# Vocabulary

Terms generalists flatten together that this role keeps sharply separate — the value is in the misuse, not the definition.

## Torque vs. preload

Torque is the rotational force applied to a fastener during installation, measured at the wrench. Preload is the resulting axial clamping force in the fastener, which is what actually holds the joint. The two are related by T = K·D·F, where K (friction coefficient) is highly sensitive to lubrication and finish.

**In use:** "We torqued to 340 in-lb, but the preload that delivers depends on whether this bolt is dry or lubed — check the finish before you log it as verified."

**Common misuse:** treating "torqued to spec" as equivalent to "preload verified" — the torque value alone says nothing about delivered preload without a known K.

## K-factor

The empirical friction/nut-factor coefficient relating applied torque to axial preload in T = K·D·F. It is a property of the fastener's finish, lubrication state, and reuse history, not a universal constant.

**In use:** "This is a re-installed bolt with anti-seize on the threads — use the lubricated K, not the dry value from the drawing note."

**Common misuse:** applying a single K-factor from a general reference table to every fastener regardless of its actual as-installed finish and lubrication condition.

## Gauge factor (GF)

The proportionality constant relating a strain gauge's fractional resistance change to strain: GF = (ΔR/R) / ε. It's specific to each gauge lot and is printed on the gauge's packaging.

**In use:** "Confirm the GF entered in the DAQ software matches this lot's packaging value, not last month's lot — a wrong GF silently scales every strain reading."

**Common misuse:** leaving a default or previous lot's GF entered in the acquisition software instead of the value specific to the gauges actually bonded for this test.

## Microstrain (µε)

Strain expressed in millionths (10^-6) — the practical unit for structural test strain, since raw strain values (e.g., 0.00132) are awkward to read and log. 1,320 µε = 0.00132 strain.

**In use:** "Peak reading was 1,321 microstrain at limit load — convert that to stress before comparing it to the yield allowable."

**Common misuse:** reporting a raw strain value in scientific notation on a test record instead of the microstrain convention practitioners actually read and compare against.

## Rosette (strain gauge)

A set of two or three gauges bonded at fixed angles (commonly 0°/45°/90°) at a single location to recover the full in-plane strain state, from which principal strains and stresses are computed — a single uniaxial gauge cannot do this.

**In use:** "The lug radius is a biaxial stress location — spec a rosette there, not a single gauge."

**Common misuse:** substituting a single uniaxial gauge at a location the test plan calls out for a rosette, then reporting its raw strain as if it were the principal stress.

## Margin of safety (MS)

The fractional (or percentage) reserve between an allowable value and the applied/predicted value: MS = (allowable / applied) − 1. A positive MS means the structure clears the requirement; MS = 0 is the limiting case.

**In use:** "MS against Fty at limit load came out to +3.88 — comfortably positive, ultimate load is the governing case here, not this test point."

**Common misuse:** computing MS against the wrong allowable (yield when ultimate governs, or vice versa) or against the wrong load case (limit when ultimate is the actual design driver).

## Limit load vs. ultimate load

Limit load is the maximum load expected in service; the structure must sustain it without detrimental permanent deformation. Ultimate load is limit load times a safety factor (commonly 1.5 in civil aviation structures); the structure must sustain it for at least 3 seconds without failure, deformation not required to be recoverable.

**In use:** "This test point is at 100% limit load — no permanent set expected. Ultimate load test is a separate point later in the sequence, and that's where we expect to see it start yielding."

**Common misuse:** treating a positive margin at limit load as proof the structure is adequate at ultimate load — they're different load cases with different acceptance criteria.

## Test uncertainty ratio (TUR)

The ratio of the tolerance band being verified to the measuring instrument's uncertainty. A TUR below the applicable threshold (commonly 4:1, sometimes stated as 10:1 in older or more conservative quality manuals) means the instrument's own noise is too large a fraction of the tolerance to draw a reliable pass/fail conclusion.

**In use:** "TUR on this torque wrench against the ±20 in-lb tolerance band is only 3:1 — pull a better-calibrated wrench before we sign this off."

**Common misuse:** citing an instrument's calibration as "current" without checking whether its stated uncertainty is actually small enough, relative to the specific tolerance being verified, to trust the reading.

## First article inspection (FAI)

A complete, ballooned-drawing verification of every characteristic on a part's engineering drawing against a first-produced (or first-after-change) unit, per AS9102. It is a full accountability record, not a sample inspection.

**In use:** "FAI on this bracket needs every GD&T callout and material note ballooned, not just the three critical dimensions."

**Common misuse:** treating "FAI complete" as satisfied by inspecting only the characteristics judged likely to fail, leaving the rest of the drawing's callouts unverified against the actual part.

## NDI vs. NDT

Nondestructive inspection (NDI) and nondestructive testing (NDT) are used near-interchangeably in practice, but NDI in aerospace maintenance/production contexts usually refers to the specific inspection task against a defined accept/reject standard, while NDT is the broader discipline/method family (penetrant, eddy current, ultrasonic, radiographic, magnetic particle).

**In use:** "Run the NDI per the process spec's eddy current procedure — that's the specific method and acceptance criteria for this part."

**Common misuse:** naming "NDT" on a work order without specifying which method, leaving the technician to choose one that may not be sensitive to the defect type the drawing intends to screen for.

## Dynamic pressure (q)

The kinetic-energy-per-volume term in aerodynamic force equations: q = 0.5·ρ·V². It's the quantity force coefficients (CL, CD) are normalized against, not the static or total pressure.

**In use:** "Tunnel dynamic pressure at this test point was 55.25 psf — that's what we divide the measured lift by to get CL."

**Common misuse:** confusing dynamic pressure with the tunnel's static or stagnation (total) pressure reading, which are different quantities on the same pitot-static instrumentation.

## Reynolds number (Re)

The dimensionless ratio of inertial to viscous forces in a flow: Re = ρ·V·L/μ. It governs boundary-layer behavior (laminar vs. turbulent, separation), and a test article's aerodynamic coefficients only extrapolate reliably to another Reynolds number within a validated correlation range.

**In use:** "Test Re was 2.08 million against a flight Re of 12 million — flag the CL comparison as outside our correlated range until we run the higher-Re entry."

**Common misuse:** comparing test-measured force coefficients directly against a flight-condition prediction without checking whether the Reynolds numbers are close enough for the comparison to be valid.

## Lift-off (eddy current)

The gap between an eddy current probe and the part surface, which strongly attenuates the signal — even a thin coating or surface roughness variation changes the reading independent of any actual flaw.

**In use:** "The indication amplitude dropped when we rescanned near the fastener head — check for a lift-off effect from the sealant fillet before calling it a flaw."

**Common misuse:** reading an eddy current amplitude change as a defect indication without first ruling out a lift-off variation from coating thickness, surface roughness, or probe angle.

## Wet torque vs. dry torque

Torque values computed or specified assuming a lubricated (wet) versus unlubricated (dry) fastener condition. The same torque number delivers substantially different preload depending on which K-factor regime the fastener is actually in.

**In use:** "Drawing note doesn't specify — confirm with engineering whether this is a wet or dry torque callout before we install with anti-seize."

**Common misuse:** assuming a torque value is dry by default (or wet by default) without checking the drawing note or work order, when the two conventions can differ in delivered preload by 30% or more at the same torque.
