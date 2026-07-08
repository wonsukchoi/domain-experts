# Vocabulary

Terms a cross-disciplinary generalist reaches for constantly and flattens together — each with the misuse that lets a marginal design or an unowned interface pass review.

## Factor of safety vs. margin of safety

**Factor of safety (FoS)** is a ratio: failure load ÷ maximum expected load (or allowable capacity ÷ demand). **Margin of safety (MoS)** is that same relationship expressed as MoS = FoS − 1, i.e. the fractional reserve capacity *beyond* the expected load. An FoS of 1.2 sounds comfortably above "passing" (1.0) but is only a 20% margin — thin enough that a single unmodeled load case can erase it.
**In use:** "FoS 1.2 on that connection isn't a lot of headroom — that's 20% margin, not 120%."
**Common misuse:** quoting the FoS number alone as if it were the margin, which overstates the actual reserve by a full 1.0 and hides how little slack an "acceptable" design really carries.

## Load path vs. load case

**Load path** is the physical route a force travels from where it's applied to where it's ultimately resisted (foundation, anchor, ground) — which members and connections carry it, in order. **Load case** is a specific defined combination of loads (dead + live + wind, dead + seismic, etc.) the structure or system is analyzed against. A substitution can leave every load case's magnitude unchanged while completely rerouting the load path through a different, unverified connection.
**In use:** "The two-rod split didn't change any load case — it changed the load path. That upper connection now carries load it was never designed to see."
**Common misuse:** treating "no load case changed" as proof nothing needs re-verification, when the failure mode lives in the path a load travels, not the magnitude tables.

## Verification vs. validation

**Verification** asks "did we build the thing right?" — does the deliverable meet its stated requirements/specification. **Validation** asks "did we build the right thing?" — does it meet the actual need in its intended use environment. A system can pass every verification test against its written spec and still fail validation if the spec itself was wrong or incomplete.
**In use:** "This module verifies clean against every requirement in the ICD — but nobody's validated that the ICD's units convention matches what the other team's software actually expects."
**Common misuse:** using "verified" and "validated" interchangeably, so a fully spec-compliant deliverable is assumed safe for its real-world use case without ever checking the spec against that use case.

## Traceability

The checkable link from a requirement to the specific test or inspection that confirms it was met (the V-model's left-leg-to-right-leg connection). No named verification method attached means it's a wish-list entry, not a requirement.
**In use:** "No line in the verification matrix points back to this requirement — untraceable, so nobody's on the hook to confirm it."
**Common misuse:** treating the requirements doc and the test plan as separately complete, without checking every requirement in the first has a named counterpart in the second.

## Interface Control Document (ICD) vs. spec

A **spec** describes what one component or subsystem must do on its own. An **ICD** describes the boundary between two components or teams specifically — units, tolerances, data formats, connector pinouts, timing — the things that only matter because two parties have to agree on them. A component can be perfectly spec-compliant and still fail at an interface if the ICD was never written or never enforced.
**In use:** "Both sides met their own spec. Nobody wrote an ICD stating the units convention, so 'met spec' didn't stop a 4.45x unit mismatch at the handoff."
**Common misuse:** assuming that if both sides of an interface separately meet their own specs, the interface between them is automatically sound — the ICD is a distinct deliverable, not a byproduct of two good specs.

## Tolerance stack-up

The cumulative dimensional or performance variation that results when several individually-toleranced parts or measurements are combined in series. Each part can be within its own individual tolerance and the assembly can still fail to fit or function because the tolerances stacked in the same direction.
**In use:** "Each of these five shims is within its printed tolerance — but stack them worst-case and you're 0.4 mm outside the assembly's fit-up window."
**Common misuse:** checking each component's tolerance in isolation and concluding the assembly is fine, without running the worst-case (or statistical) stack-up across the full chain of parts.

## Derating

Deliberately operating a component below its rated maximum (current, voltage, temperature, pressure) to extend its service life or absorb conditions the rating doesn't fully capture — a design choice, not evidence the original rating was wrong. A part run at its rated maximum continuously is not "meeting spec with margin," it's running at zero derating margin.
**In use:** "We're derating this power supply to 70% of nameplate for continuous duty — the nameplate rating assumes intermittent load, and this application isn't intermittent."
**Common misuse:** treating a component's nameplate/catalog rating as the safe continuous operating point in every application, rather than checking whether the rated duty cycle matches the actual use case and derating accordingly.

## Single point of failure (SPOF)

A single component, connection, or interface whose failure alone — with no other contributing fault — takes down the whole system or safety function. Redundancy only eliminates an SPOF if the redundant path is independent; two paths that share one unrecognized common element (one power feed, one control signal, one unowned interface) are not actually redundant.
**In use:** "We've got two pumps, but they both draw from the same control signal — that signal is still a single point of failure for the whole redundant pair."
**Common misuse:** counting a system as "redundant" because it has duplicate hardware, without tracing whether the duplicates share an unexamined common dependency that reintroduces the single point of failure.

## Root cause vs. proximate cause

**Proximate cause** is the immediate mechanical event that triggered a failure (the connection sheared). **Root cause** is the upstream process gap that let that event become possible (a substitution nobody re-verified). Fixing only the proximate cause reproduces the same failure with different hardware next time.
**In use:** "Proximate cause: the sheared hanger rod. Root cause: shop-drawing substitutions don't route back through the engineer of record — fix that, or this repeats."
**Common misuse:** closing an incident report at what broke, without tracing back to what let the unverified change through in the first place.

## Design basis vs. design intent

**Design basis** is the documented set of loads, codes, assumptions, and criteria a design was actually calculated against — a specific, checkable list. **Design intent** is the more general functional goal the design was meant to achieve. A substitution can still serve the design intent ("hold the catwalk up") while violating the design basis (the specific load path and connection capacity that calculation relied on).
**In use:** "The fabricator's swap still serves the design intent — the catwalk still hangs. It violates the design basis, because that connection was never calculated for the load it now carries."
**Common misuse:** approving a change because it doesn't obviously contradict the design intent, without checking it against the specific, documented design basis the original calculation used.

## Boundary condition

The stated assumption about how a component is supported, restrained, or connected at its edges, which the entire internal calculation depends on (fixed, pinned, free, continuous). Changing how a part is actually connected in the field — without updating the calculation's boundary condition — invalidates the calculation even if every other input stays the same.
**In use:** "That beam was calculated as continuous over two supports. Field-splicing it there turns it into two simply-supported spans — the boundary condition changed, so the original moment calculation no longer applies."
**Common misuse:** assuming a calculation still holds after a field change to how a part is physically connected, without checking whether that change altered the boundary condition the calculation assumed.

## Competency boundary (five-of-seven / OPM 0801)

The documented threshold — for a General Engineer, the OPM 0801 standard's five-of-seven core coursework areas (statics/dynamics, strength of materials, fluid mechanics, thermodynamics, electrical fields/circuits, materials science, or a comparable area) — past which a problem requires a named specialist rather than analogical reasoning. It is a scope boundary tied to a specific qualifying standard, not a general sense of "how confident I feel."
**In use:** "This is a heat-transfer problem outside my five areas — I can scope it, but the calculation itself routes to a thermal specialist."
**Common misuse:** treating "I've seen something like this before" as equivalent to formal competency in the area, instead of checking the problem against the specific credentialed boundary and routing it when it falls outside.
