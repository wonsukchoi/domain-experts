### A function makes an external call before updating its own internal state
- **Usually means:** A reentrancy vulnerability — an attacker can recursively re-enter the function before the state update takes effect, potentially draining funds multiple times.
- **First question:** Does this function update all relevant internal state before making any external call, per checks-effects-interactions?
- **Data to pull:** The function's code, specifically the ordering of state updates relative to external calls.

### A privileged/administrative function's access control is tested only for the authorized-caller path
- **Usually means:** Whether unauthorized callers are actually rejected hasn't been confirmed, which is the test that actually matters for this class of vulnerability.
- **First question:** Is there a test confirming an unauthorized address cannot successfully call this function?
- **Data to pull:** Test suite for this function, specifically tests targeting unauthorized-caller rejection.

### A contract reads price data from a single source, especially a low-liquidity one
- **Usually means:** The price feed may be manipulable within a single transaction (commonly via a flash loan), which is a well-documented DeFi exploit pattern.
- **First question:** Is this price sourced from a single spot reading, or from a manipulation-resistant design (TWAP, multiple aggregated sources)?
- **Data to pull:** Oracle/price-feed source and methodology, liquidity depth of the underlying source if a DEX pool.

### A contract is being prepared for mainnet deployment with no explicit decision on upgradability
- **Usually means:** If a bug is later found, there may be no mechanism to fix it, since immutable deployed code generally can't be changed after the fact.
- **First question:** Has a deliberate decision been made about whether this contract needs an upgrade mechanism (proxy pattern) before deployment?
- **Data to pull:** Contract architecture documentation, stated upgradability decision (or its absence).

### A contract design includes storage writes inside a loop with an unbounded or large iteration count
- **Usually means:** This could produce prohibitively high gas costs or cause the transaction to run out of gas and fail entirely at realistic scale.
- **First question:** What is the expected maximum iteration count for this loop, and has gas cost been estimated at that scale?
- **Data to pull:** Loop's expected iteration range, gas cost estimate at maximum expected scale.

### A contract handling significant value is being deployed to mainnet without an independent security audit
- **Usually means:** Vulnerabilities that internal testing missed (reentrancy, access control, oracle manipulation, and others) may go undetected until exploited in production.
- **First question:** Has this contract undergone an independent third-party security audit, and were its findings addressed before deployment?
- **Data to pull:** Audit report (or its absence), value/assets the contract is expected to hold.

### A reentrancy fix reorders state updates but doesn't add a reentrancy guard as defense in depth
- **Usually means:** The primary fix may be correct, but relying on ordering alone without a second layer of protection leaves less margin for error if another code path introduces the same pattern later.
- **First question:** Has a reentrancy guard modifier been added in addition to the checks-effects-interactions reordering?
- **Data to pull:** Current function implementation, presence or absence of a reentrancy guard.

### A contract's test suite only covers the happy path with no fuzzing or adversarial test scenarios
- **Usually means:** Edge cases and adversarial inputs (the kind attackers actually use) may not have been tested, despite the contract passing all its existing tests.
- **First question:** Has this contract been tested with fuzzing or property-based testing targeting adversarial inputs, not just expected-use test cases?
- **Data to pull:** Test suite composition, presence of fuzzing/property-based test coverage.
