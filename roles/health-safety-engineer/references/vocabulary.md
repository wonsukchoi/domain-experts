# Vocabulary

Terms generalists flatten together that a health and safety engineer keeps sharply separate — the value is in the misuse, not the definition.

## Hazard vs. risk

A **hazard** is a source with the potential to cause harm (an unguarded pinch point, a pressurized vessel, a toxic chemical). **Risk** is the combination of that hazard's severity and the probability/exposure of it actually causing harm. A hazard can be present with low risk (a chemical stored below its threshold quantity, rarely handled) or absent with the risk conversation still needed (a process change that would introduce one).

**In use:** "The hazard hasn't changed — it's still a 480V panel — but the risk dropped once we added the interlock, because probability of contact went from likely to rare."

**Common misuse:** using "hazard" and "risk" interchangeably, which makes "we removed the hazard" and "we reduced the risk" sound like the same claim when they're different engineering outcomes.

## Hierarchy of controls

A ranked preference order for hazard controls: elimination, substitution, engineering controls, administrative controls, PPE — ranked by reliability, not by cost or speed of implementation. Each tier depends on every tier below it also failing before harm occurs.

**In use:** "We're not skipping to PPE — check whether the process can substitute the solvent before we spec respirators."

**Common misuse:** treating the hierarchy as a menu to pick from based on convenience rather than a default that requires justification to skip downward.

## Point of operation

The specific location on a machine where work is actually performed on the material — where cutting, forming, or shaping happens, and therefore where the point-of-operation guarding requirement (OSHA 1910.212, 1910.217) applies. Distinct from other pinch points or moving parts on the same machine, which fall under general machine-guarding requirements instead.

**In use:** "The point of operation is guarded by the light curtain; the flywheel still needs a separate fixed guard under 1910.212."

**Common misuse:** treating "the machine is guarded" as a single binary fact, when point-of-operation guarding and general machine guarding are separate requirements that can each independently pass or fail.

## Performance Level (PL) vs. Safety Integrity Level (SIL)

**Performance Level** (ISO 13849-1) rates the reliability of a machine safety function on a discrete safeguarding application (a-e scale). **Safety Integrity Level** (IEC 61508/61511) rates a safety instrumented function in a process context, typically expressed as Probability of Failure on Demand. Both answer "how reliable does this safety function need to be," but apply to different domains — PL to discrete machine safeguarding, SIL to process safety instrumented systems.

**In use:** "This is a press guard, so we need the PLr from B11.19's risk graph — SIL doesn't apply here, that's for the SIS on the reactor."

**Common misuse:** citing a SIL rating for a machine guard or a PL rating for a process safety instrumented function, mixing frameworks that use similar-sounding math but different standards and calculation methods.

## Independent Protection Layer (IPL)

A device, system, or human action in a LOPA scenario that is capable, on its own, of preventing the scenario's consequence, and that is independent of the initiating event and of every other credited layer (different sensor, different logic solver, different final element). A layer sharing a component with another credited layer isn't independent, even if it appears as a separate line on the cause-and-effect matrix.

**In use:** "The BPCS alarm and the SIS trip both read off the same transmitter — we can only credit one of them as an IPL."

**Common misuse:** crediting two protection layers that share an instrument, inflating the calculated risk reduction beyond what the hardware actually provides.

## Management of Change (MOC)

A documented review process (required under PSM, 1910.119(l)) triggered by any change to process chemistry, technology, equipment, or procedures — evaluating safety impact before the change is implemented, not after. A like-for-like replacement is generally exempt; anything that changes a parameter the original PHA assumed is not.

**In use:** "Swapping that control valve for a different manufacturer's model isn't like-for-like — route it through MOC before startup."

**Common misuse:** treating MOC as paperwork for major capital projects only, missing that a setpoint change or a substitute component can just as easily invalidate the assumptions behind an existing PHA.

## Process Hazard Analysis (PHA) vs. Job Safety Analysis (JSA)

A **PHA** is a systematic, team-based analysis (commonly HAZOP) of an entire process's hazards, required under PSM for covered processes and revalidated on a fixed cycle. A **JSA** (or JHA) is a task-level breakdown of the steps in a specific job, identifying the hazard and control at each step — narrower in scope, usually not tied to a regulatory revalidation cycle.

**In use:** "The PHA covers the reactor system as a whole; we still need a JSA for the operator's manual sampling task on that line."

**Common misuse:** treating a JSA as satisfying PSM's PHA requirement, or vice versa — they answer different-scoped questions and neither substitutes for the other.

## Threshold quantity (TQ)

The chemical-specific quantity listed in PSM's Appendix A (or the EPA's Risk Management Program list) above which a process handling that chemical becomes covered by the full regulatory program. Aggregation rules apply across interconnected vessels at one location.

**In use:** "We're at 8,000 lb of anhydrous ammonia on-site against a 10,000 lb threshold — still under, but the next expansion tips us over and triggers full PSM coverage."

**Common misuse:** checking a single vessel's quantity against the threshold without aggregating interconnected process quantities at the same location, understating actual on-site inventory.

## As Low As Reasonably Practicable (ALARP)

A risk-acceptance principle: risk is reduced until the cost, time, or difficulty of further reduction is grossly disproportionate to the additional risk reduction achieved — not reduced to zero, and not stopped at the first "acceptable" matrix score without considering whether a practicable further reduction exists.

**In use:** "The residual score is in the acceptable band, but adding the second check valve is low-cost and closes a credible failure mode — that's still ALARP territory, not gold-plating."

**Common misuse:** treating "acceptable" on the risk matrix as the finish line, rather than continuing to ask whether a reasonably practicable further reduction remains available.

## Guide word (HAZOP)

One of a fixed set of deviation prompts (no/none, more, less, as well as, part of, reverse, other than) applied systematically to each process parameter at each defined node, forcing coverage of deviation types a free-form brainstorm reliably skips.

**In use:** "Apply the 'reverse' guide word to the cooling water node — what happens on backflow, not just loss of flow."

**Common misuse:** running a HAZOP-labeled session without actually stepping through each guide word at each node, producing brainstorm-quality coverage under a HAZOP-quality label.

## Recordable vs. lost-time vs. first-aid case

A **recordable** case (29 CFR 1904.7) meets OSHA's threshold for logging on the 300 log — death, days away from work, restricted work, medical treatment beyond first aid, or several specific listed conditions. A **lost-time** case is a recordable subset involving days away from work. A **first-aid** case is explicitly excluded from recordability under 1904.7's first-aid treatment list, regardless of how serious the underlying incident felt.

**In use:** "Stitches make it recordable, not first aid — check the specific treatment against the 1904.7 list before logging it either way."

**Common misuse:** assuming severity of the underlying event determines recordability, rather than checking the specific treatment rendered against 1904.7's defined criteria.

## Safeguard vs. warning

A **safeguard** (guard, interlock, presence-sensing device) physically or functionally prevents access to a hazard. A **warning** (sign, light, alarm) informs a person of a hazard but does not prevent exposure — it depends on the person receiving and correctly acting on the information every time.

**In use:** "A warning label isn't a control for this hazard — we need an actual safeguard before this closes."

**Common misuse:** counting a warning as having addressed a hazard on the hierarchy of controls, when it sits below even administrative controls in reliability.
