# UX design working vocabulary

Terms a UX designer uses precisely. Format: definition → how a practitioner says it → common misuse.

**Don't Make Me Think (Krug's heuristic)** — The principle that any moment a user has to stop and figure out how something works is a design cost, even if they eventually succeed — the goal is a zero-stop path through the primary flow.
In use: "Users hesitated for 3+ seconds at this step in every test session — that hesitation is the cost, even though everyone eventually figured it out."
Misuse: treating eventual task success as evidence the design worked, ignoring the friction and hesitation cost along the way that "don't make me think" is specifically about.

**Fitts's Law** — The principle that a target's ease of use (size, proximity to resting position) directly affects how much it gets used — the priority action should be placed where it's easiest to reach, not just where it's logically grouped.
In use: "The primary CTA is bigger and closer to the thumb's resting position on mobile — that's Fitts's Law in practice, not just visual hierarchy."
Misuse: placing the priority action based purely on logical grouping or visual hierarchy conventions without considering actual physical/cursor ease of reach.

**Progressive disclosure** — Showing only the minimum information/options needed to act now, revealing complexity only when the user explicitly asks for it (advanced settings, "show more"), rather than presenting every option up front.
In use: "Bulk actions are behind a 'bulk mode' toggle scoped to the specific task — that's progressive disclosure, not a permanent navigation fork."
Misuse: presenting every possible option or setting on the main screen for the rare user who needs it, burdening the common-case user with complexity they don't need.

**Recognition over recall** — Designing so users can recognize available options (menus, autocomplete, visible state) rather than requiring them to remember what's possible, since working memory is small and unreliable under task load.
In use: "We show the available filter options as a visible list instead of requiring users to remember and type a filter syntax — recognition over recall."
Misuse: requiring users to recall commands, codes, or options from memory when a visible, recognizable alternative (a menu, an autocomplete) would reduce cognitive load.

**Nielsen's severity scale** — A framework for prioritizing usability issues by actual impact: cosmetic (low), minor (workaround exists), major (blocks task), catastrophic (prevents completion or causes data loss) — used to avoid treating every issue with the same urgency.
In use: "This is a major issue — it blocks task completion for a meaningful share of users — versus the color contrast note, which is cosmetic."
Misuse: prioritizing usability fixes by ease of implementation or recency of report rather than by actual severity/user impact.

**Heuristic evaluation** — A fast expert-review pass against established usability principles (e.g., Nielsen's 10 heuristics) conducted before spending user-testing budget, used to catch known-pattern issues early and cheaply.
In use: "The heuristic evaluation caught the missing visibility-of-system-status issue before we spent testing budget confirming it with users."
Misuse: skipping a cheap expert heuristic pass and going straight to expensive user testing, missing known-pattern issues that could have been caught faster and more cheaply.

**Task completion rate** — The percentage of users who successfully complete a defined task in a flow, a business-translatable usability metric distinct from satisfaction or aesthetic impressions.
In use: "Task completion rate dropped from 92% to 77% on this step — that's the number that translates directly into the support ticket volume increase."
Misuse: reporting only satisfaction scores or qualitative impressions to stakeholders without task completion data, missing the metric that most directly translates to business impact (drop-off, support cost).

**Dark pattern** — A design choice that manipulates users into an action that serves a business metric at the expense of their genuine interest or informed consent, distinct from a legitimate business-goal-driven design decision that's transparent about the tradeoff.
In use: "That's a dark pattern — it boosts signup conversion by hiding the unsubscribe cost, not by making the value proposition genuinely clearer."
Misuse: labeling any business-goal-aligned design choice as a "dark pattern" reflexively, or conversely, implementing a genuinely manipulative pattern without naming the user-trust tradeoff explicitly to stakeholders.

**Paradox of choice** — The finding that more options can reduce completion and satisfaction even when users report wanting more choice, used to argue for a sensible default over expanding configurability by default.
In use: "Per the paradox of choice, we're shipping with one well-designed default and moving the alternate options behind an advanced setting, not presenting all three options up front."
Misuse: assuming users' stated preference for more options ("I want more choices") should directly drive adding more configurability, when the actual behavioral result of more options is often reduced completion and satisfaction.

**Design system / component library** — A shared set of reusable interface components with consistent behavior and appearance, ensuring the same control looks and behaves the same everywhere it appears across a product.
In use: "The date picker behaves identically across all five places it's used — that consistency comes from the design system, not from each team rebuilding it."
Misuse: allowing each team or flow to implement its own version of a common control, breaking the consistency that reduces the attention cost users pay to relearn conventions across the product.
