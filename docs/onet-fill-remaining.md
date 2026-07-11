# O*NET gap-fill — remaining scope and runbook

Continuation of the mass role-authoring pass done 2026-07-11. See `docs/CONTEXT.md` for the short summary; this file has the full detail needed to resume without re-deriving anything.

## What's left

8 O*NET major groups, ~161 real (non-"All Other", non-military) occupations still uncovered. Groups 19, 21, 25, 27, 29, 31 are done (186 roles shipped this pass). Groups 55 (Military Specific) and all "All Other" catch-all codes are intentionally skipped per standing repo convention (see prior `docs/CONTEXT.md` history).

Remaining groups, smallest first (do the small ones first to validate the pipeline is healthy before the big ones):

| Group | Count | Note |
|---|---|---|
| 49 | 2 | Install/Maint/Repair remainder |
| 43 | 3 | Office/Admin remainder |
| 53 | 3 | Transportation remainder |
| 33 | 17 | Protective Service |
| 41 | 15 | Sales |
| 39 | 22 | Personal Care & Service |
| 47 | 36 | Construction/Extraction remainder |
| 51 | 63 | Production — biggest remaining group |

## How to run it (Claude Code + Workflow tool)

1. Recreate the runner script below at any scratch path (e.g. your session scratchpad) — **do not put it inside this repo's tracked tree**, it accidentally got committed once already and had to be reverted (`git log` for "chore: remove workflow-runner scratch script").
2. For each group below, call `Workflow({scriptPath: "<path-to-script>", args: <that group's JSON array>})`.
3. Wait for completion. The script itself does draft (parallel, one agent per occupation, full AUTHORING.md pipeline solo) then ops (lint/regenerate/commit/push) as two phases.
4. If the ops phase fails or the workflow errors mid-run (API outages cause `stalled`/`connection closed` errors — this happened once on group 25), do NOT assume nothing landed:
   - `git status --short` in the repo to see which `roles/<slug>/` dirs got written before the crash.
   - Check each candidate dir has all 4 files (`SKILL.md` + `references/{playbook-or-artifacts,red-flags,vocabulary}.md`). Delete any partial/incomplete ones (crashed mid-write) — those occupations need a clean re-run.
   - For complete-but-uncommitted dirs, spawn a one-off ops agent (see prompt template below) to lint/commit/push just that batch, then re-launch a fresh workflow for whatever's still missing.
5. Known agent quirk: an agent sometimes checks `ls roles/` mid-run, sees the directory it just wrote, and mistakenly concludes "already exists, skipping" — even though nothing existed before it started. If a "skipped: duplicate" note doesn't cite a prior git commit for that path, treat it with suspicion (check `git log --all --oneline -- roles/<slug>` — if empty, it's not actually a duplicate) and consider it salvageable.

## Known issue to fix eventually

`roles/critical-care-nurse/` is mapped to `onet_soc_code: "29-1141.01"` (Acute Care Nurses) but titled/slugged as if it were "Critical Care Nurse" — the actual O*NET code `29-1141.03` (Critical Care Nurses) is technically still uncovered, and a sibling agent skipped it thinking this was already the right role. Needs a human/agent pass to either rename this role to `acute-care-nurse` and free up `29-1141.03` for its own role, or confirm the content genuinely covers both and merge properly.

## Runner script (`onet-fill-group.js`)

```js
export const meta = {
  name: 'onet-fill-group',
  description: 'Author spec-2 domain-expert roles for one O*NET major group, lint+regenerate+commit',
  phases: [
    { title: 'Draft' },
    { title: 'Ops' },
  ],
}

const REPO = '/Users/wonsukchoi/Developer/opensource/domain experts'

const targets = typeof args === 'string' ? JSON.parse(args) : args
const group = targets[0].group

const DRAFT_SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    code: { type: 'string' },
    title: { type: 'string' },
    status: { type: 'string', enum: ['added', 'skipped'] },
    score: { type: 'number' },
    note: { type: 'string' },
  },
  required: ['code', 'title', 'status'],
}

const OPS_SCHEMA = {
  type: 'object',
  properties: {
    group: { type: 'string' },
    added_slugs: { type: 'array', items: { type: 'string' } },
    lint_clean: { type: 'boolean' },
    committed: { type: 'boolean' },
    pushed: { type: 'boolean' },
    commit_sha: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['group', 'added_slugs', 'lint_clean'],
}

function draftPrompt(t) {
  return `Repo: "${REPO}" (cd there first). Domain-experts skill library — turns human job roles into agent-loadable skill files.

Read in full before writing anything: AUTHORING.md, TEMPLATE.md, and CONTRIBUTING.md's "Exact recipe for adding a role" section in this checkout, plus one gold-standard example role under roles/ (financial-manager, lawyer-contracts, product-manager, data-scientist, or marketing-strategist — pick whichever is closest in shape to this occupation: playbook-style if the role executes processes, artifacts-style if it produces documents/models).

Your occupation: O*NET-SOC ${t.code} — "${t.title}".

Step 0 — verify uncovered: run \`grep -i "${t.code}" ROADMAP.md\` and \`ls roles/\` (grep for close keywords) to confirm no existing role already covers this occupation under a different slug or synonym. If one does, skip and report why instead of creating a duplicate.

Pick a kebab-case slug for roles/<slug>/. Base it on the natural job title, not the raw O*NET phrasing verbatim when that phrasing is awkward taxonomy-speak (e.g. "Physicians, Pathologists" -> "pathologist"). For Postsecondary/specialty variants that might collide with a plausible existing non-academic role, disambiguate the slug (e.g. "chemistry-teacher-postsecondary") — check roles/ first.

Run the FULL AUTHORING.md pipeline yourself, solo, in one pass: Pass 0 research (find 3-5+ real named sources — practitioner books, standards docs, professional associations, postmortems; O*NET task lists only as a coverage skeleton, never as prose source — O*NET text is exactly the generic content this repo rejects), Pass 1 draft to spec, Pass 2 adversarial self-critique (quote every derivable sentence, find every idea stated twice, recompute worked-example arithmetic, check all four red-flag fields, check the banned-pattern list), Pass 3 revise fixing every defect found, Pass 4 self-score against AUTHORING.md's 9-criterion rubric.

Ship bar: >=14/18 with no zero on any criterion. If your best revision can't reach that bar (occupation too thin/obscure for a genuine expert voice, or effectively a duplicate) — do NOT write files. Report status "skipped" with why.

If shipping, write exactly four files: roles/<slug>/SKILL.md (frontmatter: onet_soc_code: "${t.code}", category from the fixed list, maturity: draft, spec: 2), references/playbook.md OR artifacts.md (per AUTHORING.md's naming rule), references/red-flags.md (7-14 entries), references/vocabulary.md (8-17 terms). Follow every exact format in AUTHORING.md/TEMPLATE.md/CONTRIBUTING.md verbatim — frontmatter shape, section order, dedup rule, banned-word list, "when X default Y unless Z" heuristic form, worked example with reconciling numbers and a quoted deliverable.

Do NOT run git commands, lint_roles.py, or generate_roadmap.py — a separate batch step handles that after every role in this group is drafted.

Report via structured output: slug, code, title, status (added/skipped), your self-assigned score out of 18, and a one-line note (why skipped, or any concern worth a human second look).`
}

function opsPrompt(group, added) {
  const slugList = added.map(d => d.slug).join(' ')
  return `Repo: "${REPO}" (cd there first). A batch of ${added.length} new domain-expert roles for O*NET major group ${group} was just drafted by other agents: ${slugList || '(none — all skipped)'}.

If the list is empty, just report and stop — nothing to do.

Otherwise, in order:
1. \`git status\` — confirm only the new roles/<slug>/ directories are untracked/new (no unexpected changes elsewhere).
2. \`git add roles/<slug>\` for each of: ${slugList}
3. Run \`python3 scripts/lint_roles.py\` against these slugs (check its --help or read the script if unsure of multi-slug invocation) until 0 errors. Fix banned-pattern hits, missing sections, malformed red-flags/vocabulary entries, or frontmatter issues yourself by editing files directly — resolve, don't just report. If a role is unsalvageable within reasonable effort, \`git rm -r roles/<slug>\` it and drop it from the added list.
4. \`python3 scripts/generate_roadmap.py\` to refresh ROADMAP.md, README's role-count block, and data/roles.json.
5. \`git add -A -- roles README.md ROADMAP.md data/roles.json\` — stage ONLY role directories and the three generated files, never a bare \`git add -A\`. If other unexpected changes exist in the working tree, leave them untouched and note them.
6. \`git commit -m "role: add batch — O*NET group ${group} (<N> roles)"\` with the real final N and a short bullet list of slugs in the body.
7. \`git pull --rebase --autostash\` (another session may be pushing to main concurrently).
8. \`git push\`
9. Run \`node bin/cli.js list >/dev/null\` to confirm the CLI still parses every role.

Report via structured output: group, final added_slugs (after any drops), lint_clean (true once 0 errors), committed, pushed, commit_sha, notes on anything fixed or dropped.`
}

phase('Draft')
log(`Group ${group}: drafting ${targets.length} roles`)
const drafted = (await parallel(targets.map(t => () =>
  agent(draftPrompt(t), { label: `${group}:${t.code}`, schema: DRAFT_SCHEMA, agentType: 'general-purpose' })
))).filter(Boolean)

const added = drafted.filter(d => d.status === 'added')
const skipped = drafted.filter(d => d.status === 'skipped')
log(`Group ${group}: ${added.length} added, ${skipped.length} skipped, ${targets.length - drafted.length} agent failures`)

phase('Ops')
let ops = null
if (added.length > 0) {
  ops = await agent(opsPrompt(group, added), { label: `ops:${group}`, schema: OPS_SCHEMA, agentType: 'general-purpose' })
  log(`Group ${group} ops: lint_clean=${ops?.lint_clean} pushed=${ops?.pushed} sha=${ops?.commit_sha}`)
} else {
  log(`Group ${group}: nothing to commit`)
}

return { group, drafted, ops }
```

## Remaining group payloads (`args` for the Workflow call)

### Group 49 (2)
```json
[{"code": "49-9098.00", "title": "Helpers--Installation, Maintenance, and Repair Workers", "group": "49"}, {"code": "49-9099.01", "title": "Geothermal Technicians", "group": "49"}]
```

### Group 43 (3)
```json
[{"code": "43-2011.00", "title": "Switchboard Operators, Including Answering Service", "group": "43"}, {"code": "43-4161.00", "title": "Human Resources Assistants, Except Payroll and Timekeeping", "group": "43"}, {"code": "43-5011.01", "title": "Freight Forwarders", "group": "43"}]
```

### Group 53 (3)
```json
[{"code": "53-1042.00", "title": "First-Line Supervisors of Helpers, Laborers, and Material Movers, Hand", "group": "53"}, {"code": "53-1044.00", "title": "First-Line Supervisors of Passenger Attendants", "group": "53"}, {"code": "53-6051.00", "title": "Transportation Inspectors", "group": "53"}]
```

### Group 33 (17)
```json
[{"code": "33-1011.00", "title": "First-Line Supervisors of Correctional Officers", "group": "33"}, {"code": "33-1012.00", "title": "First-Line Supervisors of Police and Detectives", "group": "33"}, {"code": "33-1021.00", "title": "First-Line Supervisors of Firefighting and Prevention Workers", "group": "33"}, {"code": "33-1091.00", "title": "First-Line Supervisors of Security Workers", "group": "33"}, {"code": "33-2022.00", "title": "Forest Fire Inspectors and Prevention Specialists", "group": "33"}, {"code": "33-3011.00", "title": "Bailiffs", "group": "33"}, {"code": "33-3021.02", "title": "Police Identification and Records Officers", "group": "33"}, {"code": "33-3041.00", "title": "Parking Enforcement Workers", "group": "33"}, {"code": "33-3052.00", "title": "Transit and Railroad Police", "group": "33"}, {"code": "33-9011.00", "title": "Animal Control Workers", "group": "33"}, {"code": "33-9031.00", "title": "Gambling Surveillance Officers and Gambling Investigators", "group": "33"}, {"code": "33-9032.00", "title": "Security Guards", "group": "33"}, {"code": "33-9091.00", "title": "Crossing Guards and Flaggers", "group": "33"}, {"code": "33-9092.00", "title": "Lifeguards, Ski Patrol, and Other Recreational Protective Service Workers", "group": "33"}, {"code": "33-9093.00", "title": "Transportation Security Screeners", "group": "33"}, {"code": "33-9094.00", "title": "School Bus Monitors", "group": "33"}, {"code": "33-9099.02", "title": "Retail Loss Prevention Specialists", "group": "33"}]
```

### Group 41 (15)
```json
[{"code": "41-1011.00", "title": "First-Line Supervisors of Retail Sales Workers", "group": "41"}, {"code": "41-1012.00", "title": "First-Line Supervisors of Non-Retail Sales Workers", "group": "41"}, {"code": "41-2011.00", "title": "Cashiers", "group": "41"}, {"code": "41-2012.00", "title": "Gambling Change Persons and Booth Cashiers", "group": "41"}, {"code": "41-2021.00", "title": "Counter and Rental Clerks", "group": "41"}, {"code": "41-2022.00", "title": "Parts Salespersons", "group": "41"}, {"code": "41-2031.00", "title": "Retail Salespersons", "group": "41"}, {"code": "41-3091.00", "title": "Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel", "group": "41"}, {"code": "41-4011.07", "title": "Solar Sales Representatives and Assessors", "group": "41"}, {"code": "41-4012.00", "title": "Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products", "group": "41"}, {"code": "41-9011.00", "title": "Demonstrators and Product Promoters", "group": "41"}, {"code": "41-9012.00", "title": "Models", "group": "41"}, {"code": "41-9022.00", "title": "Real Estate Sales Agents", "group": "41"}, {"code": "41-9041.00", "title": "Telemarketers", "group": "41"}, {"code": "41-9091.00", "title": "Door-to-Door Sales Workers, News and Street Vendors, and Related Workers", "group": "41"}]
```

### Group 39 (22)
```json
[{"code": "39-1013.00", "title": "First-Line Supervisors of Gambling Services Workers", "group": "39"}, {"code": "39-1014.00", "title": "First-Line Supervisors of Entertainment and Recreation Workers, Except Gambling Services", "group": "39"}, {"code": "39-1022.00", "title": "First-Line Supervisors of Personal Service Workers", "group": "39"}, {"code": "39-2021.00", "title": "Animal Caretakers", "group": "39"}, {"code": "39-3011.00", "title": "Gambling Dealers", "group": "39"}, {"code": "39-3012.00", "title": "Gambling and Sports Book Writers and Runners", "group": "39"}, {"code": "39-3021.00", "title": "Motion Picture Projectionists", "group": "39"}, {"code": "39-3031.00", "title": "Ushers, Lobby Attendants, and Ticket Takers", "group": "39"}, {"code": "39-3091.00", "title": "Amusement and Recreation Attendants", "group": "39"}, {"code": "39-3092.00", "title": "Costume Attendants", "group": "39"}, {"code": "39-3093.00", "title": "Locker Room, Coatroom, and Dressing Room Attendants", "group": "39"}, {"code": "39-4012.00", "title": "Crematory Operators", "group": "39"}, {"code": "39-4021.00", "title": "Funeral Attendants", "group": "39"}, {"code": "39-5011.00", "title": "Barbers", "group": "39"}, {"code": "39-5091.00", "title": "Makeup Artists, Theatrical and Performance", "group": "39"}, {"code": "39-5092.00", "title": "Manicurists and Pedicurists", "group": "39"}, {"code": "39-5093.00", "title": "Shampooers", "group": "39"}, {"code": "39-6011.00", "title": "Baggage Porters and Bellhops", "group": "39"}, {"code": "39-7012.00", "title": "Travel Guides", "group": "39"}, {"code": "39-9011.01", "title": "Nannies", "group": "39"}, {"code": "39-9032.00", "title": "Recreation Workers", "group": "39"}, {"code": "39-9041.00", "title": "Residential Advisors", "group": "39"}]
```

### Group 47 (36)
```json
[{"code": "47-1011.03", "title": "Solar Energy Installation Managers", "group": "47"}, {"code": "47-2041.00", "title": "Carpet Installers", "group": "47"}, {"code": "47-2042.00", "title": "Floor Layers, Except Carpet, Wood, and Hard Tiles", "group": "47"}, {"code": "47-2043.00", "title": "Floor Sanders and Finishers", "group": "47"}, {"code": "47-2053.00", "title": "Terrazzo Workers and Finishers", "group": "47"}, {"code": "47-2071.00", "title": "Paving, Surfacing, and Tamping Equipment Operators", "group": "47"}, {"code": "47-2072.00", "title": "Pile Driver Operators", "group": "47"}, {"code": "47-2082.00", "title": "Tapers", "group": "47"}, {"code": "47-2131.00", "title": "Insulation Workers, Floor, Ceiling, and Wall", "group": "47"}, {"code": "47-2132.00", "title": "Insulation Workers, Mechanical", "group": "47"}, {"code": "47-2142.00", "title": "Paperhangers", "group": "47"}, {"code": "47-2152.04", "title": "Solar Thermal Installers and Technicians", "group": "47"}, {"code": "47-3011.00", "title": "Helpers--Brickmasons, Blockmasons, Stonemasons, and Tile and Marble Setters", "group": "47"}, {"code": "47-3012.00", "title": "Helpers--Carpenters", "group": "47"}, {"code": "47-3013.00", "title": "Helpers--Electricians", "group": "47"}, {"code": "47-3014.00", "title": "Helpers--Painters, Paperhangers, Plasterers, and Stucco Masons", "group": "47"}, {"code": "47-3015.00", "title": "Helpers--Pipelayers, Plumbers, Pipefitters, and Steamfitters", "group": "47"}, {"code": "47-3016.00", "title": "Helpers--Roofers", "group": "47"}, {"code": "47-4011.01", "title": "Energy Auditors", "group": "47"}, {"code": "47-4051.00", "title": "Highway Maintenance Workers", "group": "47"}, {"code": "47-4061.00", "title": "Rail-Track Laying and Maintenance Equipment Operators", "group": "47"}, {"code": "47-4071.00", "title": "Septic Tank Servicers and Sewer Pipe Cleaners", "group": "47"}, {"code": "47-4091.00", "title": "Segmental Pavers", "group": "47"}, {"code": "47-4099.03", "title": "Weatherization Installers and Technicians", "group": "47"}, {"code": "47-5011.00", "title": "Derrick Operators, Oil and Gas", "group": "47"}, {"code": "47-5012.00", "title": "Rotary Drill Operators, Oil and Gas", "group": "47"}, {"code": "47-5013.00", "title": "Service Unit Operators, Oil and Gas", "group": "47"}, {"code": "47-5022.00", "title": "Excavating and Loading Machine and Dragline Operators, Surface Mining", "group": "47"}, {"code": "47-5023.00", "title": "Earth Drillers, Except Oil and Gas", "group": "47"}, {"code": "47-5032.00", "title": "Explosives Workers, Ordnance Handling Experts, and Blasters", "group": "47"}, {"code": "47-5041.00", "title": "Continuous Mining Machine Operators", "group": "47"}, {"code": "47-5043.00", "title": "Roof Bolters, Mining", "group": "47"}, {"code": "47-5044.00", "title": "Loading and Moving Machine Operators, Underground Mining", "group": "47"}, {"code": "47-5051.00", "title": "Rock Splitters, Quarry", "group": "47"}, {"code": "47-5071.00", "title": "Roustabouts, Oil and Gas", "group": "47"}, {"code": "47-5081.00", "title": "Helpers--Extraction Workers", "group": "47"}]
```

### Group 51 (63) — biggest, do last
```json
[{"code": "51-1011.00", "title": "First-Line Supervisors of Production and Operating Workers", "group": "51"}, {"code": "51-2011.00", "title": "Aircraft Structure, Surfaces, Rigging, and Systems Assemblers", "group": "51"}, {"code": "51-2021.00", "title": "Coil Winders, Tapers, and Finishers", "group": "51"}, {"code": "51-2022.00", "title": "Electrical and Electronic Equipment Assemblers", "group": "51"}, {"code": "51-2023.00", "title": "Electromechanical Equipment Assemblers", "group": "51"}, {"code": "51-2031.00", "title": "Engine and Other Machine Assemblers", "group": "51"}, {"code": "51-2051.00", "title": "Fiberglass Laminators and Fabricators", "group": "51"}, {"code": "51-2061.00", "title": "Timing Device Assemblers and Adjusters", "group": "51"}, {"code": "51-2092.00", "title": "Team Assemblers", "group": "51"}, {"code": "51-3022.00", "title": "Meat, Poultry, and Fish Cutters and Trimmers", "group": "51"}, {"code": "51-3023.00", "title": "Slaughterers and Meat Packers", "group": "51"}, {"code": "51-3092.00", "title": "Food Batchmakers", "group": "51"}, {"code": "51-3093.00", "title": "Food Cooking Machine Operators and Tenders", "group": "51"}, {"code": "51-4022.00", "title": "Forging Machine Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4023.00", "title": "Rolling Machine Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4031.00", "title": "Cutting, Punching, and Press Machine Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4032.00", "title": "Drilling and Boring Machine Tool Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4034.00", "title": "Lathe and Turning Machine Tool Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4035.00", "title": "Milling and Planing Machine Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4052.00", "title": "Pourers and Casters, Metal", "group": "51"}, {"code": "51-4061.00", "title": "Model Makers, Metal and Plastic", "group": "51"}, {"code": "51-4062.00", "title": "Patternmakers, Metal and Plastic", "group": "51"}, {"code": "51-4072.00", "title": "Molding, Coremaking, and Casting Machine Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4081.00", "title": "Multiple Machine Tool Setters, Operators, and Tenders, Metal and Plastic", "group": "51"}, {"code": "51-4122.00", "title": "Welding, Soldering, and Brazing Machine Setters, Operators, and Tenders", "group": "51"}, {"code": "51-4192.00", "title": "Layout Workers, Metal and Plastic", "group": "51"}, {"code": "51-4194.00", "title": "Tool Grinders, Filers, and Sharpeners", "group": "51"}, {"code": "51-5111.00", "title": "Prepress Technicians and Workers", "group": "51"}, {"code": "51-5113.00", "title": "Print Binding and Finishing Workers", "group": "51"}, {"code": "51-6011.00", "title": "Laundry and Dry-Cleaning Workers", "group": "51"}, {"code": "51-6021.00", "title": "Pressers, Textile, Garment, and Related Materials", "group": "51"}, {"code": "51-6031.00", "title": "Sewing Machine Operators", "group": "51"}, {"code": "51-6041.00", "title": "Shoe and Leather Workers and Repairers", "group": "51"}, {"code": "51-6042.00", "title": "Shoe Machine Operators and Tenders", "group": "51"}, {"code": "51-6051.00", "title": "Sewers, Hand", "group": "51"}, {"code": "51-6063.00", "title": "Textile Knitting and Weaving Machine Setters, Operators, and Tenders", "group": "51"}, {"code": "51-6064.00", "title": "Textile Winding, Twisting, and Drawing Out Machine Setters, Operators, and Tenders", "group": "51"}, {"code": "51-7031.00", "title": "Model Makers, Wood", "group": "51"}, {"code": "51-7032.00", "title": "Patternmakers, Wood", "group": "51"}, {"code": "51-7041.00", "title": "Sawing Machine Setters, Operators, and Tenders, Wood", "group": "51"}, {"code": "51-7042.00", "title": "Woodworking Machine Setters, Operators, and Tenders, Except Sawing", "group": "51"}, {"code": "51-8012.00", "title": "Power Distributors and Dispatchers", "group": "51"}, {"code": "51-8013.03", "title": "Biomass Plant Technicians", "group": "51"}, {"code": "51-8013.04", "title": "Hydroelectric Plant Technicians", "group": "51"}, {"code": "51-8031.00", "title": "Water and Wastewater Treatment Plant and System Operators", "group": "51"}, {"code": "51-8092.00", "title": "Gas Plant Operators", "group": "51"}, {"code": "51-8093.00", "title": "Petroleum Pump System Operators, Refinery Operators, and Gaugers", "group": "51"}, {"code": "51-8099.01", "title": "Biofuels Processing Technicians", "group": "51"}, {"code": "51-9011.00", "title": "Chemical Equipment Operators and Tenders", "group": "51"}, {"code": "51-9022.00", "title": "Grinding and Polishing Workers, Hand", "group": "51"}, {"code": "51-9031.00", "title": "Cutters and Trimmers, Hand", "group": "51"}, {"code": "51-9041.00", "title": "Extruding, Forming, Pressing, and Compacting Machine Setters, Operators, and Tenders", "group": "51"}, {"code": "51-9051.00", "title": "Furnace, Kiln, Oven, Drier, and Kettle Operators and Tenders", "group": "51"}, {"code": "51-9061.00", "title": "Inspectors, Testers, Sorters, Samplers, and Weighers", "group": "51"}, {"code": "51-9071.06", "title": "Gem and Diamond Workers", "group": "51"}, {"code": "51-9123.00", "title": "Painting, Coating, and Decorating Workers", "group": "51"}, {"code": "51-9141.00", "title": "Semiconductor Processing Technicians", "group": "51"}, {"code": "51-9161.00", "title": "Computer Numerically Controlled Tool Operators", "group": "51"}, {"code": "51-9192.00", "title": "Cleaning, Washing, and Metal Pickling Equipment Operators and Tenders", "group": "51"}, {"code": "51-9195.00", "title": "Molders, Shapers, and Casters, Except Metal and Plastic", "group": "51"}, {"code": "51-9195.03", "title": "Stone Cutters and Carvers, Manufacturing", "group": "51"}, {"code": "51-9196.00", "title": "Paper Goods Machine Setters, Operators, and Tenders", "group": "51"}, {"code": "51-9198.00", "title": "Helpers--Production Workers", "group": "51"}]
```

## Release

After finishing (or after any meaningful batch), bump `package.json` version (minor for role batches), commit, `git tag v<version>`, `git push origin v<version>` — triggers the npm publish GitHub Action automatically (OIDC trusted publishing, no manual `npm publish` needed). Last release this pass: `v0.5.0`.
