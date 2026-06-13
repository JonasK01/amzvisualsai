#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the AMZ Visuals relaunch backlog as an Excel workbook."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ORANGE = "F06524"
DARK = "221F1F"
HEADER_FILL = PatternFill("solid", fgColor=ORANGE)
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, color=DARK, size=16)
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")
CENTER = Alignment(horizontal="center", vertical="top")
thin = Side(style="thin", color="DDDDDD")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

PRIO_FILL = {
    "Blocker": PatternFill("solid", fgColor="E74C3C"),
    "Hoch":    PatternFill("solid", fgColor="E67E22"),
    "Mittel":  PatternFill("solid", fgColor="F1C40F"),
    "Niedrig": PatternFill("solid", fgColor="BDC3C7"),
}
PRIO_FONT = {
    "Blocker": Font(bold=True, color="FFFFFF"),
    "Hoch":    Font(bold=True, color="FFFFFF"),
    "Mittel":  Font(bold=True, color=DARK),
    "Niedrig": Font(bold=True, color=DARK),
}
TYP_FILL = {
    "Bug-Fix":   PatternFill("solid", fgColor="FADBD8"),
    "Anpassung": PatternFill("solid", fgColor="FDEBD0"),
    "Neu":       PatternFill("solid", fgColor="D6EAF8"),
}

wb = Workbook()

# ----------------------------------------------------------------------------
# Sheet 1: Aufgabenliste
# ----------------------------------------------------------------------------
ws = wb.active
ws.title = "Aufgabenliste"

headers = ["ID", "Kategorie", "Typ", "Priorität", "Titel", "Beschreibung",
           "Quelle (Zeit/Frame)", "Aufwand", "Verantwortlich", "Status"]

# ID, Kategorie, Typ, Priorität, Titel, Beschreibung, Quelle
rows = [
    # --- BLOCKER ---
    ("B1", "Onboarding", "Bug-Fix", "Blocker", "Registrierung kaputt / keine Bestätigungsmail",
     "Neue User können sich nicht registrieren; es kommt keine Bestätigungsmail (auch nicht im Spam). Erstregistrierung schlägt fehl. Zuerst Supabase Auth/E-Mail-Provider/Webhooks prüfen.",
     "02:24–03:37"),
    ("B2", "Zahlung", "Bug-Fix", "Blocker", "Zahlung schließt nicht ab (bleibt 'pending')",
     "UI zeigt 'payment successful', Order bleibt aber 'payment pending'; Designer-Seite bestätigt, dass keine Zahlung ankam. Auch mit 100%-Rabattcode. 'Finish order' lädt sehr lange. Stripe-Webhook/Supabase prüfen.",
     "13:00–15:14"),
    ("B3", "AI Modul", "Bug-Fix", "Blocker", "AI-Bildgenerierung läuft nicht",
     "Das AI-Generierungs-Modul ('AI Visuals') startet gar nicht. Kernfeature ist down.",
     "23:30"),
    # --- HOCH ---
    ("H1", "Order-Flow", "Bug-Fix", "Hoch", "State-Verlust beim Tab-Wechsel",
     "Beim Anlegen von Produkt/Visual-Order führt das Wechseln zu einem anderen Browser-Tab (z.B. um Wettbewerber-ASIN zu kopieren) teils zum Rauswerfen / Datenverlust. Autosave des Produkt- und Order-Drafts nötig.",
     "11:32–12:19"),
    ("H2", "Order-Status", "Bug-Fix", "Hoch", "Falscher Status 'in progress' statt 'finalizing'",
     "Nach 'approve anyway' (Projekt ohne Einzelreview freigeben) springt der Status auf 'in progress'; korrekt wäre 'finalizing'.",
     "17:36–18:01"),
    ("H3", "Designer", "Bug-Fix", "Hoch", "Designer-Dashboard aktualisiert nicht automatisch",
     "Der Designer muss neu laden, um neue Zustände zu sehen. Live-/Auto-Update fehlt.",
     "18:24–19:20"),
    ("H4", "Designer", "Anpassung", "Hoch", "Approval-Status für Designer missverständlich",
     "Bei 'approve anyway' (ohne Einzel-Approval) sieht der Designer das Projekt als 'approved', obwohl Items nicht freigegeben sind und User-Kommentare/Änderungen existieren. Echten Review-Status eindeutig machen und User-Kommentare prominent zeigen.",
     "19:20–19:58"),
    ("H5", "Benachrichtigung", "Neu", "Hoch", "Keine Completion-Notification / E-Mail",
     "Wenn der Designer 'complete' markiert, bekommt der Client keine In-App-Notification und keine E-Mail. Notification soll zudem auf 'ungelesen' springen.",
     "21:43–21:58"),
    ("A2", "AI Modul", "Neu", "Hoch", "AI Prompt-Agent für Main Image",
     "Aus Produktdaten + hochgeladenem Bild automatisch ein starkes Main-Image-Konzept erzeugen: relevantes Element kombinieren (z.B. Produkt + Huhn), passenden Badge/Hook vorschlagen (z.B. '40% Protein'), Essen appetitlicher wirken lassen, Produkt originalgetreu erhalten. Ziel: klickstarke Amazon-Main-Images.",
     "24:39–26:03"),
    # --- MITTEL ---
    ("U1", "Copy", "Anpassung", "Mittel", "Text 'few projects' korrigieren",
     "Nach der Zahlung steht 'few projects' → sollte 'View project' / 'View visual order' heißen.",
     "14:11"),
    ("U2", "Review-UI", "Anpassung", "Mittel", "Order-Übersicht hat zu viel Copy",
     "In der Order-/Visual-Übersicht ist zu viel Text; das Wichtigste ist schwer erkennbar. Vereinfachen, Hierarchie schärfen.",
     "15:56–16:13"),
    ("U3", "Review-UI", "Anpassung", "Mittel", "'Pending review' nicht pro Bild",
     "'Pending review' wird auf jedem Bild angezeigt (zu unruhig). Stattdessen einmal pro Produkt neben dem Produktnamen anzeigen (z.B. 'Main V1 – Pending review'). Status-Badge vor dem Produkt verbessern.",
     "16:13–16:41"),
    ("U4", "Review-UI", "Anpassung", "Mittel", "Einzelbild zeigt 'Approved'",
     "Nach Freigabe eines Einzelbilds soll dieses klar 'Approved' anzeigen; der 'Approve'-Button verschwindet dann dafür.",
     "17:15–17:36"),
    ("U5", "Order-Flow", "Anpassung", "Mittel", "'Review order'-Schritt entfernen",
     "Der separate 'Review order'-Schritt wirkt überflüssig – erwägen, direkt zur Zahlung zu gehen.",
     "12:39–12:55"),
    ("U6", "Review-UI", "Anpassung", "Mittel", "'Feedback'-Wording für Client entfernen",
     "Bei fertigem Projekt 'konnte kein Feedback geben'. Alles mit 'Feedback' für den Client entfernen; stattdessen 'Nicht zufrieden? Melde dich bei uns' + Kontakt-E-Mail.",
     "22:07–22:21"),
    ("U7", "Download", "Anpassung", "Mittel", "Download-Auffindbarkeit verbessern",
     "Aus der fertigen Order ist der Download schwer zu finden. Klaren Hinweis/Link ergänzen: 'Zum Download in die Visual Library' (oder direkt verlinken).",
     "22:21–22:38"),
    ("F1", "Download", "Neu", "Mittel", "Ganzes Produkt als ein Ordner downloaden",
     "In der Visual Library ist der Download pro Bild. Gewünscht: Download auf Produktebene ('Alle herunterladen') als ein Ordner (z.B. alle Kachava Listing Images), nicht Bild für Bild.",
     "22:38–23:30"),
    ("V2", "UI/Design", "Anpassung", "Mittel", "Text-Kontrast global zu niedrig",
     "Info-Banner ('Keep your profile current', 'Product Information'), Hilfetexte und Platzhalter sind hellgrau auf hell; Landing-Subheadline (Orange auf hell) und CVR-Zeilen kaum lesbar. Kontrast auf WCAG AA anheben.",
     "Frames f1,f7,f9,f19,f46"),
    ("V3", "UI/Design", "Bug-Fix", "Mittel", "Chat-Widget überlappt CTAs/Modals",
     "'Got any questions?'-Chat unten rechts liegt über Primär-CTA (z.B. 'Create Brand') und über dem Upload-Modal → verdeckt Klicks. Position/Z-Index anpassen.",
     "Frames f7,f9,f52"),
    ("V4", "Stabilität", "Bug-Fix", "Mittel", "Leere/kaputte Render-States",
     "Mehrere komplett leere App-Screens (Supabase-URLs sichtbar) während des Flows → Render-/Lade-Fehlerzustände abfangen (Loading-/Error-States). Hängt mit B1/B2/B3 zusammen.",
     "Frames f3,f13,f50,f54"),
    # --- NIEDRIG ---
    ("U8", "Brand-Form", "Anpassung", "Niedrig", "Hinweis: Brand Guide ersetzt Farben/Fonts",
     "Im Brand-Formular Hinweis ergänzen: 'Wenn ein Brand Guide hochgeladen ist, müssen Farben/Schriften nicht ausgefüllt werden.'",
     "05:13–05:37"),
    ("V1", "Copy", "Bug-Fix", "Niedrig", "Tippfehler 'No Gas' → 'No-Gos'",
     "Im Brand-Formular steht 'No Gas'; korrekt: 'No-Gos'.",
     "Frame f9"),
    ("F4", "Website", "Anpassung", "Niedrig", "Landing-Page Politur",
     "Bessere Logos in 'See Our Work in Action'; Value-Props 'Instant Ordering / Amazon-specific AI' besser visualisieren.",
     "01:22–01:58"),
    # --- PARTNERPROGRAMM (Affiliate, lean) ---
    ("P1", "Partnerprogramm", "Neu", "Hoch", "Affiliate-Tool an Stripe anbinden (Tolt)",
     "Empfehlung TOLT (statt Rewardful): auto Auszahlungen via Wise/Payoneer/PayPal, flat ab 49$/Mo, keine Payout-Gebühren, ~15 Min Setup. Liest echte Stripe-Charges -> lifetime 25% auf tatsächlich gezahlten Betrag automatisch. Liefert Tracking-Links, Cookie-Attribution, Partner-Dashboards, Auszahlungen.",
     "Entscheidung 13.06."),
    ("P2", "Partnerprogramm", "Neu", "Hoch", "Agentur-Attribution bei Registrierung",
     "?ref=CODE aus Affiliate-Link in Cookie speichern und User zuordnen; zusätzlich optionales Feld bei Signup 'Von einer Agentur empfohlen? (Name/Code)'. Beides schreibt referred_by_agency.",
     "Entscheidung 13.06."),
    ("P3", "Partnerprogramm", "Neu", "Mittel", "Partner-Dashboard (lean)",
     "Read-only-Ansicht für Agenturen: geworbene Kunden, Umsatz, verdiente Provision, Auszahlungsstatus. V1 ggf. direkt aus dem Affiliate-Tool, später nativ.",
     "Entscheidung 13.06."),
    ("P4", "Partnerprogramm", "Neu", "Mittel", "Partner-Landingpage + Bewerbung",
     "Seite /partners: Nutzen (25% lifetime, ohne Design), Funktionsweise, Bewerbungsformular -> Affiliate-Link wird generiert.",
     "Entscheidung 13.06."),
    ("P5", "Partnerprogramm", "Neu", "Niedrig", "Partner-Welcome-Kit",
     "Onboarding-Material: kurzes Loom, 1-Seiten-Guide, Sales-Deck/Vorher-Nachher-Assets, fertige E-Mail-Templates zum Weiterleiten an Kunden. Kein Code.",
     "Entscheidung 13.06."),
    ("P6", "Partnerprogramm", "Neu", "Mittel", "Agentur-managed Modus (optional)",
     "Für Agenturen, die selbst im eigenen Account für Kunden bestellen: 25% als Dauerrabatt statt Provision; Kunden als Brands. Nutzt bestehende Strukturen.",
     "Entscheidung 13.06."),
    # --- SUBSCRIPTIONS (Ad-Pakete, monatlich) ---
    ("S1", "Subscriptions", "Neu", "Hoch", "Stripe-Abo + Customer Portal",
     "Monatliche Abos parallel zu Einmal-Services (z.B. Ad Premium Package = 5 Brand Ad Creatives + 3 Ad Videos/Monat). Stripe Product + recurring Price, Checkout im Subscription-Mode. Customer Portal aktivieren für Self-Service-Kündigung (zum Periodenende), Kartenwechsel, Rechnungen.",
     "Entscheidung 13.06."),
    ("S2", "Subscriptions", "Neu", "Hoch", "Generisches Plan-/Kontingent-Modell",
     "Datengetriebene Tarife mit Monats-Kontingenten (quotas JSON, z.B. {ad_creative:5, ad_video:3}); subscriptions + quota_usage je Periode, an org_id gebunden. Generisch bauen (mehrere Tarife geplant), nicht hartcodiert.",
     "Entscheidung 13.06."),
    ("S3", "Subscriptions", "Neu", "Hoch", "Subscription-Webhooks",
     "checkout.session.completed/subscription.created (anlegen), invoice.paid (KONTINGENT-RESET = neue Periode), subscription.updated (Status/cancel_at_period_end/Tarifwechsel), subscription.deleted, invoice.payment_failed (past_due + sperren). Signaturen prüfen, idempotent.",
     "Entscheidung 13.06."),
    ("S4", "Subscriptions", "Neu", "Hoch", "Kontingent-Enforcement (use-it-or-lose-it)",
     "Bei jeder Ad-Creative/Ad-Video-Generierung: used_count < limit -> erlauben + atomar hochzählen, sonst SPERREN mit Reset-Datum. Kein Rollover, kein Overage (sperren bis nächster Zyklus).",
     "Entscheidung 13.06."),
    ("S5", "Subscriptions", "Neu", "Mittel", "Plans-UI + Verbrauchsanzeige",
     "Bereich Plans/Subscription (Tarif-Karten), Subscribe-CTA. Aktives Abo mit Rest diesen Monat (z.B. 'Creatives 3/5, Videos 2/3'), Erneuerungsdatum, Verwalten/Kündigen -> Customer Portal. Bei aufgebraucht generieren sperren + Reset-Datum; past_due-Banner.",
     "Entscheidung 13.06."),
    ("S6", "Subscriptions", "Neu", "Niedrig", "Up-/Downgrade-Handling",
     "Tarifwechsel mid-cycle: Stripe regelt Abrechnung (Proration); Kontingent-Änderung ab nächster Periode (v1). Später verfeinern.",
     "Entscheidung 13.06."),
]

# Title row
ws.merge_cells("A1:J1")
ws["A1"] = "AMZ Visuals – Relaunch Backlog (Bugs / Anpassungen / Neu)"
ws["A1"].font = TITLE_FONT
ws["A1"].alignment = Alignment(vertical="center")
ws.row_dimensions[1].height = 26
ws.merge_cells("A2:J2")
ws["A2"] = "Quelle: Loom-Walkthrough + Visual UI Review (13.06.2026). Spalten Aufwand/Verantwortlich/Status zum Selbst-Befüllen."
ws["A2"].font = Font(italic=True, color="555555", size=9)

# Header
hr = 3
for c, h in enumerate(headers, start=1):
    cell = ws.cell(row=hr, column=c, value=h)
    cell.fill = HEADER_FILL
    cell.font = HEADER_FONT
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = BORDER
ws.row_dimensions[hr].height = 24

# Data
r = hr + 1
for (rid, kat, typ, prio, titel, besch, quelle) in rows:
    ws.cell(row=r, column=1, value=rid).alignment = CENTER
    ws.cell(row=r, column=2, value=kat).alignment = TOP
    tcell = ws.cell(row=r, column=3, value=typ); tcell.alignment = CENTER
    if typ in TYP_FILL: tcell.fill = TYP_FILL[typ]
    pcell = ws.cell(row=r, column=4, value=prio); pcell.alignment = CENTER
    pcell.fill = PRIO_FILL[prio]; pcell.font = PRIO_FONT[prio]
    ws.cell(row=r, column=5, value=titel).alignment = WRAP
    ws.cell(row=r, column=5).font = Font(bold=True, color=DARK)
    ws.cell(row=r, column=6, value=besch).alignment = WRAP
    ws.cell(row=r, column=7, value=quelle).alignment = WRAP
    ws.cell(row=r, column=8, value="").alignment = TOP            # Aufwand
    ws.cell(row=r, column=9, value="").alignment = TOP            # Verantwortlich
    ws.cell(row=r, column=10, value="Offen").alignment = CENTER   # Status
    for c in range(1, 11):
        ws.cell(row=r, column=c).border = BORDER
    r += 1

widths = [6, 16, 12, 11, 30, 55, 20, 10, 16, 10]
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = "A4"
ws.auto_filter.ref = f"A{hr}:J{r-1}"

# ----------------------------------------------------------------------------
# Sheet 2: Module & Roadmap
# ----------------------------------------------------------------------------
ws2 = wb.create_sheet("Module & Roadmap")
mheaders = ["Modul / Initiative", "Status heute", "Umfang (Scope)", "Phase", "Priorität"]
modules = [
    ("AI Image Creation (reparieren + finalisieren)",
     "Existiert, aber KAPUTT (läuft nicht)",
     "1) Generierung wieder lauffähig machen (B3). 2) Flow: Produkt → Typ 'Main Image' → Referenzbild → Generieren. 3) Prompt-Agent (A2): Produktdaten→starkes Konzept+Badge. 4) Produkttreue (Produkt aus Foto erhalten). 5) Text via Overlays/Templates, nicht AI. 6) Amazon-Konformität als Guardrail.",
     "Phase 2 (parallel zu Fixes)", "Hoch"),
    ("Ad-Video-Modul",
     "Existiert NICHT (neu)",
     "Im Tool kaufbar als Abo. Stufe 1: Template-/Motion-basiert (Bilder+Animation+Text+Musik, z.B. Remotion) mit Amazon-/Social-Export-Presets. Stufe 2: generatives AI-Video (Kling/Runway/Veo) als Premium. Abrechnung via Credits/Subscription.",
     "Phase 2–3", "Hoch (strategisch)"),
    ("Agentur-PARTNERPROGRAMM (Affiliate) – LEAN",
     "Neu – LEAN-Weg statt White-Label (Entscheidung 13.06.)",
     "Agenturen = Provisionspartner (25% lifetime). Kunde registriert sich direkt auf amzvisuals.ai, Zuordnung via Affiliate-Link (?ref=) + Signup-Feld. Fertiges Affiliate-Tool auf Stripe (Rewardful/Tolt/FirstPromoter) = minimal Dev. Beide Angebote (Self-Serve + Done-for-you) inkludiert. Details: docs/07.",
     "Phase 1–2", "Hoch (strategisch)"),
    ("Full White-Label (später, nur bei Nachfrage)",
     "Existiert NICHT – aufgeschoben",
     "Eigene Subdomain + Branding, Client-Login unter Agenturmarke, Wholesale-Billing, API. Erst bauen, wenn mehrere große Agenturen es konkret brauchen. Voraussetzung org_id ab Tag 1 ist eingeplant.",
     "Phase 3+ (später)", "Niedrig"),
    ("Done-for-you Flow (bestehend) marktreif machen",
     "Größtenteils gebaut, mit Blocker-Bugs",
     "Blocker B1/B2 fixen (Signup+Zahlung), Order→Backend stabil, Liefer-/Review-Schleife, Notifications/E-Mail (H5). Schnellster Weg zu erstem Umsatz.",
     "Phase 1 (zuerst)", "Blocker"),
]
ws2.merge_cells("A1:E1")
ws2["A1"] = "Module & Roadmap"
ws2["A1"].font = TITLE_FONT
ws2.row_dimensions[1].height = 26
for c, h in enumerate(mheaders, start=1):
    cell = ws2.cell(row=2, column=c, value=h)
    cell.fill = HEADER_FILL; cell.font = HEADER_FONT
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = BORDER
ws2.row_dimensions[2].height = 24
rr = 3
for (name, status, scope, phase, prio) in modules:
    ws2.cell(row=rr, column=1, value=name).alignment = WRAP
    ws2.cell(row=rr, column=1).font = Font(bold=True, color=DARK)
    ws2.cell(row=rr, column=2, value=status).alignment = WRAP
    ws2.cell(row=rr, column=3, value=scope).alignment = WRAP
    ws2.cell(row=rr, column=4, value=phase).alignment = WRAP
    pc = ws2.cell(row=rr, column=5, value=prio); pc.alignment = CENTER
    base = prio.split()[0]
    if base in PRIO_FILL: pc.fill = PRIO_FILL[base]; pc.font = PRIO_FONT[base]
    for c in range(1, 6):
        ws2.cell(row=rr, column=c).border = BORDER
    rr += 1
for i, w in enumerate([34, 30, 70, 22, 16], start=1):
    ws2.column_dimensions[get_column_letter(i)].width = w
ws2.freeze_panes = "A3"

# ----------------------------------------------------------------------------
# Sheet 3: Kontext / Hinweise
# ----------------------------------------------------------------------------
ws3 = wb.create_sheet("Kontext & Hinweise")
notes = [
    ("Wichtigster Befund", "Das LIVE-Tool ist viel weiter als der alte Prototyp (sb1-oc1x2hve). Signup, Zahlung, Designer-Dashboard mit Versionierung, Visual Library und AI-Modul existieren bereits. Die 3 Prioritäten = FIX + FINISH, kein Greenfield."),
    ("Tech-Stack (live)", "Backend = Supabase (*.supabase.co-URLs in den Frames sichtbar). Eigene /designer-Route. Bei B1/B2 zuerst Supabase Auth/RLS/Webhooks/Keys prüfen."),
    ("Interner Adoptions-Hebel", "Jonas: 'Design-Erstellung in ClickUp ist aktuell einfacher als im Tool.' → Das Tool muss mind. so schnell/einfach wie ClickUp werden, sonst nutzt es intern niemand. North-Star-UX-Ziel."),
    ("Relaunch", "Soft-Launch: veröffentlichen, aber kein großer Marketing-Push. Ehrlich bleiben."),
    ("Agentur-Modell (Entscheidung 13.06.)", "Affiliate-/Partnerprogramm statt White-Label: Kunde direkt auf amzvisuals.ai, Agentur per Affiliate-Link (?ref=) + Signup-Feld zugeordnet, 25% lifetime Provision auf alle Käufe. Fertiges Affiliate-Tool auf Stripe (Rewardful/Tolt/FirstPromoter) = minimal Dev. Skalierung braucht Marketing+Vertrieb (Close-Outbound an Agenturen). Details: docs/07."),
    ("Multi-Tenancy", "org_id/tenant_id von Tag 1 in Datenmodell, Auth & Storage – auch wenn Full White-Label erst später. Nachrüsten ist teuer."),
    ("AI-Provider-Abstraktion", "Bild-/Video-Modelle hinter Interfaces (ImageProvider/VideoProvider) kapseln – Modelle ändern sich monatlich."),
    ("Gut – behalten", "A+-Output-Qualität ('All the Quality, None of the Compromise'), Vorher-Nachher-Slider auf der Landing, Wettbewerber-ASIN + Inspiration-ASIN-Eingabe, Brand-/Produkt-Formulare."),
    ("Methode/Grenzen", "Findings aus Loom-Transcript + 60 Video-Frames (1 fps, niedrige Qualität). Manche Klein-Texte unscharf; für exakte Kontrastwerte/feine Copy wären hochauflösende Screenshots besser."),
    ("Vollständige Doku", "Repo JonasK01/amzvisualsai, Branch claude/hopeful-gauss-41dvp7: docs/01–06 (Bestandsaufnahme, Produkt-Spec, Handoff, Go-to-Market, Walkthrough-Findings, UI-Review)."),
]
ws3.merge_cells("A1:B1")
ws3["A1"] = "Kontext & Hinweise"
ws3["A1"].font = TITLE_FONT
ws3.row_dimensions[1].height = 26
for c, h in enumerate(["Thema", "Hinweis"], start=1):
    cell = ws3.cell(row=2, column=c, value=h)
    cell.fill = HEADER_FILL; cell.font = HEADER_FONT
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = BORDER
rr = 3
for (thema, hinweis) in notes:
    ws3.cell(row=rr, column=1, value=thema).alignment = WRAP
    ws3.cell(row=rr, column=1).font = Font(bold=True, color=DARK)
    ws3.cell(row=rr, column=2, value=hinweis).alignment = WRAP
    for c in range(1, 3):
        ws3.cell(row=rr, column=c).border = BORDER
    rr += 1
ws3.column_dimensions["A"].width = 26
ws3.column_dimensions["B"].width = 95
ws3.freeze_panes = "A3"

out = "/home/user/amzvisualsai/AMZVisuals_Relaunch_Backlog.xlsx"
wb.save(out)
print("Saved:", out)
print("Aufgaben:", len(rows), "| Module:", len(modules), "| Hinweise:", len(notes))
