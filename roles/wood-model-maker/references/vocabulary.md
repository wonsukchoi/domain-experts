# Vocabulary

### Scale conversion
The calculation translating a full-scale dimension to its equivalent at a model's reduced scale, ideally performed independently from the original source for each feature rather than chained from previously converted features.
**In use:** "Converting each window position directly from the full-scale drawing at 1:50 — not stepping off the last one we cut."
**Common misuse:** Chaining scale conversions by measuring from a previously cut model feature rather than the original source dimension — this compounds small reading/rounding errors progressively across a sequence of features, rather than keeping each one's error independent and bounded.

### Scale error projection
The calculation of what a small error at model scale actually represents once converted back to full scale, used to judge whether a seemingly minor imprecision is actually significant.
**In use:** "A tenth of an inch off at model scale doesn't sound like much, but at 1:50 that's five inches at full size — that's the number that actually matters."
**Common misuse:** Judging a model-scale error's significance by its small absolute physical size alone — the relevant question is what that error represents once the scale ratio is applied, which is often much larger than intuition about "it's a small model" suggests.

### Material representation (at scale)
The practice of selecting a model material based on how it will visually read at the model's actual scale and viewing distance, rather than assuming the full-scale "correct" material choice translates directly.
**In use:** "The full-scale material's a matte stone finish, but at this model's scale we tested a few options and a different material actually reads more convincingly as 'stone' from typical viewing distance."
**Common misuse:** Assuming the literal full-scale material, simply scaled down, will look correct in the model — texture, gloss, and color saturation don't always translate proportionally, and a material chosen for full-scale accuracy can look wrong at model scale without testing.

### Model purpose (communication vs. functional)
The fundamental distinction between a model built primarily to communicate design intent visually/proportionally versus one built to verify functional/dimensional fit, which determines where precision effort should be allocated.
**In use:** "This is a functional fit-check model — dimensional accuracy is what matters here, not matching the final finish."
**Common misuse:** Building every model to a uniform precision/finish standard regardless of its actual purpose — a concept communication model over-engineered for dimensional precision wastes effort in the wrong place, while a functional model under-specified on dimensional accuracy fails its actual purpose even if it looks polished.

### Chained measurement (model-scale)
Measuring a new feature's position relative to a previously measured or cut feature, rather than independently from the original source data, causing errors to compound progressively across a sequence.
**In use:** "We're not chaining these mullion positions — each one traces back to the original drawing independently."
**Common misuse:** Treating chained measurement as a time-saving convenience without recognizing its compounding-error risk — the same principle that causes compounding error in other precision trades (layout work, for example) applies directly to scale model construction.

### Reference baseline (model construction)
A fixed, established point or line on a model from which all scaled dimensions are measured, ensuring consistency and traceability back to the original source data.
**In use:** "Every window position on this facade references the same baseline — that's what keeps our conversions independent instead of chained."
**Common misuse:** Allowing the "reference point" for measurement to shift informally during construction (measuring from whatever feature was most recently completed) rather than maintaining a single, fixed baseline throughout — this is functionally identical to chaining and produces the same compounding-error risk.

### Construction robustness (model-specific)
The structural durability and joinery approach appropriate to a specific model's anticipated handling, shipping, and display lifespan, rather than a single standard applied to every model.
**In use:** "This one's shipping to three trade shows over a year — building it more robustly than we would a one-time internal review model."
**Common misuse:** Applying uniform construction standards across all models regardless of their actual use case — over-building a one-time review model wastes time and cost, while under-building a model destined for repeated handling or shipping risks damage before it serves its purpose.

### Proof-of-concept model (fit-check)
A model built specifically to verify functional or spatial fit — whether components physically work together as designed — prioritizing dimensional accuracy over visual/material representation.
**In use:** "This is strictly a fit-check model — we're not painting or finishing it, just confirming these two assemblies actually mate correctly at this dimension."
**Common misuse:** Investing finishing/material-representation effort into a fit-check model at the expense of dimensional verification time, or conversely, assuming a fit-check model's rough finish means its dimensional accuracy can also be loose — the model's precision budget should go entirely toward the dimension that actually matters for its stated purpose.
