# Frontend Engineer — Playbook

## Core Web Vitals before/after comparison (filled example)

| Metric | Baseline | After blanket lazy-load (regression) | After correct fix |
|---|---|---|---|
| LCP | 3.8s (poor) | 4.6s (poor, worse) | **2.1s (good)** |
| INP | — | — | 180ms (good, threshold <200ms) |
| CLS | — | — | 0.05 (good, threshold <0.1) |

**Use:** Always measure all three vitals together — a fix targeted at LCP could theoretically affect INP or CLS too, and confirming they remain good is part of validating the fix, not an afterthought.

## LCP root-cause diagnosis checklist

1. Identify the page's current LCP element (often a hero image, video, or large text block).
2. Check whether that specific element is render-blocked, lazy-loaded, or otherwise delayed.
3. If lazy-loaded, remove lazy-loading from this element specifically and consider `fetchpriority="high"`.
4. Re-measure LCP to confirm the fix, then check INP and CLS haven't regressed as a side effect.

## Layout thrashing audit pattern

**Anti-pattern (interleaved read/write):**
> For each element: write a style change, then immediately read `offsetHeight` — forces a synchronous layout recalculation on every iteration.

**Fix (batched read/write):**
> First loop: read all needed layout properties (`offsetHeight`, etc.) into variables for every element.
> Second loop: apply all style writes using the previously read values.
> Result: only one layout recalculation instead of one per element.

**Use:** Any interaction code that reads a layout property right after writing a DOM change is a candidate for this batching fix — the more elements involved, the more the thrashing cost compounds.

## Bundle size reduction checklist

1. Run a bundle analyzer to identify the largest contributors to the current bundle size.
2. For each large dependency, check whether it's needed on initial load or can be code-split to a later-loaded chunk.
3. Check for unused exports or entire-library imports that prevent tree shaking from removing dead code.
4. Re-measure bundle size and parse/execute time after changes, ideally on a throttled/mid-tier device profile.

## Accessibility-by-default checklist (per interactive element)

1. Does this element use the semantic HTML tag matching its actual behavior (button, a, input, etc.)?
2. If a custom component is required, does it replicate the expected keyboard behavior (focus, Enter/Space activation) of its semantic equivalent?
3. Does it have an accessible name (visible text, aria-label, or aria-labelledby)?
4. Has it been tested with keyboard-only navigation and a screen reader, not just visually?

## Performance findings memo — filled example

> **Core Web Vitals Regression Analysis — Product Page**
> Baseline LCP: 3.8s (poor). Blanket lazy-loading change (including the hero/LCP image) regressed LCP to 4.6s.
> **Root cause: The lazy-loaded element was the LCP element itself** — below-the-fold images were never the actual bottleneck.
> **Fix: Removed lazy-loading and added `fetchpriority="high"` on the hero image; kept lazy-loading on genuinely below-the-fold images.**
> **Result: LCP improved to 2.1s (good). INP (180ms) and CLS (0.05) both remain within "good" thresholds — no regression introduced elsewhere.**
