"""
Raja Rani Michigan — HERO-DISH POSTER BUILDER (working reference implementation)

This is a known-good, end-to-end Pillow build of an approved-style hero-dish poster.
Adapt the CONFIG block for a new dish; the structure below matches the approved layout.

PREREQS
  pip install rembg onnxruntime arabic_reshaper python-bidi --break-system-packages
  Fonts (download to ./fonts/ from raw.githubusercontent.com — they are NOT preinstalled):
    Cinzel        ofl/cinzel/Cinzel%5Bwght%5D.ttf
    Great Vibes   ofl/greatvibes/GreatVibes-Regular.ttf
    Oswald        ofl/oswald/Oswald%5Bwght%5D.ttf
  Assets (bundled in ../assets/): logo_transparent.png, halal_badge.png, diamond_tile.png

FOOD CUTOUT (do this first, separately):
    from rembg import remove
    cut = remove(Image.open('source_photo.jpg'))   # crop generously first!
    # verify alpha bbox has margin on ALL sides, then tighten with ~10px padding
    # expect >=65% opaque / >=20% transparent; mostly-semi-transparent == bad mask

DO NOT render this via HTML/CSS + wkhtmltoimage — see references/production_pipeline.md.
ALWAYS verify each region's pixels before presenting (see bottom of this file).
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350

def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    if weight:
        try: f.set_variation_by_axes([weight])
        except Exception: pass
    return f

cinzel_huge  = font('fonts/Cinzel-Bold.ttf', 82, 900)
cinzel_tiny  = font('fonts/Cinzel-Bold.ttf', 15, 700)
great_vibes  = font('fonts/GreatVibes-Regular.ttf', 62)
osw_tag      = font('fonts/Oswald.ttf', 22, 500)
osw_feat     = font('fonts/Oswald.ttf', 19, 600)
osw_foot     = font('fonts/Oswald.ttf', 20, 500)
osw_footb    = font('fonts/Oswald.ttf', 27, 700)
osw_order    = font('fonts/Oswald.ttf', 24, 700)
osw_order_b  = font('fonts/Oswald.ttf', 38, 700)

GOLD  = (241, 196, 83)
CREAM = (245, 236, 214)

def tw(d, t, f, tr=0):
    if tr == 0: return d.textlength(t, font=f)
    return sum(d.textlength(c, font=f) + tr for c in t) - tr

def draw_tracked(d, y, t, f, fill, tr=0, cx=W/2, x=None):
    if x is None:
        x = cx - tw(d, t, f, tr)/2
    for c in t:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + tr

def grad_text(size, txt, f, tr=0):
    tmp = Image.new('L', size, 0)
    d = ImageDraw.Draw(tmp)
    x = (size[0] - tw(d, txt, f, tr))/2
    for c in txt:
        d.text((x, 0), c, font=f, fill=255)
        x += d.textlength(c, font=f) + tr
    h = size[1]
    top, mid, low = np.array([255,246,222]), np.array([241,196,83]), np.array([166,112,10])
    col = np.zeros((h,3)); half = h//2
    for y in range(h):
        if y < half:
            t = y/max(half,1); col[y] = top*(1-t)+mid*t
        else:
            t = (y-half)/max(h-half,1); col[y] = mid*(1-t)+low*t
    grad = Image.fromarray(np.tile(col[:,None,:], (1,size[0],1)).astype('uint8'), 'RGB')
    out = Image.new('RGBA', size, (0,0,0,0))
    out.paste(grad, (0,0), tmp)
    return out

def star(d, cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        a = math.pi/2 + i*math.pi/5
        rad = r if i % 2 == 0 else r*0.42
        pts.append((cx + rad*math.cos(a), cy - rad*math.sin(a)))
    d.polygon(pts, fill=fill)

# ---- background: black + subtle diamond pattern ----
bg = np.zeros((H, W, 3), 'uint8')
for y in range(H):
    t = min(y/1000, 1.0)
    bg[y,:,:] = (np.array([26,26,26])*(1-t) + np.array([0,0,0])*t).astype('uint8')
canvas = Image.fromarray(bg, 'RGB').convert('RGBA')

tile = Image.open('diamond_tile.png').convert('RGBA')
pat = Image.new('RGBA', (W,H), (0,0,0,0))
for yy in range(0, H, tile.height):
    for xx in range(0, W, tile.width):
        pat.paste(tile, (xx,yy), tile)
canvas.alpha_composite(pat)
d = ImageDraw.Draw(canvas)

# ---- gold border frame ----
d.rectangle((22,22,W-22,H-22), outline=GOLD+(190,), width=3)
d.rectangle((30,30,W-30,H-30), outline=GOLD+(85,), width=1)

# ---- logo ----
logo = Image.open('raja_rani_logo_cropped.png').convert('RGBA').resize((236,236), Image.LANCZOS)
canvas.alpha_composite(logo, (W//2-118, 40))

# ---- PEOPLE'S CHOICE ribbon (approved element) ----
rw, rh = 196, 76
rx, ry = W-52-rw, 56
d.rectangle((rx,ry,rx+rw,ry+rh), fill=(8,8,8,240), outline=GOLD+(210,), width=2)
draw_tracked(d, ry+13, "PEOPLE'S CHOICE", cinzel_tiny, GOLD+(255,), tr=1.5, cx=rx+rw/2)
sx = rx + rw/2 - (5*21)/2 + 10
for i in range(5):
    star(d, sx + i*21, ry+50, 8.5, GOLD+(255,))

y = 292

# ---- script eyebrow ----
eb = "Irresistible"
d.text((W/2 - tw(d, eb, great_vibes)/2, y), eb, font=great_vibes, fill=(255,255,255,255))
y += 74

# ---- huge gold serif dish name ----
l1 = grad_text((W-80, 100), "BUTTER", cinzel_huge, tr=4)
canvas.alpha_composite(l1, (40, y)); y += 92
l2 = grad_text((W-80, 100), "CHICKEN", cinzel_huge, tr=4)
canvas.alpha_composite(l2, (40, y)); y += 104
d = ImageDraw.Draw(canvas)

# ---- ornament divider ----
d.line((W/2-150, y, W/2-26, y), fill=GOLD+(200,), width=2)
d.line((W/2+26, y, W/2+150, y), fill=GOLD+(200,), width=2)
d.polygon([(W/2,y-9),(W/2+13,y),(W/2,y+9),(W/2-13,y)], fill=GOLD+(255,))
y += 24

# ---- tagline ----
draw_tracked(d, y, "RICH.  CREAMY.  UNFORGETTABLE.", osw_tag, CREAM+(255,), tr=3)
y += 44

# ---- FOOD CUTOUT (no frame, floating with shadow) ----
cut = Image.open('butter_chicken_cutout.png').convert('RGBA')
target_w = 860
scale = target_w / cut.width
cut = cut.resize((target_w, int(cut.height*scale)), Image.LANCZOS)
cx_pos = W//2 - cut.width//2
cy_pos = y + 6

# soft drop shadow from the alpha silhouette
alpha = cut.split()[3]
sh = Image.new('RGBA', (cut.width+120, cut.height+120), (0,0,0,0))
sh.paste((0,0,0,150), (60, 74), alpha)
sh = sh.filter(ImageFilter.GaussianBlur(26))
canvas.alpha_composite(sh, (cx_pos-60, cy_pos-60))
canvas.alpha_composite(cut, (cx_pos, cy_pos))
d = ImageDraw.Draw(canvas)

y = cy_pos + cut.height + 10

# ---- feature row (approved: 3 features w/ dividers) ----
feats = ["SLOW SIMMERED", "RICH IN FLAVOR", "CHEF'S SIGNATURE"]
seg = (W - 200) / 3
for i, ft in enumerate(feats):
    fx = 100 + seg*i + seg/2
    draw_tracked(d, y, ft, osw_feat, CREAM+(255,), tr=2, cx=fx)
    if i < 2:
        dx = 100 + seg*(i+1)
        d.line((dx, y-4, dx, y+26), fill=GOLD+(140,), width=1)

# ---- Halal badge (real asset from approved poster) ----
halal = Image.open('halal_badge_hires.png').convert('RGBA').resize((104,104), Image.LANCZOS)
canvas.alpha_composite(halal, (W-166, y-124))

# ---- ORDER NOW circular badge (approved element) ----
ob_r, obx, oby = 60, 118, y-72
d.ellipse((obx-ob_r, oby-ob_r, obx+ob_r, oby+ob_r), fill=(8,8,8,255), outline=GOLD+(255,), width=3)
d.text((obx - d.textlength("ORDER", font=osw_order)/2, oby-28), "ORDER", font=osw_order, fill=GOLD+(255,))
d.text((obx - d.textlength("NOW", font=osw_order_b)/2, oby-2), "NOW", font=osw_order_b, fill=(255,255,255,255))

# ---- GOLD footer band (approved style: gold band, dark text, icons) ----
fh = 118
fy0 = H - fh
foot = Image.new('RGBA', (W, fh), (0,0,0,0))
fd = ImageDraw.Draw(foot)
gcol = np.zeros((fh,3))
for i in range(fh):
    t = i/max(fh-1,1)
    gcol[i] = np.array([252,196,42])*(1-t) + np.array([228,164,12])*t
foot = Image.fromarray(np.tile(gcol[:,None,:], (1,W,1)).astype('uint8'), 'RGB').convert('RGBA')
canvas.alpha_composite(foot, (0, fy0))
d = ImageDraw.Draw(canvas)
d.line((0, fy0, W, fy0), fill=(10,10,10,255), width=3)

INK = (18,18,18,255)
isz = 26
ic_fb    = Image.open('ic_fb.png').convert('RGBA').resize((isz,isz), Image.LANCZOS)
ic_pin   = Image.open('ic_pin.png').convert('RGBA').resize((isz,isz), Image.LANCZOS)
ic_phone = Image.open('ic_phone.png').convert('RGBA').resize((34,34), Image.LANCZOS)
ic_globe = Image.open('ic_globe.png').convert('RGBA').resize((isz,isz), Image.LANCZOS)
ic_ig    = Image.open('ic_ig.png').convert('RGBA').resize((isz,isz), Image.LANCZOS)

r1, r2 = fy0+26, fy0+66
# left block
canvas.alpha_composite(ic_fb, (44, r1))
d.text((44+isz+10, r1+1), "RAJA RANI Indian Restaurant", font=osw_foot, fill=INK)
canvas.alpha_composite(ic_pin, (44, r2))
d.text((44+isz+10, r2+1), "45172 Ford Road Canton, MI 48187", font=osw_foot, fill=INK)
# centre phone
ph = "+1734-404-5523"
pw = d.textlength(ph, font=osw_footb)
canvas.alpha_composite(ic_phone, (int(W/2 - pw/2 - 46), fy0+42))
d.text((W/2 - pw/2, fy0+44), ph, font=osw_footb, fill=INK)
# right block
wsite = "www.rajaranimichigan.com"
soc   = "raja_rani_indian_restaurant"
ww = d.textlength(wsite, font=osw_foot); sw = d.textlength(soc, font=osw_foot)
canvas.alpha_composite(ic_globe, (int(W-44-ww-isz-10), r1))
d.text((W-44-ww, r1+1), wsite, font=osw_foot, fill=INK)
canvas.alpha_composite(ic_ig, (int(W-44-sw-isz-10), r2))
d.text((W-44-sw, r2+1), soc, font=osw_foot, fill=INK)

canvas.convert('RGB').save('raja_rani_butter_chicken.jpg', quality=95)
print('DONE  photo_bottom =', cy_pos+cut.height, ' feature_y =', y, ' footer_y =', fy0)
