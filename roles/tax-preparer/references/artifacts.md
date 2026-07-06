# Tax preparer artifacts — templates with real structure

Filled templates an agent can populate for a new engagement. Example figures follow the Maria worked example in `SKILL.md` (single, W-2 + Schedule C, tax year 2024) unless noted. Federal-only; state conformity varies and isn't covered here.

## 1. Client intake / document organizer

Checklist form, one row per document type, with a status column so gaps are visible before the return is started, not discovered mid-preparation.

| Document | Applies? | Received | Notes |
|---|---|---|---|
| W-2(s) | Yes | ✅ | 1 employer, $52,000 wages, $4,100 fed withholding |
| 1099-NEC / 1099-K (self-employment) | Yes | ✅ | $61,000 gross receipts, 1 platform |
| 1099-INT / 1099-DIV | No | — | No bank/brokerage interest reported this client |
| 1099-B (brokerage) | No | — | — |
| 1098 (mortgage interest) | No | — | Renter |
| 1098-T (tuition) | No | — | — |
| 1095-A (marketplace health coverage) | Yes | ⬜ pending | Needed to reconcile premium tax credit against SE health insurance deduction |
| Prior-year return | Yes | ✅ | Used for carryovers, comparison, safe-harbor % |
| Business mileage log | Yes | ✅ | 1,200 business miles logged |
| Home office measurements | Yes | ✅ | 300 sq ft, simplified method elected |
| Estimated payments made this year | Yes | ✅ | $0 — flagged for 2210 calculation |
| IRS transcript pulled (Wage & Income) | — | ⬜ | Pull if any 1099 suspected missing |

**Rule:** don't start the return with a "pending" row on anything income-related — the 1095-A gap above must close before filing, since it affects both the SE health insurance deduction and any premium tax credit reconciliation on Form 8962.

## 2. Schedule C reconciliation worksheet (naive vs. corrected)

| Line | Client's naive figure | Preparer-corrected figure | Source / basis |
|---|---|---|---|
| Gross receipts | $61,000 | $61,000 | 1099-K + bank deposit reconciliation |
| Software/equipment | $9,200 | $9,200 | Receipts provided |
| Home office (simplified, 300 sq ft × $5) | $0 | $1,500 | Measured space, exclusive business use confirmed |
| Vehicle (1,200 mi × $0.67, 2024 rate) | $0 | $804 | Mileage log |
| **Total expenses** | **$9,200** | **$11,504** | |
| **Net profit** | **$51,800** | **$49,496** | |

**Rule:** never accept a client's own expense total without asking what's missing — home office and mileage are the two most commonly self-omitted categories because clients don't realize they qualify.

## 3. Due-diligence documentation (Form 8867 support file)

Not the form itself — the backup that has to exist *behind* it. One block per benefit claimed.

**If EITC/CTC/ODC claimed (dependent-related):**
- Relationship test: documented how (birth certificate, custody order, school records)?
- Residency test: majority-of-year address confirmed how (school enrollment, medical records)?
- Support test: who provided >50% of support — confirmed how?
- Knowledge test: anything in the interview that contradicts the claimed facts, and how was it resolved?

**If AOTC claimed:**
- 1098-T received and reconciled to actual qualified expenses paid (not just the box amount)?
- First 4 years of postsecondary education confirmed — prior-year returns checked for prior AOTC claims (4-claim lifetime limit)?

**If HOH claimed:**
- Unmarried or considered unmarried (lived apart from spouse last 6 months) confirmed how?
- Paid >50% of household costs — confirmed with what records (rent/mortgage, utilities, food)?
- Qualifying person lived with taxpayer >half the year — confirmed how?

**Rule:** if any block above has an unanswered line, the position doesn't get claimed this filing — "we'll fix it later" is how a $635-per-benefit penalty (2024) happens.

## 4. Client summary letter (balance-due version)

```
Subject: Your 2024 federal return — summary before filing

[Client name],

Bottom line: your 2024 federal return shows a balance due of $15,238
(after $4,100 already withheld from your paycheck).

Why it's a balance due and not a refund:
- Self-employment tax on your freelance income: $6,993. This isn't
  withheld anywhere during the year — it's calculated once, at filing,
  on your net Schedule C profit.
- I found $2,304 in deductions you hadn't claimed (home office, mileage)
  and $8,296 in deductions that reduce your taxable income regardless of
  whether you itemize (half your self-employment tax, your health
  insurance premiums). Combined, these lowered what you owe by roughly
  $3,300 versus your own estimate.
- The remaining gap is simply that no tax was withheld on your freelance
  income during the year.

What changes for 2025:
- I'm setting you up with quarterly estimated payments of approximately
  $3,600 (Form 1040-ES; due 4/15, 6/15, 9/15, 1/15) so next April isn't
  a repeat surprise.
- Please request a 1095-A reconciliation from your marketplace insurer
  before we file — it affects both your health insurance deduction and
  any premium tax credit adjustment.

Payment options for the $15,238 balance: full payment by 4/15, or an
IRS payment plan (Form 9465) if a lump sum isn't workable — happy to
walk through either.
```

## 5. Estimated tax payment schedule (Form 1040-ES basis)

| Quarter | Due date | Suggested payment | Basis |
|---|---|---|---|
| Q1 | 4/15 | $900 | 25% of $3,600 target, sized to prior-year safe harbor (110% of last year's $19,338 liability spread over 4 payments, less anticipated withholding) |
| Q2 | 6/15 | $900 | Same |
| Q3 | 9/15 | $900 | Same |
| Q4 | 1/15 (following year) | $900 | Same; adjust in Q3 if freelance income is tracking materially above or below plan |

**Rule:** recompute after Q2 actuals are in — a flat quarterly number set in April and never revisited is how a client ends up underpaid again despite "making estimated payments."

## 6. IRS notice response letter (CP2000 example)

```
Re: CP2000 Notice dated [date] — Tax Year 2024 — [Name/SSN last 4]

We received the CP2000 proposing additional tax of $[X] based on a
1099-B reported by [broker] that the notice states was not included
on the return.

This item was in fact reported: see Schedule D, Form 8949 Part II,
line [X], which reports the sale with basis of $[Y], resulting in the
gain already included in the return's total taxable income. Enclosed:
copy of Schedule D/8949 as filed, and the broker's 1099-B/cost-basis
statement showing the same transaction.

We respectfully request the proposed adjustment be withdrawn. Please
contact us at [phone] with any questions.

[Preparer name, PTIN, POA authorization reference if Form 2848 is on file]
```

**Rule:** always attach the specific line/form reference where the IRS's own notice already exists in the return — a bare denial without a pointer to the offsetting entry gets a form-letter rejection back.
