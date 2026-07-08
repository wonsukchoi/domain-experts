# Vocabulary

### Reference frame vs. datum
A datum (e.g., NAD83) is a model of the Earth's shape and an origin/orientation choice; a reference frame is a specific, dated realization of that datum built from actual station coordinates (e.g., NAD83(2011)) that changes slightly with each readjustment.
**In use:** "NAD83 is the datum, but NAD83(2011) at epoch 2010.00 is the actual frame this project is delivered in — those aren't interchangeable."
**Common misuse:** treating "NAD83" as one fixed set of numbers instead of a family of realizations that differ from each other by measurable amounts.

### Epoch
The specific date to which a set of coordinates applies, needed because points on the Earth's surface move continuously relative to a global reference frame.
**In use:** "This mark's published position is epoch 2010.00 — anything observed today needs to be reduced to that epoch or the comparison is meaningless."
**Common misuse:** omitting the epoch entirely, as if a coordinate were valid indefinitely rather than a snapshot.

### NSRS (National Spatial Reference System)
NGS's official, consistent national coordinate system — the network of published horizontal, vertical, and gravity control that all federally-recognized geodetic work ties back to.
**In use:** "The client wants this tied to the NSRS, not just internally self-consistent — that means it has to connect to published control, not a local arbitrary origin."
**Common misuse:** treating any GPS-derived coordinate as automatically "on the NSRS" regardless of whether it was ever tied to published control.

### CORS (Continuously Operating Reference Station)
A permanent GNSS station, part of the national CORS network, that continuously logs data usable as a fixed reference for processing other GNSS observations.
**In use:** "We're baselining to three CORS at 18, 24, and 31 km rather than relying on one."
**Common misuse:** assuming any nearby permanent GNSS station qualifies as a CORS with NGS-grade coordinate quality, without checking its actual status.

### OPUS (Online Positioning User Service)
NGS's free web service that processes a static GNSS observation file against nearby CORS and returns a coordinate solution with quality metrics.
**In use:** "Run both sessions through OPUS separately before combining anything — that's how we catch a bad session before it enters the adjustment."
**Common misuse:** treating a single OPUS solution as a finished, adjustment-grade coordinate rather than one input session requiring an independent check.

### Order and class
The relative-accuracy classification assigned to a control point or network — historically a classical traverse/triangulation table (1st, 2nd Class I/II, 3rd Class I/II), now typically the separate GPS relative-positioning table (AA/A/B) for GNSS-observed work.
**In use:** "This achieves B-order, not A-order — check which table the spec is actually citing before comparing numbers."
**Common misuse:** applying the classical order/class distance-error formula to a GPS baseline, or vice versa — the two tables aren't interchangeable.

### Minimally-constrained adjustment
A least-squares network adjustment that fixes only enough parameters (position and orientation, not scale from external control) to solve the network, used to check the observations' internal consistency before trusting any external control.
**In use:** "The minimally-constrained run flagged a 4 cm residual on that baseline — we found the bad antenna height before it touched the final coordinates."
**Common misuse:** skipping straight to a fully-constrained adjustment, which hides a bad control point's error by distributing it across the whole network.

### Fully-constrained adjustment
A least-squares network adjustment that fixes the network to external control (published NSRS coordinates), producing final publishable coordinates.
**In use:** "Once the minimally-constrained pass came back clean, we ran it fully-constrained against the three CORS."
**Common misuse:** treating the fully-constrained result as validation of the observations, when it can only validate them if the minimally-constrained pass was checked first.

### Geoid undulation (N)
The vertical separation between the mathematical ellipsoid (what GNSS measures against) and the geoid (the equipotential surface approximating mean sea level, what "elevation" means in practice), at a given location.
**In use:** "N here is about −29 m — that's not a rounding error, it's the geoid model doing its job."
**Common misuse:** assuming N is a small, ignorable correction; it varies regionally and can exceed a meter of change over tens of kilometers.

### Ellipsoidal height (h) vs. orthometric height (H)
h is the direct GNSS-measured height above the reference ellipsoid; H is height above the geoid ("elevation" in the conventional sense), related by H = h − N.
**In use:** "The receiver gives you h — don't hand that to the engineer as elevation without subtracting the geoid model's N first."
**Common misuse:** using h and H interchangeably, especially when a GNSS unit's screen just says "height" with no qualifier.

### PID (Permanent Identifier)
NGS's unique code for a specific control station, used to look up its datasheet, published coordinates, and adjustment history.
**In use:** "Pull the datasheet for PID AB1234 before we plan to use it as control — check the superseded date."
**Common misuse:** referring to a mark only by a local project name, losing the ability to trace it back to its authoritative NGS record.

### ARP (Antenna Reference Point)
The specific physical point on a GNSS antenna to which the manufacturer's calibration model assumes height measurements are made — not necessarily the base of the antenna or an obvious visual point.
**In use:** "Confirm which ARP this antenna's calibration file assumes before we trust the recorded height."
**Common misuse:** measuring antenna height to a convenient point rather than the exact reference point the receiver's calibration expects, introducing an offset the adjustment can't detect on its own.

### Baseline (GNSS vector)
The three-dimensional vector between two simultaneously-observing GNSS receivers, derived from carrier-phase processing — the fundamental observation in static GNSS surveying, not a single point's coordinate.
**In use:** "We need three independent baselines forming a closed loop here, not three unrelated point solutions."
**Common misuse:** thinking of GNSS results as independent point positions rather than as vectors between pairs of stations that only become coordinates after a network adjustment.

### Error ellipse (95% confidence)
The elliptical region around an adjusted point's coordinate, defined by semi-major and semi-minor axis lengths, within which the true position falls at a stated confidence level — the standard way network/local accuracy is reported for a 2D position.
**In use:** "Semi-major axis is 1.9 cm at 95% confidence — that's the number that goes in the accuracy statement, not a single circular tolerance."
**Common misuse:** reporting a single scalar "accuracy" number when the actual uncertainty is directionally asymmetric and better described by the two axis lengths.

### NAPGD2022 / NATRF2022
NGS's ongoing modernization of the National Spatial Reference System, replacing NAD83 and NAVD88 with new terrestrial reference frames (e.g., NATRF2022 for the conterminous US) and a new gravimetric geoid model (GEOID2022), directly tied to a global reference frame rather than a plate-fixed one.
**In use:** "Once NATRF2022 is adopted here, this project's NAD83(2011) coordinates will need a formal transformation, not just a relabel."
**Common misuse:** assuming the transition is a simple renaming rather than a genuine reference-frame change with its own transformation parameters.
