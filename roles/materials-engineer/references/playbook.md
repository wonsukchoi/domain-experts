# Playbook

Filled worked calculations for the three artifact types this role produces most often: a material-selection ranking, a hardenability determination, and an inspection-interval derivation. Populate with the actual component's numbers; the structure and arithmetic below are real and reconcile.

## Material selection — Ashby performance index

**Load case:** minimum-mass cantilever beam, fixed bending stiffness (stiffness-limited, not strength-limited). For this load case the performance index to *maximize* is M1 = E^(1/2) / ρ (Ashby, *Materials Selection in Mechanical Design*). A different load case uses a different index — strength-limited tension in a minimum-mass part maximizes Sy / ρ; a minimum-mass axial-stiffness tie maximizes E / ρ. Confirm the load case before pulling an index off a chart.

| Candidate | E (GPa) | ρ (g/cm3) | M1 = E^0.5/ρ | Rank | Relative mass for equal stiffness (M1,steel / M1,candidate) |
|---|---|---|---|---|---|
| AISI 4340 steel | 205 | 7.85 | 1.82 | 5 | 1.00 (baseline) |
| Ti-6Al-4V | 113.8 | 4.43 | 2.41 | 4 | 0.76 |
| 6061-T6 aluminum | 68.9 | 2.70 | 3.07 | 3 | 0.59 |
| AZ31B magnesium | 45.0 | 1.77 | 3.79 | 2 | 0.48 |
| Unidirectional CFRP (fiber axis) | 135.0 | 1.60 | 7.26 | 1 | 0.25 |

Steel has the highest absolute modulus (205 GPa, more than any other candidate) and ranks *last* on the index that actually matters for this load case — the beam's stiffness per unit mass depends on E^0.5/ρ, not E alone, and steel's high density outweighs its modulus advantage. Switching from steel to 6061-T6 at equal bending stiffness cuts mass to 59% of the steel baseline; CFRP cuts it to 25%, before any layup or manufacturability screen.

**Next screen — eliminate on constraints the index doesn't capture:** service temperature ceiling, joining method compatibility, galvanic pairing with adjacent parts, and a relative material cost multiplier (order-of-magnitude, verify current pricing before a sourcing decision — steel ≈1x, aluminum ≈3x, magnesium ≈6-8x, titanium ≈20-25x, aerospace-grade CFRP ≈12-18x per kg, as commonly cited in materials-selection texts). A candidate that wins the index but fails a hard constraint (e.g., CFRP against a >150°C continuous service temperature for a standard epoxy matrix) drops out regardless of rank.

## Hardenability determination — Jominy/Grossmann

**Question:** does a candidate steel through-harden to spec at the core of the actual section size, given the shop's quench severity — not just at the surface where a Rockwell tester usually gets applied.

**Given:** 50 mm (2 in) diameter round bar, oil quench with moderate agitation (quench severity H = 0.35, per Grossmann's H-value scale). Spec requires minimum 40 HRC at the bar's center after quench and temper.

**Step 1 — convert section size and quench severity to an equivalent Jominy distance.** Using the standard Lamont bar-diameter/quench-severity correlation chart (round bar diameter vs. H-value, read at the center position): a 50 mm diameter bar at H = 0.35 equates to a center-position Jominy distance of approximately **J = 12 (in sixteenths of an inch from the quenched end, i.e., 12/16 in ≈ 19 mm)**. This conversion is the load-bearing step — it translates "how big is the part and how hard is the quench" into "which point on the Jominy curve applies."

**Step 2 — read each candidate's Jominy curve at J = 12/16 in:**

| Steel | Jominy hardness at J=4/16in (HRC) | at J=8/16in (HRC) | at J=12/16in (HRC) | Meets 40 HRC core spec? |
|---|---|---|---|---|
| AISI 4140 (Cr-Mo, H-band) | 54 | 50 | 46 | Yes — 6 HRC margin |
| AISI 1040 (plain carbon) | 55 | 28 | 24 | No — 16 HRC short |

Both steels can be flame- or induction-quenched to a similar *surface* hardness (54-55 HRC) — a surface-only hardness check would pass either grade. The 1040's hardness collapses past the first few sixteenths of an inch because it has no alloying content to slow the transformation at depth; the 4140's chromium and molybdenum sustain hardenability through the section. Specifying "40 HRC minimum, surface Rockwell check" would have let 1040 ship on a part that fails at the core; specifying the Jominy distance (or an H-steel hardenability band) catches it before heat treat.

**Deliverable — heat-treat spec callout:** "Material: AISI 4140H per ASTM A304, hardenability band per SAE J1268. Quench: oil, H = 0.30-0.40. Temper to 46-50 HRC core hardness, verified by sectioning and hardness traverse at bar center on first-article; production verification by Jominy end-quench test per ASTM A255 at incoming inspection, J12/16in >= 44 HRC minimum acceptance."

## Inspection interval — Paris-law crack growth to critical flaw size

**Given:** high-strength steel component (KIC = 60 MPa*m^0.5, typical for quenched-and-tempered 4340 at this strength level — ASM/Barsom & Rolfe data), edge-crack geometry factor Y = 1.12, applied cyclic stress range at the flaw location Δσ = 300 MPa, smallest flaw an in-service NDI method reliably detects (90% probability of detection at 95% confidence) a0 = 1.0 mm.

**Step 1 — critical flaw size.** a_c = (1/π) x (KIC / (Y x σmax))^2, with σmax the peak stress = 560 MPa: a_c = (1/π) x (60 / (1.12 x 560))^2 = (1/π) x (60/627.2)^2 = (1/π) x 0.009153 = **0.00291 m = 2.91 mm**.

**Step 2 — cycles to grow from a0 to a_c, Paris law.** da/dN = C(ΔK)^m with ΔK = Y*Δσ*sqrt(pi*a); using generic steel constants C = 6.9x10^-12, m = 3.0 (m/cycle, MPa*m^0.5 units — Barsom & Rolfe). Integrating da/dN = C(YΔσ)^3 pi^1.5 a^1.5 from a0 to a_c:

N = 2(a0^-0.5 - a_c^-0.5) / [C (YΔσ)^3 pi^1.5]

a0^-0.5 = 1/sqrt(0.001) = 31.62; a_c^-0.5 = 1/sqrt(0.00291) = 18.53; difference x2 = 26.18.
(YΔσ)^3 = (1.12 x 300)^3 = 336^3 = 3.79x10^7. pi^1.5 = 5.568.
Denominator = 6.9x10^-12 x 3.79x10^7 x 5.568 = 1.457x10^-3.
N = 26.18 / 1.457x10^-3 ≈ **17,970 cycles** from a barely-detectable 1 mm flaw to the 2.91 mm critical size.

**Step 3 — set the inspection interval.** Damage-tolerant practice (e.g., the logic behind FAA AC 25.571) sets the inspection interval at a fraction of the calculated crack-growth life, not the full life, to cover scatter in both the growth-rate constants and the detection assumption — a factor of 2 on the calculated cycles is a common conservative default. Interval = N / 2 ≈ **8,985 cycles**, rounded down to **8,500 cycles between NDI inspections**, using a method with demonstrated 90/95 POD at 1.0 mm on this geometry. If the qualified NDI method's smallest reliable detection size is larger than 1.0 mm, re-run Step 2 with the actual a0 — the interval shrinks fast as a0 approaches a_c.
