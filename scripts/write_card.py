"""Render README.md (Hugging Face dataset card) from data/full/stats.json.

Usage: python3 scripts/write_card.py   (run after build_full.py)
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPS = ["A_reconstructed", "B_wiki_history", "C_github_commits", "D_mix"]
VARIANTS = ["5stage", "9step"]
SPLITS = ["train", "validation", "test"]


def main():
    stats = json.load(open(os.path.join(ROOT, "data", "full", "stats.json")))
    total = sum(stats[f"{g}_{v}"]["rows"] for g in GROUPS for v in VARIANTS)
    configs = []
    for g in GROUPS:
        for v in VARIANTS:
            c = f"{g}_{v}"
            files = [f"      - split: {s}\n        path: data/full/{c}/{s}.parquet"
                     for s in SPLITS if stats[c][s]]
            configs.append(f"  - config_name: {c}\n" + ("    default: true\n" if c == "A_reconstructed_9step" else "")
                           + "    data_files:\n" + "\n".join(files))
    for g in GROUPS:
        for v in VARIANTS:
            configs.append(f"  - config_name: trial_{g}_{v}\n    data_files: data/trial/{g}_{v}.parquet")
    size = "1K<n<10K" if total < 10_000 else "10K<n<100K"
    table = "\n".join(
        f"| `{g}_{v}` | {stats[f'{g}_{v}']['rows']:,} | {stats[f'{g}_{v}']['train']:,} / {stats[f'{g}_{v}']['validation']:,} / "
        f"{stats[f'{g}_{v}']['test']:,} | {stats[f'{g}_{v}']['mean_final_words']:,} |"
        for g in GROUPS for v in VARIANTS)
    body = open(os.path.join(ROOT, "docs", "card_body.md")).read().replace("{{TABLE}}", table)
    card = f"""---
license: cc-by-sa-4.0
language:
  - en
pretty_name: Draft-to-Polish Trajectories (Computer Science)
tags:
  - text-diffusion
  - iterative-refinement
  - revision-history
  - writing-process
  - computer-science
task_categories:
  - text-generation
size_categories:
  - {size}
configs:
{chr(10).join(configs)}
---

""" + body
    open(os.path.join(ROOT, "README.md"), "w").write(card)
    print(f"README.md written ({total:,} rows across 8 configs)")


if __name__ == "__main__":
    main()
