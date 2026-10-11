---
license: cc-by-sa-4.0
language:
  - en
pretty_name: Draft-to-Polish Trajectories (CS) — trial
tags:
  - text-diffusion
  - iterative-refinement
  - revision-history
  - writing-process
  - computer-science
task_categories:
  - text-generation
size_categories:
  - n<1K
configs:
  - config_name: A_reconstructed_5stage
    data_files: data/A_reconstructed_5stage.parquet
  - config_name: A_reconstructed_9step
    data_files: data/A_reconstructed_9step.parquet
  - config_name: B_wiki_history_5stage
    data_files: data/B_wiki_history_5stage.parquet
  - config_name: B_wiki_history_9step
    data_files: data/B_wiki_history_9step.parquet
  - config_name: C_github_commits_5stage
    data_files: data/C_github_commits_5stage.parquet
  - config_name: C_github_commits_9step
    data_files: data/C_github_commits_9step.parquet
  - config_name: D_mix_5stage
    data_files: data/D_mix_5stage.parquet
  - config_name: D_mix_9step
    data_files: data/D_mix_9step.parquet
---

# Draft-to-Polish Trajectories (Computer Science) — 10-row trial

Training data for a **text-diffusion prototype in which denoising is drafting**: instead of going from
noise to text, each timestep moves a document from *idea → outline → rough draft → cited draft → polished
final*, the way people actually write.

Every row is **one document** shown as an ordered list of complete snapshots (`steps`). Step 0 is the
idea (a prompt or a title); the last step is the finished, cited text. All rows are computer science.

This is a **trial**: 4 approaches × 2 granularities = 8 files of 10 rows each, built to be compared and
graded before scaling up.

## The four approaches

| file prefix | approach | where the steps come from | strength | weakness |
|---|---|---|---|---|
| `A_reconstructed` | Backward reconstruction | Final = a real, cited arXiv CS paper introduction or Wikipedia CS section. Earlier steps written *backwards* from it under strict rules ([spec](docs/reconstruction_spec.md)): no new facts, only the source's real citations. | Clean, aligned stages exactly matching outline → fill → cite → polish | Intermediate drafts are model-written (distilled), not real human drafts |
| `B_wiki_history` | Real revision history | Snapshots of a Wikipedia CS article's actual edit history, from first version to today (reverted edits skipped). | Real human process; citations accrue naturally | Stages are not labeled; growth is uneven; whole articles are long |
| `C_github_commits` | Real git history | Successive commits of a real design document (Rust RFCs, Python PEPs) from first draft to accepted text. | Real drafting by the authors; several start from an outline template | Design docs, not essays; citations are mostly links, not references |
| `D_mix` | Mix | 7 A-type rows (5 arXiv intros + ENIAC, Dijkstra's algorithm) + 3 B-type rows (Huffman coding, Levenshtein distance, Rabin–Karp). No document appears in A or B. | Tests whether the two kinds combine | — |

## The two granularities

* `*_5stage` — 5 steps. For A: `prompt, outline, rough_draft, cited_draft, final`. For B/C: `title` + 4 real
  versions (`earliest_version, early_revision, late_revision, final`).
* `*_9step` — 9 steps. For A: `prompt, skeleton_outline, detailed_outline, partial_draft, rough_draft,
  draft_citation_needed, cited_draft, revised_draft, final`. For B/C: `title` + 8 real versions.

The A 5-stage steps are exactly steps 0/2/4/6/8 of the 9-step rows. For B/C, real versions are picked
from the history so that consecutive steps are roughly equal amounts of progress toward the final text
(measured by word-level similarity), always including the first version and the final one.

## Schema

| field | type | description |
|---|---|---|
| `id` | string | `<approach letter>-<source>` |
| `approach` | string | `reconstructed` / `wiki_history` / `github_commits` |
| `doc_type` | string | `paper_introduction` / `encyclopedia_section` / `encyclopedia_article` / `design_document` |
| `domain` | string | always `computer_science` |
| `title` | string | document title |
| `num_steps` | int | 5 or 9 |
| `steps` | list | ordered snapshots, each `{step, name, text, word_count, citation_count, similarity_to_final, provenance}` |
| `source` | struct | `{url, license, authors, section, source_id, notes}` |

`provenance` says where each step's text came from: `reconstructed`, `source`, `source_title`,
`enwiki rev <id> (<date>)`, or `commit <sha> (<date>)`.

## What's in the trial

| file | rows | steps | mean final length (words) | documents |
|---|---|---|---|---|
| A_reconstructed | 10 | 5 / 9 | 1,169 | arXiv: Gated SAEs, Vigenère key length, palindrome/square streaming, residential-proxy traffic, Z3alpha SMT strategies · Wikipedia: Turing machine, Halting problem, Quicksort (History); Hash table (Hash function); Lambda calculus (History) |
| B_wiki_history | 10 | 5 / 9 | 2,371 | Bloom filter, Skip list, Merkle tree, Trie, Rope, Fenwick tree, Bogosort, Byzantine fault, Two Generals' Problem, Dining philosophers |
| C_github_commits | 10 | 5 / 9 | 2,610 | Rust RFCs: or-patterns, trait alias, feature unification, destructuring assignment, `black_box` · PEPs 318, 308, 479, 526, 378 |
| D_mix | 10 | 5 / 9 | 1,590 | arXiv: Tao, query expansion for cross-encoders, upsampling fairness, OOD via normalizing flows, attention bridges · Wikipedia: ENIAC, Dijkstra's algorithm · histories: Huffman coding, Levenshtein distance, Rabin–Karp |

## Reviewing

Start at [`review/`](review/README.md): one folder per file, each with an index table and one page per
row showing every step (collapsible) plus per-step word count, citation count, similarity to final and
provenance.

## Known issues (trial)

* **A, arXiv rows**: papers that cite by author name read like "[9] and [10] recently used…" because
  names are replaced by numbered markers in extraction. Uncited drafts say "prior work…" instead of
  inventing names.
* **A/D, Wikipedia rows**: Wikipedia `{{rp}}` page locators survive as ": 2" after some markers; they
  appear only in the final and revised steps.
* **B**: real histories are uneven. Levenshtein distance (D) jumps from 0.17 to 1.0 similarity in its
  last step because the article was substantially rewritten in September 2026. Rope has a single
  reference; Rabin–Karp has none inline (its sources are a general bibliography), so neither shows a
  citation stage. Whole articles are long (Bloom filter's final is ~7,500 words).
* **C**: some documents arrive nearly complete in one commit (e.g. the or-patterns RFC goes from a
  269-word stub to 2,893 words in one commit). Citations in RFCs/PEPs are mostly links, so
  `citation_count` (bracketed numeric markers) is approximate there.
* `similarity_to_final` is word-level `difflib` ratio; it is a progress signal, not a quality score.

## Sources and licenses

* arXiv papers: only papers whose arXiv license is CC BY 4.0 or CC BY-SA 4.0 (checked against arXiv
  OAI-PMH metadata). Attribution is in each row's `source`.
* Wikipedia: CC BY-SA 4.0; attribution to Wikipedia contributors with revision links.
* Rust RFCs: MIT OR Apache-2.0. Python PEPs: placed in the public domain (or CC0) by their authors.

Because the Wikipedia and CC BY-SA material is share-alike, the dataset as a whole is released under
**CC BY-SA 4.0**.

## Reproducing

```bash
pip install requests beautifulsoup4 lxml mwparserfromhell pyarrow
python3 scripts/fetch_arxiv.py 2404.16014 > sources/final_text/arxiv_2404.16014.json
python3 scripts/fetch_wikipedia.py "Quicksort" "history" > sources/final_text/wiki_Quicksort.json
(cd scripts && python3 fetch_wiki_history.py "Bloom filter") > sources/wiki_history/Bloom_filter.json
python3 scripts/fetch_git_history.py <clone of rust-lang/rfcs> text/2535-or-patterns.md https://github.com/rust-lang/rfcs "MIT OR Apache-2.0" > sources/github_history/rfc_2535-or-patterns.json
python3 scripts/build_dataset.py
```
