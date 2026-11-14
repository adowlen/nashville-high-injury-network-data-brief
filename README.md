# Nashville Vision Zero High Injury Network - Machine Readable brief, 2026-11-14

Of the 297 segments in Nashville's Vision Zero High Injury Network layer, the layer records 29,530 crashes and 1,955 KSI crashes across 226.3 miles; the 16 High-tier segments hold 372 of those KSI crashes (19.0 percent, derived) on 13.8 miles (6.1 percent of network miles, derived). The layer states no study window for its counts.

Full brief: brief-draft.md. Headline graphic: hero.png.

## Contents
- brief-draft.md - the brief
- stats.json - every headline figure with its population printed
- charts/ - KSI per mile by tier, tier miles vs KSI share, top streets by KSI, top streets by KSI per mile
- data/ - panels, the raw snapshot CSV, the pre-flight audit output, the pull log, the source layer metadata, and the independent verifier output
- code/ - pull_data.py, audit_section10.py, build_stats.py, verify_independent.py, charts.py, hero_composite.py
- verification.md - pre-flight audit, methods checklist, join hygiene, sync gate, story gate
- sources.md, reviewer-notes.md, social-drafts.md

## Reproduce
```
python3 code/pull_data.py
python3 code/audit_section10.py
python3 code/build_stats.py
python3 code/verify_independent.py
python3 code/charts.py
python3 code/hero_composite.py
```
Dependencies (matching the code's actual imports): Python 3 standard library for pull, audit, and verifier; pandas, numpy, and pyarrow for build_stats.py only (it reads the 2026-11-02 warehouse crash layer for the fusion section - that layer is not in this repo; every network figure reproduces from data/nashville_hin_raw.csv alone); matplotlib and numpy for charts only; Pillow for the hero composite only.

## Source
Vision Zero High Injury Network (Vision_Zero_High_Injury_Network_view), Metropolitan Government of Nashville and Davidson County, ArcGIS FeatureServer layer 0 (services2.arcgis.com/HdTo6HJqh92wn4D8). Snapshot November 14, 2026; service data last edit 2025-01-03; the layer states no study window for its crash counts.

## License
Brief text and derived data products: CC BY 4.0 (see LICENSE). Underlying records are Metro Nashville government open data.

Part of Machine Readable: https://adowlen.github.io/machine-readable/
