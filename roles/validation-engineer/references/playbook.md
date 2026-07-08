# Validation Engineer — Playbook

Filled worksheets for the five calculations/assessments this role executes repeatedly. Numbers below are worked examples, not the ones in SKILL.md's worked example — use the structure, replace the inputs.

## 1. PDE/HBEL-based cleaning MACO worksheet

**Inputs required before calculating (reject the request if any is missing):**

| Input | Symbol | Source |
|---|---|---|
| Permitted daily exposure | PDE | Toxicology assessment or ICH M7 TTC default (1.5 µg/day genotoxic-unstudied; 120 µg/day Class 3 default) |
| Minimum batch size, next product | MBS | Batch record, mg |
| Largest daily dose, next product | LDD | Product label, mg/day |
| Shared surface area | SSA | Equipment train drawing, cm² |
| Swab area | SA | SOP-CV swab template, cm² |

**Calculation, worked (Compound X, PDE = 10 µg/day from a compound-specific NOAEL-based assessment, next-product MBS = 250,000,000 mg, LDD = 500 mg/day, SSA = 62,500 cm², SA = 25 cm²):**

```
MACO_total   = (PDE × MBS) / LDD
             = (0.010 mg/day × 250,000,000 mg) / 500 mg/day
             = 2,500,000 / 500
             = 5,000 mg

Swab limit   = MACO_total × (SA / SSA)
             = 5,000 mg × (25 cm² / 62,500 cm²)
             = 5,000 × 0.0004
             = 2.0 mg per 25 cm² swab  →  0.08 mg/cm²
```

**Legacy screens, computed for comparison only — never the governing limit if lower than PDE-based:**

```
10 ppm rule       = 10 mg/kg × batch size (kg)
1/1000-dose rule  = (0.001 × LDD_previous_product × MBS) / LDD_next_product
```

**Governing-limit rule:** take `min(PDE-based MACO, 10 ppm MACO, 1/1000-dose MACO)`. Report all three; adopt the lowest as the protocol acceptance criterion; retain the other two as documented supplementary screens.

**Acceptance-criteria memo template:**

```
Scope: Cleaning validation, [equipment train], [previous product] → [next product]
Toxicological input: PDE = [x] µg/day per [compound-specific NOAEL / ICH M7 TTC default], source: [toxicology report ref]
MACO calculation: MACO = (PDE × MBS) / LDD = [value] mg total carryover, SSA = [value] cm²
Swab acceptance limit: [value] µg per [x] cm² swab ([value] µg/cm²)
Legacy comparison (not governing): 10 ppm → [value] mg; 1/1000-dose → [value] mg
Disposition: Protocol [ref] approved at ≤[value] µg/swab; execution on next scheduled changeover.
```

## 2. GAMP 5 category assessment worksheet

Score the system against each question; the highest-numbered "yes" sets the category.

| Question | If yes → category |
|---|---|
| Is it operating-system/infrastructure with no GxP business logic (network switch, OS, DB engine)? | Cat 1 |
| Is it commercial off-the-shelf, unmodified, no user-configurable business rules? | Cat 3 |
| Is it configured — user-defined workflows, calculations, business rules, or reports built on a commercial platform? | Cat 4 |
| Is any part bespoke code written for this deployment (custom scripts, macros with GxP calculations, custom interfaces)? | Cat 5 |

**Evidence depth by category:**

| Category | IQ | OQ | PQ | Extra |
|---|---|---|---|---|
| 1 | Yes — install checks only | — | — | — |
| 3 | Yes | Intended-use confirmation + supplier test evidence on file | Not usually required | Supplier audit if not previously qualified |
| 4 | Yes | Risk-based OQ on configured logic only, traced to requirements | Yes, on the configured workflow | Configuration spec + traceability matrix |
| 5 | Yes | Full test-case OQ, code review | Yes | SDLC evidence: design spec, unit test records, FAT/SAT |

**Worked example.** A LIMS platform (COTS core, Cat 3) with a site-configured custom stability-calculation module (Cat 4 logic layered on it) and one bespoke interface script pulling data into a client's ERP (Cat 5 component) → assess **each component separately**, don't round the whole system up or down to one category. Evidence plan: Cat 3 depth on the LIMS core (supplier evidence + intended-use test), Cat 4 depth on the stability module (configuration spec, traceability matrix, risk-based OQ on the calculation logic), Cat 5 depth on the interface script (code review, unit test records, FAT/SAT).

## 3. PPQ batch-count justification worksheet

```
1. Pull process capability from development/engineering runs: Cpk = [value]
2. Classify process/product complexity: novel platform | established platform, new product | established platform, established product
3. Classify prior knowledge: none | partial (similar product, same platform) | extensive (same product family, ≥3 prior platform validations)
4. Apply the matrix:
```

| Cpk | Complexity | Prior knowledge | Minimum PPQ batches |
|---|---|---|---|
| < 1.33 | novel | none | 5+ |
| < 1.33 | established platform | partial | 4–5 |
| ≥ 1.33 | established platform | partial | 3–4 |
| ≥ 1.67 | established platform | extensive | 3 |

**Never write "3" without the row.** The justification memo cites the Cpk figure, complexity classification, and prior-knowledge classification that produced the count — an auditor asking "why three" gets the row, not "per Annex 15."

## 4. ASTM E2500 verification-tier assignment

```
Tier A (full verification): novel equipment, no platform history, direct product-contact critical parameter
Tier B (targeted verification): established equipment design, new critical parameter or new product
Tier C (rely on vendor/platform data + confirmatory spot-check): established equipment, established parameter, existing FAT/SAT on file from vendor
```

Assign per critical aspect (not per equipment unit) — a single skid can carry Tier A on one parameter (a novel spray-coating rate) and Tier C on another (a standard temperature control loop already qualified on three prior identical skids).

## 5. Analytical method LOQ confirmation protocol (ICH Q2)

```
1. Calculate LOQ statistically: LOQ = 10 × (SD of response / slope of calibration curve)
2. Prepare confirmatory samples at 50%, 100%, 150% of the calculated LOQ concentration, n = 6 replicates each
3. Acceptance thresholds at the 100% LOQ level:
   - %RSD (precision) ≤ 20% for trace/impurity methods (tighter, e.g. ≤10%, if the method's own validation protocol pre-specifies it)
   - Recovery (accuracy) 80–120% of nominal
4. If either threshold fails: LOQ is not confirmed — raise the reported LOQ to the next concentration tested and repeat, or investigate assay robustness (mobile-phase stability, detector noise floor) before re-testing
5. Only a concentration meeting both thresholds is the reportable LOQ; the statistically calculated value alone is not validation-complete
```
