# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual water balance analysis, curtailment schedule, or conservation evaluation — not for general reasoning (that's `SKILL.md`).

## Water balance / reliability worksheet

```
Basin: [name]

Average annual yield: 95,000 AF
Drought-scenario yield (1-in-20-yr sequence, worst year): 58,000 AF  <- use this for planning, not average
Mandated ecological flow requirement: 12,000 AF (binding, applied first)

Available for consumptive allocation in drought year: 58,000 - 12,000 = 46,000 AF

Demand (current):
  Agricultural (senior rights, priority date [year]): 38,000 AF
  Municipal (junior rights, priority date [year]): 45,000 AF, growing ~2%/yr
  Total demand: 83,000 AF

Strict-priority drought-year allocation:
  Agricultural (full senior right): 38,000 AF
  Municipal (residual): 46,000 - 38,000 = 8,000 AF
  Municipal shortfall: 45,000 - 8,000 = 37,000 AF (82% curtailment)

Gap-closing measures needed (does NOT close via conservation alone):
  Conservation (realistic 10-15% municipal demand reduction): 4,500-6,750 AF
  Drought-sharing agreement target: [X] AF
  Backup/banked supply target: [X] AF
  Remaining gap after all measures: [calculate]
```

## Curtailment priority schedule (communicate BEFORE shortage, not during)

```
Basin: [name]                          Priority date basis: [prior appropriation / other framework]

Priority order (senior to junior):
  1. [Right holder], priority date [date], [volume] AF
  2. [Right holder], priority date [date], [volume] AF
  3. [Right holder], priority date [date], [volume] AF
  ...

Ecological flow requirement: applied as a constraint BEFORE this priority list, not as the most
junior "right" in the list — confirm applicable legal framework for this specific basin.

Communication plan: this schedule distributed to all right-holders annually and updated when
priority changes, NOT introduced for the first time during an active shortage declaration.
```

## Conservation program evaluation

```
Program: [name]                        Target: [X]% demand reduction

Baseline demand (pre-program, weather-normalized): [X] AF/year
Modeled/targeted reduction: [Y]%
Measured actual reduction (post-implementation, weather-normalized): [Z]%

Realistic range check: well-designed urban conservation programs commonly achieve single-digit to
low-double-digit percentage reductions (verify against comparable program data for this context) —
if the required gap-closing target exceeds this range, conservation alone will not close it;
supply-side measures are needed for the remainder.

Gap not addressable by conservation = Total required reduction - realistic conservation potential
```
