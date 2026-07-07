# Vocabulary

Terms generalists conflate or use loosely that a practitioner keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse to avoid.

## Rekey vs. replace

**Rekey** changes the internal pin/wafer combination of an existing cylinder so old keys stop working and new ones do, reusing the same hardware. **Replace** swaps the entire lock body/cylinder for new hardware, usually to change grade, brand, or keyway, or because the existing hardware is damaged.

*Practitioner usage:* "Teardown's clean and it's at 40% of rated cycle life — this is a rekey, not a replace, unless you specifically want the grade bump."

*Common misuse:* treating "rekey" and "replace" as interchangeable quotes for the same problem, or assuming rekey is always available regardless of a compromised master-level cut (it isn't cheaper if the whole system's hierarchy needs re-pinning).

## Master key vs. grand master key vs. change key

**Change key** operates one specific cylinder only. **Master key** operates every cylinder pinned to accept it, typically all units in one building or zone. **Grand master key** sits a level above multiple master keys, operating across zones (e.g., every building in a complex) whose individual masters don't operate each other's doors.

*Practitioner usage:* "His key was cut to the building master, not a unit change key — that's why all 36 cylinders are in scope, not just the doors he used."

*Common misuse:* calling any key that opens more than one door a "master key" regardless of its actual position in the hierarchy, which understates or overstates the rekey scope needed when a key goes missing.

## MACS (Maximum Adjacent Cut Specification)

The maximum permitted difference in cut depth between two adjacent chambers on a key, set by the cylinder manufacturer to prevent the key from binding or the pins from jamming during insertion.

*Practitioner usage:* "Check this pin kit's actual MACS before you cut that combination — don't assume 7 just because that's the Schlage-pattern number."

*Common misuse:* applying a memorized MACS value across cylinders from different manufacturers or pin-kit families without checking the specific chart, producing a key that binds or won't turn smoothly.

## TPP (Total Position Progression)

The standard method for designing a master key system: systematically assigning cut depths across chambers so that change keys, masters, and (if applicable) grand masters all operate their intended cylinders without unintended cross-operation.

*Practitioner usage:* "Run the TPP worksheet before you cut anything — figure out how many chambers you can afford to split before you start pinning cylinders."

*Common misuse:* skipping the worksheet and pinning cylinders ad hoc, discovering cross-keying (a key opening a door it shouldn't) only after the system is already installed.

## Cross keying

An unintended condition where a key operates a cylinder it wasn't designed to, usually from a pinning error or from squeezing too many hierarchy levels into too few chambers.

*Practitioner usage:* "That's cross keying, not a coincidence — unit 4B's key shouldn't turn in 4C's lock, and it does because we ran out of splittable chambers."

*Common misuse:* assuming cross keying only happens by hardware defect; it's most often a design-side consequence of over-mastering a system with too few chambers for the number of hierarchy levels requested.

## Bump key vs. pick vs. impressioning

A **bump key** is cut to the maximum depth at every chamber and struck to momentarily separate the pin stacks at the shear line. **Picking** manipulates each pin individually with a tension wrench and pick to find the shear line. **Impressioning** cuts a blank key progressively based on marks left by turning it under tension in the target lock, without disassembly.

*Practitioner usage:* "Bump resistance and pick resistance are tested and rated separately — a cylinder can be UL 437-listed for pick resistance and still be vulnerable to bumping if it isn't specifically bump-resistant."

*Common misuse:* treating "pick-resistant" as a blanket claim covering all attack methods; each method (bumping, picking, impressioning) has its own resistance mechanism and its own rating claim.

## ANSI/BHMA Grade 1 / 2 / 3

The ANSI/BHMA A156.2 tiered rating for bored and preassembled door locks, based on operational cycle testing and security/strength tests: Grade 1 (~800,000 cycles, highest security tests) for high-traffic commercial and high-security use; Grade 2 (~400,000 cycles) for light commercial and heavy residential; Grade 3 (~200,000 cycles) for standard residential.

*Practitioner usage:* "That's Grade 3 builder-grade hardware on a door 200 people use a day — it's not a defect, it's the wrong grade for the traffic."

*Common misuse:* treating "commercial" and "residential" labels on packaging as equivalent to the grade, when the grade and the marketing label don't always match, and traffic — not occupancy type — is what determines the right grade.

## UL 437 vs. UL 768

**UL 437** is the standard for key-operated (pin tumbler and similar) burglary-resistant locks, testing pick, drill, and pry resistance. **UL 768** is the standard for mechanical combination locks, testing manipulation and X-ray resistance.

*Practitioner usage:* "The cylinder's UL 437-listed; the safe's dial is UL 768 Group 1 — two separate listings, don't quote one number for both components."

*Common misuse:* citing a single "UL-rated" claim for a product that has a key lock and a combination lock, when each mechanism carries its own separate listing under a different standard.

## Burglary rating (UL 687) vs. fire rating (UL 72)

**UL 687** rates a safe's resistance to forced physical entry by tool class and net working time (TL-15, TL-30, TRTL-60, etc.). **UL 72** rates how long a safe's interior stays below a damaging temperature threshold during a standardized fire exposure (Class 350, 1-hour/2-hour). A safe can carry one, both, or neither listing.

*Practitioner usage:* "This box is TL-30, no UL 72 listing at all — great for cash and jewelry, does nothing for the paper documents your customer also wants to store."

*Common misuse:* assuming any "safe" protects against both theft and fire by default, or recommending a burglary-rated box for a customer whose actual stated concern is fire protection for documents.

## Shear line

The point inside a pin tumbler cylinder where the gap between the top pins and bottom (or key) pins aligns exactly with the edge of the plug, allowing it to rotate — the mechanical basis of every pin tumbler lock's function and every picking/bumping attack against one.

*Practitioner usage:* "Every master wafer you add is one more shear line the plug has to line up, and one more point a pick can feel for."

*Common misuse:* treating "shear line" as a synonym for "keyway" or "lock mechanism" generally, rather than the specific alignment point that determines whether the plug turns.

## Rotating constant

In a master-keyed system, a chamber deliberately left unsplit (no master wafer) across every cylinder in the system, holding the same cut depth everywhere to preserve a security floor that isn't weakened by progression.

*Practitioner usage:* "Chamber one stays a rotating constant on this whole system — that's the one shear point that isn't also carrying a master-level split."

*Common misuse:* treating every chamber as available for master-wafer progression to maximize the number of possible change keys, without reserving any unsplit chamber, which measurably weakens the system's pick resistance.
