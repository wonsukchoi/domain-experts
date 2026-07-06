export const meta = {
  name: 'audit-roles',
  description: 'Re-score a batch of shipped domain-expert roles against AUTHORING.md and flag/deprecate stale ones',
  phases: [
    { title: 'Select', detail: 'pick the batch: oldest-audited status:active roles' },
    { title: 'Audit', detail: 'per-role source-currency check + fresh Pass 4 rescore' },
    { title: 'Report', detail: 'stamp frontmatter, open one PR for refresh/deprecate flags' },
  ],
}

const batchSize = (args && args.batchSize) || 10

phase('Select')

const SELECT_SCHEMA = {
  type: 'object',
  properties: { slugs: { type: 'array', items: { type: 'string' } } },
  required: ['slugs'],
}

const selection = await agent(
  `In the domain-experts repo root, read data/roles.json. Filter to roles whose status is "active" or absent/null. ` +
  `Sort ascending by last_audited (roles with no last_audited first, then oldest date next). Return the first ` +
  `${batchSize} slugs.`,
  { label: 'select', schema: SELECT_SCHEMA }
)

if (!selection.slugs.length) {
  log('No active roles due for audit.')
  return { status: 'noop', audited: 0 }
}

log(`Auditing ${selection.slugs.length} roles: ${selection.slugs.join(', ')}`)

phase('Audit')

const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    total: { type: 'number' },
    stale_sources: { type: 'boolean' },
    stale_notes: { type: 'string' },
    defects: { type: 'array', items: { type: 'string' } },
  },
  required: ['total', 'stale_sources', 'defects'],
}

const audited = await pipeline(
  selection.slugs,
  slug => agent(
    `Audit roles/${slug}/ in the domain-experts repo: read SKILL.md and every references/*.md file.\n` +
    `1) Sources section — are the named standards/books/postmortems still current, or superseded since this was drafted?\n` +
    `2) Fresh score against AUTHORING.md's 9-criterion/18-point rubric (Specificity, Dedup, Worked example, Heuristics, ` +
    `Red flags, Vocabulary, Sources, Non-derivability, Harness match) as if reviewing it cold — do not assume it still ` +
    `deserves its original score.\n` +
    `3) Re-apply AUTHORING.md's banned-pattern list — it may have grown since this role was drafted.\n` +
    `Return total (0-18), stale_sources (bool), stale_notes (what changed, if stale), and defects (short list, empty if none).`,
    { label: `audit:${slug}`, phase: 'Audit', schema: AUDIT_SCHEMA }
  ).then(result => ({ slug, result }))
)

phase('Report')

const stamped = []
const flagged = []
for (const item of audited.filter(Boolean)) {
  const { slug, result } = item
  if (result.total < 14 || result.stale_sources) {
    flagged.push({ slug, score: result.total, defects: result.defects, staleNotes: result.stale_notes })
  } else {
    stamped.push({ slug, score: result.total })
  }
}

// No separate failure counter is stored — a role already flagged needs-refresh
// that fails again is the second consecutive failure, so it deprecates.
const statusChecks = await parallel(flagged.map(f => () =>
  agent(
    `In the domain-experts repo, read roles/${f.slug}/SKILL.md frontmatter. Return true if status is currently ` +
    `"needs-refresh", else false.`,
    {
      label: `check-status:${f.slug}`,
      schema: { type: 'object', properties: { alreadyFlagged: { type: 'boolean' } }, required: ['alreadyFlagged'] },
    }
  ).then(r => ({ ...f, alreadyFlagged: r.alreadyFlagged }))
))

const toRefresh = statusChecks.filter(Boolean).filter(f => !f.alreadyFlagged)
const toDeprecate = statusChecks.filter(Boolean).filter(f => f.alreadyFlagged)

if (!stamped.length && !toRefresh.length && !toDeprecate.length) {
  log('Audit batch complete — nothing to change.')
  return { status: 'noop', audited: selection.slugs.length }
}

const pr = await agent(
  `In the domain-experts repo root, on a new branch \`audit/roles-batch\`:\n` +
  `1) For these roles, set frontmatter last_audited to today's date (YYYY-MM-DD, via \`date +%F\`) and audit_score to ` +
  `the given score, keep status "active": ${JSON.stringify(stamped)}\n` +
  `2) For these roles, stamp last_audited/audit_score and set status "needs-refresh" (first failed audit): ` +
  `${JSON.stringify(toRefresh)}\n` +
  `3) For these roles, set status "deprecated" and \`git mv\` the whole directory from roles/<slug>/ to ` +
  `roles/_deprecated/<slug>/ (second consecutive failed audit): ${JSON.stringify(toDeprecate)}\n` +
  `Then run \`python3 scripts/generate_roadmap.py\`, \`python3 scripts/lint_roles.py\`, \`python3 scripts/check_links.py\` ` +
  `— fix any new lint errors your own edits introduced (deprecated roles are excluded from lint's default sweep once ` +
  `moved out of roles/, so no fix should be needed there). Stage everything, commit as ` +
  `${JSON.stringify(`audit: refresh ${selection.slugs.length} roles (${toRefresh.length} needs-refresh, ${toDeprecate.length} deprecated)`)}, ` +
  `\`git pull --rebase --autostash origin main\`, push the branch, and open a PR via \`gh pr create\` with each ` +
  `flagged role's defects/stale-notes in the body. Never commit or push directly to main. Return the PR URL.`,
  { label: 'report:pr', phase: 'Report' }
)

return { status: 'done', stamped, toRefresh, toDeprecate, pr }
