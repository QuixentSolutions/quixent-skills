# Madras Magic — Drive Asset Inventory

This file documents what actually lives in Vengatesh's connected Google Drive for this client, so
future sessions don't have to rediscover folder contents from scratch. Counts and contents below
were verified directly (via `parentId =` structured queries, the reliable method — title-based
search undercounts files with empty `fileExtension` fields, which is common for phone-uploaded
photos/videos).

## Folder structure and counts (verified 24-Jun-2026)

| Folder | Folder ID | File count | Content type |
|---|---|---|---|
| Madras magic client info | `1W4MVIFmdHQq0XTk4sxnjvODljzjPuV-Z` | 3 | Instagram screenshots (grand opening, bio/profile) |
| Madras magic approvals | `1ugemoY8edJuMdKbydA963acYB1KC9kHh` | 25 | Mix of Instagram screenshots of live/approved posts + some raw photos/videos |
| Madras magic rejections | `1RI2FDS_WG9tr0puf-kBDvixnA_DeDhLD` | 12 | Mostly raw rejected design files (cricket banner variants, stamp card draft, logo variants) + 2 short videos |
| Madras magic foods | `1D4MJVH5G1GNTHQQ5h90V3EDXSqNJyJOr` | 40 | **Genuine raw professional food photography** (DSLR filenames like `1Y6A####.jpg`) + a few Instagram screenshots + 1 large video |
| (External) madras_magic_ad_workspace_final.xlsx | Google Sheet, ID `1SFnCFbS-Idwfx0PTsqIgG087RaoYQXT8` | — | The original iteration tracker — richest source of rejection *reasons* in text form |

**Key lesson learned**: don't assume a folder's literal name perfectly predicts its contents.
"Approvals" and "rejections" both contain a mix of file types; "foods" turned out to hold the real
unused photography, not an obviously-named folder. Always verify with a structured `parentId =`
query before concluding a folder is empty or irrelevant.

## What's genuinely useful in each, and what to ignore

### Client info folder
Useful for: confirming bio facts (grand opening Dec 30 2024, hours 11:00–14:30 / 17:00–21:30,
address, contact details) if a brief needs "About us" style content. Not useful for new design
material — it's all already-published screenshots.

### Approvals folder
Mostly re-confirms posts already documented in the main profile (Butter Chicken, Golden Ghee Masala
Chicken, Mother's Day Set, Happy Hour combo, Idli vs Dosa, Cheese Crispy Sticks, Tandoori Briyani).
Useful as a sanity-check archive, not a source of new ideas — these are all things that have already
been posted publicly.

### Rejections folder — genuinely useful, confirmed evidence
- **Cricket banner, 2 rejected variants**: identical dense composition (Indian flag, trophy, Taipei
  101 line-art, multiple real cricket club logos, Yingfeng Cricket Ground) — rejected purely because
  the date read "June 6-7,13-14 **2025**" instead of 2026. The corrected, approved version (also in
  the approvals folder) is otherwise pixel-identical. This is now logged in section 1.1 of
  `client_profile.md` as the cleanest direct evidence of the wrong-year rejection pattern.
- A stamp/loyalty card draft and an early logo variant are also present — useful as historical
  reference if doing further loyalty-card or logo-adjacent work, but no specific rejection reason
  was confirmed for these in conversation, so don't assume why they were rejected without asking.

### Foods folder — the real asset library
This is raw, professional, photo-real food photography — confirmed genuine on direct visual
inspection (real plating, real props, real lighting, no AI-render artifacts). Key finds:
- **`1Y6A5918.jpg`**: Cheera Paneer, alternate uncropped angle with cardamom pods, brass dish,
  magazine prop in background — same dish as the published post but a different framing.
- **`1Y6A1799.jpg`**: takeaway meal box (naan, tandoori chicken, vegetables, curry cup) — matches
  the published combo post but higher quality/uncropped.
- **`1Y6A1814.jpg`**: the Jamun cocktail, wider angle, with Cheera Paneer and a paneer/cottage
  cheese skewer dish visible in the background — confirms this was a multi-dish photoshoot session,
  not single isolated product shots.
- **`1Y6A5954.jpg`**: a full table spread — cone dosa, idli steamer, naan, mango lassi, paneer
  skewers, blue mocktail, a copper-pot curry, cheese crispy sticks, and small Tamil/Indian decor
  figurines in frame. **This is the standout unused asset** — a single photo capturing breadth of
  the menu, well-lit and styled, not yet used as a standalone post as of this session.
- Several filenames repeat with near-identical content (e.g. `1Y6A1805.jpg` appears twice under
  different file IDs) — likely accidental duplicate uploads, not different shots.
- A handful of files in this folder are still Instagram screenshots (Mother's Day posts) mixed in
  with the raw photography — check `mimeType` and filename pattern (DSLR-style `1Y6A####` vs.
  `Screenshot_########_######.jpg`) before assuming a file is raw photography.

## How to use this inventory in future sessions

1. **Before generating a new design concept**, check this file first to see if usable raw
   photography already exists for the relevant dish, rather than assuming a photoshoot is needed
   or defaulting to a text-only brief.
2. **When syncing** (Vengatesh says "sync drive" / "sync folders" / similar), re-run the
   `parentId =` query against all 4 folder IDs below and compare counts against the "last verified
   count" below. If counts differ, list what's new and process per SKILL.md's sync workflow.
3. **Always query by `parentId =` directly**, never title-based search — confirmed the only
   reliable method for files with empty `fileExtension` fields (common with phone uploads).
4. **Don't assume folder names are exhaustive descriptions of contents** — verify before reporting
   counts or contents to Vengatesh.
5. **A surfaced raw photo doesn't replace the iteration tracker for rejection *reasons*** — combine
   visual evidence from these folders with the Excel sheet's text record when both are relevant.

## Last verified counts (for sync comparison)

| Folder | Folder ID | Last verified count | Last verified date |
|---|---|---|---|
| Madras magic client info | `1W4MVIFmdHQq0XTk4sxnjvODljzjPuV-Z` | 3 files + 1 subfolder ("Menu", 1 file) | 09-Jul-2026 |
| Madras magic approvals | `1ugemoY8edJuMdKbydA963acYB1KC9kHh` | 28 | 09-Jul-2026 |
| Madras magic rejections | `1RI2FDS_WG9tr0puf-kBDvixnA_DeDhLD` | 13 | 09-Jul-2026 |
| Madras magic foods | `1D4MJVH5G1GNTHQQ5h90V3EDXSqNJyJOr` | 40 | 09-Jul-2026 |

When a sync runs, update this table with the new counts and date so the next sync has an accurate
baseline to compare against.

## New files found in 02-Jul-2026 sync (unconfirmed context — ask Vengatesh)

Only the approvals folder changed (25 to 27 files). Both new files are unidentified beyond filename
and timestamp and need Vengatesh's confirmation before being logged as approved evidence anywhere
else:

- `_Instagram Post-1.mp4` (added 26-Jun-2026) — **confirmed by Vengatesh**: the 26-Jun-2026 Friday
  reel logged in the Excel sheet (approved on iteration 1, but resent 3x for missing bgm/low
  quality per section 2.11 of client_profile.md).
- `mm 123.png` (added 02-Jul-2026) — **confirmed by Vengatesh**: the 30-Jun-2026 Tuesday post,
  Pani Puri (印度脆球) hero design, green bg. Logged in `posted_content_registry.md`.

## New items found in 09-Jul-2026 sync (unconfirmed context — ask Vengatesh)

- **New "Menu" subfolder** (`1ICDQj724XpjhbaN014fPtgfWZUDh_RTj`) under the client info folder,
  created 06-Jul-2026, containing one file: `MM Menu_compressed.pdf` — the restaurant's full current
  menu (bilingual EN/CN), covering banana leaf feast, starters/appetizers, dosa/idly special, mains,
  beverages, and mocktails, each with exact Chinese names and NTD pricing. **Genuinely useful**: use
  this as the authoritative source for dish names and Chinese spelling when drafting new briefs,
  rather than guessing or relying on a single machine translation (ties directly into the section
  1.1 text-accuracy hard rule in `client_profile.md`).
- `IMG-20260707-WA0005.jpg` (approvals folder, added 07-Jul-2026) and `IMG-20260707-WA0000.jpg`
  (rejections folder, added 07-Jul-2026) — dates line up exactly with the 7-Jul-2026 Tuesday post
  logged in the Excel sheet (v1 rejected for background "too dark," v2 approved), so these are very
  likely that post's two versions — **but not yet visually confirmed by Vengatesh**.
