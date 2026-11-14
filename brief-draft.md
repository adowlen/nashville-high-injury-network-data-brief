# Nashville's High Injury Network: 372 of its 1,955 recorded KSI crashes sit on 16 High-tier segments that make up 6.1 percent of its miles

**One-line summary:** Of the 297 segments in Nashville's Vision Zero High Injury Network layer pulled on November 14, 2026, the layer records 29,530 crashes and 1,955 KSI crashes (killed-or-seriously-injured crashes, as recorded in the layer's own sum_ksi_cr field) across 226.3 miles; the 16 segments in the layer's High priority tier hold 372 of those KSI crashes (19.0 percent, derived) on 13.8 miles (6.1 percent of network miles, derived).

Start with the scale. Machine Readable pulled the full layer from Metro's ArcGIS service on November 14, 2026; the pulled row count matches the server's own count exactly (297). One row is one road segment. Every segment carries the layer's "Road is on the HIN" flag at 1. The layer records a crash count (frequency, alias "Number of Crashes on this segment") and a KSI crash count (sum_ksi_cr, alias "Sum of KSI crashes on this segment") for each segment. The layer carries no date field and states no study window for those counts, so this brief reports them as the network's recorded accounting as published, not as a count for any named period, and prints no trend. No exposure denominator exists in the layer - there is no traffic-volume field - so per-mile figures in this brief use segment length as the denominator and are labeled as such; they are not exposure rates.

## The network as recorded

- Segments: 297, on 175 named streets.
- Length: 226.3 miles in total (length_mi, alias "Length (mi)"). The layer also carries a normalized length field (length_mil) totaling 229.0 miles; no figure in this brief uses it as a denominator.
- Recorded crashes: 29,530 across the 297 segments.
- Recorded KSI crashes: 1,955, which is 6.6 percent of the network's recorded crashes (derived).
- Recorded KSI crashes per mile: 8.6 across the network as a whole (1,955 / 226.3 miles, derived).

Human scale (derived): about 9 recorded KSI crashes per network mile.

## Priority tiers

The layer's Category field (alias "Priority Tiers") divides the network into three tiers. All figures below are the layer's own recorded counts.

- High: 16 segments, 13.8 miles (6.1 percent of network miles, derived). 4,373 recorded crashes; 372 recorded KSI crashes (19.0 percent of the network's 1,955, derived); 27.0 recorded KSI crashes per mile (372 / 13.8, derived); KSI crashes are 8.5 percent of the tier's recorded crashes (372 of 4,373).
- Medium: 93 segments, 70.6 miles (31.2 percent). 12,090 recorded crashes; 731 recorded KSI crashes (37.4 percent of 1,955, derived); 10.4 KSI crashes per mile (derived); KSI crashes are 6.1 percent of the tier's recorded crashes (731 of 12,090).
- Low: 188 segments, 141.9 miles (62.7 percent). 13,067 recorded crashes; 852 recorded KSI crashes (43.6 percent of 1,955, derived); 6.0 KSI crashes per mile (derived); KSI crashes are 6.5 percent of the tier's recorded crashes (852 of 13,067).

The tier with the fewest miles holds the highest KSI-per-mile figure. The Low tier holds the largest single share of recorded KSI crashes (852 of 1,955) because it holds most of the network's miles.

Human scale (derived): about 1 in 5 of the network's recorded KSI crashes sits on the 16 High-tier segments.

## Concentration within the network

- The 10 segments with the highest recorded KSI counts hold 317 KSI crashes (16.2 percent of 1,955, derived).
- The 30 highest segments hold 661 (33.8 percent, derived) on 13.2 percent of network miles (derived).
- 47 of the 297 segments record a KSI count of 0. A recorded 0 is a count in the layer, not a missing value: no field in the pulled layer is blank on any record.

## Streets

Aggregating each street's segments in the network (segment counts and lengths summed; the figures describe the street's network segments, not the whole street):

- Gallatin Pike: 10 segments, 8.2 miles, 1,838 recorded crashes, 173 recorded KSI crashes - the highest street total. 21.1 KSI crashes per mile over its network segments (derived).
- Murfreesboro Pike: 11 segments, 10.5 miles, 2,600 recorded crashes (the highest street crash total), 165 recorded KSI crashes; 15.6 per mile (derived).
- Old Hickory Blvd: 15 segments (the most of any street), 13.1 miles, 2,079 recorded crashes, 156 recorded KSI crashes; 11.9 per mile (derived).
- Nolensville Pike: 8 segments, 7.8 miles, 1,882 recorded crashes, 110 recorded KSI crashes; 14.2 per mile (derived).
- Bell Rd: 9 segments, 8.8 miles, 1,353 recorded crashes, 95 recorded KSI crashes; 10.8 per mile (derived).

By KSI crashes per mile, among streets with at least 1 mile of network segments: Lafayette St records 26.1 per mile (37 KSI crashes on 1.4 miles, 1 segment), then Gallatin Pike at 21.1, Donelson Pike at 18.1 (39 on 2.2 miles), Robinson Rd at 17.4 (28 on 1.6 miles), and W Trinity Ln at 16.2 (49 on 3.0 miles). Per-mile figures for individual short segments are not ranked in this brief: a segment of 0.07 miles with 4 recorded KSI crashes produces a per-mile figure of 61.2 that reflects the segment's length, not a comparable rate, so segment-level per-mile values are printed only for the aggregated streets above and the tier totals.

The two highest individual segments are both on Gallatin Pike and both in the High tier: 45 recorded KSI crashes on a 0.90-mile segment (328 recorded crashes) and 44 on a second 0.90-mile segment (302 recorded crashes).

## What the published crash layer can and cannot add

This brief's companion dataset is the crash layer published in the Nashville Traffic Accidents brief (2026-11-02): 222,902 reported crashes with counts populated, January 1, 2019 to October 31, 2026. The two layers cannot be joined at segment level from the published fields: the crash layer carries a street address for each crash, and the HIN layer carries segment names but no segment street ranges or geometry in the attribute table as pulled, so a crash cannot be assigned to a specific HIN segment from the published attributes.

What can be computed is a street-name match, and this brief prints it only as a labeled upper bound, never as on-network crashes: a crash name-matches when either side of its street address, after house-number stripping and abbreviation expansion, equals one of the network's 175 street names. On that basis, 109,443 of the 222,279 crashes with an address (49.2 percent) name-match a network street, including 35,884 of the 68,289 injury-or-fatal crashes with an address (52.5 percent, derived). The name-matched total (109,443) is 3.7 times the network's own recorded crash total (29,530), which is the expected result of matching whole streets against specific segments of those streets. The crash layer also carries no injury-severity split, so its injury-or-fatal measure is not the HIN layer's KSI measure and the two are never compared as the same measure.

## What this might mean

One reading of the tier figures is that the network's own prioritization and its recorded KSI density point at the same small set of segments: the High tier is 6.1 percent of network miles at 27.0 recorded KSI crashes per mile, against 6.0 per mile across the Low tier's 141.9 miles. An alternative explanation sits alongside it: the tiers were constructed from crash history (the layer's Alta weighted index field records the prioritization scoring), so a tier built from recorded crashes recording more crashes per mile is partly the selection method describing itself, and the figures here cannot separate how much of the gap is selection from how much is current conditions - the layer states no study window, so no figure in this brief describes a current rate. What the layer does support, without either reading, is the accounting itself: where its recorded KSI crashes sit, street by street and tier by tier, in the published record.

## Who can act

- **NDOT (Nashville Department of Transportation and Multimodal Infrastructure)** controls the Vision Zero program and the High Injury Network project list, including the HIN Local Intersection Improvements program. The concrete action the data points to is sequencing: the 16 High-tier segments and the named streets above are the layer's own recorded KSI concentrations. Cost class: budget decision for corridor and intersection capital work; the prioritization read itself is a low-cost operational step. Outcome measure: a refreshed HIN layer whose recorded KSI counts and tier assignments are re-published with a stated study window, and, over time, the crash layer published 2026-11-02 re-pulled on the same streets.
- **Metro Council** controls transportation capital appropriations and meets Tuesday, November 17, 2026. The concrete action is appropriation sequencing against the tier list the layer publishes. Cost class: budget decision. Outcome measure: funded project lists that name HIN segments, checkable against this layer's segment names.
- **Metro's open-data publishers** control the layer itself. The concrete action is adding the study window and a segment identifier that a crash record can be joined to (a street range or a published geometry key), so the network's accounting can be checked against the crash layer at segment level. Cost class: low-cost operational change. Outcome measure: a future pull of this same layer carrying a date field or window statement and joinable segment keys.

## Methods

Pull: full layer, paginated, ordered by OBJECTID, November 14, 2026; pulled rows (297) equal the server count. Fields relied on: full_name, Category, length_mi, length_mil, frequency, sum_ksi_cr, hin_59_per, Alta_weighted_index. KSI in this brief always means the layer's sum_ksi_cr field ("Sum of KSI crashes on this segment") - crashes, not people; the Vision Zero Action Plan's published people counts (deaths and severe injuries as people) are a different measure on a different window and are not used or compared here. No record is excluded from any denominator: no field in the pull is blank, and a recorded sum_ksi_cr of 0 (47 segments) is treated as a count. Per-mile figures use length_mi. The crash-layer fusion is a street-name match only, with its match population and limits printed in its own section above. Direction of causality: none is claimed; tier membership and recorded counts are both products of the same recorded history, and the brief says so where the figures are interpreted.
