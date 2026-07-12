# Playbook

Filled workflows a counter person actually runs, with real structure and plausible numbers. Adapt the numbers to your catalog and pricing matrix — the structure and sequence are the reusable part.

## 1. VIN / build-option decode workflow

Run before quoting anything application-sensitive (brakes, steering, ABS, airbag, drivetrain, electrical). Skip only for genuinely universal parts.

**Steps, filled example (2015 Chevrolet Silverado 1500, front brakes):**

1. **Get the 17-digit VIN.** Decline to quote a safety-critical part on year/make/model alone once a VIN is available — offer to look it up from the door jamb or registration if the caller doesn't have it memorized.
2. **Decode to base application.** VIN decode returns: 2015 Silverado 1500, 5.3L V8, 2WD, standard suspension — base front rotor 12.6", part# RB-12630.
3. **Check for option-package overrides.** Cross-check the VIN-linked build data or ask for the RPO code sticker (GM: glovebox) for trailering/handling package codes (e.g., Z82/JHD-class packages) that upsize brakes independent of trim badge. Found: trailering package present → rotor upsizes to 13.6", part# RB-13660, requires bracket kit BK-1366.
4. **Re-run the catalog search against the corrected application**, not the base one. Quote only the corrected line.
5. **Note the override on the ticket** ("VIN-confirmed trailering pkg — 13.6\" rotor, not base 12.6\"") so the next counter person doesn't re-quote base on a repeat visit.

**Rule:** any part category with more than one fitment inside a single year/make/model (brakes, engine-dependent sensors, 2WD/4WD-dependent driveline parts) gets step 3. Universal parts (wiper blades, bulk filters by spec, shop supplies) skip straight to price.

## 2. Supersession chase

Never quote or promise stock on a part number flagged superseded without walking the full chain.

**Filled example:**

```
Customer part# requested: WP-4410
Catalog flag: SUPERSEDED → WP-4410R
  WP-4410R flag: SUPERSEDED → WP-4410R2
    WP-4410R2 flag: ACTIVE — current price $38.25, 6 in stock local, 40 at DC
Quote: WP-4410R2, $38.25, in stock. Do NOT quote WP-4410 or WP-4410R pricing —
both are stale; WP-4410R2 may differ in gasket material or bolt pattern from
the original request even though it's the "same" water pump.
```

**Rule:** stop only at a number with no further supersession flag. If the chain changes anything customer-visible (bolt pattern, connector, included hardware), say so — don't assume "same part, new number."

## 3. Commercial account matrix pricing (filled example)

Commercial accounts buy off a cost-plus matrix tied to account tier, not retail list. A typical three-tier structure:

| Account tier | Basis | Markup over cost | Example: $60-cost caliper |
|---|---|---|---|
| Tier A (high volume, net-15, low comeback rate) | Cost | +18% | $70.80 |
| Tier B (standard commercial, net-30) | Cost | +28% | $76.80 |
| Tier C (new/low-volume/slow-pay history) | Cost | +40%, or COD only | $84.00 |
| Retail walk-in | List | — | $109.00 |

**Tier movement triggers (review quarterly, not ad hoc):**
- Move Tier B → Tier A after 2 consecutive quarters of on-time payment and monthly volume above the tier's stated threshold.
- Move any tier → COD immediately on a payment default over 45 days past terms, regardless of tenure.
- A comeback rate on sold parts above roughly 3% of line items in a quarter is a conversation with the account before a tier change, not an automatic demotion — check whether the comebacks are parts-caused or install-caused first.

## 4. Will-call vs. delivery vs. DC transfer

| Situation | Default routing | Why |
|---|---|---|
| Tech waiting at the lift, part in local stock | Will-call, counter pickup | Delivery round-trip (driver + tech idle time) costs more than the trip saves. |
| Tech mid-job, part in local stock, not urgent | Delivery on next scheduled run | Batches with other stops; no added driver cost. |
| Part not in local stock, in stock at DC | DC transfer, quote real ETA (same-day cutoff vs. next-day) | Never promise "in stock" language for a DC part — say "transferring, ETA X." |
| Part not in stock anywhere in network | Special order, vendor lead time quoted, deposit taken on non-returnable items | Set expectations before the shop commits the vehicle's bay time to the job. |

## 5. Line review structure (with vendor rep, quarterly)

1. **Pull sell-through and comeback data by SKU** for the quarter — not gut feel. Flag anything with sell-through under ~2 units/month tying up shelf space, and anything with a comeback rate meaningfully above the category average.
2. **Reset stocking levels** on the fast movers first (min/max quantities), then decide on slow movers: keep at reduced quantity, special-order-only, or discontinue local stock.
3. **Renegotiate matrix cost on volume categories** — a vendor rep expects this at every review; walking in without the sell-through numbers means negotiating from a weaker position than the data supports.
4. **Document any fitment or quality issues surfaced by comeback data** and route them to the vendor rep by SKU, with counts — "brake pads squealing" without a SKU and count doesn't get fixed upstream.
