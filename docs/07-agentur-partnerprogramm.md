# 07 · Agentur-Partnerprogramm (Affiliate) — Lean-Ansatz

> Ergebnis der Entscheidung vom 13.06.2026. Ersetzt für den Start das schwere
> White-Label-Konzept durch ein **Affiliate-/Partnerprogramm** — gleicher Effekt
> (Agenturen bringen Kunden, verdienen mit), aber **minimaler Development-Aufwand**.

## Kernidee

Agenturen sind **Empfehlungs-/Provisionspartner**, kein White-Label-Mandant.

- Der **Endkunde registriert sich direkt auf amzvisuals.ai** → deine Marke, deine
  Daten, **deine direkte Kundenbeziehung** (wichtig für Upsells & Retention).
- Die **Agentur wird dem Kunden zugeordnet** und erhält **25% Provision** auf dessen
  Umsatz.
- Vorteil für die Agentur: Provision **+** bessere Amazon-Performance im Kundenaccount
  **+** glücklicherer Kunde — ohne selbst Design machen zu müssen.

> Bewusst **kein** klassisches White-Label (eigene Domain, Client-Login unter
> Agenturmarke, Wholesale-Billing) zum Start. Das kommt erst, wenn genug Agenturen
> es wirklich verlangen (siehe „Später / Full White-Label").

## Attribution (wie die Agentur dem Kunden zugeordnet wird)

Zwei Wege, beide schreiben `referred_by_agency`:

1. **Affiliate-Link (Hauptweg):** `amzvisuals.ai/?ref=AGENTURCODE`
   → `ref` wird in einem Cookie gespeichert → bei der Registrierung **automatisch
   vorausgewählt/zugeordnet**.
2. **Feld bei der Registrierung (Fallback):** „Von einer Agentur empfohlen?
   Agenturname/Code" — falls jemand ohne Link kommt.

## Provision

- **25% lifetime/wiederkehrend** auf **alle** Käufe des geworbenen Kunden
  (nicht nur Erstkauf). → dauerhafter Anreiz für die Agentur, den Kunden im Tool zu
  halten und zu pushen.
- Beispiel: Kunde kauft für 1.000 $ → 250 $ Provision an die Agentur.
- Gilt für **beide** Angebote: Self-Serve AI **und** Done-for-you.
- Auszahlung: monatlich, ab Mindestbetrag (z. B. 50 $).
- *(Alternative falls gewünscht: nur Erstkauf statt lifetime — einfache Umstellung.)*

## Technik (bewusst minimal)

**Der Low-Dev-Trick:** Da Stripe bereits genutzt wird, ein **fertiges Affiliate-Tool**
auf Stripe aufsetzen statt selbst zu bauen:
- Kandidaten: **Rewardful · Tolt · FirstPromoter** (alle Stripe-nativ).
- Liefern out-of-the-box: Tracking-Links, Cookie-Attribution, **Partner-Dashboards**,
  Provisions-Berechnung (recurring), **automatische Auszahlungen**, Terms.
- **Eigenentwicklung minimal:** nur das optionale „Agentur-Feld bei Signup" + das
  `ref`-Cookie-Capturing (oft schon vom Tool abgedeckt).

→ Unterschied: **Tage statt Wochen** Entwicklung.

## Zwei Agentur-Modi (beide unterstützt)

1. **Referral-Modus (Standard):** Kunde ist auf der Plattform, Agentur empfiehlt via
   Link, kassiert 25% Provision. *Primär — das willst du skalieren.*
2. **Agentur-managed (optional):** Agentur bestellt selbst im eigenen Account für ihre
   Kunden (legt Kunden als „Brands" an). Statt Provision: **25% Dauerrabatt**. Nutzt
   bestehende Strukturen, kein Sonderbau.

## Partner-Onboarding (Vertrieb, nicht Code)

- **`/partners`-Landingpage:** Nutzen („verdien 25% lifetime, ohne Design zu machen"),
  Funktionsweise, Bewerbungsformular → Link wird generiert.
- **Welcome-Kit** pro Agentur: kurzes Loom, 1-Seiten-Guide, **Sales-Deck/Vorher-Nachher-
  Assets** zum Zeigen beim Kunden, **fertige E-Mail-Templates** zum Weiterleiten.
- Ziel: Agentur kann **am selben Tag** anfangen zu vermitteln.

## Skalierung = Marketing + Vertrieb (über Close CRM)

Viele Agenturen kommen nicht von allein — eigener Recruiting-Funnel nötig:
- **Outbound über Close:** Zielliste „Amazon-/E-Com-Agenturen ohne Design-Team" →
  Sequenz „Biete deinen Kunden Top-Visuals an + verdien 25%, ohne Designer".
- Communities (Skool, LinkedIn, FB-Gruppen), Partner-of-Partner-Empfehlungen.
- Siehe [04-go-to-market.md](04-go-to-market.md) §4.

## Guardrails / To-decide
- Attributions-Fenster (z. B. 60–90 Tage Cookie) + **lifetime** Zuordnung nach Signup.
- Self-Referral verhindern (Agentur kauft nicht über eigenen Link für sich).
- Provisions-Terms / Partner-AGB (das Affiliate-Tool liefert Vorlagen).
- Klarheit: Provision auf Netto vor/nach Rabattcodes?

## Später / Full White-Label (nur wenn nachgefragt)
Eigene Subdomain + Branding, Client-Login unter Agenturmarke, Wholesale-Billing,
API. Erst bauen, wenn mehrere große Agenturen es konkret brauchen. Voraussetzung
dafür ist bereits in [03-developer-handoff.md](03-developer-handoff.md) eingeplant
(`org_id` von Tag 1).
