"""List English Wikipedia computer-science articles from a set of CS categories (+ one level of
subcategories), with page length, and assign each article to exactly one pool.

Usage: (cd scripts && python3 list_wiki_cs.py) > sources/wiki_cs_articles.json

Pools are disjoint so no document appears in two approaches:
  "history"  → B / D(B-part): revision-history trajectories
  "section"  → A / D(A-part): one cited section, reconstructed backwards
Assignment is a stable hash of the title (1 in 3 → section).
"""
import hashlib, json, sys
from fetch_wiki_history import get

ROOTS = [
    "Data structures", "Algorithms", "Sorting algorithms", "Search algorithms", "Graph algorithms",
    "String algorithms", "Cryptographic algorithms", "Cryptography", "Distributed computing problems",
    "Distributed algorithms", "Concurrency control", "Concurrent computing", "Programming language concepts",
    "Programming paradigms", "Type theory", "Compiler construction", "Compiler optimizations",
    "Computational complexity theory", "Theory of computation", "Formal languages", "Automata (computation)",
    "Computer architecture", "Operating system technology", "Memory management", "Computer networking",
    "Network protocols", "Machine learning algorithms", "Artificial neural networks", "Information theory",
    "Error detection and correction", "Data compression", "Databases", "Computer graphics algorithms",
    "Numerical analysis", "Software engineering", "Computer security", "Computability theory",
    "Logic in computer science", "Randomized algorithms", "Approximation algorithms", "History of computing",
]
MIN_BYTES, MAX_BYTES = 6_000, 90_000


def members(cat, cmtype):
    out, cont = [], {}
    while True:
        d = get({"action": "query", "list": "categorymembers", "cmtitle": f"Category:{cat}",
                 "cmtype": cmtype, "cmlimit": 500, **cont})
        out += [m["title"] for m in d["query"]["categorymembers"]]
        if "continue" not in d:
            return out
        cont = d["continue"]


def main():
    titles = set()
    for root in ROOTS:
        cats = [root] + [c.split(":", 1)[1] for c in members(root, "subcat")]
        for c in cats:
            titles.update(t for t in members(c, "page") if not t.startswith(("List of", "Outline of", "Comparison of", "Timeline of")))
        print(f"{root}: {len(titles)} titles so far", file=sys.stderr)
    titles = sorted(titles)
    sizes = {}
    for i in range(0, len(titles), 50):
        d = get({"action": "query", "prop": "info", "titles": "|".join(titles[i:i + 50])})
        for p in d["query"]["pages"]:
            if "missing" not in p and p.get("ns") == 0:
                sizes[p["title"]] = p["length"]
    rows = []
    for t, n in sorted(sizes.items()):
        if MIN_BYTES <= n <= MAX_BYTES:
            h = int(hashlib.sha1(t.encode()).hexdigest(), 16)
            rows.append({"title": t, "bytes": n, "pool": "section" if h % 3 == 0 else "history"})
    json.dump(rows, sys.stdout, indent=1, ensure_ascii=False)
    print(f"{len(rows)} articles ({sum(r['pool'] == 'history' for r in rows)} history, "
          f"{sum(r['pool'] == 'section' for r in rows)} section)", file=sys.stderr)


if __name__ == "__main__":
    main()
