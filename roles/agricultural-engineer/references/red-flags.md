# Red flags

Smell tests an agricultural engineer, NRCS reviewer, or P.E. checking a design package catches on first pass.

### Grain-bin wall load computed as hydrostatic (fluid) pressure instead of Janssen's equation

- **Usually means:** the designer treated stored grain like stored water, missing that wall friction reduces lateral pressure and flattens its growth with depth.
- **First question:** was p_h computed with Janssen's equation (γ, R, μ', K) for the actual grain type and wall material, or with a straight p = γh assumption?
- **Data to pull:** the structural calc package, the grain type and wall-friction coefficient used, ASABE EP433's μ'/K table for that grain-wall pairing.

### Irrigation system capacity checked against seasonal average water use, not peak-day demand

- **Usually means:** the capacity check used total seasonal inches divided by season length instead of the crop's peak-growth-stage ET rate.
- **First question:** what ET rate and growth stage was used in the gpm calculation, and does it match the crop's known peak-demand window?
- **Data to pull:** the capacity calculation's stated design ET value, university extension peak-ET guidance for the crop and region, the system's rated application efficiency.

### Manure application rate set from total N on the manure analysis, no first-year availability coefficient applied

- **Usually means:** the plan credited 100% of analyzed N against the crop's requirement instead of the manure-type-and-method-specific first-year availability fraction.
- **First question:** what availability coefficient was applied, and does it match the actual application method (injected vs. surface, incorporated vs. not)?
- **Data to pull:** the manure analysis report, the nutrient management plan's stated availability coefficient and source, the following two seasons' credited carryover N.

### Drainage or ditching design proceeding on mapped hydric soil with no wetland determination on file

- **Usually means:** the hydraulic design was finalized before a Swampbuster/wetland-conversion compliance check was routed through NRCS.
- **First question:** has an NRCS wetland determination or minimal-effect exemption been issued for this area, and does the design predate or postdate it?
- **Data to pull:** SSURGO hydric-soil classification for the parcel, NRCS wetland determination record, any minimal-effect or exemption paperwork.

### Waterway or outlet structure sized to a design storm return period below the downstream consequence class

- **Usually means:** a default 10-year storm was used without checking whether the structure protects higher-value or life-safety downstream infrastructure that warrants a longer return period.
- **First question:** what's downstream of this structure, and does the chosen return period match NRCS guidance for that consequence class?
- **Data to pull:** the design memo's stated return period, downstream land use/infrastructure map, applicable NRCS Conservation Practice Standard's return-period table.

### Erosion-control channel lining specified with one "design velocity" reused across different lining types

- **Usually means:** a single permissible-velocity number was carried from a previous design without matching it to the actual soil or vegetation condition of this channel.
- **First question:** what lining is actually being installed here, and does the design velocity match its permissible-velocity range, not a generic figure?
- **Data to pull:** channel cross-section and lining specification, permissible-velocity table by lining type, as-built photos if erosion is already suspected.

### Tile-drainage spacing pulled from a rule-of-thumb table without checking mapped or measured hydraulic conductivity

- **Usually means:** a standard spacing was applied uniformly across the field without adjusting for the soil unit's actual Ksat, understating or overstating the number of laterals needed.
- **First question:** what hydraulic conductivity value was used for this spacing calculation, and does it match the mapped soil unit(s) the tile actually crosses?
- **Data to pull:** SSURGO Ksat values by soil unit, the spacing calculation's stated Ksat input, field drainage-complaint history if spacing is already suspected of being wrong.

### Manure or wastewater storage structure sized to the annual production volume alone, no freeboard or precipitation addition

- **Usually means:** the storage volume calculation covered only the manure/wastewater generated, omitting freeboard, direct precipitation onto the storage surface, and any dilution or wash water added.
- **First question:** does the storage volume calculation include freeboard and a precipitation/dilution allowance, or only the base production estimate?
- **Data to pull:** the storage design calculation, required non-discharge storage period for the operation's permit class, regional precipitation data used (or omitted).

### Structural design for a bin, shed, or storage structure omits a stated wind or snow load basis

- **Usually means:** the structure was designed to "how we've always built it" rather than a cited ASCE 7 wind/snow load for the site's actual location and exposure category.
- **First question:** what wind speed and snow load (and exposure/risk category) does the structural calc cite, and do they match the site's actual location?
- **Data to pull:** the structural calc package's load basis, ASCE 7 map values for the site, local building department's adopted load requirements if more stringent.

### Well or pump capacity shortfall triggers an immediate upgrade recommendation with no soil-water-buffer check

- **Usually means:** the capacity shortfall was treated as an automatic capital-project trigger without checking whether the field's available water capacity can buffer the deficit through scheduling.
- **First question:** what's the cumulative deficit over the peak-demand window, and does it exceed the root zone's usable soil water storage at the operator's actual management-allowed depletion?
- **Data to pull:** the capacity shortfall calculation, soil AWC and effective root depth for the field, planned or actual soil-moisture monitoring data through the peak window.

### Irrigation pipeline sized to one diameter throughout with no velocity check

- **Usually means:** the mainline was sized for the required flow rate without checking that resulting velocity stays under the threshold that risks excess friction loss or water-hammer damage on valve closure.
- **First question:** what's the computed velocity in each pipe segment at design flow, and does any segment exceed roughly 5 ft/s?
- **Data to pull:** pipeline sizing calculation with segment diameters and flows, friction-loss table used, any water-hammer analysis for segments with automated valves.
