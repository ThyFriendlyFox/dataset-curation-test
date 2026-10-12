"""Mark off-topic articles in sources/wiki_cs_articles.json using Wikidata "instance of" (P31).

Usage: (cd scripts && python3 topic_filter.py ../sources/wiki_cs_articles.json)

CS categories also contain products, companies, people and services (e.g. phone models, a
messaging app, biographies). An article is marked topic_ok=false when its Wikidata item is an
instance of (a subclass of) one of EXCLUDE; concepts, algorithms, theorems, languages and
protocols stay. Titles map to Wikidata items via PetScan; P31 is queried in batches over SPARQL.
"""
import json, sys, time
import requests
from fetch_wiki_history import UA
from list_wiki_cs import ROOTS, PETSCAN

EXCLUDE = {
    "Q5": "human", "Q43229": "organization", "Q4830453": "business", "Q7397": "software",
    "Q2424752": "product", "Q1172284": "dataset", "Q35127": "website", "Q1668024": "service",
    "Q15416": "television program", "Q7889": "video game", "Q1656682": "event",
}
# ...unless it is also one of these (e.g. a programming language is also "software")
KEEP = {"Q9143": "programming language", "Q8366": "algorithm", "Q175263": "data structure",
        "Q15836568": "communication protocol", "Q235557": "file format", "Q7184903": "abstract data type"}
SPARQL = "https://query.wikidata.org/sparql"


def qids():
    out = {}
    for root in ROOTS:
        for wait in (0, 20, 60):
            time.sleep(wait)
            r = requests.get(PETSCAN, timeout=300, headers=UA, params={
                "language": "en", "project": "wikipedia", "categories": root.replace(" ", "_"), "depth": 1,
                "ns[0]": 1, "format": "json", "doit": 1})
            if r.ok:
                for p in r.json()["*"][0]["a"]["*"]:
                    if p.get("q"):
                        out[p["title"].replace("_", " ")] = p["q"]
                break
    return out


def matching(items, classes):
    """{qid: class label} for items that are instances of (a subclass of) one of `classes`."""
    found = {}
    values = " ".join(f"wd:{c}" for c in classes)
    for i in range(0, len(items), 250):
        batch = " ".join(f"wd:{q}" for q in items[i:i + 250])
        query = (f"SELECT DISTINCT ?item ?c WHERE {{ VALUES ?item {{ {batch} }} VALUES ?c {{ {values} }} "
                 f"?item wdt:P31/wdt:P279* ?c . }}")
        for wait in (0, 10, 60):
            time.sleep(wait)
            r = requests.get(SPARQL, params={"query": query}, timeout=300,
                             headers={**UA, "Accept": "application/sparql-results+json"})
            if r.ok:
                for b in r.json()["results"]["bindings"]:
                    found.setdefault(b["item"]["value"].rsplit("/", 1)[1], classes[b["c"]["value"].rsplit("/", 1)[1]])
                break
        else:
            r.raise_for_status()
        print(f"  checked {min(i + 250, len(items))}/{len(items)}", file=sys.stderr, flush=True)
    return found


def main(path):
    rows = json.load(open(path))
    title_q = qids()
    items = sorted({title_q[r["title"]] for r in rows if r["title"] in title_q})
    keep = matching(items, KEEP)
    bad = {q: why for q, why in matching(items, EXCLUDE).items() if q not in keep}
    for r in rows:
        q = title_q.get(r["title"])
        r["wikidata"] = q
        r["topic_ok"] = q not in bad
        if q in bad:
            r["excluded_as"] = bad[q]
    json.dump(rows, open(path, "w"), indent=1, ensure_ascii=False)
    n_bad = sum(not r["topic_ok"] for r in rows)
    print(f"{n_bad} of {len(rows)} marked off-topic", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1])
