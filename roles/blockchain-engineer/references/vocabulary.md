### Reentrancy
A vulnerability where a contract makes an external call before updating its own internal state, allowing an attacker's contract to recursively re-enter the function and repeat an action (like a withdrawal) multiple times before the state update takes effect.
**In use:** "The withdrawal function is vulnerable to reentrancy because it sends funds before zeroing the user's balance."
**Common misuse:** Assuming a single fix (like adding a reentrancy guard) is sufficient without also checking that state updates happen before external calls throughout the contract.

### Checks-effects-interactions pattern
The standard smart contract design pattern: first check conditions (requirements/validations), then apply effects (update internal state), and only then perform interactions (external calls) — this ordering is the primary defense against reentrancy.
**In use:** "We reordered the function to follow checks-effects-interactions — balance is zeroed before the external transfer, not after."
**Common misuse:** Writing a function that performs an external call before its internal state update, violating this pattern and creating a reentrancy opening.

### Reentrancy guard
A modifier (typically a lock/mutex flag) that prevents a function from being re-entered while it's still executing, used as a defense-in-depth layer alongside checks-effects-interactions.
**In use:** "The reentrancy guard modifier blocks any nested call to this function during its execution, even if the ordering fix were somehow bypassed."
**Common misuse:** Relying on a reentrancy guard alone without also applying checks-effects-interactions ordering, or vice versa, rather than using both as complementary layers of defense.

### Gas
The unit measuring computational cost on a blockchain like Ethereum, charged per operation, with storage writes costing significantly more than reads or in-memory computation.
**In use:** "This loop's gas cost scales with the number of users, and could exceed the block gas limit at realistic scale."
**Common misuse:** Designing contract logic without accounting for gas cost, leading to expensive or outright failing (out-of-gas) transactions once usage scales beyond a small test case.

### Access control (smart contract)
The mechanism restricting who can call a specific function, typically enforced via an explicit modifier checking the caller's address or role.
**In use:** "The mint function needs an owner-only access control modifier, and a test confirming non-owner callers are rejected."
**Common misuse:** Implementing an access control check but only testing that the authorized caller succeeds, without confirming unauthorized callers are actually rejected.

### Oracle (blockchain)
A mechanism that brings external, off-chain data (commonly price data) onto the blockchain for a smart contract to use.
**In use:** "This contract's oracle uses a time-weighted average price across multiple sources to resist manipulation."
**Common misuse:** Using a single spot-price reading from one low-liquidity source as an oracle, which can be manipulated within a single transaction.

### Time-weighted average price (TWAP)
An oracle design that averages a price over a defined time window rather than reading an instantaneous spot price, making manipulation significantly more expensive since it would need to be sustained across the entire window.
**In use:** "Switching to a TWAP oracle over a 30-minute window makes a single-transaction price manipulation attack impractical."
**Common misuse:** Assuming any averaging mechanism is sufficient without checking the time window is long enough to actually resist realistic manipulation attempts.

### Flash loan
An uncollateralized loan that must be borrowed and repaid within a single blockchain transaction, commonly used (legitimately or maliciously) to temporarily acquire large capital for arbitrage or, in exploit scenarios, to manipulate a price feed.
**In use:** "The attacker used a flash loan to temporarily manipulate the pool's spot price and trigger an undercollateralized liquidation."
**Common misuse:** Assuming a large capital requirement makes an attack impractical, when a flash loan can provide that capital temporarily within a single transaction at minimal cost.

### Proxy pattern (upgradability)
A smart contract architecture where a lightweight proxy contract delegates calls to a separate, replaceable logic contract, allowing the underlying logic to be upgraded while preserving the proxy's address and stored state.
**In use:** "We deployed this contract behind a proxy so we can fix bugs in the logic contract without migrating user balances."
**Common misuse:** Deciding to add upgradability after a contract is already deployed as immutable, when the proxy architecture generally has to be designed in from the start.

### Smart contract audit
An independent, expert security review of a smart contract's code before deployment, checking for known vulnerability classes (reentrancy, access control gaps, oracle manipulation, and others).
**In use:** "This contract handles significant user funds, so it needs an independent audit before mainnet launch, not just internal review."
**Common misuse:** Treating an audit as optional or reserved only for the largest projects, when any contract handling meaningful value carries real risk from undetected vulnerabilities.
