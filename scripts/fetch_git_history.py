"""Extract every distinct version of one document from a git repository's history.

Usage: python3 scripts/fetch_git_history.py REPO_DIR PATH REPO_URL LICENSE > sources/github_history/<slug>.json

Follows renames (e.g. Rust RFC drafts start as text/0000-*.md and get numbered on merge).
Strips metadata headers (PEP RFC-2822 header block, RFC "- Feature Name:" bullet block) so that
status/date churn is not counted as drafting. Versions identical after stripping are collapsed.
The 5- and 9-step snapshots are chosen later by build_dataset.py.
"""
import json, re, subprocess, sys


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, check=True).stdout


def strip_header(text):
    lines = text.split("\n")
    if lines and re.match(r"^PEP:\s*\d+", lines[0]):  # PEP header block runs to first blank line
        lines = lines[lines.index("") + 1:] if "" in lines else lines
    else:  # RFC: leading "- Feature Name:", "- Start Date:", ... bullets
        i = 0
        while i < len(lines) and (re.match(r"^\s*-\s+[\w ()]+:", lines[i]) or not lines[i].strip()):
            i += 1
        if i and any(re.match(r"^\s*-\s+(Feature Name|Start Date|RFC PR|Rust Issue)", l) for l in lines[:i]):
            lines = lines[i:]
    return "\n".join(lines).strip()


def main(repo, path, repo_url, license_):
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
    slug = re.sub(r"^\d+-", "", path.rsplit("/", 1)[-1].rsplit(".", 1)[0])
    title = slug.replace("-", " ").replace("_", " ")  # RFCs: the file slug is the only title
    head = git(repo, "show", f"HEAD:{path}")
    m = re.search(r"^Title:\s*(.+)$", head, re.M)  # PEPs carry the title in the header
    json.dump({
        "source_type": "git_document_history", "source_id": f"{repo_url}/blob/{git(repo, 'rev-parse', 'HEAD').strip()}/{path}",
        "title": m.group(1).strip() if m else title, "repo": repo_url, "path": path, "license": license_,
        "total_commits": len(entries), "distinct_versions": len(versions), "versions": versions,
    }, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main(*sys.argv[1:])
