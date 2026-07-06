# madras-magic-design-brief

A Claude skill that helps predict what **Madras Magic Restaurant** (Indian restaurant in Taiwan, [@madrasmagic_indiancuisine](https://instagram.com/madrasmagic_indiancuisine)) will approve or reject, generate on-brand design concepts and reel scripts, and track how the client's taste evolves over time — grounded in real iteration history, not guesswork.

## What this is

- An evidence-based pattern profile, not a trained ML model. "Learning" means new confirmed approvals/rejections get logged as documented evidence, and existing rules get strengthened, added, or flagged as contradicted.
- Can produce text-only design briefs and actual mockup images (composited from real client photos and the real logo).
- Cannot generate video/reel files — only detailed written reel scripts for a human to film/edit.
- Approval predictions are reasoned likelihood assessments against documented patterns, not guarantees.
- Nothing auto-runs in the background — every sync/update/prediction happens only on request.

## Structure

```
madras-magic-design-brief/
├── SKILL.md                              # Entry point: rules, triggers, workflow
├── assets/
│   └── iteration_log_template.csv        # Logged approval/rejection history
└── references/
    ├── client_profile.md                 # Client preferences, hard rules, contacts
    ├── checklists.md                     # Pre-delivery self-check checklist
    ├── design_generation_guide.md        # How to build mockups/compositing rules
    ├── drive_asset_inventory.md          # Index of the 4 connected Drive folders
    ├── posted_content_registry.md        # What's already been published
    ├── reel_script_guide.md              # Reel/video script format guide
    ├── taste_trends.md                   # Evolving taste-trend hypotheses
    └── approval_prediction_guide.md      # How predictions are reasoned
```

## Usage

Install as a Claude skill (`/mnt/skills/user/madras-magic-design-brief` or your Claude Projects skill directory). Trigger phrases include starting any new design brief for Madras Magic, or syncing sources with phrases like "sync xl sheet", "sync drive", "sync folders", "check for updates".

## Sync sources

- Google Sheet: `madras_magic_ad_workspace_final.xlsx`
- 4 Google Drive folders (IDs listed in `references/drive_asset_inventory.md`)

See `SKILL.md` for the full sync procedure and hard rules (no AI-generated food imagery, no web-sourced images, all designs are drafts pending Vengatesh's review, Chinese text requires native-speaker verification).
