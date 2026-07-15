# Quality system artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Hold/release decision model (filled — see Worked example in SKILL.md for full narrative)

| Item | Value |
|---|---|
| Test result (initial) | 449.2 MPa (±2.5 MPa) vs. 450 MPa spec |
| Estimated probability truly below spec | 55% |
| Cost of downstream failure if defective | $192,000 (20,000 units × 0.8% field failure rate × $1,200/failure) |
| Expected cost of releasing now | $105,600 (55% × $192,000) |
| Cost of holding for confirmatory testing | $85,000 (2-day delay) |
| **Decision (before conservative-default bias applied)** | **Hold — expected cost of releasing ($105,600) exceeds hold cost ($85,000)** |
| Confirmatory test cost | $12,000 |
| Confirmatory result | 447.8 MPa (±0.8 MPa) — clearly below spec |
| **Final disposition** | **Reject batch; root cause investigation initiated** |

## 2. Cost-of-quality tracker (filled example)

| Category | This quarter | Trend |
|---|---|---|
| Prevention (training, process design, supplier audits) | $85,000 | Flat |
| Appraisal (inspection, testing) | $210,000 | Flat |
| Internal failure (scrap, rework, retesting) | $340,000 | Rising 12% QoQ |
| External failure (warranty, returns, recalls, liability) | $890,000 | Rising 8% QoQ |
| **Total cost of quality** | **$1,525,000** | |

**Reading it:** prevention and appraisal spend combined ($295,000) look modest against the much larger failure costs ($1,230,000) — the rising internal/external failure trend is the signal that prevention is likely underinvested, not the flat prevention line looking "efficient."

## 3. Root cause analysis worksheet (5 Whys, filled example)

| Why # | Question | Answer |
|---|---|---|
| 1 | Why did this batch fail the strength spec? | Raw material composition was out of tolerance. |
| 2 | Why was the raw material out of tolerance? | The supplier's lot [X] had a composition deviation. |
| 3 | Why wasn't this caught before it entered production? | Incoming inspection tests for dimensional spec but not this specific composition parameter. |
| 4 | Why doesn't incoming inspection test this parameter? | It was assumed stable based on the supplier's certification, with no periodic verification. |
| 5 | Why was that assumption never verified? | No process exists for periodically auditing supplier certification claims against independent testing. |

**Rule applied:** the fix targets the systemic gap (root cause 5: no periodic verification process) via a supplier corrective action and an incoming inspection update — not just a one-off rejection of this batch.

## 4. CAPA verification tracker (filled example)

| CAPA # | Issue | Corrective action | Verification period | Status |
|---|---|---|---|---|
| CAPA-2026-014 | Raw material composition deviation | Supplier corrective action + added incoming composition test | 3 production lots | Open — 1 of 3 lots verified clean so far |
| CAPA-2026-009 | Torque spec drift on assembly line 3 | Recalibrated torque tool, added SPC monitoring | 30 days | Closed — no recurrence over verification period, fix confirmed effective |

**Rule applied:** CAPA-014 stays open until all 3 verification lots are confirmed clean — documentation completion alone doesn't close it.
