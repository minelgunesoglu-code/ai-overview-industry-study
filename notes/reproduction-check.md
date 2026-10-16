# Reproduction check

Checked on 17 October 2026 against the article as published at
https://ismybrandinai.com/ai-overview-citations-by-industry (published 12 June
2026, last updated 10 October 2026).

## Result

**Every figure checked matches.** `notes/verify.py` runs 39 checks, the published
figures and statements plus consistency checks on the files, and all 39 pass. No
figure was changed, and no data was changed.

## What was checked

1. **The files are the published files.** The two files in `data/` are
   byte-identical to the ones the article links to. SHA-256:

    8cf3659176155ac4cdd1ce825259e466566b8c582f4a1d0abdee5f175f34e743  data/ai-overview-citations-by-industry-2026-06.csv
    4ce97a8515603a0054952ff70171a35c2be71438a89cf178d096bcc2255c7def  data/ai-overview-citations-by-industry-2026-06.json

2. **The CSV and the JSON agree.** The JSON's `rows` equal the CSV rows.

3. **Every figure in the article recounts from the rows.** Output of
   `python3 notes/verify.py ../ai-overview-cited-domains-study/data/ai-overview-cited-domains-2026-06-10.csv`:

```
[OK ] CSV rows equal JSON rows: published True, computed True
[OK ] searches: published 30, computed 30
[OK ] searches with an AI Overview: published 27, computed 27
[OK ] searches without one: published 3, computed 3
[OK ] no-AI-Overview queries: published ['best air purifier', 'best mattresses', 'best seo tools'], computed ['best air purifier', 'best mattresses', 'best seo tools']
[OK ] six industries, five searches each: published [5, 5, 5, 5, 5, 5], computed [5, 5, 5, 5, 5, 5]
[OK ] sources per AI Overview, mean rounded ('about 6'): published 6, computed 6
[OK ] sources per AI Overview, range: published (2, 10), computed (2, 10)
       (exact mean: 6.33, median 6)
[OK ] AI Overviews with review/authority media (RM): published 24, computed 24
[OK ] AI Overviews citing Reddit: published 11, computed 11
[OK ] Reddit share, % ('about 41%'): published 41, computed 41
[OK ] reddit_in_panel agrees with type code R: published True, computed True
[OK ] AI Overviews with a vendor or retailer (V): published 20, computed 20
[OK ] Reddit in consumer electronics: published (0, 5), computed (0, 5)
[OK ] Reddit present: best airlines for long flights: published 'yes', computed 'yes'
[OK ] Reddit present: best suvs: published 'yes', computed 'yes'
[OK ] Reddit present: best electric cars: published 'yes', computed 'yes'
[OK ] Reddit present: best robot vacuum: published 'yes', computed 'yes'
[OK ] Reddit present: best refrigerator: published 'yes', computed 'yes'
[OK ] Reddit present: best car insurance: published 'yes', computed 'yes'
[OK ] Reddit present: best renters insurance: published 'yes', computed 'yes'
[OK ] Reddit present: best high yield savings account: published 'yes', computed 'yes'
[OK ] Reddit present: best project management software: published 'yes', computed 'yes'
[OK ] Reddit present: best crm for small business: published 'yes', computed 'yes'
[OK ] Reddit present: best multivitamin: published 'yes', computed 'yes'
[OK ] Reddit absent: best credit cards: published 'no', computed 'no'
[OK ] Reddit absent: best cd rates: published 'no', computed 'no'
[OK ] Reddit absent: best coffee makers: published 'no', computed 'no'
[OK ] Reddit absent: best running shoes: published 'no', computed 'no'
[OK ] Reddit absent: best travel destinations 2025: published 'no', computed 'no'
[OK ] Reddit absent: best cars: published 'no', computed 'no'
[OK ] Reddit in health and personal care ('multivitamin only'): published ['best multivitamin'], computed ['best multivitamin']
[OK ] airlines: top three sources are Reddit (from the row note): published True, computed True
[OK ] searches in both studies, same wording, AI Overview both times: published 6, computed 6
       best electric toothbrush: Reddit 10 June no, 11-12 June no
       best high yield savings account: Reddit 10 June yes, 11-12 June yes
       best project management software: Reddit 10 June yes, 11-12 June yes
       best protein powder: Reddit 10 June yes, 11-12 June no
       best robot vacuum: Reddit 10 June no, 11-12 June yes
       best vpn: Reddit 10 June yes, 11-12 June no
[OK ] Reddit both times: published ['best high yield savings account', 'best project management software'], computed ['best high yield savings account', 'best project management software']
[OK ] Reddit neither time: published ['best electric toothbrush'], computed ['best electric toothbrush']
[OK ] Reddit in one snapshot only: published ['best protein powder', 'best robot vacuum', 'best vpn'], computed ['best protein powder', 'best robot vacuum', 'best vpn']
[OK ] 'best coffee maker' (10 June): Reddit first in the panel: published True, computed True
[OK ] 'best coffee makers' (11-12 June): no Reddit: published 'no', computed 'no'

39 of 39 checks match.
```

## Notes on the counts

- "About 6 sources on average" is a mean of 6.33 rounded; the median is 6.
- The review-media count of 24 and the vendor count of 20 are read from
  `source_types_present`. The "best cameras" row has no codes in that field (its
  note describes all six sources as niche blogs without bracketed codes), so it
  counts in neither, which agrees with the article: cameras were cited from small
  enthusiast blogs, not big media.
- Reddit's 11 agrees with both `reddit_in_panel` and the type code `R`.
