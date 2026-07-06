# Software QA Analyst/Tester — Playbook

## Boundary value test matrix (filled example — discount code validation)

| Test value | Expected result | Actual result (before fix) | Bug found? |
|---|---|---|---|
| $49.99 (below min) | No discount | No discount | No |
| **$50.00 (exact min)** | **Discount applies** | **No discount** | **Yes — boundary bug** |
| $50.01 (above min) | Discount applies | Discount applies | No |
| $499.99 (below max) | Discount applies | Discount applies | No |
| $500.00 (exact max) | Discount applies | Discount applies | No |
| $500.01 (above max) | No discount | No discount | No |

**Use:** Always test the exact boundary value alongside the values just inside and outside it — the mid-range test alone would never surface this comparison-operator bug, no matter how much line coverage it achieves.

## Coverage-vs-quality distinction (filled example)

| Metric | Naive mid-range test only | Full boundary suite |
|---|---|---|
| Line coverage | 100% | 100% |
| Boundary bug detected? | **No** | **Yes** |

**Use:** Never treat 100% line coverage as evidence a function is well-tested — this example shows identical line coverage with a completely different bug-detection outcome, because line coverage doesn't measure whether the right values were tested.

## Test pyramid ratio check (illustrative structure)

| Layer | Healthy proportion (illustrative) | Current suite | Assessment |
|---|---|---|---|
| Unit tests | ~70% of total tests | 20% | Undersized — likely contributing to slow, hard-to-diagnose failures |
| Integration tests | ~20% | 25% | Roughly appropriate |
| End-to-end tests | ~10% | 55% | Oversized — "ice cream cone" pattern |

**Use:** Periodically audit the suite's actual composition against this shape — a suite that's grown organically tends to accumulate E2E tests faster than unit tests, drifting toward the unhealthy inverted pattern.

## Bug severity/priority classification matrix

| | Low business impact | High business impact |
|---|---|---|
| **Low technical severity** | Low priority | Medium-High priority (e.g., cosmetic bug on high-traffic page) |
| **High technical severity** | Medium priority (e.g., crash in rarely used feature) | Highest priority |

**Use:** Classify each bug on both axes independently before assigning a fix priority — a low-severity bug in a high-traffic, frequently occurring scenario (like the $50.00 discount example) can outrank a high-severity bug in a rarely used feature.

## Flaky test triage checklist

1. Confirm the test genuinely fails inconsistently on unchanged code (not a real, newly introduced bug).
2. Check for common flaky-test causes: timing/race conditions, shared test state, external dependency instability, non-deterministic ordering.
3. If root cause is identified, fix it directly.
4. If root cause isn't immediately clear, quarantine the test (mark it as skipped/known-flaky) with a tracked ticket for follow-up investigation — never leave it silently re-run-until-green in the regular suite.

## QA findings memo — filled example

> **Bug Report — Discount Code Boundary Logic**
> Bug: Orders totaling exactly $50.00 incorrectly fail to receive the discount, due to a strict `>` comparison instead of `>=`. Found via boundary value analysis — invisible to the existing mid-range test case despite that test achieving 100% line coverage.
> Severity: Medium (financial impact, no crash/data loss). Priority: High ($50.00 is a common order value, frequent occurrence expected).
> **Fix: Corrected comparison to `>=`. Added full boundary test suite (49.99, 50.00, 50.01, 499.99, 500.00, 500.01) to regression suite to prevent recurrence.**
> **Note: 100% line coverage on the original test suite did not indicate this bug was absent — coverage measured what code ran, not whether the boundary logic was correctly tested.**
