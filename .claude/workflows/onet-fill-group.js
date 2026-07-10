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
5. \`git add -A\`
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
