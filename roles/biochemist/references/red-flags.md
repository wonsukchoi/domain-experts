# Biochemist — Red Flags

### Km/Vmax reported from total protein concentration, no active-site titration
- **Usually means:** analyst assumed A280 or Bradford total protein equals active enzyme concentration, absorbing an inactive-fraction bias into every downstream constant.
- **First question:** was active enzyme concentration determined by active-site titration or burst kinetics, or only estimated from total protein?
- **Data to pull:** the active-site titration data (if it exists); the ratio of specific activity to a historical reference value for this enzyme.

### Inhibition mechanism named from a single-[S] IC50 shift
- **Usually means:** the full Km/Vmax panel across multiple inhibitor and substrate concentrations was skipped in favor of a faster single-point assay.
- **First question:** is there a full kinetics dataset (≥3 inhibitor concentrations × ≥4 substrate concentrations) behind this mechanism claim, or just one IC50 curve?
- **Data to pull:** the raw rate data across the [S]/[I] matrix; the Km/Vmax-vs-[I] replot and its R².

### Binding affinity (Kd) trusted from a single method, especially SPR alone
- **Usually means:** speed or cost pressure skipped orthogonal confirmation; SPR immobilization or avidity artifacts can produce an affinity that doesn't hold in solution.
- **First question:** has this Kd been confirmed by a second method with a different physical principle (e.g., ITC)?
- **Data to pull:** the SPR sensorgram fit quality (Chi²); any ITC or fluorescence-polarization data for the same interaction.

### Structural method chosen before checking target's biophysical properties
- **Usually means:** default to whatever method the lab has running, rather than a check against target size, flexibility, and available quantity.
- **First question:** has the target's size, oligomeric state, and stability been characterized (SEC-MALS, DLS) before committing to a structural method?
- **Data to pull:** SEC-MALS or DLS data on the purified target; crystallization screening history if crystallography was already attempted.

### Kinetic value drifts >20% between a fresh prep and a stored/freeze-thawed aliquot
- **Usually means:** activity loss on storage (aggregation, oxidation of a reactive cysteine, proteolysis), not a change in the underlying biology.
- **First question:** was the fresh-prep condition re-run as a control alongside the stored aliquot in the same experiment?
- **Data to pull:** specific-activity time course across storage duration; SDS-PAGE or SEC comparing fresh vs. stored sample for aggregation/degradation.

### Buffer or temperature not matched between reference and test conditions in a binding/kinetics comparison
- **Usually means:** two datasets generated on different days or by different people under slightly different buffer/pH/ionic-strength conditions are being compared as if directly comparable.
- **First question:** were both conditions run in the same buffer, pH, ionic strength, and temperature?
- **Data to pull:** the buffer recipe and temperature log for each dataset being compared.

### Isolated yield drops sharply (>50% loss) at a purification step with no explanation
- **Usually means:** aggregation, nonspecific binding to a column resin, or a concentration-step error (e.g., protein sticking to a concentrator membrane).
- **First question:** was the flow-through/wash fraction checked for the target protein, or assumed to be clean loss?
- **Data to pull:** SDS-PAGE of flow-through and wash fractions from that step; column loading capacity vs. actual load.

### Structure solved but functional/kinetic data never reconciled against it
- **Usually means:** the structural and functional characterization tracks ran independently without cross-checking (e.g., a proposed catalytic residue from the structure never confirmed by mutagenesis/kinetics).
- **First question:** does the kinetic behavior (e.g., mutation of a proposed active-site residue) match what the structure predicts?
- **Data to pull:** site-directed mutagenesis kinetics data, if it exists, for residues implicated by the structure.

### Purity reported as a single number with no method specified
- **Usually means:** the purity claim (e.g., ">95% pure") isn't attributable to a specific assay and may not reflect what the downstream use actually needs to know.
- **First question:** purity by which method — SDS-PAGE densitometry, SEC, mass spec — and does that method's blind spot matter here?
- **Data to pull:** the raw gel image or chromatogram behind the purity number.
