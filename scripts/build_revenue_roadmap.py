#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

ORANGE=(240,101,36); DARK=(34,31,31); GRAY=(120,120,128); GREEN=(34,170,94)
BG=(247,248,250); WHITE=(255,255,255); LINE=(229,231,235); DARKBAR=(60,60,70)
F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(s,b=False): return ImageFont.truetype(FB if b else F, s)
S=2; W,H=1600*S,1020*S
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
def t(x,y,s,fo,fi,center=False,right=False):
    if center or right:
        bb=d.textbbox((0,0),s,font=fo); w=bb[2]-bb[0]
        x=x-w/2 if center else x-w
    d.text((x,y),s,font=fo,fill=fi)

# Header
t(80*S,52*S,"amz",f(34,True),DARK); bb=d.textbbox((0,0),"amz",font=f(34,True))
t(80*S+(bb[2]-bb[0]),52*S,"visuals",f(34,True),ORANGE)
bb2=d.textbbox((0,0),"amzvisuals",font=f(34,True)); t(80*S+(bb2[2]-bb2[0]),52*S,".ai",f(34,True),DARK)
t(80*S,108*S,"3-Monats-Revenue-Plan",f(54,True),DARK)
t(80*S,178*S,"Ziel: 15k MRR  +  30k Projects  ·  low spend  ·  Engines: Cold Email (15k) · Agenturen (Tolt 25%) · Content · Free Teardown",f(24),GRAY)

# Chart
cx0=140*S; cx1=W-120*S; cyb=560*S; cyt=250*S; maxv=30000
months=["Monat 1","Monat 2","Monat 3"]
mrr=[3000,8000,15000]; proj=[8000,18000,30000]
n=len(months); slot=(cx1-cx0)/n; bw=80*S
# gridlines
for gv in [0,10000,20000,30000]:
    yy=cyb-(cyb-cyt)*gv/maxv
    d.line([cx0,yy,cx1,yy],fill=LINE,width=2*S)
    t(cx0-16*S,yy-14*S,f"{gv//1000}k",f(18),GRAY,right=True)
for i in range(n):
    cxc=cx0+slot*i+slot/2
    # MRR bar (orange) + projects bar (dark) side by side
    h1=(cyb-cyt)*mrr[i]/maxv; h2=(cyb-cyt)*proj[i]/maxv
    x1=cxc-bw-8*S; x2=cxc+8*S
    d.rounded_rectangle([x1,cyb-h1,x1+bw,cyb],radius=8*S,fill=ORANGE)
    d.rounded_rectangle([x2,cyb-h2,x2+bw,cyb],radius=8*S,fill=DARKBAR)
    t(x1+bw/2,cyb-h1-32*S,f"${mrr[i]//1000}k",f(22,True),ORANGE,center=True)
    t(x2+bw/2,cyb-h2-32*S,f"${proj[i]//1000}k",f(22,True),DARKBAR,center=True)
    t(cxc,cyb+16*S,months[i],f(26,True),DARK,center=True)
# legend
lx=cx1-360*S; ly=cyt-6*S
d.rounded_rectangle([lx,ly,lx+22*S,ly+22*S],radius=5*S,fill=ORANGE)
t(lx+32*S,ly,"MRR (kumuliert)",f(20),DARK)
d.rounded_rectangle([lx+200*S,ly,lx+222*S,ly+22*S],radius=5*S,fill=DARKBAR)
t(lx+232*S,ly,"Projects (kum.)",f(20),DARK)

# Month cards
cards=[
 ("Monat 1 — Fundament + erstes Cash",
  ["Dev: Checkout (B1/B2) + AI (B3) fixen","Cold-Infra: Domains + Warmup","10–15 Vorher/Nachher-Teardowns","Warme Audience + Webinar → erste Abos","Concierge-Sales via Stripe-Link"]),
 ("Monat 2 — Engine skalieren",
  ["Cold @ Vollvolumen (1–2k/Woche)","8–10 Agentur-Partner (Tolt)","Content 3–5/Woche (YT/TikTok/Reels)","Annual-Angebot + Upsell Starter→Premium","Beste Betreffzeile/Offer iterieren"]),
 ("Monat 3 — Push aufs Ziel",
  ["Bester Kanal (CAC) doppelt pushen","Case-Study + Webinar #2","15+ Agentur-Partner","Referral-Loop aktivieren","→ 15k MRR + 30k Projects"]),
]
y0=640*S; ch=320*S; gap=36*S
cw=(W-160*S-2*gap)/3; x0=80*S
for i,(title,items) in enumerate(cards):
    x=x0+i*(cw+gap)
    pop = i==2
    d.rounded_rectangle([x,y0,x+cw,y0+ch],radius=20*S,fill=WHITE,outline=(ORANGE if pop else LINE),width=(3*S if pop else 2*S))
    # number circle
    d.ellipse([x+28*S,y0+28*S,x+28*S+44*S,y0+28*S+44*S],fill=ORANGE)
    t(x+28*S+22*S,y0+34*S,str(i+1),f(28,True),WHITE,center=True)
    t(x+92*S,y0+30*S,title.split("—")[1].strip(),f(24,True),DARK)
    t(x+92*S,y0+62*S,title.split("—")[0].strip(),f(18,True),GRAY)
    cy=y0+118*S
    for it in items:
        d.ellipse([x+34*S,cy+8*S,x+34*S+10*S,cy+18*S],fill=ORANGE)
        t(x+58*S,cy,it,f(20),DARK); cy+=40*S

t(W//2,y0+ch+28*S,"Budget ~$0–1k/Mo (Tools + optional VA/Editor) · keine großen Ads · Voraussetzung: Checkout funktioniert + Lieferkapazität (AI-Fix)",
  f(20,True),GRAY,center=True)

img=img.resize((W//S,H//S),Image.LANCZOS)
out="/home/user/amzvisualsai/docs/assets/3-month-revenue-roadmap.png"
import os; os.makedirs(os.path.dirname(out),exist_ok=True); img.save(out)
print("Saved:",out)
