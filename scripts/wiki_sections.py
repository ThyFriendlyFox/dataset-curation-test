"""Pick one cited section from each Wikipedia article in the "section" pool (approach A / D).

Usage: (cd scripts && python3 wiki_sections.py ../sources/wiki_cs_articles.json ../sources/wiki_sections)

Fetches current wikitext 20 articles per request (rate-limit friendly), converts it with
wikitext.convert, splits it at '## ' headings, and keeps the section (including its '### '
subsections) with the most citations among those of 250–1300 words with >= 3 citation groups.
Markers are renumbered within the section. Writes OUT_DIR/wiki_<slug>.json in the same format as
fetch_wikipedia.py output; articles with no qualifying section are recorded in OUT_DIR/_rejected.txt.
"""
import json, os, re, sys, urllib.parse
from fetch_wiki_history import get
from wikitext import convert

CITE = re.compile(r"\[(\d+(?:,\d+)*)\]")


def sections(text):
    """Yield (heading, body) for each top-level '## ' section; the lead is ('Lead', ...)."""
    parts = re.split(r"(?m)^## (.+)$", text)
    yield "Lead", parts[0].strip()
    for i in range(1, len(parts), 2):
        yield parts[i].strip(), parts[i + 1].strip()


def renumber(body, refs):
    by_n = {r["n"]: r["text"] for r in refs}
    order = []
    for m in CITE.finditer(body):
        for n in m.group(1).split(","):
            if int(n) not in order: order.append(int(n))
    remap = {o: i + 1 for i, o in enumerate(order)}
    body = CITE.sub(lambda m: "[" + ",".join(str(remap[int(n)]) for n in m.group(1).split(",")) + "]", body)
    return body, [{"n": remap[o], "text": by_n[o]} for o in order if o in by_n]


def best_section(text, refs):
    best = None
    for head, body in sections(text):
        words, groups = len(body.split()), len(CITE.findall(body))
        if 250 <= words <= 1300 and groups >= 3 and (best is None or groups > best[2]):
            best = (head, body, groups)
    return best


def main(articles_path, out):
    os.makedirs(out, exist_ok=True)
    titles = [a["title"] for a in json.load(open(articles_path)) if a["pool"] == "section"]
    rej_path = os.path.join(out, "_rejected.txt")
    rejected = set(open(rej_path).read().split("\n")) if os.path.exists(rej_path) else set()
    slug = lambda t: re.sub(r"[^A-Za-z0-9_]", "", t.replace(" ", "_"))
    todo = [t for t in titles if t not in rejected and not os.path.exists(os.path.join(out, f"wiki_{slug(t)}.json"))]
    kept = 0
    with open(rej_path, "a") as rej:
        for i in range(0, len(todo), 20):
            d = get({"action": "query", "prop": "revisions", "titles": "|".join(todo[i:i + 20]),
                     "rvprop": "ids|timestamp|content", "rvslots": "main"})
            for page in d["query"]["pages"]:
                revs = page.get("revisions")
                if not revs or "content" not in revs[0]["slots"]["main"]:
                    continue  # content omitted (size cap) — picked up on a later run
                rev = revs[0]
                text, refs = convert(rev["slots"]["main"]["content"])
                pick = best_section(text, refs)
                if pick is None:
                    rej.write(page["title"] + "\n"); rej.flush()
                    continue
                head, body, _ = pick
                body, srefs = renumber(body, refs)
                t = urllib.parse.quote(page["title"].replace(" ", "_"), safe="")
                row = {"source_type": "encyclopedia_article", "source_id": f"enwiki:{page['title']}#rev{rev['revid']}",
                       "title": page["title"], "authors": "Wikipedia contributors", "year": rev["timestamp"][:4],
                       "url": f"https://en.wikipedia.org/w/index.php?title={t}&oldid={rev['revid']}",
                       "license": "https://creativecommons.org/licenses/by-sa/4.0/", "section": head,
                       "word_count": len(body.split()), "text": body, "references": srefs}
                path = os.path.join(out, f"wiki_{slug(page['title'])}.json")
                with open(path + ".tmp", "w", encoding="utf-8") as f:
                    json.dump(row, f, indent=2, ensure_ascii=False)
                os.replace(path + ".tmp", path)
                kept += 1
            print(f"{min(i + 20, len(todo))}/{len(todo)} fetched, kept {kept}", flush=True)
    print(f"DONE kept {kept}", flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])
