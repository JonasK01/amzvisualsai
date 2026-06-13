# 03 · Developer-Handoff

Dieses Dokument ist für den Developer. Es übersetzt die [Produkt-Spec](02-produkt-spec.md)
in Architektur, Stack-Empfehlung und ein priorisiertes Ticket-Backlog.

## 1. Leitprinzipien

1. **Prototyp = Design-Referenz, nicht Codebasis.** Das gute UI (`sb1-oc1x2hve`)
   übernehmen, aber auf ein echtes Fundament (Backend, Auth, Zahlung) stellen.
2. **Multi-Tenancy von Tag 1.** `organization_id` überall, auch wenn White-Label
   erst später live geht. Nachrüsten ist teuer.
3. **Provider-Abstraktion für AI.** Bild- und Video-Modelle hinter Interfaces
   (`ImageProvider`, `VideoProvider`) — Modelle ändern sich monatlich.
4. **Asynchron denken.** Generierung/Rendering laufen über Queue + Status, nie
   synchron im Request.
5. **Klein schneiden, früh Umsatz.** Done-for-you-Flow zuerst live (kein AI nötig),
   dann AI-Image-MVP (Hero + Lifestyle).

## 2. Empfohlener Tech-Stack

| Schicht | Empfehlung | Begründung |
|---|---|---|
| Frontend | Bestehendes React/Vite-UI → ggf. **Next.js** | SSR, Routing, API-Routes, Auth-Integration; UI 1:1 übernehmbar |
| Auth | Clerk / Supabase Auth / Auth.js | Org-/Team-Support für Multi-Tenancy |
| DB | **Postgres** (Supabase oder Neon) | Relational, RLS für Tenant-Isolation |
| Storage/CDN | S3 oder Cloudflare R2 + CDN | Uploads & Outputs |
| Queue/Jobs | Inngest / Trigger.dev / BullMQ | Async AI-/Video-Jobs, Retries, Status |
| Zahlung | **Stripe** (Billing + Credits + Connect) | Abos, Einmalzahlung, Wholesale; Connect für Agentur-Auszahlung |
| AI-Bild | hinter `ImageProvider`: fal.ai / Replicate / Gemini-Image + Background-Removal | austauschbar halten, evaluieren |
| AI-/Video-Render | **Remotion** (Stufe 1) + `VideoProvider` (Stufe 2: Kling/Runway/Veo) | template-basiert robust, generativ als Premium |
| Hosting | Vercel (Frontend) + Worker für Jobs | schnell, skaliert |

> Stack-Wahl ist eine Empfehlung, kein Dogma — wenn der Developer in einem anderen
> Setup (z. B. Supabase-zentriert) schneller ist, ist das ok, solange die
> Leitprinzipien (Multi-Tenant, Provider-Abstraktion, Async) erfüllt sind.

## 3. Datenmodell (Skizze)

```
organizations (tenant)         # auch für White-Label-Agenturen
  id, name, type[direct|agency], branding{logo,colors,domain}, plan, credits

users
  id, org_id, email, role[owner|member|client]

brands
  id, org_id, name, logo, colors, fonts, guidelines

products
  id, org_id, brand_id, name, asin, marketplace, source_images[]

orders                         # Done-for-you
  id, org_id, product_id, services[], status, price, assignee

generations                    # Self-Serve AI (Bild)
  id, org_id, product_id, type[hero|lifestyle|infographic|aplus],
  provider, prompt, status, input_assets[], output_assets[], credits_used

videos
  id, org_id, product_id, format, template, status, output_asset, credits_used

credit_ledger
  id, org_id, delta, reason, ref_id

subscriptions / payments       # Stripe-Sync
```

Tenant-Isolation über `org_id` + (bei Supabase) Row-Level-Security.

## 4. Ticket-Backlog (priorisiert)

### Epic 0 — Fundament (Voraussetzung für alles)
- [ ] Repo-Setup: Code aus `sb1-oc1x2hve` migrieren, ENV-Config, Linting, CI, Tests-Gerüst
- [ ] `CreateNewOrder.tsx` (~1.600 Z.) in Teilkomponenten zerlegen
- [ ] Auth + Org-/User-Modell (Multi-Tenant von Anfang an)
- [ ] Postgres-Schema (siehe §3), Migrations
- [ ] Asset-Upload + Storage/CDN
- [ ] Stripe-Grundintegration (Kunde, Zahlung, Webhooks)

### Epic 1 — Done-for-you live (schnellster Umsatz)
- [ ] Bestell-Flow an echtes Backend hängen (Order anlegen, speichern, Status)
- [ ] Zahlung beim Checkout (Einmalzahlung Service/Bundle)
- [ ] Auftrags-Dashboard für Kunde **und** internes Fulfillment-/Admin-Board
- [ ] Datei-Upload (Briefing, Produktfotos) + Liefer-/Review-Schleife (Kommentare)
- [ ] E-Mail-Benachrichtigungen (Status, Lieferung)

### Epic 2 — AI Image Creation (MVP: Hero + Lifestyle)
- [ ] `ImageProvider`-Interface + 1 Provider integrieren
- [ ] Background-Removal-Pipeline (Produkttreue!)
- [ ] Hero-Generierung (weißer HG, Amazon-Maße) + Lifestyle (Szene generieren)
- [ ] Async-Job + Status-UI + Varianten-Auswahl
- [ ] Credits abziehen / Re-Roll
- [ ] Amazon-Konformitäts-Check vor Download
- [ ] Danach: Infografik + A+-Modul (Template-Overlays)

### Epic 3 — Ad-Video (Stufe 1 zuerst)
- [ ] Remotion-Setup + Render-Worker
- [ ] 3–5 Video-Templates (Feature-Highlight, Lifestyle-Montage, …)
- [ ] Export-Presets (Amazon Listing / Sponsored Brands / 9:16 / 1:1)
- [ ] Musik-Bibliothek (lizenzfrei) + Text-Overlay-Editor
- [ ] Danach: `VideoProvider` (generatives AI-Video) als Premium

### Epic 4 — White-Label / Agenturen
- [ ] Branding pro Org (Logo, Farben, Subdomain)
- [ ] Reseller-Dashboard (Kunden, Aufträge, Verbrauch)
- [ ] Agentur-eigene Preise/Pakete + Marge
- [ ] Wholesale-/Credit-Billing (Stripe), Rollen client/member/owner
- [ ] Full-Stufe: Custom Domain, eigene E-Mail-Domain, API-Zugang

## 5. Grobe Aufwandseinordnung

Reihenfolge (nicht parallel alles): **Epic 0 + 1** zuerst → erster echter Umsatz.
Dann **Epic 2** (das eigentliche „AI"-Versprechen). Dann **Epic 3**, dann **Epic 4**.
White-Label-Architektur (org_id) aber bereits in Epic 0 mitziehen.

Konkrete Tages-/Wochenschätzungen erst nach Stack-Festlegung mit dem Developer —
diese hängen stark von der gewählten Plattform und seiner Erfahrung ab.

## 6. Offene Punkte (vom Developer/Jonas zu klären)
- Wo liegt ggf. ein bereits begonnener AI-Teil? (StackBlitz-Account des Developers prüfen)
- Welche AI-Provider sind budgetseitig ok? (Kosten pro Generierung/Render)
- Eigene Fulfillment-Kapazität für Done-for-you (intern vs. Freelancer)?
- Rechtliches: Lizenzen für Stock/Musik, AGB, Amazon-ToS, DSGVO (DE/EU-Hosting?)
