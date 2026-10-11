"""Fetch one section of an English Wikipedia article with its footnoted references.

Usage: python3 scripts/fetch_wikipedia.py "Article title" "section-title-regex" > sources/<slug>.json
Uses the Parsoid HTML (each heading's content is wrapped in a <section>); text is CC BY-SA 4.0.
"""
import json, re, sys, time, urllib.parse
import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "dataset-curation-test/0.1 (https://github.com/ThyFriendlyFox/dataset-curation-test) python-requests"}


def get(url, **kw):
    """GET with backoff on 429 (Wikimedia rate limits anonymous REST traffic)."""
    for wait in (0, 10, 30, 60, 120):
        time.sleep(wait)
        r = requests.get(url, headers=UA, timeout=60, **kw)
        if r.status_code != 429:
            r.raise_for_status()
            return r
    r.raise_for_status()


def clean(s):
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\s+([,.;:)])", r"\1", s).replace("( ", "(")


def main(title, sec_re):
    t = urllib.parse.quote(title.replace(" ", "_"), safe="")
    q = get("https://en.wikipedia.org/w/api.php", params={
        "action": "query", "prop": "revisions", "titles": title, "rvprop": "ids|timestamp",
        "redirects": 1, "format": "json", "formatversion": 2}).json()["query"]["pages"][0]
    rev, ts = q["revisions"][0]["revid"], q["revisions"][0]["timestamp"]
    html = get(f"https://en.wikipedia.org/w/rest.php/v1/revision/{rev}/html").text
    soup = BeautifulSoup(html, "lxml")
    sec = next((s for s in soup.find_all("section")
                if s.find(re.compile("^h2$"), recursive=True) and
                re.search(sec_re, s.find(re.compile("^h2$")).get_text(), re.I)), None)
    if sec is None:
        sys.exit(f"{title}: no h2 section matching {sec_re!r}")
    notes = {li["id"]: li for li in soup.select("ol.mw-references li[id]")}
    num = {}
    for sup in sec.select("sup.mw-ref"):
        a = sup.find("a", href=True)
        nid = a["href"].split("#")[-1] if a else None
        if nid in notes and "explanatory" not in " ".join(notes[nid].parent.get("class", [])) and \
                not sup.get("data-mw", "").count('"group"'):
            sup.replace_with(f"[{num.setdefault(nid, len(num) + 1)}]")
        else:
            sup.decompose()  # explanatory notes / footnote groups aren't citations
    for junk in sec.select("figure, table, style, .mw-empty-elt, .hatnote, .shortdescription, math, .mwe-math-element"):
        junk.decompose()
    blocks = []
    for el in sec.find_all(["h2", "h3", "h4", "p", "li"]):
        if el.find_parent(["li"]) and el.name == "li": continue
        txt = clean(el.get_text(" "))
        txt = re.sub(r"\]\s+\[", "][", txt).replace("][", ",")
        if not txt: continue
        if el.name == "h2": continue
        blocks.append(("## " if el.name in ("h3", "h4") else "- " if el.name == "li" else "") + txt)
    text = "\n\n".join(blocks)
    refs = []
    for nid, n in sorted(num.items(), key=lambda kv: kv[1]):
        body = notes[nid].select_one(".mw-reference-text")
        refs.append({"n": n, "id": nid, "text": clean(body.get_text(" ")) if body else None})
    json.dump({
        "source_type": "encyclopedia_article", "source_id": f"enwiki:{q['title']}#rev{rev}",
        "title": q["title"], "authors": "Wikipedia contributors", "year": ts[:4],
        "url": f"https://en.wikipedia.org/w/index.php?title={t}&oldid={rev}",
        "license": "https://creativecommons.org/licenses/by-sa/4.0/",
        "section": clean(sec.find("h2").get_text(" ")),
        "word_count": len(text.split()), "text": text, "references": refs,
    }, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main(*sys.argv[1:])
