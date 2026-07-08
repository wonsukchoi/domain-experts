# Playbook

Filled formulas, thresholds, and worked mini-examples a petroleum engineer runs against. Verify against the governing regulator (SEC, state O&G commission), the operator's own well-control manual, and the current API/ISO/SPE edition — these are commonly applied industry standards, not a substitute for the jurisdiction- or lease-specific rule in front of you.

## 1. Arps decline curve equations

**Hyperbolic:** q(t) = qi / (1 + b·Di·t)^(1/b), for 0 < b < 1 (or b=1 harmonic special case).
**Exponential (b=0):** q(t) = qi·e^(-Di·t).
**Cumulative, hyperbolic:** Np(t) = [qi/((1-b)·Di)]·[1-(q(t)/qi)^(1-b)].
**Cumulative, exponential:** Np(t) = (qi - q(t))/Di.
**Instantaneous secant decline:** D(t) = Di/(1+b·Di·t).

*Example (gas well, different case from SKILL.md's oil well): qi=4.2 MMcf/d, Di=0.55/yr, b=0.5. At t=3 yr: q(3) = 4.2/(1+0.5×0.55×3)^(1/0.5) = 4.2/(1.825)^2 = 4.2/3.331 = 1.261 MMcf/d. Np(3) = [4.2×365/((1-0.5)×0.55)]·[1-(1.261/4.2)^0.5] = (5,569.1)·[1-0.548] = 2,517 MMcf.*

**Rule:** apply a terminal decline rate Dmin (commonly 5-10%/yr, basin- or company-specific) once the instantaneous secant decline D(t) falls to that floor, and switch the forecast to exponential from that point forward — an unswitched hyperbolic tail with b>=1 has no finite EUR.

## 2. Material balance — P/Z method (volumetric gas reservoir)

**P/Z vs. Gp is linear:** P/Z = (Pi/Zi) - (Pi/Zi)/G × Gp, where G = original gas in place (OGIP), Gp = cumulative gas produced, Pi/Zi = initial pressure/Z-factor.

*Example: Pi/Zi = 5,800 psia. Two survey points: at Gp1=8 Bcf, P/Z1=4,950; at Gp2=20 Bcf, P/Z2=3,600. Slope = (3,600-4,950)/(20-8) = -1,350/12 = -112.5 psi/Bcf. G = -(Pi/Zi)/slope = -5,800/-112.5 = 51.6 Bcf. Cross-check: extrapolating the line to P/Z=0 gives Gp=G=51.6 Bcf, consistent.*

**Rule:** if the P/Z vs. Gp plot curves rather than fitting a straight line, water/aquifer influx is likely present — switch to the generalized material balance equation (adds a We influx term) rather than forcing a straight-line fit through curved data.

## 3. Vogel's IPR (below bubble point, solution-gas drive)

**q/qmax = 1 - 0.2(Pwf/Pr) - 0.8(Pwf/Pr)²**, where qmax is the absolute open flow potential (AOF), Pr = average reservoir pressure, Pwf = flowing bottomhole pressure.

*Example: a test point of q=400 bopd at Pwf=1,800 psi, Pr=3,000 psi (Pwf/Pr=0.6). qmax = q / [1-0.2(0.6)-0.8(0.6)²] = 400/[1-0.12-0.288] = 400/0.592 = 675.7 bopd. Forecasting at a lower Pwf=1,000 psi (Pwf/Pr=0.333): q = 675.7×[1-0.2(0.333)-0.8(0.333)²] = 675.7×[1-0.0667-0.0889] = 675.7×0.8444 = 570.6 bopd.*

**Rule:** valid only below the bubble point (two-phase flow). Above bubble point, use a straight-line productivity index instead: q = J×(Pr-Pwf), with J (PI, bbl/d/psi) determined from a single well test.

## 4. Nodal analysis — IPR x VLP intersection

The well produces where the IPR curve (reservoir deliverability, falling with rate) crosses the vertical lift performance (VLP/tubing) curve (rising with rate as friction losses grow), not at the IPR curve's unconstrained value.

*Example: at Pwf=1,200 psi, IPR (from Section 3's Vogel fit) predicts q=515 bopd; the tubing-size-specific VLP curve at that same Pwf predicts q=390 bopd for the installed 2-7/8" tubing. The two curves actually intersect near Pwf≈1,340 psi, q≈365 bopd — that intersection, not the IPR-alone value, is the well's real producing point. A smaller tubing size or an artificial lift method that lowers the VLP curve is what moves the intersection toward the IPR curve's higher potential.*

**Rule:** re-run the VLP curve whenever tubing size, artificial lift method, or wellhead backpressure changes — the IPR curve alone never tells you the actual rate.

## 5. Casing/tubing burst, collapse, and triaxial design check

**API minimum internal yield (burst) pressure, thin-wall pipe:** P_burst = 0.875 × (2×Yp×t)/D, where Yp = minimum yield strength (psi), t = nominal wall thickness (in), D = outside diameter (in); the 0.875 factor accounts for manufacturing wall-thickness tolerance.

*Example: 5.5" OD, 17 lb/ft, N-80 casing (t=0.304 in, Yp=80,000 psi). P_burst = 0.875×(2×80,000×0.304)/5.5 = 0.875×48,640/5.5 = 0.875×8,843.6 = 7,738 psi (API rated burst).*

**Design factor:** applied working pressure limit = P_burst / DF, with a commonly used minimum burst design factor of 1.10-1.125. At DF=1.10: working limit = 7,738/1.10 = 7,035 psi.

**Triaxial (von Mises) check under combined load:** axial tension reduces effective collapse resistance and axial compression reduces effective burst resistance versus the zero-axial-load catalog rating; the governing check computes the von Mises equivalent stress from the combined axial, radial, and tangential stress components at the pipe wall and compares it to yield, not burst/collapse independently.

**Rule:** run the worst credible load case (max anticipated surface pressure for burst; full evacuation, e.g., during lost circulation, for collapse) through the triaxial check, not the single-axis catalog rating alone — the catalog rating assumes zero axial load, which is never the field condition on a landed string carrying its own weight.

## 6. Voidage replacement ratio (VRR) — waterflood/injection monitoring

**VRR = (reservoir-barrel injection volume) / (reservoir-barrel production volume, oil+water+gas at reservoir conditions)**, over the same period.

*Example: monthly oil production 45,000 bbl (Bo=1.25 rb/stb → 56,250 rb), water production 30,000 bbl (Bw≈1.0 → 30,000 rb), associated gas at reservoir conditions ≈ 4,000 rb equivalent. Total reservoir voidage = 90,250 rb. Water injected: 82,000 bbl at Bw=1.0 → 82,000 rb. VRR = 82,000/90,250 = 0.909.*

**Rule:** VRR sustained below 1.0 across multiple reporting periods means withdrawal is outpacing replacement — investigate injector count, injectivity, and facility injection capacity before assuming reservoir pressure will hold; VRR well above 1.0 for an extended period risks parting pressure/fracture-induced channeling at the injectors.

## 7. SPE-PRMS reserves categories and SEC pricing basis

| Category | Cumulative probability standard | Typical evidence required |
|---|---|---|
| Proved (1P) | Reasonable certainty, ~P90 | Direct offset production, established reliable-technology area, current economics at SEC price |
| Proved + Probable (2P) | ~P50 | More likely than not to be recovered; less direct offset support acceptable |
| Proved + Probable + Possible (3P) | ~P10 | Low but non-negligible chance of recovery; geologically plausible but unconfirmed |

**SEC price basis for filed reserves:** trailing 12-month average of the first-day-of-each-month price (not a single current spot price, not a forward strip), held flat for the life of the reserves unless a contract specifies otherwise.

**Rule:** a Proved location must have direct offset well support and pass the current-economics test at the SEC price basis; missing either drops it to Probable or Possible regardless of the team's geologic confidence.
