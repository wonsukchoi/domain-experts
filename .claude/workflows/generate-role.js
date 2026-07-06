export const meta = {
  name: 'generate-role',
  description: 'Resolve a free-text need to an existing/new domain-expert role and draft it via the AUTHORING.md Pass 0-4 pipeline',
  phases: [
    { title: 'Resolve', detail: 'match existing roles, judge granularity' },
    { title: 'Research', detail: 'Pass 0 — gather named sources and numbers' },
    { title: 'Draft', detail: 'Pass 1 — write SKILL.md and references/ trio' },
    { title: 'Critique', detail: 'Pass 2/3 — adversarial review and revise, looped' },
    { title: 'Gate', detail: 'lint_roles.py, check_links.py, open PR' },
  ],
}

const need = args
if (!need || typeof need !== 'string') {
  throw new Error('generate-role requires a free-text need string as args, e.g. {args: "agent for 2D mobile puzzle game dev"}')
}

phase('Resolve')

const MATCH_SCHEMA = {
  type: 'object',
  properties: {
    confident: { type: 'boolean' },
    candidates: {
      type: 'array',
      items: {
        type: 'object',
        properties: { slug: { type: 'string' }, file: { type: 'string' }, score: { type: 'number' } },
        required: ['slug', 'file'],
      },
    },
  },
  required: ['confident', 'candidates'],
}

const matchResult = await agent(
  `In the domain-experts repo root, run: node bin/cli.js match ${JSON.stringify(need)} --json\n` +
  `Parse stdout as JSON. Return confident (bool) and up to 3 candidates as {slug, file, score} from the ` +
  `"best" and "candidates" fields of the CLI output ("file" is the SKILL.md path).`,
  { label: 'resolve:match', schema: MATCH_SCHEMA }
)

const GRANULARITY_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['use_existing', 'new_leaf', 'new_parent'] },
    slug: { type: 'string', description: 'existing slug to use, or the new kebab-case slug to create' },
    parent: { type: ['string', 'null'], description: 'parent slug when verdict is new_leaf, else null' },
    rationale: { type: 'string' },
  },
  required: ['verdict', 'slug', 'parent', 'rationale'],
}

const candidateBlock = (matchResult.candidates || []).map(c => `- ${c.slug} (${c.file})`).join('\n') || '(none found)'

const resolution = await agent(
  `A user needs an agent skill for: ${JSON.stringify(need)}\n\n` +
  `domain-experts CLI's closest matches (confident: ${matchResult.confident}):\n${candidateBlock}\n\n` +
  `Read each candidate's full SKILL.md in the domain-experts repo. Apply AUTHORING.md's three quality tests ` +
  `(practitioner-nod, counterfactual, non-derivability) to a GRANULARITY question, not a content question: would a ` +
  `practitioner doing exactly this need get WRONG guidance from the candidate's Decision framework, Tools & methods, ` +
  `or Worked example — not just "less detail," but decisions, tools, or failure modes that actually differ? ` +
  `If yes and a reasonable parent exists among the candidates, verdict "new_leaf" naming that candidate as parent. ` +
  `If yes and no reasonable parent exists, verdict "new_parent". Otherwise "use_existing" with the best candidate's slug. ` +
  `For new roles, propose a kebab-case slug consistent with existing roles/ directory naming. Return structured output.`,
  { label: 'resolve:granularity', schema: GRANULARITY_SCHEMA }
)

log(`Resolution: ${resolution.verdict} -> ${resolution.slug}${resolution.parent ? ` (parent: ${resolution.parent})` : ''}`)

if (resolution.verdict === 'use_existing') {
  return { status: 'use_existing', slug: resolution.slug, rationale: resolution.rationale }
}

phase('Research')

const parentContext = resolution.parent
  ? await agent(
      `In the domain-experts repo, read roles/${resolution.parent}/SKILL.md and its references/*.md files in full. ` +
      `Return their combined text verbatim, nothing else.`,
      { label: 'resolve:parent-context' }
    )
  : ''

const research = await agent(
  `Pass 0 Research per AUTHORING.md's "LLM drafting pipeline" section, for a new domain-experts role "${resolution.slug}" ` +
  `covering: ${need}\n` +
  (resolution.parent
    ? `This is a specialization leaf under parent role "${resolution.parent}". Shared context from the parent (for consistency, not for copying):\n${parentContext}\n`
    : '') +
  `Collect 5+ named sources (practitioner books, standards docs, postmortems, well-regarded forum/community threads, ` +
  `O*NET task lists as a coverage skeleton ONLY — O*NET text itself is generic and must not appear verbatim in the draft). ` +
  `Output source notes with harvested numbers, thresholds, named positions, and war stories. If you find no concrete ` +
  `numbers, say so explicitly rather than inventing any.`,
  { label: 'research', phase: 'Research' }
)

phase('Draft')

const skillDraft = await agent(
  `In the domain-experts repo, read AUTHORING.md and TEMPLATE.md in full, then read one gold-standard example role of ` +
  `matching shape (pick the closest from financial-manager, lawyer-contracts, product-manager, data-scientist, ` +
  `marketing-strategist). Pass 1 Draft: write roles/${resolution.slug}/SKILL.md to spec — frontmatter: name: ${resolution.slug}, ` +
  `spec: 2, maturity: draft, status: active${resolution.parent ? `, parent: ${resolution.parent}` : ''}, a category from ` +
  `AUTHORING.md's allowed set, and a description naming concrete task types.\n\n` +
  `Pass 0 research notes:\n${research}\n\n` +
  `Every claim must trace to the research notes or be flagged [heuristic — needs practitioner check]. Follow the dedup ` +
  `rule (each idea stated exactly once, in the section where it does the most work) and the banned-pattern list. Write ` +
  `the file with the Write tool. Return the final file contents.`,
  { label: 'draft:skill', phase: 'Draft' }
)

await agent(
  `In the domain-experts repo, read roles/${resolution.slug}/SKILL.md (just written) plus AUTHORING.md's references/ file ` +
  `specs. Pass 1 Draft: write the deep-dive file under roles/${resolution.slug}/references/ — playbook.md if the role's ` +
  `output is executed processes, artifacts.md if it's documents/models (see AUTHORING.md's naming rule). Fill it with real ` +
  `template structures, plausible example numbers, and step sequences with thresholds — never descriptions of examples. ` +
  `Use the Write tool.`,
  { label: 'draft:deepdive', phase: 'Draft' }
)

await agent(
  `In the domain-experts repo, read roles/${resolution.slug}/SKILL.md. Pass 1 Draft: write ` +
  `roles/${resolution.slug}/references/red-flags.md — 7-14 flags, each with AUTHORING.md's exact four fields (a signal ` +
  `with a numeric threshold, Usually means, First question, Data to pull). Use the Write tool.`,
  { label: 'draft:red-flags', phase: 'Draft' }
)

await agent(
  `In the domain-experts repo, read roles/${resolution.slug}/SKILL.md. Pass 1 Draft: write ` +
  `roles/${resolution.slug}/references/vocabulary.md — 8-17 terms of art generalists misuse (not terms they could just ` +
  `look up), each with a definition, an "in use:" example sentence, and a misuse note. Use the Write tool.`,
  { label: 'draft:vocabulary', phase: 'Draft' }
)

phase('Critique')

const SCORE_SCHEMA = {
  type: 'object',
  properties: {
    total: { type: 'number' },
    criteria: {
      type: 'array',
      items: { type: 'object', properties: { name: { type: 'string' }, points: { type: 'number' } }, required: ['name', 'points'] },
    },
    verdict: { type: 'string', enum: ['ship', 'revise', 'abandon'] },
  },
  required: ['total', 'criteria', 'verdict'],
}

// AUTHORING.md caps revision at 2 loops back to Pass 2 — 3 score attempts total, revise after the first two only.
let scored = null
for (let loopIdx = 0; loopIdx < 3; loopIdx++) {
  const critique = await agent(
    `Fresh adversarial review of roles/${resolution.slug}/ in the domain-experts repo against AUTHORING.md's Pass 2 ` +
    `checklist: (a) quote every sentence derivable from the role title alone; (b) find every idea stated more than once; ` +
    `(c) recompute all worked-example arithmetic; (d) check every red flag has all four fields; (e) apply the ` +
    `banned-pattern list. Read every file in roles/${resolution.slug}/ first. Output a numbered defect list.`,
    { label: `critique:${loopIdx}`, phase: 'Critique' }
  )

  if (loopIdx < 2) {
    await agent(
      `In the domain-experts repo, revise roles/${resolution.slug}/ to fix every defect below, or explicitly contest a ` +
      `defect with a one-line reason instead of silently ignoring it:\n${critique}\nEdit the files directly.`,
      { label: `revise:${loopIdx}`, phase: 'Critique' }
    )
  }

  scored = await agent(
    `Fresh score of roles/${resolution.slug}/ in the domain-experts repo against AUTHORING.md's 9-criterion/18-point ` +
    `rubric (Specificity, Dedup, Worked example, Heuristics, Red flags, Vocabulary, Sources, Non-derivability, Harness ` +
    `match). Read every file first, score each 0/1/2, sum. Verdict "ship" if total>=14 and no criterion is 0, "revise" ` +
    `if fixable, "abandon" if fundamentally generic or lacking real sources.`,
    { label: `score:${loopIdx}`, schema: SCORE_SCHEMA, phase: 'Critique' }
  )

  log(`Pass 4 score (loop ${loopIdx}): ${scored.total}/18 — ${scored.verdict}`)
  if (scored.verdict === 'ship' || scored.verdict === 'abandon') break
}

if (!scored || scored.verdict !== 'ship') {
  log(`Abandoning ${resolution.slug} — never reached ship threshold (last: ${scored ? scored.total : 0}/18). ` +
      `Per AUTHORING.md: an unfilled slot is recoverable, a shipped-generic role is not.`)
  return { status: 'abandoned', slug: resolution.slug, score: scored ? scored.total : 0, detail: scored }
}

phase('Gate')

await agent(
  `In the domain-experts repo root: run \`git add roles/${resolution.slug}\`, then \`python3 scripts/lint_roles.py ` +
  `${resolution.slug}\`, then \`python3 scripts/check_links.py\`. If lint has any ERROR, fix it and re-run until 0 ` +
  `errors. Then run \`python3 scripts/generate_roadmap.py\` and \`git add -A\`. Do NOT commit. Report the final lint ` +
  `and generate_roadmap.py output verbatim.`,
  { label: 'gate:lint', phase: 'Gate' }
)

const pr = await agent(
  `In the domain-experts repo root, checked-out on main with the new role already staged: create branch ` +
  `\`role/${resolution.slug}\`, commit as ${JSON.stringify(`role: add ${resolution.slug}` + (resolution.parent ? ` (leaf of ${resolution.parent})` : ''))}, ` +
  `\`git pull --rebase --autostash origin main\`, push the branch, and open a PR via \`gh pr create\` with the rubric ` +
  `score (${scored.total}/18) and this resolution rationale in the body: ${JSON.stringify(resolution.rationale)}. Never ` +
  `push or commit directly to main. Return the PR URL.`,
  { label: 'gate:pr', phase: 'Gate' }
)

return { status: 'shipped', slug: resolution.slug, parent: resolution.parent, score: scored.total, pr }
