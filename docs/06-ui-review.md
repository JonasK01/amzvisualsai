# 06 · Visual UI Review (from Loom frames, 2026-06-13)

> Basis: 60 distinkte Frames aus dem (komprimierten) Loom-Video, mit ffmpeg
> extrahiert und einzeln gesichtet. Hier stehen Dinge, die man **sehen** muss —
> ergänzend zu [05-walkthrough-findings.md](05-walkthrough-findings.md) (gesprochene Punkte).
> Qualität der Quelle: niedrig (29 MB, 1 fps) → Detailtexte teils unscharf.
> `NEU` = rein visueller Fund, nicht im Transcript. `BESTÄTIGT` = stützt einen 05-Punkt.

## Tech-Beobachtungen (für Developer)
- **Backend = Supabase.** Auf den kaputten/leeren Ladescreens sind `*.supabase.co`-
  URLs sichtbar (f50, f54). Mehrere Blocker-States (Signup/Payment) hingen auf
  Supabase-Requests → bei B1/B2 zuerst **Supabase-Calls / RLS / Auth / Webhooks**
  prüfen.
- **Eigene `/designer`-Route** existiert (Upload-New-Version-Modal, f52).
- App-Navigation: `Visuals · Brands · Products · Visual Library · Account · AI Visuals`.

## 🔎 Rein visuelle Funde (NEU)

| # | Fund | Frame |
|---|---|---|
| V1 `NEU` | **Tippfehler: „No Gas"** im Brand-Formular — soll **„No-Gos"** heißen. | f9 |
| V2 `NEU` | **Durchgehend zu kontrastarme Texte.** Info-Banner („Keep your profile current", „Product Information"), Feld-Hilfetexte und Platzhalter sind hellgrau auf hell → schwer lesbar. Auch auf der Landing: Subheadline (Orange auf Hell) und die beiden Benefit-/CVR-Zeilen unter dem Vorher-Nachher sind kaum lesbar. Kontrast erhöhen (WCAG AA). | f1, f7, f9, f19, f46 |
| V3 `NEU` | **Support-Chat-Widget überlappt Aktionen.** „Got any questions? I'm happy to help" liegt unten rechts über dem Primär-CTA-Bereich (z. B. „Create Brand") und über dem Upload-Modal → kann Klicks verdecken. Position/Z-Index prüfen. | f7, f9, f52 |
| V4 `NEU` | **Viele komplett leere Screens** während des Flows — teils externe Seiten, aber f50/f54 (Supabase) sowie Signup/Payment sind unsere App, die nicht rendert. Stützt die Instabilität („a lot of things have been downed"). | f3, f13, f50, f54 |

## ✅ Visuell BESTÄTIGT (stützt 05)

| # | Fund | 05-Bezug | Frame |
|---|---|---|---|
| V5 | **Status-Badges auf JEDEM Modul** (orange Balken pro Item) im Review-Screen → genau das „pending review überall, zu unruhig". | U3 | f43, f46 |
| V6 | **„Feedback (Comment)"-Label** im Review-/Kommentar-Panel (mit grünem Approve / rotem Request-Changes) → „Feedback"-Wording für Client entfernen. | U6 | f43, f46 |
| V7 | **Review-Modal wirkt voll/gedrängt** (Bildvorschau links, Modul-Status + Kommentare + Feedback-Feld rechts) → „zu viel Copy, Wichtiges schwer erkennbar". | U2 | f43, f46 |
| V8 | **Viele offene Browser-Tabs**, ständiges Wechseln Google/Amazon/Shop → stützt „State-Verlust beim Tab-Wechsel". | H1 | f18, f52, f56 |

## 👍 Visuell stark — behalten, nicht kaputt machen
- **Landing „See Our Work in Action"**: Vorher-Nachher-Slider (Tantra Massage Oil) mit
  Tab-Kategorien (Main Images / Listing / A+ Premium / Brand Story / Brand Store) — überzeugend. (f1)
- **A+-Output-Qualität** („All the Quality, None of the Compromise" mit sauberer
  Icon-Reihe: Non-GMO, Vegan, No Soy …) — echtes Verkaufsargument. (f46)
- **Designer „Upload New Version"-Modal**: klar (Desktop File *Required* / Mobile *Optional*). (f52)
- **Brand-/Produkt-Formulare**: saubere 2-Spalten-Struktur, Pflichtfeld-Sternchen vorhanden. (f7, f19)
- **Ziel-/Referenzbild** (Huhn + Igel + Meise, „40% Protein", „MADE IN EU") zeigt die
  angestrebte Main-Image-Qualität für das AI-Modul. (f31, f60)

## Konkrete Quick-Win-Liste (klein, hohe Wirkung)
1. „No Gas" → „No-Gos" fixen. (V1)
2. Globalen Text-/Banner-Kontrast anheben. (V2)
3. Chat-Widget-Position so, dass es CTAs/Modals nicht überlappt. (V3)
4. Im Review-Screen: Status-Badge **einmal pro Produkt** statt pro Bild; „Feedback"
   → „Brauchst du etwas? Melde dich bei uns". (V5–V7)

## Hinweis zur Methode / Grenzen
Niedrige Quellqualität + 1 fps: einige kleine Texte sind unscharf, und reine
Bewegungs-/Timing-Glitches (Animationen, Ladespinner-Dauer) sind in Einzelframes
nicht voll beurteilbar. Für Layout, Hierarchie, Kontrast, Copy und State-Probleme
reicht es aber gut. Höher aufgelöste Screenshots einzelner Screens würden V2 (Kontrast-
Werte) und unscharfe Detail-Copy noch genauer machen.
