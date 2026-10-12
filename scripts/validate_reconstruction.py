"""Validate reconstructed rows (approach A) against their source.

Usage: python3 scripts/validate_reconstruction.py sources/reconstructed/<name>.json [...]
Prints one line per file (OK or the problems) and exits 1 if any file fails.

Checks: the 8 step names in order; no citation markers before the cited draft; one
"[citation needed]" per citation group of the final in step 5; the cited draft's marker
sequence equals the final's; every reference line in steps 6–7 copied verbatim from the source;
no 3+ digit number (year, quantity) that is absent from the final text and its references.
"""
import json, os, re, sys

CITE = re.compile(r"\[(\d+(?:[,–-]\d+)*)\]")
NAMES = ["prompt", "skeleton_outline", "detailed_outline", "partial_draft", "rough_draft",
         "draft_citation_needed", "cited_draft", "revised_draft"]


def body(t):
    return t.split("\nReferences:")[0]


def check(path):
    r = json.load(open(path, encoding="utf-8"))
    src_path = r.get("source_file", "")
    if not os.path.exists(src_path):
        return [f"source_file not found: {src_path}"]
    src = json.load(open(src_path, encoding="utf-8"))
    steps = sorted(r.get("steps", []), key=lambda s: s["step"])
    if [s.get("name") for s in steps] != NAMES:
        return [f"step names {[s.get('name') for s in steps]}"]
    probs = []
    final_markers = CITE.findall(src["text"])
    refs = {str(x["n"]): x["text"] for x in src["references"]}
    for s in steps[:6]:
        if CITE.search(s["text"]):
            probs.append(f"citation marker in step {s['step']}")
    if CITE.findall(body(steps[6]["text"])) != final_markers:
        probs.append("cited_draft marker sequence differs from final")
    n_cn = steps[5]["text"].count("[citation needed]")
    if n_cn != len(final_markers):
        probs.append(f"step 5 has {n_cn} [citation needed], final has {len(final_markers)} citation groups")
    for s in steps[6:8]:
        if final_markers and "\nReferences:\n" not in s["text"]:
            probs.append(f"no References list in step {s['step']}")
            continue
        for line in s["text"].split("\nReferences:\n")[1].split("\n") if "\nReferences:\n" in s["text"] else []:
            m = re.match(r"\[(\d+)\] (.*)", line)
            if m and refs.get(m.group(1)) != m.group(2):
                probs.append(f"reference [{m.group(1)}] not verbatim in step {s['step']}")
    allowed = set(re.findall(r"\d{3,}", src["text"] + " " + " ".join(v or "" for v in refs.values())))
    new = set()
    for s in steps:
        new |= set(re.findall(r"\d{3,}", body(s["text"]))) - allowed
    if new:
        probs.append(f"numbers not in final: {sorted(new)[:6]}")
    if any(len(s["text"].split()) < 3 for s in steps):
        probs.append("empty or near-empty step")
    return probs


def main(paths):
    bad = 0
    for p in paths:
        try:
            probs = check(p)
        except Exception as e:  # malformed JSON etc.
            probs = [f"unreadable: {e}"]
        bad += bool(probs)
        print(f"{os.path.basename(p)}: {'OK' if not probs else 'FAIL — ' + '; '.join(probs)}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
