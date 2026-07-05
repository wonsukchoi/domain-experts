#!/usr/bin/env python3
"""
Run skill-vs-baseline evals. See evals/README.md.

Usage:
    python3 evals/run_evals.py [role-slug ...] [--only <scenario-id>]
                               [--model <model>] [--cmd <agent command>]

For each scenario, produces a baseline response (generic expert prompt) and
a skill response (SKILL.md as context), then a blind judge scores both
against the scenario's observable criteria in randomized A/B order.
"""

import argparse
import datetime
import json
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENARIOS = Path(__file__).resolve().parent / "scenarios"
RESULTS = Path(__file__).resolve().parent / "results"

JUDGE_PROMPT = """You are a strict grader comparing two anonymous responses to the same professional scenario.

SCENARIO:
{task}

RESPONSE A:
{a}

RESPONSE B:
{b}

CRITERIA — for each, decide which response satisfies it: "A", "B", "both", or "neither".
Apply a STRICT standard:
- A criterion is satisfied only if the response explicitly does the specific behavior described — including any named check, number, ordering, or artifact the criterion mentions. Touching the topic generically does NOT count.
- "both" only when BOTH responses fully meet the strict standard. If one does it with specifics and the other gestures at it vaguely, credit only the specific one.
- When unsure, prefer "neither" over generous credit.
{criteria}

Then set "overall": which response would a 15-year practitioner in this field rate as the better professional answer — "A", "B", or "tie". Judge on decision quality and specificity, not length or formatting.

Reply with ONLY a JSON object, no prose, shaped exactly like:
{{"criteria": [{{"n": 1, "verdict": "A|B|both|neither"}}, ...], "overall": "A|B|tie"}}
"""


def run_agent(cmd, model, prompt, timeout=300):
    argv = list(cmd)
    if model:
        argv += ["--model", model]
    argv += ["-p", prompt]
    r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(f"{argv[0]} failed: {r.stderr[:500]}")
    return r.stdout.strip()


def judge(cmd, model, task, resp_a, resp_b, criteria):
    prompt = JUDGE_PROMPT.format(
        task=task,
        a=resp_a,
        b=resp_b,
        criteria="\n".join(f"{i+1}. {c}" for i, c in enumerate(criteria)),
    )
    out = run_agent(cmd, model, prompt)
    m = re.search(r"\{.*\}", out, re.DOTALL)
    if not m:
        raise ValueError(f"judge returned no JSON: {out[:300]}")
    return json.loads(m.group(0))


def run_scenario(cmd, model, judge_model, slug, skill_text, sc):
    role_title = slug.replace("-", " ")
    print(f"[{sc['id']}] running...", flush=True)
    baseline = run_agent(
        cmd, model,
        f"You are an experienced {role_title}. A colleague asks:\n\n{sc['task']}",
    )
    skilled = run_agent(
        cmd, model,
        "Adopt the following professional role definition completely — its "
        "principles, heuristics, red flags, and decision framework — and answer "
        f"the question at the end in that role.\n\n{skill_text}\n\n"
        f"A colleague asks:\n\n{sc['task']}",
    )

    # Blind, randomized order.
    skill_is_a = random.random() < 0.5
    a, b = (skilled, baseline) if skill_is_a else (baseline, skilled)
    j = judge(cmd, judge_model, sc["task"], a, b, sc["criteria"])
    verdicts = j["criteria"]

    skill_letter = "A" if skill_is_a else "B"
    base_letter = "B" if skill_is_a else "A"
    skill_hits = sum(1 for v in verdicts if v["verdict"] in (skill_letter, "both"))
    base_hits = sum(1 for v in verdicts if v["verdict"] in (base_letter, "both"))
    overall = j.get("overall", "tie")
    overall_side = ("skill" if overall == skill_letter
                    else "baseline" if overall == base_letter else "tie")
    if skill_hits != base_hits:
        winner = "skill" if skill_hits > base_hits else "baseline"
    else:
        winner = overall_side  # criteria tie -> practitioner-preference tiebreak
    result = {
        "id": sc["id"],
        "role": slug,
        "criteria_total": len(sc["criteria"]),
        "skill_hits": skill_hits,
        "baseline_hits": base_hits,
        "overall_preference": overall_side,
        "winner": winner,
        "verdicts": verdicts,
        "skill_was": skill_letter,
        "responses": {"baseline": baseline, "skill": skilled},
    }
    print(f"[{sc['id']}] skill {skill_hits}/{len(sc['criteria'])} vs baseline "
          f"{base_hits}/{len(sc['criteria'])}, pref={overall_side} -> {winner}")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roles", nargs="*", help="role slugs; default all with scenario files")
    ap.add_argument("--only", help="run a single scenario id")
    ap.add_argument("--model", default=None, help="model override passed to the agent CLI")
    ap.add_argument("--judge-model", default=None,
                    help="model for the judge (default: same as --model); use a stronger one")
    ap.add_argument("--workers", type=int, default=3, help="concurrent scenarios")
    ap.add_argument("--cmd", default="claude", help="agent CLI command (default: claude)")
    args = ap.parse_args()
    cmd = args.cmd.split()
    judge_model = args.judge_model or args.model

    files = sorted(SCENARIOS.glob("*.json"))
    if args.roles:
        files = [f for f in files if f.stem in args.roles]
    if not files:
        sys.exit("no scenario files matched")

    RESULTS.mkdir(exist_ok=True)
    jobs = []
    for f in files:
        spec = json.loads(f.read_text())
        slug = spec["role"]
        skill_text = (ROOT / "roles" / slug / "SKILL.md").read_text()
        for sc in spec["scenarios"]:
            if args.only and sc["id"] != args.only:
                continue
            jobs.append((slug, skill_text, sc))

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [
            ex.submit(run_scenario, cmd, args.model, judge_model, slug, skill_text, sc)
            for slug, skill_text, sc in jobs
        ]
        results = []
        for fut in futures:
            try:
                results.append(fut.result())
            except Exception as e:
                print(f"scenario failed: {e}", file=sys.stderr)

    if not results:
        sys.exit("no scenarios ran")

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS / f"{stamp}.json"
    out.write_text(json.dumps({"model": args.model, "results": results}, indent=2))

    wins = sum(1 for r in results if r["winner"] == "skill")
    ties = sum(1 for r in results if r["winner"] == "tie")
    print(f"\n{'scenario':<8} {'skill':>5} {'base':>5} {'pref':>9}  winner")
    for r in sorted(results, key=lambda x: x["id"]):
        print(f"{r['id']:<8} {r['skill_hits']:>5} {r['baseline_hits']:>5} "
              f"{r['overall_preference']:>9}  {r['winner']}")
    print(f"\nskill wins {wins}/{len(results)} (ties {ties}) — full output: {out}")


if __name__ == "__main__":
    main()
