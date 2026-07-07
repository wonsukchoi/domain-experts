# Technical Writer — Red Flags

### Support tickets citing "the docs say X but it does Y" — more than 5/month on one page
- **Usually means:** The documented example is stale relative to a recent API/behavior change; second likeliest is an edge case the doc never covered but reads as if it did.
- **First question:** When was this page last verified against the live system, and does that predate the most recent related release?
- **Data to pull:** Page's last-verified date vs. the API changelog for that endpoint/feature.

### A doc page's "last updated" date is more than 2 major releases behind current
- **Usually means:** The page isn't in the release process — no PR gate ties doc updates to the feature that changed.
- **First question:** Is this page in the docs-as-code repo tied to CI, or maintained separately (CMS, wiki)?
- **Data to pull:** Release notes for the intervening versions; diff against the page's described behavior.

### A getting-started tutorial takes more than 8 steps before the first successful API call
- **Usually means:** The tutorial is front-loading setup/conceptual material instead of getting to a working example fast; classic Diátaxis violation (tutorial trying to also be an explanation page).
- **First question:** Which of these steps are truly required before step 1 succeeds, versus "nice to know"?
- **Data to pull:** Time-to-first-successful-call from onboarding analytics, if instrumented.

### A reference doc page has zero worked examples
- **Usually means:** The page was generated from a schema/spec without a human pass to add a real request/response pair; readers will bounce to search for a blog post or Stack Overflow answer instead.
- **First question:** Can I execute this endpoint right now using only what's on this page?
- **Data to pull:** Page view + bounce/exit rate if analytics exist; support tickets referencing this endpoint.

### More than 20% of doc pages have no CI-verified example
- **Usually means:** Docs-as-code exists in name but the example-execution check either doesn't exist or doesn't cover most pages — drift is inevitable without it.
- **First question:** What fraction of pages actually run their examples in CI versus just live in the same repo?
- **Data to pull:** CI config coverage report; list of pages excluded from the example-test suite.

### Top search terms on the docs site return zero-result or low-relevance pages
- **Usually means:** Readers are searching for a task or error message that isn't covered by existing content structure — a real content gap, not a search-tuning problem.
- **First question:** What are readers actually trying to do when they search this term?
- **Data to pull:** Site search analytics — top queries with zero or low click-through results.

### A procedure has never been walked by anyone outside the authoring team
- **Usually means:** The writer (or the engineer who wrote it) is too close to the system to notice missing prerequisite knowledge or an assumed environment state.
- **First question:** Who outside this team has actually run these exact steps, cold, and where did they get stuck?
- **Data to pull:** None exists yet — this itself is the gap; schedule a cold-read session.

### Time-to-first-successful-call is trending up release over release
- **Usually means:** New complexity (auth changes, new required parameters) is outpacing doc updates, or onboarding docs haven't been re-tested against the current flow.
- **First question:** What changed in the onboarding flow or required setup since the last release where this metric was flat?
- **Data to pull:** Onboarding funnel analytics segmented by release/cohort.

### A docs PR merges without sign-off from the feature's code owner
- **Usually means:** Docs are being written from the spec or from asking around, not verified against the person who actually knows current behavior.
- **First question:** Did the feature owner actually review this, or just approve the PR without reading the docs diff?
- **Data to pull:** PR review history — who approved, and whether their comments addressed the docs content specifically.

### A single page mixes reference, tutorial, and explanation content
- **Usually means:** The page grew organically without an editorial pass, or it's trying to serve every reader type at once because splitting it felt like more work.
- **First question:** Is this genuinely a small, known audience that wants all three together, or is that an assumption?
- **Data to pull:** Page analytics — do readers scroll past sections, suggesting they only wanted one part?
