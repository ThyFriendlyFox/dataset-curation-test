"""Assemble the full datasets: 4 approaches x {5-stage, 9-step}, each with train/validation/test splits.

Usage: python3 scripts/build_full.py
Writes data/full/<config>/{train,validation,test}.parquet, data/full/stats.json and
review/full/<config>/ sample pages. Row construction is shared with the trial (build_dataset.py).

Pools (no document is used by two approaches):
  A-type  every reconstruction in sources/reconstructed/ that passes validate_reconstruction
  B-type  sources/wiki_history/*.json (trial) + sources/wiki_history_full/*.json.gz
  C       sources/github_history/*.json (trial) + sources/github_history_full/*.json.gz
Wikipedia articles marked off-topic (topic_filter.py) are excluded from every pool.
D takes a disjoint share: 25% of the A-type pool plus 3 real-history rows for every 7 (B-type first,
topped up from C), so D is ~70/30 reconstructed/real like the trial. Trial rows keep their trial assignment. Assignment and splits are stable hashes.
B/C histories with too few distinct versions for a variant are left out of that variant, never padded.
"""
import glob, hashlib, json, os, sys
from multiprocessing import Pool
import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_dataset as bd
from validate_reconstruction import check as validate

ROOT, S = bd.ROOT, bd.S
VARIANTS = ("5stage", "9step")
SPLITS = (("train", 90), ("validation", 95), ("test", 100))


def h(s):
    return int(hashlib.sha1(s.encode()).hexdigest(), 16)


def split_of(row_id):
    v = h("split:" + row_id) % 100
    return next(name for name, upper in SPLITS if v < upper)


def stem(path):
    b = os.path.basename(path)
    return b[:-8] if b.endswith(".json.gz") else b[:-5]


def off_topic():
    """Slugs of Wikipedia articles marked off-topic by topic_filter.py (products, people, orgs...)."""
    path = S("wiki_cs_articles.json")
    if not os.path.exists(path):
        return set()
    import re
    return {re.sub(r"[^A-Za-z0-9_]", "", r["title"].replace(" ", "_"))
            for r in json.load(open(path)) if r.get("topic_ok") is False}


def pools():
    bad = off_topic()
    a = {}
    for p in sorted(glob.glob(S("reconstructed", "*.json"))):
        n = stem(p)
        if n.startswith("wiki_") and n[5:] in bad:
            continue
        if not validate(p):
            a[n] = p
    b = {stem(p): p for p in sorted(glob.glob(S("wiki_history", "*.json")))}
    for p in sorted(glob.glob(S("wiki_history_full", "*.json.gz"))):
        if stem(p) not in bad:
            b.setdefault(stem(p), p)  # trial copy wins when both exist
    c = {stem(p): p for p in sorted(glob.glob(S("github_history_full", "*.json.gz")))}
    for p in sorted(glob.glob(S("github_history", "*.json"))):
        c.setdefault(stem(p), p)
    return a, b, c


def allocate(a, b, c):
    """Split pools so no document is in two files. D is ~70% reconstructed / 30% real history:
    25% of the new A-type rows, plus 3 real-history rows per 7 — taken from B first (25% of the new
    B pool at most) and topped up from C when Wikipedia's rate limit keeps B small."""
    trial_a, trial_da = set(bd.A_ROWS), set(bd.D_A_ROWS)
    trial_b, trial_db = set(bd.B_ALL[:10]), set(bd.B_ALL[10:13])
    trial_c = set(bd.C_ROWS)
    order = lambda names: sorted(names, key=lambda n: h("alloc:" + n))
    new_a = order(n for n in a if n not in trial_a | trial_da)
    new_b = order(n for n in b if n not in trial_b | trial_db)
    new_c = order(n for n in c if n not in trial_c)
    n_da = round(0.25 * len(new_a))
    n_real = round(n_da * 3 / 7)
    n_db = min(round(0.25 * len(new_b)), n_real)
    n_dc = max(0, n_real - n_db - len(trial_db))
    d_a, d_b, d_c = trial_da | set(new_a[:n_da]), trial_db | set(new_b[:n_db]), set(new_c[:n_dc])
    return ({n for n in a if n not in d_a}, {n for n in b if n not in d_b}, {n for n in c if n not in d_c},
            d_a, d_b, d_c)


def build_one(job):
    """(kind, name, path) -> {variant: row or None, ...}; runs in a worker process."""
    kind, name, path = job
    out = {}
    for v in VARIANTS:
        try:
            if kind == "A":
                row = bd.a_row(name, v)
            elif kind == "B":
                row = bd.b_row(name, v, path)
            else:
                row = bd.c_row(name, v, path)
        except Exception as e:  # malformed source: report, don't kill the build
            out[v] = f"error: {e}"
            continue
        want = 5 if v == "5stage" else 9
        s = row["steps"]
        if len(s) != want or s[-1]["word_count"] < 100 or s[1]["similarity_to_final"] >= 0.999:
            out[v] = None  # history too short for this variant, or no real change
            continue
        row["domain"], row["num_steps"] = "computer_science", want
        row["split"] = split_of(row["id"])
        out[v] = row
    return kind, name, out


def write_config(config, rows):
    d = os.path.join(ROOT, "data", "full", config)
    os.makedirs(d, exist_ok=True)
    counts = {}
    for split, _ in SPLITS:
        part = [r for r in rows if r["split"] == split]
        counts[split] = len(part)
        if part:
            pq.write_table(pa.Table.from_pylist(part), os.path.join(d, f"{split}.parquet"), compression="zstd")
    return counts


def main():
    a, b, c = pools()
    a_main, b_main, c_main, d_a, d_b, d_c = allocate(a, b, c)
    jobs = [("A", n, a[n]) for n in sorted(a)] + [("B", n, b[n]) for n in sorted(b)] + [("C", n, c[n]) for n in sorted(c)]
    print(f"pools: A-type {len(a)} (A {len(a_main)}, D {len(d_a)}), B-type {len(b)} (B {len(b_main)}, D {len(d_b)}), "
          f"C {len(c)} (C {len(c_main)}, D {len(d_c)})", flush=True)
    built, errors, dropped = {}, [], {v: 0 for v in VARIANTS}
    with Pool(os.cpu_count()) as pool:
        for i, (kind, name, out) in enumerate(pool.imap_unordered(build_one, jobs, chunksize=4), 1):
            for v, r in out.items():
                if isinstance(r, str):
                    errors.append(f"{kind}/{name}/{v}: {r}")
                elif r is None:
                    dropped[v] += 1
                else:
                    built[(kind, name, v)] = r
            if i % 200 == 0:
                print(f"  built {i}/{len(jobs)}", flush=True)
    groups = {"A_reconstructed": [("A", n) for n in sorted(a_main)],
              "B_wiki_history": [("B", n) for n in sorted(b_main)],
              "C_github_commits": [("C", n) for n in sorted(c_main)],
              "D_mix": [("A", n) for n in sorted(d_a)] + [("B", n) for n in sorted(d_b)] + [("C", n) for n in sorted(d_c)]}
    stats = {}
    for g, members in groups.items():
        for v in VARIANTS:
            config = f"{g}_{v}"
            rows = [built[(k, n, v)] for k, n in members if (k, n, v) in built]
            counts = write_config(config, rows)
            words = [r["steps"][-1]["word_count"] for r in rows]
            stats[config] = {"rows": len(rows), **counts, "mean_final_words": round(sum(words) / max(1, len(words)))}
            samples = sorted((r for r in rows if r["split"] == "test"), key=lambda r: h(r["id"]))[:10]
            bd.review(f"full/{config}", samples)
            print(f"{config}: {stats[config]}", flush=True)
    stats["_dropped_short_history"] = dropped
    stats["_errors"] = errors[:50]
    with open(os.path.join(ROOT, "data", "full", "stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    if errors:
        print(f"{len(errors)} errors (first: {errors[0]})")


if __name__ == "__main__":
    main()
