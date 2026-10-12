"""Extract every distinct version of design documents from a git repository's history.

Single document:  python3 scripts/fetch_git_history.py REPO_DIR PATH REPO_URL LICENSE > out.json
Whole repo:       python3 scripts/fetch_git_history.py --batch REPO_DIR GLOB REPO_URL LICENSE PREFIX OUT_DIR

Follows renames (e.g. Rust RFC drafts start as text/0000-*.md and get numbered on merge).
Strips metadata headers (PEP RFC-2822 block, YAML front matter, "- Feature Name:" / "* Proposal:" /
"Author(s):" style lines at the top) so status/date churn is not counted as drafting. Versions
identical after stripping are collapsed. Snapshots are chosen later by build_dataset.py.
Batch mode keeps documents with >= MIN_VERSIONS distinct versions and a final of
MIN_WORDS..MAX_WORDS words, and writes PREFIX_<slug>.json.gz files.
"""
import fnmatch, gzip, json, os, re, subprocess, sys

MIN_VERSIONS, MIN_WORDS, MAX_WORDS = 5, 400, 8000
META_KEYS = (r"Feature Name|Start Date|RFC PR|Rust Issue|Proposals?|Authors?|Author\(s\)|Review Managers?|Status|"
             r"Implementation|Upcoming Feature Flag|Decision Notes|Bugs?|Previous Revisions?|Previous Proposal|Reviews?|"
             r"Type|Issues?|Prototype|Discussion(?: at)?|Last [Uu]pdated|Created|Requires|Category|Version|Target|"
             r"Contributors?|Champions?|YouTrack issue|Design|Pitch|Vision|Roadmap|Review thread|Shepherd")
META_LINE = re.compile(rf"^\s*(?:[-*]\s+)?\**\s*(?:{META_KEYS})\s*\**\s*(?:\(s\))?\s*\**\s*:")


# Go design docs open with "Name\" byline lines and a date line
DATE_OR_BYLINE = re.compile(r"^\s*(?:[A-Z][\w.'-]+(?: [A-Z][\w.'-]+){0,3}\s*\\|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\.? \d{1,2},? \d{4}|\d{4}-\d{2}-\d{2})\s*$")


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, check=True).stdout


def strip_header(text):
    """Remove the document's metadata header, keeping a leading '# Title' line."""
    if text.startswith("---\n") and "\n---" in text[4:]:  # YAML front matter (EIPs, Scala SIPs)
        text = text[4:].split("\n---", 1)[1].lstrip("-\n")
    lines = text.split("\n")
    if lines and re.match(r"^PEP:\s*\d+", lines[0]):  # PEP header block runs to the first blank line
        return "\n".join(lines[lines.index("") + 1:] if "" in lines else lines).strip()
    out, in_header = [], True
    for i, line in enumerate(lines):
        if in_header:
            if META_LINE.match(line) or DATE_OR_BYLINE.match(line):
                continue
            # header ends at the first section heading or first real paragraph line
            if re.match(r"^#{2,}\s", line) or (line.strip() and not line.startswith("# ") and len(line.split()) > 12
                                               and not META_LINE.match(line)):
                in_header = False
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def title_of(raw_head, final_text, path):
    m = re.search(r"^Title:\s*(.+)$", raw_head, re.M)  # PEP header
    if m: return m.group(1).strip()
    m = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", raw_head.split("\n---", 2)[0] if raw_head.startswith("---") else "", re.M)
    if m: return m.group(1).strip()  # YAML front matter
    m = re.search(r"^#\s+(.+)$", final_text, re.M)
    if m and m.group(1).strip().lower() not in ("summary", "abstract", "motivation"):
        return re.sub(r"^\s*(SE-\d+|KEEP-\d+|SIP-\d+)\s*[:-]\s*", r"\1: ", m.group(1).strip())
    slug = re.sub(r"^\d+-", "", path.rsplit("/", 1)[-1].rsplit(".", 1)[0])
    return slug.replace("-", " ").replace("_", " ")  # RFCs: the file slug is the only title


def history(repo, path, repo_url, license_):
    log = git(repo, "log", "--follow", "--format=%H%x09%cI%x09%s", "--name-only", "--", path)
    entries, cur = [], None
    for line in log.split("\n"):
        if "\t" in line:
            sha, date, subj = line.split("\t", 2)
            cur = {"sha": sha, "date": date, "subject": subj}
            entries.append(cur)
        elif line.strip() and cur is not None:
            cur["path"] = line.strip()
    entries.reverse()  # oldest first
    versions, prev = [], None
    for e in entries:
        try:
            raw = git(repo, "show", f"{e['sha']}:{e['path']}")
        except subprocess.CalledProcessError:
            continue  # file deleted in this commit
        body = strip_header(raw)
        if body == prev or not body:
            continue
        prev = body
        versions.append({"commit": e["sha"], "date": e["date"], "path": e["path"],
                         "commit_message": e["subject"], "word_count": len(body.split()), "text": body})
    head = git(repo, "show", f"HEAD:{path}")
    return {
        "source_type": "git_document_history", "source_id": f"{repo_url}/blob/{git(repo, 'rev-parse', 'HEAD').strip()}/{path}",
        "title": title_of(head, versions[-1]["text"] if versions else "", path), "repo": repo_url, "path": path,
        "license": license_, "total_commits": len(entries), "distinct_versions": len(versions), "versions": versions,
    }


def batch(repo, pattern, repo_url, license_, prefix, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    files = [f for f in git(repo, "ls-files").split("\n") if fnmatch.fnmatch(f, pattern)]
    # cheap pre-filter on commit counts (no blobs needed) before pulling every version
    counts = {}
    for line in git(repo, "log", "--format=", "--name-only").split("\n"):
        if line in files or line in counts:
            counts[line] = counts.get(line, 0) + 1
    kept = 0
    for f in files:
        slug = re.sub(r"[^A-Za-z0-9_.-]", "_", f.rsplit("/", 1)[-1].rsplit(".", 1)[0])
        out = os.path.join(out_dir, f"{prefix}_{slug}.json.gz")
        if os.path.exists(out):
            kept += 1
            continue
        if counts.get(f, 0) < MIN_VERSIONS and "rfcs" not in repo_url:  # RFC drafts live under other names
            continue
        try:
            d = history(repo, f, repo_url, license_)
        except subprocess.CalledProcessError:
            continue
        if d["distinct_versions"] < MIN_VERSIONS or not MIN_WORDS <= d["versions"][-1]["word_count"] <= MAX_WORDS:
            continue
        with gzip.open(out + ".tmp", "wt", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False)
        os.replace(out + ".tmp", out)
        kept += 1
    print(f"{prefix}: {len(files)} files, kept {kept}", flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "--batch":
        batch(*sys.argv[2:])
    else:
        json.dump(history(*sys.argv[1:]), sys.stdout, indent=2, ensure_ascii=False)
