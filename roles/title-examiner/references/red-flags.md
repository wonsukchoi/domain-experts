# Red flags — signals a title examiner notices instantly

Smell tests with thresholds. Any one alone can be resolvable; two or more on the same chain of title is a pattern worth a deeper review before issuing a commitment.

### A grantor in the chain doesn't match the prior instrument's grantee name exactly, with no documented explanation
- **Usually means:** either a genuine gap in the chain of title, or an unrecorded name change (marriage, court order) that needs documentation to bridge — either way, it can't be waved past as a minor discrepancy.
- **First question:** "Is there a recorded document (marriage certificate, name-change order) bridging this name difference, or is this an actual break in the chain?"
- **Data to pull:** the two instruments in question, any recorded name-change documentation, chain-of-title tracing log (see `references/artifacts.md` §3).

### A judgment or lien matches the current owner's name with no corroborating identifier checked
- **Usually means:** the examiner may be about to attach (or dismiss) an instrument based on name alone, when a different person entirely could share the name.
- **First question:** "What corroborating identifiers — address, occupation, suffix, date of birth — have actually been checked against the underlying case file?"
- **Data to pull:** the judgment/lien's underlying case file, current owner's identifying information from the loan/deed file, defect classification worksheet (see `references/artifacts.md` §2).

### A found judgment or tax lien is treated as a live encumbrance without checking its enforceability period
- **Usually means:** the instrument may already be legally expired and unenforceable, making a demand for payoff or release unnecessary.
- **First question:** "How old is this judgment/lien relative to the jurisdiction's enforcement or renewal period, and has it been renewed if applicable?"
- **Data to pull:** judgment/lien recording date, jurisdiction's specific enforcement/renewal statute, any recorded renewal or satisfaction.

### The search period covers less than the jurisdiction's marketable title act requirement
- **Usually means:** the search may not actually establish marketable title even if no defects were found within the (too-short) period searched.
- **First question:** "What's this jurisdiction's specific marketable title act period, and does the search actually cover a root of title that far back?"
- **Data to pull:** state marketable title act statute, chain-of-title tracing log showing the root of title's date relative to today.

### A priority conclusion is reached without first confirming whether the jurisdiction is race, notice, or race-notice
- **Usually means:** the same facts can produce opposite priority outcomes depending on which recording statute type governs — an analysis that skips this step may reach the wrong conclusion regardless of how carefully the facts were otherwise reviewed.
- **First question:** "Which recording statute type governs this jurisdiction, and does the priority analysis actually apply that specific rule?"
- **Data to pull:** jurisdiction's recording statute, recording statute type quick-reference (see `references/artifacts.md` §4), timeline and notice status of the competing claims.

### A title defect is classified as requiring a full cure (corrective deed, quiet title action) without checking whether it could be insured over instead
- **Usually means:** the transaction may face an unnecessary delay if a faster underwriting exception would have resolved the issue just as effectively.
- **First question:** "Has this specific defect actually been evaluated against underwriting's insurable-with-exception standard, or was 'must cure' assumed by default?"
- **Data to pull:** defect classification worksheet (see `references/artifacts.md` §2), underwriter's specific guidelines for this defect type.

### An encumbrance search was run only against the current owner's name, not every name that has appeared in the chain
- **Usually means:** an encumbrance recorded against a prior owner — one still enforceable and potentially attached to the property, not just the individual — may have been missed entirely.
- **First question:** "Has the judgment/lien/UCC search been run against every grantee name that has held title during the search period, not just the current owner?"
- **Data to pull:** chain-of-title tracing log's full list of names, encumbrance index search results for each name individually.

### A survey-based issue (encroachment, unrecorded easement) is assumed covered by the recorded-instrument search alone
- **Usually means:** a physical boundary or encroachment issue that wouldn't appear in any recorded index may go undetected without an independent current survey review.
- **First question:** "Has a current survey been reviewed separately from the recorded-instrument search, or is the assumption that recorded title search covers this too?"
- **Data to pull:** current survey (if obtained), comparison against the legal description and any recorded easements.
