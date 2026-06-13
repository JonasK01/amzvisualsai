#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

# Brand
ORANGE = (240, 101, 36); DARK = (34, 31, 31); GRAY = (120, 120, 128)
GREEN = (34, 170, 94); BG = (247, 248, 250); WHITE = (255, 255, 255)
LINE = (229, 231, 235); POP = (240, 101, 36)

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(sz, bold=False): return ImageFont.truetype(FB if bold else F, sz)

S = 2  # supersample for crisp text
W, H = 1560*S, 1000*S
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text(x, y, s, font, fill, center=False, right=False):
    if center or right:
        bb = d.textbbox((0,0), s, font=font); w = bb[2]-bb[0]
        x = x - w/2 if center else x - w
    d.text((x, y), s, font=font, fill=fill)

# Header
text(80*S, 56*S, "amz", f(40, True), DARK)
bb = d.textbbox((0,0), "amz", font=f(40, True))
text(80*S+ (bb[2]-bb[0]), 56*S, "visuals", f(40, True), ORANGE)
bb2 = d.textbbox((0,0), "amzvisuals", font=f(40, True))
text(80*S+(bb2[2]-bb2[0]), 56*S, ".ai", f(40, True), DARK)
text(80*S, 120*S, "Monthly Ad Packages", f(58, True), DARK)
text(80*S, 196*S, "Wiederkehrende Abos  ·  monatlich kündbar  ·  über Stripe", f(28), GRAY)

# Cards
cards = [
    {"name":"Ad Starter", "tag":"TARIF", "price":"$197", "popular":False,
     "items":[("2 Brand Ad Creatives / Monat",True),("1 Ad Video / Monat",True),
              ("Amazon-optimiert",True),("White-Label Dateien",False)]},
    {"name":"Ad Premium Package", "tag":"EMPFOHLEN", "price":"$497", "popular":True,
     "items":[("5 Brand Ad Creatives / Monat",True),("3 Ad Videos / Monat",True),
              ("Amazon-optimiert",True),("Monatlich kündbar",True)]},
    {"name":"Ad Agency", "tag":"TARIF", "price":"$997", "popular":False,
     "items":[("12 Brand Ad Creatives / Monat",True),("8 Ad Videos / Monat",True),
              ("Priority-Lieferung",True),("White-Label Dateien",True)]},
]

cw, ch = 440*S, 600*S
gap = 40*S
total = len(cards)*cw + (len(cards)-1)*gap
x0 = (W - total)//2
y0 = 280*S

for i, c in enumerate(cards):
    x = x0 + i*(cw+gap)
    y = y0
    pop = c["popular"]
    # card bg
    d.rounded_rectangle([x, y, x+cw, y+ch], radius=24*S, fill=WHITE,
                        outline=(POP if pop else LINE), width=(4*S if pop else 2*S))
    # popular ribbon
    if pop:
        rw, rh = 150*S, 44*S
        d.rounded_rectangle([x+cw-rw-24*S, y-rh//2, x+cw-24*S, y+rh//2], radius=22*S, fill=POP)
        text(x+cw-rw//2-24*S, y-rh//2+9*S, "POPULAR", f(22, True), WHITE, center=True)
    pad = 36*S
    cy = y + 44*S
    # tag
    tagcol = GREEN if c["tag"]=="EMPFOHLEN" else GRAY
    text(x+pad, cy, c["tag"], f(20, True), tagcol); cy += 36*S
    # name
    text(x+pad, cy, c["name"], f(36, True), DARK); cy += 64*S
    # price
    text(x+pad, cy, c["price"], f(56, True), ORANGE)
    bbp = d.textbbox((0,0), c["price"], font=f(56, True))
    text(x+pad+(bbp[2]-bbp[0])+12*S, cy+28*S, "/ Monat", f(26), GRAY)
    cy += 92*S
    # divider
    d.line([x+pad, cy, x+cw-pad, cy], fill=LINE, width=2*S); cy += 28*S
    text(x+pad, cy, "Enthalten:", f(24, True), DARK); cy += 46*S
    for label, ok in c["items"]:
        col = GREEN if ok else (200,200,205)
        mark = "✓" if ok else "—"
        text(x+pad, cy-2*S, mark, f(26, True), col)
        text(x+pad+38*S, cy, label, f(25), DARK if ok else (170,170,175))
        cy += 46*S
    # button
    by = y+ch-80*S
    d.rounded_rectangle([x+pad, by, x+cw-pad, by+52*S], radius=14*S,
                        fill=(ORANGE if pop else WHITE), outline=ORANGE, width=2*S)
    text(x+cw//2, by+12*S, "Subscribe", f(26, True), (WHITE if pop else ORANGE), center=True)

# Footer note
fy = y0 + ch + 50*S
text(W//2, fy, "Empfohlene Preise (USD)  ·  25% Partner-Provision bereits eingeplant  ·  jährlich = 2 Monate gratis",
     f(26, True), DARK, center=True)
text(W//2, fy+40*S, "Use-it-or-lose-it · bei Limit gesperrt bis nächster Monat · Kündigung zum Periodenende (Stripe Customer Portal)",
     f(23), GRAY, center=True)

img = img.resize((W//S, H//S), Image.LANCZOS)
out = "/home/user/amzvisualsai/docs/assets/ad-packages-pricing-mockup.png"
import os; os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out)
print("Saved:", out)
