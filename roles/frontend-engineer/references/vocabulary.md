### LCP (Largest Contentful Paint)
A Core Web Vital measuring how long it takes for the largest visible content element (often a hero image or heading) to render, used as a proxy for perceived load speed.
**In use:** "LCP is 3.8 seconds — well above the 2.5-second 'good' threshold."
**Common misuse:** Applying a general performance optimization (like lazy-loading) without checking whether it affects the specific element the LCP metric measures.

### INP (Interaction to Next Paint)
A Core Web Vital measuring the responsiveness of a page to user interactions, capturing the delay between an interaction and the next visual update.
**In use:** "INP came in at 180ms, within the good threshold of under 200ms."
**Common misuse:** Assuming a page with fast load time (good LCP) is automatically responsive to interaction, without separately measuring INP.

### CLS (Cumulative Layout Shift)
A Core Web Vital measuring visual stability — how much visible content unexpectedly shifts position during page load, often caused by images or embeds without reserved space.
**In use:** "CLS is 0.05, well within the good threshold of under 0.1, since the hero image has explicit dimensions set."
**Common misuse:** Displaying images or dynamic content without reserved dimensions, allowing layout to shift as content loads and worsening CLS.

### Critical rendering path
The sequence of steps a browser must complete (parsing HTML, CSS, and JavaScript) before it can render the first paint of a page.
**In use:** "Inlining the critical CSS shortened the critical rendering path, improving first paint."
**Common misuse:** Loading all CSS and JavaScript synchronously in the document head regardless of whether it's needed for first paint, unnecessarily lengthening the critical rendering path.

### Layout thrashing (forced synchronous layout)
A performance anti-pattern where interleaved DOM writes and layout-property reads force the browser to synchronously recalculate layout repeatedly, rather than batching the work.
**In use:** "This loop reads offsetHeight right after each DOM write — that's forced synchronous layout, and it's happening on every iteration."
**Common misuse:** Writing interaction code that alternates between DOM writes and layout reads without batching, multiplying the layout recalculation cost.

### Code splitting
A bundling technique that breaks an application's JavaScript into separate chunks loaded on demand, rather than shipping the entire application bundle upfront.
**In use:** "We code-split the admin dashboard route so regular users never download that bundle."
**Common misuse:** Shipping the entire application as a single bundle regardless of what each page actually needs, forcing users to download and parse code irrelevant to their current view.

### Tree shaking
A build-time optimization that removes unused code (dead code, unused exports) from the final bundle.
**In use:** "Tree shaking removed the unused utility functions from this library, cutting bundle size significantly."
**Common misuse:** Assuming tree shaking automatically removes all unused code regardless of how a dependency is imported, when certain import patterns (e.g., importing an entire library rather than specific functions) can prevent it from working effectively.

### Semantic HTML
Using HTML elements according to their intended meaning and behavior (button for clickable actions, nav for navigation, form controls for inputs) rather than generic elements styled to look similar.
**In use:** "Using a real button element here means keyboard focus and activation work correctly without any extra code."
**Common misuse:** Building interactive elements with generic divs and click handlers, which requires significant additional ARIA and JavaScript work to replicate what semantic elements provide by default.

### ARIA (Accessible Rich Internet Applications)
A set of attributes that can be added to HTML to improve accessibility for assistive technologies, typically used to supplement (not replace) semantic HTML.
**In use:** "We added ARIA labels to clarify this icon-only button's purpose for screen reader users."
**Common misuse:** Using ARIA attributes to retrofit accessibility onto non-semantic markup instead of using the correct native semantic element in the first place, which is generally more reliable.

### Real user monitoring (RUM)
Performance measurement collected from actual users' devices and network conditions in production, as opposed to lab-based synthetic testing.
**In use:** "Lab testing showed good LCP, but RUM data revealed much worse real-world performance on lower-end devices."
**Common misuse:** Relying solely on lab tool measurements (like Lighthouse on a fast development machine) without checking real user monitoring data, which can reveal significantly different performance for actual users.
