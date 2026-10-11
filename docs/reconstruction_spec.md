# Reconstruction spec (approach A, and the A-rows of D)

Each row starts from a **real, finished, cited text** (`sources/final_text/*.json`): an arXiv CS paper
introduction (CC BY / CC BY-SA / CC0) or a Wikipedia CS article section (CC BY-SA). We work *backwards*
from that final text to produce the drafts a writer would plausibly have produced on the way there —
the same direction as the forward (noising) process in diffusion training.

## The 9 steps

| step | name | what it contains |
|---|---|---|
| 0 | `prompt` | The user's rough idea: one or two sentences, as a person would ask for it ("Write the history section of an article on quicksort…"). No facts beyond the topic and scope. |
| 1 | `skeleton_outline` | Headings / top-level points only (3–7 lines). |
| 2 | `detailed_outline` | Each top-level point expanded into terse sub-bullets with the key facts, names, dates, numbers that the final text uses. Fragments, not sentences. |
| 3 | `partial_draft` | First ~half of the outline turned into rough prose; the rest still bullets. |
| 4 | `rough_draft` | Everything in rough prose. Same information as the final, but unpolished: plain or clumsy wording, some repetition, weak transitions, occasional run-on, paragraph order may differ slightly. No citation markers. |
| 5 | `draft_citation_needed` | The rough draft with `[citation needed]` placed exactly where the final text has citations (and only there). |
| 6 | `cited_draft` | Placeholders replaced by the real markers `[n]` from the final text, plus a `References` list containing exactly the references cited. Prose still rough. |
| 7 | `revised_draft` | Structural and flow edits done (paragraph order, transitions, merged/split sentences) but word-level polish not finished; close to final but clearly not identical. Citations as in final. |
| 8 | `final` | The source text, verbatim, with its references. (Filled in by the build script — do not write it.) |

The **5-stage** variant uses steps `0, 2, 4, 6, 8` (prompt → outline → rough draft → cited draft → final),
so the two variants are always aligned.

## Hard rules

1. **No new facts.** Every claim in steps 1–7 must come from the final text. Rough drafts may be vaguer
   or clumsier, never wrong or invented.
2. **No invented citations.** Steps 6–7 use only the reference numbers and reference entries in the
   source's `references`; each `[n]` attaches to the same claim it supports in the final text.
   Steps 0–5 contain no `[n]` markers.
3. **Same document.** Every step is a full snapshot of the *same* piece, in the same register (an
   encyclopedia section stays an encyclopedia section; a paper intro stays a paper intro).
4. **Monotone progress.** Each step should be strictly closer to the final than the previous one.
5. Keep math/inline code as it appears in the source. Use `## ` for headings if the piece has subsections.
6. Reference lists in steps 6–7: a line `References:` followed by `[n] <reference text>` lines, copied
   verbatim from the source's `references`.

## Output format

One JSON file per row at `sources/reconstructed/<source file name>`:

```json
{"source_file": "sources/final_text/<name>.json",
 "steps": [{"step": 0, "name": "prompt", "text": "..."}, ..., {"step": 7, "name": "revised_draft", "text": "..."}]}
```
