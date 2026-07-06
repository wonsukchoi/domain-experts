# Blockchain Engineer — Playbook

## Reentrancy exploit impact calculation (filled example)

| Component | Value |
|---|---|
| Attacker's legitimate deposit | $10,000 |
| Recursive calls before gas exhaustion (illustrative bound) | ~20 |
| **Total drained** (20 × $10,000) | **$200,000** |
| Amplification factor | 20x the attacker's actual deposit |
| Contract's total holdings | $500,000 |
| **Percentage of contract drained** | $200,000 ÷ $500,000 = **40%** |

**Use:** This kind of calculation illustrates why reentrancy is treated as a critical-severity finding — the amplification factor means a modest legitimate position can be leveraged into a large-scale drain within a single transaction.

## Checks-effects-interactions audit checklist (per function)

1. List every external call the function makes (transfers, calls to other contracts).
2. For each external call, identify what internal state changes are related to it (balances, flags, counters).
3. Confirm all related internal state changes happen **before** the external call, not after.
4. If any external call precedes a related state update, flag as a reentrancy risk requiring reordering.
5. Add a reentrancy guard modifier as a second layer of defense, especially for functions handling value transfers.

## Access control test checklist (per privileged function)

1. Identify every function restricted to a specific role (owner, admin, specific address).
2. Write a test confirming the authorized role can successfully call the function.
3. **Write a separate test confirming an unauthorized caller is rejected** — this is the test that actually validates the access control, not the authorized-path test alone.
4. Repeat for every privileged function in the contract, not just the most obviously sensitive ones.

## Oracle design comparison table

| Design | Manipulation resistance | Notes |
|---|---|---|
| Single spot price from one DEX pool | Low | Vulnerable to single-transaction (flash loan) manipulation, especially on low-liquidity pools |
| Time-weighted average price (TWAP) over a defined window | Moderate-High | Manipulation would need to be sustained across the entire window, raising cost significantly |
| Multiple aggregated sources (median/weighted average across independent feeds) | High | A single compromised or manipulated source has limited effect on the aggregate |

**Use:** Any contract making a financial decision (liquidation, collateral valuation, swap pricing) based on price data should use a TWAP or multi-source design, never a single spot-price read, given how well-documented and repeatable the single-source manipulation attack pattern is.

## Pre-mainnet deployment checklist

1. Has the upgradability decision (immutable vs. proxy pattern) been made deliberately, not by default?
2. Has every function with an external call been checked against checks-effects-interactions?
3. Has every privileged function's access control been tested for unauthorized-caller rejection?
4. Has any price/external data dependency been designed with a manipulation-resistant oracle?
5. Has gas cost been estimated for all loops/storage-heavy operations at realistic maximum scale?
6. Has the contract undergone an independent security audit if it will handle significant value?

## Security findings memo — filled example

> **Smart Contract Security Finding — Staking Withdrawal Function**
> Vulnerability: Reentrancy — external ETH transfer occurs before internal balance is zeroed, allowing recursive re-entry.
> Exploit impact estimate: An attacker with a $10,000 legitimate balance could drain approximately $200,000 (20x amplification via ~20 recursive calls), representing 40% of the contract's total $500,000 holdings.
> **Fix applied: Reordered to checks-effects-interactions (balance zeroed before external call), plus a reentrancy guard modifier as defense in depth.**
> **Recommendation: Re-audit all other functions in this contract making external calls for the same pattern before mainnet deployment.**
