# Design Generation Guide — Raja Rani Michigan Posters

## Before you start
1. Read `client_profile.md` for hard rules and stylistic patterns.
2. Confirm the dish(es)/theme for this poster:
   - **Weekend Special / dish-specific request:** pull exact names + prices from `assets/menu.json` or `references/menu_reference.md`.
   - **Event/occasion request** (Mother's Day, Banana Leaf Feast, festive, seasonal, combo): check `drive_asset_inventory.md` for a past poster of the same or a similar occasion so you don't duplicate a layout or an already-used tagline.
3. Decide the poster **type** (see the categories in `drive_asset_inventory.md`): weekend menu board, single hero dish, combo/bundle, festival/seasonal, recurring weekly promo, or loyalty/trust — this determines the layout template to reach for.

## Building the actual visual

> **READ `references/production_pipeline.md` FIRST.** It documents which rendering approaches silently fail and the exact method that works. The short version:
> - **Deliverable is always an image file (`.jpg`/`.png`), never HTML.** The client has explicitly said not to give HTML designs.
> - **Do not render via HTML/CSS + wkhtmltoimage** — the sandbox's ancient WebKit silently drops gradient text, blend modes, and tiled patterns, and pushes overflowing elements off-canvas. This caused repeated "background is black / ORDER NOW is missing" failures.
> - **Composite directly with Pillow (PIL).** Download fonts from the Google Fonts GitHub mirror; they are not preinstalled.
> - **The food photo must be a background-removed cutout (`rembg`) floating with a soft drop shadow — never in a box, oval, frame, or vignette.** This is the single most-repeated mistake.
> - **Verify every region programmatically before presenting** — don't assume an element rendered.

- **Canvas / aspect ratio:** default to a square (1080×1080) or portrait (1080×1350) format suited for Instagram/Facebook feed posts unless the client specifies a story (1080×1920) or print size.
- **Background:** solid black or a very dark charcoal-to-black gradient, overlaid with the subtle gold diamond-lattice tile. Never a light background (except the narrow approved exceptions: cream/temple "People's Choice" treatment, bright-yellow bold treatment, dark-brown for desserts).
- **Logo block (top):** recreate the three-line lockup — "RAJA RANI" (large, bold, gold, serif/display), "INDIAN RESTAURANT" (smaller, tracked caps, gold or white), "Taste of Chettinad" (thin gold script/italic, smallest) — centered at the top. Optionally flank with a thin gold rule or small ornament.
- **Headline:** the poster's theme/occasion in a large gold or white display font directly below the logo block ("WEEKEND SPECIAL," "DIWALI SPECIAL," "BANANA LEAF FEAST," etc.).
- **Body:**
  - Menu-board style: stacked dish name + price lines (gold name/price, white secondary detail), optionally split into Veg/Non-Veg columns.
  - Hero-dish style: a **background-removed food cutout floating with a drop shadow** (never framed), a short script eyebrow word ("Irresistible", "Delicious"), the dish name as the dominant type element (large gold-gradient Cinzel serif, or bold condensed sans for a punchier ad), a short caps tagline ("RICH. CREAMY. UNFORGETTABLE."), and optionally a 3-item feature row with gold dividers ("SLOW SIMMERED | RICH IN FLAVOR | CHEF'S SIGNATURE").
  - Combo/event style: a clean price table or a date/time/registration block.
- **Halal badge:** use the **real badge asset** extracted from an approved poster (see `production_pipeline.md` §4) — do not hand-draw an approximation. Place it in a lower corner unless this is a pure greeting/press poster.
- **CTA badge:** the brand's signature **circular** badge — black fill, gold ring, "ORDER" over "NOW" stacked — placed in a lower corner. (A rounded gold pill is *not* the brand's style; that was a rejected deviation.)
- **Footer band:** on hero-dish posters this is a **solid gold band with near-black text and dark icons** — left column [facebook] restaurant name / [pin] address; centre [phone] number in bold; right column [globe] website / [instagram] handle. Menu-board and festival posters sometimes use a black band with gold text instead — match the closest reference poster for the type you're building. Icons are required; draw them as clean vectors (the ones embedded in posters are too low-res to reuse).
- **Photography:** real, appetizing photographic images only — never AI-generated or illustrated food imagery in the final poster.

  **Important environment reality:** there is **no AI image-generation tool** in this sandbox, and bash network egress is limited to package repos, so a food photo **cannot be downloaded from the open web onto disk** (`web_fetch` also refuses image content). Plan around this instead of promising a photo you can't obtain.

  Preference order:
  1. A photo the user uploads in the conversation (**best — ask for one if the dish has no existing photo**).
  2. A photo already inside an approved poster in Drive — but it must be **background-removed into a clean cutout** (`rembg`), never a rectangular crop of the old poster, which drags along the old background/pattern/badges and reads as "cropped and pasted."
  3. The client's site (`rajaranimichigan.com`) for menu photos.

  If a requested dish has no usable photo anywhere, **say so plainly and ask the user to upload one** — do not substitute an unrelated dish's photo, and do not silently re-skin an old poster's image.

## After building
- **Verify programmatically before presenting** (see `production_pipeline.md` §6): sample each region (logo, badge/ribbon, headline, tagline, food cutout, feature row, Halal badge, ORDER NOW badge, footer) and confirm it has real, non-black pixel content. Also trace the vertical layout math to confirm nothing overflows the canvas or collides with the footer. Silently-dropped and pushed-off-canvas elements are the most common failure and are invisible unless you check.
- Double-check every hard rule from `client_profile.md`'s "Hard brand rules" section is present: logo at top, black-and-gold palette, full footer (phone/address/website/social **with icons**), Halal badge (unless exempted), circular ORDER NOW badge.
- Confirm the food is a **floating cutout with a drop shadow** — not framed, boxed, ovaled, or vignetted.
- Double-check every dish name/price against `assets/menu.json` — typos or stale prices are the easiest way to fail review.
- If this is a weekend special, check `drive_asset_inventory.md` to avoid repeating a dish combination or tagline used very recently.
- Present the result and briefly note any assumptions made (aspect ratio chosen, which dishes were picked if the brief was open-ended, whether a placeholder image was used).
