# Vocabulary

Terms generalists flatten together that an electrical/electronics drafter keeps sharply separate — the value is in the misuse, not the definition.

## One-line diagram vs. elementary (three-line) diagram

A **one-line diagram** represents an entire power system (utility feed through main disconnect, feeders, panels) with a single line standing in for all phase conductors — a system-coordination view. An **elementary diagram** (also "three-line" or "schematic") draws each phase conductor separately and includes the full control/relay logic — a buildable, field-wiring-level view.

**In use:** "The one-line's fine for the coordination study, but the electrician needs the elementary to actually wire the starter's control circuit."

**Common misuse:** treating a one-line as sufficiently detailed to build from, or bloating a one-line with control-relay logic that belongs on the elementary diagram instead.

## Ampacity vs. conductor (insulation) rating

**Ampacity** is the maximum current a conductor can carry continuously under stated conditions, as looked up from NEC Table 310.16 for the *applicable* temperature column. **Conductor rating** (e.g., THHN's 90°C rating) is the insulation's own temperature limit — the ceiling, not the usable value once termination limits are applied.

**In use:** "The wire's rated 90°C, but its ampacity on this circuit is capped at the 75°C column because the breaker terminals are only listed that high."

**Common misuse:** citing the insulation's full temperature rating as if it were automatically the usable ampacity, skipping the termination-rating check required by 110.14(C).

## Full-load current (FLC) vs. full-load amps (FLA)

**FLC** is the standardized value from NEC Table 430.250, used for branch-circuit, feeder, and protection sizing regardless of the specific motor installed. **FLA** is the actual full-load current stamped on a specific motor's nameplate, used to cross-check overload relay selection against that particular motor's real performance.

**In use:** "Size the conductor and breaker off the Table 430.250 FLC — once the motor's on site, check the overload setting against its nameplate FLA too."

**Common misuse:** using a motor's nameplate FLA for conductor and OCPD sizing (defeats the standardized code table) or using Table 430.250's FLC for overload-relay fine-tuning (the table value isn't calibrated to a specific motor's actual draw).

## Wire number vs. net name

A **wire number** is a drawing-set label (often purely numeric, e.g., "11") printed at each termination point along a physical conductor, used to trace it across schematic, one-line, and panel wiring sheets. A **net name** is the electrical engineering term for the same electrically continuous connection, often descriptive (e.g., "CR1_COIL") in an EDA tool's underlying data model.

**In use:** "Wire 11 and the net CR1_COIL are the same connection — the wire number is just what's printed on the drawing."

**Common misuse:** treating the wire number itself as if it defined connectivity, when changing the printed number doesn't change what's electrically connected — reusing a number for two different nets is a labeling error, not a wiring error, but it misleads whoever traces the drawing.

## Net-based vs. segment-based wire numbering

A **net-based** scheme assigns one wire number to an entire electrically continuous node, end to end, regardless of how many devices it passes through. A **segment-based** scheme assigns a new number every time the conductor passes through a terminal point (relay contact, terminal block, splice), so one electrical node can carry several different wire numbers along its length.

**In use:** "Confirm which convention this client uses before you start — net-based means wire 11 stays 11 from the pushbutton to the coil; segment-based means it changes at every contact it passes through."

**Common misuse:** mixing the two schemes on the same drawing set, so the same printed number sometimes means "one continuous node" and sometimes means "one segment," with no way to tell which from the drawing alone.

## THHN/THWN (dual-rated conductor)

A conductor insulation type rated 90°C dry (THHN) and 75°C wet (THWN) simultaneously — most branch-circuit wire installed today carries both ratings on the same jacket. Distinct from the *ampacity* actually usable on a given circuit, which is capped by the termination rating regardless of the conductor's dual rating.

**In use:** "It's THHN/THWN dual-rated, so wet-location routing doesn't change the conductor spec — just confirm the termination cap still applies."

**Common misuse:** assuming a dual-rated conductor's higher (90°C) number is automatically usable, ignoring the separate termination-temperature check.

## Continuous load / continuous duty

A load expected to run at maximum current for 3 hours or more, triggering the 125% conductor and OCPD sizing factor under 210.19(A)(1) and 430.22 — distinct from a non-continuous or intermittent load, which is sized at 100% of the actual current.

**In use:** "This conveyor motor runs continuously through the shift — size the branch circuit at 125%, not 100%, of FLC."

**Common misuse:** applying the 125% factor universally, or skipping it for a load that is in fact continuous because the equipment "doesn't seem industrial."

## Overload protection vs. short-circuit/ground-fault protection

**Overload protection** (NEC Article 430, Part III) guards against sustained moderate overcurrent that would overheat the motor over time — sized at 115-125% of FLC. **Short-circuit/ground-fault protection** (Article 430, Part IV) guards against a sudden high-magnitude fault — sized at up to 250% of FLC for an inverse-time breaker. Both protect the same circuit but against different fault modes, from two different table lookups.

**In use:** "The overload relay and the breaker aren't redundant — one's sized for a slow overheat, the other's sized for an instantaneous fault."

**Common misuse:** assuming a correctly sized breaker eliminates the need for separate overload protection, or applying the short-circuit percentage (250%) to the overload calculation.

## Conduit fill vs. current-carrying conductor (CCC) count

**Conduit fill** (Chapter 9 Table 1) is the percentage of raceway cross-sectional area conductors are permitted to occupy, counting every conductor including the EGC and any neutral. **CCC count**, used for the Table 310.15(C)(1) ampacity adjustment factor, excludes the EGC and a balanced neutral — a smaller number derived for a different purpose.

**In use:** "Four conductors for the fill calculation, but only three current-carrying for the adjustment factor — the EGC doesn't count toward derating."

**Common misuse:** using the same conductor count for both calculations, either over-derating ampacity by including the EGC or under-filling the fill check by excluding it.

## Equipment grounding conductor (EGC) vs. grounding electrode conductor (GEC)

The **EGC** (Table 250.122) bonds non-current-carrying metal parts of equipment back to the system, sized from the upstream OCPD's rating. The **grounding electrode conductor** (Table 250.66) connects the service's grounding electrode system to the system ground, sized from the service's ungrounded conductor size — a different conductor, different table, different purpose, despite the similar name.

**In use:** "Don't pull the EGC size from Table 250.66 — that's the grounding electrode table, not the equipment grounding table."

**Common misuse:** conflating the two similarly named conductors and citing the wrong table when sizing either one.

## Schematic capture vs. PCB layout

**Schematic capture** is the electronic drawing of a circuit's logical connectivity (components and nets) in an EDA tool, independent of physical placement. **PCB layout** is the physical placement and routing of that same netlist onto a board's copper layers, governed by trace width, clearance, and stack-up rules the schematic itself doesn't specify.

**In use:** "The schematic's approved — now it's a layout problem: trace widths, layer stack-up, and clearance to the connector."

**Common misuse:** treating layout as a mechanical afterthought to a completed schematic, when trace-width and impedance decisions made during layout can require a schematic-level change (e.g., splitting a net across two vias) that the schematic author needs to approve.

## Ladder diagram / rung numbering

A **ladder diagram** represents control logic as horizontal "rungs" between two vertical power rails, each rung containing a series/parallel arrangement of contacts driving an output (coil, light, solenoid). **Rung numbers**, printed down the left margin, are the cross-reference an elementary diagram and a PLC program (if the logic is later converted) both use to locate the same logic step.

**In use:** "The seal-in contact's on rung 4 — cross-reference it there if the PLC conversion needs to match this rung's logic."

**Common misuse:** treating rung numbers as equivalent to wire numbers; they identify a logic step, not a physical conductor, and the same rung can contain several different wire numbers.

## Symbol legend / cross-reference table

A **symbol legend** defines every graphic symbol used on a drawing set against its standard (IEEE 315/ANSI Y32.2) meaning, including any project-specific deviation. A **cross-reference table** (often auto-generated by EDA/CAE tools) lists every device's sheet and location, letting a reader locate a relay coil's contacts wherever they appear across the set.

**In use:** "Check the cross-reference table for every place CR1's contacts show up before you touch its coil circuit."

**Common misuse:** skipping the cross-reference check and editing a device's coil circuit without locating every sheet where its contacts are used, missing a downstream logic change.
