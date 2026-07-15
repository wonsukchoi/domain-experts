# Quality management working vocabulary

Terms a quality manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Cost of quality (COQ)** — A framework tracking four cost categories: prevention (avoiding defects), appraisal (inspection/testing), internal failure (defects caught before shipping), and external failure (defects reaching the customer) — used to make the true, often invisible cost of quality visible.
In use: "Our prevention spend looks efficient, but external failure costs are 4x higher than internal — that's the number that should be driving investment, not the visible line items alone."
Misuse: tracking only prevention and appraisal spend as "the cost of quality," missing that internal and external failure costs are often the largest and most consequential category, and that low visible spend can mask much larger hidden failure costs.

**Root cause analysis (5 Whys, fishbone/Ishikawa, fault tree)** — Structured techniques for identifying the systemic cause of a non-conformance, as distinct from a fix that addresses only the specific instance without preventing recurrence.
In use: "5 Whys traced this defect past the obvious operator error to an unclear work instruction that's been ambiguous for months — that's the actual root cause."
Misuse: closing a non-conformance with a fix for the specific instance (retraining the operator, reworking the specific batch) without identifying and addressing the underlying systemic cause, guaranteeing the same failure mode recurs.

**CAPA (Corrective and Preventive Action)** — A documented process addressing both the immediate correction of a non-conformance and the preventive action to stop recurrence, closed only after verifying the preventive fix actually worked, not when documentation is complete.
In use: "This CAPA stays open for three more production lots — we need to verify the corrective action actually prevented recurrence, not just that the paperwork is filed."
Misuse: closing a CAPA once the documentation is complete without a verification period confirming the fix actually prevented recurrence, treating it as a compliance exercise rather than a real quality improvement.

**Statistical process control (SPC)** — Using control charts and statistical thresholds to monitor a process for drift or instability, catching a process trending out of control before it produces an actual out-of-spec result, as opposed to relying on 100% end-product inspection.
In use: "The SPC chart flagged this process trending toward the upper control limit three shifts before it would have produced an actual out-of-spec unit."
Misuse: relying solely on end-of-line inspection to catch defects rather than monitoring the process itself for early drift signals that SPC is specifically designed to surface.

**Conservative-default (ambiguity bias)** — The deliberate policy of defaulting toward the more cautious decision (hold, reject) when a quality determination is genuinely ambiguous, given the asymmetry between the cost of a false hold and the cost of a false release.
In use: "The result is genuinely ambiguous given measurement uncertainty — per our conservative-default policy, this holds until confirmatory testing resolves it, not because we assume it's defective, but because the asymmetric cost favors caution under real ambiguity."
Misuse: resolving genuine measurement or determination ambiguity in favor of whichever outcome is more convenient (usually release, under schedule pressure) rather than applying a deliberate, named default bias toward caution.

**Quality independence** — The principle that a quality function's hold/release authority has to be able to override production and schedule pressure to mean anything — tested by whether holds are ever actually enforced against pressure, not just whether independence exists on paper.
In use: "The independence test here is simple: has quality actually held a shipment against schedule pressure in the last year? If not, that's a real signal, not proof everything's been fine."
Misuse: assuming quality independence exists because it's stated in a policy document, without checking whether hold decisions have ever actually been enforced against real production or schedule pressure.

**Measurement uncertainty** — The range within which a measured value's true value likely falls, given the precision limits of the measurement method — critical context for determining whether a result near a spec limit is genuinely ambiguous or clearly in/out of spec.
In use: "449.2 MPa with ±2.5 MPa uncertainty against a 450 MPa spec is genuinely ambiguous — the true value could plausibly be above or below the line."
Misuse: treating a measured value as a precise, certain number without accounting for its stated measurement uncertainty, which can make a genuinely ambiguous result look falsely definitive in either direction.

**Supplier quality audit** — A structured evaluation of a supplier's own quality processes and capability, treating supplier-originated risk as an extension of the receiving organization's own quality system rather than an external, separate concern.
In use: "The root cause traced back to the supplier's raw material lot — that's now a supplier corrective action tracked in our own CAPA system, not just a rejected shipment."
Misuse: treating a supplier-originated defect as solely the supplier's problem to reject and move past, missing that a shipped product with that defect is still the receiving organization's own quality failure to the end customer.

**Incoming inspection** — Quality verification performed on materials or components received from a supplier before they enter production, a first-line defense against supplier-originated defects distinct from and complementary to supplier audits.
In use: "Incoming inspection caught the raw material composition issue before it entered the production line — that's a separate control from the supplier audit process."
Misuse: relying solely on supplier audits (periodic, process-level) without incoming inspection (per-shipment, material-level) to catch a specific batch or lot issue that a periodic audit wouldn't necessarily surface.

**Detection capability validation** — Verifying that an inspection or testing process actually catches real defects when they occur (e.g., via a known-defect spike test or gauge repeatability and reproducibility study), as distinct from assuming a low defect-finding rate reflects genuine quality rather than inadequate detection.
In use: "We ran a known-defect spike test through the inspection line and confirmed it catches 98% of injected defects — that's what lets us trust the low defect-finding rate as real, not just under-detection."
Misuse: treating a consistently low or zero defect-finding rate as automatic evidence of quality success without validating that the detection process is actually capable of catching defects when they're present.
