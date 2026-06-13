# 05 · Walkthrough Findings (Loom, 2026-06-13)

> Quelle: Narrierter User-Walkthrough (Jonas) durch das **live deployte** Tool.
> Sprache des Originals: Englisch. Diese Doku ist developer-facing → Englisch,
> mit Timestamps `[mm:ss]` zur Rückverfolgung im Loom.

## ⚠️ Key insight — the live product is much further than the prototype

The audited repo `sb1-oc1x2hve` is an **early UI mockup**. The **live tool** that
Jonas walked through already has: signup/login, brand creation, product creation,
visual-order flow, **payment with discount codes**, a **designer dashboard with
file versioning**, a **visual library**, and an **AI image-generation module**.

So the three priorities are NOT greenfield — they are **fix + finish**:
- "Finalize AI image creation" = **fix a broken, already-built feature**.
- Ad-Video = the main genuinely *new* module (subscription, sold in-tool).
- White-Label = wanted **ASAP**, still to build.

> **Action for the developer:** this findings list is against the LIVE codebase
> (not `sb1-oc1x2hve`). Make sure we are all working off the live repo.

## Strategic framing (from intro)

- **Relaunch = soft launch.** Publish + write some things, but *not* a heavy
  marketing push. "Be honest with each other." → matches our no-heavy-ads GTM.
- **Internal adoption blocker (important):** *"design creation in ClickUp is
  easier than the tool"* — the designer has to do the work anyway and the ClickUp
  process already exists. ⇒ The tool must become **at least as fast/easy as
  ClickUp**, or internal scaling (Phase 1) stalls. Track this as a north-star UX goal.
- **Ad-Video** is currently out of scope → make it a buyable in-tool product on a
  **subscription model**.
- **White-Label labeling wanted ASAP** so other agencies can use it.
- **Website:** "fastest way to get Amazon visuals" angle is good. Polish: swap some
  logos in "see our work in action"; the "instant ordering / Amazon-specific AI"
  value props could be better visualized in the hero fields. [01:22–01:58]

---

## 🔴 Blockers (must fix for relaunch)

| # | Finding | TS |
|---|---|---|
| B1 | **Signup broken** — new user creation fails; no confirmation email arrives (not in spam either). "A lot of things have been downed." First user registration does not work. | 02:24–03:37 |
| B2 | **Payment does not complete** — UI shows "payment successful" but order stays **"payment pending"**; designer side confirms payment didn't go through. Even tested with a 100% discount code; "finish order" loads very long. | 13:00–15:14 |
| B3 | **AI image creation not working** — the AI generation ("AI topic") does not run at all. Core differentiator is down. | 23:30–24:39 |

---

## 🟠 High-priority bugs / workflow correctness

| # | Finding | TS |
|---|---|---|
| H1 | **State loss on navigation** — while setting up a product / visual order, switching to another browser tab (e.g. to copy a competitor ASIN) sometimes **kicks the user out / loses progress**. Need autosave of the product-service + order draft. | 11:32–12:19 |
| H2 | **Wrong status after "approve anyway"** — approving the whole project without reviewing each item sets status to **"in progress"**; it should be **"finalizing"**. | 17:36–18:01 |
| H3 | **Designer dashboard does not auto-update** — designer must reload to see new state. | 18:24–19:20 |
| H4 | **Approval-state confusion for designer** — when the user uses "approve anyway" (without per-image approval), the designer sees the project as **"approved"** even though items were *not* approved (user comments/changes exist). Designers may wrongly mark complete. Make the real review/approval state unambiguous to the designer, and surface user comments prominently. | 19:20–19:58 |
| H5 | **No completion notification** — when designer marks complete, the **client gets no in-app notification** and **no email**. Notification should also flip to **unread**. | 21:43–21:58 |

---

## 🟡 UX / copy improvements

| # | Finding | TS |
|---|---|---|
| U1 | Post-payment copy says **"few projects"** → should read "view project / view visual order". | 14:11 |
| U2 | **Order overview has too much copy**; hard to see the most important info. Simplify. | 15:56–16:13 |
| U3 | **"Pending review" shown on every image** → too noisy. Show it **once, next to the product name** (e.g. `Main V1 — Pending review`), not per image. Improve the status badge in front of the product. | 16:13–16:41 |
| U4 | After approving a single image, that image should clearly show **"Approved"**; the "approve" action/button should then disappear for it. | 17:15–17:36 |
| U5 | **"Review order" step feels unnecessary** — consider removing it (go straight to payment). | 12:39–12:55 |
| U6 | On a completed project the user "could not give feedback" → **remove anything labeled "feedback"**; replace with "Not happy with something? Feel free to reach out to us" + an email/contact. | 22:07–22:21 |
| U7 | **Download discoverability** — from a completed order it's hard to download. Add clear path/link: "To download, go to your **Visual Library**" (or link directly). | 22:21–22:38 |
| U8 | Brand form: add hint **"If a brand guide is uploaded, you don't need to fill out colors/fonts."** | 05:13–05:37 |

---

## 🟢 Feature requests / improvements

| # | Finding | TS |
|---|---|---|
| F1 | **Download whole product as one folder** — in Visual Library, downloading is per-image. Want a **product-level "download all" → single folder** (e.g. all Kachava listing images at once), not image-by-image. | 22:38–23:30 |
| F2 | **Ad-Video module (NEW)** — buyable in-tool, **subscription** model. (Out of scope today.) | 00:46–01:06 |
| F3 | **White-Label / agency labeling (NEW, ASAP)** — other agencies use the tool under their brand. | 01:06–01:22 |
| F4 | Website polish: better logos in "see our work in action"; better visualization of "instant ordering / Amazon-specific AI" value props. | 01:22–01:58 |

### Confirmed flows that work well (keep, don't break)
- "My Visual Orders" list — clean, liked. [04:02]
- Brand creation incl. logo upload, hex colors, Instagram link as brand reference. [04:33–06:40]
- Product creation: description via **paste OR file upload**, ASIN, dimensions, weight, USPs. [06:40–08:48]
- Visual-order setup: **competitor ASINs** (comma-separated, "compare me with the organic #1") + **inspiration ASIN** ("where you like the visual vibe") + **brand-colors vs product-colors** choice + optional image plan. [09:19–11:32] — strong, keep.
- Visual Library output quality "very final", good. [23:10–23:30]

---

## AI Image Module — status & prompt requirements [23:30–26:03]

**Status:** built but **not running** (B3). Once fixed, the generation flow is:
`product (optional) → generation type = Main Image → reference image = the product
photo (or an added asset) → generate` (example: "white background, chicken next to
the product").

**Prompt/agent requirements Jonas wants** (for Amazon main images that are
click-through-strong):
- Use the **filled-in product info** + the **uploaded image info** as context.
- Generate a **strong concept**, not just text-to-image: *composite* real product
  with relevant elements (e.g. product + a chicken/bird next to it).
- Auto-suggest an **important badge / hook** (e.g. "40% Protein", "Healthy muscle"),
  make the food look **more appetizing where it makes sense**.
- Keep the **real product intact** (product fidelity) — only build the scene around it.
- Rationale on Amazon-algorithm concern: connecting relevant elements on one image
  is fine and converts; the example main image (badges + chicken + bird + hi-res
  product) is the target quality. [25:11–26:03]

> Ties directly to Produkt-Spec §2 (product fidelity, text via overlays/templates,
> `ImageProvider` abstraction). The new addition here is an **AI "concept/prompt
> agent"** that turns product data into a strong main-image brief automatically.

---

## Open questions for Jonas / developer
1. **Confirm the live repo** and grant access — these findings are against the live
   tool, not `sb1-oc1x2hve`.
2. B1/B2/B3 root causes: are these env/deploy outages ("a lot of things have been
   downed") or real code bugs? Check logs/Stripe webhooks/AI-provider keys first.
3. Ad-Video subscription: pricing & which provider (see Produkt-Spec §3).
4. White-Label scope for first version: Light (logo+colors+subdomain) vs Full.
