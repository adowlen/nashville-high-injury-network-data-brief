from PIL import Image, ImageDraw, ImageFont
import os, json, textwrap
BASE=os.path.expanduser("~/workspace/goals/daily-civic-data-brief/hidden_files/nashville-hin-brief-2026-11-14")
art=os.path.join(BASE,"hero_source","media-generation-hero-art-nashville-hin-0-b77a5621-f227-4029-bda1-8144eafd0ad1.webp")
img=Image.open(art).convert("RGB"); W,H=img.size
d=ImageDraw.Draw(img,"RGBA")
for y in range(int(H*0.42)):
    a=int(200*(1-y/(H*0.42))+40); d.line([(0,y),(W,y)],fill=(18,18,18,min(a,235)))
def font(sz,bold=True):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,sz)
def wrap(text,f,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
d.text((60,60),"372 of 1,955",font=font(int(W*0.085)),fill=(232,163,61))
y=60+int(W*0.115); f2=font(int(W*0.040))
for line in wrap("19.0% of the network's KSI crashes sit on 16 High-tier segments — 6.1% of its miles",f2,W-120):
    d.text((60,y),line,font=f2,fill=(255,255,255)); y+=int(W*0.055)
source="Source: Nashville Vision Zero High Injury Network layer, 297 segments (pulled Nov 14, 2026) — HIN recorded counts"
fs=font(int(W*0.019),False); sl=wrap(source,fs,W-120)
yy=H-int(H*0.045)
for line in sl: d.text((60,yy),line,font=fs,fill=(235,235,235)); yy+=int(W*0.026)
open(os.path.join(BASE,"hero-headline.txt"),"w").write("372 of 1,955 — 19.0% of the network's KSI crashes sit on 16 High-tier segments — 6.1% of its miles\n"+source+"\n")
img.save(os.path.join(BASE,"hero.png")); print("hero saved", img.size)
