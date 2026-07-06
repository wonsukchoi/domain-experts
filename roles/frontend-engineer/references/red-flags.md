### A lazy-loading optimization is applied to all images site-wide, including above-the-fold content
- **Usually means:** The largest visible element (the LCP candidate) may be getting delayed rather than sped up, since lazy-loading defers fetch until the browser determines an element is near the viewport.
- **First question:** Is the lazy-loaded element the page's actual LCP element, or genuinely below the fold?
- **Data to pull:** LCP measurement before and after the change, identification of which element is the current LCP candidate.

### A performance optimization is measured against only one Core Web Vital
- **Usually means:** The change could be improving the targeted metric while silently regressing a different one.
- **First question:** Have LCP, INP, and CLS all been measured before and after this change, not just the one being optimized?
- **Data to pull:** Before/after measurements for all three Core Web Vitals.

### Interaction-handling code alternates between writing a DOM change and immediately reading a layout property
- **Usually means:** Forced synchronous layout (layout thrashing) is likely occurring, and it compounds significantly if this pattern repeats in a loop.
- **First question:** Are all DOM reads (offsetHeight, getBoundingClientRect, etc.) batched together, separate from all DOM writes, or are they interleaved?
- **Data to pull:** The specific interaction code, a performance profile showing forced layout events.

### A new dependency or feature was added without checking its bundle size impact
- **Usually means:** Main-thread parse/execute time may have crept up, with the effect more pronounced on lower-end devices than on the development machine used to test it.
- **First question:** What is this dependency's bundle size contribution, and could it be code-split to load only when actually needed?
- **Data to pull:** Bundle analyzer output before and after adding the dependency.

### Performance testing was only conducted on a fast development machine or high-speed network
- **Usually means:** Real-world degradation on lower-end mobile devices or slower networks could be significantly worse than what testing revealed.
- **First question:** Has this change been tested under throttled/mid-tier device and network conditions representative of real users?
- **Data to pull:** Performance measurements under throttled conditions, real user monitoring data if available.

### Interactive UI elements are built with non-semantic markup (a div with a click handler instead of a button)
- **Usually means:** Keyboard navigation and screen reader compatibility likely don't work correctly without significant additional ARIA retrofitting, and even then may not be as reliable as native semantic elements.
- **First question:** Would this element behave correctly under keyboard-only navigation and with a screen reader as currently built?
- **Data to pull:** Accessibility audit results, keyboard navigation test results for this component.

### An image is displayed without explicit width/height attributes
- **Usually means:** A layout shift is likely to occur once the image finishes loading, contributing to a worse CLS score.
- **First question:** Does this image have explicit dimensions (or an aspect-ratio placeholder) reserved before it loads?
- **Data to pull:** CLS measurement, specific elements contributing to layout shift.

### A page's INP is poor but no profiling has identified what's blocking the main thread during interaction
- **Usually means:** Without identifying the specific blocking script or handler, any fix attempted is likely to be a guess rather than a targeted correction.
- **First question:** Has a performance profile been captured during the actual slow interaction to identify the specific long task blocking the main thread?
- **Data to pull:** Performance profile/trace during the interaction, list of long tasks and their source.
