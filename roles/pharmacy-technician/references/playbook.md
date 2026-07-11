# Playbook

Filled operational references, not descriptions of them. Defaults, not laws — deviating consciously and documenting why is normal practice.

## 1. NCPDP reject-code triage table

Read the code before touching anything else. Common codes and the actual next action (not "call insurance"):

| Code | Meaning | Usual cause | Next action |
|---|---|---|---|
| 70 | Product/service not covered | Drug isn't on the plan's formulary at all | Check formulary alternative list; route to pharmacist for therapeutic-interchange discussion, not a resubmit |
| 75 | Prior authorization required | Plan requires clinical justification before paying | Route to PA queue; fax/portal the PA form to prescriber — resubmitting unchanged never clears this |
| 76 | Plan limitations exceeded | Quantity or duration cap hit (e.g., 30-tab/30-day max on a drug prescribed at 60) | Recompute quantity vs. plan's stated limit; split fill to the covered quantity or route for a quantity-limit exception |
| 79 | Refill too soon | Days'-supply math says patient shouldn't need it yet — recompute *at the current sig*, not just the last one on file | If a dose changed since the last fill, redo the days'-supply calc at the new rate before assuming the reject is wrong or right |
| 88 | DUR reject error | Drug utilization review flagged an interaction, duplicate therapy, or high dose | Pull the specific DUR alert text; this is a pharmacist clinical call, not a technician override |
| MR / 65 | Product not on file / NDC not covered | Billing NDC doesn't match a covered package size | Check 10-digit product NDC vs. 11-digit billing NDC conversion; verify correct package size was selected, not just correct drug |

## 2. Days'-supply formulas by sig type

The formula changes with the sig — using the wrong one is the single most common cause of a false reject-79 or reject-76.

- **Fixed frequency (BID/TID/QID):** quantity ÷ (doses/day). Example: #90 tabs, TID → 90 ÷ 3 = **30 days**.
- **PRN with a stated maximum (e.g., "q4h PRN pain, max 6/day"):** use the *maximum* frequency for the conservative days'-supply, not an assumed average — plans reject on the max-frequency assumption, so filling to a lower assumed average creates the false-early-refill pattern. #60 tabs at max 6/day → 60 ÷ 6 = **10 days**.
- **Insulin (units):** total units in the pen/vial ÷ units per day. Example: one 3mL pen = 300 units; sig 24 units/day → 300 ÷ 24 = **12.5 days**, round down to 12 for supply purposes.
- **Inhalers (actuations):** actuations per canister ÷ actuations/day. Example: 200-actuation canister, sig 2 puffs BID (4/day) → 200 ÷ 4 = **50 days**.
- **Titrated/changed dose since last fill:** always recompute against the *new* sig's daily rate, and separately flag what the next fill's days'-supply should be going forward — the old rate and the new rate almost never agree, and both numbers matter to the next reject check.

## 3. USP <795> beyond-use-date (BUD) defaults for non-sterile compounds

Use when no manufacturer or published stability study covers the specific preparation. These are conservative ceilings, not targets — a documented stability reference can extend them; nothing shortens the process of finding one.

| Preparation type | Default BUD (no stability data available) |
|---|---|
| Water-containing oral formulations (suspensions, solutions) | 14 days, refrigerated |
| Water-containing topical/dermal/mucosal formulations | 30 days |
| Non-aqueous formulations (oil-based suspensions, ointments) | 90 days |
| Solid oral formulations (capsules from bulk powder) | 180 days, or 25% of remaining manufacturer expiration/time-to-expiration, whichever is shorter |

Sterile (<797>) and hazardous-drug (<800>) preparations follow separate, stricter tables tied to risk level (immediate-use, low-, medium-, high-risk) and require engineering controls (ISO-classified hoods, closed-system transfer devices) that a non-sterile compound doesn't — never apply the <795> table to a sterile preparation.

## 4. High-alert / LASA verification sequence

For any drug on ISMP's High-Alert Medications list (insulin, opioids, anticoagulants, chemotherapy/antineoplastics, concentrated electrolytes, neuromuscular blockers) or its Confused Drug Names list:

1. Read the full name, strength, and form off the label — not the bin position or muscle memory.
2. Check tall-man lettering against the stock label if the drug has a known confusable pair (hydrOXYzine/hydrOMORphone, DOPamine/DOBUTamine, clonidine/Klonopin, hydralazine/hydroxyzine).
3. Barcode-scan at the point of fill; a scan mismatch is a hard stop, not a "check again by eye" prompt.
4. Perform the independent double-check — a second person, physically re-verifying drug, strength, and patient, not the same person re-reading their own work.
5. Stage for pharmacist final check with the specific verification already documented, so the pharmacist's check is confirmatory, not the first check.

## 5. DAW (Dispense As Written) codes

| Code | Meaning |
|---|---|
| 0 | No product selection indicated (default, no substitution instruction) |
| 1 | Prescriber requires brand — no substitution |
| 2 | Patient requested brand |
| 3 | Pharmacist selected brand (e.g., generic not in stock) |
| 5 | Brand dispensed, priced as generic |
| 7 | Substitution not allowed — brand mandated by law |
| 8 | Generic not available in marketplace |
| 9 | Plan requests brand |

Miskeying DAW (especially 0 vs. 1) is a common source of an unexpected copay dispute at the register — check it against the actual prescription language, not the default the system pre-fills.
