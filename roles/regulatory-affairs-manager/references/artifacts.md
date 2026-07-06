# Regulatory submission-strategy artifacts

Filled templates for the four recurring regulatory-strategy documents: predicate comparison, claims-to-evidence gap matrix, pathway cost/timeline model, and change-control decision tree.

## 1. Predicate comparison table

| Factor | Candidate predicate A (2019 clearance) | Candidate predicate B (2023 clearance) |
|---|---|---|
| Intended use match | Partial — nodule detection only | None found — no cleared device with combined intended use |
| Technological characteristics | Similar imaging modality, older CNN architecture | Newer architecture, different training population |
| Adverse event / recall history | None on record | 1 Class II recall (2024, false-negative rate above labeled spec) |
| FDA scrutiny level | Low — no open issues | Elevated — recall under active FDA monitoring |
| Recommendation | Use as reference for nodule-detection performance benchmark only | Avoid — recall history invites additional scrutiny transferred onto new submission |

Decision rule: when no predicate matches intended use, this table is evidence *for* De Novo, not a forcing function to stretch a partial-match predicate into a 510(k) argument.

## 2. Claims-to-evidence gap matrix

| Proposed label claim | Supporting evidence | Gap | Action |
|---|---|---|---|
| "Detects pulmonary nodules ≥6mm with 92% sensitivity" | Clinical validation study, n=1,240, reader study arm | None | Ready |
| "Detects pneumothorax" | Retrospective dataset only, n=340, no prospective reader study | Sensitivity/specificity not established prospectively | Add prospective arm before submission or narrow claim to "retrospectively validated" |
| "Reduces radiologist review time by 30%" | No workflow-time study conducted | No supporting data at all | Remove claim from labeling; reserve for post-market study |
| "For use across all chest X-ray equipment vendors" | Validation performed on 2 of 5 major vendor systems | Untested on 3 vendor systems | Narrow claim to validated vendors, or add validation arms |

Rule: any row with a gap gets resolved (add data or narrow the claim) before the submission is assembled — never submitted as-is with the gap noted internally only.

## 3. Pathway cost/timeline model

| Pathway | Upfront cost | Rejection/refile probability | Refile cost if triggered | Refile delay if triggered | Expected cost | Expected timeline |
|---|---|---|---|---|---|---|
| 510(k), mismatched predicate | $185,000 | 40% | $150,000 | 180 days | $185,000 + 0.40×$150,000 = $245,000 | 177 + 0.40×180 = 249 days |
| De Novo (direct) | $310,000 | ~0% (no predicate dependency) | n/a | n/a | $310,000 | 150 + 45 (1 AI cycle) = 195 days |
| PMA (reference, high-risk class only) | $1.2M+ | n/a | n/a | n/a | $1.2M+ | 180-day FDA review target, commonly 12+ months with panel/AI cycles |

Fill the rejection-probability row from FDA public decision-summary precedent for the specific device category, not a generic estimate — the number is the load-bearing part of this table.

## 4. Change-control decision tree (post-approval design change)

```
Does the change affect intended use or indications for use?
├── Yes → New submission required (510(k)/PMA supplement/De Novo not applicable post-grant)
└── No → Does it affect sterilization, biocompatibility, or a safety-critical software function?
    ├── Yes → New submission or Special 510(k)/PMA supplement, per FDA's 2017 change-guidance flowchart
    └── No → Does it affect performance specifications claimed in the current label?
        ├── Yes → Special 510(k) or PMA supplement (abbreviated review)
        └── No → Letter to file — document rationale, verification/validation evidence, and risk assessment in the Design History File
```

Every "No" branch answer needs a dated, signed rationale in the Design History File — an undocumented "we decided it was minor" is treated by FDA as no assessment having occurred at all.

## 5. Post-market reportability decision memo (template)

```
Event: <description of adverse event/complaint>
Date of awareness: <date> — this starts the reporting clock, not date of root-cause confirmation
Device involved: <model/version>
Did device cause or contribute to death or serious injury? <yes/no/undetermined>
  If undetermined: FDA MDR still requires filing within the standard window if "may have caused or contributed" — undetermined does not exempt from filing
Applicable reporting requirement: <FDA MDR 30-day / 5-day / EU MDR serious incident 15-day (or 2-day for serious public health threat)>
Filing deadline: <date, calculated from awareness date>
Decision: <file / do not file>, rationale: <specific reasoning, not "team judgment">
```
