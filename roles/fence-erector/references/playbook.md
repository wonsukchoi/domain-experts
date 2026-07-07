# Playbook

Filled sizing templates a fence erector runs before and during a job. Every figure below is a worked example following common code sections and industry rules of thumb — always verify the local frost-depth table, the adopted pool code, and the specific hardware manufacturer's rating before ordering material or signing off on a job.

## 1. Post embedment depth vs. frost line

Method: compare the 1/3-of-exposed-height rule against local frost depth + 6 in buffer; use whichever is greater. Frost-susceptible climates almost always make frost the governing number for anything over ~4 ft tall.

**Filled example — 6 ft exposed height, local frost depth 36 in:**

| Rule | Calculation | Result |
|---|---|---|
| 1/3-of-height rule | 6 ft ÷ 3 | 2.0 ft embedment |
| Frost + 6 in buffer | 36 in + 6 in | 3.5 ft embedment |
| **Governing depth** | max(2.0, 3.5) | **3.5 ft** |

Total post length = 6 ft exposed + 3.5 ft embedded = **9.5 ft** — order 10 ft stock and cut down, not 8 ft stock sized to the smaller number.

**Reference table by common frost depths (6 ft fence, 6 in buffer):**

| Local frost depth | Frost-driven embedment | Governs over 1/3-rule (2.0 ft)? |
|---|---|---|
| 12 in | 1.5 ft | No — use 2.0 ft |
| 24 in | 2.5 ft | Yes — use 2.5 ft |
| 36 in | 3.5 ft | Yes — use 3.5 ft |
| 48 in | 4.5 ft | Yes — use 4.5 ft |

**Takeaway:** below roughly 18 in of local frost depth, the 1/3-rule already covers it; above that, frost depth takes over and the gap between the two rules widens fast — always pull the actual local number rather than assuming a national average.

## 2. Footing diameter and concrete volume

Method: footing diameter ≈ 3x the post's actual width; concrete volume per hole = π × radius² × embedment depth.

**Filled example — 4x4 post (3.5 in actual, ≈0.29 ft), 3.5 ft embedment:**

- Footing diameter = 3.5 in × 3 ≈ 10.5 in → round up to a 12 in auger bit.
- Radius = 0.5 ft.
- Volume per hole = π × (0.5 ft)² × 3.5 ft ≈ 2.75 cu ft.

**Filled example — full run, 64 ft fence, 8 ft post spacing, 1 gate post:**

- Line/corner posts: 64 ft ÷ 8 ft = 8 spans → 9 posts.
- Plus 1 gate post = **10 holes total**.
- Total concrete = 10 × 2.75 cu ft = 27.5 cu ft = 27.5 ÷ 27 ≈ **1.02 cu yd**.
- Order **1.25 cu yd** (≈20% over) to cover spillage and hole-diameter variance from uneven auguring.

**Post-size-to-footing reference table:**

| Post (actual width) | Footing diameter (3x rule) | Nearest standard auger |
|---|---|---|
| 4x4 (3.5 in) | 10.5 in | 12 in |
| 6x6 (5.5 in) | 16.5 in | 18 in |
| 4 in round metal | 12 in | 12 in |

## 3. Wind-load sanity check for solid privacy panels

Method: force on a panel = exposed area × design wind pressure; check that the governing embedment depth (from Section 1) gives enough soil resistance, and if not, oversize the corner/end posts or shorten the span between them.

**Filled example — 8 ft × 6 ft panel, 90 mph design wind speed, Exposure B (~15 psf design pressure):**

- Exposed area = 8 ft × 6 ft = 48 sq ft.
- Lateral force = 48 sq ft × 15 psf = **720 lb** at that panel.
- Overturning moment about grade ≈ force × height-to-centroid = 720 lb × 3 ft = **2,160 ft-lb** per panel, resisted by the two posts bracketing it.

**Rule of thumb:** at moderate exposure (B) and design wind speeds up to ~100 mph, the frost-driven embedment depth from Section 1 is typically adequate for standard 4x4 line posts on 8 ft spacing; above that, or at Exposure C/D (open/coastal), shorten post spacing to 6 ft or step up to 6x6 posts at corners and ends, where the moment is highest.

## 4. Pool/child-safety barrier checklist

Method: run every measurement independently — none of these substitute for another.

| Requirement | Minimum/maximum | Fails if |
|---|---|---|
| Barrier height above grade | 48 in minimum | Any section under 48 in, including at a slope transition |
| Max gap under barrier | 4 in | Grade settles or erodes, opening a gap above 4 in |
| Max opening in barrier (mesh/picket gap) | 4 in (no 4 in sphere passes) | Decorative lattice or wide picket spacing exceeds 4 in |
| Gate operation | Self-closing and self-latching | Spring-hinge fails, or gate is propped open during a project phase |
| Release-mechanism height (pool side) | 54 in minimum above grade | Latch mounted at a "normal" 36-42 in gate-latch height |
| Climbable features (rails, decorative elements) within 45 in below top | None permitted | Horizontal rail placed low enough to act as a foothold |

**Filled example — client's 42 in aesthetic request vs. code:**

- Requested: 42 in to match the rest of the yard.
- Code minimum: 48 in.
- **Shortfall: 6 in — non-negotiable, build to 48 in regardless of matching height elsewhere on the property.**

## 5. Gate hinge and truss-rod sizing

Method: compare gate width and estimated weight against the sag-risk thresholds; below both thresholds, standard hinges suffice, at or above either, add hinges and a diagonal truss rod or specify welded steel framing.

| Gate width | Estimated weight | Hinge count | Truss rod / diagonal brace |
|---|---|---|---|
| ≤ 4 ft | ≤ 100 lb | 2-3 (use 3 near the threshold) | Not required |
| 4-6 ft | 100-200 lb | 3 | Required |
| 6-8 ft (single leaf) or double-drive | 200+ lb | 3-4, plus a king post at the hinge side | Required, or welded steel frame |

**Filled example — 4 ft cedar walk gate, estimated ~80 lb:**

- Width and weight both sit under the mandatory-truss threshold, but width is exactly at the 4 ft line — use 3 hinges for margin rather than the minimum 2, no truss rod required yet.
- Note on file: if the gate is later widened or a second leaf added, re-run this table — the truss-rod requirement triggers immediately at that point.
