# Working Vocabulary — Terms Generalists Misuse

Format per term: definition, a sentence a practitioner would actually say, and the common misuse.

---

**Technical win vs. champion**
A technical win is the evaluators' and champion's agreement that the product meets the requirements — an event, confirmed at a point in time. A champion is a person, the internal advocate who carries that agreement forward through procurement and leadership.
**In use:** "We have the technical win as of Friday's exit report; whether the champion can carry it through budget approval is a separate question."
**Common misuse:** treating "we have a champion" as equivalent to "we have a technical win" — a champion can exist before any evaluation has actually happened, and an evaluation can be won without one strong advocate (multithreaded deals sometimes have several moderate ones instead).

**POC vs. pilot**
A POC (proof-of-concept) is a bounded technical evaluation against pre-agreed success criteria, run before a purchase decision, usually free. A pilot is a limited production deployment, usually after a purchase decision or a paid commitment, testing operational rollout rather than technical fit.
**In use:** "This isn't a pilot — nothing's been purchased yet — it's a 3-week POC with signed exit criteria."
**Common misuse:** using "pilot" for what is actually an unpaid pre-sale evaluation, which lets a prospect treat an open-ended production trial as free — the label determines both the commercial terms and how bounded the scope is allowed to be.

**MEDDPICC**
A discovery and qualification scaffold: Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition — eight things a deal needs answered, not eight boxes to check.
**In use:** "We're 5 of 8 on MEDDPICC — no Paper Process answer yet, so I'm not scoping the POC until we know their procurement SLA."
**Common misuse:** filling in the CRM fields with guesses to close out the form before a forecast call, rather than treating a blank field as a real gap in the deal.

**BANT**
An older qualification framework (Budget, Authority, Need, Timeline), vendor-centric and largely superseded by MEDDPICC in complex B2B sales because it asks about the buyer's constraints without mapping the internal decision process or naming a champion.
**In use:** "BANT tells us they have budget and a date; it doesn't tell us who signs or who else needs to say yes — that's the gap MEDDPICC fills."
**Common misuse:** treating a "yes" on all four BANT letters as full qualification — a deal can be BANT-qualified and still die because no economic buyer or champion was ever actually confirmed.

**Multithreading**
Maintaining relationships with more than one stakeholder inside the account, across different functions or levels, so the deal doesn't depend on a single point of contact.
**In use:** "We're single-threaded through the champion right now — I want the data engineer and the economic buyer in the next call before we scope the POC."
**Common misuse:** counting every person cc'd on an email as a "thread" — multithreading means each contact independently understands and can advocate for the deal, not that their name appears in a distribution list.

**Bake-off**
A formal, structured head-to-head technical evaluation of two or more vendors against the same criteria and, ideally, the same data set.
**In use:** "The bake-off rubric is co-written with the champion and locked before either vendor sees results — otherwise whoever wrote it wins it."
**Common misuse:** calling any competitive deal a "bake-off" even when only one vendor is actually being evaluated with real access — a bake-off implies both sides get equivalent access, timing, and data, not a courtesy demo slot after a decision is already made.

**Discovery vs. demo**
Discovery is the work of establishing the customer's actual pain, environment, and decision process through questions and data review. Demo is presenting the product against that established pain. Healthy cycles do discovery first and keep doing it throughout, not once at the start.
**In use:** "We're not ready to demo — discovery hasn't produced a number we can build success criteria around yet."
**Common misuse:** treating discovery as a single call that happens before the "real" sales process starts, rather than an ongoing check that continues to reveal new stakeholders and requirements through the POC.

**Paper process**
The specific internal steps (legal review, security questionnaire, procurement approval, signature routing) a purchase must pass through after the technical win, and how long each step typically takes at this account.
**In use:** "Technical win is done; paper process here runs security review then a 3-week procurement cycle, so close is realistically 5-6 weeks out, not next week."
**Common misuse:** treating "paper process" as a formality to mention once at the end — it should be mapped during discovery, since a technical win followed by an unmapped 8-week procurement cycle is a forecasting error, not a surprise.

**Power sponsor vs. coach**
A power sponsor is a stakeholder with the authority and political capital to protect and advance the deal internally (often the economic buyer or someone close to them). A coach is anyone inside the account willing to share information about the process, without necessarily having authority.
**In use:** "Our champion is a strong coach — she tells us everything — but she's not a power sponsor; we still need someone above her actively pushing this."
**Common misuse:** treating any helpful internal contact as equally valuable — a coach without power can describe the political landscape accurately and still be unable to move the deal through it.

**Proof of value (PoV) vs. POC**
A POC answers "does it work technically, against these criteria." A proof of value goes further, quantifying the business outcome (cost saved, revenue protected, hours reduced) the technical result implies — usually built as a value model layered on top of POC results.
**In use:** "The POC confirmed the flag-reduction number; the PoV translates that into roughly 1,300 analyst-hours/month saved, which is what goes in front of the VP."
**Common misuse:** using the terms interchangeably — a technically successful POC with no PoV attached often stalls at the economic buyer stage because nobody translated the technical result into a number that stage cares about.

**RFP vs. RFI vs. RFQ**
An RFI (request for information) gathers vendor capabilities early, often before a shortlist exists. An RFP (request for proposal) asks shortlisted vendors for a full solution and commercial proposal, typically the formal document evaluated against a scoring rubric. An RFQ (request for quote) asks for pricing only, implying the technical decision is already made.
**In use:** "This is an RFQ, not an RFP — they're not asking us to prove fit, they're asking what it costs, which means the technical decision already happened somewhere we weren't in the room."
**Common misuse:** responding to an RFQ with a full technical proposal, or to an RFI as if it were a binding commercial ask — each document implies a different stage of the buyer's process, and misreading the stage wastes response hours or looks presumptuous.

**Vaporware (in a demo context)**
Presenting a feature that is not in the current generally-available release — whether unreleased, roadmap-only, or a one-off custom build — as though a customer could rely on it today.
**In use:** "That reporting view isn't GA yet — it's committed for Q3. I'll show you the current export instead so we're not demoing vaporware."
**Common misuse:** assuming disclosure only matters for entirely fictional features — showing a real but uncommitted roadmap item without the "not yet shipped, not yet committed" caveat is the same failure mode with better production values.

**Happy ears**
The tendency for a rep or SE to interpret polite customer interest, engagement, or agreement as strong buying intent, because the alternative interpretation is unwelcome.
**In use:** "The room nodded along, but nobody could name the economic buyer afterward — that's happy ears, not a qualified deal."
**Common misuse:** used only to describe others' optimism — the same bias affects the SE reporting their own POC results, which is why signed, numeric success criteria exist: they remove the option to hear what you want to hear.

**Value engineering**
Building a quantified model that translates the product's technical result into the economic buyer's terms — cost avoided, revenue protected, hours saved — using the customer's own baseline numbers, not industry averages.
**In use:** "The value-engineering model uses their actual 51,000-flag baseline, not an industry benchmark — that's what makes the ROI number defensible in front of their CFO."
**Common misuse:** building the ROI case from generic industry statistics when the customer's own numbers were available from discovery — a model built on someone else's baseline collapses the moment the economic buyer asks "is that our number or an average?"
