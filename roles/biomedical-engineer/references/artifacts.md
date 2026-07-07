# Biomedical Engineer — Artifacts

## Design FMEA worksheet (filled example — wearable insulin patch pump)

| Failure mode | Effect | Severity (1-10) | Cause | Occurrence (1-10) | Current controls | Detection (1-10) | RPN | Mitigation | Post-mitigation RPN |
|---|---|---|---|---|---|---|---|---|---|
| Delivery-line occlusion at fold radius | Missed insulin delivery, hyperglycemia | 8 | Line kinks at patch fold under wear motion | 4 (2.1% bench rate) | Pressure-sensor occlusion algorithm | 3 (22-min median lag) | 96 | Strain-relief collar (DWG-4471 Rev C) + algorithm retune to 15-min floor | 32 |
| Reservoir seal leak | Under-delivery, skin irritation from insulin contact | 6 | Seal compression set over 72-hr wear | 3 (0.8% at 72hr, accelerated aging) | Visual leak indicator strip | 4 (patient-dependent noticing) | 72 | Dual-durometer seal material, re-verify 90-day aging | 30 |
| Battery depolarization below cutoff during cold-chain storage | Device fails to power on at first use | 5 | Storage below 0°C for >48hr untested | 2 (rare per distribution QA data) | Cold-chain indicator on shipping carton | 2 (indicator is visible pre-use) | 20 | No action — below threshold, monitor via complaint trend | 20 |
| Bluetooth pairing failure with companion app | Delayed dose confirmation, patient re-attempts pairing | 3 | Firmware race condition on reconnect | 6 (11% of field pairing attempts in beta) | User retry instructions in labeling | 5 (patient self-reports failure) | 90 | Firmware patch (v2.3) serializing reconnect handshake | 21 |

**Threshold rule applied:** RPN > 80 OR severity ≥ 8 → mandatory documented mitigation and design-review sign-off before freeze. Rows 1 and 4 tripped the rule; rows 2 and 3 were below threshold but row 2 was mitigated anyway per program policy of closing any RPN > 50 with a low-cost fix available.

## Traceability matrix (excerpt)

| Design input ID | Input (testable) | Design output | Verification method | Result | Validation method | Result |
|---|---|---|---|---|---|---|
| DI-014 | Delivery line shall withstand 500 wear-motion cycles at fold point with ≤0.5% occlusion incidence | Strain-relief collar DWG-4471 Rev C | Bench cycling protocol BP-22 | Pass — 0.3% (2/500) | Simulated-use study SU-09 (30 subjects, 72hr wear) | Pass — 0 occlusion events |
| DI-021 | Occlusion detection algorithm shall alarm within 15 min of onset at 95% confidence | Pressure-sensor firmware v2.3 | Bench test BT-31, n=200 simulated occlusions | Pass — 14.2 min median, 95th pctile 16.8 min | — (verification-only requirement) | — |
| DI-033 | Device shall be operable by a representative user with no prior training within 3 attempts | UI/label design v4 | — (validation-only requirement) | — | Summative usability study HF-07, n=18 (3 user groups × 6) | Pass — 17/18 succeeded within 2 attempts |
| DI-041 | Reservoir seal shall show ≤2% volume loss over 72hr wear at 35°C | Dual-durometer seal material | Bench aging protocol BP-30 | Pass — 1.1% loss at 72hr | — | — |

**Gap check before freeze:** any Design input row with both Verification and Validation columns empty is an unresolved requirement — none present in this excerpt; DI-021 and DI-041 are verification-only by design (non-clinical parameters), DI-033 is validation-only by design (usability can't be bench-tested).

## Biocompatibility test-battery selection (ISO 10993, by contact category)

| Contact category | Contact duration | Required endpoints |
|---|---|---|
| Surface device, skin contact | Limited (≤24hr) | Cytotoxicity, sensitization, irritation |
| Surface device, skin contact | Prolonged (24hr-30 days) | + Cytotoxicity, sensitization, irritation (same, longer exposure justification) |
| External communicating, tissue/bone/dentin | Limited (≤24hr) | + Cytotoxicity, sensitization, irritation, material-mediated pyrogenicity |
| Implant, tissue/bone | Permanent (>30 days) | + Subacute/subchronic toxicity, genotoxicity, implantation, chronic toxicity, carcinogenicity (case-by-case) |

**Patch pump applies as:** Surface device, skin contact, prolonged (7-day wear cycles, worn back-to-back) — full battery: cytotoxicity, sensitization, irritation, re-scoped whenever adhesive or housing material changes.

## Design History File (DHF) index skeleton

```
DHF-[product]-[rev]
1. Design Plan (scope, phases, gate criteria)
2. Design Inputs (user needs, design input specification, change log with rationale)
3. Design Outputs (drawings, specs, software architecture, labeling)
4. Design Reviews (dated minutes, attendees, decisions, action items closed)
5. Verification (protocols, raw data, reports, traceability to inputs)
6. Validation (protocols incl. human factors, raw data, reports, traceability to user needs)
7. Risk Management File (DFMEA, use-related risk analysis, RPN log, mitigation closure)
8. Design Transfer (manufacturing process validation, Cpk data, first-article inspection)
9. Design Changes Post-Freeze (change request, impact assessment, re-verification/validation scope, approval)
```
