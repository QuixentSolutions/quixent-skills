# Pre-Send Checklist — Raja Rani Michigan Posters

Run through this before presenting any finished poster:

## Brand fundamentals
- [ ] Logo lockup ("RAJA RANI / INDIAN RESTAURANT / Taste of Chettinad") is at the top, gold-on-black, legible.
- [ ] Background is black / near-black. No light backgrounds.
- [ ] Gold/yellow is the dominant accent color for headlines, prices, and dividers.
- [ ] Footer includes all four: phone (+1 734-404-5523), address (45172 Ford Road Canton, MI 48187), website (www.rajaranimichigan.com), social handle (raja_rani_indian_restaurant).
- [ ] Halal badge present (unless this is a pure greeting/press/testimonial poster where it's been previously omitted).
- [ ] CTA badge present and worded appropriately ("ORDER NOW" for food, "REGISTER NOW"/"BOOK NOW"/date for events).

## Content accuracy
- [ ] Every dish name matches `assets/menu.json` spelling exactly.
- [ ] Every price matches `assets/menu.json` / `references/menu_reference.md` exactly.
- [ ] If a requested dish isn't in the menu file, this was flagged to the person rather than guessed.
- [ ] Event details (date, time, day-of-week restriction, dine-in-only, etc.) are stated clearly and match what the person specified.

## Imagery (the most-repeated failure — check every time)
- [ ] The deliverable is an **image file** (`.jpg`/`.png`), **not HTML**.
- [ ] The food is a **background-removed cutout floating with a soft drop shadow**.
- [ ] It is **NOT** in a box, rounded rectangle, oval, circle frame, or vignette/fade.
- [ ] It is **NOT** a rectangular crop lifted from an old poster (which drags the old background, pattern, and stray badges with it and reads as "cropped and pasted").
- [ ] The cutout isn't clipped — the whole bowl/plate is present, with margin on all sides.
- [ ] Halal badge is the **real extracted asset**, not a hand-drawn lookalike.
- [ ] Footer has **icons** (facebook, pin, phone, globe, instagram), not bare bullet dots.
- [ ] CTA is the brand's **circular** black-and-gold "ORDER / NOW" badge, not a generic pill button.
- [ ] If no real photo existed for the dish, the user was **asked to upload one** — no unrelated dish's photo was substituted, and no AI image was passed off as real.

## Render integrity (verify programmatically — do not eyeball-and-hope)
- [ ] Each region sampled and confirmed to have real, non-black content: logo, ribbon/badge, headline, tagline, food cutout, feature row, Halal badge, ORDER NOW badge, footer band.
- [ ] Vertical layout math traced: nothing overflows the 1350px canvas or collides with the footer. (Off-canvas overflow is what silently deletes the CTA.)
- [ ] Colors verified against the closest approved reference poster (e.g. dish-name text color — some approved posters use **white**, not gold).

## Design quality
- [ ] Food photography (if used) looks appetizing and high-contrast, not flat/stock/clip-art.
- [ ] Text hierarchy is clear at a glance: headline > dish/price > footer.
- [ ] Layout doesn't feel identical to a very recently produced poster for the same occasion (check `drive_asset_inventory.md`).
- [ ] Aspect ratio suits the stated platform (square/portrait for feed, tall for stories, larger canvas for print).

## Before presenting
- [ ] Any assumptions made (dish selection, aspect ratio, placeholder imagery) are stated plainly, not buried.
- [ ] Any element that could not be verified (e.g. image preview failed to render) is flagged honestly rather than presented as confirmed.
