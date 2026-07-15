## `onet_occupations.tsv`

Code + title for all 1,016 detailed occupations from the O*NET database (release 30.3), used as the master checklist in [`ROADMAP.md`](../ROADMAP.md). Descriptions were dropped to keep this file small — full descriptions are available from the source below if needed.

**Source & attribution:** This file uses information from the Occupational Information Network (O*NET) database, developed by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA), and the National Center for O*NET Development. Used under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/). O*NET® is a trademark of USDOL/ETA. Source: [onetcenter.org/database.html](https://www.onetcenter.org/database.html).

Regenerate `ROADMAP.md` and the README role-count summary from this file plus the current `roles/` directory by running `scripts/generate_roadmap.py`.

## `esco_occupations.tsv`

All 2,942 member occupations from the EU's ESCO taxonomy (v1.2), fetched 2026-07-15 via the [public ESCO API](https://ec.europa.eu/esco/api), diffed and semantically triaged against this repo's roles. Columns: ISCO code, title, status (`covered` / `likely-covered` / `dup` / `niche` / `new` / `skipped-armed-forces`), matching repo role slug where one exists, and ESCO URI. The 260 `new` occupations form the checklist in [`ESCO-BACKLOG.md`](../ESCO-BACKLOG.md).

**Source & attribution:** This file uses the ESCO classification of the European Commission. ESCO is available free of charge; see [esco.ec.europa.eu](https://esco.ec.europa.eu/en/use-esco/download) for terms of use.
