"""The 2026 award tile carries a three-photograph collage of the TEDx talk: the stage photograph, the speaker card
and the TEDxCVS title panel. Built at the tile's own 575x420 shape so it fills the tile with no letterboxing.
Writes assets/img/tedx-collage-{800,1200}.jpg."""
import os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "originals", "client"), os.path.join(ROOT, "assets", "img")
W, H, GAP, GROUND = 1200, 877, 10, (18, 12, 14)

def fill(path, box, focus=(0.5, 0.5), window=None):
    """Cover-crop `path` into box=(w, h). window=(top, bottom) first takes that vertical slice of the source."""
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    if window:
        im = im.crop((0, round(im.height * window[0]), im.width, round(im.height * window[1])))
    bw, bh = box
    s = max(bw / im.width, bh / im.height)
    im = im.resize((max(bw, round(im.width * s)), max(bh, round(im.height * s))), Image.LANCZOS)
    x = min(max(round(im.width * focus[0] - bw / 2), 0), im.width - bw)
    y = min(max(round(im.height * focus[1] - bh / 2), 0), im.height - bh)
    return im.crop((x, y, x + bw, y + bh))

sheet = Image.new("RGB", (W, H), GROUND)
left = round(W * 0.52)
right = W - left - GAP
top_h = round((H - GAP) * 0.56)

sheet.paste(fill(os.path.join(SRC, "ted-x-2.jpg"), (left, H), (0.5, 0.45)), (0, 0))
sheet.paste(fill(os.path.join(OUT, "tedx-stage-800.jpg"), (right, top_h), (0.42, 0.5)), (left + GAP, 0))
sheet.paste(fill(os.path.join(SRC, "ted-x.jpg"), (right, H - top_h - GAP), (0.5, 0.5), window=(0.0, 0.16)),
            (left + GAP, top_h + GAP))

for w in (800, 1200):
    r = sheet.resize((w, round(H * w / W)), Image.LANCZOS)
    r.save(os.path.join(OUT, f"tedx-collage-{w}.jpg"), "JPEG", quality=84, optimize=True, progressive=True)
    print(f"tedx-collage-{w}: {r.size}")
