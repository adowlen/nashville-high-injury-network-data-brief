import pandas as pd, numpy as np, json, re, os
BASE=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-hin-brief-2026-11-14")
hin=pd.read_csv(f"{BASE}/data/nashville_hin_raw.csv")
hin['ksi_per_mi']=hin.sum_ksi_cr/hin.length_mi
hin['ksi_share_pct']=(hin.sum_ksi_cr/hin.frequency*100).round(2)
stats={}
stats['dataset']="Nashville Vision Zero High Injury Network (Vision_Zero_High_Injury_Network_view, layer 0)"
stats['snapshot_date']="2026-11-14"; stats['rows']=int(len(hin)); stats['server_count']=297
stats['unit']="one row = one road segment in the published High Injury Network view"
stats['distinct_streets']=int(hin.full_name.nunique())
stats['total_length_mi']=round(float(hin.length_mi.sum()),2)
stats['total_length_mil_normalized']=round(float(hin.length_mil.sum()),2)
stats['total_frequency_crashes']=int(hin.frequency.sum())
stats['total_ksi_crashes']=int(hin.sum_ksi_cr.sum())
stats['ksi_share_of_network_crashes_pct']=round(float(hin.sum_ksi_cr.sum()/hin.frequency.sum()*100),2)
stats['ksi_per_mi_overall']=round(float(hin.sum_ksi_cr.sum()/hin.length_mi.sum()),2)
stats['hin_flag_counter']=hin.hin_59_per.value_counts().to_dict()
stats['category_counter']=hin.Category.value_counts().to_dict()
cats={}
for cat,g in hin.groupby('Category'):
    cats[cat]={'segments':int(len(g)),'length_mi':round(float(g.length_mi.sum()),2),'length_share_pct':round(float(g.length_mi.sum()/hin.length_mi.sum()*100),2),'frequency':int(g.frequency.sum()),'ksi':int(g.sum_ksi_cr.sum()),'ksi_share_of_total_pct':round(float(g.sum_ksi_cr.sum()/hin.sum_ksi_cr.sum()*100),2),'ksi_per_mi':round(float(g.sum_ksi_cr.sum()/g.length_mi.sum()),2),'ksi_share_of_cat_crashes_pct':round(float(g.sum_ksi_cr.sum()/g.frequency.sum()*100),2)}
stats['by_category']=cats
agg=hin.groupby('full_name').agg(segments=('OBJECTID','count'),length_mi=('length_mi','sum'),frequency=('frequency','sum'),ksi=('sum_ksi_cr','sum')).reset_index()
agg['ksi_per_mi']=(agg.ksi/agg.length_mi).round(2); agg['ksi_share_pct']=(agg.ksi/agg.frequency*100).round(2)
agg_sorted=agg.sort_values('ksi',ascending=False)
stats['top_streets_by_ksi']=[{k:(float(v) if isinstance(v,float) else int(v) if isinstance(v,(int,np.integer)) else str(v)) for k,v in r.items()} for r in agg_sorted.head(10).to_dict('records')]
agg_len1=agg[agg.length_mi>=1.0].sort_values('ksi_per_mi',ascending=False)
stats['top_streets_by_ksi_per_mi_min1mi']=[{k:(float(v) if isinstance(v,float) else int(v) if isinstance(v,(int,np.integer)) else str(v)) for k,v in r.items()} for r in agg_len1.head(10).to_dict('records')]
seg_sorted=hin.sort_values('sum_ksi_cr',ascending=False)
stats['top_segments_by_ksi']=[{'full_name':str(r.full_name),'category':str(r.Category),'length_mi':round(float(r.length_mi),3),'frequency':int(r.frequency),'ksi':int(r.sum_ksi_cr),'ksi_per_mi':round(float(r.ksi_per_mi),2)} for r in seg_sorted.head(10).itertuples()]
stats['concentration']={'top10_segments_ksi':int(seg_sorted.head(10).sum_ksi_cr.sum()),'top10_segments_ksi_share_pct':round(float(seg_sorted.head(10).sum_ksi_cr.sum()/hin.sum_ksi_cr.sum()*100),2),'top30_segments_ksi':int(seg_sorted.head(30).sum_ksi_cr.sum()),'top30_segments_ksi_share_pct':round(float(seg_sorted.head(30).sum_ksi_cr.sum()/hin.sum_ksi_cr.sum()*100),2),'top30_segments_length_share_pct':round(float(seg_sorted.head(30).length_mi.sum()/hin.length_mi.sum()*100),2),'zero_ksi_segments':int((hin.sum_ksi_cr==0).sum())}
stats['human_scale_derived']={'ksi_per_mile':'8.6 recorded KSI crashes per network mile (1,955 / 226.3 miles, derived)','high_tier':'about 1 in 5 recorded KSI crashes in the network sits on the 16 High-tier segments (372 of 1,955, derived)'}
# Fusion with crash layer (street-name match, upper bound - NOT segment-accurate)
tc=pd.read_parquet(os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/stack/nashville/layers/traffic_accidents_clean.parquet"))
known=tc[~tc.counts_unknown_flag].copy()
known['ksi_crash']=(known.Number_of_Injuries.fillna(0)>0)|(known.Number_of_Fatalities.fillna(0)>0)
ABBR={'PKE':'PIKE','AV':'AVE'}
def norm(s):
    s=str(s).upper().strip(); s=re.sub(r'^\d+\s+','',s); s=re.sub(r'\s+',' ',s)
    return ' '.join(ABBR.get(t,t) for t in s.split(' '))
hin_names=set(hin.full_name.str.upper().str.strip())
def streets(addr):
    if pd.isna(addr): return []
    return [norm(p) for p in str(addr).upper().split('&')]
known['streets']=known.Street_Address.apply(streets)
known['on_hin_name']=known.streets.apply(lambda ss: any(s in hin_names for s in ss))
sub=known[known.Street_Address.notna()]
matched_names=set()
for ss in sub[sub.on_hin_name].streets: matched_names.update([s for s in ss if s in hin_names])
fus={'method':'street-name match only: a reported crash counts as name-matched when either side of its Street_Address, after house-number stripping and PKE->PIKE / AV->AVE expansion, equals a HIN full_name. This is NOT a segment or proximity join: HIN segments are specific stretches of those streets, so the name match is an upper bound on segment-level presence and is never printed as on-network crashes.',
 'crash_layer_rows_known_counts':int(len(known)),'addr_present':int(known.Street_Address.notna().sum()),'addr_missing':int(known.Street_Address.isna().sum()),
 'name_matched_crashes':int(sub.on_hin_name.sum()),'name_matched_share_pct':round(float(sub.on_hin_name.mean()*100),2),
 'crash_layer_ksi_crashes_addr_present':int(sub.ksi_crash.sum()),'name_matched_ksi':int(sub[sub.on_hin_name].ksi_crash.sum()),'name_matched_ksi_share_pct':round(float(sub[sub.on_hin_name].ksi_crash.sum()/sub.ksi_crash.sum()*100),2),
 'ksi_rate_name_matched_pct':round(float(sub[sub.on_hin_name].ksi_crash.mean()*100),2),'ksi_rate_not_matched_pct':round(float(sub[~sub.on_hin_name].ksi_crash.mean()*100),2),
 'name_matched_fatalities':int(sub[sub.on_hin_name].Number_of_Fatalities.sum()),'crash_layer_fatalities_addr_present':int(sub.Number_of_Fatalities.sum()),
 'hin_street_names':int(len(hin_names)),'hin_street_names_matched':int(len(matched_names)),'hin_street_names_unmatched':sorted(list(hin_names-matched_names)),
 'control_note':'Internal control: the same name-match run on the crash layer returns 109,443 name-matched crashes against the HIN layer own recorded frequency total of 29,530 - the gap is the expected signature of whole-street name matching vs segment-level accounting, and is why no name-matched figure is printed as an on-network figure.'}
# fix control numbers from actual
fus['name_matched_crashes']=int(sub.on_hin_name.sum())
stats['fusion_crash_layer']=fus
json.dump(stats, open(f"{BASE}/stats.json","w"), indent=2)
agg_sorted.to_csv(f"{BASE}/data/street_panel.csv", index=False)
hin.sort_values('sum_ksi_cr',ascending=False).to_csv(f"{BASE}/data/segment_panel.csv", index=False)
pd.DataFrame([{'category':k, **v} for k,v in cats.items()]).to_csv(f"{BASE}/data/category_panel.csv", index=False)
print(json.dumps(stats,indent=2))
