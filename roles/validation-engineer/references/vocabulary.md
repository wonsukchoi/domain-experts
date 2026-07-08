# Vocabulary — Validation Engineer

Terms generalists routinely use as loose synonyms for each other. Each entry gives the precise meaning, a sentence showing correct use, and the specific confusion to avoid.

**Verification (vs. validation)**
Definition: Confirming an output conforms to a specified design input — "did we build it right" (21 CFR 820.30(f)). A verification test compares the product against its own spec, not against real user need.
In use: "Verification confirmed the assembly meets the drawing tolerance; validation against actual clinician handling is still open."
Misuse note: Generalists use "verified" and "validated" interchangeably. Passing every verification test proves nothing about whether the spec itself reflects real use — a design can be fully verified and never validated.

**Validation (vs. verification)**
Definition: Confirming the finished item performs against actual user needs under actual or simulated use conditions (21 CFR 820.30(g)). It is a claim about real-world performance, not spec conformance.
In use: "The device passed verification months ago, but validation under simulated bedside use just surfaced a usability failure the spec never captured."
Misuse note: Teams often report "validated" the moment a protocol is signed, treating the signature as the validated state itself rather than as documentation of a lifecycle stage that has to keep being true (see Stage 3 CPV).

**PPQ (Process Performance Qualification)**
Definition: Stage 2 of the FDA process-validation lifecycle — demonstrating, with commercial-scale batches under normal operating conditions, that a process reliably produces conforming product. It is not a synonym for "the validation batches" generically.
In use: "PPQ batch 3 of 5 trended outside the pre-set blend-uniformity RSD limit."
Misuse note: People say "we ran PPQ" to mean any three batches run back-to-back. PPQ batch count is a risk-based justification (process variability, complexity, prior platform knowledge) — citing a fixed number of PPQ runs with no rationale behind it is citing a retired convention, not a requirement.

**Stage 3 / CPV (Continued Process Verification)**
Definition: The ongoing statistical trending of a commercial process after PPQ, per FDA's 2011 guidance — ongoing, not a one-time closeout activity.
In use: "The validation package has no Stage 3 CPV plan behind it, so the validated state it describes stopped being true the day the raw-material lot changed."
Misuse note: Generalists treat "Stage 3" as a checkbox satisfied by writing a monitoring SOP. It means the trending is actually running and current — an unexecuted CPV plan is functionally the same gap as having none.

**MACO (Maximum Allowable Carryover)**
Definition: The calculated total mass of a prior product's residue permissible on shared equipment before the next product runs, derived from a governing safety limit (ideally PDE/HBEL) divided across a batch and surface-area basis. It is a total-mass figure, not a concentration or a swab-result number by itself.
In use: "MACO = (PDE × minimum batch size) / largest daily dose of the next product = 150 mg total allowable carryover."
Misuse note: People use "MACO" and "swab limit" interchangeably. MACO is the total carryover across the whole shared surface; the swab (or per-area) limit is MACO apportioned by the sampled area's fraction of the total surface — conflating the two under- or over-states the acceptance criterion by orders of magnitude.

**PDE / HBEL (Permitted Daily Exposure / Health-Based Exposure Limit)**
Definition: A toxicologically derived daily exposure limit for a specific compound, set from NOAEL or equivalent safety data (or an applicable default such as ICH M7's TTC when compound-specific data is unavailable). It is the current governing basis for a cleaning acceptance criterion under EU GMP Annex 15/EMA guidance.
In use: "Toxicology assigned PDE = 1.5 µg/day per the ICH M7 default threshold, since Product A's degradant carries an unresolved genotoxic-impurity structural alert."
Misuse note: Generalists treat PDE/HBEL as an alternative option to the legacy 10 ppm or 1/1000-dose rule, pick whichever is more convenient, and don't check which is lower. The lower, more protective limit governs regardless of which method is "standard" for the product class — for a low-dose, high-potency, or sensitizing compound the PDE-based number is routinely the tighter one.

**TTC (Threshold of Toxicological Concern)**
Definition: A conservative, compound-agnostic default exposure limit (ICH M7 sets 1.5 µg/day for an unstudied genotoxic impurity) used only when no compound-specific NOAEL-derived PDE exists.
In use: "No compound-specific PDE was on file, so toxicology defaulted to the ICH M7 TTC of 1.5 µg/day."
Misuse note: TTC is not a generic "safe default" that can be invoked to skip toxicological assessment — it's specifically the fallback for genotoxic/unstudied-impurity scenarios, and using it in place of an available compound-specific PDE discards real safety data for a more conservative but less-informed number.

**GAMP 5 category**
Definition: A four-tier classification (Category 1 infrastructure, 3 non-configurable COTS, 4 configurable, 5 bespoke code) that sets how much CSV/CSA evidence a computerized system needs — not whether it needs any.
In use: "The LIMS configuration is Category 4, so it needs configuration documentation and risk-based OQ, not the full-SDLC evidence a Category 5 bespoke build requires."
Misuse note: Generalists apply one script depth — usually maximal — to every system regardless of category, over-testing a Category 3 COTS system while under-testing the configured business logic on a Category 4 system that actually carries the risk.

**CSV vs. CSA (Computer System Validation vs. Computer Software Assurance)**
Definition: CSV is fully scripted, document-heavy test execution; CSA (per FDA's 2022 draft guidance) is a four-step risk-based process — define intended use, assess risk of failure, plan assurance activities, document confidence — that reallocates testing effort by risk rather than scripting everything uniformly.
In use: "We scoped this as CSA: unscripted testing with confidence-based documentation for the low-risk workflow, full scripted CSV reserved for the Category 5 bespoke module."
Misuse note: People treat CSA as "less validation" or a compliance shortcut. It doesn't remove the underlying requirement to validate — it changes how the evidence is generated and documented, and still expects fully scripted CSV for higher-risk, bespoke code.

**IQ/OQ/PQ (Installation, Operational, Performance Qualification)**
Definition: The three qualification stages confirming, in order, that equipment is installed per spec (IQ), operates across its intended ranges (OQ), and performs consistently under real production conditions (PQ). PQ for a process specifically, at commercial scale, is PPQ.
In use: "IQ confirmed utility connections match the P&ID; OQ is still open on the extended temperature range."
Misuse note: Generalists use "IQ/OQ/PQ" as one bundled deliverable executed in a single pass. Each stage answers a different question and depends on the prior one passing — running OQ before IQ discrepancies are resolved just documents a qualification against unconfirmed installation conditions.

**ASTM E2500 (risk-based verification)**
Definition: A commissioning-and-qualification approach that verifies critical aspects through the design/specification/verification/acceptance lifecycle proportional to risk, in place of a uniform traditional C&Q test program applied identically to every system.
In use: "Equipment commissioning followed ASTM E2500 risk-based verification rather than a traditional full IQ/OQ test script, since the utility system carries no direct product-quality impact."
Misuse note: Generalists assume E2500 means "less testing" across the board. It reallocates verification effort toward the elements with actual quality impact — a specific existing regulatory commitment to the classic IQ/OQ format can still require that format regardless of E2500's risk logic.

**LOQ (Limit of Quantitation) vs. LOD (Limit of Detection)**
Definition: LOD is the lowest amount reliably distinguishable from noise; LOQ is the lowest amount quantifiable with acceptable precision and accuracy (ICH Q2). A calculated LOQ (from a calibration curve, say) is not the same as a validated one.
In use: "The statistically calculated LOQ was confirmed empirically with precision and accuracy runs at that concentration, per ICH Q2."
Misuse note: Analysts report a mathematically derived LOQ as validation-complete. Without confirmatory precision/accuracy data run at that actual concentration, the calculated number is an estimate, not a validated limit.

**Deviation vs. CAPA (Corrective and Preventive Action)**
Definition: A deviation is a documented departure from an approved protocol or procedure during execution, investigated for root cause before disposition. CAPA is the broader corrective/preventive action system that a deviation's root cause may feed into — not every deviation requires a full CAPA.
In use: "The OOS result was documented as a deviation, root-caused to a probe calibration drift, and dispositioned with a re-test; no CAPA was opened since the root cause was isolated to one instrument."
Misuse note: Generalists use "deviation" and "CAPA" as synonyms, or worse, disposition a deviation without root-causing it first — redefining or waiving an acceptance criterion after the fact to make failing data pass is not a disposition, it's data manipulation.

**Traceability matrix**
Definition: The document mapping user requirements through functional/design specifications to the test cases that verify them, demonstrating every requirement was tested and every test traces back to a requirement — bidirectional, not a one-way test list.
In use: "The traceability matrix shows URS-14 mapped to FS-22 mapped to OQ-07; there's no orphaned test case and no untested requirement."
Misuse note: Teams build a list of tests performed and call it a traceability matrix. Without the reverse mapping — confirming every requirement has a corresponding test — gaps in coverage are invisible until an inspector or a field failure finds them.
