# Draft-to-Polish Trajectories (Computer Science)

Training data for a **text-diffusion model in which denoising is drafting**. Instead of going from noise
to text, each timestep moves a document from *idea → outline → rough draft → cited draft → polished final*,
the way people actually write.

Every row is **one document** shown as an ordered list of complete snapshots (`steps`). Step 0 is the
idea (a prompt or a title); the last step is the finished text. Every row is computer science or closely
related (algorithms, theory, systems, programming languages, ML, security, networking).

## Configs

Four approaches, each at two granularities, each with train / validation / test splits.

| config | rows | train / validation / test | mean final length (words) |
|---|---|---|---|
{{TABLE}}

The 80 rows of the first trial (10 per config) are kept as `trial_*` configs and are also included in the
full configs.

```python
from datasets import load_dataset
ds = load_dataset("<this repo>", "A_reconstructed_9step")   # or any config above
row = ds["train"][0]
for s in row["steps"]:
    print(s["step"], s["name"], s["word_count"])
```

## The four approaches

| prefix | where the steps come from | strength | weakness |
|---|---|---|---|
| `A_reconstructed` | The final is a real, cited text: an openly licensed arXiv CS paper introduction or a Wikipedia CS article section. Earlier steps are written *backwards* from it under strict rules ([spec](docs/reconstruction_spec.md)): no new facts, only the source's real citations, every row machine-validated. | Clean, aligned stages exactly matching outline → fill → cite → polish | Intermediate drafts are model-written (distilled), not real human drafts |
| `B_wiki_history` | Real snapshots of a Wikipedia CS article's edit history, from its first version to today (reverted edits skipped). | Real human process; citations accrue naturally | Stages are not labeled; growth is uneven; articles are long. Small, because Wikipedia rate-limits history downloads |
| `C_github_commits` | Real successive commits of a design document, from first draft to accepted text: Rust RFCs, Python PEPs, Swift Evolution, Go, Kotlin KEEP and Scala SIP proposals, Ethereum EIPs. | Real drafting by the authors; many start from an outline template | Design documents, not essays; citations are mostly links |
| `D_mix` | ~70% A-type rows + ~30% real-history rows (B-type first, topped up with C-type). No document appears in two configs. | Tests whether reconstructed and real trajectories combine | — |

## The two granularities

* `*_5stage`: 5 steps. A: `prompt, outline, rough_draft, cited_draft, final`. B/C: `title` + 4 real versions
  (`earliest_version, early_revision, late_revision, final`).
* `*_9step`: 9 steps. A: `prompt, skeleton_outline, detailed_outline, partial_draft, rough_draft,
  draft_citation_needed, cited_draft, revised_draft, final`. B/C: `title` + 8 real versions.

A's 5-stage steps are exactly steps 0/2/4/6/8 of its 9-step rows. For B/C, versions are picked from the
real history so consecutive steps are roughly equal amounts of progress toward the final (word-level
similarity), always including the first version and the final one. Histories with fewer than 8 distinct
versions appear only in the 5-stage configs (never padded), which is why the 9-step B/C/D configs are smaller.

## Schema

| field | type | description |
|---|---|---|
| `id` | string | `<approach letter>-<source>` |
| `approach` | string | `reconstructed` / `wiki_history` / `github_commits` |
| `doc_type` | string | `paper_introduction` / `encyclopedia_section` / `encyclopedia_article` / `design_document` |
| `domain` | string | always `computer_science` |
| `title` | string | document title |
| `num_steps` | int | 5 or 9 |
| `split` | string | `train` / `validation` / `test` (stable hash of `id`) |
| `steps` | list | ordered snapshots: `{step, name, text, word_count, citation_count, similarity_to_final, provenance}` |
| `source` | struct | `{url, license, authors, section, source_id, notes}` |

`provenance` says where each step's text came from: `reconstructed`, `source`, `source_title`,
`enwiki rev <id> (<date>)`, or `commit <sha> (<date>)`.

## How it was built

* **A sources.** arXiv OAI-PMH harvest of CS papers (primary category `cs.*`) licensed CC BY / CC BY-SA /
  CC0; the Introduction is extracted from arXiv's HTML with citations as `[n]` and the cited bibliography
  entries; kept if 250–1,300 words with ≥3 resolved citations. Wikipedia: CS articles from 41 CS categories
  (via PetScan), one cited section per article (250–1,300 words, ≥3 citations).
* **Topic filter.** Wikipedia articles whose Wikidata item is a person, organization, company, product,
  software product, website, dataset or event are excluded (programming languages, algorithms, data
  structures, protocols and file formats are kept).
* **A drafts.** Written by parallel model writers following [the spec](docs/reconstruction_spec.md), then
  checked by [`validate_reconstruction.py`](scripts/validate_reconstruction.py): no citation markers before
  the cited draft, `[citation needed]` exactly where the final cites, cited-draft markers identical to the
  final's, references verbatim, and no numbers absent from the final. Writers skipped sources with garbled
  extraction (missing equations, stripped code) rather than invent content.
* **B/C histories.** Wikipedia revisions via the MediaWiki API (wikitext converted to text with numbered
  citations); git histories from full clones, following renames and stripping metadata headers.

## Review

Sample pages for every config are in [`review/full/`](review/full/) (10 test-split rows each, every step
viewable), and the graded trial is in [`review/trial/`](review/trial/README.md).

## Known issues

* **A, arXiv rows**: papers that cite by author name read like "[9] and [10] recently used…", because
  names become numbered markers in extraction. Uncited drafts say "prior work…" rather than invent names.
* **A, Wikipedia rows**: some page locators survive as ": 2" after markers (final and revised steps only).
* **B** is small: Wikipedia rate-limits this environment's shared IP, so only a few dozen full histories
  could be downloaded. Real histories are uneven (an article may be rewritten in one edit), and some
  articles have no inline citations, so they show no citation stage.
* **C**: some documents arrive nearly complete in one commit. Citations are mostly links, so
  `citation_count` (bracketed numeric markers) is approximate.
* The topic filter is not perfect; a small share of rows are adjacent fields (applied math, signal
  processing) or general computing history.
* `similarity_to_final` is word-level `difflib` ratio, a progress signal, not a quality score.

## Sources and licenses

* arXiv papers: only papers whose arXiv license is CC BY 4.0, CC BY-SA 4.0 or CC0 (checked in OAI-PMH
  metadata); attribution in each row's `source`.
* Wikipedia: CC BY-SA 4.0; attribution to Wikipedia contributors with revision links.
* Rust RFCs: MIT OR Apache-2.0 · Python PEPs: public domain / CC0 · Swift Evolution, Kotlin KEEP, Scala SIPs:
  Apache-2.0 · Go proposals: BSD-3-Clause · Ethereum EIPs: CC0.

Because Wikipedia and CC BY-SA material is share-alike, the dataset as a whole is released under
**CC BY-SA 4.0**; each row's own license is in `source.license`.

## Reproducing

```bash
pip install requests beautifulsoup4 lxml mwparserfromhell pyarrow
(cd scripts && python3 harvest_arxiv.py ../sources/arxiv 2024-03-01 2024-08-31 3000)
(cd scripts && python3 list_wiki_cs.py) > sources/wiki_cs_articles.json
(cd scripts && python3 topic_filter.py ../sources/wiki_cs_articles.json)
(cd scripts && python3 wiki_sections.py ../sources/wiki_cs_articles.json ../sources/wiki_sections)
python3 scripts/fetch_git_history.py --batch <clone> 'text/*.md' https://github.com/rust-lang/rfcs "MIT OR Apache-2.0" rfc sources/github_history_full
# A drafts: see docs/reconstruction_spec.md; validate with scripts/validate_reconstruction.py
python3 scripts/build_full.py && python3 scripts/write_card.py
```
