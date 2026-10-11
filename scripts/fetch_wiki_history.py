"""Build a real draft trajectory from an English Wikipedia article's revision history.

Usage: python3 scripts/fetch_wiki_history.py "Article title" > sources/wiki_history/<slug>.json

Saves converted text for a pool of candidate revisions (first real version → current), skipping
revisions later reverted (tag mw-reverted) and redirects. The 5- and 9-step snapshots are chosen
later from this pool by build_dataset.py, by growth toward the final text.
"""
import json, re, sys, time
import requests
from wikitext import convert

UA = {"User-Agent": "dataset-curation-test/0.1 (https://github.com/ThyFriendlyFox/dataset-curation-test) python-requests"}
API = "https://en.wikipedia.org/w/api.php"
POOL = 16  # per sampling angle; ~35-45 candidate revisions per article after merging


def get(params):
    """GET with patient backoff on 429, honoring Retry-After (Wikimedia rate-limits shared egress IPs)."""
    wait = 1
    for _ in range(15):
        time.sleep(wait)
        r = requests.get(API, params={**params, "format": "json", "formatversion": 2}, headers=UA, timeout=60)
        if r.status_code != 429:
            r.raise_for_status()
            return r.json()
        wait = min(300, max(int(r.headers.get("retry-after") or 30) + 5, wait * 2))
    r.raise_for_status()


def history(title):
    revs, cont = [], {}
    while True:
        d = get({"action": "query", "prop": "revisions", "titles": title, "redirects": 1, "rvlimit": 500,
                 "rvdir": "newer", "rvprop": "ids|timestamp|size|tags|comment", **cont})
        page = d["query"]["pages"][0]
        revs += page.get("revisions", [])
        if "continue" not in d:
            return page["title"], revs
        cont = d["continue"]


def wikitexts(revids, batch=10):
    """Content of many revisions; batched (one request per `batch` revids) to stay under rate limits."""
    out = {}
    for i in range(0, len(revids), batch):
        d = get({"action": "query", "prop": "revisions", "revids": "|".join(map(str, revids[i:i + batch])),
                 "rvprop": "ids|content", "rvslots": "main"})
        for page in d["query"]["pages"]:
            for r in page.get("revisions", []):
                out[r["revid"]] = r["slots"]["main"].get("content", "")
    return out


def main(title):
    title, revs = history(title)
    good = [r for r in revs if "mw-reverted" not in r.get("tags", []) and r["size"] > 300]
    final = revs[-1]
    # Candidate pool, from three angles (articles reach full size early and are then rewritten for
    # years at similar size, so size alone misses the late, near-final versions):
    #   1. byte-size growth (stub → full length)
    #   2. evenly spaced through the edit history
    #   3. geometrically closer to the present (n/2, n/4, ... edits before the current version)
    n = len(good)
    picks = set()
    for i in range(POOL):
        t = final["size"] * (i / (POOL - 1)) ** 1.5
        picks.add(next((j for j, r in enumerate(good) if r["size"] >= t), n - 1))
        picks.add(round((n - 1) * i / (POOL - 1)))
    step = n // 2
    while step >= 1:
        picks.add(n - 1 - step)
        step //= 2
    pool = [good[j] for j in sorted(p for p in picks if 0 <= p < n)]
    if not pool or pool[-1]["revid"] != final["revid"]:
        pool.append(final)
    snaps = []
    raws = wikitexts([r["revid"] for r in pool])
    for r in pool:
        raw = raws.get(r["revid"], "")
        if raw.lstrip().upper().startswith("#REDIRECT"):
            continue
        text, refs = convert(raw)
        snaps.append({"revid": r["revid"], "timestamp": r["timestamp"], "bytes": r["size"],
                      "comment": r.get("comment", ""), "word_count": len(text.split()),
                      "text": text, "references": refs, "wikitext": raw})  # raw kept so conversion can be redone offline
    json.dump({
        "source_type": "wikipedia_revision_history", "source_id": f"enwiki:{title}",
        "title": title, "authors": "Wikipedia contributors",
        "url": f"https://en.wikipedia.org/w/index.php?title={title.replace(' ', '_')}&action=history",
        "license": "https://creativecommons.org/licenses/by-sa/4.0/",
        "total_revisions": len(revs), "reverted_or_tiny_skipped": len(revs) - len(good),
        "snapshots": snaps,
    }, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1])
