# Playbook

Filled templates a floor associate or manager runs directly, not descriptions of them.

## 1. Peak-hour floor coverage template

Built from the traffic-by-hour report, not a flat schedule. Example week for a specialty apparel store averaging 1,180–1,200 weekly visits:

| Hour block | Share of daily traffic | Associates scheduled | Register(s) open | Fitting room target queue |
|---|---|---|---|---|
| Open–11am | 8% | 1 | 1 | n/a |
| 11am–2pm | 22% | 2 | 1 | ≤3 min |
| 2pm–5pm | 25% | 2 | 1–2 (if >20% conv. target) | ≤3 min |
| **5pm–7pm** | **32%** | **3** | **2** | **≤3 min** |
| 7pm–close | 13% | 1–2 | 1 | ≤3 min |

**Rule:** the two highest-traffic blocks get the most experienced pairing, never two same-week new hires alone — a new hire paired with a tenured associate during peak closes at roughly the tenured associate's rate; two new hires alone during peak typically run 4–6 points below team average conversion until week 3–4 of ramp.

## 2. Add-on / cross-sell pairing list (filled example, apparel)

Primary item → suggested add-on, priced under ~30% of primary, with the trigger line:

| Primary item purchased | Add-on suggestion | Add-on price vs. primary | Trigger line (say in fitting room or at shelf, not register) |
|---|---|---|---|
| Wool coat ($220) | Cashmere-blend scarf ($58) | 26% | "That coat runs a little open at the collar — this scarf's the exact weight for it, want me to grab your size?" |
| Jeans ($88) | No-show socks 3-pack ($16) | 18% | "These run slim through the ankle — I'd pair them with a no-show sock, saves you the sock-line showing." |
| Dress shoes ($140) | Shoe trees ($24) | 17% | "Since these are full-grain leather, a shoe tree after each wear roughly doubles the life of the shape." |
| Interview blazer ($180) | Pocket square ($22) | 12% | "This one's got a nicer break with a pocket square — want to see it with one before you decide?" |

**Rule:** deliver the trigger line while the customer still has the primary item in hand (fitting room, shelf) — the same line said at the register after the customer has already committed to a total converts at roughly a third of the fitting-room rate.

## 3. Greeting → trial-close script skeleton (Friedman's steps, adapted, not recited)

```
1. OPEN (non-transactional): comment on the specific product in the
   customer's hand or that they're near — never "can I help you?"
   e.g. "That jacket's actually one of our warmest — is it for
   somewhere cold, or more everyday?"

2. INVESTIGATE (2-3 questions max): occasion, must-haves, budget
   signal — listen for the budget signal, don't ask for it directly.

3. PRESENT: show the item that answers what was just said, lead with
   the benefit ("this'll keep you warm down to about 20°F"), feature
   second ("it's a 700-fill down").

4. TRIAL CLOSE: a low-commitment yes/no that tests readiness —
   "want to try it on?" not "so, what do you think?" (too open,
   invites stalling).

5. HANDLE the objection that actually surfaces (price, fit, "let me
   think about it") — don't pre-empt objections that weren't raised,
   it plants doubt that wasn't there.

6. ADD-ON: from the pairing list, while the primary item is still in
   hand (Section 2).

7. CLOSE: assume the sale in the phrasing — "I'll get this rung up
   for you" not "did you want to buy this?"
```

## 4. No-receipt / return decision tree

```
Item has current-season tag attached, condition sellable?
├── NO (worn, damaged, tag removed) → decline exchange/refund,
│     offer repair/damage-policy path if one exists.
└── YES
     ├── Receipt or card-lookup match found?
     │    ├── YES → refund to original tender at ticketed price.
     │    └── NO → continue.
     └── No receipt, no card match:
          ├── Single occurrence, low dollar (<$75), first return
          │    from this customer on file → store credit at
          │    lowest verified recent selling price (not ticket
          │    price) — closes the price-arbitrage gap without
          │    penalizing a legitimate return.
          ├── Repeat no-receipt returns from same customer (3+ in
          │    90 days) or same SKU pattern across customers →
          │    escalate to manager before completing; check
          │    exception report for a wardrobing pattern
          │    (Section red-flags.md #3).
          └── Item value >$75 with no receipt → manager override
               required regardless of history.
```

## 5. Loss-prevention exception report — reading it (filled example)

Weekly register exception summary, 4 associates, one register each:

| Associate | Transactions | Voids | Void rate | No-sales (drawer open, no sale) | Discount overrides | Override rate |
|---|---|---|---|---|---|---|
| A | 210 | 3 | 1.4% | 1 | 5 | 2.4% |
| B | 198 | 4 | 2.0% | 2 | 6 | 3.0% |
| C | 205 | 14 | **6.8%** | 9 | 22 | **10.7%** |
| D | 190 | 5 | 2.6% | 3 | 7 | 3.7% |

**Reading it:** store average void rate ~2.0%, average override rate ~3.0%. Associate C sits at 3–4x both, with a no-sale count nearly matching void count — a pattern consistent with drawer-open cover for an unrung item ("sweethearting") rather than normal price-check voids, which don't correlate with no-sales. **Next step:** pull time-stamped transaction detail for Associate C's void and no-sale events against camera coverage for that register before any conversation — data first, conversation second.
