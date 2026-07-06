### An input-range function's test suite only tests typical mid-range values
- **Usually means:** Boundary conditions (off-by-one, comparison-operator bugs at exact min/max values) are likely untested regardless of how high the reported coverage is.
- **First question:** Have the exact boundary values (min, min-1, min+1, max, max-1, max+1) been explicitly tested?
- **Data to pull:** Current test cases for this function, the valid input range's exact boundaries.

### A test suite reports high code coverage but has few boundary/edge-case-specific test assertions
- **Usually means:** Coverage may reflect that code executed, not that its actual logic branches and edge cases were meaningfully checked.
- **First question:** Do the existing tests specifically assert on boundary and edge-case behavior, or just confirm the code runs without error on typical inputs?
- **Data to pull:** Test case list for the covered code, specific assertions made in each test.

### An automated test suite is dominated by end-to-end tests with relatively few unit tests
- **Usually means:** This is an inverted "ice cream cone" shape, likely producing slow, flaky, hard-to-diagnose failures compared to a properly shaped pyramid.
- **First question:** What is the current ratio of unit to integration to E2E tests, and does it favor a broad unit-test base?
- **Data to pull:** Test suite composition by test type/layer.

### A flaky test is being re-run until it passes rather than triaged
- **Usually means:** A real intermittent bug could be hiding behind the "just flaky" label, and repeated re-running erodes trust in the suite's overall signal.
- **First question:** Has this test been root-caused, or is it being dismissed and re-run without investigation?
- **Data to pull:** Flaky test's failure history and any investigation notes (or their absence).

### Test effort appears evenly distributed across all features regardless of business risk
- **Usually means:** High-risk areas (e.g., payment processing) may be under-tested relative to their actual failure impact, while low-risk areas receive disproportionate test depth.
- **First question:** Has test effort been explicitly weighted by risk (probability × impact of failure) for each functional area?
- **Data to pull:** Test case count/depth by functional area, business risk assessment for each area.

### A bug's severity and priority are reported as a single combined rating
- **Usually means:** Conflating technical impact (severity) with business impact (priority) can misrank issues — a low-severity but high-priority bug (e.g., a cosmetic issue on a high-traffic page) might get deprioritized incorrectly.
- **First question:** Has this bug been classified on both severity and priority dimensions separately?
- **Data to pull:** Bug's technical impact (crash/data loss vs. cosmetic) and business impact (frequency, revenue/trust exposure).

### A regression suite doesn't include the specific boundary values that previously caused a bug
- **Usually means:** The same class of bug could recur undetected if the fix isn't backed by a regression test targeting the exact boundary condition that exposed it.
- **First question:** Were the specific boundary values that revealed this bug added to the regression suite after the fix?
- **Data to pull:** Regression suite contents for the fixed function, the original bug's specific triggering input.

### A test suite's coverage number is reported without any context on what type of coverage (line, branch, or otherwise) it measures
- **Usually means:** Line coverage and branch coverage can tell very different stories about the same code, and reporting just a number without specifying which type can overstate confidence.
- **First question:** Is this a line coverage or branch coverage figure, and does the reported percentage account for untested logical branches even within "covered" lines?
- **Data to pull:** Coverage tool's specific metric type and methodology.
