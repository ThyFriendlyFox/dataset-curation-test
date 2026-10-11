"""Assemble the 8 trial files (4 approaches x {5-stage, 9-step}) from sources/.

  A  reconstructed     real final text (arXiv intro / Wikipedia section) + drafts written backwards from it
  B  wiki_history      real Wikipedia revision history, sampled from first version to current
  C  github_commits    real git history of a design document (Rust RFC / Python PEP)
  D  mix               7 A-type rows + 3 B-type rows (no rows shared with A or B)

Every row has the same schema; step 0 is always the "idea" (prompt for A, title for B/C) and the last
step is always the finished document. The 5-stage variant of A is steps 0,2,4,6,8 of the 9-step one;
for B/C both variants are sampled from the same pool of real versions.

Usage: python3 scripts/build_dataset.py   (writes data/*.parquet, data/*.jsonl, review/*.md)
"""
import difflib, glob, json, os, re
import pyarrow as pa
import pyarrow.parquet as pq

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = lambda *p: os.path.join(ROOT, "sources", *p)

A_ROWS = ["arxiv_2404.16014", "arxiv_2312.09956", "arxiv_2309.14788", "arxiv_2404.10610", "arxiv_2401.17159",
          "wiki_Turing_machine", "wiki_Halting_problem", "wiki_Quicksort", "wiki_Hash_table", "wiki_Lambda_calculus"]
D_A_ROWS = ["arxiv_2404.10921", "arxiv_2311.09175", "arxiv_2401.13555",
            "wiki_ENIAC", "wiki_Garbage_collection_computer_science", "wiki_Dijkstras_algorithm", "wiki_Publickey_cryptography"]
B_ALL = ["Bloom_filter", "Skip_list", "Merkle_tree", "Trie", "Rope_data_structure", "Fenwick_tree", "Bogosort",
         "Byzantine_fault", "Two_Generals_Problem", "Dining_philosophers_problem", "Huffman_coding",
         "Levenshtein_distance", "RabinKarp_algorithm"]
C_ROWS = ["rfc_2535-or-patterns", "rfc_1733-trait-alias", "rfc_3692-feature-unification",
          "rfc_2909-destructuring-assignment", "rfc_2360-bench-black-box",
          "pep_0318", "pep_0308", "pep_0479", "pep_0526", "pep_0378"]

STEP_NAMES_9 = ["prompt", "skeleton_outline", "detailed_outline", "partial_draft", "rough_draft",
                "draft_citation_needed", "cited_draft", "revised_draft", "final"]
STAGE_NAMES_5 = ["prompt", "outline", "rough_draft", "cited_draft", "final"]
A_5_FROM_9 = [0, 2, 4, 6, 8]
CITE = re.compile(r"\[(\d+(?:[,–-]\d+)*)\]")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def with_refs(text, refs):
    if not refs:
        return text
    return text + "\n\nReferences:\n" + "\n".join(f"[{r['n']}] {r['text']}" for r in refs)


def similarity(a, b):
    """Word-level similarity in [0,1] (difflib ratio); used to place snapshots along the path to final."""
    return round(difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio(), 4)


def step(i, name, text, final_text, provenance):
    return {"step": i, "name": name, "text": text, "word_count": len(text.split()),
            "citation_count": len(CITE.findall(text.split("\nReferences:\n")[0])),
            "similarity_to_final": similarity(text, final_text), "provenance": provenance}


def pick(pool, k, final_text):
    """Choose k versions from a chronological pool: first + final always, the rest spaced evenly by
    similarity to the final text (so steps are roughly equal amounts of progress), kept in time order."""
    sims = [similarity(v["full_text"], final_text) for v in pool]
    chosen = [0]
    lo = sims[0]
    for j in range(1, k - 1):
        target = lo + (1 - lo) * j / (k - 1)
        cands = [i for i in range(chosen[-1] + 1, len(pool) - 1) if i not in chosen]
        if not cands:
            break
        chosen.append(min(cands, key=lambda i: (abs(sims[i] - target), i)))
    chosen.append(len(pool) - 1)
    return [pool[i] for i in chosen]


# ---------- A: reconstructed ----------
def a_row(name, variant):
    src = load(S("final_text", f"{name}.json"))
    rec = load(S("reconstructed", f"{name}.json"))
    final = with_refs(src["text"], src["references"])
    texts = [s["text"] for s in sorted(rec["steps"], key=lambda s: s["step"])] + [final]
    assert len(texts) == 9, name
    prov = ["reconstructed"] * 8 + ["source"]
    idx = range(9) if variant == "9step" else A_5_FROM_9
    names = STEP_NAMES_9 if variant == "9step" else STAGE_NAMES_5
    steps = [step(j, names[j], texts[i], final, prov[i]) for j, i in enumerate(idx)]
    is_paper = src["source_type"] == "research_paper"
    return {
        "id": f"A-{name}", "approach": "reconstructed", "doc_type": "paper_introduction" if is_paper else "encyclopedia_section",
        "title": src["title"] + ("" if is_paper else f" — {src['section']}"),
        "source": {"url": src["url"], "license": src["license"], "authors": src["authors"],
                   "section": src["section"], "source_id": src["source_id"], "notes": ""},
        "steps": steps,
    }


# ---------- B: Wikipedia revision history ----------
def b_row(name, variant):
    src = load(S("wiki_history", f"{name}.json"))
    pool = [{**s, "full_text": with_refs(s["text"], s["references"])} for s in src["snapshots"] if s["word_count"] >= 20]
    final = pool[-1]["full_text"]
    k = 8 if variant == "9step" else 4
    snaps = pick(pool, k, final)
    names = ["title"] + ([f"revision_{i}" for i in range(1, k)] if variant == "9step" else
                         ["earliest_version", "early_revision", "late_revision"])
    names[-1] = "final"
    steps = [step(0, "title", src["title"], final, "source_title")]
    for j, s in enumerate(snaps, start=1):
        steps.append(step(j, names[j] if j < len(names) else "final", s["full_text"], final,
                          f"enwiki rev {s['revid']} ({s['timestamp'][:10]})"))
    return {
        "id": f"B-{name}", "approach": "wiki_history", "doc_type": "encyclopedia_article", "title": src["title"],
        "source": {"url": src["url"], "license": src["license"], "authors": src["authors"], "section": "whole article",
                   "source_id": src["source_id"],
                   "notes": f"{src['total_revisions']} revisions in history; {len(pool)} candidate versions sampled"},
        "steps": steps,
    }


# ---------- C: git history ----------
def c_row(name, variant):
    src = load(S("github_history", f"{name}.json"))
    pool = [{**v, "full_text": v["text"]} for v in src["versions"]]
    final = pool[-1]["full_text"]
    k = 8 if variant == "9step" else 4
    snaps = pick(pool, k, final)
    names = ["title"] + ([f"revision_{i}" for i in range(1, k)] if variant == "9step" else
                         ["earliest_version", "early_revision", "late_revision"])
    names[-1] = "final"
    steps = [step(0, "title", src["title"], final, "source_title")]
    for j, v in enumerate(snaps, start=1):
        steps.append(step(j, names[j], v["full_text"], final, f"commit {v['commit'][:10]} ({v['date'][:10]})"))
    kind = "Rust RFC" if name.startswith("rfc") else "Python PEP"
    return {
        "id": f"C-{name}", "approach": "github_commits", "doc_type": "design_document",
        "title": f"{kind}: {src['title']}",
        "source": {"url": src["source_id"], "license": src["license"],
                   "authors": f"{src['repo']} contributors", "section": "whole document", "source_id": src["source_id"],
                   "notes": f"{src['total_commits']} commits touching the file; {src['distinct_versions']} distinct versions"},
        "steps": steps,
    }


def write(fname, rows):
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    for r in rows:
        r["domain"] = "computer_science"
        r["num_steps"] = len(r["steps"])
    with open(os.path.join(ROOT, "data", f"{fname}.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    pq.write_table(pa.Table.from_pylist(rows), os.path.join(ROOT, "data", f"{fname}.parquet"), compression="zstd")
    review(fname, rows)


def review(fname, rows):
    os.makedirs(os.path.join(ROOT, "review"), exist_ok=True)
    out = [f"# {fname}\n", f"{len(rows)} rows. Mark each row **pass / fail** — row ids are the headings.\n",
           "| # | id | title | steps | words (first→last) | citations (first→last) |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        s = r["steps"]
        out.append(f"| {i} | `{r['id']}` | {r['title'][:60]} | {len(s)} | {s[1]['word_count']}→{s[-1]['word_count']} "
                   f"| {s[1]['citation_count']}→{s[-1]['citation_count']} |")
    for i, r in enumerate(rows, 1):
        out += [f"\n---\n\n## {i}. `{r['id']}` — {r['title']}\n",
                f"Source: <{r['source']['url']}> · License: {r['source']['license']} · {r['source']['notes']}\n",
                "| step | name | words | citations | similarity to final | provenance |", "|---|---|---|---|---|---|"]
        out += [f"| {s['step']} | {s['name']} | {s['word_count']} | {s['citation_count']} | {s['similarity_to_final']:.2f} | {s['provenance']} |"
                for s in r["steps"]]
        for s in r["steps"]:
            body = s["text"].replace("```", "ˋˋˋ")  # keep code fences inside a step from breaking the page
            out.append(f"\n<details><summary><b>Step {s['step']} — {s['name']}</b> ({s['word_count']} words)</summary>\n\n"
                       f"````text\n{body}\n````\n\n</details>")
    with open(os.path.join(ROOT, "review", f"{fname}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def main():
    have_b = [b for b in B_ALL if os.path.exists(S("wiki_history", f"{b}.json"))]
    b_rows, d_b_rows = have_b[:10], have_b[10:13]
    for variant in ("5stage", "9step"):
        write(f"A_reconstructed_{variant}", [a_row(n, variant) for n in A_ROWS])
        write(f"B_wiki_history_{variant}", [b_row(n, variant) for n in b_rows])
        write(f"C_github_commits_{variant}", [c_row(n, variant) for n in C_ROWS])
        write(f"D_mix_{variant}", [a_row(n, variant) for n in D_A_ROWS] + [b_row(n, variant) for n in d_b_rows])
    print("B rows:", len(b_rows), "D B-rows:", len(d_b_rows))


if __name__ == "__main__":
    main()
