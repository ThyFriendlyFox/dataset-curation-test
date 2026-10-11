"""Fetch one section (default: Introduction) of an openly licensed arXiv paper, with its cited references.

Usage: python3 scripts/fetch_arxiv.py ARXIV_ID [section-title-regex] > sources/ARXIV_ID.json
License comes from arXiv OAI-PMH metadata; only CC BY / CC BY-SA / CC0 are accepted.
Text comes from arXiv's HTML rendering (LaTeXML), falling back to ar5iv for older papers.
"""
import json, re, sys
import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "dataset-curation-test/0.1 (https://github.com/ThyFriendlyFox/dataset-curation-test) python-requests"}
ALLOWED = re.compile(r"creativecommons\.org/(licenses/by(-sa)?/|publicdomain/zero)")


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def main(aid, sec_re="introduction"):
    oai = requests.get("https://oaipmh.arxiv.org/oai", headers=UA, timeout=60, params={
        "verb": "GetRecord", "identifier": f"oai:arXiv.org:{aid}", "metadataPrefix": "arXiv"}).text
    meta = BeautifulSoup(oai, "xml").find("arXiv")
    lic = meta.license.text if meta.license else ""
    if not ALLOWED.search(lic):
        sys.exit(f"{aid}: license not CC BY/BY-SA/CC0: {lic!r}")
    html = None
    for url in (f"https://arxiv.org/html/{aid}", f"https://ar5iv.labs.arxiv.org/html/{aid}"):
        r = requests.get(url, headers=UA, timeout=60)
        if r.ok and "ltx_document" in r.text:
            html, src_url = r.text, url
            break
    if html is None:
        sys.exit(f"{aid}: no HTML rendering available")
    soup = BeautifulSoup(html, "lxml")
    sec = next((s for s in soup.select("section.ltx_section")
                if re.search(sec_re, s.find(re.compile("^h[1-6]$")).get_text(), re.I)), None)
    if sec is None:
        sys.exit(f"{aid}: no section matching {sec_re!r}")
    bib = {li["id"]: clean(li.get_text(" ")) for li in soup.select("li.ltx_bibitem")}
    num = {}
    # Replace each citation group with [n,...] markers keyed by first appearance.
    for cite in sec.select("cite.ltx_cite"):
        ids = []
        for a in cite.select("a[href*='#bib']"):
            bid = a["href"].split("#")[-1]
            if bid not in ids: ids.append(bid)
        cite.replace_with("[" + ",".join(str(num.setdefault(b, len(num) + 1)) for b in ids) + "]" if ids else "")
    for m in sec.select("math"):
        m.replace_with(m.get("alttext", ""))
    for junk in sec.select("figure, .ltx_note, .ltx_tag_section, table"):
        junk.decompose()
    blocks = []
    for el in sec.select("h3, h4, .ltx_para > p, .ltx_para > .ltx_itemize li, .ltx_para > .ltx_enumerate li"):
        t = clean(el.get_text(" "))
        t = re.sub(r"\s+([,.;:)])", r"\1", t).replace("( ", "(")
        if not t: continue
        if el.name in ("h3", "h4"): blocks.append("## " + t)
        elif el.name == "li": blocks.append("- " + t)
        else: blocks.append(t)
    text = "\n\n".join(dict.fromkeys(blocks))  # nested li/p can repeat; keep first
    refs = [{"n": n, "id": b, "text": re.sub(r"^\[?\d+\]?\s*", "", bib.get(b, "")) or None}
            for b, n in sorted(num.items(), key=lambda kv: kv[1])]
    authors = [clean(f"{a.forenames.text if a.forenames else ''} {a.keyname.text}") for a in meta.find_all("author")]
    json.dump({
        "source_type": "research_paper", "source_id": f"arXiv:{aid}",
        "title": clean(meta.title.text), "authors": ", ".join(authors),
        "year": meta.created.text[:4], "categories": meta.categories.text.split(),
        "url": f"https://arxiv.org/abs/{aid}", "html_url": src_url, "license": lic,
        "section": clean(sec.find(re.compile("^h[1-6]$")).get_text(" ")),
        "word_count": len(text.split()), "text": text, "references": refs,
    }, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main(*sys.argv[1:])
