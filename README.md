# AI Overview Industry Study

**Which sources Google's AI Overview cites on 30 buyer searches across six industries, collected by hand on 11 to 12 June 2026**

| | |
|---|---|
| **Article** | https://ismybrandinai.com/ai-overview-citations-by-industry |
| **Repository** | https://github.com/minelgunesoglu-code/ai-overview-industry-study |
| **Archive** | DOI: to be added after the Zenodo release |
| **Collected** | 11 to 12 June 2026, by hand, one run per query |
| **Engine** | Google AI Overview, the source panel it labels "N sites" |
| **Sample** | 30 "best [category]" buyer searches, five in each of six industries; 27 produced an AI Overview, 3 did not |
| **Headline** | Review and authority media appeared in **24 of the 27** AI Overviews; Reddit in **11 of 27** (41%), and in none of the five consumer electronics searches. |
| **Licence** | CC BY 4.0 (`LICENSE`); see `LICENCE-NOTES.md` for what it does and does not cover |

A follow-up to the [AI Overview Cited-Domains Study](https://ismybrandinai.com/most-cited-sources-in-ai-overviews).
Searches were run in Google with US English settings (`gl=us`, `hl=en`). Thirty
buyer searches were split evenly across six industries: software, consumer
electronics, home and appliances, finance and insurance, health and personal care,
and auto and travel. Where an AI Overview appeared, every source in its panel was
recorded by title or brand and given a site type.

**What is measured:** whether a search produced an AI Overview, how many sources
its panel listed, whether Reddit was among them, and which site types were
present.
**What is NOT measured:** how prominently a source was placed, whether a cited page
is accurate, and how one industry compares with another in search volume.

---

## 1. Findings

All figures below are the ones published in the article. Each is recounted from
the rows by `notes/verify.py`; see `notes/reproduction-check.md`.

| | |
|---|---|
| Searches | 30, five per industry |
| With an AI Overview | 27 (no AI Overview: best mattresses, best air purifier, best seo tools) |
| Sources per AI Overview | about 6 (mean 6.33, median 6, range 2 to 10) |
| Review or authority media present | 24 of 27 |
| Vendor or retailer present | 20 of 27 |
| Reddit present | 11 of 27 (41%) |
| Reddit in consumer electronics | 0 of 5 |

Reddit appeared on the searches for airlines, SUVs, electric cars, robot vacuums,
refrigerators, car and renters insurance, savings accounts, project management,
CRM and multivitamins. It was absent from credit cards, CD rates, coffee makers,
running shoes, travel destinations and "best cars". On "best airlines for long
flights" the top three sources were all Reddit threads.

**Overlap with the first study.** Six searches ran in both studies with the same
wording and produced an AI Overview both times, on 10 June and again on 11 to 12
June. Reddit was in the panel both times for two of them (project management
software, high-yield savings accounts), in neither for one (electric
toothbrushes), and in one snapshot only for three (VPNs, protein powder, robot
vacuums). `notes/verify.py` checks this when given the first study's CSV.

---

## 2. What is in this repository

```
data/ai-overview-citations-by-industry-2026-06.csv   30 rows, one per query
data/ai-overview-citations-by-industry-2026-06.json  the same rows plus the method, the type key and the known limits
notes/
  verify.py                 recounts the published figures from the rows
  reproduction-check.md     the result of that recount
  zenodo-release-steps.md   how this repository is archived on Zenodo
```

This is a data package with method notes. The two data files are byte-identical
to the ones published on the site.

### Columns

| Column | Meaning |
|---|---|
| `vertical` | the industry the search was assigned to |
| `query` | the search, as typed |
| `ai_overview_present` | `yes` if an AI Overview appeared on the run |
| `sources_in_panel` | the source count the panel showed (0 when there was no AI Overview) |
| `reddit_in_panel` | `yes` or `no`; empty when there was no AI Overview |
| `source_types_present` | the site types present, separated by `\|` |
| `raw_note` | the note written during collection: the sources by name, each with its type |

Site types: `R` Reddit, `F` other forum, `RM` review or authority media, `V` vendor
or retailer, `L` independent listicle or niche blog, `YT` YouTube, `N` news, `WK`
reference.

### Rules worth knowing before recounting

- Site type was assigned by hand from each source's title and brand, not by
  reading the page. That classification is a judgement, and the rows are
  published so any single one of them can be disputed.
- A domain counts once per AI Overview, however prominently it was placed.
  Grouped citations count by their lead domain.
- `source_types_present` holds only the codes written in brackets in the note.
  On "best cameras" the note describes all six sources as niche enthusiast blogs
  without bracketed codes, so the field is empty for that row.

---

## 3. Recounting the figures

```bash
python3 notes/verify.py
# with the comparison against the first study:
python3 notes/verify.py path/to/ai-overview-cited-domains-2026-06-10.csv
```

Python 3.8 or later, standard library only. Run it from the repository root.

---

## 4. Limits

- One engine, US English settings and one two-day snapshot, one run
  per query, from one signed-in Chrome profile. AI Overviews are personalised and
  change between runs.
- 30 searches, five per industry: enough to show per-industry patterns, not to
  rank the web. Industries differ in search volume, so comparisons are about the
  pattern within each, not their size.

---

## 5. Citing this

> Gunesoglu, M. (2026). *AI Overview Industry Study* [Data set].
> Is My Brand in AI. https://ismybrandinai.com/ai-overview-citations-by-industry

If a count here does not match what you get from the files, open an issue and a
correction will be published saying what changed.
