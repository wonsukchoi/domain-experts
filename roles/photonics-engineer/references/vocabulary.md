# Vocabulary

### Beam waist (w0)
The radius (at the 1/e² intensity point) of a Gaussian beam at its narrowest point along the propagation axis.
**In use:** "We're solving for a 5.2 µm output waist to match the fiber's mode field radius, not just eyeballing a small spot."
**Common misuse:** treating "waist" and "spot size" as interchangeable with the beam's full diameter — the waist is a radius, and papers/datasheets mix 1/e² radius, 1/e² diameter, and FWHM conventions without always stating which.

### Rayleigh range (zR)
The distance from the beam waist over which the beam radius grows to sqrt(2) times its waist value — the practical extent over which a beam counts as "collimated." zR = π w0² / λ.
**In use:** "At w0 = 100 µm and 1550 nm, zR is about 2 cm — this beam is nowhere near collimated over the 1 m free-space hop we need."
**Common misuse:** assuming a beam described as "collimated" stays parallel indefinitely, instead of checking zR against the actual propagation distance.

### M² (beam quality factor)
The ratio of a real beam's beam-parameter product to that of an ideal (diffraction-limited) Gaussian beam of the same wavelength; M² = 1 is ideal, higher values mean the beam focuses to a larger spot and diverges faster than an ideal beam of the same waist.
**In use:** "This multimode pump diode has M² ≈ 25 — don't use the single-mode Gaussian focusing formula on it without the M² correction factor."
**Common misuse:** assuming M² = 1 for any laser without checking the datasheet or measuring it, which understates real focused spot size and overstates coupling efficiency.

### Mode field diameter (MFD)
The diameter of the guided optical mode in a single-mode fiber, larger than the physical core diameter because the mode extends into the cladding; the number that actually matters for coupling efficiency, not the core diameter.
**In use:** "SMF-28's MFD is 10.4 µm at 1550 nm — that's the number the coupling-lens calc needs, not the 8.2 µm core diameter."
**Common misuse:** using the fiber's core diameter instead of its MFD when sizing a coupling lens, which mis-sizes the target waist.

### Numerical aperture (NA)
A dimensionless measure of the range of angles over which a lens or fiber can accept or emit light; NA = n sin(θ), where θ is the half-angle of the accepted/emitted light cone.
**In use:** "The collimating lens needs an NA of at least 0.4 to capture this diode's full divergence angle without clipping the beam."
**Common misuse:** treating NA as directly comparable to f-number without converting (f/# ≈ 1/(2 NA) for small angles) — the two describe the same physical limit in different unit systems.

### Airy disk / diffraction limit
The central bright spot of the diffraction pattern formed when a beam or point source is focused or imaged by a finite-aperture lens; its diameter (2.44 λ f/#) is the smallest spot or resolvable feature an aberration-free lens can produce at that f-number and wavelength.
**In use:** "We're already at the Airy disk diameter for this f/2.8 lens — a better-corrected lens buys nothing further without going faster or shorter wavelength."
**Common misuse:** assuming a "sharper" or more expensive lens can always resolve finer detail, ignoring that diffraction — not lens quality — is the limiting factor once a system is diffraction-limited.

### f-number (f/#)
The ratio of a lens's focal length to its clear aperture diameter; a smaller f-number means a faster (larger-aperture-relative-to-focal-length) lens that focuses to a smaller diffraction-limited spot.
**In use:** "Dropping from f/8 to f/4 cuts the Airy disk diameter in half — that's the lever, not a different coating."
**Common misuse:** confusing a "faster" (smaller f/#) lens with a "better" one in every sense — faster lenses are typically harder to correct for aberrations and more expensive, a real tradeoff against the smaller diffraction spot.

### Insertion loss vs. return loss
Insertion loss is the optical power lost passing through a component (connector, splice, coupler), expressed in dB; return loss is the power reflected back toward the source at that same interface, also in dB but on a different scale where a larger number means less reflection.
**In use:** "This APC connector has 0.25 dB insertion loss and 60+ dB return loss — the low back-reflection is why we specified APC over UPC on this amplified link."
**Common misuse:** treating a low insertion-loss connector as automatically low-reflection — insertion loss and return loss are independent specs, and a UPC connector can have excellent insertion loss with far worse return loss than an APC of the same grade.

### OTDR event
A discrete reflective or loss feature (connector, splice, break, macrobend) visible as a spike or step in an optical time-domain reflectometer's backscatter trace, located by its round-trip time delay along the fiber.
**In use:** "The OTDR trace shows a 1.4 dB event at 34.2 km that isn't in the as-built splice log — that's the fault, not anything downstream."
**Common misuse:** reading OTDR trace distance directly without correcting for the fiber's actual group index, which shifts the apparent event location from the physical one.

### Nominal Ocular Hazard Distance (NOHD)
The distance from a laser source beyond which the beam's irradiance or radiant exposure drops below the applicable MPE for direct intrabeam viewing — the standard measure of how far a laser's naked-eye hazard extends.
**In use:** "NOHD for this beam is 1.7 mm — negligible for naked-eye viewing, but that number assumes no magnifying optic is ever pointed at it."
**Common misuse:** treating NOHD as covering all viewing conditions, when it's specifically a naked-eye, unaided-viewing calculation.

### Maximum Permissible Exposure (MPE)
The level of laser radiation (irradiance or radiant exposure) below which the probability of eye or skin injury is considered negligible, tabulated by wavelength band and exposure duration in ANSI Z136.1/IEC 60825-1.
**In use:** "MPE at 1550 nm for a 10+ second exposure is orders of magnitude higher than at 633 nm, because 1550 nm doesn't focus on the retina."
**Common misuse:** using one MPE value across different wavelengths or exposure durations instead of pulling the specific table entry for the actual source and scenario.

### Accessible Emission Limit (AEL)
The maximum output power or energy permitted for a laser product to remain within a given hazard class, defined per wavelength band and exposure condition in the classification standard.
**In use:** "500 mW CW is the commonly cited Class 3B/Class 4 boundary — above that, additional interlocks and PPE requirements apply regardless of wavelength."
**Common misuse:** assuming AEL class boundaries are the same fixed power value across all classes and wavelengths — only the 3B/4 boundary is close to wavelength-independent; the lower class boundaries vary substantially by band.

### Laser hazard class (1, 1M, 2, 2M, 3R, 3B, 4)
The IEC 60825-1/ANSI Z136.1 classification scheme ranking laser products by ocular/skin hazard under stated viewing conditions; the "M" designations (1M, 2M) specifically flag products that are safe unaided but hazardous when viewed through magnifying or beam-collecting optics.
**In use:** "This telecom transmitter is Class 1M — safe to look at directly, not safe to inspect with a fiber-scope loupe without an attenuating filter."
**Common misuse:** treating "Class 1" and "Class 1M" as equivalent because both are described as "eye safe" — 1M carries an explicit instrument-viewing restriction that plain Class 1 doesn't.

### Thermal lensing
A power-dependent change in an optic's or gain medium's effective focal length caused by a temperature gradient (and the resulting refractive-index gradient) from absorbed optical power.
**In use:** "Focus shifts by 15 µm between 2 W and 20 W output and recovers fully after a five-minute cooldown — that's thermal lensing in the gain crystal, not a drifted mount."
**Common misuse:** diagnosing a power-dependent, reversible focus or beam-quality shift as a mechanical alignment problem, which sends the fix down the wrong path (re-torquing a mount that was never loose).

### Chromatic dispersion vs. modal dispersion
Chromatic dispersion is pulse spreading in a fiber from different wavelengths within a source's spectrum traveling at different group velocities; modal dispersion is pulse spreading from different propagation modes in a multimode fiber traveling different path lengths. Different fiber types, different fixes.
**In use:** "This is single-mode fiber, so modal dispersion isn't in play — the eye closure at high data rate is chromatic dispersion, and we're specifying a narrower-linewidth source to fix it."
**Common misuse:** applying a multimode-fiber modal-dispersion fix (like a mode conditioning patch cord) to a single-mode chromatic-dispersion problem, or vice versa — the two mechanisms are unrelated and need different corrective actions.

### Bend loss (macrobend / microbend)
Macrobend loss is optical power lost when a fiber is bent to a radius tighter than its specified minimum bend radius, letting light escape the core; microbend loss is loss from small-scale random bends, typically from cabling or installation pressure, distributed along the fiber's length.
**In use:** "The macrobend loss at that 90-degree turn is 1.8 dB — that's the missing loss in the OTDR trace, not a bad splice."
**Common misuse:** attributing a distributed, gradual loss increase along a cable run to a single splice or connector event, when the actual cause is microbending from cable installation tension or a tight cable-tray radius.

### Fresnel reflection
The partial reflection of light at any interface between two materials of different refractive index (glass-to-air at a fiber end face, lens surface, etc.), independent of surface flatness or polish quality.
**In use:** "That unmated connector's 4% Fresnel reflection is the -14 dB return-loss spike on the OTDR trace, not a bad splice further down the line."
**Common misuse:** assuming an anti-reflection coating eliminates Fresnel reflection entirely — a good AR coating reduces it substantially (to a fraction of a percent) but doesn't remove it, and the residual is still budgeted in a high-return-loss link.
