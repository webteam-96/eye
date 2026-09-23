"""Partner logos for the strip on the Home page. The client's files arrive at mixed sizes, some with a flat matte
around the mark and two set in a solid box. Each is trimmed of its uniform border and centred on white at a common
size, so the strip reads as one row. Writes assets/img/logo-<slug>-{240,480}.png."""
import os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "originals", "client"), os.path.join(ROOT, "assets", "img")
BOX, PAD = (480, 240), 10          # 2x of the 240x120 the page paints

LOGOS = [
    ("canara-bank", "canara-bank.webp"),
    ("delhi-police", "delhi-police.webp"),
    ("hdfc-bank", "hdfc-bank.webp"),
    ("ge", "ge-general-electrical.webp"),
    ("uber", "uber.webp"),
    ("virgo", "vigro.webp"),
    ("nbcfdc", "nbcfdc.png"),
    ("mind-vriksha", "mind-vriksha.png"),
]

def trim(im, tol=14):
    """Drop a uniform border (the flat matte several of these files carry) when all four corners agree."""
    px = im.load()
    w, h = im.size
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    if max(max(abs(a - b) for a, b in zip(c, corners[0])) for c in corners) > tol:
        return im
    bg = corners[0]
    def row_is_bg(y): return all(max(abs(a - b) for a, b in zip(px[x, y], bg)) <= tol for x in range(0, w, 2))
    def col_is_bg(x): return all(max(abs(a - b) for a, b in zip(px[x, y], bg)) <= tol for y in range(0, h, 2))
    t = 0
    while t < h - 1 and row_is_bg(t): t += 1
    b = h - 1
    while b > t and row_is_bg(b): b -= 1
    l = 0
    while l < w - 1 and col_is_bg(l): l += 1
    r = w - 1
    while r > l and col_is_bg(r): r -= 1
    return im.crop((l, t, r + 1, b + 1))

for slug, src in LOGOS:
    im = Image.open(os.path.join(SRC, src))
    im = Image.alpha_composite(Image.new("RGBA", im.size, (255, 255, 255, 255)), im.convert("RGBA")).convert("RGB")
    im = trim(ImageOps.exif_transpose(im))
    inner = (BOX[0] - 2 * PAD, BOX[1] - 2 * PAD)
    s = min(inner[0] / im.width, inner[1] / im.height)
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    for w in (480, 240):
        canvas = Image.new("RGB", (w, round(BOX[1] * w / BOX[0])), "white")
        r = im.resize((max(1, round(im.width * w / BOX[0])), max(1, round(im.height * w / BOX[0]))), Image.LANCZOS)
        canvas.paste(r, ((canvas.width - r.width) // 2, (canvas.height - r.height) // 2))
        canvas.save(os.path.join(OUT, f"logo-{slug}-{w}.png"), optimize=True)
    print(f"logo-{slug}: trimmed to {im.size}")
