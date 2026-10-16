"""Recount the figures published in the AI Overview Industry Study.

This script was written after publication, to check the article's figures
against the published rows. The data were collected by hand. Standard library only. Run from the repository root:

    python3 notes/verify.py

The six-search comparison with the AI Overview Cited-Domains Study needs that
study's CSV. Pass its path as the first argument to include it, for example:

    python3 notes/verify.py ../ai-overview-cited-domains-study/data/ai-overview-cited-domains-2026-06-10.csv
"""
import csv
import json
import statistics
import sys
from pathlib import Path

DATA = Path("data")
CSV_FILE = DATA / "ai-overview-citations-by-industry-2026-06.csv"
JSON_FILE = DATA / "ai-overview-citations-by-industry-2026-06.json"

checks = []


def check(label, published, computed):
    ok = published == computed
    checks.append(ok)
    print(f"[{'OK ' if ok else 'DIFF'}] {label}: published {published!r}, computed {computed!r}")


with CSV_FILE.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
meta = json.loads(JSON_FILE.read_text(encoding="utf-8"))

json_rows = [{k: ("" if v is None else str(v)) for k, v in r.items()} for r in meta["rows"]]
check("CSV rows equal JSON rows", True, json_rows == rows)

aio = [r for r in rows if r["ai_overview_present"] == "yes"]
check("searches", 30, len(rows))
check("searches with an AI Overview", 27, len(aio))
check("searches without one", 3, len(rows) - len(aio))
check("no-AI-Overview queries", ["best air purifier", "best mattresses", "best seo tools"],
      sorted(r["query"] for r in rows if r["ai_overview_present"] != "yes"))

per_vertical = {}
for r in rows:
    per_vertical[r["vertical"]] = per_vertical.get(r["vertical"], 0) + 1
check("six industries, five searches each", [5] * 6, sorted(per_vertical.values()))

counts = [int(r["sources_in_panel"]) for r in aio]
check("sources per AI Overview, mean rounded ('about 6')", 6, round(statistics.mean(counts)))
check("sources per AI Overview, range", (2, 10), (min(counts), max(counts)))
print(f"       (exact mean: {statistics.mean(counts):.2f}, median {statistics.median(counts)})")


def types(r):
    return set(filter(None, r["source_types_present"].split("|")))


check("AI Overviews with review/authority media (RM)", 24, sum("RM" in types(r) for r in aio))
reddit = [r for r in aio if r["reddit_in_panel"] == "yes"]
check("AI Overviews citing Reddit", 11, len(reddit))
check("Reddit share, % ('about 41%')", 41, round(100 * len(reddit) / len(aio)))
check("reddit_in_panel agrees with type code R", True,
      all((r["reddit_in_panel"] == "yes") == ("R" in types(r)) for r in aio))
check("AI Overviews with a vendor or retailer (V)", 20, sum("V" in types(r) for r in aio))

elec = [r for r in rows if r["vertical"] == "Consumer electronics"]
check("Reddit in consumer electronics", (0, 5), (sum(r["reddit_in_panel"] == "yes" for r in elec), len(elec)))

by_q = {r["query"]: r for r in rows}
for q in ["best airlines for long flights", "best suvs", "best electric cars", "best robot vacuum",
          "best refrigerator", "best car insurance", "best renters insurance",
          "best high yield savings account", "best project management software",
          "best crm for small business", "best multivitamin"]:
    check(f"Reddit present: {q}", "yes", by_q[q]["reddit_in_panel"])
for q in ["best credit cards", "best cd rates", "best coffee makers", "best running shoes",
          "best travel destinations 2025", "best cars"]:
    check(f"Reddit absent: {q}", "no", by_q[q]["reddit_in_panel"])
health_reddit = [r["query"] for r in rows if r["vertical"].startswith("Health") and r["reddit_in_panel"] == "yes"]
check("Reddit in health and personal care ('multivitamin only')", ["best multivitamin"], health_reddit)
check("airlines: top three sources are Reddit (from the row note)", True,
      "Reddit ×3" in by_q["best airlines for long flights"]["raw_note"]
      and "top 3" in by_q["best airlines for long flights"]["raw_note"])

# Comparison with the AI Overview Cited-Domains Study (10 June 2026).
if len(sys.argv) > 1:
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        first = {r["query"]: r for r in csv.DictReader(f)}
    both = sorted(q for q in by_q if q in first
                  and by_q[q]["ai_overview_present"] == "yes" and first[q]["ai_overview_present"] == "yes")
    check("searches in both studies, same wording, AI Overview both times", 6, len(both))
    pairs = {q: (first[q]["reddit_in_panel"], by_q[q]["reddit_in_panel"]) for q in both}
    for q, p in pairs.items():
        print(f"       {q}: Reddit 10 June {p[0]}, 11-12 June {p[1]}")
    check("Reddit both times", ["best high yield savings account", "best project management software"],
          [q for q, p in pairs.items() if p == ("yes", "yes")])
    check("Reddit neither time", ["best electric toothbrush"], [q for q, p in pairs.items() if p == ("no", "no")])
    check("Reddit in one snapshot only", ["best protein powder", "best robot vacuum", "best vpn"],
          [q for q, p in pairs.items() if p[0] != p[1]])
    check("'best coffee maker' (10 June): Reddit first in the panel", True,
          first["best coffee maker"]["cited_domains"].startswith("reddit.com"))
    check("'best coffee makers' (11-12 June): no Reddit", "no", by_q["best coffee makers"]["reddit_in_panel"])
else:
    print("       (comparison with the Cited-Domains Study skipped: no path given)")

print()
print(f"{sum(checks)} of {len(checks)} checks match.")
