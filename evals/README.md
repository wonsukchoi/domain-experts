# Evals — proving the counterfactual test

AUTHORING.md's second ship test says: *an agent loaded with the role makes different, better decisions than the same agent without it.* This harness measures that instead of asserting it.

## How it works

For each scenario in `scenarios/<role-slug>.json`:

1. **Baseline arm** — the model gets only a generic instruction ("You are an experienced `<role>`") plus the task.
2. **Skill arm** — the model gets the role's full `SKILL.md` as context plus the same task.
3. **Blind judge** — a separate model call sees both responses in randomized A/B order (it never knows which arm is which) and checks each of the scenario's observable criteria: which response satisfies it (A / B / both / neither).

A criterion is written as an observable behavior a practitioner would show ("flags that flat deferred revenue contradicts the bookings growth story"), never as vibes ("sounds professional"). The skill wins a scenario when it satisfies strictly more criteria than baseline.

## Run

Requires the `claude` CLI by default (any agent CLI following the `--model <m> -p <prompt>` convention works with `--cmd`). `--backend` swaps the whole invocation style instead:

```sh
python3 evals/run_evals.py                         # all scenarios, all roles
python3 evals/run_evals.py financial-manager       # one role
python3 evals/run_evals.py financial-manager --only fm-1
python3 evals/run_evals.py --model claude-haiku-4-5-20251001   # cheaper runs

# Other backends — same scenarios, same judge logic, different model under test:
python3 evals/run_evals.py --backend ollama --model llama3.1        # local model via `ollama run`
OPENAI_API_KEY=sk-... python3 evals/run_evals.py --backend openai --model gpt-4o-mini
```

Results land in `evals/results/<UTC timestamp>.json` plus a printed summary table. Results are point-in-time measurements against a specific model — they are **not** committed as ongoing truth; re-run when roles or models change.

## Adding scenarios

3–5 per role, in `scenarios/<role-slug>.json`:

```json
{
  "role": "financial-manager",
  "scenarios": [
    {
      "id": "fm-1",
      "task": "the situation + ask, written like a real user would",
      "criteria": [
        "observable expert behavior 1",
        "observable expert behavior 2"
      ]
    }
  ]
}
```

Good criteria come straight from the role's red-flags and worked example — the things the SKILL.md explicitly teaches. If a criterion isn't taught by the role file, the eval is testing the model, not the skill.
