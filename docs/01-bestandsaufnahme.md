# 01 · Bestandsaufnahme (Code-Audit)

Stand: Juni 2026. Basis: Code-Audit des einzigen auffindbaren Codes,
`JonasK01/sb1-oc1x2hve` (StackBlitz/Bolt-Export). Das verbundene Repo
`JonasK01/amzvisualsai` ist leer.

> **⚠️ KORREKTUR (nach Loom-Walkthrough 2026-06-13):** Der hier auditierte Code
> `sb1-oc1x2hve` ist ein **frühes UI-Mockup**, **nicht** das live deployte Produkt.
> Das echte, live deployte Tool ist deutlich weiter: Signup/Login,
> Brand-/Produkt-Anlage, Visual-Order-Flow, **Bezahlung mit Rabattcodes**,
> **Designer-Dashboard mit Versionierung**, **Visual Library** und ein
> **AI-Image-Generierungs-Modul** existieren bereits (Letzteres aktuell *kaputt*,
> nicht *fehlend*). Die folgende „Was fehlt"-Analyse gilt also für den Prototyp,
> **nicht** für das Live-Produkt. Siehe [05-walkthrough-findings.md](05-walkthrough-findings.md).
> Nächster Schritt: Zugriff auf das **Live-Repo** sicherstellen.

## TL;DR

Was existiert, ist ein **wunderschön gestaltetes, aber reines Frontend-Mockup**
eines Agentur-Bestellportals. Es ist ein **klickbarer Prototyp**, kein
funktionierendes Produkt. Es gibt **kein Backend, keine AI, kein Video, keine
Zahlung, keinen Login**. Alle Daten sind hartcodiert.

Wichtig für die Erwartungssteuerung: Die drei Prioritäten (AI-Bildgenerierung,
Ad-Video, White-Label) sind **Neubauten**, keine Finalisierungen.

## Was gebaut ist ✅

| Bereich | Beschreibung |
|---|---|
| Dashboard-Shell | Topbar, Sidebar (Visuals, Brands, Products, Visual Library, Account), Hauptbereich |
| Auftragsliste | „My Visual Orders" mit Such-/Filter-/Sortier-UI — auf **Mock-Daten** |
| Bestell-Flow | `CreateNewOrder.tsx` (~1.600 Zeilen): Service-Auswahl, Detail-Modals, Tooltips |
| Order-Zusammenfassung | `OrderSummary.tsx`, `ReviewOrder.tsx` |
| Service-Detail-Modal | `ServiceDetailModal.tsx` (~580 Zeilen) |
| Brand-Verwaltung | Liste von Marken (Mock), Such-UI |
| Design-System | Radix-UI-basierte Komponenten (button, card, tabs, input, avatar, badge, progress) |

### Service-Katalog (bereits mit Preisen im Code definiert)

**Einzelservices**
- Listing Images — 500 € (statt 750 €)
- A+/A++ Premium — 450 € (statt 650 €)
- Brand Story — 400 € (statt 580 €)
- Brand Store — 900 € (statt 1.200 €)

**Bundles**
- Launch Boost — 799 € (7× Listing Images + 5× A+ Content)
- Conversion Booster — 1.149 € (7× Listing + 7× A+ Premium + 3× Brand Story)
- AMZ Brand Domination — 1.899 € (Listing + A+ Premium + Brand Story + Brand Store)
- Starter Package — 550 € · Complete Brand Package — 1.200 € · Content Creator — 450 €

> Diese Preis-/Paketlogik ist wertvoll und sollte ins finale Produkt übernommen werden.

## Was NICHT existiert ❌

Code-weite Suche nach `ai`, `video`, `generate`, `api`, `fetch`, `auth`,
`upload`, `stripe`, `supabase` → **0 Treffer**.

| Fehlend | Konsequenz |
|---|---|
| Backend / DB / API | Nichts wird gespeichert; alles Mock |
| Authentifizierung | Kein Login, kein User-Konzept |
| Zahlung (Stripe) | Kein Umsatz möglich |
| Datei-Upload | Kunde kann keine Produktfotos hochladen |
| **AI-Bildgenerierung** | Kernversprechen „AI" nicht vorhanden |
| **Ad-Video-Modul** | Nicht vorhanden |
| **White-Label / Multi-Tenant** | Nicht vorhanden |
| „Products", „Visual Library", „Account" | „Coming soon"-Platzhalter |
| State-Persistenz | Reload = alles weg |

## Code-Qualität & Risiken

- **Stärke:** Sehr gutes, produktionsnahes UI/UX. Das Design ist ein echtes Asset.
- **Risiko 1 – Monolith:** `CreateNewOrder.tsx` mit ~1.600 Zeilen ist zu groß;
  bei Backend-Anbindung in kleinere Komponenten + State-Management aufteilen.
- **Risiko 2 – Bolt-Lock-in:** Export ist sauber (Vite), aber ohne Tests,
  ohne Env-Config, ohne CI. Vor Skalierung Fundament legen.
- **Risiko 3 – Mock-Sortierung:** Sortierlogik ist Platzhalter (`new Date()` vs `new Date()`).
- **Risiko 4 – Assets:** Bilder liegen als lokale Dateien (`/Mainv1.jpg` etc.),
  nicht in einem Asset-/CDN-Konzept.

## Empfehlung

Den Prototyp als **UI-Referenz und Design-Vorlage** behandeln, nicht als
Codebasis, die man „nur fertig macht". Das finale Produkt braucht ein echtes
Fundament (Backend, Auth, Zahlung, AI-Pipelines). Das gute UI wird darauf
neu/weiterverdrahtet. Reihenfolge siehe [Developer-Handoff](03-developer-handoff.md).
