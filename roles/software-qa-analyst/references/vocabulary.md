### Boundary value analysis
A test design technique focused on the edges of a valid input range (minimum, maximum, and values just inside/outside those boundaries), since off-by-one and comparison-operator bugs concentrate there.
**In use:** "Boundary value analysis on the $50-$500 discount range caught a bug the mid-range test completely missed."
**Common misuse:** Testing only comfortable, typical values from the middle of a range, leaving boundary conditions — where bugs actually concentrate — unchecked.

### Equivalence partitioning
A test design technique that divides an input space into partitions expected to be handled the same way, then tests one representative value per partition rather than exhaustively testing every possible input.
**In use:** "We partitioned valid, too-low, and too-high order totals, then picked a representative test value from each partition."
**Common misuse:** Testing many values within the same equivalence partition (redundant coverage) while missing a partition entirely (a real gap), rather than deliberately covering each distinct partition.

### Test pyramid
A model for structuring an automated test suite with a broad base of fast unit tests, a moderate layer of integration tests, and a small top layer of slower, more expensive end-to-end tests.
**In use:** "Our test suite has grown into an inverted pyramid — mostly E2E tests and very few unit tests — that's why failures take so long to diagnose."
**Common misuse:** Letting a test suite grow organically into an "ice cream cone" shape (mostly E2E, few unit tests) without periodically checking and correcting its structure against the pyramid model.

### Code coverage (line / branch)
A metric measuring what percentage of a codebase's lines (or logical branches) executed during a test run — line coverage counts executed lines; branch coverage additionally checks whether each conditional path was exercised.
**In use:** "Line coverage was 100%, but branch coverage revealed the boundary condition was never actually tested."
**Common misuse:** Treating a high line coverage percentage as proof of thorough testing, when it only confirms code executed, not that its logic branches or edge cases were meaningfully checked.

### Flaky test
A test that produces inconsistent pass/fail results when run against the same, unchanged code, typically due to timing issues, shared state, or environmental dependencies.
**In use:** "This test failed twice this week with no code changes — it needs to be triaged, not just re-run."
**Common misuse:** Repeatedly re-running a flaky test until it passes without investigating the root cause, which can mask a real intermittent bug and erode trust in the test suite's overall signal.

### Regression suite
The set of automated tests run to confirm that previously working functionality (including previously fixed bugs) hasn't broken due to new changes.
**In use:** "We added the boundary value test cases to the regression suite so this specific bug can't silently reappear."
**Common misuse:** Fixing a bug without adding a corresponding regression test for the specific condition that exposed it, leaving the codebase vulnerable to the same bug recurring undetected.

### Risk-based testing
An approach to allocating test effort based on the probability and impact of failure for each functional area, concentrating depth where a defect would matter most.
**In use:** "Payment processing gets our deepest test coverage; the rarely used settings page gets lighter coverage, based on risk."
**Common misuse:** Spreading test effort evenly across all features regardless of business risk, under-investing in high-impact areas and over-investing in low-risk ones.

### Bug severity
A classification of a defect's technical impact — how badly it breaks the system (crash, data loss, incorrect calculation) — independent of how often it occurs or how much business impact it has.
**In use:** "Severity here is Medium — it's a financial calculation error, not a crash or data loss."
**Common misuse:** Conflating severity with priority, treating them as a single combined rating rather than two independent dimensions.

### Bug priority
A classification of how urgently a defect needs to be fixed, based on business impact — frequency of occurrence, revenue exposure, customer-trust impact — independent of its technical severity.
**In use:** "Priority is High even though severity is Medium — this bug affects a very common order value and will occur frequently."
**Common misuse:** Assuming a low-severity bug is automatically low priority, missing cases where frequent occurrence or high business exposure make it urgent despite modest technical impact.

### Ice cream cone (anti-pattern)
An inverted test pyramid shape — dominated by slow, expensive end-to-end tests with a thin base of unit tests — that produces slow, flaky, and hard-to-diagnose test suites.
**In use:** "This suite is an ice cream cone — mostly E2E tests — which is why a single failure takes hours to root-cause."
**Common misuse:** Allowing a test suite's shape to drift toward this anti-pattern without periodic review, since it tends to happen gradually as E2E tests accumulate faster than unit tests during a project's growth.
