---
name: new-shop-trichy-design-brief
description: Use this skill whenever Vengatesh is creating, planning, or reviewing a design (Meta ad creative, social post, poster, banner, or AI-generated image) or a Meta ads idea/hook for the client New Shop Trichy (a franchise outlet of the New Shop 24/7 convenience retail chain, https://newshop.in/, located at Ground Floor, 120, Bharathiar Salai, Melapudur, Cantonment, Tiruchirappalli, Tamil Nadu 620001). Trigger this for any new ad/design brief, when Vengatesh asks to "generate ad ideas" or "give me hooks" with or without a theme, when drafting Meta ad creative or copy, before starting design work, when self-checking a draft, when the client's request is vague, when asked about upcoming Trichy events or Tamil festivals worth running ads around, or when asked to sync/update the brand kit, Drive assets, or festival calendar. Covers Instagram/Facebook posts, Meta ad creatives (feed/reels/story), AI-generated product/lifestyle imagery, and print posters/banners for this specific outlet.
---

# New Shop Trichy — Design & Meta Ads Brief Assistant

Helps Vengatesh generate Meta ad ideas and hooks (with or without a given theme), produce on-brand AI-generated and real-photo creative, and time campaigns around Trichy-local events and Tamil festivals — for the New Shop franchise outlet at Bharathiar Salai, Cantonment, Tiruchirappalli.

**Read this section before doing anything else.**
- This is a **franchise** account, not an independent brand — it uses the **same logo and visual theme as the official/national New Shop brand** (confirmed by Vengatesh). There is no separate "Trichy look" to design. Localization happens in copy, imagery/setting, and campaign timing — not the logo, colors, or core identity. See `references/brand_guidelines.md` for what's still needed as actual files vs. what's already settled.
- Unlike other clients in this workspace, **AI-generated imagery is allowed and expected** here — but real photos (storefront, signage, staff) should be used wherever local trust/recognition matters. See `references/ai_image_guide.md` for the quality bar and when to prefer real photos.
- The core repeat workflow is **ad idea generation**: Vengatesh gives a theme, or asks for ideas with no theme and expects the skill to propose one from the Trichy/Tamil festival calendar. See "Ad idea generation workflow" below.
- Several inputs are still incomplete (brand kit, product mix, ad account access, competitor set). Where a brief depends on missing info, say so explicitly and use a clearly marked placeholder/assumption rather than guessing silently.
- Nothing in this skill auto-runs. Every generation, sync, or update happens only when asked in a message.

## Confirmed facts (don't re-ask for these)

- **Address:** Ground Floor, 120, Bharathiar Salai, Melapudur, Cantonment, Tiruchirappalli, Tamil Nadu 620001
- **Location anchors:** ~0.8 km from Tiruchirappalli Junction (Trichy Junction) railway station; ~0.5 km from the Central Bus Stand; Cantonment commercial belt; near Joseph Eye Hospital, KMC Speciality, and K.A.P. Viswanathan Govt. Medical College; near Nalli Silks. This is a **transit + commercial + healthcare** footfall profile — not college-belt or temple-pilgrim-adjacent (Srirangam/Rockfort are elsewhere in Trichy, not walking distance from this outlet).
- **Parent brand:** New Shop — India's franchised 24/7 convenience retail chain (newshop.in). Typical category mix across outlets: fresh food cafe, FMCG, stationery, tobacco, OTC medicines, and services like printing, ticket booking, ATM, courier — **but confirm which of these this specific outlet actually offers** before promoting any of them (see open items).
- **Languages:** Currently using **English captions for now** (Vengatesh's explicit call). Earlier direction was Tamil/Tanglish by default since the audience is Tamil-speaking Trichy locals — that reasoning still stands and this may revert; check with Vengatesh before assuming which is current if this file looks stale. No Chinese and no Taiwan-market conventions — this is a Trichy, Tamil Nadu (India) outlet.
- **Phone:** 91761 22210 (confirmed)
- **Instagram:** @newshoptrichy (confirmed)

## Open items — confirm before finalizing brand-locked or product-specific creative

1. ~~Official logo file~~ — **received**, saved at `assets/brand/new_shop_official_logo.png`. Use as-is; never redraw (see `references/brand_guidelines.md`). Exact hex codes and approved fonts still unconfirmed.
2. ~~Which product/service categories this outlet offers~~ — **confirmed**, summarized at `references/product_categories.md` (applies to Trichy too, per Vengatesh).
3. ~~Instagram/Facebook handle for this outlet~~ — **confirmed**: @newshoptrichy
4. Meta Business Manager / ad account access
5. Opening date (for launch campaign timing)
6. Nearby competitor stores near Bharathiar Salai/Cantonment
7. Ad approval workflow (does New Shop corporate need to sign off?)
8. Real photography of the actual storefront/signage

## Ad idea generation workflow

This is the primary everyday use of this skill.

**When Vengatesh gives a theme** (e.g., "Pongal offer," "monsoon coolers," "exam season"):
1. Pull the theme's context from `references/trichy_calendar.md` — dates, local relevance, what's realistic for this outlet's product mix.
2. Check `references/posted_content_registry.md` so hooks/angles aren't repeated.
3. Check `references/brand_guidelines.md` for locked-brand constraints.
4. Produce 3–5 **hook variants** covering different angles (urgency, price/offer, local-pride/local-landmark, convenience/transit-moment) — each with a short caption **in the current default language (see "Languages" above — English for now)** — plus a suggested visual direction (AI-generated vs. real photo, per `references/ai_image_guide.md`) and a recommended format (feed/reels/story) per `references/meta_ads_playbook.md`.
5. Log the chosen direction to `references/posted_content_registry.md` once Vengatesh picks one.

**When no theme is given:**
1. Scan `references/trichy_calendar.md` for the nearest upcoming festival/event/seasonal window, ranked by ad-worthiness for a convenience-store format.
2. Cross-check against `references/posted_content_registry.md` to avoid repeating a recently-used theme.
3. Propose 2–3 theme options with a one-line rationale each (why it fits this outlet's location/audience), then generate hooks for whichever Vengatesh picks — same 5 steps as above.

## Product spotlight workflow

Used when Vengatesh asks for a post about a specific product (named, or shown via photo), rather than a festival/theme post.

1. Confirm the product against `references/product_categories.md` — don't feature it if it's not confirmed stocked, and never feature smoking accessories (Stash Pro) in paid ad creative.
2. **Auto-generate the description** following `references/product_description_guide.md` — product name, category tag, a 2–3 sentence attractive description, and a short CTA line. Don't wait to be asked for this; it's a default part of every product spotlight.
3. Follow the mandatory design rules in `references/brand_guidelines.md` — black+yellow-only background, real logo untouched at the top — and give the description its own styled panel in the layout, not just a one-line caption (see design placement notes in `product_description_guide.md`).
4. If a real product photo is provided, composite it as-is (background cleanup like removing a white backdrop is fine; don't alter the product itself). If no photo is provided, either ask for one or offer an original illustration, per `references/ai_image_guide.md`.
5. Log it to `references/posted_content_registry.md` once finalized.

## How to use this skill for other tasks

1. **For any new creative**, read `references/brand_guidelines.md` first for locked vs. localizable elements.
2. **For what's actually stocked**, check `references/product_categories.md` before naming specific products in a hook — and never feature smoking accessories (Stash Pro) in paid ad creative.
3. **For product spotlight posts**, follow the dedicated workflow above and `references/product_description_guide.md`.
4. **For AI-generated visuals**, follow `references/ai_image_guide.md` — consistency, red-flags checklist (no garbled text-in-image, no inaccurate products), and when a real photo is mandatory instead.
5. **For Meta ad specs/format/targeting**, see `references/meta_ads_playbook.md`.
6. **For audience targeting**, see `references/audience_profile.md` — this outlet's segments are transit commuters, hospital visitors/staff, and the local Cantonment commercial crowd, not students or pilgrims.
7. **For festival/event timing**, see `references/trichy_calendar.md`.
8. **Before sending any brief**, check `references/checklists.md`.
9. **After a design/ad goes live or gets feedback**, log it to `references/posted_content_registry.md`.

## Updating this skill

- When the brand kit arrives, update `references/brand_guidelines.md` and remove it from "Open items" above.
- When product mix, handle, or ad account access is confirmed, update the relevant file and this list.
- Tamil festival dates shift yearly (lunar calendar) — `references/trichy_calendar.md` needs an annual date refresh; don't assume last year's dates carry over.
- Keep `references/posted_content_registry.md` current every time a theme/hook is actually used, so idea generation doesn't repeat itself.
