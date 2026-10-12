"""Harvest openly licensed arXiv CS paper introductions for approach A / D.

Usage: (cd scripts && python3 harvest_arxiv.py OUT_DIR FROM_DATE UNTIL_DATE [MAX_PAPERS])

1. OAI-PMH ListRecords over set=cs (by metadata datestamp), keeping papers whose license is
   CC BY / CC BY-SA / CC0 and whose *primary* category is cs.*.
2. For each, extract the Introduction (fetch_arxiv.extract) and keep it if it is 250–1300 words,
   cites >= 3 distinct references, and every cited reference resolved to bibliography text.
Writes OUT_DIR/arxiv_<id>.json; resumable (skips ids already written or listed in OUT_DIR/_rejected.txt).
"""
import os, re, sys, time
import json
import requests
from bs4 import BeautifulSoup
from fetch_arxiv import ALLOWED, UA, extract

OAI = "https://oaipmh.arxiv.org/oai"


def oai_records(frm, until):
    params = {"verb": "ListRecords", "set": "cs", "metadataPrefix": "arXiv", "from": frm, "until": until}
    while True:
        for wait in (0, 10, 30, 60, 120, 300):
            time.sleep(wait)
            r = requests.get(OAI, params=params, headers=UA, timeout=120)
            if r.status_code == 200:
                break
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "xml")
        for rec in soup.find_all("arXiv"):
            yield rec
        tok = soup.find("resumptionToken")
        if not tok or not tok.text.strip():
            return
        params = {"verb": "ListRecords", "resumptionToken": tok.text.strip()}


def main(out, frm, until, max_papers=10**9):
    os.makedirs(out, exist_ok=True)
    rej_path = os.path.join(out, "_rejected.txt")
    rejected = set(open(rej_path).read().split()) if os.path.exists(rej_path) else set()
    kept = len([f for f in os.listdir(out) if f.startswith("arxiv_")])
    seen = 0
    with open(rej_path, "a") as rej:
        for meta in oai_records(frm, until):
            aid = meta.id.text.strip()
            cats = meta.categories.text.split() if meta.categories else []
            lic = meta.license.text if meta.license else ""
            path = os.path.join(out, f"arxiv_{aid.replace('/', '_')}.json")
            if not cats or not cats[0].startswith("cs.") or not ALLOWED.search(lic):
                continue
            seen += 1
            if aid in rejected or os.path.exists(path):
                continue
            try:
                row = extract(aid, meta)
                n_cited = len(row["references"])
                if not (250 <= row["word_count"] <= 1300):
                    raise ValueError(f"length {row['word_count']}")
                if n_cited < 3 or any(r["text"] is None for r in row["references"]):
                    raise ValueError(f"citations {n_cited}")
            except Exception as e:  # network errors and unusable papers alike: skip, don't retry forever
                rej.write(aid + "\n"); rej.flush()
                time.sleep(1)
                continue
            with open(path + ".tmp", "w", encoding="utf-8") as f:
                json.dump(row, f, indent=2, ensure_ascii=False)
            os.replace(path + ".tmp", path)
            kept += 1
            if kept % 25 == 0:
                print(f"kept {kept} (open-licensed cs candidates seen {seen})", flush=True)
            if kept >= int(max_papers):
                break
            time.sleep(1)
    print(f"DONE kept {kept}, seen {seen}", flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])
