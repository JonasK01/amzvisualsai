# 14 · Execution-Playbook — Schritt für Schritt zu Revenue

> Die exakten Schritte, um den 3-Monats-Plan (docs/13) umzusetzen. Reihenfolge
> einhalten. `[ ]` = abhaken. Tools low-spend. „DoD" = Definition of Done.

---

## WOCHE 1 — Setup (5 Workstreams parallel)

### A) Dev: Checkout & AI reparieren (höchste Prio)
- [ ] Developer auf `docs/10` + `AMZVisuals_Developer_ToDo_EN.xlsx` ansetzen.
- [ ] **B1 Signup**, **B2 Zahlung** zuerst — ohne die kommt kein Geld rein.
- [ ] **B3 AI** danach (treibt Lieferkapazität).
- **DoD:** Ein Test-Kauf mit echter Karte geht durch, Order-Status wird „paid", Bestätigungsmail kommt.

### B) Payments-Fallback (damit du SOFORT verkaufen kannst, ohne aufs Tool zu warten)
- [ ] Stripe öffnen → **Payment Links** → „+ New".
- [ ] Je einen Link erstellen für: Listing Images, A+ Premium, Brand Story, Brand Store
  (Einmal) **und** für Ad Starter/Premium/Agency (als **recurring monthly**).
- [ ] Links in einem Doc sammeln → im Sales-Gespräch direkt schicken.
- **DoD:** Du kannst heute eine Rechnung/Link verschicken und Geld empfangen.

### C) Cold-Email-Infrastruktur (richtig, sonst Liste verbrannt)
- [ ] 2–3 **Sekundär-Domains** kaufen (Namecheap/Cloudflare), z. B. `getamzvisuals.com`,
  `tryamzvisuals.com`, `amzvisuals-team.com`. **Nicht** die Hauptdomain nutzen.
- [ ] Pro Domain **2–3 Postfächer** anlegen (Google Workspace ~$6/Postfach, oder
  Smartlead/Instantly „done-for-you inboxes").
- [ ] Pro Domain **DNS setzen: SPF, DKIM, DMARC** (sonst Spam).
- [ ] Domains in **Smartlead oder Instantly** (~$30–100/Mo) verbinden.
- [ ] **Warmup einschalten** → **14 Tage laufen lassen**, bevor du echte Mails sendest.
- [ ] Open-Tracking AUS, eigenes Tracking-Domain setzen (Deliverability).
- [ ] Sende-Limit: starte ~20/Postfach/Tag, hochrampen auf ~30–50.
  (3 Domains × 3 Postfächer × 40 = ~360/Tag = ~1,8k/Woche → 15k in ~8–9 Wochen.)
- **DoD:** Postfächer warm, Tool verbunden, Testmail landet im Posteingang (nicht Spam).

### D) CRM (Close) + Partner-Tool (Tolt)
- [ ] **15k Leads in Close importieren**, taggen: `seller` vs `agentur`, schlechte Bilder markieren.
- [ ] **Lead-Status-Pipeline** anlegen: Neu → Kontaktiert → Geantwortet → Call gebucht → Kunde/Partner → Kein Interesse.
- [ ] **Smart View** „Seller – Neu" + „Agentur – Neu".
- [ ] **Sequenzen** aus `docs/08` als Templates anlegen (noch nicht aktiv senden).
- [ ] **Tolt** mit Stripe verbinden → Programm „25% lifetime, auf tatsächlich gezahlten Betrag" → Partner-Link-Format aktivieren.
- **DoD:** Liste segmentiert, Sequenz-Templates bereit, Tolt erzeugt Partner-Links.

### E) Sales-Assets produzieren (das Verkaufs-Herzstück)
- [ ] **10–15 Vorher/Nachher-Teardowns** erstellen (verschiedene Kategorien). Bis AI
  gefixt: manuell/mit Designer; danach im Tool.
- [ ] **1-Seiten-Sales-Deck** + die Pricing-Visual (`docs/assets/ad-packages-pricing-mockup.png`).
- [ ] **Free-Teardown-Prozess** definieren: Lead nennen → Hauptbild redesignen → als „Vorschau" schicken.
- **DoD:** Du hast Beweise + ein klares „Free Teardown"-Angebot zum Verschicken.

---

## WOCHE 2 — Warm-Launch (schnellstes Geld zuerst)
- [ ] **Launch-E-Mail** an Academy-Liste/Alt-Kunden: „Neue Ad-Pakete + Launch-Angebot"
  (z. B. erster Monat rabattiert oder 1 gratis Teardown). CTA = Payment-Link/Call.
- [ ] **Live-Webinar/Workshop** ansetzen: „2x CTR durchs Hauptbild" → am Ende Pakete pitchen.
- [ ] Alle Interessenten in Close → sofort Call/Teardown → closen (Payment-Link).
- [ ] Erste 3–5 **Agenturen** aus deinem Netzwerk persönlich ansprechen (Tolt-Link).
- **DoD:** Erste zahlende Kunden + erste Agentur-Partner. Ziel Ende M1: ~3k MRR + ~8k Projects.

---

## WOCHE 3–4 — Cold live + Agentur-Akquise
- [ ] Warmup fertig → **Cold-Sequenz an Segment „Seller"** starten (Teardown-Hook).
- [ ] **Jede positive Antwort → kostenloses Teardown** → Call → Close (Payment-Link/Tool).
- [ ] **Cold-Sequenz an Segment „Agentur"** (docs/08, „25% lifetime, ohne Designer").
- [ ] **Content-Start:** 3–5 Teardown-Videos (YouTube/TikTok/Reels) – Format „Ich redesigne dieses Listing".
- [ ] Wöchentlich Zahlen reviewen, beste Betreffzeile/Offer behalten.
- **DoD:** Cold-Engine läuft, erste Cold-Closes, Content-Kadenz steht.

---

## MONAT 2 — Skalieren
- [ ] Cold auf Vollvolumen (~1,8k/Woche), A/B auf Betreff & Offer.
- [ ] **8–10 Agentur-Partner** (je 1–3 Kunden) → großer MRR-Hebel.
- [ ] Content 3–5/Woche, Teardowns überall recyceln.
- [ ] **Annual-Angebot** (2 Monate gratis) + **Upsell Starter→Premium** an Bestandskunden.
- **DoD Ende M2 (kumuliert):** ~8k MRR + ~18k Projects.

## MONAT 3 — Push aufs Ziel
- [ ] Den Kanal mit bestem CAC verdoppeln (meist Cold-Teardown oder Agenturen).
- [ ] **Case-Study + Webinar #2** (jetzt mit echten Ergebnissen).
- [ ] Agentur-Partner 15+, **Referral-Loop** (Kunde wirbt Kunde, Credits als Anreiz).
- **DoD Ende M3:** **~15k MRR + ~30k Projects.**

---

## Täglicher Founder-Rhythmus (90 Tage)
1. **Replies & Teardowns zuerst** (warmer Lead = sofort reagieren).
2. **Calls** führen + closen (Payment-Link parat).
3. **Outreach-Nachschub** (neue Cold-Batch + Agentur-Follow-ups).
4. Abends: neue Leads/Teardowns für morgen vorbereiten.
- **Montag:** Content-Batch + Wochenzahlen. **Freitag:** Agentur-Akquise.

## Wöchentliche KPIs (in Close)
Cold: gesendet · Reply% · Teardowns · Calls · Closes · $ — MRR & #Abos/Tarif · Churn —
Projects $ & #Orders — Agenturen: #Partner · Kunden/Partner.

## Spend-Übersicht (low)
Domains + Smartlead/Instantly ~$150–250/Mo · optional VA ~$300–500/Mo · optional
Editor ~$300/Mo · Close + Tolt bestehend. **Keine großen Ads.**

## Die 3 häufigsten Fehler (vermeiden)
1. Cold ohne Warmup/DNS → Liste verbrannt.
2. Aufs „perfekte Tool" warten → nutze Payment-Links & Concierge ab Tag 1.
3. Mehr verkaufen als liefern → Kapazität im Blick (AI-Fix B3 ist das Ceiling).
