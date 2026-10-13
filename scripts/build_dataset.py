"""Assemble the 8 trial files (4 approaches x {5-stage, 9-step}) from sources/.

  A  reconstructed     real final text (arXiv intro / Wikipedia section) + drafts written backwards from it
  B  wiki_history      real Wikipedia revision history, sampled from first version to current
  C  github_commits    real git history of a design document (Rust RFC / Python PEP)
  D  mix               7 A-type rows + 3 B-type rows (no rows shared with A or B)

Every row has the same schema; step 0 is always the "idea" (prompt for A, title for B/C) and the last
step is always the finished document. The 5-stage variant of A is steps 0,2,4,6,8 of the 9-step one;
for B/C both variants are sampled from the same pool of real versions.

Usage: python3 scripts/build_dataset.py   (writes data/trial/*.parquet, data/trial/*.jsonl, review/trial/)
"""
import difflib, functools, glob, gzip, json, os, re
import pyarrow as pa
import pyarrow.parquet as pq
from wikitext import convert

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = lambda *p: os.path.join(ROOT, "sources", *p)

A_ROWS = ["arxiv_2404.16014", "arxiv_2312.09956", "arxiv_2309.14788", "arxiv_2404.10610", "arxiv_2401.17159",
          "wiki_Turing_machine", "wiki_Halting_problem", "wiki_Quicksort", "wiki_Hash_table", "wiki_Lambda_calculus"]
D_A_ROWS = ["arxiv_2404.10921", "arxiv_2311.09175", "arxiv_2401.13555", "arxiv_2402.06537", "arxiv_2404.17918",
            "wiki_ENIAC", "wiki_Dijkstras_algorithm"]
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
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def resolve(path):
    """Source paths in reconstruction files may be absolute or relative to the repo root."""
    return path if os.path.isabs(path) else os.path.join(ROOT, path)


def with_refs(text, refs):
    if not refs:
        return text
    return text + "\n\nReferences:\n" + "\n".join(f"[{r['n']}] {r['text']}" for r in refs)


@functools.lru_cache(maxsize=8192)  # both variants of a row score the same snapshots
def similarity(a, b):
    """Word-level similarity in [0,1] (difflib ratio); used to place snapshots along the path to final."""
    return round(difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio(), 4)


def step(i, name, text, final_text, provenance):
    return {"step": i, "name": name, "text": text, "word_count": len(text.split()),
            "citation_count": len(CITE.findall(text.split("\nReferences:\n")[0])),
            "similarity_to_final": similarity(text, final_text), "provenance": provenance}


def pick(pool, k, final_text):
    """Choose k versions from a chronological pool, always including the first and the final one.

    Picks the in-order subset that maximizes the smallest step of progress (gain in similarity to the
    final text) between consecutive snapshots; ties go to the most even spacing. This avoids
    near-duplicate "no-op" steps and regressions where the history allows it."""
    sims = [similarity(v["full_text"], final_text) for v in pool]
    n = len(pool)
    if n <= k:
        return pool
    # best[j][i]: (min gain, -sum of squared gains) for a path of j+1 picks ending at index i
    NEG = (-9.0, 0.0)
    best = [[NEG] * n for _ in range(k)]
    back = [[-1] * n for _ in range(k)]
    best[0][0] = (9.0, 0.0)
    for j in range(1, k):
        for i in range(j, n):
            for p in range(j - 1, i):
                if best[j - 1][p] == NEG:
                    continue
                g = sims[i] - sims[p]
                cand = (min(best[j - 1][p][0], g), best[j - 1][p][1] - g * g)
                if cand > best[j][i]:
                    best[j][i], back[j][i] = cand, p
    idx, i = [], n - 1
    for j in range(k - 1, -1, -1):
        idx.append(i)
        i = back[j][i]
    return [pool[i] for i in reversed(idx)]


# ---------- A: reconstructed ----------
def a_row(name, variant):
    rec = load(S("reconstructed", f"{name}.json"))
    src = load(resolve(rec["source_file"]) if rec.get("source_file") else S("final_text", f"{name}.json"))
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


def snapshot_names(k):
    """Step names for B/C rows: 'title' then k real versions, the last being the final text."""
    middle = [f"revision_{i}" for i in range(1, k)] if k != 4 else ["earliest_version", "early_revision", "late_revision"]
    return ["title"] + middle + ["final"]


# ---------- B: Wikipedia revision history ----------
def b_row(name, variant, path=None):
    src = load(path or S("wiki_history", f"{name}.json"))
    pool = []
    for s in src["snapshots"]:
        if "wikitext" in s:  # re-convert with the current converter
            s = {**s, **dict(zip(("text", "references"), convert(s["wikitext"])))}
            s["word_count"] = len(s["text"].split())
        if s["word_count"] >= 20:
            pool.append({**s, "full_text": with_refs(s["text"], s["references"])})
    final = pool[-1]["full_text"]
    k = 8 if variant == "9step" else 4
    snaps = pick(pool, k, final)
    names = snapshot_names(k)
    steps = [step(0, "title", src["title"], final, "source_title")]
    for j, s in enumerate(snaps, start=1):
        steps.append(step(j, names[j], s["full_text"], final,
                          f"enwiki rev {s['revid']} ({s['timestamp'][:10]})"))
    return {
        "id": f"B-{name}", "approach": "wiki_history", "doc_type": "encyclopedia_article", "title": src["title"],
        "source": {"url": src["url"], "license": src["license"], "authors": src["authors"], "section": "whole article",
                   "source_id": src["source_id"],
                   "notes": f"{src['total_revisions']} revisions in history; {len(pool)} candidate versions sampled"},
        "steps": steps,
    }


# ---------- C: git history ----------
C_KINDS = {"rfc": "Rust RFC", "pep": "Python PEP", "se": "Swift Evolution", "go": "Go proposal",
           "keep": "Kotlin KEEP", "sip": "Scala SIP", "eip": "Ethereum EIP"}


def c_row(name, variant, path=None):
    src = load(path or S("github_history", f"{name}.json"))
    pool = [{**v, "full_text": v["text"]} for v in src["versions"]]
    final = pool[-1]["full_text"]
    k = 8 if variant == "9step" else 4
    snaps = pick(pool, k, final)
    names = snapshot_names(k)
    steps = [step(0, "title", src["title"], final, "source_title")]
    for j, v in enumerate(snaps, start=1):
        steps.append(step(j, names[j], v["full_text"], final, f"commit {v['commit'][:10]} ({v['date'][:10]})"))
    kind = C_KINDS[name.split("_", 1)[0]]
    return {
        "id": f"C-{name}", "approach": "github_commits", "doc_type": "design_document",
        "title": f"{kind}: {src['title']}",
        "source": {"url": src["source_id"], "license": src["license"],
                   "authors": f"{src['repo']} contributors", "section": "whole document", "source_id": src["source_id"],
                   "notes": f"{src['total_commits']} commits touching the file; {src['distinct_versions']} distinct versions"},
        "steps": steps,
    }


def write(fname, rows):
    os.makedirs(os.path.join(ROOT, "data", "trial"), exist_ok=True)
    for r in rows:
        r["domain"] = "computer_science"
        r["num_steps"] = len(r["steps"])
    with open(os.path.join(ROOT, "data", "trial", f"{fname}.jsonl"), "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    pq.write_table(pa.Table.from_pylist(rows), os.path.join(ROOT, "data", "trial", f"{fname}.parquet"), compression="zstd")
    review(f"trial/{fname}", rows)


def review(fname, rows):
    """Human-readable pages: review/<fname>/README.md (index) + one page per row (GitHub won't
    render a single multi-MB markdown file)."""
    d = os.path.join(ROOT, "review", fname)
    os.makedirs(d, exist_ok=True)
    for old in glob.glob(os.path.join(d, "*.md")):
        os.remove(old)
    index = [f"# {fname}\n", f"{len(rows)} rows. Open a row, read its steps top to bottom, and mark it **pass / fail** "
             "(by row number or id).\n",
             "| # | id | title | steps | words (first→last) | citations (first→last) |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        s = r["steps"]
        page = f"{i:02d}-{r['id']}.md"
        index.append(f"| {i} | [`{r['id']}`]({page}) | {r['title'][:70]} | {len(s)} | {s[1]['word_count']}→{s[-1]['word_count']} "
                     f"| {s[1]['citation_count']}→{s[-1]['citation_count']} |")
        out = [f"# {i}. {r['title']}\n", f"`{r['id']}` · [{fname}](README.md)\n",
               f"Source: <{r['source']['url']}> · License: {r['source']['license']}"
               + (f" · {r['source']['notes']}" if r['source']['notes'] else "") + "\n",
               "| step | name | words | citations | similarity to final | provenance |", "|---|---|---|---|---|---|"]
        out += [f"| {x['step']} | {x['name']} | {x['word_count']} | {x['citation_count']} | {x['similarity_to_final']:.2f} | {x['provenance']} |"
                for x in s]
        for x in s:
            body = x["text"].replace("````", "ˋˋˋˋ")  # keep the step's own fences from closing ours
            out.append(f"\n<details><summary><b>Step {x['step']} — {x['name']}</b> ({x['word_count']} words)</summary>\n\n"
                       f"````text\n{body}\n````\n\n</details>")
        with open(os.path.join(d, page), "w", encoding="utf-8") as f:
            f.write("\n".join(out) + "\n")
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index) + "\n")


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
