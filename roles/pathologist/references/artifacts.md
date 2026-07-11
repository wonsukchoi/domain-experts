# Artifacts — filled templates a pathologist actually produces

## 1. Synoptic report template (CAP-style), filled — invasive breast carcinoma

```
SPECIMEN: Right breast, partial mastectomy
PROCEDURE: Partial (segmental) mastectomy, wire-localized
TUMOR SITE: Upper outer quadrant

HISTOLOGIC TYPE: Invasive ductal carcinoma, no special type
HISTOLOGIC GRADE (Nottingham/Elston-Ellis):
  Tubule/gland formation score: 3/3
  Nuclear pleomorphism score:   3/3
  Mitotic count score:          2/3  (9 mitoses/10 HPF, 0.55 mm field diameter)
  TOTAL SCORE: 8/9  → GRADE 3

TUMOR SIZE: 1.8 cm (greatest dimension, invasive component)
MARGINS:
  Superior:  negative, 2.1 cm
  Inferior:  negative, 1.8 cm
  Medial:    negative, 1.4 cm
  Lateral:   negative, 0.9 cm
  Deep:      negative, 0.1 cm (no tumor on ink — SSO-ASTRO 2014 adequate for invasive Ca)
  Superficial: negative, 3.0 cm

LYMPHOVASCULAR INVASION: Not identified
REGIONAL LYMPH NODES: 2 sentinel nodes, 0/2 positive (H&E + cytokeratin IHC)

pTNM (AJCC 8th ed.): pT1c pN0(sn)
BIOMARKERS:
  ER: Positive, 95% strong nuclear staining
  PR: Positive, 60% moderate nuclear staining
  HER2: Negative, IHC 1+ (no reflex FISH per ASCO/CAP guideline)
  Ki-67: 22% (lab-specific reference range noted in report footer)

AJCC ANATOMIC STAGE: IA
AJCC PROGNOSTIC STAGE: IB (Grade 3 bumps a T1N0M0, HR-positive/HER2-negative
  tumor from IA to IB per the AJCC 8th-edition prognostic-stage table)

COMMENT: Deep margin close (1 mm) but negative — no tumor on ink. Per SSO-ASTRO
2014 consensus, this is an adequate margin for invasive carcinoma receiving
whole-breast irradiation; re-excision is not indicated on margin grounds alone.
```

Cassette map backing the report (documented at grossing, before any diagnosis is reached):
A1 superior margin · A2 inferior margin · A3 medial margin · A4 lateral margin ·
A5 superficial margin · A6 deep margin · A7 deep margin re-submitted en face
(closest approach to tumor) · A8–A9 serial tumor cross-sections · A10 background
parenchyma, uninvolved.

## 2. Gross description worksheet template (resection specimen)

```
Specimen received [fresh / in formalin], labeled "[site], [procedure]."
Orientation: [suture/clip present? which margin does it mark?]
Dimensions (fresh): [L] x [W] x [D] cm
Dimensions (post-fixation, if remeasured): [L] x [W] x [D] cm
  — note: fixation shrinkage of 10–20% is expected; if imaging size and
    gross/fixed size disagree by more than that, state which measurement
    (fresh vs. fixed) the report is using and why, rather than letting the
    discrepancy stand unexplained at tumor board.
Inking scheme: [color per margin, e.g., superior=blue, inferior=black...]
Lesion: [size] cm, [color/consistency], distance to nearest margin: [ ] cm at [which margin]
Sectioning: serial sections at [interval, e.g., 3-5 mm] perpendicular to [long axis / chest wall]
Representative sections submitted: [cassette letters/numbers + what each contains]
All grossly abnormal areas submitted: [yes/no + cassette reference]
```

## 3. IHC differential-panel decision table

Build the panel from the H&E-generated differential — order the minimum set that discriminates, not the maximal set available.

| Working differential (from H&E) | First-line discriminating panel | Interpretation note |
|---|---|---|
| Undifferentiated malignant neoplasm (carcinoma vs. lymphoma vs. melanoma vs. sarcoma) | pancytokeratin (AE1/AE3), CD45, S100/SOX10, desmin | Run all four together — a "positive for everything" result usually means a control or fixation problem, not a hybrid tumor; recheck same-run positive/negative controls before re-interpreting biology. |
| Adenocarcinoma, site of origin unclear (metastatic workup) | CK7, CK20, TTF-1, CDX2, GATA3, PAX8 | TTF-1+ suggests lung or thyroid — not lung alone; interpret against the clinical/radiologic context, not as a single-marker verdict. |
| Follicular thyroid lesion, capsular/vascular invasion equivocal on H&E | Deeper levels through the capsule; defer additional IHC — this is a sampling/leveling problem, not a marker problem | IHC (e.g., HBME-1, galectin-3) is adjunctive at best for this specific question; the answer usually comes from finding or excluding definitive capsular/vascular invasion on more tissue, not from a stain. |
| Spindle cell lesion (reactive vs. sarcoma vs. GIST) | SMA, desmin, S100, CD34, DOG1, Ki-67 | Ki-67 index supports a malignant impression but does not itself make the call; pair with mitotic count and infiltrative growth pattern on H&E. |
| Lymphoma subclassification | CD20, CD3, CD5, CD10, BCL2, BCL6, MYC, Ki-67 | A single marker never subclassifies a lymphoma — the pattern across the panel plus architecture does; MYC/BCL2 "double expressor" status changes prognosis and is reported explicitly, not folded into a generic "positive" line. |

## 4. Grading systems quick reference

| System | Organ | Components | Score → Grade mapping |
|---|---|---|---|
| Nottingham (Elston-Ellis) | Breast, invasive carcinoma | Tubule formation (1-3) + nuclear pleomorphism (1-3) + mitotic count (1-3) | 3-5 = Grade 1; 6-7 = Grade 2; 8-9 = Grade 3 |
| Gleason / ISUP Grade Group | Prostate | Primary + secondary (or worst) architectural pattern, each 3-5 | Gleason ≤6 = Grade Group 1; 3+4=7 = Group 2; 4+3=7 = Group 3; 8 = Group 4; 9-10 = Group 5 |
| Fuhrman / ISUP nucleolar grade | Renal cell carcinoma | Nucleolar prominence at specified objective power | Grade 1 (invisible/inconspicuous at 400x) through Grade 4 (bizarre multinucleated giant cells) |

Sampling-bias note to attach whenever a grade comes from a needle biopsy rather than a resection: state the specimen type in the same sentence as the grade (e.g., "Gleason 6 (Grade Group 1) on needle biopsy") — literature-documented upgrading at prostatectomy for biopsy Gleason 6 runs roughly 30-40%, so the biopsy grade is a floor, not a final answer.

## 5. Margin / re-excision decision table by consensus guideline

| Diagnosis | Margin status | Re-excision indicated? | Source |
|---|---|---|---|
| Invasive carcinoma, breast-conserving surgery + whole-breast RT | No tumor on ink, any distance | No, on margin grounds alone | SSO-ASTRO 2014 |
| DCIS, breast-conserving surgery + whole-breast RT | Tumor within 2 mm of ink | Yes, consider re-excision | SSO-ASTRO-ASCO 2016 |
| DCIS, breast-conserving surgery + whole-breast RT | ≥2 mm clearance | No | SSO-ASTRO-ASCO 2016 |
| Invasive carcinoma | Tumor present at ink (positive) | Yes | SSO-ASTRO 2014 |

Always state which of these two guidelines applies in the comment — DCIS and invasive disease use different thresholds, and applying the DCIS 2 mm rule to an invasive-only margin (or vice versa) is the single most common margin-interpretation error a generalist reviewer makes.
