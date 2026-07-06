# Madras Magic — Design Generation Guide

How to actually build a mockup image for this client, grounded in real assets rather than
generated/AI imagery — which would violate the client's #1 confirmed hard rule.

## Core principle: real assets only

- **Never generate AI food imagery** for this client, even as a placeholder or "just to show the
  idea" — the client has explicitly rejected designs for looking AI-generated, especially for
  print. This rule applies even to draft/concept stages shown to Vengatesh, since a habit of using
  AI placeholders risks one slipping through to the client by accident.
- **Always use real, unused photography** from the Drive "foods" folder (see
  `drive_asset_inventory.md` for the inventory) where possible. If no suitable real photo exists
  for a requested dish, say so plainly and offer text-only brief instead of generating a fake image.
- **Always use the real logo**, cropped directly from an existing approved design file — never
  redraw or approximate it. The cleanest known source crop is from the Cheese Crispy Sticks post
  (exact pixel boundary: x 93–1133, y 0–307 in that source image, black rounded-rectangle header
  containing the logo badge + Chinese name + English name + script tagline). Crop once, save as
  `header.png`, and reuse across designs rather than re-cropping each time.

## Header treatment — two confirmed variants

Both are pulled directly from approved client artwork. Pick based on the content bucket, don't
default to one blindly:

1. **Full-width header bar** (Cheese Crispy Sticks, Butter Chicken, Idli vs Dosa, Tandoori Chicken
   Briyani) — black rounded-rectangle bar spanning the full frame width at the top: logo badge +
   Chinese name (large gold) + English name (small caps) + script tagline. This is the more common,
   "premium hero" treatment — default to this unless the brief calls for something more casual.
2. **Compact top-left badge** (confirmed via Pani Puri, approved 30-Jun-2026) — the same logo/name
   content, but scaled down into a smaller black rounded-rectangle box tucked in the top-left corner
   only, leaving the rest of the top of the frame open for large display type. Use this when the
   headline type needs to dominate the top of the frame (bold poster-style treatments, e.g. the
   green-bg Pani Puri post) rather than sharing that space with a full-width brand bar.

**Compositing/layering order, confirmed by every approved design examined** (Pani Puri, Tandoori
Briyani, Cheese Crispy Sticks, Idli vs Dosa): the food/background photo is the base layer, the logo
header sits on top of it as a fixed-position element (never cropped or obscured by the food), and
headline/caption text is placed last, fitted into whatever space remains around the photo and logo.
When building a design, follow this same order — place the photo first since its crop/color drives
everything else, drop the logo header on top at a known anchor point since it's a fixed asset that
doesn't adapt to the photo, then size and position text last since it's the most flexible element.

## Workflow

1. **Check `posted_content_registry.md` first, before anything else.** Confirm the requested dish
   hasn't already been posted, and that the layout/format you're about to propose hasn't already
   been used — either for this dish or overused generally within the current conversation. If
   either check fails, say so explicitly and adjust: pick a different angle for an already-posted
   dish, suggest an unposted dish instead, or pick a format marked "not yet used in any real
   published post" in the registry.
2. **Identify the dish and check naming carefully.** Cross-reference the dish against confirmed
   names from approved posts/menus before labeling anything. If a photo's exact dish identity is
   ambiguous (e.g. a generic-looking curry that could be more than one menu item), use generic
   descriptive language instead of guessing a specific name — getting this wrong directly
   contradicts the #1 text-accuracy rule. Flag the ambiguity to Vengatesh rather than silently
   picking one.
3. **Pick a color/layout bucket deliberately, and vary it across requests.** Don't default to the
   same dark-green vertical-stack template every time — that's already been used multiple times in
   this conversation history. Cross-check `posted_content_registry.md`'s format table for what's
   fresh. Real structural variety options established so far:
   - Dark green/maroon + gold vertical stack (header → headline → photo → caption) — the most-used
     "premium hero" template, reserve for when nothing more specific is requested.
   - Bright/bold poster-type with tilted photo and a price tag — casual, trendy bucket.
   - Minimal split-screen (full-bleed photo one side, generous negative space + small refined type
     the other) — elegant/quiet bucket.
   - Full-bleed photo with editorial gradient fade into a multi-column text panel — magazine/
     showcase bucket, good for multi-dish or "about us" style posts.
   - Circular badge/seal composition on a warm cream background — intimate, stamp-like bucket,
     good for a single specialty item.
   When asked for "different concepts" or "try different," actively pick a structure not yet used
   in the current conversation rather than reskinning the same layout with new colors.
4. **Crop source photos deliberately**, not just centered defaults — check the crop at full
   resolution before finalizing; some source photos lose quality or composition strength when
   cropped too tightly (a real limitation hit when attempting a tight sambar-bowl crop from a wide
   group shot — the resolution wasn't sufficient for a clean hero crop). If a crop looks weak,
   either pick a different photo or use a wider crop.
5. **Build as an HTML file, render with `wkhtmltoimage`** (confirmed working in this environment;
   Google Fonts are blocked by network restrictions, so use system-safe fonts like Georgia and
   "Noto Serif TC" with serif fallback rather than `@import`-ing web fonts).
6. **Always flag unverified Chinese copy explicitly** in the response — any caption/headline text
   beyond dish names taken directly from confirmed sources is a draft that needs native-speaker
   verification before going near the client. State this every time, not just the first time.
7. **Save renders to `/mnt/user-data/outputs/` and present them** — don't just describe a concept
   in text when an actual mockup was requested.
8. **After the design is finalized or sent**, offer to add it to `posted_content_registry.md`'s
   tracking (even before client approval, mark it clearly as "proposed, not yet approved" so it
   doesn't get confused with confirmed published content — only move it to the main table once
   Vengatesh confirms the client approved it).

## What NOT to do

- Don't propose a dish or layout format without checking `posted_content_registry.md` first —
  repeating an already-posted dish or an overused format wastes effort and risks boring the
  client's audience.
- Don't reuse the exact same template structure repeatedly when asked for variety — this has
  happened before in this project and was called out directly.
- Don't guess a specific dish name from a photo alone when there's real ambiguity — use generic
  language and flag it.
- Don't skip the real-logo-crop step and redraw an approximation instead, even if it looks similar.
- Don't present a generated mockup as send-ready — always note what still needs verification
  (Chinese copy, dish naming, final export size for the actual use case).
