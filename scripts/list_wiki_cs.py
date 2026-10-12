"""List English Wikipedia computer-science articles from a set of CS categories (+ one level of
subcategories, via PetScan), with page length, and assign each article to exactly one pool.

Usage: (cd scripts && python3 list_wiki_cs.py) > sources/wiki_cs_articles.json

Pools are disjoint so no document appears in two approaches:
  "history"  → B / D(B-part): revision-history trajectories
  "section"  → A / D(A-part): one cited section, reconstructed backwards
Assignment is a stable hash of the title (1 in 3 → section).
"""
import hashlib, json, sys, time
import requests
from fetch_wiki_history import UA

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
# trial documents keep their trial approach
FORCE = {**{t: "section" for t in ("Turing machine", "Halting problem", "Quicksort", "Hash table", "Lambda calculus",
                                   "ENIAC", "Dijkstra's algorithm", "Garbage collection (computer science)",
                                   "Public-key cryptography", "Compiler")},
         **{t: "history" for t in ("Bloom filter", "Skip list", "Merkle tree", "Trie", "Rope (data structure)",
                                   "Fenwick tree", "Bogosort", "Byzantine fault", "Two Generals' Problem",
                                   "Dining philosophers problem", "Huffman coding", "Levenshtein distance",
                                   "Rabin–Karp algorithm")}}


PETSCAN = "https://petscan.wmcloud.org/"


def petscan(cat, depth=1):
    """Articles (ns 0) in a category tree, with page length — one request via PetScan (Toolforge),
    which spares the rate-limited Wikipedia API."""
    for wait in (0, 20, 60, 120):
        time.sleep(wait)
        r = requests.get(PETSCAN, timeout=300, headers=UA, params={
            "language": "en", "project": "wikipedia", "categories": cat.replace(" ", "_"), "depth": depth,
            "ns[0]": 1, "format": "json", "doit": 1})
        if r.ok:
            return {p["title"].replace("_", " "): p["len"] for p in r.json()["*"][0]["a"]["*"]}
    print(f"  skipped {cat}: HTTP {r.status_code}", file=sys.stderr, flush=True)
    return {}


def main():
    sizes = {}
    for root in ROOTS:
        sizes.update(petscan(root))
        print(f"{root}: {len(sizes)} titles so far", file=sys.stderr, flush=True)
    rows = []
    for t, n in sorted(sizes.items()):
        if MIN_BYTES <= n <= MAX_BYTES and not t.startswith(("List of", "Outline of", "Comparison of", "Timeline of")):
            h = int(hashlib.sha1(t.encode()).hexdigest(), 16)
            rows.append({"title": t, "bytes": n, "pool": FORCE.get(t, "section" if h % 3 == 0 else "history")})
    json.dump(rows, sys.stdout, indent=1, ensure_ascii=False)
    print(f"{len(rows)} articles ({sum(r['pool'] == 'history' for r in rows)} history, "
          f"{sum(r['pool'] == 'section' for r in rows)} section)", file=sys.stderr)


if __name__ == "__main__":
    main()
