import csv, json, os, collections
BASE=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-hin-brief-2026-11-14")
rows=list(csv.DictReader(open(f"{BASE}/data/nashville_hin_raw.csv")))
stats=json.load(open(f"{BASE}/stats.json")); checks=[]
def chk(name, a, b): checks.append({"check":name,"expected":b,"got":a,"pass":a==b})
chk("rows", len(rows), stats['rows'])
chk("distinct streets", len(set(r['full_name'] for r in rows)), stats['distinct_streets'])
chk("total frequency", sum(int(r['frequency']) for r in rows), stats['total_frequency_crashes'])
chk("total ksi", sum(int(r['sum_ksi_cr']) for r in rows), stats['total_ksi_crashes'])
chk("total length rounds", round(sum(float(r['length_mi']) for r in rows),2), stats['total_length_mi'])
for cat in ['High','Medium','Low']:
    g=[r for r in rows if r['Category']==cat]
    chk(f"{cat} segments", len(g), stats['by_category'][cat]['segments'])
    chk(f"{cat} ksi", sum(int(r['sum_ksi_cr']) for r in g), stats['by_category'][cat]['ksi'])
    chk(f"{cat} freq", sum(int(r['frequency']) for r in g), stats['by_category'][cat]['frequency'])
chk("zero ksi segments", sum(1 for r in rows if int(r['sum_ksi_cr'])==0), stats['concentration']['zero_ksi_segments'])
agg={}
for r in rows: agg[r['full_name']]=agg.get(r['full_name'],0)+int(r['sum_ksi_cr'])
chk("top street Gallatin ksi", agg['GALLATIN PIKE'], 173)
chk("top street Murfreesboro ksi", agg['MURFREESBORO PIKE'], 165)
res={"checks":len(checks),"passed":sum(1 for c in checks if c['pass']),"detail":checks}
json.dump(res, open(f"{BASE}/data/verify_independent_output.json","w"), indent=2)
print(res['passed'],"/",res['checks'],"passed"); assert res['passed']==res['checks']
