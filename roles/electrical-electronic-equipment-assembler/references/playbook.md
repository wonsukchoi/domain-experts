# Playbook

## Solder joint inspection worksheet (IPC-A-610 style)

Fill for any joint of uncertain quality or per the sampling plan.

| Field | Value |
|---|---|
| Board/component | PCB #6604, U12 Lead 3 |
| Workmanship standard | IPC-A-610 Class 2 |
| Required wetting coverage | 270° minimum |
| Initial magnified inspection | ~180° coverage |
| Pass/fail | FAIL |
| Continuity test result (for comparison) | PASS — demonstrates continuity ≠ workmanship compliance |
| Rework performed | Reflow with additional solder |
| Post-rework inspection | 285° coverage |
| Pass/fail | PASS |

**Rule:** always inspect against the standard's specific numeric criteria under magnification — a passing continuity or functional test does not confirm workmanship standard compliance.

## ESD/crimp verification checklist

1. Confirm ESD sensitivity classification for each component before handling.
2. Use grounded, ESD-safe workstation and proper handling (wrist strap, grounded mat) for every ESD-sensitive component, regardless of how routine the handling seems.
3. For crimped connections, confirm crimp height measurement or pull test per the sampling plan — not visual inspection alone.
4. Document ESD procedure compliance and crimp verification results in the assembly's quality record.
5. If any ESD exposure is suspected (a dropped grounding strap, an ungrounded handling event), flag the affected component/unit for investigation rather than assuming no damage occurred.

## Workmanship standard reference by class (illustrative — always use the applicable governing standard)

| Class | Typical application | General reliability requirement |
|---|---|---|
| Class 1 | General consumer products | Basic functional performance |
| Class 2 | Dedicated service (industrial, commercial) | Extended life, some environmental stress expected |
| Class 3 | High-reliability (aerospace, medical, military) | Continued performance required, high consequence of failure |

**Rule:** confirm which class applies to the specific product/application before inspecting — using the wrong class's criteria either over- or under-verifies relative to what the actual application requires.
