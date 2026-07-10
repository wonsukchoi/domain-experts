# Playbook

## Marker efficiency and cumulative fabric waste calculation (filled example)

Marker: 100 sq yd fabric laid, 88 sq yd pattern area. Production run: 500 markers.

| Step | Value |
|---|---|
| Total fabric laid | 100 sq yd |
| Pattern piece area | 88 sq yd |
| Marker efficiency | (88 / 100) × 100 = 88% |
| Waste percentage | 100% − 88% = 12% |
| Waste per marker | 100 × 0.12 = 12 sq yd |
| Total waste, 500-marker run | 500 × 12 = 6,000 sq yd |

**Comparison across efficiency levels (same 100-sq-yd marker, 500-marker run):**

| Marker efficiency | Waste per marker | Total waste, 500-marker run |
|---|---|---|
| 85% | 15 sq yd | 500 × 15 = 7,500 sq yd |
| 88% | 12 sq yd | 500 × 12 = 6,000 sq yd |
| 92% | 8 sq yd | 500 × 8 = 4,000 sq yd |
| 95% | 5 sq yd | 500 × 5 = 2,500 sq yd |

**Rule applied:** Each additional percentage point of marker efficiency saves 5 sq yd of fabric per 500-marker run at this marker size — improving from 88% to 92% (a 4-point gain) saves 2,000 sq yd, a real, calculable cost reduction worth pursuing before committing to full production at a lower efficiency.

## Ply-height accuracy reference by fabric type (filled example)

| Fabric type | Typical accuracy-preserving ply height | Notes |
|---|---|---|
| Lightweight cotton/poly blend | 80–100 plies | Thin, stable fabric holds accuracy at higher stacks |
| Mid-weight denim | 40–60 plies | Thicker fabric, moderate stack limit |
| Heavy wool coating | 15–25 plies | Thick, less stable fabric requires much lower stacks for accuracy |
| Stretch/knit fabric | 10–20 plies | Stretch behavior under cutting pressure limits safe stack height significantly |

**Applied check:** Running a stretch knit fabric at the equipment's 100-ply physical maximum (appropriate for lightweight cotton) would produce significant distortion at lower layers — ply height limits are fabric-specific, and reusing a limit validated for one fabric type on a very different one risks exactly the accuracy problem the limit exists to prevent.
