# AMZ Visuals (amzvisuals.ai)

Zentrales Produkt-, Spezifikations- und Übergabe-Repo für **amzvisuals.ai** — das
SaaS-Tool für hochkonvertierende Amazon-Visuals (Listing Images, A+ Content,
Brand Store, Brand Story) mit AI-Unterstützung.

> **Wichtig:** Dieses Repo enthält aktuell **die Spezifikation und Übergabe-Doku**,
> nicht den Anwendungscode. `JonasK01/sb1-oc1x2hve` ist nur ein **frühes UI-Mockup**.
> Das **live deployte Tool ist deutlich weiter** (Signup, Zahlung, Designer-Dashboard
> mit Versionierung, Visual Library, AI-Modul) — der Walkthrough vom 13.06. zeigt das.
> Nächster Schritt: Zugriff aufs **Live-Repo** sicherstellen.
> Details: [docs/01-bestandsaufnahme.md](docs/01-bestandsaufnahme.md) ·
> [docs/05-walkthrough-findings.md](docs/05-walkthrough-findings.md).

## Vision

amzvisuals.ai ist ein **Hybrid-Produkt**:

1. **Self-Serve AI** — Seller erstellen Listing-Bilder, Infografiken, A+-Module und
   Ad-Videos weitgehend selbst per AI im Tool (skaliert, margenstark).
2. **Done-for-you (Premium)** — Komplexe Aufträge (Brand Store, volle A+-Strecken)
   werden vom Team/Designer geliefert. AI nur als internes Beschleunigungs-Tool.
3. **White-Label für Agenturen** — Agenturen ohne eigenes Design bieten amzvisuals
   unter ihrer Marke ihren Kunden an (Reseller-/Wiederverkäufer-Kanal).

## Die drei aktuellen Prioritäten

| Priorität | Status heute | Doku |
|---|---|---|
| 1. AI Image Creation Tool finalisieren | Existiert im sichtbaren Code **nicht** | [Produkt-Spec §2](docs/02-produkt-spec.md#2-modul-ai-image-creation) |
| 2. Ad-Video-Modul | Existiert **nicht** | [Produkt-Spec §3](docs/02-produkt-spec.md#3-modul-ad-video) |
| 3. Agentur-/White-Label-Lösung | Existiert **nicht** | [Produkt-Spec §4](docs/02-produkt-spec.md#4-modul-white-label--agenturen) |

## Dokumente

1. **[Bestandsaufnahme](docs/01-bestandsaufnahme.md)** — Was wirklich gebaut ist
   (Code-Audit des Prototyps), was fehlt, ehrliche Lückenanalyse.
2. **[Produkt-Spec](docs/02-produkt-spec.md)** — Hybrid-Produkt + Detail-Spezifikation
   der drei Module, developer-ready.
3. **[Developer-Handoff](docs/03-developer-handoff.md)** — Tech-Stack, Architektur,
   Ticket-Backlog mit Reihenfolge & Aufwandsschätzung.
4. **[Go-to-Market](docs/04-go-to-market.md)** — Intern zuerst Umsatz, dann extern,
   ohne viel Ads. Agentur-White-Label-Kanal. Outbound über Close CRM.
5. **[Walkthrough-Findings](docs/05-walkthrough-findings.md)** — Developer-fertige
   Bug-/UX-/Feature-Liste aus Jonas' Loom-Walkthrough (13.06.) mit Timestamps:
   3 Blocker (Signup, Zahlung, AI), High-/Medium-Bugs, AI-Prompt-Anforderungen.
6. **[Visual UI Review](docs/06-ui-review.md)** — rein visuelle Funde aus den
   Video-Frames (Tippfehler „No Gas", Kontrast-Probleme, Chat-Widget überlappt CTAs,
   Status-Badge pro Bild). Backend = **Supabase**.

## Tech (Prototyp heute)

Vite · React 18 · TypeScript · Tailwind · Radix UI · lucide-react · gebaut in Bolt.
Markenfarbe `#f06524` (Orange), Schrift Mona Sans.
