#!/usr/bin/env python3
"""
Parity test: role-skill answers vs real practitioners' published answers.

For each harvested question, the skill-loaded model writes an answer; a
blind judge compares it against the practitioner's accepted answer in
randomized A/B order. Parity = win+tie rate. See evals/parity/README.md.

Usage:
    python3 evals/parity/run_parity.py [role-slug ...]
        [--model M] [--judge-model M] [--workers N] [--cmd claude]
"""

import argparse
import datetime
import json
import random
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RESULTS = HERE / "results"

JUDGE_PROMPT = """You are a senior practitioner grading two anonymous answers to a real question from your field.

QUESTION:
{q}

ANSWER A:
{a}

ANSWER B:
{b}

Judge which answer would better serve the asker. Rules:
- Grade substance: correctness, completeness on the points that matter, actionability, and honesty about uncertainty/jurisdiction/context limits.
- Do NOT reward length, formatting, or hedging boilerplate. A short correct answer beats a long padded one.
- Penalize confident errors hardest.
- One answer may address context the other ignores; weigh what the asker actually needed.

Reply with ONLY JSON, no prose:
{{"winner": "A|B|tie", "reason": "<one sentence>", "a_errors": "<confident factual errors in A, or none>", "b_errors": "<confident factual errors in B, or none>"}}
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


def run_question(cmd, model, judge_model, slug, skill_text, item):
    print(f"[{item['id']}] answering...", flush=True)
    skill_answer = run_agent(
        cmd, model,
        "Adopt the following professional role definition completely — its principles, "
        "heuristics, red flags, and decision framework — and answer the question at the "
        "end as that practitioner would: direct, specific, honest about limits. "
        "Do not mention the role definition itself.\n\n"
        f"{skill_text}\n\nQUESTION:\n\n{item['question']}",
    )
    skill_is_a = random.random() < 0.5
    a, b = (skill_answer, item["expert_answer"]) if skill_is_a else (item["expert_answer"], skill_answer)
    out = run_agent(cmd, judge_model, JUDGE_PROMPT.format(q=item["question"], a=a, b=b))
    m = re.search(r"\{.*\}", out, re.DOTALL)
    if not m:
        raise ValueError(f"judge returned no JSON: {out[:300]}")
    j = json.loads(m.group(0))
    skill_letter = "A" if skill_is_a else "B"
    outcome = ("win" if j["winner"] == skill_letter
               else "tie" if j["winner"] == "tie" else "loss")
    res = {
        "id": item["id"],
        "role": slug,
        "outcome": outcome,
        "judge_reason": j.get("reason", ""),
        "skill_errors": j.get("a_errors" if skill_is_a else "b_errors", ""),
        "expert_errors": j.get("b_errors" if skill_is_a else "a_errors", ""),
        "source": item["source"],
        "skill_answer": skill_answer,
    }
    print(f"[{item['id']}] {outcome} — {res['judge_reason'][:90]}")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roles", nargs="*")
    ap.add_argument("--model", default=None)
    ap.add_argument("--judge-model", default=None)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--cmd", default="claude")
    args = ap.parse_args()
    cmd = args.cmd.split()
    judge_model = args.judge_model or args.model

    files = sorted((HERE / "questions").glob("*.json"))
    if args.roles:
        files = [f for f in files if f.stem in args.roles]
    if not files:
        sys.exit("no question files matched")

    jobs = []
    for f in files:
        spec = json.loads(f.read_text())
        slug = spec["role"]
        skill_text = (ROOT / "roles" / slug / "SKILL.md").read_text()
        jobs += [(slug, skill_text, q) for q in spec["questions"]]

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(run_question, cmd, args.model, judge_model, s, t, q)
                for s, t, q in jobs]
        results = []
        for fut in futs:
            try:
                results.append(fut.result())
            except Exception as e:
                print(f"question failed: {e}", file=sys.stderr)

    if not results:
        sys.exit("nothing ran")
    RESULTS.mkdir(exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS / f"{stamp}.json"
    out.write_text(json.dumps({"model": args.model, "judge_model": judge_model,
                               "results": results}, indent=2, ensure_ascii=False))

    wins = sum(r["outcome"] == "win" for r in results)
    ties = sum(r["outcome"] == "tie" for r in results)
    print(f"\n{'question':<28} outcome")
    for r in sorted(results, key=lambda x: x["id"]):
        print(f"{r['id']:<28} {r['outcome']}")
    n = len(results)
    print(f"\nvs real practitioner answers: {wins} wins, {ties} ties, "
          f"{n - wins - ties} losses of {n} — parity rate {(wins + ties) / n:.0%}")
    print(f"full output: {out}")


if __name__ == "__main__":
    main()
