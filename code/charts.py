import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, pandas as pd, json, os
BASE=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-hin-brief-2026-11-14")
stats=json.load(open(f"{BASE}/stats.json"))
CHAR="#232323"; AMBER="#E8A33D"; TEAL="#2A9D8F"; GREY="#8A8A8A"
plt.rcParams.update({"font.size":10,"axes.edgecolor":GREY,"text.color":CHAR,"axes.labelcolor":CHAR,"xtick.color":CHAR,"ytick.color":CHAR})
def save(fig,name): fig.tight_layout(); fig.savefig(f"{BASE}/charts/{name}",dpi=200); plt.close(fig); print(name)
# 1 category KSI per mile
cats=['Low','Medium','High']; vals=[stats['by_category'][c]['ksi_per_mi'] for c in cats]; ns=[stats['by_category'][c]['segments'] for c in cats]; ks=[stats['by_category'][c]['ksi'] for c in cats]
fig,ax=plt.subplots(figsize=(6.4,3.8))
bars=ax.bar(cats,vals,color=[GREY,TEAL,AMBER])
for b,v,n,k in zip(bars,vals,ns,ks): ax.text(b.get_x()+b.get_width()/2,v+0.6,f"{v:.2f}\n({k} KSI, {n} segs)",ha='center',fontsize=9)
ax.set_ylabel("Recorded KSI crashes per mile"); ax.set_title("KSI crashes per mile by priority tier\n(HIN layer's own recorded counts, 297 segments)",fontsize=11)
ax.set_ylim(0,max(vals)*1.25); save(fig,"chart_category_ksi_per_mile.png")
# 2 top streets by KSI
top=pd.DataFrame(stats['top_streets_by_ksi']).iloc[::-1]
fig,ax=plt.subplots(figsize=(6.8,4.4))
bars=ax.barh(top.full_name,top.ksi,color=TEAL)
for b,v,l in zip(bars,top.ksi,top.length_mi): ax.text(v+3,b.get_y()+b.get_height()/2,f"{v} KSI / {l:.1f} mi",va='center',fontsize=9)
ax.set_xlabel("Recorded KSI crashes, all segments of the street in the network (HIN layer)")
ax.set_title("Streets carrying the most recorded KSI crashes in the network",fontsize=11); ax.set_xlim(0,200); save(fig,"chart_top_streets_ksi.png")
# 3 concentration: tier length share vs KSI share
import numpy as np
x=np.arange(3); w=0.38
ls=[stats['by_category'][c]['length_share_pct'] for c in cats]; kss=[stats['by_category'][c]['ksi_share_of_total_pct'] for c in cats]
fig,ax=plt.subplots(figsize=(6.4,3.8))
ax.bar(x-w/2,ls,w,color=GREY,label="Share of network miles"); ax.bar(x+w/2,kss,w,color=AMBER,label="Share of recorded KSI crashes")
for i,(a,b) in enumerate(zip(ls,kss)): ax.text(i-w/2,a+1.2,f"{a:.1f}%",ha='center',fontsize=9); ax.text(i+w/2,b+1.2,f"{b:.1f}%",ha='center',fontsize=9)
ax.set_xticks(x); ax.set_xticklabels([f"{c} ({stats['by_category'][c]['segments']} segs)" for c in cats]); ax.legend(fontsize=8); ax.set_ylabel("Percent"); ax.set_ylim(0,72)
ax.set_title("Miles vs KSI crashes, by tier (HIN layer's own recorded counts)",fontsize=11); save(fig,"chart_tier_concentration.png")
# 4 top streets ksi per mile (min 1 mi aggregated)
top2=pd.DataFrame(stats['top_streets_by_ksi_per_mi_min1mi']).head(8).iloc[::-1]
fig,ax=plt.subplots(figsize=(6.8,4.0))
bars=ax.barh(top2.full_name,top2.ksi_per_mi,color=AMBER)
for b,v,k,l in zip(bars,top2.ksi_per_mi,top2.ksi,top2.length_mi): ax.text(v+0.5,b.get_y()+b.get_height()/2,f"{v:.1f} ({k} KSI / {l:.1f} mi)",va='center',fontsize=9)
ax.set_xlabel("Recorded KSI crashes per mile, streets aggregated over their network segments (>=1 network mile only)")
ax.set_title("Highest KSI-per-mile streets in the network (aggregated, >=1 mi)",fontsize=11); ax.set_xlim(0,32); save(fig,"chart_top_streets_per_mile.png")
