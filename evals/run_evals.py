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

JUDGE_PROMPT = """You are grading two anonymous responses to the same professional scenario.

SCENARIO:
{task}

RESPONSE A:
{a}

RESPONSE B:
{b}

CRITERIA — for each, decide which response satisfies it: "A", "B", "both", or "neither".
Satisfying means the response actually does the behavior, not merely mentions the topic.
{criteria}

Reply with ONLY a JSON object, no prose, shaped exactly like:
{{"criteria": [{{"n": 1, "verdict": "A|B|both|neither"}}, ...]}}
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roles", nargs="*", help="role slugs; default all with scenario files")
    ap.add_argument("--only", help="run a single scenario id")
    ap.add_argument("--model", default=None, help="model override passed to the agent CLI")
    ap.add_argument("--cmd", default="claude", help="agent CLI command (default: claude)")
    args = ap.parse_args()
    cmd = args.cmd.split()

    files = sorted(SCENARIOS.glob("*.json"))
    if args.roles:
        files = [f for f in files if f.stem in args.roles]
    if not files:
        sys.exit("no scenario files matched")

    RESULTS.mkdir(exist_ok=True)
    results = []
    for f in files:
        spec = json.loads(f.read_text())
        slug = spec["role"]
        skill_text = (ROOT / "roles" / slug / "SKILL.md").read_text()
        role_title = slug.replace("-", " ")

        for sc in spec["scenarios"]:
            if args.only and sc["id"] != args.only:
                continue
            print(f"[{sc['id']}] baseline...", flush=True)
            baseline = run_agent(
                cmd, args.model,
                f"You are an experienced {role_title}. A colleague asks:\n\n{sc['task']}",
            )
            print(f"[{sc['id']}] skill...", flush=True)
            skilled = run_agent(
                cmd, args.model,
                "Adopt the following professional role definition completely — its "
                "principles, heuristics, red flags, and decision framework — and answer "
                f"the question at the end in that role.\n\n{skill_text}\n\n"
                f"A colleague asks:\n\n{sc['task']}",
            )

            # Blind, randomized order.
            skill_is_a = random.random() < 0.5
            a, b = (skilled, baseline) if skill_is_a else (baseline, skilled)
            print(f"[{sc['id']}] judging...", flush=True)
            verdicts = judge(cmd, args.model, sc["task"], a, b, sc["criteria"])["criteria"]

            skill_letter = "A" if skill_is_a else "B"
            base_letter = "B" if skill_is_a else "A"
            skill_hits = sum(1 for v in verdicts if v["verdict"] in (skill_letter, "both"))
            base_hits = sum(1 for v in verdicts if v["verdict"] in (base_letter, "both"))
            results.append({
                "id": sc["id"],
                "role": slug,
                "criteria_total": len(sc["criteria"]),
                "skill_hits": skill_hits,
                "baseline_hits": base_hits,
                "winner": ("skill" if skill_hits > base_hits
                           else "baseline" if base_hits > skill_hits else "tie"),
                "verdicts": verdicts,
                "skill_was": skill_letter,
                "responses": {"baseline": baseline, "skill": skilled},
            })
            print(f"[{sc['id']}] skill {skill_hits}/{len(sc['criteria'])} vs "
                  f"baseline {base_hits}/{len(sc['criteria'])} -> {results[-1]['winner']}")

    if not results:
        sys.exit("no scenarios ran")

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS / f"{stamp}.json"
    out.write_text(json.dumps({"model": args.model, "results": results}, indent=2))

    wins = sum(1 for r in results if r["winner"] == "skill")
    ties = sum(1 for r in results if r["winner"] == "tie")
    print(f"\n{'scenario':<8} {'skill':>5} {'base':>5}  winner")
    for r in results:
        print(f"{r['id']:<8} {r['skill_hits']:>5} {r['baseline_hits']:>5}  {r['winner']}")
    print(f"\nskill wins {wins}/{len(results)} (ties {ties}) — full output: {out}")


if __name__ == "__main__":
    main()
