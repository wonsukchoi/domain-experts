export const meta = {
  name: 'scan-project',
  description: 'Read a target project and propose domain-expert skills it would benefit from',
  phases: [
    { title: 'Scan', detail: 'stack, README, structure, recent history — read-only' },
    { title: 'Synthesize', detail: 'propose candidate needs, cross-check against existing roles' },
  ],
}

const projectPath = args && args.projectPath
if (!projectPath || typeof projectPath !== 'string') {
  throw new Error('scan-project requires {projectPath: "<absolute path to the project to scan>"} as args')
}

phase('Scan')

const PROFILE_SCHEMA = {
  type: 'object',
  properties: {
    stack: { type: 'array', items: { type: 'string' } },
    domain_signals: { type: 'array', items: { type: 'string' } },
    maturity: { type: 'string', enum: ['early', 'growing', 'mature'] },
    notable_dirs: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['stack', 'domain_signals', 'maturity', 'notable_dirs', 'summary'],
}

const profile = await agent(
  `Read-only reconnaissance of the project at ${JSON.stringify(projectPath)}. Do NOT write or edit anything there.\n` +
  `1) Stack: check for package.json/requirements.txt/pyproject.toml/Cargo.toml/go.mod/Gemfile/*.csproj (whichever exist) and read them.\n` +
  `2) Read the top of README.md if present — just the pitch/description, not the whole file.\n` +
  `3) List the directory structure 2-3 levels deep, skipping node_modules/.git/build artifacts/vendor dirs.\n` +
  `4) If it's a git repo, run \`git log --oneline -30\` inside it for feature/domain hints.\n` +
  `5) Check for CONTRIBUTING.md or docs/ for team-size or process hints.\n` +
  `Return a project profile: stack (list of technologies), domain_signals (short phrases hinting at the business/industry ` +
  `domain, e.g. "payments", "2D mobile game", "internal admin tool"), maturity (early/growing/mature — judged from commit ` +
  `volume, test coverage presence, CI config presence), notable_dirs (a handful of directories that best signal what the ` +
  `project actually does), and a 2-4 sentence summary. This profile is internal working data only — it will not be saved ` +
  `anywhere outside this conversation.`,
  { label: 'scan', schema: PROFILE_SCHEMA }
)

log(`Scanned ${projectPath}: ${profile.summary}`)

phase('Synthesize')

const SUGGESTIONS_SCHEMA = {
  type: 'object',
  properties: {
    suggestions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          need: { type: 'string', description: 'a free-text need statement, phrased the way a user would ask for an agent role' },
          rationale: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['need', 'rationale', 'confidence'],
      },
    },
  },
  required: ['suggestions'],
}

const raw = await agent(
  `A project was scanned with this profile:\n${JSON.stringify(profile, null, 2)}\n\n` +
  `In the domain-experts repo, read data/roles.json to see what expert roles already exist (slug + description), so you ` +
  `don't propose needs that duplicate well-covered ground.\n\n` +
  `Propose 3-7 candidate need-statements for domain-expert agent skills this specific project would benefit from — not ` +
  `generic ("a developer") but specific to what the profile actually shows (stack, domain signals, maturity). Each ` +
  `need should be phrased the way a user would ask for it, e.g. "agent for 2D mobile puzzle game dev" or "agent for a ` +
  `Stripe-based subscription billing system". For each, give a one-sentence rationale tying it to a specific signal in ` +
  `the profile (not a generic justification) and a confidence level.`,
  { label: 'synthesize:propose', schema: SUGGESTIONS_SCHEMA }
)

const enriched = await parallel((raw.suggestions || []).map(s => () =>
  agent(
    `In the domain-experts repo root, run: node bin/cli.js match ${JSON.stringify(s.need)} --json\n` +
    `Parse stdout as JSON. Return cli_confident (its "confident" field) and cli_best_slug (its "best.slug" field, or null).`,
    {
      label: `synthesize:match:${s.need.slice(0, 30)}`,
      schema: {
        type: 'object',
        properties: { cli_confident: { type: 'boolean' }, cli_best_slug: { type: ['string', 'null'] } },
        required: ['cli_confident', 'cli_best_slug'],
      },
    }
  ).then(m => ({ ...s, ...m }))
))

const suggestions = enriched.filter(Boolean)
log(`Proposed ${suggestions.length} candidate need(s).`)

return { profile, suggestions }
