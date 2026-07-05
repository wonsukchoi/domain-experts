# Compliance officer working vocabulary

Terms a compliance officer uses precisely and a generalist often blurs together. Format: definition → how a practitioner says it → common misuse.

**SAR vs. CTR** — A Currency Transaction Report (CTR) is mandatory for any single or same-day-aggregated cash transaction over $10,000, filed regardless of suspicion. A Suspicious Activity Report (SAR) is filed when activity appears designed to evade reporting requirements or otherwise indicates possible illegal activity, regardless of dollar amount.
In use: "No CTR was triggered here — every deposit stayed under $10K — but that's exactly the pattern that makes it a SAR."
Misuse: treating "no CTR required" as "no filing required." They test different things; a transaction can clear the CTR threshold test and still obligate a SAR.

**Structuring (smurfing)** — Deliberately breaking a transaction into smaller pieces, or spreading it across accounts/branches/days, specifically to stay under a reporting threshold. A federal offense under 31 U.S.C. § 5324 independent of whether the underlying funds are illicit.
In use: "The amounts alone aren't the violation — the pattern of staying just under $10K across three branches is the violation."
Misuse: assuming structuring requires proving the underlying funds were criminal proceeds. It doesn't; evading the reporting requirement is itself the offense.

**Beneficial ownership / CDD Rule 25% threshold** — Under FinCEN's Customer Due Diligence Rule, banks must identify any individual owning 25% or more of a legal-entity customer, plus one individual with significant managerial control, at account opening and on trigger events.
In use: "Ownership cert on file is 14 months stale — refresh it as part of this case, separate from the SAR timeline."
Misuse: treating the 25% threshold as a ceiling on diligence rather than a floor — a lower-ownership individual with clear control (e.g., sole signatory) still needs identification under the control-person prong.

**Three lines of defense** — Business unit (1st line) owns and manages its own risk; compliance/risk (2nd line) designs and independently tests controls; internal audit (3rd line) tests whether the 2nd line's testing was adequate.
In use: "Compliance drafting the branch's cash-handling procedure instead of testing it is 2nd line doing 1st-line work — that's an independence problem, not efficiency."
Misuse: treating the model as a reporting hierarchy rather than a functional separation — the violation is doing another line's job, regardless of who technically reports to whom.

**Material weakness vs. significant deficiency (SOX)** — A significant deficiency is a control gap important enough to merit the audit committee's attention; a material weakness is severe enough that a material misstatement wouldn't be prevented or detected on a timely basis. Only material weaknesses require public disclosure.
In use: "This is a significant deficiency for now — no misstatement has occurred — but two more quarters of override activity at this rate escalates it."
Misuse: using the terms interchangeably in a board memo; the disclosure obligation only attaches to the higher bar, so miscategorizing understates or overstates what's legally required to be said publicly.

**MRA / MRIA vs. self-identified finding** — A Matter Requiring Attention (MRA) or Matter Requiring Immediate Attention (MRIA) is a finding the regulator issued during an exam. A self-identified finding is one the compliance function found and reported on its own, before the exam.
In use: "Two of the three items on this quarter's tracker are self-identified — that's the signal the program is actually testing, not just waiting to be told."
Misuse: reporting both categories identically in a board deck. Regulators and boards read self-identified findings as evidence the program works; burying that distinction wastes the credit it earns.

**Root cause analysis** — Identifying the underlying reason a control failed (design gap, execution failure, or absence of any control), distinct from describing the symptom or assigning blame to an individual.
In use: "Root cause isn't 'the analyst missed it' — the alert threshold was set too high for that risk tier, so the analyst never saw it."
Misuse: stopping at "needs more training" without checking whether the control existed, was followed, or never existed — training is the fix for exactly one of those three, and the easiest to write down without verifying.

**Safe harbor (SAR confidentiality)** — Federal law protects institutions from liability for filing a SAR in good faith, and separately prohibits disclosing to the subject that a SAR was filed ("anti-tipping").
In use: "We don't tell the customer why the account is under enhanced monitoring — safe harbor confidentiality covers the filing itself."
Misuse: assuming safe harbor means the institution is immune from liability for the underlying conduct being reported, or that it excuses skipping the filing because "the customer will find out anyway."

**False-positive rate (alert tuning)** — The share of system-generated alerts that, on review, don't warrant a case or filing. Used to decide whether a monitoring scenario's thresholds need adjustment.
In use: "Rapid movement of funds is running a 98.7% false-positive rate with almost no true-positive yield — that scenario's threshold needs raising."
Misuse: treating a high false-positive rate alone as sufficient reason to loosen a scenario tied to a felony-level pattern like structuring or sanctions evasion — the asymmetric cost of missing a true positive there outweighs analyst time saved.

**Look-back review** — A retrospective review of historical transactions (often 12 months or a period specified by a regulator/consent order) to determine whether a newly discovered pattern or control gap existed earlier and went undetected.
In use: "Before we close this as a one-off, run a 12-month look-back — did this pattern exist before the alert caught it this time?"
Misuse: skipping the look-back because the current case is already resolved — the look-back is what tells you whether the control gap is closed or just the one instance.

**Control design effectiveness vs. operating effectiveness** — Design effectiveness asks whether a control, if performed as specified, would prevent or detect the risk. Operating effectiveness asks whether it actually was performed as specified, consistently, over the period tested.
In use: "The control is well-designed — the gap is operating effectiveness, it wasn't consistently run in Q3."
Misuse: fixing a control's operating failure (e.g., "remind people to do it") without checking whether the design itself was ever adequate, or vice versa — declaring a redesigned control "fixed" without testing whether it's actually being performed.

**Corrective action plan (CAP)** — The documented remediation plan tied to a specific finding, with an owner, a committed date, and (properly) an independent-retest step before closure.
In use: "The CAP for finding 2025-EX-03 is 62% complete against the June 30 commit date — on track, but flag it if July starts without full closure."
Misuse: marking a CAP "closed" the moment remediation is implemented, without the independent retest that confirms the fix holds under a live sample.

**Independence (2nd line)** — The organizational and practical separation of the compliance function from the business it oversees, such that a finding can escalate without being diluted or blocked by the unit it concerns.
In use: "Compliance reporting through the chief revenue officer instead of the CEO or board is an independence problem, regardless of how good the analysts are."
Misuse: equating independence with having a separate department name — a compliance team that's organizationally separate but whose budget, headcount, or bonus pool is controlled by the business it monitors isn't functionally independent.

**Risk appetite statement** — The board-approved statement of how much of a given risk type the institution is willing to accept, expressed in specific, measurable terms (not "we take compliance seriously").
In use: "Our risk appetite statement caps high-risk-geography wire exposure at 2% of total wire volume — we're at 3.1%, which is a board-level breach, not an operational note."
Misuse: writing or accepting a risk appetite statement in qualitative language with no measurable threshold, which makes it unenforceable as anything other than a values statement.
