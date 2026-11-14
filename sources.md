# Source audit: Nashville Vision Zero High Injury Network brief (2026-11-14)

Every figure in brief-draft.md, traced to its derivation. Counts were produced by code/build_stats.py and are stored in stats.json; the independent recomputation is in data/verify_independent_output.json (17 of 17 checks passed); the pre-flight audit is in data/audit_output.txt and in verification.md.

## The datasets

1. High Injury Network (primary dataset for all network figures)
- Name: Vision Zero High Injury Network (Vision_Zero_High_Injury_Network_view, layer 0), Metro Nashville open data, owner NashvilleOpenData
- Endpoint used: https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Vision_Zero_High_Injury_Network_view/FeatureServer/0
- Pull: 2026-11-14, paginated query ordered by OBJECTID, 297 records; server count confirmed with returnCountOnly before download and equal to the local count. Service data last edit 2025-01-03 (recorded when the lead was verified live 2026-11-13).
- Saved copy: data/nashville_hin_raw.csv; layer metadata as served: data/source-metadata-layer.json; pull log: data/pull_log.json.
- Fields relied on: full_name ("Segment Name"), Category ("Priority Tiers"), length_mi ("Length (mi)"), length_mil ("Normalized Length (mi)"), frequency ("Number of Crashes on this segment"), sum_ksi_cr ("Sum of KSI crashes on this segment"), hin_59_per ("Road is on the HIN"), Alta_weighted_index ("Tiers").
- The layer carries no date field and states no study window for frequency or sum_ksi_cr. No figure in the brief assigns the counts to a period.

2. Crash layer (fusion section only)
- Nashville Traffic Accidents (Traffic_Accidents_2, layer 0), as published in the Nashville Traffic Accidents brief (2026-11-02, adowlen/nashville-traffic-accidents-data-brief): 222,903 reported crashes, January 1, 2019 to October 31, 2026; the fusion uses the 222,902 rows with counts populated from that package's cleaned warehouse layer (stack/nashville/layers/traffic_accidents_clean.parquet).
- Measure used: injury-or-fatal crashes (Number_of_Injuries > 0 or Number_of_Fatalities > 0). The crash layer carries no severity split, so this measure is never labeled KSI.
- Join: street-name match only (method and limits in verification.md and in the brief's fusion section). No segment-level or proximity join is claimed.

3. Program context (Who can act naming only; no figure derives from these)
- NDOT High Injury Network (HIN) Local Intersection Improvements, Nashville.gov project page, last updated October 26, 2026: https://www.nashville.gov/departments/transportation/projects/high-injury-network - NDOT's Vision Zero program framing and its five-intersection HIN improvements program.
- Nashville Vision Zero Action Plan 2022-2026 (draft, December 2021; Alta Planning + Design): the plan that constructed the High Injury Network. Its people counts (468 deaths, 2,899 severe injuries, since 2014) are a different measure on a different window from the layer's crash counts and are cited here only to record that they were NOT used or compared.
- Metro Council meeting Tuesday, November 17, 2026: the regular meeting date in the pick record for this brief (leads_log.md, CHOSEN BY ALEX 2026-11-13); the brief asserts no safety item on that meeting's agenda.

## Figure-by-figure audit

1. **297 segments, 175 named streets, all hin_59_per = 1** - Counter over full_name and hin_59_per in the audit output. stats.json: rows, distinct_streets, hin_flag_counter.
2. **226.3 miles (length_mi sum 226.27); normalized length_mil sum 228.98, never a denominator** - stats.json: total_length_mi, total_length_mil_normalized.
3. **29,530 recorded crashes; 1,955 recorded KSI crashes; 6.6 percent (derived: 1,955 / 29,530); 8.6 KSI per mile (derived: 1,955 / 226.27)** - stats.json: total_frequency_crashes, total_ksi_crashes, ksi_share_of_network_crashes_pct, ksi_per_mi_overall.
4. **Tiers: High 16 segments / 13.8 mi / 4,373 crashes / 372 KSI / 19.0 percent of 1,955 (derived) / 27.0 per mile (derived) / 8.5 percent of tier crashes; Medium 93 / 70.6 / 12,090 / 731 / 37.4 / 10.4 / 6.1; Low 188 / 141.9 / 13,067 / 852 / 43.6 / 6.0 / 6.5** - stats.json: by_category; panel: data/category_panel.csv.
5. **Concentration: top 10 segments 317 KSI (16.2 percent, derived); top 30 segments 661 (33.8 percent, derived) on 13.2 percent of miles (derived); 47 segments with a recorded KSI count of 0** - stats.json: concentration.
6. **Streets: Gallatin Pike 10 segments / 8.2 mi / 1,838 crashes / 173 KSI / 21.1 per mile (derived); Murfreesboro Pike 11 / 10.5 / 2,600 / 165 / 15.6; Old Hickory Blvd 15 / 13.1 / 2,079 / 156 / 11.9; Nolensville Pike 8 / 7.8 / 1,882 / 110 / 14.2; Bell Rd 9 / 8.8 / 1,353 / 95 / 10.8** - stats.json: top_streets_by_ksi; panel: data/street_panel.csv.
7. **Per-mile streets (>=1 network mile aggregated): Lafayette St 26.1 (37 on 1.4 mi, 1 segment); Gallatin Pike 21.1; Donelson Pike 18.1 (39 on 2.2); Robinson Rd 17.4 (28 on 1.6); W Trinity Ln 16.2 (49 on 3.0)** - stats.json: top_streets_by_ksi_per_mi_min1mi.
8. **Top segments: Gallatin Pike (High) 45 KSI on 0.901 mi, 328 crashes; Gallatin Pike (High) 44 on 0.901 mi, 302 crashes** - stats.json: top_segments_by_ksi; panel: data/segment_panel.csv.
9. **Fusion: 222,279 of 222,902 known-count crashes carry an address; 109,443 name-matched (49.2 percent); 35,884 of 68,289 injury-or-fatal crashes with an address name-matched (52.5 percent, derived); name-match total is 3.7x the layer's own 29,530 (derived)** - stats.json: fusion_crash_layer, including its method statement and measure note.
10. **Hero figure: 372 of 1,955 (19.0 percent)** - Item 4's High-tier figures, composited from stats.json by code/hero_composite.py; hero-headline.txt carries the same text.
