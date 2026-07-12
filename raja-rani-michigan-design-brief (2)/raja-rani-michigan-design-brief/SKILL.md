---
name: raja-rani-michigan-design-brief
description: Use this skill whenever creating, planning, or reviewing a promotional poster, banner, or social media design for the client Raja Rani Michigan (Raja Rani Indian Restaurant, Canton, MI — Instagram/Facebook handle raja_rani_indian_restaurant, website rajaranimichigan.com). Trigger this for any new poster request (weekly Weekend Special posters, single-dish spotlights, combo/bundle offers, festival or seasonal posters like Diwali/Mother's Day/Banana Leaf Feast/Valentine's Day, recurring weekly promos like Chat Night or Dosa Night, loyalty/gift-card/press posters), before starting design work, when the client's request is vague, when self-checking a draft before sending it, or when asked to sync/refresh the reference posters or menu from Google Drive. Covers brand guidelines (black-and-yellow premium theme, logo placement, footer requirements), menu sourcing, and past-poster reference lookup.
---

# Raja Rani Michigan Poster Design Assistant

Helps produce on-brand promotional posters for Raja Rani Indian Restaurant (Canton, MI), grounded in the client's actual menu data and the real posters the designer has already made — not generic restaurant-poster guesswork.

**What this skill is:** a brand/menu reference profile plus a repeatable poster-generation process. It is not a template generator with fixed slots — every poster should be freshly composed to fit the week's dishes or occasion while following the same hard brand rules every time.

**What this skill can produce:** actual rendered poster **image files** (`.jpg`/`.png`) built from real menu data, the client's real logo/badge assets, and the documented visual language — or a text design brief a human designer can build from.

**Two things it cannot do (be upfront about these):** it has **no AI image generator**, and it **cannot download food photos from the open web** (network egress is limited to package repos). Real dish photos must come from the user, from an approved poster in Drive (background-removed into a cutout), or from the client's site. If a dish has no usable photo, ask for one.

**Deliver image files, never HTML** — the client has explicitly asked not to receive HTML designs.

## How to use this skill

1. **Read `references/client_profile.md` first, always** — hard brand rules (logo, black-and-gold palette, footer, Halal badge, CTA) and the soft stylistic patterns for each poster type.
2. **Identify the poster type** from the request: Weekend Special menu board, single hero-dish spotlight, combo/bundle offer, festival/seasonal/event poster, recurring weekly promo, or loyalty/trust poster. `references/drive_asset_inventory.md` catalogs real past examples of each type by filename/description.
3. **Source every dish name and price from the menu data** — `assets/menu.json` (raw export, source of truth) or `references/menu_reference.md` (condensed, human-readable version grouped by category: Weekend Specials, People Choice, Biryani, Tandoori, Desserts, Beverages, etc.). Never invent a dish or price; if a requested dish isn't in the menu file, say so.
4. **For vague or open-ended requests** (e.g. "make this week's Weekend Special poster" with no dishes specified), pick a reasonable, appealing combination from the "Weekend Specials" menu category (or another fitting category for the occasion), state the picks explicitly, and proceed — don't block on asking unless the request is genuinely ambiguous about *type* (e.g. unclear whether it's a weekend menu board vs. a single-dish spotlight).
5. **Build the poster** following `references/design_generation_guide.md` (layout, color, footer, imagery) **and `references/production_pipeline.md` (MANDATORY before writing any rendering code)** — the latter documents which rendering approaches silently fail, the Pillow compositing method that works, how to produce food cutouts with `rembg`, and where the real logo/Halal assets come from.
6. **Verify the render programmatically, then run `references/checklists.md`** before presenting the result.
7. **If asked to "sync drive" or "check menu updates"** — re-query the Drive folder (`parentId = '13hM3lUL7Fo1DA6rIbgz_MUPyf2SJ5_u_'`) and re-check the uploaded `menu.json` against what's in `assets/menu.json`; report what's new or changed, and update the reference files if there's a genuine change (new poster style, new menu category, price changes) rather than silently ignoring drift.

## Quick-reference: the non-negotiables

- **Logo at the very top**, every poster: "RAJA RANI" (large gold) / "INDIAN RESTAURANT" (smaller gold/white caps) / "Taste of Chettinad" (thin gold script) — centered.
- **Black background, gold/yellow accents** — the premium black-and-yellow theme applies to every poster, including festival ones (layer the festive motif on top of it, don't replace it).
- **Footer, every poster:** phone (+1 734-404-5523), address (45172 Ford Road Canton, MI 48187), website (www.rajaranimichigan.com), social handle (raja_rani_indian_restaurant).
- **Halal badge** in the lower third, unless it's a pure greeting/press/testimonial poster.
- **A CTA badge** — "ORDER NOW" for food posters, an event-appropriate action (register/book/date) for events.
- **Menu accuracy** — every dish name and price traced back to `assets/menu.json`.

For full brand detail and stylistic patterns: `references/client_profile.md`. For the poster-type catalog and Drive sync instructions: `references/drive_asset_inventory.md`. For the condensed menu: `references/menu_reference.md` (raw source: `assets/menu.json`). For the build process: `references/design_generation_guide.md`. For the rendering pipeline, cutout method, real assets, and known failure modes: `references/production_pipeline.md`. For the final check: `references/checklists.md`.

## Updating this skill

When new posters are approved and added to the Drive folder, or the menu changes:
- Update `references/drive_asset_inventory.md` with new poster types/examples.
- Re-export `assets/menu.json` and regenerate `references/menu_reference.md` if the menu changes.
- Add any newly-confirmed hard rule or stylistic pattern to `references/client_profile.md`, keeping old rules intact unless the client explicitly overrides them — note contradictions rather than silently overwriting.
