# Production Pipeline — How to Actually Render a Raja Rani Poster

This file exists because several approaches were tried and failed. Read it before writing any rendering code.

---

## 1. Do NOT render via HTML/CSS → wkhtmltoimage

The sandbox has `wkhtmltoimage 0.12.6`, built on a very old WebKit. It **silently fails** on modern CSS — it does not error, it just renders the element as blank/black. Confirmed broken:

- `background-blend-mode` → ignored
- `background-clip: text` / `-webkit-background-clip: text` gradient text → renders as **nothing** (invisible)
- Tiled `background-image` with `background-size` on the same element as a gradient → pattern silently dropped
- Flex/absolute stacking that overflows the canvas → elements pushed off-canvas with no warning

Symptoms this produced repeatedly: "the background is totally black," "the ORDER NOW button is missing," "the footer lost its pattern." These were **not** design mistakes — they were the renderer dropping elements. Do not try to fix them by tweaking CSS.

**Also: the user explicitly does not want HTML deliverables.** The deliverable is always an image file (`.jpg`/`.png`), never an `.html`.

## 2. DO render with Pillow (PIL) direct pixel compositing

Build the poster by compositing layers directly. This gives exact control and nothing silently disappears.

- Canvas: `1080 × 1350` (portrait IG feed) unless told otherwise.
- Fonts are **not installed** in the sandbox — download from the Google Fonts GitHub mirror (allowed domain `raw.githubusercontent.com`):
  - Cinzel (display serif — dish names): `ofl/cinzel/Cinzel%5Bwght%5D.ttf`
  - Cinzel Decorative: `ofl/cinzeldecorative/CinzelDecorative-Black.ttf`
  - Great Vibes (script eyebrow): `ofl/greatvibes/GreatVibes-Regular.ttf`
  - Oswald (condensed sans — taglines/footer): `ofl/oswald/Oswald%5Bwght%5D.ttf`
  - Noto Naskh Arabic (only if hand-drawing a Halal badge): `ofl/notonaskharabic/NotoNaskhArabic%5Bwght%5D.ttf`
- Cinzel and Oswald are **variable fonts** — set weight via `font.set_variation_by_axes([900])`.
- Gold gradient text: render the glyphs to an `L` mask, build a vertical gradient array, and `paste(grad, (0,0), mask)`. (This is the effect that silently fails in wkhtmltoimage.)
- For Arabic (`حلال`), reshape first: `arabic_reshaper.reshape()` → `bidi.algorithm.get_display()`. **But prefer the real extracted badge asset (below) over hand-drawing one.**

## 3. Food photos MUST be cutouts — this is the #1 recurring mistake

**Every approved hero-dish poster** (Karampodi Shrimp, Chilli Paneer, Paneer Tikka, Butter Chicken, Fish Pakoda) shows the dish as a **background-removed cutout floating directly on the poster background**, with a soft drop shadow beneath it.

**Never** do any of these — all were rejected:
- ❌ Photo inside a rounded rectangle / box / frame
- ❌ Photo inside an oval or circle frame
- ❌ Photo with a vignette or feathered fade at the edges
- ❌ A rectangular region cropped out of an old poster and pasted in (the old poster's background, pattern, and stray badges come along with it and it reads as "cropped and pasted")

**Correct method:**
```python
from rembg import remove          # pip install rembg onnxruntime --break-system-packages
cutout = remove(Image.open(src))  # model auto-downloads from github releases (allowed domain)
```
Then:
1. Crop the source **generously** so the dish never touches the crop edge — verify the alpha bbox has margin on all four sides, otherwise the bowl gets clipped.
2. Tighten to the alpha bbox with ~10px padding.
3. Sanity-check the mask: expect roughly ≥65% opaque / ≥20% fully transparent. A mask that is mostly *semi*-transparent is a bad cutout.
4. Drop shadow: paste the alpha silhouette as black, offset down slightly, `GaussianBlur(~26)`, composite **under** the cutout.

## 4. Reusable real assets (extract once, reuse)

- **Logo** — Drive file "Raja Rani logo updated", ID `1eCmVoD_16WyRf6b804xIiq1R-zWQPn9H` (1409×1409 JPEG, near-white `#F7F7F7` background). Make transparent by keying out pixels where `R,G,B > 235`. This is the client's real logo — always prefer it over redrawing the lockup.
- **Halal badge** — no standalone asset exists; extract it from a high-resolution approved poster. Locate it by scanning for its distinctive teal-green in the bottom-right quadrant (`r<90, 90<g<190, 50<b<150`), then crop to a circle with an elliptical alpha mask. Extract from the **largest** source poster available (e.g. the Butter Chicken poster is 2558×3200 → yields a sharp ~262px badge). Do not hand-draw an approximation.
- **Footer icons** (facebook, location pin, phone, globe, instagram) — the ones embedded in the posters are only ~25px in compressed JPEG, so they go blurry when scaled up. **Draw these as clean vector shapes in PIL** instead of extracting.
- **Diamond-lattice background pattern** — generate a seamless ~140px tile (gold diamond outline + quarter-diamonds at the four corners for tiling continuity) at low alpha (~70/255), then tile it over the black gradient.

## 5. Footer: gold band, dark ink (for hero-dish posters)

The approved hero-dish posters use a **solid gold/yellow footer band with near-black text and dark icons**, not a black band with gold text. Layout:

- Left column (2 rows): [facebook icon] `RAJA RANI Indian Restaurant` / [pin icon] `45172 Ford Road Canton, MI 48187`
- Centre: [phone icon] `+1734-404-5523` — larger, bold
- Right column (2 rows): [globe icon] `www.rajaranimichigan.com` / [instagram icon] `raja_rani_indian_restaurant`

Menu-board/festival posters sometimes use a black footer with gold text — check the closest reference poster for the type you're building.

## 6. Verify programmatically BEFORE presenting

The image viewer can fail to render previews. Never assume an element landed. After building, sample each region and assert it has real content:

```python
def check(name, box):
    r = arr[y0:y1, x0:x1]
    gold   = ((r[:,:,0]>180)&(r[:,:,1]>130)&(r[:,:,2]<170)).mean()
    bright = (r.mean(axis=2)>110).mean()
    print(name, r.mean(), gold, bright)
```
Check: logo, ribbon/badge, headline, tagline, food cutout, feature row, halal badge, ORDER NOW badge, footer band. A region reading `mean≈0` means it silently failed to render.

Also **trace the vertical layout math** and assert nothing overflows 1350px or collides with the footer — off-canvas overflow is what caused the "ORDER NOW is missing" failures.

## 7. Known environment limits — be honest about these

- **There is no AI image-generation tool available.** New food photography cannot be generated. The only real dish photos available are (a) images the user uploads, (b) photos inside the approved posters in Drive, (c) the client's website. If a requested dish has no usable photo, **say so and ask for one** rather than reusing an unrelated dish's photo or silently substituting.
- `bash` network egress is restricted to package repos (pypi, npm, github, crates) — **you cannot download a food photo from the open web onto disk**. `web_fetch` also refuses image content. So "just grab a stock photo" is not possible; plan around it.
