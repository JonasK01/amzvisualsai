# 02 · Produkt-Spezifikation

Zielbild: **Hybrid** aus Self-Serve-AI und Done-for-you, plus White-Label-Kanal
für Agenturen. Diese Spec ist die Grundlage für den Developer-Handoff.

## 1. Produktmodell (Hybrid)

```
                amzvisuals.ai
   ┌──────────────────┬──────────────────┐
   │   SELF-SERVE AI   │   DONE-FOR-YOU    │
   │  (skaliert)       │   (Premium)       │
   ├──────────────────┼──────────────────┤
   │ AI Image Creation │ Brand Store        │
   │ Ad-Video (AI)     │ volle A+-Strecken  │
   │ Infografiken      │ Sonderwünsche      │
   │ Hintergrund-Swap  │ Review durch Team  │
   └──────────────────┴──────────────────┘
            ▲                    ▲
            └─── beide auch als ─┘
                  WHITE-LABEL für Agenturen
```

- **Self-Serve** = Credits/Abo. Kunde lädt Produktfoto hoch → AI generiert →
  Kunde lädt herunter. Hohe Marge, skaliert ohne Personal.
- **Done-for-you** = der bestehende Bestell-Flow. Höherpreisig, Team liefert.
  Schneller erster Umsatz, dient als Proof + Trainingsdaten für die AI.
- **White-Label** = Agenturen schalten beides unter eigener Marke frei.

**Sequenzierung:** Done-for-you-Flow zuerst produktiv schalten (schnellster Umsatz),
parallel AI-Image-MVP bauen, dann Ad-Video, dann White-Label. Begründung siehe
[Go-to-Market](04-go-to-market.md).

---

## 2. Modul: AI Image Creation

**Ziel:** Aus einem einfachen Produktfoto (oder ASIN) konvertierende
Amazon-Visuals generieren — markenkonsistent, Amazon-konform.

### User Flow
1. Kunde wählt Produkt (Upload Foto **oder** ASIN-Import) + Marketplace + Marke.
2. Kunde wählt Output-Typ: Hero-Bild (weißer HG) · Lifestyle · Infografik · A+-Modul.
3. AI generiert 3–4 Varianten.
4. Kunde verfeinert (Prompt, Hintergrund, Text-Overlays) und lädt herunter.

### Output-Typen & technischer Ansatz
| Output | Ansatz |
|---|---|
| Hero (weißer Hintergrund) | Background-Removal + Clean-Compositing (Amazon-Vorgabe: reiner weißer HG) |
| Lifestyle | Produkt freistellen → AI-Szene generieren → realistisches Einsetzen (Schatten/Licht) |
| Infografik | AI-Szene/Feature-Shots + Template-basierte Text-/Icon-Overlays (kein freier AI-Text — Lesbarkeit!) |
| A+-Modul | Kombination aus Bildern + Template-Layouts in Amazon-A+-Maßen |

### Wichtige Design-Entscheidungen (für Developer)
- **Produkttreue ist kritisch.** Reine Text-zu-Bild-Generierung verändert das
  Produkt → unbrauchbar für Amazon. Lösung: Produkt aus echtem Foto **freistellen
  und erhalten**, nur Hintergrund/Szene generieren (Compositing/Inpainting).
- **Text gehört in Templates, nicht in die AI-Generierung.** AI-generierter Text in
  Bildern ist unzuverlässig. Infografik-/A+-Texte über editierbare Overlay-Layer.
- **Amazon-Konformität als Guardrail:** Maße, weißer HG bei Hero, keine
  unzulässigen Claims/Badges. Als Validierungs-Layer vor Download.
- **Modell-agnostisch bauen.** Provider hinter einem Interface kapseln
  (`ImageProvider`), damit Modelle austauschbar bleiben. Kandidaten:
  Gemini-Image / „nano-banana", fal.ai, Replicate (SDXL + ControlNet/Inpainting),
  Background-Removal-Services. Konkrete Wahl im Handoff evaluieren.

### MVP-Schnitt (klein anfangen)
Erst **Hero + Lifestyle** (höchster Nutzen, technisch am klarsten). Infografik und
A+-Modul danach. Credits pro Generierung; Re-Rolls kosten Credits.

---

## 3. Modul: Ad-Video

**Ziel:** Kurze Produkt-/Werbevideos für Amazon (Sponsored Brands Video,
Listing-Video) und Social, generiert aus vorhandenen Bildern/Produktfotos.

### User Flow
1. Kunde wählt Produkt + (optional) bereits generierte Bilder als Input.
2. Wählt Format: Amazon-Listing-Video · Sponsored Brands · Social (9:16 / 1:1).
3. Wählt Stil/Template (Feature-Highlights, Unboxing-Look, Lifestyle-Montage).
4. AI erzeugt Video; Kunde kann Szenen/Text/Musik anpassen → Export.

### Technischer Ansatz (zwei Stufen)
- **Stufe 1 (schnell, robust):** Template-/Motion-basiert — Bilder + Ken-Burns/
  Slide-Animationen + Text-Overlays + Musik, gerendert serverseitig
  (z. B. Remotion). Vorhersehbar, günstig, Amazon-konform.
- **Stufe 2 (AI-Video):** Generative Clips (Image-to-Video) für dynamische Szenen,
  zusammengeschnitten mit Stufe-1-Templates. Provider-Kandidaten evaluieren
  (Kling, Runway, Veo, Luma). Hinter `VideoProvider`-Interface kapseln.

> Empfehlung: Mit **Stufe 1** live gehen (zuverlässiger ROI für Seller),
> generatives AI-Video als Premium-Erweiterung nachziehen.

### Amazon-Anforderungen beachten
Listing-Video-Maße/Länge, Sponsored-Brands-Video-Specs (Länge, Auflösung,
keine Schwarzbalken, kein Amazon-Logo etc.) als Export-Presets hinterlegen.

---

## 4. Modul: White-Label / Agenturen

**Ziel:** Agenturen, die kein eigenes Design haben, bieten amzvisuals unter
**ihrer** Marke ihren Kunden an. Das ist der wichtigste externe Wachstumshebel.

### Kernfähigkeiten
| Feature | Beschreibung |
|---|---|
| Multi-Tenant | Agentur = Organisation; deren Kunden = Sub-Accounts darunter |
| Eigenes Branding | Logo, Farben, eigene (Sub-)Domain `studio.agentur.de`, Absender-E-Mail |
| Eigene Preise | Agentur setzt eigene Endkundenpreise; Plattform-Preis = ihr Einkauf (Marge) |
| Reseller-Dashboard | Übersicht aller Kunden, Aufträge, Verbrauch, Abrechnung |
| Rollen & Rechte | Agentur-Admin, Agentur-Mitarbeiter, Endkunde |
| Abrechnung | Agentur zahlt Plattform (Wholesale/Credits), rechnet selbst mit Kunden ab |

### Architektur-Implikation (früh einplanen!)
Multi-Tenancy ist **schwer nachzurüsten**. Auch wenn White-Label als drittes
Modul kommt: **von Anfang an `organization_id` / `tenant_id`** in Datenmodell,
Auth und Storage einziehen. Sonst teures Refactoring später.

### Zwei White-Label-Stufen
1. **Light (schnell):** Eigenes Logo + Farben + Subdomain, gemeinsame Infrastruktur.
2. **Full:** Custom Domain, eigene E-Mail-Domain, eigene Pakete/Preise, API-Zugang.

---

## 5. Querschnitt: Was alle Module brauchen

- **Auth & Accounts** (E-Mail + OAuth), Org-/Tenant-Konzept.
- **Zahlung:** Stripe — Abos (Self-Serve), Einmalzahlung (Done-for-you),
  Credits, Wholesale-Billing für Agenturen.
- **Credits-System:** Generierungen, Re-Rolls, Video-Renders kosten Credits.
- **Asset-Storage + CDN:** Uploads & Outputs (z. B. S3/R2 + CDN).
- **Job-/Queue-System:** AI-Generierung & Video-Rendering sind asynchron → Queue,
  Status-Updates, Webhooks.
- **Brand-Kit:** Logo, Farben, Schriften, Tonalität pro Marke (treibt AI-Konsistenz).
- **Amazon-Konformitäts-Validierung:** zentral, für Bild & Video.
