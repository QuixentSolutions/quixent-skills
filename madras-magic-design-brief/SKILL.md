---
name: madras-magic-design-brief
description: Use this skill whenever Vengatesh is creating, planning, or reviewing a design (poster, banner, social media post, reel/video script, stamp card, or any visual asset) for the client Madras Magic Restaurant (Indian restaurant in Taiwan, Instagram @madrasmagic_indiancuisine). Trigger this for any new design brief, before starting design work, when drafting a concept, when self-checking a draft before sending it to the client, when the client's request is vague, when asked to predict whether a design will be approved, or when asked to generate a design/mockup/reel script. Also trigger when Vengatesh says any sync phrase such as "sync xl sheet", "sync drive", "sync folders", "check for updates", or similar — this means re-reading the live Google Sheet and the 4 connected Drive folders for new approvals/rejections/photos and updating this skill's reference files accordingly. Covers Instagram posts, reels, print posters/banners, menus, stamp/loyalty cards, and resin art designs.
---

# Madras Magic Design Brief Assistant

Helps Vengatesh predict what the client (Madras Magic Restaurant, an Indian restaurant in Taiwan) will approve or reject, generate on-brand design concepts and reel scripts, and track how the client's taste evolves over time — all grounded in real iteration history, not guesswork.

**Read this section before doing anything else: what this skill actually is and isn't.**
- This is an evidence-based pattern profile that improves as more real examples are added. It is **not** machine learning — no model is trained, no statistical confidence scores are computed. "Learning" here means: a new confirmed approval/rejection gets added as documented evidence, and existing rules get strengthened, added, or flagged as contradicted.
- This skill can produce **text-only design briefs** and **actual mockup images** (built from real client photos and the real logo, composited into a layout). It **cannot** generate actual video/reel files — only detailed written reel scripts (shot list, pacing, on-screen text timing, music mood) for a human to film/edit.
- Approval predictions are **reasoned likelihood assessments against documented patterns**, not guarantees. Always say so plainly when giving one.
- Nothing in this skill auto-runs in the background. Every sync, every update, every prediction happens only when Vengatesh asks for it in a message — there is no live or continuous connection to the Drive folders or the Excel sheet between conversations.

## Sync triggers — re-reading live sources on request

When Vengatesh says any of: **"sync xl sheet"**, **"sync drive"**, **"sync folders"**, **"check for updates"**, **"sync everything"**, or clearly equivalent phrasing:

1. Read the live Excel sheet (`madras_magic_ad_workspace_final.xlsx`, Google Sheet ID `1SFnCFbS-Idwfx0PTsqIgG087RaoYQXT8`) via Google Drive's `read_file_content`. Compare rows against what's already logged in `assets/iteration_log_template.csv` and `references/client_profile.md`. Pull out any genuinely new rows.
2. Query all 4 Drive folders by their `parentId` (IDs are listed in `references/drive_asset_inventory.md`) — use the structured `parentId = '<id>'` query, **not** title-based search, since phone-uploaded files often have empty `fileExtension` fields that break title search. Compare file counts and filenames against the inventory file to find what's new.
3. For each new item found:
   - If it's a clear approval or rejection with a discoverable reason (visual evidence, sheet notes, or by asking Vengatesh directly when the reason isn't obvious from the file alone) — add it to `client_profile.md` under the relevant section, append a row to `assets/iteration_log_template.csv`, **and add the dish/format to `references/posted_content_registry.md`** if it represents newly-confirmed published content.
   - If it's new raw photography with no associated outcome yet, add it to `references/drive_asset_inventory.md` as an available asset, not as approved/rejected evidence.
   - If it contradicts an existing documented rule, do **not** silently overwrite the old rule — note the contradiction explicitly (see "Updating the profile" below) and ask Vengatesh whether this reflects a genuine shift in preference.
4. Update `references/taste_trends.md` if the new evidence is enough to support or weaken a trend hypothesis.
5. Summarize what changed in plain language before doing anything else — don't silently update files without telling Vengatesh what was found.

If nothing has changed since the last sync, say so plainly rather than implying something was updated.

## How to use this skill for everyday tasks

1. **Before starting a new design**, read `references/client_profile.md` in full for hard rules, soft preferences, and rejection patterns.
2. **Check `references/posted_content_registry.md`** for every new design request — confirm the dish and the layout/format haven't already been used, to avoid repeating already-posted content. If either has been used, say so explicitly and pick a genuinely different angle, dish, or format.
3. **Check `references/drive_asset_inventory.md`** before assuming a new photoshoot or AI image is needed — real unused client photography may already exist.
4. **Check `references/taste_trends.md`** for any active trend hypotheses that might apply to a new design — apply cautiously, flagged as a hypothesis, not a settled rule.
5. **Check the brief against `references/checklists.md`** based on asset type.
6. **For vague briefs**, fill the gap using documented house style and state assumptions explicitly rather than silently deciding.
7. **For design/mockup requests**, see `references/design_generation_guide.md` for how to build an actual composited image using real assets (real logo crop, real unused photos) rather than generated/AI food imagery.
8. **For reel/video requests**, see `references/reel_script_guide.md` for how to write a shot-by-shot script grounded in confirmed reel patterns. Be explicit that this is a script for filming, not a generated video.
9. **For "will this get approved?" requests**, see `references/approval_prediction_guide.md` for the structured review process — check against every hard rule, name what's confirmed-safe vs. unverifiable, and always end with a concrete "things to change" list when anything is uncertain.
10. **After getting real client feedback**, log it (see "Updating the profile" below) — update `references/posted_content_registry.md` too if it's now a published dish/format, not just `client_profile.md`.

## Quick-reference: the highest-value lessons

These cost the most rounds historically — check these first, always:

- **Spelling and language accuracy is the #1 repeat offender.** Verify Chinese text with a native speaker or back-translation before sending — never rely on a single machine translation.
- **Never let food/scene imagery look AI-generated.** Confirmed dealbreaker, especially for print. Use real photography only.
- **Print jobs need print-safe color and the right file format.** Default to delivering both JPEG and PDF; proof colors for print, not screen brightness.
- **Cultural/identity elements need care, not decoration.** Tamil identity markers (Thiruvalluvar, Thirukural, Tamil script) paired with specific Taiwan landmarks works well; generic "Indian-coded" motifs like arches risk misreading. Flag ambiguous iconography before sending.
- **Sizes and specs are exact, not approximate.** Confirm final export matches stated dimensions.
- **Multiple rounds are normal; identical repeated mistakes are the real failure signal.**

For full details with evidence: `references/client_profile.md`. For checklists: `references/checklists.md`. For Drive contents: `references/drive_asset_inventory.md`. For already-posted dishes/formats (check before proposing anything new): `references/posted_content_registry.md`. For trend tracking: `references/taste_trends.md`. For design generation: `references/design_generation_guide.md`. For reel scripts: `references/reel_script_guide.md`. For approval prediction: `references/approval_prediction_guide.md`.

## Updating the profile

The profile is a living document. When Vengatesh shares a new completed project, or after a sync finds new evidence:
- Add new rejection/approval reasons to the relevant category in `client_profile.md`, or create a new category if genuinely new.
- If new evidence contradicts an existing rule, **do not delete the old rule** — note the contradiction explicitly and ask Vengatesh whether the client's taste has actually shifted, or whether it's a one-off. Log this in `references/taste_trends.md` as an open hypothesis until there's enough evidence to treat it as confirmed.
- Keep evidence citations (which iteration, what happened, source file) so the profile stays grounded in real history, not vague generic advice.
- Never apply a "trend" from `taste_trends.md` as if it were a confirmed rule — always state it's a hypothesis with N supporting examples, and let Vengatesh weigh in once enough evidence accumulates.
