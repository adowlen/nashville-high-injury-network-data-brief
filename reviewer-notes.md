# Reviewer notes - Nashville Vision Zero High Injury Network, 2026-11-14

## Thesis (recorded before the fusion analysis and final prose)
Thesis: Nashville's High Injury Network layer records its KSI crashes concentrated in a small top tier - the 16 High-tier segments are a small share of the network's miles but hold a disproportionate share of its recorded KSI crashes, at several times the per-mile figure of the rest of the network - while the layer states no study window, so its accounting can be ranked but not dated.

## Claims most likely to be challenged
- The headline (372 of 1,955 KSI crashes on 16 High-tier segments, 19.0% on 6.1% of miles). Both inputs are the layer's own recorded fields; the tier was built from crash history, so concentration is partly the selection method - stated in the brief's interpretation section.
- "KSI crashes": the brief uses the layer's alias ("Sum of KSI crashes on this segment") - crashes, not people. The Vision Zero Action Plan's 468 deaths / 2,899 severe injuries are people on a since-2014 window and are deliberately never compared.
- The street-name match (109,443 name-matched crashes, 52.5% of injury-or-fatal crashes with an address): printed only as a labeled upper bound, never as on-network crashes; the 3.7x gap against the layer's own 29,530 is printed with it.
- Per-mile rankings: printed only for tiers and for streets aggregated over >=1 network mile; individual short-segment per-mile values are explicitly not ranked (0.07-mile segment at 61.2/mi is the documented reason).

## Methods checks that could not be completed
- Study window: the layer carries no date field and states no window for frequency / sum_ksi_cr. Cannot be completed from the layer; stated prominently in the brief, and no trend or current-rate claim is printed.
- Segment-level join to the crash layer: impossible from published attributes (no segment ranges/geometry key in the attribute table as pulled; crash layer has addresses only). Replaced with the labeled street-name upper bound; the limitation is a finding of the brief.
- Exposure: no traffic-volume field exists in the layer, so no exposure rate is printed; per-mile figures use length and are labeled.

## Findings that surprised us
- All 297 segments carry hin_59_per = 1, including all 188 Low-tier segments: the published view is the network itself, tiers and all, not a top slice.
- The Low tier, not the High tier, holds the largest share of recorded KSI crashes (852 of 1,955) - a length effect the brief prints alongside the per-mile figures.
- Two Gallatin Pike High-tier segments of identical recorded length (0.90 mi) hold 45 and 44 KSI crashes, the two highest segment counts in the layer.
