# Security risk artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Incident layer diagnosis (filled — see Worked example in SKILL.md for full narrative)

| Layer | Function | Did it fail here? |
|---|---|---|
| Perimeter | Keep unauthorized people out of the building | No — badge-based entry worked as designed |
| Access control | Ensure only currently-authorized badges grant access | **Yes — stale contractor badge, 45 days post-departure, still active** |
| Monitoring/detection | Catch and flag suspicious activity | Not tested — no camera coverage in this storage room |
| Response | React to and investigate the incident | Worked — incident was investigated and root cause identified |

**Rule applied:** the fix targets the layer that actually failed (access control), not the layer leadership's initial instinct focused on (detection/cameras).

## 2. Access review audit (filled example)

| Finding | Count | Detail |
|---|---|---|
| Total badges issued (active + inactive) | 620 | 450 current employees + 170 former employees/contractors |
| Stale active badges found | 34 | Average 62 days post-departure, still active |
| Last full access review conducted | 14 months ago | Policy requires quarterly (3-month) review |
| Estimated expected annual loss from stale badges | ~$2,244/year | 34 badges × 3% annual misuse probability × $2,200 avg incident value |

**Rule applied:** the audit quantifies the systemic gap (34 stale badges), not just the single incident, and prices the fix against this larger exposure.

## 3. Control cost/benefit comparison (filled example)

| Option | Cost | Layer addressed | Addresses root cause of this incident? |
|---|---|---|---|
| Building-wide camera upgrade (60 cameras) | $85,000 | Detection | No — wouldn't have prevented the stale-badge access |
| Automated access review integration | $8,500 one-time + $400/month ($12,700 year 1) | Access control | Yes — directly closes the stale-badge gap |

**Rule applied:** the cheaper option ($12,700 vs. $85,000) is recommended because it addresses the layer that actually failed, not because it's cheaper in isolation — cost and root-cause fit both point the same direction here.

## 4. Threat model summary (filled example, office facility)

| Adversary/scenario | Likelihood | Consequence | Primary controls |
|---|---|---|---|
| Opportunistic theft (unsecured items, stale access) | Moderate | Low-moderate (individual item loss) | Access review, secured storage, badge audit |
| Insider misuse of legitimate access | Low-moderate | Moderate-high (data, asset access) | Background screening, access review, behavioral awareness |
| Workplace violence | Low | High | Visitor management, emergency response plan, staff training |
| Targeted intrusion (industrial espionage) | Low | High (IP loss) | Layered access control, monitoring at sensitive areas, need-to-know access design |

**Rule applied:** control investment is weighted by likelihood × consequence for this specific facility's actual threat profile, not a generic checklist applied uniformly regardless of context.
