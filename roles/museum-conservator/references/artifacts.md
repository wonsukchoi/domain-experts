# Museum Conservator — Artifacts

Filled templates for the two documents conservators produce most often. Populate these directly; don't describe them.

## Condition Report

```markdown
CONDITION REPORT

Object: [Accession #] — [object name/title]
Date of examination: [YYYY-MM-DD]
Examiner: [name, credential]
Context: [routine survey / incoming loan / outgoing loan / post-treatment / disaster response]

MATERIALS: [e.g., wool plain-weave, brass buttons, cotton thread]
DIMENSIONS: [H x W x D, cm]

OVERALL CONDITION: [Excellent / Good / Fair / Poor] — [one sentence summary]

DETAILED OBSERVATIONS (keyed to numbered diagram or photo set):
1. [Location] — [observation, e.g., "proper right shoulder seam: 3cm tear, fiber loss consistent with insect grazing, active frass present"]
2. [Location] — [observation]
3. [Location] — [observation]

IMAGING: Overall (front/back), raking light at [locations], UV-fluorescence at [locations if varnish/retouch suspected]
PRIOR TREATMENT EVIDENCE: [none observed / describe: e.g., "brass button #3 shows solder repair, non-original, likely prior conservation"]

STABLE vs. ACTIVE DAMAGE: [classify each item above]
RECOMMENDATION: [monitor / treat — see treatment proposal / no action needed]
```

**Example, filled** (excerpt matching the SKILL.md worked example):

```markdown
Object: 1988.14.2 — Union Army enlisted wool sack coat, jacket + trousers
Date of examination: 2024-03-11
Examiner: J. Alvarez, conservator
Context: routine IPM follow-up (trap-count spike triggered inspection)

MATERIALS: wool plain-weave (jacket/trousers), brass buttons (9), cotton lining
DIMENSIONS: jacket 68 x 55 x 10 cm (folded); trousers 90 x 45 x 8 cm (folded)

OVERALL CONDITION: Fair — active insect damage, structurally sound

DETAILED OBSERVATIONS:
1. Proper right shoulder seam — grazing loss to wool nap, ~4cm x 2cm area, fresh frass visible, consistent with active Tineola bisselliella larval feeding
2. Left cuff — old moth grazing, no fresh frass, appears historical/stable
3. Buttons (9) — stable, light tarnish, no action needed
4. Trouser waistband — stable, minor fiber loss at fold lines from handling, historical

IMAGING: Overall front/back (both garments), detail + raking light at shoulder seam
PRIOR TREATMENT EVIDENCE: none observed

STABLE vs. ACTIVE DAMAGE: Item 1 active; items 2–4 stable
RECOMMENDATION: Treat item 1 per low-temperature protocol (see treatment proposal); monitor items 2–4, no treatment needed
```

## Treatment Proposal / Treatment Report

```markdown
TREATMENT PROPOSAL

Object: [Accession #] — [object name]
Proposed by: [conservator], [date]
Approved by: [curator/registrar], [date]

REASON FOR TREATMENT: [what triggered this — link to condition report finding]
PROPOSED TREATMENT: [step-by-step method, materials named by product/brand where relevant]
ESTIMATED TIME/COST: [range, with the driver of the range named]
RISK IF UNTREATED: [specific, not "will get worse"]
RISK OF TREATMENT: [specific — chemical, mechanical, cosmetic]
ALTERNATIVES CONSIDERED: [named alternative(s) and why rejected]
REVERSIBILITY: [fully reversible / reversible with effort / irreversible — and why that's acceptable here]

--- treatment executed, filed as TREATMENT REPORT ---

DATE(S) OF TREATMENT: [range]
ACTUAL TREATMENT PERFORMED: [as proposed / deviations and why]
MATERIALS USED: [specific products, batch/lot if relevant — this is what a future conservator needs to identify and reverse the work]
BEFORE/AFTER PHOTOGRAPHY: [file references]
POST-TREATMENT CONDITION: [summary]
FOLLOW-UP MONITORING PLAN: [schedule and trigger for re-check]
```

## Environmental Excursion Log Entry

For when a data logger or manual reading shows a reading outside the set parameter for a case, room, or storage area — pairs with red-flags.md thresholds.

```markdown
ENVIRONMENTAL EXCURSION LOG

Location: [gallery/case/storage area ID]
Logger reading: [date/time, RH%, temp °C]
Set parameter: [ASHRAE class or institution-specific target, e.g., "Class A: 50% RH ±5%, 21°C ±2°C"]
Duration of excursion: [hours/days]
Likely cause: [HVAC failure / seasonal changeover / door propped open / logger malfunction — investigate before assuming equipment failure]
Objects affected: [list, by material sensitivity — most sensitive first]
Action taken: [temporary buffering — e.g., silica gel, portable dehumidifier — / object moved / HVAC ticket filed #___]
Follow-up: [re-check interval]
```

## IPM Trap Log (running table, populate monthly)

| Location | Trap ID | Month | Count | Species (if ID'd) | Baseline avg (trailing 12mo) | Flag? |
|---|---|---|---|---|---|---|
| Textile storage, shelf 3 | T-01 | 2024-02 | 3 | — | 2.8 | No |
| Textile storage, shelf 3 | T-01 | 2024-03 | 22 | Tineola bisselliella | 2.8 | Yes — 7.8x baseline |
| Loading dock | T-07 | 2024-03 | 14 | Dermestidae (carpet beetle) | 9.1 | No — seasonal range |

**Flag rule:** count exceeds 3x the trailing 12-month average for that trap, or any count of a known textile pest (webbing clothes moth, carpet beetle larvae) found inside a case rather than at a perimeter/loading location.
