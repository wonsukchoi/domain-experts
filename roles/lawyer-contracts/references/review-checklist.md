# Contract Review Checklist — Operational Process

How to actually run a review, from a cold PDF to a defensible markup. US commercial default.

---

## 1. First-pass triage (the 15-minute version)

Do not read page 1 to page N. Read in this order:

1. **Parties, preamble, signature blocks (1 min).** Correct legal entities? Right subsidiary? An agreement signed by the wrong entity protects nobody. Check signatory authority on bigger deals.
2. **Term and termination (2 min).** How long are we stuck, who can leave, what notice, auto-renewal window. If there's an auto-renewal with a notice deadline, calendar it *now* — this is the most common self-inflicted wound in commercial contracting.
3. **Limitation of liability (3 min).** Cap amount, what's carved out, consequential-damages waiver. This tells you the worst case before you know anything else.
4. **Indemnification (2 min).** Who defends whom against what. Confirm the vendor IP indemnity exists and isn't capped into meaninglessness.
5. **IP / data ownership (2 min).** Who owns deliverables, who owns and can use the data, what survives termination.
6. **Order of precedence + exhibit list (2 min).** Which document wins on conflict, and whether every referenced exhibit/SOW/order form is actually attached. A missing "Exhibit B (Security Requirements)" is a finding, not a footnote.
7. **Governing law / dispute resolution (1 min).** Where would we actually have to enforce this?
8. **Skim the definitions (2 min)** — flag any defined term that will decide a fight later ("Confidential Information," "Deliverables," "Fees," "Material Breach") and check it against how the operative clauses use it.

Output of triage: a one-paragraph risk summary and a decision — full review, targeted review of 3–4 clauses, or sign-as-is. Most contracts should not get a full review.

## 2. Risk tiering — how deep to go

Tier by **annual value × data/IP sensitivity × strategic dependence**, not by page count.

| Tier | Profile | Review depth |
|---|---|---|
| **Tier 1** | >$250k/yr, or vendor touches PII/PHI/payment data or source code, or business-critical dependency (can't operate without it), or exclusivity/non-compete terms | Full clause-by-clause review, playbook comparison, negotiation memo, escalation triggers defined |
| **Tier 2** | $25k–$250k/yr, moderate data (business-confidential, no regulated data), replaceable vendor | Triage + targeted review of LoL, indemnity, IP/data, termination, auto-renewal. Redline only playbook deviations |
| **Tier 3** | <$25k/yr, no sensitive data, standard tool/service, click-through or vendor form | Triage only. Flag anything uncapped, any IP grant of our content, auto-renewal terms. Otherwise accept — the review cost exceeds the risk |

Escalators that bump a contract up a tier regardless of dollars: personal data of customers/employees; our IP embedded in their product; exclusivity; publicity/reference rights; anything with an indemnity *we* give.

## 3. Cross-reference traps (where clean-looking contracts fail)

Run these checks mechanically — they catch more real defects than clever doctrinal analysis:

- **Defined terms vs. usage.** Every capitalized term: is it defined? Defined once? Used consistently? Watch for a term defined narrowly ("Services" = Exhibit A items) but used broadly in the liability clause, or vice versa. Also the reverse trap: an *undefined* capitalized term ("Customer Data") that everyone assumes means something specific.
- **Order of precedence.** If the MSA says it controls over SOWs, but the SOW template says "notwithstanding anything in the MSA…," you have a live conflict that the precedence clause may or may not resolve. Check whether order forms/SOWs can amend the MSA — if sales can sign an order form, sales can amend your MSA.
- **Exhibits overriding the body.** Read every exhibit *after* forming a view on the body. Security exhibits, SLAs, and DPAs routinely contain their own liability language, remedies ("credits are the sole and exclusive remedy"), or termination terms that quietly rewrite the deal.
- **Survival clause vs. reality.** Does the survival list include confidentiality, indemnification, LoL, data return, accrued payment? Does anything survive that *shouldn't* (e.g., a license to your data)?
- **Notice clause vs. operative deadlines.** If termination requires notice "in accordance with Section 14" and Section 14 requires certified mail to an address nobody monitors, your 30-day window is shorter than it looks.
- **Cross-references that point nowhere.** "Subject to Section 9.3" where Section 9 has two subsections — usually a fossil from an earlier draft, and evidence a clause was cut without cleanup. Find out what was cut.
- **Renewal pricing.** Auto-renewal "at then-current list price" or with an uncapped uplift is a price term hiding in the term clause. Cap renewal increases (CPI or 3–5%).

## 4. Markup etiquette (how to redline without burning the deal)

**Phrasing redlines:**
- Every substantive edit gets a comment stating (a) the risk it addresses, (b) in business terms, (c) with the proposed resolution already in the text. "Uncapped exposure for data-breach costs; proposed 3x super-cap per our standard" — not "revised for clarity."
- Propose language; never just strike. A deletion with no replacement reads as obstruction and forces another round-trip.
- Keep the counterparty's structure and defined terms where possible. Rewriting their clause in your house style triples review friction for zero risk reduction.
- Mark severity in the cover email: which items are *required* vs. *requested*. This is your credibility budget — if everything is required, nothing is.

**When to comment vs. edit:**
- **Edit** when you know the position and the fix (playbook items, defined-term corrections, cap numbers).
- **Comment (no edit)** when you need information first ("Does vendor hold SOC 2? If yes, we can accept this section as-is"), when the issue is a business decision, not a legal one (price, exclusivity scope — flag and route to the deal owner), or when the fix depends on which of two acceptable structures the counterparty prefers.
- **Neither** for style, grammar, or "I'd have drafted it differently." If it doesn't change risk or meaning, leave it alone.

**Process hygiene:**
- Redline in tracked changes against *their* latest version, never a clean retype — an undisclosed change discovered in a comparison destroys trust permanently, and counterparties always run comparisons.
- Version-name files with date and party turn (`MSA_AcmeCo_2026-07-06_CustomerTurn3`).
- Before sending: run a final compare against the prior turn to confirm your own markup contains only what you intend, and re-check that any accepted counterparty edits didn't change defined terms you rely on elsewhere.
- Keep a running issues list across turns (issue / our position / their position / status). By turn 3, memory is not a system of record.

## 5. Before signature — closing checks

- All exhibits attached, all blanks filled (dates, notice addresses, cap amounts, "[___]" placeholders — search the document for brackets).
- The signed version is the negotiated version (compare final PDF against last agreed redline).
- Signature authority confirmed for both sides; entity names match the preamble.
- Post-signing obligations calendared: renewal notice deadlines, insurance certificate delivery, security review dates, price-increase windows.
