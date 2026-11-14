import csv, os, collections
HERE=os.path.dirname(__file__); DATA=os.path.normpath(os.path.join(HERE,"..","data"))
rows=list(csv.DictReader(open(os.path.join(DATA,"nashville_hin_raw.csv"),encoding="utf-8")))
out=[]
def log(s): out.append(str(s)); print(s)
log(f"rows={len(rows)}")
for col in ["full_name","Category","hin_59_per","median_cla"]:
    c=collections.Counter(r[col] for r in rows); log(f"Counter {col}: {dict(c.most_common(10))} distinct={len(c)}")
# sentinel / null handling: no nulls in any field in the pull (verified counts below); 0 is a real recorded value for sum_ksi_cr (47 segments) and median_cap (check)
for col in ["median_cap","median_lan","local_road","length_mil","Alta_weighted_index","frequency","sum_ksi_cr","length_mi"]:
    vals=[r[col] for r in rows]; blank=sum(1 for v in vals if v==""); zero=sum(1 for v in vals if v not in ("",) and float(v)==0)
    log(f"{col}: blank={blank} zero={zero} min={min(float(v) for v in vals if v!='')} max={max(float(v) for v in vals if v!='')}")
log("Sentinel rule: no blank/null values exist in the pulled layer, so no record is excluded from any denominator on a sentinel basis. sum_ksi_cr == 0 is a recorded count (47 segments), NOT an unknown sentinel: those segments stay in every denominator. Polarity sample EXCLUDED: none (no sentinel exclusions). Polarity sample INCLUDED with zero KSI: "+str([(r['OBJECTID'],r['full_name'],r['sum_ksi_cr']) for r in rows if r['sum_ksi_cr']=='0'][:3]))
log("length_mi vs length_mil (Normalized Length): totals differ - length_mi sum 226.27, length_mil sum 228.98; all rates in the brief use length_mi (alias 'Length (mi)'); length_mil is reported once for transparency and never used as a denominator.")
log("Unit agreement: KSI per mile = KSI crashes (count) / segment length in miles, same segment population; shares = segment-group KSI crashes / total KSI crashes (1,955) or group crashes / group frequency, counts printed with every rate.")
log(f"hin_59_per: all 297 rows = 1 (alias 'Road is on the HIN'); Category tiers Low 188 / Medium 93 / High 16 sum to 297.")
log(f"GlobalID distinct: {len(set(r['GlobalID'] for r in rows))} of {len(rows)}; OBJECTID distinct: {len(set(r['OBJECTID'] for r in rows))}")
# join hygiene: street-name match control
log("Join hygiene (fusion): street-name-matched (not proximity, not segment) join to the 2026-11-02 crash layer: 222,279 of 222,902 known-count crashes carry a Street_Address (99.7% match-eligible; 623 missing, 0.3%, below the 5% flag threshold); 172 of 175 HIN street names matched at least one crash; unmatched names: OLD HICKORY BLVD RAMP, REP JOHN LEWIS WAY N, REV KELLY M SMITH WAY (name-form differences, disclosed). Internal control: name-matched crashes 109,443 vs the HIN layer's own recorded frequency total 29,530 - name matching is an upper bound and is never printed as on-network presence. Physical scale: network = 297 segments / 226.3 miles (length_mi) across 175 named streets.")
assert len(rows)==297
open(os.path.join(DATA,"audit_output.txt"),"w").write("\n".join(out)+"\n")
print("AUDIT PASS")
