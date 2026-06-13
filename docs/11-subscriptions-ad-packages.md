# 11 · Subscriptions — Ad Packages (monatlich, Stripe) — Developer-Brief

> **Super wichtig / High Prio.** Neues **Abo-Produkt** parallel zu den Einmal-Services.
> Beispiel-Tarif „Ad Premium Package": **5 Brand Ad Creatives + 3 Ad Videos / Monat**,
> monatlich kündbar. Muss **generisch für mehrere Tarife** gebaut werden.

## Entscheidungen (final, 13.06.2026)
- **Kontingent-Reset:** Use-it-or-lose-it — jeden Abrechnungszyklus frisch, **kein Rollover**.
- **Überverbrauch:** bei aufgebrauchtem Kontingent **sperren bis nächster Zyklus** (kein à-la-carte, kein Metered-Overage in v1).
- **Kündigung:** **zum Periodenende** (Zugang + Restkontingent bleiben bis Ende des bezahlten Monats).
- **Tarife:** **mehrere geplant** → datengetrieben bauen (Plan-Config mit Kontingenten), nicht auf ein Paket hartcodieren.

## Datenmodell (generisch, multi-tier, multi-tenant)
```
plans
  id, name, stripe_price_id, interval='month', active,
  quotas JSONB   -- z.B. {"ad_creative": 5, "ad_video": 3}

subscriptions
  id, org_id, plan_id, stripe_subscription_id,
  status (active|past_due|canceled),
  current_period_start, current_period_end, cancel_at_period_end

quota_usage            -- eine Zeile pro Kontingent pro Periode
  id, subscription_id, period_start, quota_key ('ad_creative'|'ad_video'),
  used_count, limit
```
- Alles an `org_id` gebunden (Multi-Tenancy, siehe ARCH1).
- Generierungen referenzieren, welches Kontingent sie verbraucht haben.

## Stripe-Setup
- Pro Tarif ein **Product** + **recurring monthly Price** (Annual optional später).
- **Checkout im Subscription-Mode** (Stripe Checkout) zum Abo-Start.
- **Stripe Customer Portal aktivieren** → Self-Service **Kündigung (zum Periodenende)**,
  Karte ändern, Rechnungen. → **fast kein Eigen-Dev** für Verwaltung/Kündigung.

### Webhooks (Pflicht, signaturgeprüft + idempotent)
| Event | Aktion |
|---|---|
| `checkout.session.completed` / `customer.subscription.created` | lokale Subscription anlegen, Kontingent für 1. Periode setzen |
| `invoice.paid` | **neue Periode → Kontingent-Reset** (frische `quota_usage`, used=0) ← der monatliche Reset |
| `customer.subscription.updated` | Status, `cancel_at_period_end`, Tarifwechsel (Up/Downgrade) |
| `customer.subscription.deleted` | als `canceled` markieren (nach Periodenende) |
| `invoice.payment_failed` | `past_due` setzen, Generierung sperren, Stripe-Dunning |

## Kontingent-Logik (Enforcement)
- Bei jeder **Ad-Creative- / Ad-Video-Generierung**: prüfen `used_count < limit` für den
  `quota_key` der aktuellen Periode.
  - OK → erlauben + `used_count` **atomar** hochzählen.
  - Aufgebraucht → **blockieren** mit Hinweis „Limit erreicht – neues Kontingent am {period_end}".
- **Reset** ausschließlich über `invoice.paid` (neue Periode). Kein Übertrag (use-it-or-lose-it).

## UI
- Neuer Bereich **„Plans / Subscription"** (getrennt vom Einmal-Order-Flow): Tarif-Karten
  (wie die bestehenden Service-Karten), CTA „Subscribe".
- **Aktives Abo** anzeigen: Tarifname, **Rest diesen Monat** (z. B. „Brand Ad Creatives: 3/5 · Ad Videos: 2/3"), „erneuert am {Datum}", **„Verwalten/Kündigen" → Customer-Portal-Link**.
- Bei aufgebraucht: Generieren deaktivieren + Reset-Datum zeigen (optional Upsell höherer Tarif).
- Bei `past_due`: Banner „Zahlung aktualisieren".

## Edge Cases
- **Up-/Downgrade mid-cycle:** Stripe regelt die Abrechnung (Proration); Kontingent-Änderung
  greift **ab nächster Periode** (v1, einfachste Variante).
- **Kündigung:** Zugang + Restkontingent bis Periodenende, danach sperren.
- **Failed payment / Chargeback:** `past_due` → sperren; Refund → Zugang entziehen.

## Synergien
- **Tolt** liest auch Abo-Rechnungen → **25% lifetime Provision gilt automatisch fürs Abo**.
- Dieses Abo ist die **Monetarisierung des Ad-Video-Moduls** (AV1).

## Von Jonas zu liefern (damit Stripe live kann)
- **Preis je Tarif** (mind. erster: Ad Premium Package = … $/Monat).
- **Tarif-Liste + Kontingente** (z. B. Basic / Pro / Agency mit jeweiligen 5+3-Werten).
- Annual-Option gewünscht? (kann später)
- Begriffsklärung: Ist „Brand Ad Creative" etwas **anderes** als die bestehenden
  „Listing Images"? (für `quota_key`-Mapping)
