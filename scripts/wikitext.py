"""Convert raw wikitext to plain prose with numbered [n] citation markers and a reference list.

Shared by the revision-history builder, which has to work on old revisions (wikitext only,
no rendered HTML). Keeps section headings as '## ' lines; drops infoboxes, tables, files, and
navigation templates.
"""
import re
import mwparserfromhell as mwp

CITE_FIELDS = ("author", "last", "last1", "first", "first1", "title", "journal", "work", "website",
               "publisher", "date", "year", "volume", "issue", "pages", "doi", "url", "isbn")
DROP_SECTIONS = re.compile(r"^(see also|references|notes|footnotes|further reading|external links|bibliography|sources|citations)$", re.I)
KEEP_INLINE = {"lang", "nowrap", "math", "mvar", "var", "code", "tt", "abbr", "small", "sic"}


def _format_cite(code):
    """Render a <ref> body (usually a {{cite ...}} template) as one line."""
    tpls = code.filter_templates(recursive=False)
    t = next((t for t in tpls if str(t.name).strip().lower().startswith(("cite", "citation"))), None)
    if t is None:
        return re.sub(r"\s+", " ", code.strip_code()).strip() or None
    f = {str(p.name).strip(): re.sub(r"\s+", " ", mwp.parse(str(p.value)).strip_code()).strip()
         for p in t.params if str(p.name).strip() in CITE_FIELDS}
    author = f.get("author") or ", ".join(x for x in (f.get("last") or f.get("last1"), f.get("first") or f.get("first1")) if x)
    when = f.get("year") or f.get("date", "")
    venue = f.get("journal") or f.get("work") or f.get("website") or f.get("publisher") or ""
    parts = [author and f"{author}.", when and f"({when}).", f.get("title") and f"{f['title']}.",
             venue and f"{venue}.", f.get("doi") and f"doi:{f['doi']}", not f.get("doi") and f.get("url")]
    return " ".join(p for p in parts if p) or None


def convert(wikitext):
    """Return (text, references) for a full article's wikitext."""
    code = mwp.parse(wikitext)
    # Pass 1: definitions of named refs anywhere in the article (incl. list-defined refs).
    named = {}
    for tag in code.filter_tags(matches=lambda n: str(n.tag).lower() == "ref"):
        name = tag.get("name").value.strip().strip('"') if tag.has("name") else None
        if name and tag.contents and str(tag.contents).strip():
            named.setdefault(name, _format_cite(tag.contents))
    nums, refs = {}, []

    def ref_marker(tag):
        if tag.has("group"):
            return ""  # explanatory footnote group, not a citation
        name = tag.get("name").value.strip().strip('"') if tag.has("name") else None
        key = name or str(tag.contents).strip()
        if not key:
            return ""
        if key not in nums:
            body = named.get(name) if name else None
            body = body or (_format_cite(tag.contents) if tag.contents else None)
            if not body:
                return ""
            nums[key] = len(nums) + 1
            refs.append({"n": nums[key], "text": body})
        return f"⟦c{nums[key]}⟧"  # placeholder: literal "[0]" (array indexing etc.) must not look like a citation

    for tag in code.filter_tags(recursive=True, matches=lambda n: str(n.tag).lower() == "ref"):
        try:
            code.replace(tag, ref_marker(tag))
        except ValueError:
            pass  # already removed with a parent node
    for tag in code.filter_tags(matches=lambda n: str(n.tag).lower() == "math"):
        try: code.replace(tag, " " + str(tag.contents).strip() + " ")  # keep formulas as TeX
        except ValueError: pass
    for tag in code.filter_tags(matches=lambda n: str(n.tag).lower() in ("references", "gallery", "table", "syntaxhighlight", "source", "pre", "score")):
        try: code.remove(tag)
        except ValueError: pass
    for h in code.filter_headings():
        title = re.sub(r"\s+", " ", mwp.parse(str(h.title)).strip_code()).strip()
        # placeholder: a literal "#" at line start would be re-parsed as a wikitext list item
        try: code.replace(h, "\n" + ("⟦H2⟧ " if h.level <= 2 else "⟦H3⟧ ") + title + "\n")
        except ValueError: pass
    for t in code.filter_templates(recursive=False):
        name = str(t.name).strip().lower()
        try:
            if name in KEEP_INLINE and t.params:
                code.replace(t, str(t.params[-1].value))
            else:
                code.remove(t)
        except ValueError:
            pass
    for link in code.filter_wikilinks():
        target = str(link.title).strip().lower()
        try:
            if target.startswith(("file:", "image:", "category:")):
                code.remove(link)
        except ValueError:
            pass
    text = code.strip_code(normalize=True, collapse=True).replace("⟦H2⟧", "##").replace("⟦H3⟧", "###")
    text = re.sub(r"\{\|.*?\|\}", "", text, flags=re.S)  # leftover tables
    blocks, skip = [], False
    for line in text.split("\n"):
        m = re.match(r"^(#{2,3}) (.*)$", line.strip())
        if m:
            skip = bool(DROP_SECTIONS.match(m.group(2).strip()))
            if not skip:
                blocks.append(m.group(1) + " " + m.group(2).strip())
            continue
        if skip:
            continue
        line = re.sub(r"\s+", " ", line).strip()
        if line and not re.fullmatch(r"[\W\d_]*", line):
            blocks.append(line)
    out = "\n\n".join(blocks)
    # Group adjacent citation placeholders, renumber by first use in the surviving text, render as [n,m].
    order = []
    for m in re.finditer(r"⟦c(\d+)⟧", out):
        if int(m.group(1)) not in order: order.append(int(m.group(1)))
    remap = {old: i + 1 for i, old in enumerate(order)}
    out = re.sub(r"(?:⟦c\d+⟧\s*)*⟦c\d+⟧", lambda m: "[" + ",".join(
        dict.fromkeys(str(remap[int(n)]) for n in re.findall(r"⟦c(\d+)⟧", m.group(0)))) + "]", out)
    by_old = {r["n"]: r["text"] for r in refs}
    return out, [{"n": remap[o], "text": by_old[o]} for o in order]
