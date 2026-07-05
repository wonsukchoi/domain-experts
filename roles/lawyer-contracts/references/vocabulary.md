# Working Vocabulary — Terms a Generalist Misuses

US commercial usage. Format per entry: what it means → how a practitioner uses it in a sentence → the common misuse.

---

**Direct vs. consequential damages.**
Direct (general) damages flow naturally from the breach itself — the value of what you were promised and didn't get. Consequential (special) damages are downstream losses arising from your particular circumstances, recoverable only if foreseeable to the breaching party at contracting (*Hadley v. Baxendale*).
*Usage:* "Their waiver excludes consequential damages, so we added a sentence deeming breach-notification costs direct damages."
*Misuse:* assuming "lost profits" are always consequential — lost profits on the contract itself are typically *direct*; lost profits from collateral business are consequential. Courts split on categorizing data-breach response costs, which is exactly why you characterize them in the contract instead of litigating it later.

**Indemnify vs. hold harmless vs. defend.**
Indemnify = reimburse losses after they're incurred. Defend = pay for and run the lawsuit from day one. Hold harmless = arguably also shields against the indemnitee's own claims/liability (some courts treat it as a synonym for indemnify; some give it independent bite).
*Usage:* "They offered 'indemnify and hold harmless' but struck 'defend' — meaning we'd front years of litigation costs and chase reimbursement."
*Misuse:* treating the triplet as one ritual phrase. "Defend" is frequently the word with the most cash-flow consequence; notice which of the three is missing.

**Best efforts vs. commercially reasonable efforts.**
Efforts clauses set how hard a party must try when it doesn't promise the result. Conventional hierarchy: best efforts > reasonable best efforts > commercially reasonable efforts, with "best efforts" read (in some states) to require substantial cost even against your own interests. Delaware courts have largely collapsed the distinctions; New York keeps more of them — jurisdiction matters.
*Usage:* "Give sales 'commercially reasonable efforts' on the migration commitment; 'best efforts' invites an argument we had to spend whatever it took."
*Misuse:* granting "best efforts" as if it were a politeness upgrade, or leaving *any* efforts standard undefined when you could specify the actual actions required ("shall allocate at least two FTEs") — defined actions beat adverbs.

**Representations vs. warranties vs. covenants.**
A representation is a statement of *present or past fact* inducing the deal (remedy: misrepresentation claims, possibly rescission). A warranty is a *promise that a fact is and will be true* (remedy: breach-of-contract damages, no reliance needed). A covenant is a promise to *do or not do something in the future*.
*Usage:* "Make the security program a covenant, not just a signing-date rep — we need it true for the whole term."
*Misuse:* writing "Vendor represents that it will comply with law" — a future promise mislabeled as a rep. It matters at remedy time: reps can support fraud claims (which escape liability caps); covenants can't.

**Condition precedent.**
An event that must occur before a duty to perform arises at all. Failure of a condition means the duty never triggers — it is not itself a breach.
*Usage:* "Board approval is a condition precedent to closing; if it fails, no one breached, the deal just doesn't happen."
*Misuse:* confusing conditions with covenants. Courts disfavor forfeitures and will read ambiguous language as a covenant (breach + damages) rather than a condition (no duty at all) — if you want a true condition, say "provided that" / "subject to" and mean it.

**Novation vs. assignment.**
Assignment transfers rights (and delegation transfers duties), but the original party generally *remains liable* unless released. Novation substitutes a new party by agreement of all three parties, releasing the original.
*Usage:* "Their acquirer wants to take over the contract — fine, but by assignment they keep AcmeCo on the hook; a novation lets AcmeCo off."
*Misuse:* saying "we assigned the contract, so we're out." You're not. Only a novation (or express release) ends the assignor's liability.

**Liquidated damages vs. penalty.**
Liquidated damages: a pre-agreed damages amount, enforceable if it's a reasonable forecast of harm that would be difficult to prove. A penalty: an amount designed to punish/coerce — unenforceable in US courts (unlike some civil-law systems, where penalty clauses are valid subject to judicial reduction).
*Usage:* "Set the SLA credit at a defensible estimate of downtime cost and recite the difficulty-of-proof rationale — a number picked to sting gets struck as a penalty."
*Misuse:* labeling something "liquidated damages" and assuming the label controls. Courts look at substance. Also: a *sole-remedy* liquidated-damages clause (typical SLA credits) can silently cap your recovery for outages — sometimes that's the vendor's real goal.

**Material breach.**
A breach serious enough to excuse the other side's performance and justify termination — not just any breach. Left undefined, "material" is decided by a court using multi-factor tests after the fact.
*Usage:* "Define material breach to include any breach of Sections 7 (Confidentiality) and 9 (Data Protection), so we're not litigating materiality mid-incident."
*Misuse:* terminating over a breach a court later finds immaterial — which converts *your termination* into the material breach. When in doubt, use notice-and-cure and paper the record.

**Time is of the essence.**
Magic words making deadlines strict conditions — missing one becomes material breach territory, rather than the default rule that reasonable delay is tolerated.
*Usage:* "Add time-is-of-the-essence to the closing deliverables only; applying it contract-wide turns every slipped date into a termination fight."
*Misuse:* sprinkling it globally as boilerplate strength, not realizing it cuts both ways on your own deadlines.

**Sole remedy / exclusive remedy.**
Language making one remedy (credits, repair, refund) the *only* recourse for a given breach.
*Usage:* "SLA credits as sole remedy is acceptable only if chronic failure — say, three missed months in six — triggers a termination right."
*Misuse:* reading a remedies clause as *additive* when the word "exclusive" makes it a ceiling. This is the quiet companion of the LoL clause and often the more binding one.

**Consequential loss carve-in via indemnity.**
Not a term of art, but a structural trap: indemnification obligations often cover third-party claims that *include* consequential-type losses; whether the consequential-damages waiver applies to indemnity obligations is a classic drafting fight.
*Usage:* "State expressly that the consequential-damages waiver does not apply to the parties' indemnification obligations."
*Misuse:* assuming the waiver and the indemnity live in separate worlds. Unaddressed, courts split.

**Entire agreement / merger clause.**
Declares the written contract the complete and final deal, invoking the parol evidence rule to exclude prior discussions, emails, and drafts.
*Usage:* "The sales deck promised 99.99% uptime? The merger clause means it isn't part of the contract — get it into the SLA exhibit."
*Misuse:* believing a merger clause blocks *fraud* claims (generally it doesn't, though a specific non-reliance clause might, depending on the state) — or forgetting it kills your *own* side letters and email assurances too.

**Ipso facto clause.**
A clause terminating the contract or modifying rights upon a party's bankruptcy or insolvency.
*Usage:* "Keep the insolvency-termination trigger for out-of-court situations, but plan around it: it's largely unenforceable once they actually file, under Bankruptcy Code §365(e)."
*Misuse:* relying on it as your exit from a counterparty in Chapter 11. The automatic stay and §365 mean the debtor can usually keep the contract alive whether you like it or not.

**Estoppel / waiver (course-of-dealing drift).**
Waiver: intentionally giving up a known right — which courts can infer from conduct, like accepting late payments for a year. Anti-waiver ("no waiver of any breach shall constitute a waiver of any other breach") clauses help but are not bulletproof.
*Usage:* "If we intend to keep the strict delivery deadline, send a reservation-of-rights notice each time we accept late performance."
*Misuse:* assuming the contract-as-written stays fully enforceable while the parties behave differently for months. Paper beats memory, but conduct can beat paper.

**Force majeure vs. impossibility/impracticability vs. frustration of purpose.**
Force majeure is a *contractual* excuse defined by the clause. Impossibility/impracticability and frustration are narrow *common-law* backstops that apply when the contract is silent — and courts grant them rarely.
*Usage:* "If the FM clause doesn't list it, don't count on common-law impracticability to save us — negotiate the termination right instead."
*Misuse:* using "force majeure" loosely for any hard situation. Economic hardship — performance becoming unprofitable — is almost never an excuse under any of the three doctrines in US courts.
