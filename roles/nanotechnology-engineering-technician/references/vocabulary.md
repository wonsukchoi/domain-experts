# Vocabulary — Nanotechnology Engineering Technician

Terms generalists routinely use as loose synonyms for each other, or treat as looser than they are. Each entry gives the precise meaning, a sentence showing correct use, and the specific confusion to avoid.

**REL (Recommended Exposure Limit) vs. PEL (Permissible Exposure Limit)**
Definition: A REL is a NIOSH-recommended airborne exposure ceiling with no independent enforcement mechanism; a PEL is an OSHA-enforceable regulatory limit. For most engineered nanomaterials — including carbon nanotubes/nanofibers — no PEL currently exists, so the REL is the best available number, not a regulatory floor.
In use: "No PEL exists for CNTs, so the sampling result is being reported against the NIOSH REL of 1 µg/m³ as a working ceiling, not an enforceable limit."
Misuse note: Generalists say "the exposure limit" as if there's always a single enforceable number, or cite a REL as if OSHA can cite a violation against it. Reporting a REL result without flagging that it isn't enforceable lets a safety reviewer wrongly assume regulatory force.

**Instrument-limited (as applied to a REL)**
Definition: Describes a limit set at the floor of what current air-sampling methods can reliably measure, rather than at a toxicologically derived safe threshold. The CNT/CNF REL of 1 µg/m³ respirable elemental carbon is instrument-limited.
In use: "A clean sample at the instrument-limited REL means sampling didn't detect a problem — it doesn't mean exposure was biologically safe."
Misuse note: Treating a passing instrument-limited REL result as proof of safety is the single most common misread in this role — it conflates "below what we can currently detect" with "below what causes harm."

**Respirable elemental carbon (vs. total or inhalable carbon)**
Definition: The size-selected, sub-~4 µm fraction of airborne elemental (not organic) carbon that penetrates to the gas-exchange region of the lung — the specific fraction the NIOSH CNT/CNF method targets, distinct from total suspended particulate or the inhalable fraction.
In use: "The sample reported 0.8 µg/m³ respirable elemental carbon, below the 1 µg/m³ REL for that fraction specifically."
Misuse note: Generalists read "carbon reading" as a single undifferentiated number. A total-carbon or inhalable-fraction result is not directly comparable to the REL, which is defined against the respirable elemental-carbon fraction only.

**8-hr TWA (Time-Weighted Average)**
Definition: An exposure concentration averaged over a full 8-hour shift, not an instantaneous or peak reading. A REL or PEL expressed as a TWA can be exceeded briefly without a violation, as long as the shift-long average stays under the limit.
In use: "The peak reading during the 20-minute transfer operation exceeded 1 µg/m³, but the 8-hr TWA came in at 0.6 µg/m³."
Misuse note: Treating a single elevated grab-sample reading as itself "over the limit" ignores that most RELs/PELs are TWA-defined; conversely, a low TWA can mask a short high-intensity excursion worth investigating on its own.

**Dissipative (vs. conductive or "anti-static")**
Definition: A material property describing controlled, gradual charge bleed-off (surface resistivity roughly 10^5–10^11 ohms/sq) — distinct from conductive (near-zero resistance, rapid discharge) and from generic "anti-static" marketing claims that don't specify a resistivity class at all. Cleanroom gowning fabric must be woven with dissipative thread to function as intended.
In use: "The bunny suits failed incoming QC because the thread wasn't dissipative-grade — resistivity measured outside the qualified band."
Misuse note: Assuming any garment labeled "anti-static" or "ESD-safe" is dissipative-thread woven is a documented failure mode: non-dissipative fabric can itself generate the static charge the gowning protocol exists to suppress.

**ESD sensitivity threshold (node-dependent, not fixed)**
Definition: The minimum electrostatic discharge energy capable of damaging a device or photomask, which decreases as feature size shrinks — it is not a single facility-wide constant that, once qualified, stays valid across process generations.
In use: "The gowning and grounding protocol qualified at the 90 nm node was re-verified before use on the 45 nm line, since the damage threshold there is lower."
Misuse note: Carrying over an ESD protocol to a smaller-geometry job on the assumption that "it passed before" ignores that the threshold itself moved — a protocol adequate at one node isn't automatically adequate at the next.

**SC1 / SC2 / Piranha (RCA clean components, not interchangeable)**
Definition: SC1 (APM: NH4OH:H2O2:H2O, nominally 1:4:20 at 80°C) removes organics and particles; SC2 (HPM: HCl:H2O2:H2O) removes metallic ions; piranha (SPM: H2SO4:H2O2) strips heavy organic residue. Each targets a different contaminant class and runs a different chemistry — they are sequential steps in an RCA clean, not substitutable options.
In use: "The wafer went through SC1 for particle/organic removal, then SC2 for the ionic clean — piranha wasn't called for since there was no heavy resist residue to strip."
Misuse note: Referring to "the RCA clean" as one undifferentiated bath, or swapping which solution runs first, misses that each step is chemically targeted — skipping or reordering them changes what contamination actually gets removed.

**Growth-per-cycle (GPC) — cycle-to-cycle rate, not a single-point thickness**
Definition: In atomic layer deposition, the thickness deposited per reaction cycle, calculated from metrology at a checkpoint and tracked over successive checkpoints as the process-health signal — not the same thing as the cumulative thickness reading itself.
In use: "GPC at cycle 100 was 0.550 Å/cycle, down from the qualified 0.650 Å/cycle — a 15.4% drop worth flagging before the run continues."
Misuse note: Generalists read a single thickness checkpoint as pass/fail against the final spec and stop there. The rate derived from that checkpoint, and whether it's still moving, is the actual diagnostic signal — a thickness that's technically still "in spec" can sit on top of a GPC that's already trending toward failure.

**Self-limiting (ALD deposition mechanism)**
Definition: Describes a surface reaction that saturates and stops on its own once available reactive sites are consumed, which is what gives ALD its sub-angstrom per-cycle control — it does not mean the deposition rate is immune to drift.
In use: "ALD's self-limiting chemistry is why GPC is normally stable cycle to cycle — which is exactly why a drift from the qualified GPC signals a delivery-system problem, not normal variation."
Misuse note: Some generalists take "self-limiting" to mean "self-correcting" or "can't go wrong," and so under-react to a drifting GPC on the assumption the chemistry will settle itself back to the qualified rate. Self-limiting bounds each individual cycle's deposition; it says nothing about whether the precursor delivery feeding those cycles is still healthy.

**Witness wafer**
Definition: A dedicated monitor wafer run alongside (not instead of) the product wafer(s) in a process batch, sacrificed for destructive or time-consuming metrology so the product wafers don't have to be.
In use: "Ellipsometry ran on the witness wafer at cycle 100 rather than the product wafers, to avoid pulling them mid-run."
Misuse note: Treating the witness wafer's reading as automatically representative of the product wafers without confirming they saw equivalent process exposure (loading position, gas flow uniformity) can mask a real product-wafer deviation the witness wafer didn't experience.

**ISO Class (ISO 14644-1) — lower number is cleaner**
Definition: A numeric classification of a cleanroom's particle-count ceiling per cubic meter at specified particle sizes (e.g., ISO 5 ≤ 3,520 particles/m³ at ≥0.5 µm); the scale runs inversely — a lower class number means a stricter, cleaner environment, not a looser one.
In use: "The lithography bay is qualified ISO 5; the gowning room outside it is only ISO 7, which is the expected, looser standard for that space."
Misuse note: Assuming a higher ISO class number means "cleaner" (by analogy to higher-is-better ratings elsewhere) inverts the scale — ISO 7 is dirtier than ISO 5, not cleaner.

**Cleanroom classification — a monitored state, not a one-time certificate**
Definition: An ISO 14644-1 class rating that holds only as long as particle counts continue to verify it; it is not a permanent certification earned once and assumed to persist.
In use: "Particle counts were re-verified before the run rather than trusting the classification plaque posted at the last audit."
Misuse note: Treating a posted classification as settled fact, rather than re-checking current particle counts before a sensitive run, misses that filter loading, traffic, and door seals can degrade a bay's actual class between formal audits.

**Tip radius (AFM probe wear)**
Definition: The physical radius of curvature at an AFM probe's apex, which starts near a named spec (e.g., ~2 nm for a Bruker ScanAsyst probe, spec max 8 nm) and widens with use, directly degrading achievable image resolution independent of the sample.
In use: "Resolution loss tracked with probe hours, not sample changes, so the ScanAsyst tip was swapped rather than re-tuning the scan parameters."
Misuse note: Attributing gradually degrading AFM image resolution to the sample or process settings, rather than checking tip-radius wear against the manufacturer's spec, misses the most common and cheapest-to-fix cause.

**Qualified rate (vs. nominal spec value)**
Definition: The GPC, etch rate, or similar process rate actually verified for a specific tool/recipe/precursor lot combination during qualification runs — which can differ from the generic nominal value published for that chemistry, and is the correct baseline against which mid-run drift is measured.
In use: "The drift was measured against this tool's qualified GPC of 0.650 Å/cycle, not the generic literature value for SiN ALD."
Misuse note: Comparing an in-run reading against a textbook or vendor nominal number instead of the tool's own qualified rate can either mask a real drift (if the qualified rate was already lower) or manufacture a false alarm (if it was already higher).
