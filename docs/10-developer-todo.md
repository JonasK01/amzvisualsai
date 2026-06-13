# 10 · Was der Developer machen muss (zentrale To-do-Liste)

> **Das ist das Hauptdokument für den Developer.** Eine priorisierte, abarbeitbare
> Liste. Details zu einzelnen Punkten stehen in den verlinkten Docs; Tracking läuft
> über `AMZVisuals_Relaunch_Backlog.xlsx`.
> Reihenfolge = von oben nach unten abarbeiten.

## Kontext in 3 Sätzen
- Das **live deployte** Tool ist viel weiter als der alte Prototyp `sb1-oc1x2hve`:
  Signup, Zahlung, Brand-/Produkt-Anlage, Designer-Dashboard mit Versionierung,
  Visual Library und ein AI-Modul existieren bereits.
- **Backend = Supabase**; es gibt eine `/designer`-Route.
- Relaunch = **fixen + fertigstellen** (kein Neubau). Die 3 Blocker sind kritisch.

---

## 0. Voraussetzungen (zuerst klären)
- [ ] **Zugriff aufs Live-Repo** sicherstellen (nicht `sb1-oc1x2hve`).
- [ ] Zugriff auf **Supabase-Projekt**, **Stripe-Dashboard**, **AI-Provider-Keys**.
- [ ] Env/Secrets vollständig? (E-Mail-Provider, Stripe-Webhook-Secret, AI-Keys)
- [ ] Logging/Monitoring aktiv, damit Fehler sichtbar werden („a lot of things have been downed").

---

## 1. 🔴 BLOCKER — ohne die kein Relaunch

### B1 · Registrierung kaputt / keine Bestätigungsmail  · `02:24–03:37`
Neue User können sich nicht registrieren; keine Bestätigungsmail (auch nicht Spam).
- [ ] Supabase **Auth** + E-Mail-/SMTP-Provider prüfen (Templates, Absenderdomain, Rate-Limits).
- [ ] Signup-Flow End-to-End testen (frische E-Mail).
- [ ] Fehler-/Erfolgs-States im UI sauber anzeigen.

### B2 · Zahlung schließt nicht ab (bleibt „pending")  · `13:00–15:14`
UI zeigt „payment successful", Order bleibt „payment pending"; auch mit 100%-Code.
- [ ] **Stripe-Webhook** (`checkout.session.completed` / `payment_intent.succeeded`) prüfen — kommt er an, wird der Order-Status gesetzt?
- [ ] 100%-Rabattcode-Fall (0 €) testen — eigener Pfad nötig.
- [ ] Langer Ladezustand bei „finish order" beheben.

### B3 · AI-Bildgenerierung läuft nicht  · `23:30`
Das AI-Modul startet gar nicht.
- [ ] AI-Provider-Anbindung/Keys/Quota prüfen; Fehler loggen.
- [ ] Generierungs-Flow wieder lauffähig: Produkt → Typ „Main Image" → Referenzbild → generieren.
- [ ] (Danach Ausbau: siehe §4 AI-Modul.)

---

## 2. 🟠 HIGH — wichtige Bugs / Workflow-Korrektheit

- [ ] **H1 State-Verlust beim Tab-Wechsel** (`11:32–12:19`): Beim Anlegen von Produkt/Order autosaven, damit Wechsel zu anderem Tab (ASIN kopieren) nichts verliert.
- [ ] **H2 Falscher Status** (`17:36`): Nach „approve anyway" → Status muss **„finalizing"** sein, nicht „in progress".
- [ ] **H3 Designer-Dashboard** (`18:24`): aktualisiert nicht automatisch → Live-/Auto-Refresh.
- [ ] **H4 Approval-Status missverständlich** (`19:20`): Bei „approve anyway" sieht Designer „approved", obwohl nicht freigegeben. Echten Review-Status eindeutig machen, User-Kommentare prominent zeigen.
- [ ] **H5 Keine Completion-Benachrichtigung** (`21:43`): Bei „complete" → In-App-Notification (auf **ungelesen**) **und** E-Mail an den Client.

---

## 3. 🟡 UX / Copy / Visuell

- [ ] **U1** Copy „few projects" → „View project/order". `14:11`
- [ ] **U2** Order-Übersicht: zu viel Copy, Wichtiges schwer erkennbar → vereinfachen. `15:56`
- [ ] **U3** „Pending review" nicht pro Bild, sondern **einmal pro Produkt** neben dem Namen. `16:13`
- [ ] **U4** Freigegebenes Einzelbild zeigt klar „Approved"; Approve-Button verschwindet dann. `17:15`
- [ ] **U5** „Review order"-Schritt erwägen zu entfernen (direkt zur Zahlung). `12:39`
- [ ] **U6** „Feedback"-Wording für Client raus → „Nicht zufrieden? Melde dich bei uns" + Kontakt-Mail. `22:07`
- [ ] **U7** Download-Auffindbarkeit: klarer Hinweis/Link „Zum Download → Visual Library". `22:21`
- [ ] **U8** Brand-Form: Hinweis „Wenn Brand Guide hochgeladen, Farben/Schriften optional". `05:13`
- [ ] **V1** Tippfehler „No Gas" → **„No-Gos"** (Brand-Form). `Frame f9`
- [ ] **V2** Text-/Banner-Kontrast global anheben (WCAG AA) — Hilfetexte/Platzhalter zu hell. `f1,f7,f9,f19,f46`
- [ ] **V3** Chat-Widget-Position so, dass es CTAs/Modals nicht überlappt. `f7,f9,f52`
- [ ] **V4** Leere/kaputte Render-States abfangen (Loading-/Error-States). `f3,f50,f54`

> Details & Frames: [05-walkthrough-findings.md](05-walkthrough-findings.md) · [06-ui-review.md](06-ui-review.md)

---

## 4. Module: bauen / fertigstellen

### AI Image Creation (fixen → finalisieren)
- [ ] B3 fixen (oben).
- [ ] **Prompt-Agent (A2)** `24:39–26:03`: aus Produktdaten + Bild automatisch ein starkes Main-Image-Konzept (relevantes Element kombinieren, z. B. Produkt + Huhn; passenden Badge vorschlagen, z. B. „40% Protein").
- [ ] **Produkttreue**: echtes Produkt aus Foto erhalten, nur Szene/Hintergrund generieren (Compositing/Inpainting).
- [ ] **Text via Overlays/Templates**, nicht per AI (Lesbarkeit).
- [ ] **Amazon-Konformität** als Guardrail (Maße, weißer HG bei Hero).
- [ ] Provider hinter `ImageProvider`-Interface kapseln (austauschbar).
> Spec: [02-produkt-spec.md §2](02-produkt-spec.md)

### Ad-Video-Modul (NEU)
- [ ] Stufe 1: Template-/Motion-basiert (Bilder + Animation + Text + Musik, z. B. Remotion) + Render-Worker.
- [ ] Export-Presets: Amazon Listing / Sponsored Brands / 9:16 / 1:1.
- [ ] Im Tool kaufbar (Subscription/Credits).
- [ ] Stufe 2 (später): generatives AI-Video hinter `VideoProvider`.
> Spec: [02-produkt-spec.md §3](02-produkt-spec.md)

### Partnerprogramm (minimaler Dev — Tool macht den Rest)
- [ ] **Tolt** an Stripe anbinden (Tracking-Links, Cookie-Attribution, Partner-Dashboards, 25% lifetime, Auszahlungen Wise/Payoneer/PayPal).
- [ ] **`?ref=CODE`** aus Affiliate-Link in Cookie speichern und bei Signup dem User zuordnen (`referred_by_agency`).
- [ ] **Optionales Signup-Feld** „Von einer Agentur empfohlen? (Name/Code)" als Fallback.
- [ ] (Optional) „Agentur-managed"-Modus: 25% Dauerrabatt statt Provision.
> Spec: [07-agentur-partnerprogramm.md](07-agentur-partnerprogramm.md)

---

## 5. Architektur — von Anfang an beachten
- [ ] **Multi-Tenancy / `org_id`** in Datenmodell, Auth & Storage einziehen (auch wenn Full White-Label erst später) — Nachrüsten ist teuer.
- [ ] **Provider-Abstraktion** für AI-Bild & -Video (Modelle wechseln häufig).
- [ ] **Async-Jobs/Queue** für Generierung & Video-Rendering (nie synchron im Request); Status + Webhooks.
> Stack/Datenmodell: [03-developer-handoff.md](03-developer-handoff.md)

---

## 6. Vorgeschlagene Reihenfolge (Sprints)
1. **Sprint 1 — Relaunch-fähig:** §0 + §1 (B1, B2, B3) → Onboarding, Umsatz & AI laufen.
2. **Sprint 2 — Stabil & sauber:** §2 (H1–H5) + die größten §3-Punkte (U2, U3, U6, V2, V3).
3. **Sprint 3 — AI finalisieren:** §4 AI-Modul (Prompt-Agent, Produkttreue, Konformität).
4. **Sprint 4 — Wachstum:** §4 Partnerprogramm (Tolt + ref) und Ad-Video Stufe 1.
5. Restliche §3-Politur laufend.

> Tracking & Status pflegen in `AMZVisuals_Relaunch_Backlog.xlsx`.
