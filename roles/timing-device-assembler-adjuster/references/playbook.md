# Playbook

## Multi-position/temperature rate verification worksheet

Fill for any precision timing mechanism before final release.

| Position/Condition | Rate (sec/day) | Spec (±4 sec/day) | Pass/Fail |
|---|---|---|---|
| Dial up (room temp) | +1 | ✓ | Pass |
| Dial down | +3 | ✓ | Pass |
| Crown up | -2 | ✓ | Pass |
| Crown down | +5 | ✗ | **FAIL** |
| Crown left | 0 | ✓ | Pass |
| Temperature 4°C | -3 | ✓ | Pass |
| Temperature 38°C | +6 | ✗ | **FAIL** |

**Action if any fail:** investigate the specific component associated with the failure pattern (escapement for position-specific issues, hairspring for temperature-specific issues) before re-testing. Never release based on a passing result in only one or two conditions.

## Component-specific lubrication reference table (illustrative — always use the movement/mechanism's actual specification)

| Component | Typical lubricant type | Notes |
|---|---|---|
| Escapement pivots | Fine synthetic oil, low viscosity | Critical for consistent rate; precise amount matters |
| Mainspring barrel | Grease, moderate viscosity | Different friction/load profile than pivots |
| Balance wheel jewels | Fine synthetic oil, very low viscosity | Extremely sensitive to over-lubrication |
| Gear train pivots | Fine oil, viscosity per gear load | Match to specific gear's load/speed |

**Rule:** always use the specific movement/mechanism manufacturer's lubrication specification — this table is illustrative of the principle (component-specific matching), not a substitute for actual specified lubricants.

## Assembly sequence/checkpoint guide

1. Confirm the specified assembly sequence before starting — do not reorder for convenience.
2. At each checkpoint (as specified, typically after key sub-assemblies), verify function/fit before proceeding to the next component that would obscure access.
3. Perform cleanliness verification at each stage where contamination risk is highest (before closing up any sealed section).
4. Apply lubrication at the specified stage — some lubricants must be applied before certain components are installed, not after.
5. Complete final rate regulation and multi-position/temperature verification only after all components are installed and the mechanism is in its final assembled state.
6. Document each checkpoint's completion and any findings before proceeding to final assembly.
